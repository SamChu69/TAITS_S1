<<<<<<< HEAD
# TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219
doc_key：ARCH_FLOW  
治理等級：B+（Canonical Flow Specification｜承接 MASTER_CANON / FULL_ARCH）  
版本狀態：ACTIVE · LOCK_CANDIDATE（流程層細化，允許 Only-Add 擴充）  
版本日期：2025-12-19  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
變更原則：**Only-Add（僅可新增，不可刪減／覆寫／改寫語義）**  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / LOCAL_ENV / DEPLOY_OPS / TWSE_RULES  

---

## 0. 文件定位（Architecture Flow Specification｜不可省略）

本文件為 **TAITS Canonical Flow（L1–L11）之「最大完備流程法規」**，  
以制度化方式定義：

1) **流程觸發（Trigger）**  
2) **各層責任邊界（做什麼／不做什麼）**  
3) **中斷、退回、否決與緊急中止的法定語義**  
4) **跨運行模式的一致性（Research / Backtest / Simulation / Paper / Live）**  
5) **審計、回放、版本一致性之最低不可降標準**

📌 嚴格遵守：
- **L1–L11 不可跳步**
- **流程 ≠ 策略；流程 ≠ 下單**
- **任何中斷必須可解釋、可回放**
- **Risk / Compliance 具最高否決權**
- **Human-in-the-Loop 不可被替代**

---

## 1. Canonical Flow 的不變核心（五大流程公理）

1. **單向性（Forward-only）**  
   只能前進或中斷；不存在隱性回寫或偷偷修正。

2. **層級隔離（Layer Isolation）**  
   每層只處理該層責任；任何越權即違規。

3. **證據先於判斷（Evidence First）**  
   無 Evidence 不得進入 Regime / Risk / Strategy。

4. **否決優先於建議（Veto > Proposal）**  
   任一否決立即生效；績效不得辯護。

5. **人類裁決不可被模擬**  
   L10 僅由人類完成；AI 不得取得最終裁決權。

---

## 2. Canonical Flow 總覽（L1–L11｜不可跳步）

```text
L1  Data Ingestion（資料取得）
L2  Validation & Normalization（校驗/正規化）
L3  Snapshot & State Build（快照/狀態建構）
L4  Feature / Indicator / Structure Extraction（特徵/指標/結構）
L5  Evidence Bundle Assembly（證據包）
L6  Regime Determination（市場狀態）
L7  Risk & Compliance Gate（最高否決）
L8  Strategy Proposal Generation（策略建議）
L9  Governance Gate（治理閘門）
L10 UI Decision & Explain（人機決策/可解釋）
L11 Execution & Control（受控執行）
跨層總禁止：

層間回寫（Back-write）

跳層（Skipping）

策略直連執行

AI 自主化

Annotation 升格

3. 流程狀態轉移矩陣（State Transition Matrix｜最大完備）
Layer	輸入狀態	成功輸出	失敗狀態	失敗去向
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
4.1 類型
Hard Stop：Risk Veto / Compliance Violation

Soft Return：Evidence 不足 / Strategy 不適用 / Flow 不完整

Emergency Stop：Execution 異常 / 系統錯誤 / 人工 Kill Switch

4.2 最小審計要求
任何中斷必留：

中斷層級（Layer）

原因碼（Reason Code）

Evidence Snapshot

Version Reference

5. 多模式一致性（Mode Consistency）
允許變動：

資料來源（歷史/即時）

時間推進（模擬/真實）

Execution 開關（真實/模擬）

禁止變動：

L1–L11 順序

Risk / Governance Gate

Human Decision 存在性

審計密度

6. 全域 Hard Gates（摘要）
Gate	觸發	處置
Human Sovereignty	無人值守	BLOCK
Evidence Replay	不可回放	BLOCK
Regime Precondition	不符/衝突	DOWNGRADE / BLOCK
Risk Veto	任一疑慮	VETO
Strategy≠Execution	含方向/下單	BLOCK
Governance Completeness	缺審計	RETURN

7. L1–L11 逐層法規（精要）
L1｜Data Ingestion
輸出：raw_snapshot_id / source_provenance
禁止：推論、清洗、方向化
失敗：ABORT(L1_FETCH_FAIL)

L2｜Validation & Normalization
輸出：validated_snapshot_id / validation_report
禁止：以估算掩蓋缺口
失敗：ABORT(L2_SCHEMA_FAIL)

L3｜Snapshot & State
輸出：market_snapshot / replay_anchor
禁止：只存在記憶體
失敗：ABORT(L3_STATE_INTEGRITY_FAIL)

L4｜Feature / Structure
輸出：feature_vector / structure_state
禁止：方向化 / 非白名單 Feature / Annotation 升格
失敗：ABORT(L4_ILLEGAL_FEATURE)

L5｜Evidence Bundle
輸出：evidence_bundle_id / completeness_score
禁止：以推測補證據
失敗：RETURN 或 ABORT(L5_EVIDENCE_INCOMPLETE)

L6｜Regime
輸出：regime_state / confidence / conflict_flag
禁止：由策略反推
失敗：ABORT(L6_REGIME_UNDEFINED)

L7｜Risk & Compliance
輸出：PASS / VETO / DOWNGRADE / AVOID + reason codes
禁止：績效辯護
失敗：VETO（最高）

L8｜Strategy Proposal
輸出：proposal（非方向）
禁止：價格/數量/下單
失敗：ABORT(L8_OUTPUT_VIOLATION)

L9｜Governance Gate
輸出：PASS / RETURN / BLOCK
禁止：放行缺證據
失敗：RETURN 或 BLOCK

L10｜UI Decision
輸出：decision_trace / risk_disclosure
禁止：誘導下單 / 隱藏否決
失敗：STOP

L11｜Execution & Control
輸出：execution_log / kill_switch_state
禁止：無人值守
失敗：EMERGENCY_STOP

8. 審計（Audit）總則｜「無紀錄＝未發生」
覆蓋 L1–L11、所有中斷、所有模式

不得以 Console Log 取代正式審計物

8.1 Mandatory Audit Fields（最小集）
correlation_id / session_id / layer_id / module_id

timestamp_utc / version_ref

input_hash / output_hash / status / reason_codes

8.2 層級專屬
L3：snapshot_id

L5：evidence_id / provenance_map

L6：regime_label / confidence

L7：policy_version / veto_reason_codes

L10：user_id / ui_trace

L11：order_id_map / kill_switch_events

9. 回放（Replay）規範
Replay Bundle（最小集合）：

documents_active_map

evidence_bundle

regime_state

risk_decision

human_decision（若有）

execution_logs（若有）

all_hashes

一致性要求： 相同 Bundle → 相同結論；否則視為污染。

10. 版本一致性（Version Alignment）
所有輸出必綁 version_ref

新版不得破壞舊 Replay

與 VERSION_AUDIT 分工：

ARCH_FLOW 定義「在哪裡引用版本」

VERSION_AUDIT 管理「如何追溯/回退」

11. Mermaid（含退回/否決）
mermaid
複製程式碼
flowchart TB
  L1[L1 Data] --> L2[L2 QA]
  L2 --> L3[L3 Snapshot]
  L3 --> L4[L4 Analysis]
  L4 --> L5[L5 Evidence]
  L5 -->|OK| L6[L6 Regime]
  L5 -->|Insufficient| L4
  L6 -->|OK| L7[L7 Risk]
  L6 -->|Unclear| STOP1[STOP]
  L7 -->|PASS| L8[L8 Strategy]
  L7 -->|VETO| STOP2[STOP]
  L8 -->|OK| L9[L9 Governance]
  L8 -->|None| L6
  L9 -->|PASS| L10[L10 Human]
  L9 -->|INVALID| L4
  L10 -->|APPROVE| L11[L11 Exec]
  L10 -->|REJECT| STOP3[STOP]
  L11 -->|SUCCESS| END[END]
  L11 -->|FAIL| EMERGENCY[EMERGENCY STOP]
12. FULL_ARCH 對位
FULL_ARCH：定義「有什麼層/模組」

ARCH_FLOW：定義「如何按序運作」

任一不對位 → 非法

13. Only-Add 演進規則
允許：

新增子流程（L4.1、L7.2）

新增中斷原因碼

新增模式（Sandbox）

禁止：

刪除/合併 L1–L11

改寫中斷語義

以效能為由省略審計

（ARCH_FLOW｜最大完備整合版 完）
=======
# TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219
doc_key：ARCH_FLOW  
治理等級：B+（Canonical Flow Specification｜承接 MASTER_CANON / FULL_ARCH）  
版本狀態：ACTIVE · LOCK_CANDIDATE（流程層細化，允許 Only-Add 擴充）  
版本日期：2025-12-19  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
變更原則：**Only-Add（僅可新增，不可刪減／覆寫／改寫語義）**  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / LOCAL_ENV / DEPLOY_OPS / TWSE_RULES  

---

## 0. 文件定位（Architecture Flow Specification｜不可省略）

本文件為 **TAITS Canonical Flow（L1–L11）之「最大完備流程法規」**，  
以制度化方式定義：

1) **流程觸發（Trigger）**  
2) **各層責任邊界（做什麼／不做什麼）**  
3) **中斷、退回、否決與緊急中止的法定語義**  
4) **跨運行模式的一致性（Research / Backtest / Simulation / Paper / Live）**  
5) **審計、回放、版本一致性之最低不可降標準**

📌 嚴格遵守：
- **L1–L11 不可跳步**
- **流程 ≠ 策略；流程 ≠ 下單**
- **任何中斷必須可解釋、可回放**
- **Risk / Compliance 具最高否決權**
- **Human-in-the-Loop 不可被替代**

---

## 1. Canonical Flow 的不變核心（五大流程公理）

1. **單向性（Forward-only）**  
   只能前進或中斷；不存在隱性回寫或偷偷修正。

2. **層級隔離（Layer Isolation）**  
   每層只處理該層責任；任何越權即違規。

3. **證據先於判斷（Evidence First）**  
   無 Evidence 不得進入 Regime / Risk / Strategy。

4. **否決優先於建議（Veto > Proposal）**  
   任一否決立即生效；績效不得辯護。

5. **人類裁決不可被模擬**  
   L10 僅由人類完成；AI 不得取得最終裁決權。

---

## 2. Canonical Flow 總覽（L1–L11｜不可跳步）

```text
L1  Data Ingestion（資料取得）
L2  Validation & Normalization（校驗/正規化）
L3  Snapshot & State Build（快照/狀態建構）
L4  Feature / Indicator / Structure Extraction（特徵/指標/結構）
L5  Evidence Bundle Assembly（證據包）
L6  Regime Determination（市場狀態）
L7  Risk & Compliance Gate（最高否決）
L8  Strategy Proposal Generation（策略建議）
L9  Governance Gate（治理閘門）
L10 UI Decision & Explain（人機決策/可解釋）
L11 Execution & Control（受控執行）
跨層總禁止：

層間回寫（Back-write）

跳層（Skipping）

策略直連執行

AI 自主化

Annotation 升格

3. 流程狀態轉移矩陣（State Transition Matrix｜最大完備）
Layer	輸入狀態	成功輸出	失敗狀態	失敗去向
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
4.1 類型
Hard Stop：Risk Veto / Compliance Violation

Soft Return：Evidence 不足 / Strategy 不適用 / Flow 不完整

Emergency Stop：Execution 異常 / 系統錯誤 / 人工 Kill Switch

4.2 最小審計要求
任何中斷必留：

中斷層級（Layer）

原因碼（Reason Code）

Evidence Snapshot

Version Reference

5. 多模式一致性（Mode Consistency）
允許變動：

資料來源（歷史/即時）

時間推進（模擬/真實）

Execution 開關（真實/模擬）

禁止變動：

L1–L11 順序

Risk / Governance Gate

Human Decision 存在性

審計密度

6. 全域 Hard Gates（摘要）
Gate	觸發	處置
Human Sovereignty	無人值守	BLOCK
Evidence Replay	不可回放	BLOCK
Regime Precondition	不符/衝突	DOWNGRADE / BLOCK
Risk Veto	任一疑慮	VETO
Strategy≠Execution	含方向/下單	BLOCK
Governance Completeness	缺審計	RETURN

7. L1–L11 逐層法規（精要）
L1｜Data Ingestion
輸出：raw_snapshot_id / source_provenance
禁止：推論、清洗、方向化
失敗：ABORT(L1_FETCH_FAIL)

L2｜Validation & Normalization
輸出：validated_snapshot_id / validation_report
禁止：以估算掩蓋缺口
失敗：ABORT(L2_SCHEMA_FAIL)

L3｜Snapshot & State
輸出：market_snapshot / replay_anchor
禁止：只存在記憶體
失敗：ABORT(L3_STATE_INTEGRITY_FAIL)

L4｜Feature / Structure
輸出：feature_vector / structure_state
禁止：方向化 / 非白名單 Feature / Annotation 升格
失敗：ABORT(L4_ILLEGAL_FEATURE)

L5｜Evidence Bundle
輸出：evidence_bundle_id / completeness_score
禁止：以推測補證據
失敗：RETURN 或 ABORT(L5_EVIDENCE_INCOMPLETE)

L6｜Regime
輸出：regime_state / confidence / conflict_flag
禁止：由策略反推
失敗：ABORT(L6_REGIME_UNDEFINED)

L7｜Risk & Compliance
輸出：PASS / VETO / DOWNGRADE / AVOID + reason codes
禁止：績效辯護
失敗：VETO（最高）

L8｜Strategy Proposal
輸出：proposal（非方向）
禁止：價格/數量/下單
失敗：ABORT(L8_OUTPUT_VIOLATION)

L9｜Governance Gate
輸出：PASS / RETURN / BLOCK
禁止：放行缺證據
失敗：RETURN 或 BLOCK

L10｜UI Decision
輸出：decision_trace / risk_disclosure
禁止：誘導下單 / 隱藏否決
失敗：STOP

L11｜Execution & Control
輸出：execution_log / kill_switch_state
禁止：無人值守
失敗：EMERGENCY_STOP

8. 審計（Audit）總則｜「無紀錄＝未發生」
覆蓋 L1–L11、所有中斷、所有模式

不得以 Console Log 取代正式審計物

8.1 Mandatory Audit Fields（最小集）
correlation_id / session_id / layer_id / module_id

timestamp_utc / version_ref

input_hash / output_hash / status / reason_codes

8.2 層級專屬
L3：snapshot_id

L5：evidence_id / provenance_map

L6：regime_label / confidence

L7：policy_version / veto_reason_codes

L10：user_id / ui_trace

L11：order_id_map / kill_switch_events

9. 回放（Replay）規範
Replay Bundle（最小集合）：

documents_active_map

evidence_bundle

regime_state

risk_decision

human_decision（若有）

execution_logs（若有）

all_hashes

一致性要求： 相同 Bundle → 相同結論；否則視為污染。

10. 版本一致性（Version Alignment）
所有輸出必綁 version_ref

新版不得破壞舊 Replay

與 VERSION_AUDIT 分工：

ARCH_FLOW 定義「在哪裡引用版本」

VERSION_AUDIT 管理「如何追溯/回退」

11. Mermaid（含退回/否決）
mermaid
複製程式碼
flowchart TB
  L1[L1 Data] --> L2[L2 QA]
  L2 --> L3[L3 Snapshot]
  L3 --> L4[L4 Analysis]
  L4 --> L5[L5 Evidence]
  L5 -->|OK| L6[L6 Regime]
  L5 -->|Insufficient| L4
  L6 -->|OK| L7[L7 Risk]
  L6 -->|Unclear| STOP1[STOP]
  L7 -->|PASS| L8[L8 Strategy]
  L7 -->|VETO| STOP2[STOP]
  L8 -->|OK| L9[L9 Governance]
  L8 -->|None| L6
  L9 -->|PASS| L10[L10 Human]
  L9 -->|INVALID| L4
  L10 -->|APPROVE| L11[L11 Exec]
  L10 -->|REJECT| STOP3[STOP]
  L11 -->|SUCCESS| END[END]
  L11 -->|FAIL| EMERGENCY[EMERGENCY STOP]
12. FULL_ARCH 對位
FULL_ARCH：定義「有什麼層/模組」

ARCH_FLOW：定義「如何按序運作」

任一不對位 → 非法

13. Only-Add 演進規則
允許：

新增子流程（L4.1、L7.2）

新增中斷原因碼

新增模式（Sandbox）

禁止：

刪除/合併 L1–L11

改寫中斷語義

以效能為由省略審計

（ARCH_FLOW｜最大完備整合版 完）
>>>>>>> b86b67594931d531a6ecfabca56380f4bf2b48ef
