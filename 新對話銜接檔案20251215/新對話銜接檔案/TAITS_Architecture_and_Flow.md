# TAITS — 統一總架構與全流程（基於 V3.1 Spec）

> **系統名稱（對外）：** TAITS（台灣阿爾法智能交易系統）  
> **內部規格依據：** V3.1 Spec / TradingAgents Spec / 285 策略全集  
> **架構風格：** 五層架構 + 雙腦（Fast/Slow Brain）+ Lean 五模組 + 多智能體 + 熔斷

---

## 0. TAITS 全域總架構（總覽）

整體分層如下：

```text
Layer 0 ─ Infra Layer
Layer 1 ─ Data Layer
Layer 2 ─ Model Layer（Slow Brain + Fast Brain）
Layer 3 ─ Strategy Layer（Lean 5 Modules）
Layer 4 ─ Execution Layer（Modes + Circuit Breaker）
Layer 5 ─ UI / Monitoring Layer

      ↑
 Orchestrator / Scheduler 統一調度
```

---

## 🟥 Layer 0 — Infra Layer（基礎設施層）

這層讓 TAITS 從「一堆 Python 檔」變成「穩定的交易系統」。

### 元件與功能

- **TimescaleDB**  
  - 儲存：K 線、籌碼、新聞向量、Kronos 預測、策略信號  
  - 用途：回測、研究、統計分析  

- **Redis**  
  - 盤中快取：Tick、Fast Brain 預測、Slow Brain 結論、熔斷標記  
  - 提供毫秒級讀取，減少 DB 壓力  

- **EventBus（Async）**  
  - 將行情事件、預測事件、風控事件，分發給：  
    - Fast Brain  
    - 策略層  
    - Risk Manager / 熔斷機制  
    - UI 監控層  

- **Docker**  
  - 封裝整套 TAITS 運行環境，避免系統依賴衝突  

- **Logger + Audit Trail**  
  - 所有訊號、下單、熔斷事件皆記錄  
  - 便於日後稽核、除錯與策略回溯

> ✅ 這層讓 TAITS 從「程式集合」升級成「交易平台」。

---

## 🟦 Layer 1 — Data Layer（資料層）

融合 Spec 中的 FinMind / Cnyes / Yahoo / TWSE 等資料源，統一進入資料層。

### 資料來源與用途

| 資料來源         | 內容             | 用途                         |
|------------------|------------------|------------------------------|
| FinMind          | K 線、法人、融資券 | 技術指標、籌碼 Agent         |
| Cnyes（鉅亨）     | 新聞、事件、情緒   | News Agent、情緒分析         |
| TWSE / TPEX      | 公告、日成交、財報 | 基本面 / 財報 / 個股資訊     |
| Yahoo / 國際指數 | 匯率、美股、SOX 等 | Macro Agent（宏觀）         |
| WebSocket 行情   | Tick / 逐筆成交   | Fast Brain、Execution 使用   |

### 資料流程

```text
外部資料源
    ↓（API / 抓取）
清洗 / 對齊 / 缺值處理
    ↓
寫入 TimescaleDB（歷史資料庫）
    ↓
Redis 快取（盤中最新狀態）
```

> ✅ 這層是 TAITS 的「資料心臟」。

---

## 🟨 Layer 2 — Model Layer（雙腦架構：Slow Brain + Fast Brain）

這一層把「多智能體 TradingAgents」與「Kronos K 線預測」整合成 **雙腦系統**。

---

### 🧠 Slow Brain（慢軌，約每 1 分鐘）

- 實作：TradingAgents（Technical / Chip / Fundamental / News / Macro / Pattern / AI / Sector）  
- 任務：  
  - 看大盤趨勢  
  - 追蹤族群輪動  
  - 分析籌碼變化（外資 / 投信 / 自營）  
  - 判讀新聞與事件  
  - 給出「今天 / 這幾根 K」的大方向與理由  

#### Slow Brain 輸出範例

```json
{
  "slow_direction": "多",            // 多 / 空 / 盤整
  "slow_confidence": 0.82,
  "time_horizon": "短波段",
  "slow_reason": "外資連3買 + 電子權值領漲 + 新聞偏多"
}
```

---

### ⚡ Fast Brain（快軌，每 ~5 秒）

- 實作：Kronos K 線未來預測  
- 任務：  
  - 讀入最近 N 根 K（例如 60~240 根）  
  - 預測未來 5~10 根 K 的走勢  
  - 判斷目前是否為短線「擊球點」  

#### Fast Brain 輸出範例

```json
{
  "up_prob": 0.71,
  "down_prob": 0.16,
  "flat_prob": 0.13,
  "volatility": 0.24,
  "pattern_type": "箱體突破"
}
```

---

### 🔀 Signal Fusion（訊號融合器）

融合 Slow Brain（大方向）與 Fast Brain（短線位置），做出「這一檔、現在這個價位、該怎麼做」的結論。

#### 範例決策矩陣

| Slow Brain | Fast Brain | 行為                                   |
|------------|------------|----------------------------------------|
| 多         | 多         | 可積極做多（Full Size）               |
| 多         | 空         | 等回檔（Buy the Dip），掛好買點       |
| 空         | 多         | 不追，保留現金，或找避險               |
| 空         | 空         | 可考慮放空或減碼持股（若可融券）      |

#### 融合輸出（交給策略與資金配置）

```json
{
  "final_direction": "多",
  "entry_mode": "等回檔",
  "entry_hint": "靠近前一根低點附近佈局",
  "stop_loss": "ATR*2",
  "take_profit": "RR 2:1",
  "fusion_confidence": 0.78
}
```

> ✅ 此層為 TAITS 的核心智慧大腦。

---

## 🟩 Layer 3 — Strategy Layer（Lean 5 模組 × 285 策略）

在這一層，將 **285 策略 + 多智能體 + 雙腦輸出** 全部放進 **標準化 Lean 管線**。

---

### ① Universe Selection（選股池）

依據：

- 流動性條件（成交量、市值）  
- 族群與題材（電子、軍工、航運等）  
- 法人籌碼（外資、投信、自營）  
- 新聞強度（多空事件）  

輸出：

```python
universe = ["2330", "2603", "3035", "6531", ...]
```

---

### ② Alpha Model（策略整合器）

整合來源：

- 285 個策略信號（技術 / 籌碼 / 價值 / AI …）  
- Slow Brain 結論  
- Fast Brain（Kronos）預測  
- 市場 regime（趨勢 / 盤整 / 高波動）  

為每檔股票輸出：

```json
{
  "symbol": "2330",
  "alpha_signal": "BUY",        // BUY / HOLD / SELL
  "alpha_score": 0.81,
  "alpha_reason": "GMMA 多頭 + 投信連買 + Kronos 漲機率 0.7"
}
```

---

### ③ Portfolio Construction（部位配置）

考量：

- Alpha 分數  
- Slow/Fast Brain confidence  
- 波動（Fast Brain volatility）  
- 風險偏好（保守 / 中性 / 積極）  

計算：

- 每檔部位權重（%）  
- 總曝險上限  
- 單檔最大權重（例如 25%）  

輸出：

```json
{
  "symbol": "2330",
  "target_weight": 0.18   // 資金的 18%
}
```

---

### ④ Risk Management（風控 + 熔斷）

整合：

- 原 TAITS Risk Manager：  
  - 最大回撤  
  - 單筆虧損  
  - 單股曝險  

- 新增：**熔斷機制（Circuit Breaker）**  
  - 大盤急殺  
  - API 斷線 / 延遲  
  - 資料延遲（Data Lag）  
  - 回撤過大  
  - 單股異常波動（由 Fast Brain 通報）  

當熔斷觸發時：

```python
circuit_breaker.status = "ACTIVE"
# → 阻止所有新建部位，只允許減倉 / 平倉
```

> ✅ Risk Manager = 最終守門員。

---

### ⑤ Execution Model（下單執行）

基於富邦 API 的執行邏輯：

- ROD / IOC / FOK 支援  
- 自動調價（根據滑價限制）  
- 分批執行（模擬 TWAP / VWAP 行為）  
- 零股與整股整合下單  
- 斷線自動重試  

只有在：

- Universe 決定完成  
- Alpha 給出方向  
- Portfolio 計算完部位  
- Risk Manager & 熔斷皆通過  

的情況下，才會呼叫：

```python
fubon_api.place_order(...)
```

---

## 🟪 Layer 4 — Execution Layer（運行模式 + 熔斷總開關）

TAITS 的「運行模式」設計如下：

### 運行模式

- **Ignore**：只分析，不送單  
- **Backtest**：歷史資料回測（使用 Backtest Engine）  
- **Sandbox**：新策略 / 新 Agent 的隔離測試區  
- **Paper**：模擬交易（包含滑價、成交機率模型）  
- **Semi-Auto**：系統出訊號 → 你按「確認」才下單  
- **Auto**：全自動實盤（風控 & 熔斷通過才執行）  

### 熔斷總開關（系統級）

```python
if circuit_breaker.is_active():
    block_all_new_orders()
    only_allow_closing_positions()
```

> ✅ 確保在異常市場狀態下，TAITS 會自動進入防禦模式。

---

## 🟧 Layer 5 — UI / Monitoring Layer（前端監控）

核心畫面與功能：

### 市場總覽

- 大盤走勢  
- Slow Brain 判斷（多 / 空 / 盤整）  
- 國際指數與匯率概況  

### 個股詳情頁

- 現價 K 線  
- Kronos 預測未來 K 線（Fast Brain）  
- 各 Agent 評分（技術 / 籌碼 / 基本面 / 新聞 / 宏觀）  
- 285 策略中哪些策略亮燈  

### 交易控制面板

- 運行模式切換：Ignore / Backtest / Sandbox / Paper / Semi-Auto / Auto  
- 熔斷 & 風控燈號（API 狀態、Data Lag、Drawdown、Volatility）  

### 持倉與損益

- 持倉列表  
- 即時損益（PnL）  
- 風險指標（曝險、集中度、最大回撤追蹤）

---

## 🌀 TAITS 一天的完整流程（Pre / In / Post）

### 🟦 開盤前（Pre-Market）

1. 更新所有資料（FinMind / Cnyes / TWSE / Yahoo）。  
2. 更新指標 / 族群熱度。  
3. 執行 Slow Brain，產生日內偏多 / 偏空 / 盤整判斷。  
4. 建立當日 Universe（納入族群輪動、籌碼條件）。  
5. 執行 Kronos 初始預測（預估開盤後一小時結構）。  

> 輸出：**今日方向評估 + 當日監控標的池**

---

### 🟩 盤中（In-Market）

#### 慢軌（每 1 分鐘：Slow Brain）

- 更新法人籌碼（外資 / 投信 / 自營）。  
- 更新新聞與事件（Cnyes）。  
- 檢查大盤 regime 變化（趨勢 / 盤整 / 高波動）。  
- 更新族群輪動情況。  
- Slow Brain 更新市場方向與信心。

#### 快軌（每 5 秒：Fast Brain）

- 讀取最新 K 線窗格（如 60 根）。  
- 預測未來 5~10 根 K 線走勢。  
- 偵測短線反轉點與異常波動。

#### 訊號融合與部位建議

- Signal Fusion：Slow + Fast → Entry / Exit / Position Size。  
- Strategy & Portfolio：  
  - 若訊號有效且通過風控 → 產生具體部位調整建議。  

#### 風控與熔斷

- Risk Manager 檢查：曝險 / 單筆風險 / 回撤。  
- 熔斷條件檢查：大盤急殺、API 延遲、資料延遲等。  
- 若熔斷觸發 → 所有模式強制退到「Ignore / 只許平倉」。

#### 執行

- 根據當前運行模式：Paper / Semi-Auto / Auto。  
- Semi-Auto 下，由你確認後才送單。

---

### 🟥 收盤後（Post-Market）

1. 寫入當日所有 Log & Trade 到資料庫與檔案。  
2. 更新 Kronos 訓練資料庫（新增今日 K 線與結果）。  
3. 對今日策略變動進行回測或事後分析。  
4. 產生日報（以 Slow Brain 邏輯撰寫的 AI 日評）。  
5. 更新明日預備 Universe / 監控清單。  

---

## ✅ 最終總結（一次整合結果）

目前的 **TAITS**：

- ✅ 完全保留原 Spec 精神（多指標、多策略、多智能體）。  
- ✅ 完整融合五層架構（Infra → Data → Model → Strategy → Execution → UI）。  
- ✅ 完整具備 Fast/Slow Brain 雙軌（台股分析師視角 + AI 技術預測）。  
- ✅ 完整導入 Lean 五模組（Universe / Alpha / Portfolio / Risk / Execution）。  
- ✅ 支援多種交易模式（Ignore / Backtest / Sandbox / Paper / Semi-Auto / Auto），並內建熔斷機制。  
- ✅ 支援 Pre / In / Post 全生命週期流程。  

這份文件可作為：

- `docs/TAITS_Architecture_and_Flow.md`  
- 或專案主要 README 的核心架構章節。
---

# 【TAITS 架構與流程差異補齊（D01–D12）｜流程級落點】
## 版本：v2025-12-16
## 性質：Only-Add（追加，不覆蓋既有內容）

本章節將 D01–D12 的新增能力，**逐一掛載到既有流程**，明確標示：
- 位於第幾層（L1–L10）
- 做什麼
- 輸入 / 處理 / 輸出
- 下游影響與驗收點

---

## 全流程總覽（新增節點已標註）
L1 資料接入  
→ L2 正規化  
→ **L3 快照封存（D07 強制）**  
→ L4 特徵工廠（含 Wyckoff / 鮑迪克 / Observe-only / 題材）  
→ **L5 證據包中樞（D01）**  
→ **L6 Regime-first（D08）**  
→ **L7 Risk / Compliance（D09）**  
→ **L8 Strategy / Universe（三池）（D10）**  
→ **L9 Governance Gate（D11）**  
→ **L10 UI / Report（D12）**

---

## L1 → L2：資料接入到正規化（補齊官方來源與 Observe-only）
### 新增落點（D04 / D05 / D06）
**輸入**
- 官方 OpenAPI（TWSE / TPEx / TAIFEX / MOPS）
- 新聞/社群/題材資料
- 期貨/選擇權/融資融券（Observe-only）

**處理**
- 來源白名單驗證
- 欄位對齊（市場/新聞/衍生品/信用）
- 標的對齊（股票代碼唯一化）

**輸出**
- normalized_market_data
- normalized_news_data
- normalized_derivatives_data（Observe-only）
- normalized_credit_data（Observe-only）
- source_ref + captured_at + batch_id

**驗收**
- 任一資料可回查官方端點
- Observe-only 資料缺失需顯示（不可消失）

---

## L2 → L3：正規化到快照（D07 強制）
### 新增落點
**輸入**
- L2 全部 normalized 資料

**處理**
- 封存為不可變快照
- 產生 snapshot_ref 與 manifest

**輸出**
- snapshot_ref
- snapshot_manifest（來源/時間/缺失欄位）

**驗收**
- 任一決策皆能指定 snapshot_ref
- 歷史快照可回放

---

## L3 → L4：快照到特徵（補齊方法論與題材）
### 新增落點（D02 / D03 / D04 / D05）
**輸入**
- snapshot_ref

**處理**
- 技術特徵（趨勢/動能/波動/量能）
- Wyckoff 特徵（階段/事件/量價）
- 鮑迪克特徵（段落/背離/一致性/共振）
- Observe-only 旗標（期貨/選擇權/信用）
- 題材特徵（事件/敘事/熱度/擴散鏈）

**輸出**
- feature_vector
- feature_manifest（含缺失）

**驗收**
- 任一特徵能追溯 snapshot_ref
- 方法論特徵必有中文說明欄位

---

## L4 → L5：特徵到證據包（D01）
### 新增落點（核心）
**輸入**
- feature_vector + manifest

**處理**
- 規則觸發整理
- 證據彙總與風險標籤

**輸出（Evidence Bundle）**
- snapshot_ref
- trigger_rules[]
- technical_summary
- event_flags[]
- narrative_evidence[]
- heat_score
- rumor_risk_tags[]
- wyckoff_bundle
- bodick_bundle
- cross_market_flags
- cross_market_risk_tags[]

**驗收**
- 任一結論必附完整 Evidence Bundle
- 缺失需顯示缺失原因

---

## L5 → L6：證據包到 Regime-first（D08）
### 新增落點
**輸入**
- Evidence Bundle

**處理**
- 依證據權重判定市場狀態

**輸出**
- regime_state
- regime_confidence
- regime_snapshot_ref
- regime_evidence_refs[]

**驗收**
- Regime 變化可回溯證據
- 無證據不允許定調

---

## L6 → L7：Regime 到 Risk / Compliance（D09）
### 新增落點
**輸入**
- Regime + Evidence Bundle

**處理**
- 風控規則比對
- Observe-only 風險覆蓋（禁止追價/降權）

**輸出（Risk Audit Bundle）**
- risk_trigger_rules[]
- risk_snapshot_ref
- risk_evidence_refs[]
- blocked_actions[]
- weight_adjustments
- exit_priority_changes

**驗收**
- 任一否決可點開審計包

---

## L7 → L8：風控到策略與 Universe（三池）（D10）
### 新增落點
**輸入**
- Risk Audit Bundle
- Evidence Bundle

**處理**
- Universe 三池標記
- 策略允許/禁止/降權

**輸出**
- allowed_strategy_set
- weights
- priorities
- forced_exit_conditions

**驗收**
- 爆發池不得被直接刪除
- 僅能降權或標註風險

---

## L8 → L9：策略到治理 Gate（D11）
### 新增落點
**輸入**
- 策略決策
- Risk/Regime

**處理**
- 權限與授權檢查（Append/Modify/Refactor）

**輸出**
- permission_state
- gate_reason
- gate_snapshot_ref

**驗收**
- 無授權不可改
- 決策可審計

---

## L9 → L10：治理到 UI / Report（D12）
### 新增落點
**輸入**
- Evidence Bundle
- Regime / Risk / Gate

**處理**
- 可讀化呈現

**輸出**
- UI 面板（全證據）
- 報告（含 snapshot_ref）

**驗收**
- 點任何建議都能看到「為什麼」

---

# 【End of Architecture_and_Flow 差異補齊】

