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
