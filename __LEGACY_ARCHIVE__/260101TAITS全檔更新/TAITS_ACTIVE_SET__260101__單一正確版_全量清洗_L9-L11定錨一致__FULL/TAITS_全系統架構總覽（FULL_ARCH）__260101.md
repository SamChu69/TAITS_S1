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
版本日期：2026-01-01
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX
平行參照：ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES（alias: DATA_UNIVERSE） / DEPLOY_OPS / LOCAL_ENV / TWSE_RULES
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化邊界與否決鏈/偷換模組職責）

## L9–L11 最終語義定錨（單一正確版｜必須一致）

> 本節為 TAITS 在 L9／L10／L11 的**唯一正確語義**。  
> 任何文件中若出現與本節不一致之描述，視為舊錯口徑（不得保留於單一正確版）。

### L9｜投資報告（Investment Report｜可追蹤、可更新、可稽核）
L9 的產出定位為「**給人看的完整投資報告**」，不是一次性的口頭解說；必須可在後續事件/行情變動下持續更新並可追溯。
L9 最低交付物應包含（不限於）：
- **標的化**：標的識別、觀測起點、追蹤狀態（open/hold/watch/exit-candidate 等）、版本號與時間戳。
- **數據**：對應 L1–L8 的關鍵數據表（消息/基本/技術/籌碼/風險/制度），含來源、取樣時間、缺漏註記。
- **圖形**：至少包含價格走勢與關鍵技術指標狀態視覺化（例如均線、RSI、MACD；以「狀態」呈現，非主觀敘事）。
- **進出場建議（非下單）**：建議區間/觸發條件/失效條件（停損/停利/風險撤退），並明確標示「此為建議，不構成下單」。
- **情境更新（Regime/Event）**：當市場制度/事件/風險狀態改變，需能產生增量更新（delta）並保留回放鏈。
- **可稽核鏈**：引用到 L11 的 record_id / ledger_id（或等價識別），以確保報告可被回放與驗證。

### L10｜人類裁決與交易授權（Human Decision & Authorization｜唯一決策點）
L10 的定位為「**人類最高決策者的最終裁決介面與授權層**」。  
- **最終決策者永遠是人類**：你決定採取何種模式與是否授權交易。
- L10 可裁決/授權的動作包含（不限於）：**不動作／回測／模擬／半自動／全自動**。
- AI/Agent 在 L10 僅能提供「選項、理由、風險揭露與建議」，**不得自行構成下單行為**；下單/執行屬於 L10 授權後由執行控制規範承接。

### L11｜工程稽核與全層回放（Engineering Audit & Replay｜全層留痕）
L11 的定位為「**工程檢視與稽核回放層**」，不是下單層，也不是只記錄 L10。
- **全層留痕**：L11 必須覆蓋 L1–L11 每一層的關鍵輸入/輸出/裁決/否決/變更理由與時間戳。
- **雙料輸出**：同一筆紀錄需同時具備  
  1) 人話可讀（你能看懂，用於檢視系統是否合理）  
  2) 工程可用（可重現、可驗證、可追溯，用於開發/稽核/回放）
- **目的**：用來檢查每一層的功能是否合理、是否需要調整、以及自動/半自動/全自動在不同時點的決策依據是否一致可回放。


---

---

# TAITS_全系統架構總覽（FULL_ARCH）__251219
## Part 2｜介面契約・Trace 範本・失效模式・一致性檢核（最大完備）

doc_key：FULL_ARCH
治理等級：B（System Architecture Overview｜承接 MASTER_CANON / ARCH_FLOW）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（架構層總覽，可隨系統擴充 Only-Add）
版本日期：2026-01-01
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

（FULL_ARCH｜最大完備版 v2026-01-01 · Part 2 完）
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