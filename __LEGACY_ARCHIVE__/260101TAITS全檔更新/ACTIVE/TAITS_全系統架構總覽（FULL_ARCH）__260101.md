# TAITS_全系統架構總覽（FULL_ARCH）__251219

doc_key：FULL_ARCH  
治理等級：B  
版本狀態：ACTIVE（單一正確版｜全量重排版｜保留原文附錄）  
版本日期：2026-01-01  
檔案日期碼：260101  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
變更原則：**不刪減原文**；錯誤口徑不在正文混留，改以「附錄：原文保留」承接（避免混讀）。  

---
## 0. SOVEREIGNTY｜人類最高決策者唯一主權（不可牴觸）

- TAITS 之唯一最高主權屬於：**人類最高決策者（產品負責人／架構裁決者）**。
- 任何文件治理等級（A+／A／B／C）、任何治理閘門（Gate）、任何 Agent、任何 AI 規則、任何流程條款，**不得與人類最高決策者之明確命令牴觸**。
- 系統之責任為：在不阻擋命令的前提下，提供風險揭露、合規告警、替代方案，並強制完成稽核留痕與可回放紀錄。

### 0.1 HFI｜人類最終命令（Human Final Instruction）格式（本版定錨）
> 本段為**可執行觸發機制**：用以避免「主權存在但實務被 Freeze/Only-Add 卡死」。

**Valid HFI 最低要件：**
- `hfi_id`：HFI-YYYYMMDD-###
- `authority_actor`：人類最高決策者識別
- `authority_time`：Asia/Taipei 時戳
- `scope`：doc_key / 章節路徑 / 全檔（明確指定）
- `action`：overwrite / rewrite / reformat / replace / publish_s1 / publish_s2（至少一項）
- `intent`：目的（例如：修正錯誤定位、全量重排版、統一 L9–L11 語義）
- `acknowledgement`：最終裁決確認（「我已閱讀風險揭露並確認執行」或等價語句）

### 0.2 HFI Override（放行原則）
當 Valid HFI 存在時：
- **Freeze / Only-Add / Gate 限制不得阻止** HFI `scope` 範圍內之更新、覆寫、重排版或全量替換。
- Risk/Compliance 必須輸出完整風險揭露與反對理由，但其結果不得升格為阻止人類命令之否決；以「強制揭露＋確認＋全紀錄」承接。


## 1. Canonical Flow（L1–L11）｜L9–L11 最終語義定錨（本版唯一裁決口徑）

### 1.1 L1–L8（資訊收集與篩選層）
- **L1–L8**定位為：資料與訊號之**收集、清洗、特徵化、策略候選生成、風險/合規前置約束、Regime/Context 判讀、資金配置草案與執行前檢查**。
- 其產出不直接構成下單；其定位為 L9/L10 的輸入（Inputs）。

### 1.2 L9（投資報告層）｜必須「可讀、可追蹤、可更新」
L9 不只是解說；其定位為「**可操作的投資報告**」，至少包含：
- **數據與圖形**（可視化、統計摘要、關鍵時間序列）
- **進出場價格建議與條件**（區間/觸發條件/風險情境）
- **交易標的化追蹤**（同一標的可跨事件/跨時間更新報告；需能追溯每次更新原因）
- **買與賣的全週期**：可長抱、提早出場、停損、停利、動態調整（市場隨事件與 Regime 變動而更新）

### 1.3 L10（人類裁決／交易決策層）｜下單唯一入口
- L10 是你（人類最高決策者）做最後裁決的層：**不動作／半自動／全自動／回測／模擬／實盤**的選擇皆在 L10。
- **下單屬於 L10**；AI/策略/報告都不得自動等同於下單。

### 1.4 L11（工程稽核回放層）｜全層紀錄（非下單）
- L11 定位為：**工程稽核、可回放、可追溯**的全層記錄（涵蓋 L1–L10）。
- L11 的紀錄必須同時滿足：
  - 你能看懂的「人話版」摘要與關鍵證據鏈
  - 工程能用的「機讀版」結構化紀錄（Hash/事件流/參數/版本/輸入輸出）
- L11 **不做下單**；其作用是檢視系統每一層是否合理、是否需要調整（含半自動/全自動交易流程的可稽核性）。


## 2. 稽核承接（Mandatory Audit Artifacts）

任何由 HFI 放行的更新/覆寫/重排版/全量替換，必須同步產生：
1. **VERSION_AUDIT｜HFI Ledger**（含 change_id、scope、影響清單、套用順序、責任確認）
2. **HASH_MANIFEST**（全檔 SHA256 指紋清單）
3. **CHANGELOG**（逐檔變更摘要：改了什麼、為何改、影響範圍）

> 稽核要求用於回放與追責，不構成對人類主權命令的否決。
---

## 99. 附錄｜原文全文保留（不刪減｜供追溯與對照）
> 說明：以下為 `TAITS_全系統架構總覽（FULL_ARCH）__251231.md` 之原文全文，為避免舊標示/舊備註干擾裁決，本版將「單一正確口徑」置於正文；原文作為歷史證據保留。

<!--
TAITS｜ACTIVE UPDATED（單檔內嵌更新版）
產出日期：2025-12-29（Asia/Taipei）
更新規格：單檔內嵌；可更新處直接更新並避免重複；不可更新處以 Appendix 內嵌 Only-Add 全文。
來源檔：TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md
-->

# TAITS_全系統架構總覽（FULL_ARCH）__251219
doc_key：FULL_ARCH  
治理等級：B（System Architecture Overview｜承接 MASTER_CANON / ARCH_FLOW）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（架構層總覽，可隨系統擴充 Only-Add）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES（alias: DATA_UNIVERSE） / DEPLOY_OPS / LOCAL_ENV / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化邊界與否決鏈/偷換模組職責）  

---

---

# Addendum 2025-12-27｜Only-Add：DATA_UNIVERSE（alias）封口 × FULL_ARCH 引用口徑回歸 DATA_SOURCES × source_id 欄位解讀限縮（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_全系統架構總覽（FULL_ARCH）__251219.md（doc_key：FULL_ARCH）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：Index Gate（DOCUMENT_INDEX）＋治理等級覆蓋（A+ > A > B > C）＋衝突裁決程序（DOCUMENT_INDEX §6）＋AI_GOV（A+）最高約束  
> 口徑對齊：  
> - DATA_SOURCES｜Addendum 0 / 0.1（DATA_UNIVERSE 僅為概念別名，不具 doc_key 法律效力）  
> - DOCUMENT_INDEX｜Addendum 2025-12-27（裁決順序字串統一 × 歧義消解）  
> - DOCUMENT_INDEX｜Addendum 2025-12-27-B（B+/C+ 子級標籤定義 × 覆蓋規則對位）〔檔名：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251227B_FINAL.md〕  
> - GOVERNANCE_GATE_SPEC｜Addendum 2025-12-27（字串助記定位 × 雙軌裁決消歧）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（建議新增條目：`VA-METADATA_FIX-20251227-0005`）  
> 目的：封住本文件中「DATA_UNIVERSE」被誤當成可引用治理文件（doc_key）的風險；將 FULL_ARCH 對資料來源治理的引用口徑固定回歸 `DATA_SOURCES`；並對正文中「source_id 需存在於 DATA_UNIVERSE」等語句做限縮解讀（Only-Add，不改原文），避免 Gate/Audit/新對話載入出現引用歧義。

---

## 0. 適用範圍（Hard Boundary）

本 Addendum 僅處理「引用端歧義」與「欄位語句限縮解讀」，不改寫 FULL_ARCH 的系統模組、分層、資料流、事件流、Canonical Flow 對位或任何架構規格內容。

- 不新增新 doc_key  
- 不改寫 Canonical Flow（L1–L11）  
- 不變更覆蓋規則（A+ > A > B > C）  
- 不覆寫原文中任何段落（僅限縮解讀）

---

## 1. DATA_UNIVERSE 的法律定位（Alias ≠ doc_key）

### 1.1 統一裁決：FULL_ARCH 內的 DATA_UNIVERSE 一律視為概念別名
本文件（含檔頭平行參照與正文段落）中出現之「DATA_UNIVERSE」：
- 一律視為「資料宇宙（Data Universe）」之概念名詞／閱讀別名（alias）  
- **不得**被解讀為治理文件 doc_key  
- **不得**被寫入任何引用欄位（doc_key / evidence_doc_key / audit_doc_key / ui_doc_key / gate_doc_key）

### 1.2 引用合法性硬規則（Gate-Friendly）
凡本文件需要引用「資料來源治理文件」時（Provenance / 來源證據 / 欄位合法性約束 / 資料取得責任界面）：
- 唯一合法 doc_key **必須**為：`DATA_SOURCES`  
- 若任何輸出（Evidence/Audit/UI Trace/資料字典）出現 `doc_key=DATA_UNIVERSE`：
  - 一律視為「引用非法」
  - 依 Gate 規則裁決為 BLOCK（不得以推測補救）

---

## 2. 對既有語句的限縮解讀（Only-Add，不改原文）

### 2.1 「source_id 需存在於 DATA_UNIVERSE」之唯一可採用解讀
本文件若出現類似語句（例：「`source_id` 需存在於 DATA_UNIVERSE」），在 Freeze v1.0 下的唯一合法解讀為：

- 「source_id 必須對應到 **DATA_SOURCES（資料來源全集）**所定義之來源識別集合（source registry / source list / evidence refs）」  
- 「DATA_UNIVERSE」僅表示「資料來源全集所涵蓋之宇宙範圍（Universe）」之概念指稱，不具 doc_key 法律效力

### 2.2 若文本同時出現「DATA_SOURCES」與「DATA_UNIVERSE」
一律採「doc_key 以 DATA_SOURCES 為準，DATA_UNIVERSE 為 alias」之解讀；若仍有歧義，回到 DOCUMENT_INDEX §6（衝突裁決程序）保守處置。

---

## 3. 最小合規引用模板（可直接貼用）

> 用途：當 FULL_ARCH 的某段資料字典/欄位約束需要在其他文件/稽核記錄/Issue/PR 中引用時，固定引用資訊，避免 Gate 命中「引用不完整」。

### 3.1 引用資料來源治理（DATA_SOURCES）
```text
ref_doc_key = DATA_SOURCES
ref_doc_name = TAITS_資料來源全集（DATA_SOURCES）__251219.md
ref_section = <例如：Addendum 0 / Addendum 0.1 / Part X / Appendix Y>
ref_notes = 本文件中「DATA_UNIVERSE」僅為 alias；doc_key 一律回歸 DATA_SOURCES
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0005
```

### 3.2 引用文件合法性/等級（DOCUMENT_INDEX）
```text
ref_doc_key = DOCUMENT_INDEX
ref_purpose = index_gate_and_override_rule
ref_section = <例如：§3 / §6 / §7 / §9 / Addendum 2025-12-27 / Addendum 2025-12-27-B>
```

---

## 4. 工具/AI 抽取與重組規則（不可跳過）

凡工具或 AI 進行「片段抽取、資料字典重組、欄位規格輸出」時，必須遵守：

- 抽取片段若含「DATA_UNIVERSE」字樣：  
  - **不得**提升為 doc_key  
  - 必須同時輸出 `ref_doc_key = DATA_SOURCES`（見 §3.1）  
- 缺少必要引用欄位（doc_key/section/audit_anchor）時：  
  - 僅允許列缺口，不允許裁決性輸出（PASS/VETO/RETURN/STOP）

---

## 5. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫任何既有正文。  
- 本文件中 DATA_UNIVERSE 一律為 alias；引用 doc_key 一律回歸 DATA_SOURCES。  
- 若未能取得必要引用資訊，依 DOCUMENT_INDEX §6 保守處置，並以 VERSION_AUDIT 留痕。

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）


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
```
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

11. Mermaid｜「橫向模組域」總覽圖（System Map）
mermaid
複製程式碼
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

# TAITS_全系統架構總覽（FULL_ARCH）__251219
## Part 2｜介面契約・Trace 範本・失效模式・一致性檢核（最大完備）

doc_key：FULL_ARCH  
治理等級：B（System Architecture Overview｜承接 MASTER_CANON / ARCH_FLOW）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（架構層總覽，可隨系統擴充 Only-Add）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES（alias: DATA_UNIVERSE） / DEPLOY_OPS / LOCAL_ENV / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化邊界與否決鏈/偷換模組職責）

---

## 13. 模組介面契約（Module Interface Contracts｜全域硬規格）

> 本節是 FULL_ARCH 的「最大完備核心」：  
> 任何模組在跨 Domain 溝通時，必須使用結構化契約（Contract），不得以自由文字、臨時欄位、私下串接形成黑箱。

### 13.1 Contract 的共同硬性欄位（所有跨模組輸入/輸出都必須）
- `correlation_id`：全鏈路關聯鍵（L1–L11 同一條）
- `session_id`：UI 會話鍵（有人類介入時必須）
- `layer_id`：L1–L11
- `domain`：Data/State/Analysis/Evidence/Regime/Risk/Strategy/Gov/UI/Exec/Infra
- `module_id`：產出模組
- `timestamp_utc`
- `active_version_map_ref`：版本映射引用（缺 = SYS-VERSION → 阻斷）
- `input_refs[]`：輸入引用（含 provenance）
- `output_refs[]`：輸出引用
- `hash_manifest_ref`：完整性校驗（缺 = SYS-HASH/SYS-AUDIT → 阻斷）
- `status`：SUCCESS / FAIL / RETURN / VETO / BLOCK
- `reason_codes[]`：非 SUCCESS 必填（不可空）

### 13.2 禁止事項（Contract 層硬禁）
- 禁止只傳「摘要」而不保留可追溯引用（provenance 斷裂）
- 禁止跨層回寫（例如 L11 寫回 L4 的「策略方向」）
- 禁止私下新增未版控欄位作裁決依據（必須走 Only-Add + VERSION_AUDIT）

---

## 14. 各 Domain 最小輸入/輸出契約（Minimum IO Contracts）

> 下列為「最小可落地」的 Contract 模板（可擴充不可縮減）。  
> Schema 以「欄位級」定義，工程實作可用 JSON/Proto/Parquet 等，但語義不得改。

---

### 14.1 Data Domain（L1–L2）契約

#### 14.1.1 `DataIngested`（L1）
**輸入**：官方/授權資料端點  
**輸出**：Raw Data Artifact + Provenance

必備欄位（除 13.1 通用欄位外）：
- `source_id`（資料源主鍵，需存在於 DATA_UNIVERSE）
- `source_type`（TWSE/TAIFEX/MOPS/TDCC/券商/第三方…）
- `fetch_window`（start/end）
- `raw_payload_ref`
- `provenance_ref`（官方網址/端點/回應頭/時間戳）

禁止：
- 以非官方裁決制度（若需要制度判定，必須引用 TWSE_RULES + 官方入口）
- 省略 provenance_ref

#### 14.1.2 `DataNormalized`（L2）
**輸入**：Raw Data  
**輸出**：Canonical Data（欄位標準化）

必備欄位：
- `canonical_schema_id`
- `normalization_ruleset_version`
- `field_map_ref`（原欄位→標準欄位）
- `quality_flags[]`（缺值、異常、延遲）

禁止：
- 偷換欄位語義（例如把成交量當成交額）
- 靜默修補（任何補值必須留痕）

---

### 14.2 State & Snapshot Domain（L3）契約

#### 14.2.1 `SnapshotCreated`（L3）
**輸入**：Canonical Data  
**輸出**：Snapshot（可回放）

必備欄位：
- `snapshot_id`
- `market_time`（交易所時間）
- `trading_session_state`（可交易/不可交易/盤後等）
- `snapshot_store_ref`（必須落盤，不得只在記憶體）
- `replay_loader_ref`（可載入入口）

禁止：
- 不落盤
- Snapshot 與 version map 不一致

---

### 14.3 Analysis Domain（L4）契約

#### 14.3.1 `FeaturesComputed`（L4）
**輸入**：Snapshot/State  
**輸出**：Feature Set + Structure Descriptors

必備欄位：
- `feature_set_id`
- `feature_schema_version`
- `indicator_set_ref`
- `structure_descriptor_ref`（若有纏論/型態結構，必須以「結構描述」形式輸出）
- `feature_quality_flags[]`

硬禁（非常重要）：
- 不得產生交易方向（不得輸出 BUY/SELL/target position）
- 不得繞過 Evidence 組裝（L5）

---

### 14.4 Evidence Domain（L5）契約

#### 14.4.1 `EvidenceAssembled`（L5）
**輸入**：Feature Set + State  
**輸出**：Evidence Bundle（可稽核）

必備欄位：
- `evidence_bundle_id`
- `evidence_items[]`（每一項含：來源 ref、時間戳、hash、類型）
- `provenance_map_ref`（來源追溯映射）
- `conflict_flags[]`（衝突標記，不裁決）
- `completeness_score`（完整度分數/等級）
- `completeness_missing_items[]`（缺口清單）

禁止：
- 只留摘要不留 item refs
- 以 AI 文本替代 evidence_items（AI 只能輔助描述，不能成為唯一證據）

---

### 14.5 Regime Domain（L6）契約

#### 14.5.1 `RegimeDetermined`（L6）
**輸入**：Evidence Bundle  
**輸出**：Regime State（適用性約束）

必備欄位：
- `regime_state_id`
- `regime_label`
- `regime_confidence`
- `allowed_strategy_classes[]`（允許策略類型）
- `blocked_strategy_classes[]`（禁入類型）
- `regime_change_log_ref`

禁止：
- Regime 不明確卻放行（應降級或觸發風控升級）

---

### 14.6 Risk & Compliance Domain（L7）契約

#### 14.6.1 `RiskGateDecided`（L7）
**輸入**：Evidence + Regime + Account + Rulebook Snapshot  
**輸出**：PASS/VETO（二元）+ Token（PASS 時）

必備欄位：
- `risk_decision_id`
- `risk_gate_decision`（PASS/VETO）
- `veto_reason_codes[]`（VETO 必填）
- `policy_version`
- `rulebook_snapshot_ref`（制度快照引用）
- `risk_pass_token_ref`（PASS 必填）
- `risk_evidence_snapshot_ref`（必填）

禁止：
- 用績效辯護
- 用模糊語句替代 VETO
- 缺 token 仍放行

---

### 14.7 Strategy & Research Domain（L8）契約

#### 14.7.1 `StrategyProposed`（L8）
**輸入**：Risk PASS + Evidence/Regime  
**輸出**：Proposal（假設/情境/限制）

必備欄位：
- `proposal_id`
- `strategy_ids[]`（白名單策略 ID；必須存在 STRATEGY_UNIVERSE）
- `scenario_ref`
- `assumptions_ref`
- `limitations_ref`
- `expected_behavior_ref`（行為描述，不得是下單指令）
- `proposal_confidence`（允許，但不得作裁決）

硬禁：
- 不得產生下單指令
- 不得把特徵直接等同方向（特徵≠方向）

---

### 14.8 Governance Domain（L9）契約

#### 14.8.1 `GovernanceChecked`（L9）
**輸入**：Proposal + 全鏈路審計引用  
**輸出**：PASS/RETURN

必備欄位：
- `governance_report_id`
- `governance_status`（PASS/RETURN）
- `missing_items[]`（RETURN 必填）
- `flow_integrity_checks_ref`
- `version_consistency_checks_ref`
- `evidence_completeness_checks_ref`

禁止：
- 允許例外捷徑
- RETURN 不提供缺口清單

---

### 14.9 UI Domain（L10）契約

#### 14.9.1 `HumanDecisionRecorded`（L10）
**輸入**：Risk PASS/VETO + Gov PASS/RETURN + Evidence/Regime/Proposal  
**輸出**：APPROVE/REJECT/ABORT + UI Trace

必備欄位：
- `human_decision_id`
- `human_decision`（APPROVE/REJECT/ABORT）
- `user_id`
- `ui_trace_ref`
- `decision_signature`
- `decision_reason_ref`（可選，但不得取代風控 reason codes）

禁止：
- 自動批准
- VETO/RETURN 狀態仍允許 APPROVE

---

### 14.10 Execution & Control Domain（L11）契約

#### 14.10.1 `ExecutionIntentCreated`（L11-Pre）
**輸入**：APPROVE + Risk Token  
**輸出**：Execution Intent Draft（尚未送券商）

必備欄位：
- `intent_id`
- `idempotency_key`
- `intent_hash`
- `risk_pass_token_ref`（再次驗證）
- `channel_health_snapshot_ref`
- `kill_switch_status`
- `pre_execution_log_ref`

#### 14.10.2 `OrderLifecycleEvents`（L11-In）
- `OrderSubmitted` / `OrderAcked` / `OrderFilled` / `OrderRejected` / `OrderCanceled`
必備欄位：
- `order_id`
- `broker_order_id`（若有）
- `state_transition_ref`
- `latency_metrics_ref`

#### 14.10.3 `ReconciliationCompleted`（L11-Post）
必備欄位：
- `reconciliation_report_id`
- `reconcile_status`（OK/NOT_OK）
- `post_trade_snapshot_ref`
- `post_execution_log_ref`
- `replay_bundle_ref`

禁止：
- 無 token 送單
- 無對帳繼續送新單
- 靜默重送/靜默改單

---

## 15. 端到端 Trace（E2E Trace）範本（可直接落地審計）

> 這裡提供「一筆交易/一次裁決」從 L1 到 L11 的最小可回放追溯清單。  
> TAITS 實作時，任何缺項都應被視為 SYS-AUDIT / SYS-VERSION 類阻斷。

### 15.1 E2E Trace Manifest（最小集合）
- `correlation_id`
- `active_version_map_ref`
- L1：`raw_payload_ref` + `provenance_ref`
- L2：`canonical_data_ref` + `field_map_ref`
- L3：`snapshot_store_ref`
- L4：`feature_set_ref` + `structure_descriptor_ref`
- L5：`evidence_bundle_ref` + `provenance_map_ref` + `completeness_score`
- L6：`regime_state_ref`
- L7：`risk_gate_decision_ref` + `policy_version` + `rulebook_snapshot_ref` + `risk_pass_token_ref(PASS)`
- L8：`strategy_proposal_ref`
- L9：`governance_report_ref`
- L10：`ui_trace_ref` + `human_decision_ref` + `decision_signature`
- L11：`pre_execution_log_ref` + `order_lifecycle_refs[]` + `post_execution_log_ref` + `reconciliation_report_ref` + `replay_bundle_ref`
- `hash_manifest_ref`（全鏈路 hash 清單）

### 15.2 Mermaid｜E2E Trace 骨架圖
```mermaid
```
flowchart TB
  L1[L1 DataIngested] --> L2[L2 DataNormalized]
  L2 --> L3[L3 SnapshotCreated]
  L3 --> L4[L4 FeaturesComputed]
  L4 --> L5[L5 EvidenceAssembled]
  L5 --> L6[L6 RegimeDetermined]
  L6 --> L7[L7 RiskGateDecided]
  L7 -->|PASS| L8[L8 StrategyProposed]
  L7 -->|VETO| STOP[STOP + Audit]
  L8 --> L9[L9 GovernanceChecked]
  L9 -->|RETURN| L5
  L9 -->|PASS| L10[L10 HumanDecisionRecorded]
  L10 -->|REJECT| STOP
  L10 -->|APPROVE| L11[L11 ExecutionIntentCreated + OrderLifecycle + Reconcile]
16. 失效模式（Failure Modes）與阻斷/退回策略（最大完備）
本節把「系統會怎麼壞」制度化：
每一個 Domain 必須能明確定義 FAIL/RETURN/VETO/BLOCK 的處置，避免黑箱。

16.1 Data Domain 失效模式
資料抓取失敗（網路/端點）

狀態：FAIL（不可用）

動作：退回/重試（依 DEPLOY_OPS），必須留審計

官方資料延遲或缺漏

狀態：RETURN（若可等待）或 FAIL（若超時）

動作：標記 quality_flags，禁止靜默補值

Provenance 缺失

狀態：BLOCK（SYS-PROV）

動作：不得往下游傳遞

16.2 Snapshot/State 失效模式
Snapshot 未落盤

狀態：BLOCK（SYS-AUDIT）

動作：停止流程（不可「先跑再說」）

時間不同步（交易日/交易時段判定錯）

狀態：BLOCK（SYS-TIME）

動作：停止並提示 UI

16.3 Analysis 失效模式
Feature 計算缺值/異常

狀態：RETURN（回到 L3/L2 補資料）或 FAIL

動作：必須標記 feature_quality_flags

分析模組輸出方向性指令（越權）

狀態：BLOCK（GOV-FLOW / GOV-SCOPE）

動作：隔離該模組輸出並留痕

16.4 Evidence 失效模式
Evidence Completeness 低於門檻

狀態：RETURN（補齊清單）

動作：回到 L4/L3 取得缺口資料

Provenance 斷裂

狀態：BLOCK（SYS-PROV）

Evidence 衝突（conflict_flags）

狀態：SUCCESS（但必須帶 conflict_flags）或 RETURN（若政策要求必須解衝突）

動作：不得隱藏衝突

16.5 Regime 失效模式
Regime 低信心或不明確

狀態：RETURN（要求更多證據）或交由風控升級（MKT-REGIME-02）

Regime 判定不可交易

狀態：交由 L7 觸發 VETO（或直接標記禁入）

16.6 Risk/Compliance 失效模式（最高敏感）
規則快照缺失 / 版本不可追溯

狀態：VETO（CMP-VERSION / SYS-VERSION）

Token 生成/驗證失敗

狀態：VETO（SYS-VERIFY）

流動性/滑價/曝險超標

狀態：VETO（LIQ/EXE/PTF 類 reason codes）

16.7 Strategy/Research 失效模式
Proposal 引用未白名單策略

狀態：RETURN（GOV-DOC/STR-INDEX 類）

Proposal 試圖直接下單（越權）

狀態：BLOCK（GOV-FLOW）

16.8 Governance 失效模式
發現跳層或缺審計

狀態：RETURN（可補）或 BLOCK（不可補，如缺不可變更審計）

Index 不一致（引用不存在 doc_key）

狀態：BLOCK（GOV-DOC）

16.9 UI 失效模式
UI Trace 不可寫入不可變更儲存

狀態：BLOCK（SYS-AUDIT）→ 禁止 APPROVE

VETO/RETURN 狀態仍可按 APPROVE

狀態：嚴重違規（GOV-SCOPE）→ 必須阻斷並稽核

16.10 Execution 失效模式
通道不健康、Kill Switch 不可用

狀態：BLOCK（EXE-CHANNEL / EXE-KILL）

對帳不一致

狀態：BLOCK（停止送新單）+ 修復流程

重複下單風險

狀態：BLOCK（EXE-DUP）+ 稽核

17. FULL_ARCH × UI_SPEC × RISK_COMPLIANCE 交叉一致性檢核清單（Audit Checklist）
這一節是「避免你說的差很多」的核心：用清單把一致性硬鎖住。
實作/文件重寫時，必須逐條滿足（可新增，不可刪除）。

17.1 風控否決可視化（UI 必須做到）
 UI 有固定 Risk/Compliance Panel（不可被隱藏/折疊到看不到）

 VETO 必須硬顯示 VETO 與 veto_reason_codes[]

 VETO 狀態 APPROVE 必須 disabled（不可繞過）

 PASS 必須顯示 policy_version 與 risk_pass_token_status

17.2 Token 驗證鏈（Risk → Exec 必須做到）
 Execution 送單前必驗證 token（缺即阻斷）

 token 必綁 correlation_id、policy_version、input_hash_ref

 token 驗證失敗必出現 reason code 並回報 UI

17.3 Trace / Audit 完整性（Version/Audit 必須做到）
 任一 Flow 必有 active_version_map_ref

 任一 PASS/APPROVE/EXEC 必可回放（Replay Bundle 具備）

 缺審計物視為未發生（阻斷）

17.4 Strategy 不可越權（Strategy ≠ Order）
 Strategy/Research 只輸出 proposal/scenario/limitations

 任一策略/Agent 不得直接呼叫 Broker Adapter

 發現越權必 BLOCK 並留痕（不可「先跑」）

17.5 層級不可跳步（L1–L11）
 Governance Gate 有跳層檢測與缺口清單

 RETURN 必能導引回補齊處（UI 有跳轉/提示）

18. 模組邊界與通訊限制（Boundary & Comms Rules）
18.1 禁止「層間回寫」的具體定義
L11 的成交結果可以更新「帳戶狀態快照」與「審計物」

但不得回寫：

L4 的特徵定義（語義層）

L5 的證據內容（不得改證據）

L6 的 Regime 結論（只能新增新的 regime 判定，不能改寫舊結論）

L8 的策略邏輯（只能在新版本提出改進）

18.2 允許的回饋（Feedback）型態（Only-Add）
允許新增「事後評估報告」作為新 Evidence（下一輪流程使用）

允許新增「模型監控」報告作為新 Artifact（但不得直接變更裁決）

19. FULL_ARCH 的結構化輸出範本（可直接當工程規格附件）
若你要把 FULL_ARCH 變成「工程落地表格」，以下是最小模板（每個模組都要填）。

19.1 Module Spec Template（每模組一份）
module_id

domain

layer_binding（L?）

responsibilities（做什麼）

non_responsibilities（不做什麼）

inputs[]（Contract IDs）

outputs[]（Contract IDs）

persistence（是否必落盤/不可變更）

audit_artifacts[]

failure_modes[]（FAIL/RETURN/VETO/BLOCK）

security_scope（可讀/可寫/禁止）

only_add_rules（可新增什麼/不可改什麼）

20. Only-Add 演進規則（Part 2 補強條文）
允許新增（Only-Add）：

新 Contract 類型（必須版控、可回放）

新 failure mode 類型與 reason codes

新 UI panel（不得削弱既有 Risk/Trace/Version 顯示）

新 domain 子模組與更細的 layer binding

禁止（硬禁）：

改寫既有 Contract 欄位語義

移除通用硬性欄位（correlation_id / version_map / hash_manifest）

讓任何模組用自由文字繞過 Gate 做裁決

把 AI 提升為「裁決模組」或「取代人類裁決」

（FULL_ARCH｜最大完備版 v2025-12-19 · Part 2 完）
---

## Appendix 2025-12-28｜Only-Add：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_全系統架構總覽（FULL_ARCH）__251219.md（doc_key：FULL_ARCH）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 Addendum/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_全系統架構總覽（FULL_ARCH）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`FULL_ARCH`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=FULL_ARCH` + `canonical_filename=TAITS_全系統架構總覽（FULL_ARCH）__251219.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

# Addendum 2025-12-28｜Only-Add：GLOBAL_ALIGNMENT_PATCH（MASTER_CANON 對齊全域補丁）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md（doc_key：FULL_ARCH）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0007`）  
> 目的：以 MASTER_CANON 為主導，對齊「引用合法性、doc_key 身份、子級標籤（Label）解讀、資料治理別名（alias）封口、最小可稽核引用格式」之全域一致口徑；不改寫任何既有正文條款。

---

## G0. 適用範圍（Hard Boundary）

本 Addendum 僅處理下列事項（不創造新制度、不改寫主文）：
1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。  
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。  
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。  
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。  

本 Addendum **不處理**：
- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

- 本文件 `doc_key` 既有標示為 `FULL_ARCH`；本 Addendum 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

並統一裁決：
- 任何文件「是否可引用」＝以 DOCUMENT_INDEX 之 Authoritative Index（ACTIVE 表格）為準  
- 任何文件「治理等級 bucket」＝以 DOCUMENT_INDEX 之 A+ / A / B / C 分桶為準  
- 文件內自述之等級/狀態若與 Index 有張力：依 DOCUMENT_INDEX §6 採「保守處置」（STOP/RETURN/BLOCK；以既有 Gate/風控規範語義為準）

---

## G2. 子級標籤（Label）之唯一合法解讀（S / B+ / C+）

凡本文件或引用鏈中出現：
- `S`：視為「Supreme Canon 的顯示標籤」或「完備度標籤」，**不構成**新的治理等級 bucket。  
- `B+` / `C+`：視為「嚴格度/完備度子級標籤」，**不構成**新的治理等級 bucket。  

治理覆蓋規則仍固定為：**A+ > A > B > C**（以 DOCUMENT_INDEX 為準）。  

---

## G3. DATA_UNIVERSE（alias）封口（資料治理引用回歸 DATA_SOURCES）

統一裁決：
- 任何出現之 `DATA_UNIVERSE` 一律視為「資料宇宙（Data Universe）」概念別名（alias），**不得**作為 doc_key。  
- 任何需要引用資料來源治理時，唯一合法 doc_key：`DATA_SOURCES`。  
- 若 Evidence/Audit/UI Trace/Gate 引用欄位出現 `doc_key=DATA_UNIVERSE`：  
  - 一律視為「引用非法」→ 依 GOVERNANCE_GATE_SPEC 進行 BLOCK/RETURN（依其既有語義；不得補救）。

---

## G4. 最小可稽核引用格式（Minimum Legal Citation Format｜可直接貼用）

凡聲稱「依據治理文件」之輸出（含：Evidence、Risk/Compliance、Governance Gate、UI Decision、Execution Control、Audit）一律必須同時提供：

```text
ref_doc_key = <DOC_KEY>
ref_file = <完整檔名>
ref_version = <版本日期或檔名日期碼>
ref_section = <章節定位（§ / Heading Path）>
ref_purpose = <用途：例如 gate_check / risk_veto / ui_decision / execution_policy / audit_replay>
ref_notes = <可選：alias/Label 解讀備註>
```

缺任一欄位：
- 依 DOCUMENT_INDEX §6 採保守處置：不得形成裁決性輸出（PASS/APPROVE/EXECUTE 等）；必要時 RETURN/BLOCK。

---

## G5. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫本文件任何既有條款。  
- 本 Addendum 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。  
- 本 Addendum 目的僅在於消解引用歧義、避免 Gate 因 metadata/格式缺口而誤判，並確保全鏈路可稽核、可回放。

（Addendum 2025-12-28｜Only-Add｜Freeze v1.0 完）

