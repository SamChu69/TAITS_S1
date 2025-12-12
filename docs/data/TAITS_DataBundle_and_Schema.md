# TAITS DataBundle and Schema

## 0. 文件定位與約束

本文件為 TAITS S2（Data Layer）核心規格，定義 TAITS 內部資料結構的「唯一事實來源（Single Source of Truth）」。

本文件遵循 TAITS 核心原則：

- 策略 ≠ 下單
- Agent ≠ 策略
- AI ≠ 唯一真理
- Regime 高於單一訊號
- Risk / Compliance 可否決一切
- 官方資料優先，多層 fallback
- 架構必須可長期演進、可擴充、不縮水

S2 範圍：只允許 `RESEARCH` 流程（不得接券商、不得下單）。

---

## 1. 名詞定義

- **RawPayload**：資料來源原始回應（未標準化）
- **NormalizedFrame**：標準化後的資料表（欄位與型別符合 TAITS Schema）
- **ValidationReport**：資料品質檢核結果（OK/WARN/BLOCK）
- **AuditRecord**：每次取數/處理/落盤之稽核記錄（可追溯）
- **DataBundle**：TAITS 對外（給 Orchestrator / Agents / Research）提供的統一資料包
- **Schema Version**：Schema 版本（Semantic Versioning）

---

## 2. 全域規範（Global Conventions）

### 2.1 時區與時間戳
- TAITS 內部時間統一使用 **Asia/Taipei（UTC+8）** 的時間語意。
- **ts 欄位一律為時間戳**（timestamp），不得使用字串作為主時間欄位。
- 對於資料落盤（parquet/jsonl），允許同時提供 `ts_iso`（ISO8601字串）作為輔助欄位，但 `ts` 仍為主鍵時間欄位。

### 2.2 頻率（Frequency）
統一使用下列字串：
- `1d`（日）
- `1m`（1 分）
- `5m`（5 分）
- `15m`（15 分）
- `30m`（30 分）
- `60m`（60 分）

不得使用 `D`, `min`, `T` 等外部框架縮寫作為對外頻率。

### 2.3 市場與商品代碼（Symbol）
TAITS 內部 symbol 建議採「可擴充」格式：

- 股票（TWSE/TPEX）：`TW:2330`、`TWO:8299`
- 期貨（TAIFEX）：`TAIFEX:TXF`（或更細：`TAIFEX:TXF202512`）
- 選擇權（TAIFEX）：`TAIFEX:TXO`（細節於 S3/S4 擴充）

> 註：此格式重點是可一眼辨識市場與商品類型，並可對應資料來源的代碼映射表（mapping）。

---

## 3. TAITS 標準資料表 Schema（NormalizedFrame）

### 3.1 OHLCV Bar Schema（最小可用）
此為 S2 的最小必備 Schema，後續任何來源都必須能輸出該格式（若來源缺欄位，需在 Normalizer 處理）。

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---:|---|
| ts | timestamp | 是 | K 棒起始時間（對齊 freq） |
| symbol | string | 是 | TAITS 內部代碼，如 `TW:2330` |
| open | float | 是 | 開盤價 |
| high | float | 是 | 最高價 |
| low | float | 是 | 最低價 |
| close | float | 是 | 收盤價 |
| volume | float/int | 是 | 成交量（股/口/單位依市場定義，但需一致） |
| turnover | float | 否 | 成交額（若來源有則提供） |
| vwap | float | 否 | 加權均價（若來源有則提供） |
| trades | int | 否 | 成交筆數（若來源有則提供） |
| source | string | 是 | 來源識別（TWSE/TAIFEX/FinMind/Yahoo…） |
| freq | string | 是 | `1d/1m/5m/...` |
| schema_version | string | 是 | 例如 `1.0.0` |

#### 3.1.1 Bar 對齊規則
- `1d`：以交易日為單位，`ts` 表示該交易日的日K起始（通常為當日 00:00:00 或依規範固定值；TAITS 建議使用當日 00:00:00（UTC+8）表達該日 Bar）。
- `1m/5m/...`：`ts` 必須是該分鐘 K 棒的起始時間，且需符合頻率整除（例如 5m 的分鐘必須為 00/05/10/...）。

---

## 4. DataBundle 規格（核心）

DataBundle 是 Orchestrator/Research/Agents 的標準輸入，不直接暴露各來源的混亂格式。

### 4.1 DataBundle 結構（JSON 概念）
```json
{
  "bundle_version": "1.0.0",
  "bundle_id": "uuid-or-hash",
  "mode": "RESEARCH",
  "asof_ts": "2025-12-13T04:06:00+08:00",
  "universe": ["TW:2330", "TW:0050"],
  "datasets": {
    "bars": {
      "freq": "1d",
      "frames": [
        {
          "symbol": "TW:2330",
          "schema_version": "1.0.0",
          "source": "FinMind",
          "data": "NormalizedFrame (table-like)"
        }
      ]
    }
  },
  "validation": {
    "status": "OK",
    "reports": [
      {
        "dataset": "bars",
        "symbol": "TW:2330",
        "status": "OK",
        "issues": [],
        "summary": {"rows": 500, "missing_rate": 0.0}
      }
    ]
  },
  "audit": {
    "records": [
      {
        "source": "FinMind",
        "request_ts": "2025-12-13T04:05:12+08:00",
        "response_ts": "2025-12-13T04:05:13+08:00",
        "params": {"symbol": "2330", "freq": "1d", "start": "2023-01-01", "end": "2025-12-13"},
        "status_code": 200,
        "rows": 500,
        "content_hash": "sha256:...",
        "cache_path": "data/cache/bars/FinMind/TW_2330/1d/2023-01-01_2025-12-13.parquet",
        "validator_status": "OK"
      }
    ]
  },
  "notes": []
}
````

### 4.2 DataBundle 必填欄位

* `bundle_version`
* `bundle_id`
* `mode`（S2 只能 `RESEARCH`）
* `asof_ts`
* `universe[]`
* `datasets{...}`（至少包含一個 dataset，例如 bars）
* `validation.status`
* `audit.records[]`

---

## 5. ValidationReport 規格（品質治理）

### 5.1 狀態枚舉

* `OK`：可用
* `WARN`：可用但需警示（下游可選擇降權/跳過）
* `BLOCK`：不可用（必須中止該 dataset 或該 symbol 的使用）

> 原則：Risk/Compliance 擁有最高否決權。
> 若 validator 或 compliance 決定 `BLOCK`，則 DataBundle 必須標記並向上回報。

### 5.2 Report Schema

| 欄位      | 型別     | 必填 | 說明                       |
| ------- | ------ | -: | ------------------------ |
| dataset | string |  是 | 如 `bars`                 |
| symbol  | string |  是 | 如 `TW:2330`              |
| status  | string |  是 | OK/WARN/BLOCK            |
| issues  | list   |  是 | 規則命中清單                   |
| summary | object |  是 | 統計摘要（rows、missing_rate…） |

### 5.3 Issue Schema

| 欄位       | 型別     | 必填 | 說明                    |
| -------- | ------ | -: | --------------------- |
| rule_id  | string |  是 | 例如 `BAR_MISSING_RATE` |
| severity | string |  是 | INFO/WARN/ERROR       |
| message  | string |  是 | 人類可讀訊息                |
| evidence | object |  否 | 例如異常點位、門檻值、樣本         |

---

## 6. AuditRecord 規格（稽核追溯）

AuditRecord 用於回答三個問題：

1. 資料從哪裡來？
2. 何時抓的？用什麼參數？
3. 是否落盤？是否通過品質檢核？

### 6.1 Record Schema（最小）

| 欄位               | 型別              | 必填 |
| ---------------- | --------------- | -: |
| source           | string          |  是 |
| request_ts       | string(ISO8601) |  是 |
| response_ts      | string(ISO8601) |  是 |
| params           | object          |  是 |
| status_code      | int             |  是 |
| rows             | int             |  是 |
| content_hash     | string          |  是 |
| cache_path       | string          |  否 |
| validator_status | string          |  是 |

---

## 7. Dataset 類型（S2 僅要求 bars，其他可擴充）

S2 最小必備：`bars`（OHLCV）。

後續可擴展（S3+）但不得破壞既有 schema：

* `fundamentals`（財務）
* `corporate_actions`（除權息/分割）
* `mops_events`（重大訊息）
* `news_sentiment`（新聞情緒）
* `macro`（宏觀）

擴展規則：

* 新 dataset 必須定義 `schema_version`
* 不得直接修改既有欄位語意（只能新增）
* 重大變更需提升 major version（見 8）

---

## 8. 版本治理（Schema Versioning）

使用語意化版本（SemVer）：`MAJOR.MINOR.PATCH`

* **PATCH**：修正文件文字、非破壞性修補
* **MINOR**：新增欄位（向後相容）
* **MAJOR**：破壞性更改（不相容），必須提供 Migration 說明

最低要求：

* 所有 NormalizedFrame 必須帶 `schema_version`
* DataBundle 必須帶 `bundle_version`

---

## 9. 落盤與重現性（Reproducibility）

S2 的核心價值是「可重現」：

* 同一組 `(source, symbol, freq, start, end)` 若來源不變，應盡可能命中 cache
* 每次抓取必須產生 `content_hash`（推薦 sha256）
* 任何下游分析若要可重現，必須能回溯：

  * 使用哪個 `cache_path`
  * 對應的 `content_hash`
  * 對應的 `validator_status`

---

## 10. S2 最小演示標準（Acceptance Test）

當執行：

* `python main.py research`

必須在 log / report 呈現：

* 至少 1 個 symbol（建議 `TW:2330`）
* 至少 1 個 dataset（`bars`）
* `validation.status` = OK/WARN（BLOCK 則需清楚原因）
* `audit.records` 至少 1 條，且包含 cache_path 或明確指出未落盤原因

---

## 11. 安全與合規提示（S2 仍必須遵守）

* S2 僅研究資料，不得觸發任何下單路徑。
* 若出現任何「可能接近交易執行」的功能需求，必須先由 Risk/Compliance 審核並具備硬閘門（hard gate）。
* 任何資料來源的使用需遵循來源之條款與限制；TAITS 優先官方，聚合/第三方僅作 fallback。

---

## 12. 變更紀錄

* 1.0.0：建立 TAITS S2 DataBundle 與 OHLCV Schema 最小規格，含 Validation/Audit/Versioning/Conventions。

```

