# TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219

doc_key：ARCH_FLOW  
治理等級：B+（Canonical Flow Specification｜承接 MASTER_CANON / FULL_ARCH）  
版本狀態：ACTIVE · LOCK_CANDIDATE（流程層細化，允許 Only-Add 擴充）  
版本日期：2025-12-19  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / LOCAL_ENV / DEPLOY_OPS / TWSE_RULES  
變更原則：Only-Add（僅可新增，不可刪減／覆寫／改寫語義）

---

## 0. 文件定位（不可省略）

本文件為 **TAITS Canonical Flow（L1–L11）之流程細化法規**，  
其唯一職責為：

- 將 **MASTER_CANON 已裁決之 L1–L11**
- 轉譯為 **可實作、可檢查、可回放的流程規格**

本文件 **不具 Canonical 裁決權**，不得：
- 新增 Layer
- 改寫 Layer 語義
- 解釋或修正 MASTER_CANON

如有衝突：  
**DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決**

---

## 1. Canonical Flow 不變公理（流程層硬性約束）

1. **Forward-only**：流程只能前進或中止，不得回寫  
2. **Layer Isolation**：每層只做該層責任  
3. **Evidence First**：無 Evidence 不得進 Regime / Risk  
4. **Veto > Proposal**：否決立即生效，不得辯護  
5. **Human-in-the-Loop**：L10 僅由人類裁決

---

## 2. Canonical Flow 總覽（L1–L11）

L1  Data Ingestion
L2  Validation & Normalization
L3  Snapshot & State Build
L4  Feature / Indicator / Structure
L5  Evidence Bundle
L6  Regime Determination
L7  Risk & Compliance Gate
L8  Strategy Proposal
L9  Governance Gate
L10 Human Decision (UI)
L11 Execution & Control
全域禁止事項：

跳層（Skipping）

層間回寫（Back-write）

策略直連執行

AI 自主裁決

Annotation 升格為裁決依據

3. 流程狀態轉移矩陣（State Transition Matrix）
Layer	輸入狀態	成功輸出	失敗狀態	去向
L1	NoData	RawDataReady	SourceFail	STOP
L2	RawDataReady	CanonicalReady	QAFail	STOP
L3	CanonicalReady	SnapshotReady	SnapshotFail	STOP
L4	SnapshotReady	FeatureReady	AnalysisFail	STOP
L5	FeatureReady	EvidenceReady	EvidenceInsufficient	RETURN L4
L6	EvidenceReady	RegimeReady	RegimeUnclear	STOP
L7	RegimeReady	RiskPass	RiskVeto	STOP
L8	RiskPass	StrategyReady	NoStrategy	RETURN L6
L9	StrategyReady	FlowValid	FlowInvalid	RETURN L4
L10	FlowValid	HumanApprove	HumanReject	STOP
L11	HumanApprove	Executed	ExecFail	EMERGENCY_STOP

4. 中斷類型（Interrupt Taxonomy）
4.1 類型定義
Hard Stop：Risk / Compliance VETO

Soft Return：Evidence 不足、流程不完整

Emergency Stop：Execution 異常 / Kill Switch

4.2 最小審計要求
任何中斷必須留下：

Layer

Reason Code

Evidence Snapshot

Version Reference

5. 多模式一致性（Mode Consistency）
允許變動

資料來源（歷史 / 即時）

時間推進（模擬 / 真實）

Execution 開關

禁止變動

L1–L11 順序

Risk / Governance Gate

Human Decision 存在性

審計密度

6. 全域 Hard Gates（摘要）
Gate	觸發	處置
Human Sovereignty	無人類裁決	BLOCK
Evidence Replay	不可回放	BLOCK
Regime Precondition	不符	DOWNGRADE / BLOCK
Risk Veto	任一疑慮	VETO
Strategy ≠ Execution	含下單語義	BLOCK
Governance Completeness	缺審計	RETURN

7. L1–L11 逐層法規（精要）
L1｜Data Ingestion
輸出：raw_snapshot_id / provenance
禁止：推論、方向化
失敗：ABORT(L1_FETCH_FAIL)

L2｜Validation & Normalization
輸出：validated_snapshot_id / report
禁止：估算補缺
失敗：ABORT(L2_SCHEMA_FAIL)

L3｜Snapshot & State
輸出：market_snapshot / replay_anchor
禁止：僅存記憶體
失敗：ABORT(L3_STATE_FAIL)

L4｜Feature / Structure
輸出：feature_vector
禁止：方向化、非白名單
失敗：ABORT(L4_ILLEGAL_FEATURE)

L5｜Evidence
輸出：evidence_bundle_id / completeness
禁止：推測補證據
失敗：RETURN / ABORT

L6｜Regime
輸出：regime_state / confidence
禁止：由策略反推
失敗：ABORT(L6_UNDEFINED)

L7｜Risk & Compliance
輸出：PASS / VETO / reason codes
禁止：績效辯護
失敗：VETO（最高）

L8｜Strategy Proposal
輸出：proposal（非下單）
禁止：價格、數量
失敗：ABORT(L8_VIOLATION)

L9｜Governance Gate
輸出：PASS / RETURN / BLOCK
禁止：放行缺證據
失敗：RETURN / BLOCK

L10｜Human Decision (UI)
輸出：decision_trace
禁止：誘導、隱藏否決
失敗：STOP

L11｜Execution & Control
輸出：execution_log / kill_switch
禁止：無人值守
失敗：EMERGENCY_STOP

8. 審計總則（Audit Supremacy）
原則：無紀錄＝未發生

8.1 Mandatory Fields
correlation_id / layer_id / timestamp / version_ref
input_hash / output_hash / status / reason_codes

8.2 層級專屬
L3：snapshot_id

L5：evidence_id

L6：regime_label

L7：policy_version

L10：user_id / ui_trace

L11：order_id_map / kill_events

9. 回放（Replay）規範
Replay Bundle 必須包含：

active_documents_map

evidence_bundle

regime_state

risk_decision

human_decision（若有）

execution_logs（若有）

all_hashes

一致性要求：
同一 Bundle → 同一結論，否則視為污染

10. FULL_ARCH 對位聲明
FULL_ARCH：定義「有什麼模組」

ARCH_FLOW：定義「如何按序運作」

未對位者，一律視為 非法實作

11. Only-Add 演進規則
允許

新增子流程（L4.x、L7.x）

新增中斷原因碼

新增模式（如 Sandbox）

禁止

刪除 / 合併 L1–L11

改寫中斷語義

以效能為由省略審計

（ARCH_FLOW｜最大完備整理版 完）

