# 12_canonical_layer_l8_l11__Canonical層級L8–L11定義.md
doc_key：CANONICAL_LAYER_L8_L11（工程拆解對位：Batch 2｜Canonical Definition）  
工程類型：Canonical Definition（定義層）  
治理前提：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
Canonical 來源允許：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX（皆須為 ACTIVE）  
版本狀態：ENGINEERING_TRANSLATION（不具新增治理效力；僅做原文定義結構化轉譯）

<!--
SOURCE_TAG
Canonical 來源（ACTIVE）：
- TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md（doc_key=MASTER_ARCH）
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md（doc_key=MASTER_CANON）
- TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251219.md（doc_key=DOCUMENT_INDEX）
原文範圍：
- MASTER_CANON：§2（L1–L11 Canonical Flow）之 L8/L9/L10/L11 段落；§3（5 Axioms：Veto over proposal / Human not replaceable / Layer isolation / Forward-only）；§6（Veto 法律地位）；§4（多模式一致性 Invariant）
- MASTER_ARCH：全文中「策略 ≠ 下單 / 人類主權 / AI 非決策主體 / Risk&Compliance 最高否決不可覆寫 / 禁止無人值守交易」之定義段落
- DOCUMENT_INDEX：§1（Hard Laws：Only-Add / Index 裁決 / 無審計＝未發生）、§3（治理等級覆蓋規則）、§4（ACTIVE 唯一性）
-->

---

## 0. 文件定位（Definition Scope）

本工程檔定義 Canonical Flow 之 **L8–L11**（策略提案 → 治理閘門 → 人類裁決 → 執行控制）四層：
- 僅輸出：名詞/實體定義、枚舉、Schema/欄位骨架、State/Lifecycle 語義、禁止事項（原文明示）
- 不輸出：策略邏輯（訊號/觸發/績效）、風控裁決細則、下單實作細節、UI 行為或技術細節

---

## 1. L8｜Strategy & Research（策略與研究）— 定義

### 1.1 Layer 定義
- `layer_code`：`L8_STRATEGY_RESEARCH`
- `layer_name_zh`：策略與研究（提案）
- `layer_name_en`：Strategy & Research
- `purpose`：產生策略提案（Proposal）與情境假設（Scenario），作為下游治理檢查與人類裁決的輸入；**策略永遠不等於下單**。

### 1.2 I/O 定義（最小集合）
- `input`：`RiskDecision(PASS)` + `PassToken` + `RegimeState` + `EvidenceBundle`
- `output`：`StrategyProposal`

### 1.3 禁止事項（原文明示）
- `L8_PROHIBIT_STRATEGY_AS_ORDER`：策略 ≠ 下單；不得把策略輸出當成指令。
- `L8_PROHIBIT_DIRECT_EXECUTION_LINK`：策略不得直連 L11（不得繞過 L9/L10）。
- `L8_PROHIBIT_OVERRIDE_VETO`：不得企圖覆寫/弱化任何否決或限制（Veto > Proposal）。

### 1.4 核心實體定義（Entities）

#### 1.4.1 StrategyProposal（策略提案）
- 定義：在既定 Regime 與 Risk PASS 條件下，針對可能行動提出「提案/假設/觀察/避開/風險調整」之結構化輸出；其法律地位低於任何 Gate 與否決。

#### 1.4.2 ProposalIntent（提案意圖｜Enum）
- `PROPOSE`
- `OBSERVE`
- `AVOID`
- `RISK_ADJUST`
- `CONTEXT_ONLY`

> 註：此為最小語義集合，用以承接既有文件中對策略輸出允許語氣（proposal/context/avoid/observe/risk_adjust）的定義；更細緻意圖僅能 Only-Add 擴充。

### 1.5 L8 最小欄位（Schema / Fields）
#### 1.5.1 StrategyProposalRecord（最小欄位，不可縮減）
- `proposal_id`
- `proposal_intent`（ProposalIntent）
- `proposal_summary_ref`（可追溯描述引用）
- `assumptions_ref`（假設引用；不得以推論取代證據）
- `evidence_bundle_ref`
- `regime_state_ref`
- `risk_decision_ref`
- `pass_token_ref`（必填）
- `constraints_ref`（已知限制引用：例如不可交易/受限；不新增細則）
- `generated_at`
- `hash_manifest_ref`

---

## 2. L9｜Governance Gate（治理閘門）— 定義

### 2.1 Layer 定義
- `layer_code`：`L9_GOVERNANCE_GATE`
- `layer_name_zh`：流程治理 Gate
- `layer_name_en`：Governance Gate
- `purpose`：檢查流程完整性、引用合法性、版本/稽核物完備性；輸出 PASS/RETURN/STOP（不輸出策略、不輸出交易）。

### 2.2 I/O 定義（最小集合）
- `input`：`StrategyProposal` + `FlowTrace` + `VersionRefs`
- `output`：`GateDecision`（PASS/RETURN/STOP） + `gate_reason_codes[]`

### 2.3 禁止事項（原文明示）
- `L9_PROHIBIT_UNINDEXED_REFERENCE`：禁止引用未被 DOCUMENT_INDEX 收錄之文件/片段作為治理依據（Index 裁決）。
- `L9_PROHIBIT_SKIP_AUDIT`：禁止缺稽核/不可追溯仍放行（無審計＝未發生）。
- `L9_PROHIBIT_SHORTCUT_TO_L11`：禁止任何捷徑直達 L11。

### 2.4 核心實體定義（Entities）

#### 2.4.1 FlowTrace（流程追蹤）
- 定義：可回放的流程路徑證據（包含各層輸出引用、版本映射、hash/manifest 之最小集合）；用以證明「此提案」確實沿 Canonical Flow 生成。

#### 2.4.2 GateDecision（治理閘門裁決｜Enum）
- `DECISION_PASS`
- `DECISION_RETURN`
- `DECISION_STOP`

#### 2.4.3 GateReasonCode（閘門原因碼）
- 定義：RETURN/STOP 的必要附帶資訊（可 Only-Add 擴充，不得改寫既有語義）。

### 2.5 L9 最小欄位（Schema / Fields）
#### 2.5.1 GovernanceGateRecord（最小欄位，不可縮減）
- `gate_decision_id`
- `decision`（GateDecision）
- `gate_reason_codes[]`（decision!=PASS 時必填）
- `proposal_ref`
- `flow_trace_ref`
- `active_version_map_ref`（doc_key → version_ref 映射引用）
- `issued_at`
- `hash_manifest_ref`

---

## 3. L10｜Human Decision（人類裁決）— 定義

### 3.1 Layer 定義
- `layer_code`：`L10_HUMAN_DECISION`
- `layer_name_zh`：人類裁決
- `layer_name_en`：Human Decision
- `purpose`：人類對「通過 Gate 的提案」做最終批准或拒絕；Human-in-the-Loop 為不可移除結構。

### 3.2 I/O 定義（最小集合）
- `input`：`GateDecision(PASS)` + `StrategyProposal` + `RiskDecision` + `EvidenceBundle` + `FlowTrace`
- `output`：`HumanDecision`（APPROVE/REJECT） + `human_reason_ref`

### 3.3 禁止事項（原文明示）
- `L10_PROHIBIT_AI_AS_DECIDER`：禁止 AI 代替裁決（AI 非決策主體）。
- `L10_PROHIBIT_BYPASS_L10`：禁止移除或繞過 L10（不存在完全無人值守交易）。
- `L10_PROHIBIT_VAGUE_DECISION`：禁止模糊化裁決原因（需可追溯的理由引用）。

### 3.4 核心實體定義（Entities）

#### 3.4.1 HumanDecision（人類裁決輸出｜Enum）
- `DECISION_APPROVE`
- `DECISION_REJECT`

#### 3.4.2 HumanReason（人類理由）
- 定義：人類裁決的理由引用（可回放/可審計），不得以口述/傳聞取代可追溯證據鏈。

### 3.5 L10 最小欄位（Schema / Fields）
#### 3.5.1 HumanDecisionRecord（最小欄位，不可縮減）
- `human_decision_id`
- `decision`（HumanDecision）
- `human_reason_ref`
- `proposal_ref`
- `gate_decision_ref`
- `risk_decision_ref`
- `pass_token_ref`
- `issued_at`
- `hash_manifest_ref`

---

## 4. L11｜Execution & Control（執行與控制）— 定義

### 4.1 Layer 定義
- `layer_code`：`L11_EXECUTION_CONTROL`
- `layer_name_zh`：執行與控制
- `layer_name_en`：Execution & Control
- `purpose`：在人類批准與通行憑證成立前提下，進行嚴格執行與控制；並確保可中止、可稽核、可回放。

### 4.2 I/O 定義（最小集合）
- `input`：`HumanDecision(APPROVE)` + `PassToken` + `ExecutionConstraints` + `AuditRefs`
- `output`：`ExecutionOrders` + `ExecutionAuditTrail` + `ReplayRefs`

### 4.3 禁止事項（原文明示）
- `L11_PROHIBIT_NO_TOKEN_EXECUTION`：禁止無 PASS token 下單/執行。
- `L11_PROHIBIT_NO_KILL_SWITCH`：禁止在不可中止/無 Kill Switch 條件下執行（語義要求：必須可中止）。
- `L11_PROHIBIT_NO_AUDIT_ARTIFACTS`：禁止缺稽核物仍執行（無審計＝未發生）。
- `L11_PROHIBIT_STRATEGY_DRIVEN_ORDER_PARAMS`：禁止策略直接指定下單參數作為執行輸入（策略 ≠ 下單）。

### 4.4 核心實體定義（Entities）

#### 4.4.1 ExecutionConstraints（執行約束）
- 定義：由上游裁決與控制語義帶入的「必須遵守的執行限制」集合（例如：可交易/受限/不可交易、批准有效性、時間窗等）；本檔僅定義其存在，不定義內容細則。

#### 4.4.2 ExecutionOrders（執行指令集）
- 定義：可被交易執行模組採用之指令集合；其合法性成立條件：L7 PASS + L9 PASS + L10 APPROVE + token 成立。

#### 4.4.3 ExecutionAuditTrail（執行稽核軌跡）
- 定義：可回放、可審計的執行紀錄引用集合（含版本、hash、關聯決策與證據引用）。

### 4.5 L11 最小欄位（Schema / Fields）
#### 4.5.1 ExecutionRunRecord（最小欄位，不可縮減）
- `execution_run_id`
- `human_decision_ref`（必須為 APPROVE）
- `pass_token_ref`
- `execution_constraints_ref`
- `orders_ref`
- `audit_trail_ref`
- `replay_refs[]`
- `started_at`
- `ended_at`
- `kill_switch_ref`（語義：必須存在可中止引用）
- `hash_manifest_ref`

---

## 5. L8–L11 狀態機語義（State / Lifecycle｜Definition Only）

> 本節僅定義狀態與轉移語義；不定義內部條件細則。

### 5.1 ProposalState（枚舉）
- `PROPOSAL_CREATED`
- `PROPOSAL_SUBMITTED`
- `PROPOSAL_GATE_PASSED`
- `PROPOSAL_RETURNED`
- `PROPOSAL_STOPPED`
- `PROPOSAL_DECIDED`

### 5.2 ExecutionState（枚舉）
- `EXECUTION_PENDING`
- `EXECUTION_RUNNING`
- `EXECUTION_HALTED`
- `EXECUTION_COMPLETED`
- `EXECUTION_INVALIDATED`

### 5.3 轉移語義（Transition Semantics）
- `L9 RETURN/STOP`：提案不得進入 L10；不得「先批准再補齊」。
- `L10 REJECT`：不得進入 L11（語義終止）。
- `L7 VETO`：不得產生可用 token；即使策略提案存在，也不得進入 L9+（Veto over proposal）。
- `L11 HALTED`：一旦中止，必須保留稽核與回放引用（語義要求）。

---

## 6. 引用合法性與裁決位階（Index & Hierarchy Definition）

### 6.1 Index 裁決（Definition）
- 未列入 DOCUMENT_INDEX 之任何文件、片段、外部連結，不得作為 L9/L10/L11 的裁決依據或流程放行依據。

### 6.2 上位覆蓋（Definition）
- 若任何下游敘述與上位（MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX）衝突，衝突段落視為無效，直接適用上位文件。

---

## 7. 最終鎖定聲明（Final Lock｜State）

本檔為 L8–L11 定義層工程轉譯，僅允許 Only-Add（新增原文已明示但尚未收錄之定義/欄位/枚舉），不得刪減、覆寫、偷換語義。

---

# ✅ 本檔輸出結束（Batch 2｜第 6/7 檔：12）
