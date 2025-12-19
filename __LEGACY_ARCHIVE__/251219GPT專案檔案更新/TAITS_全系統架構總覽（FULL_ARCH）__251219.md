# TAITS_全系統架構總覽（FULL_ARCH）__251219
doc_key：FULL_ARCH  
治理等級：B（System Architecture Overview｜承接 MASTER_CANON / ARCH_FLOW）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（架構層總覽，可隨系統擴充 Only-Add）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_UNIVERSE / DEPLOY_OPS / LOCAL_ENV / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化邊界與否決鏈/偷換模組職責）  

---

## 0. 文件定位（System Architecture Map｜最大完備）

本文件為 **TAITS 全系統架構總覽圖譜（System Architecture Map）**，目的在於：

- 以「模組化視角」描述 TAITS 的整體系統構成
- 說清楚「每一模組的角色、邊界、輸入/輸出、通訊限制」
- 建立「橫向模組 × 縱向層級」的共同語言，供：
  - 工程實作
  - Agent 佈署（Agent 是操作單位，不是策略）
  - 資料流/事件流設計
  - UI 組裝與決策追溯
  - 稽核與回放

📌 本文件不做的事（避免越權）：
- 不定義 Canonical Flow 順序（由 MASTER_CANON / ARCH_FLOW 定義）
- 不定義制度鐵律（由 MASTER_ARCH 定義）
- 不定義否決條文全集（由 RISK_COMPLIANCE 定義）
- 不定義券商下單細節（由 EXECUTION_CONTROL 定義）

---

## 1. TAITS 架構總原則（Architecture Hard Principles）

### 1.1 雙維度架構（Cross-Dimension Architecture）
TAITS 採用：
- **縱向（流程層）**：L1–L11 Canonical Flow（不可跳步）
- **橫向（系統模組）**：Data / State / Analysis / Evidence / Regime / Risk&Compliance / Strategy&Research / Governance / UI / Execution&Control / Infrastructure

> ✅ 任何模組必須同時歸屬：
> - 一個「橫向模組域（Domain）」
> - 一個或多個「縱向層級（Layer: L1–L11）」  
> 且 **不得越權跨層產出**。

### 1.2 三條邊界鐵律（不可違反）
1) **策略 ≠ 下單**（Strategy 永遠不直連 Execution）  
2) **Agent ≠ 策略**（Agent 是操作單位，不能暗自串出隱性策略鏈）  
3) **AI ≠ 唯一真理**（AI 只能輔助，不得升格為裁決主體；裁決主體為人類 + 風控合規否決權）

### 1.3 否決鏈（Veto Chain）不可破壞
- Risk/Compliance 可跨層否決
- Governance Gate 可退回補齊
- UI 必須可視化否決與原因碼
- Execution 必須驗證 Risk PASS Token（否則阻斷）

---

## 2. 全系統「橫向模組域」總覽（Domains Overview｜最大完備）

> 這裡列的是 **模組域（Domain）**，不是單一服務；每個 Domain 下可再拆子模組（Only-Add）。

### 2.1 Data Domain（資料域）
**角色定位**：系統感知器官（唯一資料入口與治理）  
**典型子模組**：
- DataSources Adapter（資料源適配器）
- Data Collector（收集器）
- Data Validator（驗證器）
- Data Normalizer（正規化器）
- Corporate Actions Processor（除權息/分割/合併處理）
- Calendar & Session Service（交易日曆/交易時段）

### 2.2 State & Snapshot Domain（狀態快照域）
**角色定位**：將「當下市場與系統狀態」固化為可回放快照  
**典型子模組**：
- Market Snapshot Builder
- State Cache（狀態快取）
- Snapshot Store（快照落盤）
- Replay Loader（回放載入）

### 2.3 Analysis Domain（分析域）
**角色定位**：資料 → 可解釋特徵（只描述，不產出方向）  
**典型子模組**：
- Feature Engine（特徵引擎）
- Indicator Engine（指標引擎）
- Statistical Engine（統計引擎）
- Structure Engine（結構/型態/纏論結構容器：作為結構描述，不是下單指令）

### 2.4 Evidence Domain（證據域）
**角色定位**：把多來源資訊組裝成可審計的 Evidence Bundle  
**典型子模組**：
- Evidence Bundle Assembler
- Provenance Mapper（來源追溯映射）
- Conflict Marker（衝突標記：不裁決，只標記）
- Evidence Completeness Scorer（完整度量）

### 2.5 Regime Domain（市場狀態域）
**角色定位**：裁定市場狀態（Regime）並產出可交易/不可交易約束  
**典型子模組**：
- Regime Engine
- Regime Policy Map（Regime→允許策略類型映射）
- Regime Change Log（狀態變化紀錄）

### 2.6 Risk & Compliance Domain（風控合規域）
**角色定位**：全系統最高否決 Gate（PASS/VETO）  
**典型子模組**：
- Risk Exposure Analyzer
- Liquidity & Slippage Checker
- Compliance Rules Engine（規則快照）
- Risk PASS Token Issuer/Verifier
- Veto Reason Code Mapper

### 2.7 Strategy & Research Domain（策略研究域）
**角色定位**：產生「假設、建議、情境」，永不直連下單  
**典型子模組**：
- Strategy Library（策略庫：白名單治理）
- Universe Selector（標的池）
- Backtest Engine（回測）
- Simulation Engine（模擬）
- Scenario Generator（情境器）

### 2.8 Governance Domain（治理域）
**角色定位**：流程守門（完整性檢查、退回補齊、禁止跳層）  
**典型子模組**：
- Flow Validator（跳層檢測）
- Evidence Completeness Gate（證據門檻）
- Policy/Version Consistency Gate（版本一致性）
- Governance Decision Recorder（治理審計）

### 2.9 UI & Explainability Domain（介面與可解釋域）
**角色定位**：人與系統唯一交界面（L10 人類裁決入口）  
**典型子模組**：
- Decision Workbench（決策工作台）
- Visualization Engine（視覺化）
- Explainability Engine（可解釋呈現）
- Replay Viewer（回放檢視）
- Trace Recorder（UI Trace）

### 2.10 Execution & Control Domain（執行控制域）
**角色定位**：在合規前提下執行；可即時中止；不可繞過 Gate  
**典型子模組**：
- Execution Orchestrator
- Intent Compiler
- Broker Adapter（券商介面）
- Order State Machine
- Idempotency / De-dup Guard
- Channel Health Monitor
- Circuit Breaker
- Kill Switch Controller
- Reconciliation Engine（對帳）

### 2.11 Infrastructure Domain（基礎設施域）
**角色定位**：支撐全系統的底層能力（不可變更審計/佈署/監控/儲存）  
**典型子模組**：
- Storage / Database（含不可變更儲存）
- Message Bus / Queue（事件匯流排）
- Logging / Metrics / Tracing
- Secrets & Key Management（敏感隔離）
- Version Ledger（版本帳本）
- Access Control（RBAC）

---

## 3. 橫向模組域 × L1–L11 對位表（Module × Layer Mapping）

> Canonical Flow 定義在 MASTER_CANON / ARCH_FLOW；此處做「架構對位」，確保不跳層、不越權。

| L層 | 層級名稱 | 主要 Domain | 核心輸入 | 核心輸出 | 禁止事項（摘要） |
|---|---|---|---|---|---|
| L1 | Data Source | Data | 官方/授權資料 | Raw Data | 非官方裁決制度 |
| L2 | Normalization | Data | Raw Data | Canonical Data | 偷換欄位語義 |
| L3 | Snapshot/State | State | Canonical Data | Snapshot/State | 只在記憶體存在 |
| L4 | Analysis | Analysis | Snapshot/State | Feature/Structure | 產生交易方向 |
| L5 | Evidence | Evidence | Feature + State | Evidence Bundle | 只留摘要不留追溯 |
| L6 | Regime | Regime | Evidence | Regime State | Regime 未定就放行 |
| L7 | Risk/Compliance | Risk&Compliance | Evidence/Regime/Account | PASS/VETO + Token | 以績效辯護 |
| L8 | Strategy/Research | Strategy&Research | PASS + Evidence/Regime | Proposal/Scenario | 直連下單 |
| L9 | Governance Gate | Governance | Proposal + Audit | PASS/RETURN | 允許例外捷徑 |
| L10 | Human Decision | UI | 全部上游輸出 | APPROVE/REJECT + Trace | 自動批准 |
| L11 | Execution/Control | Execution&Control | APPROVE + Token | Orders/Logs | 無Token送單 |

---

## 4. 核心資料流（High-Level Data Flow｜最大完備）

### 4.1 主幹資料流（不含退回）
```mermaid
flowchart TB
  D1[Data Domain<br/>L1-L2] --> S1[State/Snapshot<br/>L3]
  S1 --> A1[Analysis Domain<br/>L4]
  A1 --> E1[Evidence Domain<br/>L5]
  E1 --> R1[Regime Domain<br/>L6]
  R1 --> RC[Risk & Compliance<br/>L7]
  RC -->|PASS| SR[Strategy & Research<br/>L8]
  RC -->|VETO| STOP1[STOP]
  SR --> GOV[Governance Gate<br/>L9]
  GOV -->|PASS| UI[UI Human Decision<br/>L10]
  GOV -->|RETURN| A1
  UI -->|APPROVE| EXE[Execution & Control<br/>L11]
  UI -->|REJECT| STOP2[STOP]
4.2 否決鏈與阻斷（Veto/Block）
L7 VETO：流程立即 STOP（不得進入 L8+）

L9 RETURN：退回補齊（不得跳層）

L11 BLOCK：若 Token/通道/審計缺失，Execution 必須阻斷並回報 UI

5. 事件匯流排（Event Bus）與訊息契約（Message Contracts）
本節是「最大完備」的重要差異：把模組間通訊規格拉齊，避免黑箱串接與隱性策略。

5.1 事件類型（最小集合，可擴充）
DataIngested

DataNormalized

SnapshotCreated

FeaturesComputed

EvidenceAssembled

RegimeDetermined

RiskGateDecided（PASS/VETO）

StrategyProposed

GovernanceChecked（PASS/RETURN）

HumanDecisionRecorded（APPROVE/REJECT）

ExecutionIntentCreated

OrderSubmitted / OrderAcked / OrderFilled / OrderRejected

KillSwitchTriggered

CircuitBreakerTriggered

ReconciliationCompleted

ReplayBundleAssembled

5.2 訊息契約硬性欄位（每個事件都必須）
correlation_id

event_id

event_type

timestamp

producer_module

active_version_map_ref

input_refs[] / output_refs[]（可回放引用）

hash_manifest_ref（完整性）

6. Agent 在架構中的定位（Agent Positioning｜嚴格對齊）
6.1 Agent 的本質（不可混淆）
Agent 是「模組的操作單位」或「工作流編排器的一部分」

Agent 不是：

策略本體

下單權限

流程裁決者

6.2 Agent 必須綁定（Binding Requirements）
每個 Agent 必須宣告：

所屬 Domain（Data/Analysis/Risk/UI/…）

所屬 Layer（L1–L11）

可讀/可寫的 Artifact 類型

禁止存取範圍（例如不得觸碰 Execution API）

6.3 Agent 禁止事項（硬禁）
跨層產出（例如 L4 Agent 直接產生下單方向）

私下串聯形成隱性策略（例如繞過 Governance Gate）

以 AI 文本輸出冒充 PASS/VETO 或 APPROVE/REJECT

7. AI 在架構中的位置（AI Placement｜不得升格）
最大完備要求：清楚定義 AI 的「可用範圍」與「不可越權邊界」。

7.1 AI 可存在的形式（允許）
作為 Analysis/Evidence 的輔助（例如：摘要、分類、衝突標記建議）

作為 Strategy/Research 的輔助（提出假設與情境）

作為 UI Explainability 的輔助（把證據轉成可讀解釋）

7.2 AI 不得做的事（硬禁）
不得產生「風控放行」或「合規裁決」結果

不得替代人類裁決（APPROVE）

不得直接呼叫 Execution 下單

不得以「我判斷」作為系統真相

8. 儲存與不可變更稽核（Storage & Immutable Audit）
8.1 儲存分層（推薦最小集合）
Hot Store：即時快取（State Cache）

Warm Store：可查詢的歷史（Features/Evidence 索引）

Cold Store：不可變更審計物（WORM/Append-only）

Ledger Store：版本帳本（Version Ledger）

8.2 不可變更（Immutable）硬要求
Evidence / Risk Gate / UI Trace / Execution Logs / Replay Bundle：

必須 Append-only

必須可校驗 hash

禁止回填與覆寫（Only-Add）

9. 安全與權限邊界（Security & RBAC）
9.1 權限最小集合（對齊 UI_SPEC）
Viewer：只讀

Operator：操作回放/查詢，不可 APPROVE

Trader：可在 PASS 狀態 APPROVE

Admin：管理設定，但不可覆寫風控否決

9.2 敏感資訊隔離
金鑰/憑證不得進 Repo（對齊 LOCAL_ENV / DEPLOY_OPS）

任何會觸碰券商的憑證：

只能在 Execution Domain 的受控環境中使用

且必須可審計（誰用、何時用、用於何 correlation_id）

10. 部署拓樸（Deployment Topologies｜架構層總覽）
具體上線流程與 Runbook 由 DEPLOY_OPS 定義；此處提供架構層必須支援的拓樸型態（Only-Add）。

10.1 單機拓樸（Local / Research）
Data + Analysis + Evidence + Regime + Strategy + UI 在同機

Execution 可關閉或使用模擬通道

10.2 分層服務拓樸（Paper / Live）
Data/State/Analysis：可獨立擴展

Risk/Compliance：獨立服務（高可用）

Execution：獨立服務（最小權限、最嚴隔離）

UI：獨立前端（只讀多、決策少、全留 trace）

10.3 隔離原則（必須）
Execution 與 Secrets/Keys 需最高隔離

Risk Gate 與 Version Ledger 需高可靠與不可變更

---

11. Mermaid｜「橫向模組域」總覽圖（System Map）
mermaid
flowchart LR
  subgraph DATA[Data Domain]
    DS[DataSources Adapter]
    DC[Collector]
    DV[Validator]
    DN[Normalizer]
    CA[Corp Actions]
    CAL[Calendar/Session]
  end

  subgraph STATE[State & Snapshot]
    SS[Snapshot Builder]
    SC[State Cache]
    ST[Snapshot Store]
    RP[Replay Loader]
  end

  subgraph ANALYSIS[Analysis]
    FE[Feature Engine]
    IE[Indicator Engine]
    SE[Stat Engine]
    STX[Structure Engine]
  end

  subgraph EVID[Evidence]
    EB[Evidence Assembler]
    PM[Provenance Map]
    CM[Conflict Marker]
    EC[Completeness Scorer]
  end

  subgraph REG[Regime]
    RE[Regime Engine]
    RM[Regime Policy Map]
    RL[Regime Change Log]
  end

  subgraph RISK[Risk & Compliance]
    RA[Exposure Analyzer]
    LQ[Liquidity/Slippage]
    CR[Compliance Rules]
    TK[PASS Token]
    VC[Veto Codes]
  end

  subgraph STR[Strategy & Research]
    SL[Strategy Library]
    US[Universe Selector]
    BT[Backtest]
    SIM[Simulation]
    SG[Scenario]
  end

  subgraph GOV[Governance]
    FV[Flow Validator]
    VG[Version Gate]
    EG[Evidence Gate]
    GR[Governance Recorder]
  end

  subgraph UI[UI & Explainability]
    DW[Decision Workbench]
    VX[Visualization]
    EX[Explainability]
    TR[Trace Recorder]
    RV[Replay Viewer]
  end

  subgraph EXE[Execution & Control]
    OR[Orchestrator]
    IC[Intent Compiler]
    BA[Broker Adapter]
    SM[Order State Machine]
    ID[Idempotency Guard]
    CH[Channel Health]
    CB[Circuit Breaker]
    KS[Kill Switch]
    RC2[Reconciliation]
  end

  subgraph INFRA[Infrastructure]
    BUS[Event Bus]
    LOG[Logs/Metrics/Tracing]
    IMM[Immutable Store]
    LED[Version Ledger]
    IAM[RBAC/IAM]
    SEC[Secrets/KMS]
  end

  DATA --> STATE --> ANALYSIS --> EVID --> REG --> RISK --> STR --> GOV --> UI --> EXE
  INFRA --- DATA
  INFRA --- STATE
  INFRA --- ANALYSIS
  INFRA --- EVID
  INFRA --- REG
  INFRA --- RISK
  INFRA --- STR
  INFRA --- GOV
  INFRA --- UI
  INFRA --- EXE
12. Only-Add 演進規則（FULL_ARCH 專屬）
允許：

新增 Domain 子模組

拆分現有模組為多個更細子模組

新增事件類型與訊息欄位（不得刪舊欄位）

新增部署拓樸（例如 HA、跨區）

禁止：

合併或刪除 L1–L11 的層級對位

削弱 Risk/Compliance 否決鏈

讓 Strategy/Agent 直連 Execution

把 AI 升格為「架構裁決模組」或「取代人類裁決」

（FULL_ARCH｜最大完備版 · Part 1 完）
