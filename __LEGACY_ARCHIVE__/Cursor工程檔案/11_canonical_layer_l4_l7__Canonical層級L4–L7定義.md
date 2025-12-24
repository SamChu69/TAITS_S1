# 11_canonical_layer_l4_l7__Canonical層級L4–L7定義.md
doc_key：CANONICAL_LAYER_L4_L7（工程拆解對位：Batch 2｜Canonical Definition）  
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
- MASTER_CANON：§2（L1–L11 Canonical Flow）之 L4/L5/L6/L7 段落；§3（5 Axioms：Evidence-first / Veto over proposal / Layer isolation / Forward-only）；§5（Evidence 法律地位）；§6（Veto 法律地位）
- MASTER_ARCH：全文中「Regime 高於策略 / Risk&Compliance 最高否決 / AI 非決策主體 / 不得以績效對抗否決 / 禁止傳聞與主觀」之定義段落
- DOCUMENT_INDEX：§1（Hard Laws：Only-Add / 無審計＝未發生 / Index 裁決）、§3（治理等級覆蓋規則）
-->

---

## 0. 文件定位（Definition Scope）

本工程檔定義 Canonical Flow 之 **L4–L7**（分析 → 證據 → Regime → 風險與合規）四層：
- 僅輸出：名詞/實體定義、枚舉、Schema/欄位骨架、State/Lifecycle 語義、禁止事項（原文明示）
- 不輸出：策略邏輯、風控裁決細則（僅限輸出語義）、下單／執行實作、UI 行為或技術細節

---

## 1. L4｜Analysis（分析層）— 定義

### 1.1 Layer 定義
- `layer_code`：`L4_ANALYSIS`
- `layer_name_zh`：分析層
- `layer_name_en`：Analysis
- `purpose`：由 Snapshot 產生可解釋的分析產物（特徵/描述性分析），但不產生交易行為語義。

### 1.2 I/O 定義（最小集合）
- `input`：`Snapshot`
- `output`：`FeatureSet`

### 1.3 禁止事項（原文明示）
- `L4_PROHIBIT_TRADE_DIRECTION_OUTPUT`：禁止直接產生交易方向（buy/sell）。
- `L4_PROHIBIT_ORDER_PARAMETER_OUTPUT`：禁止輸出下單參數（價格/數量/方向/有效期等）。
- `L4_PROHIBIT_LAYER_JUMP`：不得越權產生 L8+ 語義。

### 1.4 核心實體定義（Entities）

#### 1.4.1 Feature（特徵）
- 定義：由 L3 Snapshot 推導之可解釋、可回放的衍生量（可包含指標/統計量/狀態量），但其語義不得等同策略指令。

#### 1.4.2 FeatureSet（特徵集合）
- 定義：可追溯輸入 refs + 版本 refs 的特徵集合，用於 L5 Evidence 組裝。

### 1.5 L4 最小欄位（Schema / Fields）
#### 1.5.1 FeatureSetRecord（最小欄位，不可縮減）
- `featureset_id`
- `snapshot_ref`
- `feature_items[]`（可為 key/value 結構）
- `feature_ruleset_version`（或等價版本引用）
- `dependency_refs[]`（輸入依賴引用：snapshot/components）
- `hash_manifest_ref`
- `generated_at`
- `replay_hint_ref`（可回放提示或引用）

---

## 2. L5｜Evidence（證據層）— 定義

### 2.1 Layer 定義
- `layer_code`：`L5_EVIDENCE`
- `layer_name_zh`：證據層
- `layer_name_en`：Evidence
- `purpose`：把上游資料與分析產物，組裝成可審計、可回放、可追溯的 Evidence Bundle，作為後續判斷的法律基礎。

### 2.2 I/O 定義（最小集合）
- `input`：`FeatureSet`（及其依賴 refs）
- `output`：`EvidenceBundle`

### 2.3 禁止事項（原文明示）
- `L5_PROHIBIT_NO_PROVENANCE`：禁止缺 provenance。
- `L5_PROHIBIT_NON_REPLAYABLE_EVIDENCE`：禁止不可回放的證據作為裁決依據。
- `L5_PROHIBIT_HEARSAY_OR_FEELING`：禁止傳聞/主觀感覺/不可重現經驗敘事作為證據。
- `L5_PROHIBIT_SUMMARY_HIDE_RISK`：禁止以摘要遮蔽關鍵風險或衝突（僅語義限制，不涉 UI）。

### 2.4 核心實體定義（Entities）

#### 2.4.1 EvidenceItem（證據項）
- 定義：單一可追溯的證據單元（來源、時間、hash/ref、語義描述、依賴）。

#### 2.4.2 EvidenceBundle（證據包）
- 定義：由多個 EvidenceItem 組成之證據集合；必須具備 provenance、完整性、不可變性、可回放性。

### 2.5 Evidence 必備屬性（Required Properties｜Enum）
- `EVIDENCE_PROPERTY_PROVENANCE`
- `EVIDENCE_PROPERTY_COMPLETENESS`
- `EVIDENCE_PROPERTY_IMMUTABILITY`
- `EVIDENCE_PROPERTY_REPLAYABILITY`

### 2.6 L5 最小欄位（Schema / Fields）
#### 2.6.1 EvidenceBundleRecord（最小欄位，不可縮減）
- `evidence_bundle_id`
- `evidence_items[]`（每項可展開引用）
- `provenance_ref`
- `completeness_score`（或等價表達）
- `immutability_ref`（hash/manifest）
- `replay_bundle_ref`
- `conflict_flags[]`（衝突標記：存在即可，細則不在本檔）
- `asof_timestamp`
- `generated_at`
- `active_version_map_ref`（doc/policy/schema/rulebook 版本映射引用）

---

## 3. L6｜Regime（市場狀態）— 定義

### 3.1 Layer 定義
- `layer_code`：`L6_REGIME`
- `layer_name_zh`：市場狀態判定
- `layer_name_en`：Regime
- `purpose`：輸出市場狀態標籤（regime label）及其允許/禁止的動作邊界；Regime 高於策略。

### 3.2 I/O 定義（最小集合）
- `input`：`EvidenceBundle`
- `output`：`RegimeState`

### 3.3 禁止事項（原文明示）
- `L6_PROHIBIT_SINGLE_SIGNAL_REGIME`：Regime 不得由單一訊號決定。
- `L6_PROHIBIT_STRATEGY_INFER_REGIME`：不得用策略輸出去反推 Regime（Regime 高於策略）。
- `L6_PROHIBIT_FORCE_FORWARD_WHEN_UNCERTAIN`：Regime 不明確時不得硬推進（允許 STOP/RETURN 之語義，不涉細則）。

### 3.4 核心實體定義（Entities）

#### 3.4.1 RegimeState（市場狀態）
- 定義：對市場環境之狀態標籤化輸出，包含信心度與允許/禁止動作邊界；其目的在於限制下游策略宇宙可用範圍。

### 3.5 Regime 枚舉與欄位（Schema / Fields）

#### 3.5.1 RegimeLabel（枚舉｜最小集合）
- `REGIME_UNKNOWN`
- `REGIME_ALLOWED`
- `REGIME_RESTRICTED`
- `REGIME_PROHIBITED`

> 註：僅提供最小語義集合，用以表達「可交易/受限/不可交易」；更細緻標籤僅能 Only-Add 擴充（不得替換既有語義）。

#### 3.5.2 RegimeStateRecord（最小欄位，不可縮減）
- `regime_state_id`
- `regime_label`
- `regime_confidence`
- `regime_allowed_actions[]`（允許之行為類型語義集合）
- `regime_forbidden_actions[]`
- `regime_change_log_ref`（最近變化引用）
- `evidence_bundle_ref`
- `asof_timestamp`
- `generated_at`
- `hash_manifest_ref`

---

## 4. L7｜Risk & Compliance（風險與合規最高否決）— 定義

### 4.1 Layer 定義
- `layer_code`：`L7_RISK_COMPLIANCE`
- `layer_name_zh`：風險與合規最高否決
- `layer_name_en`：Risk & Compliance
- `purpose`：對下游輸出 PASS 或 VETO（含原因碼），並在 PASS 時產生可被後續引用之通行憑證（PASS token）語義；否決具有最高且不可覆寫之地位。

### 4.2 I/O 定義（最小集合）
- `input`：`RegimeState` + `EvidenceBundle`（以及必要的政策/版本引用）
- `output`：`RiskDecision`（PASS/VETO）+ `reason_codes[]` + `policy_version_ref` + `pass_token`（僅 PASS 時）

### 4.3 禁止事項（原文明示）
- `L7_PROHIBIT_SOFT_PASS`：禁止 Soft Pass（必須明確 PASS/VETO）。
- `L7_PROHIBIT_OVERRIDE_VETO_BY_PERFORMANCE`：禁止以績效/回測對抗或推翻否決。
- `L7_PROHIBIT_HUMAN_OR_AI_OVERRIDE_VETO`：否決不可被人類或 AI 覆寫（此為語義地位定義）。
- `L7_PROHIBIT_MISSING_REASON_CODES`：否決必須附 reason codes（不得模糊化）。

### 4.4 核心實體定義（Entities）

#### 4.4.1 RiskDecision（風控裁決）
- 定義：風險與合規 Gate 的輸出；僅允許 PASS 或 VETO；其裁決地位高於策略提案。

#### 4.4.2 VetoReasonCode（否決原因碼）
- 定義：VETO 之必要附帶資訊；作為審計與回放之最小法律要件（原因碼集合可 Only-Add 擴充，不得改寫既有語義）。

#### 4.4.3 PassToken（通行憑證）
- 定義：僅在 PASS 時生成之可引用憑證語義，用於證明「本次流程在該政策版本下通過 L7」；不得在 VETO 時存在。

### 4.5 L7 最小欄位（Schema / Fields）

#### 4.5.1 RiskDecisionRecord（最小欄位，不可縮減）
- `risk_decision_id`
- `decision`：`PASS` / `VETO`
- `veto_reason_codes[]`（decision=VETO 必填）
- `policy_version_ref`
- `evidence_bundle_ref`
- `regime_state_ref`
- `issued_at`
- `hash_manifest_ref`

#### 4.5.2 PassTokenRecord（最小欄位，不可縮減；僅 decision=PASS 產生）
- `pass_token_id`
- `bound_risk_decision_id`
- `policy_version_ref`
- `issued_at`
- `expires_at`（若原文允許時限語義；未知則標記 unknown，不得臆測）
- `hash_manifest_ref`

---

## 5. 跨層公理對位（Axioms Mapping｜Definition Only）

- `AXIOM_LAYER_ISOLATION`：L4 不得輸出交易語義；L7 僅輸出 PASS/VETO，不產生策略。  
- `AXIOM_EVIDENCE_FIRST`：L5 為 L6/L7 的法律基礎；缺 Evidence 不得裁決。  
- `AXIOM_VETO_OVER_PROPOSAL`：L7 VETO 地位高於任何策略提案（L8）。  
- `AXIOM_FORWARD_ONLY`：L4–L7 不得回寫修正上游；若不足則 RETURN/STOP（僅語義）。  

---

## 6. 最終鎖定聲明（Final Lock｜State）

本檔為 L4–L7 定義層工程轉譯，僅允許 Only-Add（新增原文已明示但尚未收錄之定義/欄位/枚舉），不得刪減、覆寫、偷換語義；若與上位文件衝突，一律以上位裁決順序為準（DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON）。

---

# ✅ 本檔輸出結束（Batch 2｜第 5/7 檔：11）
