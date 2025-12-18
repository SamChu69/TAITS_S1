# TAITS_全系統架構總覽（FULL_ARCH）__251219
doc_key：FULL_ARCH  
治理等級：B（System Architecture Overview｜承接 MASTER_CANON / ARCH_FLOW）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（架構層總覽，可隨系統擴充 Only-Add）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
變更原則：Only-Add（只可新增，不可刪減/覆寫/偷換定位）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX（Index 裁決）  
平行參照：ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DEPLOY_OPS / DATA_SOURCES  

---

## 0. 文件定位（Architecture Overview）

本文件為 TAITS 全系統架構總覽圖譜（System Architecture Map），其目的在於：

- 以 **模組化視角** 描述 TAITS 的整體系統構成  
- 說清楚 **每一層在系統中的角色與邊界**  
- 作為 **工程實作、Agent 佈署、資料流設計、UI 組裝** 的共同語言  

📌 本文件：

- 不定義 Canonical 流程順序（由 MASTER_CANON / ARCH_FLOW 定義）  
- 不定義制度鐵律（由 MASTER_ARCH 定義）  
- 專注於「系統由哪些部分構成、如何彼此連結」  

📌 治理對齊（A+ 約束，不可變更文件定位）  
- 本文件是「地圖」不是「流程細則」、不是「風控條文」、不是「下單規範」。  
- 若後續新增章節涉及治理/風控/執行細節，必須以「映射、邊界、引用」形式呈現，不得越權取代平行文件。

---

## 1. TAITS 系統總體分層（System Layering）

TAITS 採用 **橫向模組 × 縱向層級** 的雙維度架構：

### 1.1 縱向（流程層）
- **L1–L11 Canonical Flow（不可跳步）**  
- 各層的「責任/輸入/輸出/邊界」可在 ARCH_FLOW 找到更細化定義  
- 本文件僅保留「層級角色與模組歸屬」

### 1.2 橫向（系統模組）
- Data Layer（資料層）
- Analysis Layer（分析層）
- Decision Layer（決策層）
- Governance Layer（治理層）
- Execution Layer（執行層）
- Interface Layer（介面層）
- Infrastructure Layer（基礎設施層）

👉 任何模組必須同時歸屬：
- 一個「橫向模組（Layer Domain）」  
- 一個「縱向層級（L1–L11）」  

---

## 2. 核心系統模組總覽（Modules Overview）

> 說明格式：角色定位／包含模組／對應層級／關鍵原則／（必要時）禁止事項

---

### 2.1 Data Layer（資料層）

**角色定位**
- 系統的「感知器官」
- 所有決策的起點

**包含模組**
- DataSources Adapter（資料來源適配器）
- Data Collector（資料擷取器）
- Data Validator（資料驗證器）
- Data Normalizer（資料正規化器）

**對應層級**
- L1 / L2

**關鍵原則**
- 官方資料優先  
- 多層 fallback  
- 原始資料必須可追溯（Provenance 必留痕）  

---

### 2.2 Snapshot & State Layer（狀態層）

**角色定位**
- 系統的「即時狀態描述」
- 提供一致的市場快照、狀態緩存與可回放性基礎

**包含模組**
- Market Snapshot Builder（市場快照建構器）
- State Cache（狀態快取）
- Replay / Audit Engine（回放／稽核引擎：此處為狀態層的「快照回放能力」，非取代 VERSION_AUDIT 的全域版本稽核）

**對應層級**
- L3

**關鍵原則**
- Snapshot 必須可回放  
- 不得只存在於記憶體（必須可落盤、可追溯）

---

### 2.3 Analysis Layer（分析層）

**角色定位**
- 將資料轉為可解釋特徵（Feature / Indicator / Statistic / Structure）
- 提供後續證據層可用的「描述性輸出」

**包含模組**
- Feature Engine（特徵引擎）
- Indicator Engine（指標引擎）
- Statistical Engine（統計引擎）
- Structure Analysis（結構分析：含纏論結構、趨勢/區間結構、波動結構等「描述性」分析）

**對應層級**
- L4

**禁止事項**
- 不得產生交易方向（買/賣/加碼/減碼）  
- 不得跳過證據層直接形成策略結論  

---

### 2.4 Evidence & Regime Layer（證據與狀態層）

**角色定位**
- 系統的「判斷基礎」
- 將多來源、多特徵組裝成可審計的證據束（Evidence Bundle）
- 產出 Market Regime（市場狀態）作為策略啟用前置條件

**包含模組**
- Evidence Bundle Assembler（證據束組裝器）
- Evidence Conflict Resolver（證據衝突解決器：僅做一致性/衝突標註，不做交易裁決）
- Market Regime Engine（市場狀態引擎：Regime）

**對應層級**
- L5 / L6

**關鍵原則**
- 多證據、非單訊號  
- Regime 為策略啟用前置條件（Regime > Signal）

---

### 2.5 Risk & Compliance Layer（風控與合規層）

**角色定位**
- 系統的「煞車系統」
- 在任何執行意圖落地前提供「最高否決權」

**包含模組**
- Risk Exposure Analyzer（風險曝險分析器）
- Liquidity Checker（流動性檢查器）
- Compliance Rules Engine（合規規則引擎）

**對應層級**
- L7

**權限**
- 最高否決權  
- 可跨層中止流程  

---

### 2.6 Strategy & Research Layer（策略與研究層）

**角色定位**
- 產生「假設與建議」
- 管理策略宇宙、標的池、研究/回測/模擬等

**包含模組**
- Strategy Library（策略庫）
- Universe Selector（標的池／Universe 選擇器）
- Backtest / Simulation Engine（回測／模擬引擎）

**對應層級**
- L8

**限制**
- 永遠不直連下單  
- 僅輸出條件與情境（Scenario/Condition），不輸出執行指令  

---

### 2.7 Governance Layer（治理層）

**角色定位**
- 系統的「流程守門員」
- 驗證流程完整性、證據完整性、治理門檻是否達標

**包含模組**
- Flow Validator（流程驗證器）
- Evidence Completeness Checker（證據完整性檢查器）
- Governance Gate（治理闸門：不通過即退回）

**對應層級**
- L9

**關鍵原則**
- 不通過即退回  
- 不存在例外捷徑  

---

### 2.8 Interface Layer（介面層）

**角色定位**
- 人與系統的唯一交界面（Human-in-the-Loop 唯一入口）
- 以可解釋、可追溯方式呈現證據、Regime、風險與否決原因

**包含模組**
- Visualization Engine（視覺化引擎）
- Explainability Engine（可解釋性引擎）
- Decision Support UI（決策支援 UI）

**對應層級**
- L10

**關鍵原則**
- 可解釋性優先  
- 風險揭露優先於績效  

---

### 2.9 Execution & Control Layer（執行與控制層）

**角色定位**
- 合規前提下的執行單元（嚴格依核准意圖執行）
- 具備即時監控、急停（Kill Switch）、熔斷（Circuit Breaker）

**包含模組**
- Order Executor（下單執行器）
- Real-time Monitor（即時監控器）
- Kill Switch / Circuit Breaker（急停／熔斷）

**對應層級**
- L11

**關鍵原則**
- 完整記錄  
- 可即時中止  

---

### 2.10 Infrastructure Layer（基礎設施層）

**角色定位**
- 支撐整個系統的底層能力（儲存、訊息、日誌、版本、稽核）

**包含模組**
- Storage / Database（儲存／資料庫）
- Message Queue（訊息佇列）
- Logging & Audit（記錄與稽核）
- Version Control（版本控管）

**對應層級**
- 橫跨 L1–L11（但不得越權改寫業務邏輯）

---

## 3. Agent 於系統架構中的定位

### 3.1 Agent 的本質
- Agent 是 **模組的操作單位**
- 不是策略  
- 不是流程本身  

### 3.2 Agent 行為約束（架構視角）
每個 Agent：
- 必須綁定所屬模組  
- 必須標註所屬層級（L1–L11）  

Agent 不得：
- 跨層產出（例如：L4 Agent 直接產生 L11 執行意圖）  
- 私下串聯形成隱性策略（Shadow Strategy）  

---

## 4. 模組間資料流（High-Level Data Flow）

> 本節是「高階資料流地圖」，非 Canonical 流程細則；細則以 MASTER_CANON / ARCH_FLOW 為準。

Data Layer  
↓  
Snapshot / State  
↓  
Analysis  
↓  
Evidence & Regime  
↓  
Risk & Compliance ──┐  
↓                │（否決可中斷）  
Strategy & Research │  
↓                │  
Governance Gate ◀───┘  
↓  
UI / Human Decision  
↓  
Execution & Control  

---

## 5. 與其他核心文件的關係

### 5.1 受制於（上位裁決）
- MASTER_ARCH（最高鐵律）
- MASTER_CANON（流程順序）
- ARCH_FLOW（流程細化）

### 5.2 被引用於（下游引用）
- UI_SPEC
- Deployment_and_Operation
- Risk_and_Compliance

---

## 6. 演進與擴充原則（Only-Add）

- 可新增模組  
- 可拆分子模組  
- 不可破壞既有層級與否決鏈  

---

# 7. 【補回】系統層級與模組總覽（L1–L11）— 必須存在（不可刪減）

| Layer | 模組 | 權限 |
|---|---|---|
| L1 | Data Source | 僅收集 |
| L2 | Data Normalization | 僅清洗 |
| L3 | Snapshot & State | 僅快照/狀態 |
| L4 | Analysis Layer | 僅特徵/描述 |
| L5 | Evidence Builder | 僅證據組裝 |
| L6 | Regime Engine | 狀態裁定 |
| L7 | Risk & Compliance | 最高否決 |
| L8 | Strategy & Research | 假設/建議 |
| L9 | Governance Gate | 流程守門 |
| L10 | Decision Interface | 人類裁決 |
| L11 | Execution & Control | 嚴格執行 |

> 註：本表是 FULL_ARCH 的「地圖圖例（Legend）」。  
> 詳細責任/輸入/輸出/審計欄位：由 ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / VERSION_AUDIT 各自管轄。

---

# 8. 橫向模組 × 縱向層級 映射矩陣（Architecture Map Matrix）

> 任何模組必須落在「一個橫向域」與「一個縱向層」。  
> Infrastructure 可跨層，但不得越權改寫業務邏輯。

| 橫向域＼縱向層 | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 | L11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Data Layer | ● | ● |  |  |  |  |  |  |  |  |  |
| Snapshot & State |  |  | ● |  |  |  |  |  |  |  |  |
| Analysis Layer |  |  |  | ● |  |  |  |  |  |  |  |
| Evidence & Regime |  |  |  |  | ● | ● |  |  |  |  |  |
| Risk & Compliance |  |  |  |  |  |  | ● |  |  |  |  |
| Strategy & Research |  |  |  |  |  |  |  | ● |  |  |  |
| Governance Layer |  |  |  |  |  |  |  |  | ● |  |  |
| Interface Layer |  |  |  |  |  |  |  |  |  | ● |  |
| Execution Layer |  |  |  |  |  |  |  |  |  |  | ● |
| Infrastructure Layer | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |

---

# 9. FULL_ARCH 高階流程圖（Mermaid｜可直接放入 md，GitHub 原生渲染）

> 注意：此處是「高階流程地圖」  
> 不是 MASTER_CANON 的 Canonical 細則，也不取代 ARCH_FLOW 的細化步驟。

```mermaid
flowchart TB
  A[Data Layer<br/>資料層 (L1-L2)] --> B[Snapshot & State<br/>狀態層 (L3)]
  B --> C[Analysis Layer<br/>分析層 (L4)]
  C --> D[Evidence Builder<br/>證據層 (L5)]
  D --> E[Regime Engine<br/>市場狀態 (L6)]
  E --> F[Risk & Compliance<br/>最高否決 (L7)]
  F -->|PASS| G[Strategy & Research<br/>假設/建議 (L8)]
  F -->|VETO| X[STOP / BLOCK<br/>否決中止]

  G --> H[Governance Gate<br/>流程守門 (L9)]
  H --> I[Decision Interface<br/>人類裁決 (L10)]
  I -->|APPROVE| J[Execution & Control<br/>嚴格執行 (L11)]
  I -->|REJECT| X

  J --> K[Audit / Replay / Versioning<br/>稽核回放與版本 (Infrastructure)]
  A --> K
  B --> K
  C --> K
  D --> K
  E --> K
  F --> K
  G --> K
  H --> K
  I --> K
10. Agent 定位映射（Agent-to-Module Binding）
本節只做「定位與約束映射」，不描述 Agent 的策略細節（避免越權）。

Agent 類型	必綁模組域	必標層級	允許輸出	禁止輸出
Data Agent	Data Layer	L1–L2	原始/正規化資料	判斷/方向
Snapshot Agent	Snapshot & State	L3	Snapshot/State	策略指令
Analysis Agent	Analysis Layer	L4	Feature/Structure	買賣信號
Evidence Agent	Evidence	L5	Evidence Bundle	下單意圖
Regime Agent	Regime	L6	Regime State	直接交易
Risk Agent	Risk & Compliance	L7	PASS/VETO 理由碼	放行辯護
Research Agent	Strategy & Research	L8	假設/建議/情境	直連下單
Governance Agent	Governance	L9	完整性檢核結果	例外捷徑
UI Agent	Interface	L10	解釋/可視化	隱性自動化
Execution Agent	Execution	L11	嚴格執行紀錄	自主判斷

11. 本文件的「邊界聲明」（避免再次錯位）
FULL_ARCH 只負責：

模組地圖（Map）

模組歸屬（Domain/Layer）

高階資料流（High-Level Flow）

Agent 定位映射（Binding Map）

FULL_ARCH 不負責（不得越權）：

流程步驟與順序裁決：MASTER_CANON / ARCH_FLOW

最高鐵律條文：MASTER_ARCH

否決規則細節與理由碼全集：RISK_COMPLIANCE

下單、撤單、急停、風控前中後紀錄：EXECUTION_CONTROL

版本帳本與稽核可追溯細則：VERSION_AUDIT

12. 擴充規則（Only-Add）— 本文件專屬
允許新增：

新模組域（Domain）或子模組（Submodule）

新的映射矩陣列/欄（但不得改舊列/舊欄的語義）

新的高階流程圖（新增、並保留舊圖）

禁止：

刪除任何既有章節或表格

以「改寫定位」方式把 FULL_ARCH 變成治理條文/流程細則文件

把策略或 AI 變成 Execution 的直接來源（此為 MASTER_ARCH / RISK_COMPLIANCE 的硬禁止）

（FULL_ARCH 完）
