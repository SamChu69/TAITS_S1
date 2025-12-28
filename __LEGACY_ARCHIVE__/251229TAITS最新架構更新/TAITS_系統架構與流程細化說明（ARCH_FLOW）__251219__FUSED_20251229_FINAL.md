# HUMAN SOVEREIGNTY｜最高裁決置頂條款（Top-of-File）

> 生效日：2025-12-29（Asia/Taipei） 
> 裁決：**人類最高決策者擁有最終裁決權**；任何治理文件、流程條款、Gate/Token/Reason Code、任何 Agent/AI 內規，**不得否決或阻止**人類最高決策者的明確命令。 
> 文件與流程之角色：提供「可回放／可稽核／可追溯」之制度化表述；不得作為限制器。 
> 無明確人類命令時：系統依既有治理裁決序位與當前狀態運作。 

---

# TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219
doc_key：ARCH_FLOW 
治理等級：B+（Canonical Flow Specification｜承接 MASTER_CANON / FULL_ARCH） 
版本狀態：ACTIVE（UNFREEZE v1.1（REV2）｜FUSED Rewrite）
版本日期：2025-12-29
重編批次：RW-20251229-FUSED-0003
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live） 
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+） 
變更原則：**（僅可新增，不可刪減／覆寫／改寫語義）** 
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX 
平行參照：FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / LOCAL_ENV / DEPLOY_OPS / TWSE_RULES 

---

---

# 2025-12-27｜：B+（bucket=B）對位 × 架構裁決字串助記化 × Canonical 邊界引用模板（Freeze v1.0）

> 補充性質：（只可新增，不可刪減、覆寫、偷換既有語義） 
> 適用文件：TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md（doc_key：ARCH_FLOW） 
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0 
> 上位裁決：Index Gate（DOCUMENT_INDEX）＋治理等級覆蓋（A+ > A > B > C）＋衝突裁決程序（DOCUMENT_INDEX §6）＋AI_GOV（A+）最高約束 
> 口徑對齊： 
> - DOCUMENT_INDEX｜ 2025-12-27-B（B+/C+ 子級標籤定義 × 覆蓋規則對位）〔檔名：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251227B_FINAL.md〕 
> - DOCUMENT_INDEX｜ 2025-12-27（裁決順序字串統一 × 歧義消解） 
> - MASTER_CANON｜ 2025-12-27（S 標籤定位 × 裁決字串消歧） 
> - GOVERNANCE_GATE_SPEC｜ 2025-12-27（字串助記定位 × 雙軌裁決消歧） 
> 稽核對位：VERSION_AUDIT｜ A｜METADATA_FIX Ledger（建議新增條目：`VA-METADATA_FIX-20251227-0003`） 
> 目的：在不改寫正文的前提下，修補本文件「治理等級 B+」與 Index 覆蓋規則之對位歧義；將本文件內部可能出現的「裁決順序字串」明確定位為助記（Mnemonic），避免被誤讀為覆蓋規則；並提供一致的 Canonical 邊界引用模板，確保 Gate/Audit/UI Trace 可回放。

---

## 0. 適用範圍（Hard Boundary）

本 僅處理下列事項，**不改寫**本文件的架構模組定義、資料流、事件流、分層責任與工程規格內容：

1) 治理等級標示 `B+` 的法律定位（bucket 對位） 
2) 「裁決順序字串」之法律定位（助記 ≠ 覆蓋規則） 
3) 引用 MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX / AI_GOV 時的最小合規引用格式（引用模板）

---

## 1. B+ 的法律定位（Tag ≠ New Grade）

### 1.1 統一裁決：B+ 為顯示標籤，其 bucket 仍為 B
本文件檔頭或正文若出現「治理等級：B+」，其唯一合法解讀為：

- `B+` 為 **B 類文件內部的子級標籤（sub-grade tag）** 
- **裁決 bucket = B**（仍受 A+ / A 覆蓋；仍覆蓋 C） 
- `+` **不**構成新的治理等級層級，不改寫覆蓋規則（A+ > A > B > C）

> 兼容處理（不改原文）：既有「B+」字樣保留作顯示標籤；其覆蓋/裁決效力由本節固定回歸 bucket=B。

---

## 2. 架構文件的裁決邊界（Scope Lock）

### 2.1 本文件的裁決邊界（僅限架構/流程細化）
ARCH_FLOW 的裁決力僅限於：
- 系統架構模組分工與邊界 
- Canonical Flow（L1–L11）在工程實作中的「落地流程細化」（不得改寫 Canonical Flow 本身） 
- 事件流／資料流／介面責任的工程規格化描述

ARCH_FLOW **不得**：
- 取代 DOCUMENT_INDEX 的文件合法性裁決（doc_key / ACTIVE / 等級） 
- 取代 MASTER_ARCH 的母憲法鐵律 
- 取代 AI_GOV（A+）對 AI 行為/越權的最高約束 
- 以任何「排序字串」改寫覆蓋規則

---

## 3. 裁決順序字串的法律定位（Mnemonic ≠ Override Rule）

凡本文件內出現之「裁決順序字串」或「高→低順位」描述（例如：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON` 之類箭頭序列）：

- 一律視為 **閱讀/操作助記（Mnemonic）** 
- **不得**被用作覆蓋規則或裁決權重新分配 
- 若其表述與 DOCUMENT_INDEX §3（覆蓋規則）或 §6（衝突裁決程序）產生張力： 
 **一律回到 DOCUMENT_INDEX**（不可跳步）

---

## 4. Canonical 邊界引用模板（Gate-Friendly Reference）

> 用途：確保 ARCH_FLOW 在引用上位文件時，引用端可被 Gate/Audit 機器化檢核，避免因格式差異造成歧義。

### 4.1 引用 DOCUMENT_INDEX（合法性/等級/ACTIVE）
```text
ref_doc_key = DOCUMENT_INDEX
ref_purpose = index_gate_and_override_rule
ref_section = <例如：§3 / §6 / §7 / §9 / 2025-12-27-B>
ref_notes = B+/C+ 為子級標籤；覆蓋規則仍為 A+ > A > B > C
```

### 4.2 引用 MASTER_ARCH（母憲法鐵律）
```text
ref_doc_key = MASTER_ARCH
ref_purpose = constitutional_constraints
ref_section = <例如：主權/邊界/否決權段落>
```

### 4.3 引用 MASTER_CANON（流程語義/層級邊界）
```text
ref_doc_key = MASTER_CANON
ref_purpose = canonical_flow_semantics
ref_gov_grade = A # 以 DOCUMENT_INDEX 裁決為準；S 僅為敘事/版本標籤
ref_section = <例如：L1–L11 對位段落/§15 衝突裁決秩序>
```

### 4.4 引用 AI_GOV（AI 行為/越權最高約束）
```text
ref_doc_key = AI_GOV
ref_purpose = ai_behavior_and_decision_boundary
ref_section = <AI 越權/不可補完/不可改制度之條款>
```

---

## 5. 最終宣告（Freeze v1.0）

- 本 為 ；不改寫任何既有正文。 
- `B+` 在本文件中僅為顯示標籤；裁決 bucket 固定為 B。 
- 所有衝突裁決仍必須回到 DOCUMENT_INDEX 之覆蓋規則與程序（§3／§6）。 
- 若缺少必要引用資訊（doc_key / section / version），僅允許列缺口，不允許裁決性輸出。

（ 2025-12-27｜｜Freeze v1.0 完）

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
L1 Data Ingestion（資料取得）
L2 Validation & Normalization（校驗/正規化）
L3 Snapshot & State Build（快照/狀態建構）
L4 Feature / Indicator / Structure Extraction（特徵/指標/結構）
L5 Evidence Bundle Assembly（證據包）
L6 Regime Determination（市場狀態）
L7 Risk & Compliance Gate（最高否決）
L8 Strategy Proposal Generation（策略建議）
L9 Governance Gate（治理閘門）
L10 UI Decision & Explain（人機決策/可解釋）
L11 Execution & Control（受控執行）
跨層總禁止：

層間回寫（Back-write）

跳層（Skipping）

策略直連執行

AI 自主化

Annotation 升格

3. 流程狀態轉移矩陣（State Transition Matrix｜最大完備）
Layer 輸入狀態 成功輸出 失敗狀態 失敗去向
L1 NoData RawDataReady SourceFail STOP
L2 RawDataReady CanonicalReady QAFail STOP
L3 CanonicalReady SnapshotReady SnapshotFail STOP
L4 SnapshotReady FeatureReady AnalysisFail STOP
L5 FeatureReady EvidenceReady EvidenceInsufficient RETURN L4
L6 EvidenceReady RegimeReady RegimeUnclear STOP
L7 RegimeReady RiskPass RiskVeto STOP
L8 RiskPass StrategyReady NoStrategy RETURN L6
L9 StrategyReady FlowValid FlowInvalid RETURN L4
L10 FlowValid HumanApprove HumanReject STOP
L11 HumanApprove Executed ExecFail EMERGENCY_STOP

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
Gate 觸發 處置
Human Sovereignty 無人值守 BLOCK
Evidence Replay 不可回放 BLOCK
Regime Precondition 不符/衝突 DOWNGRADE / BLOCK
Risk Veto 任一疑慮 VETO
Strategy≠Execution 含方向/下單 BLOCK
Governance Completeness 缺審計 RETURN

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

13. 演進規則
允許：

新增子流程（L4.1、L7.2）

新增中斷原因碼

新增模式（Sandbox）

禁止：

刪除/合併 L1–L11

改寫中斷語義

以效能為由省略審計

（ARCH_FLOW｜最大完備整合版 完）
 A｜ARCH_FLOW × MASTER_CANON 差異與對齊補充
（ · Alignment · Freeze v1.0）

A.0 補充性質聲明（不可省略）

補充類型： / Guideline（對齊補充；不改寫 Canonical）

變更原則：（0 刪減 / 0 覆寫 / 0 偷換語義）

衝突裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON

A.1 與 MASTER_CANON 的定位差異（法源分工）
MASTER_CANON：裁決 L1–L11 的法律地位、責任邊界、公理（含 Human-in-the-Loop 不可移除、Veto 高於一切、Evidence First 等）

ARCH_FLOW：在不改寫 Canonical 的前提下，制度化定義：

流程觸發、狀態轉移、退回/中止語義

跨模式一致性

審計/回放/版本一致性之最低不可降標準

因此：

ARCH_FLOW 可「細化流程節點」

但不得「新增層級、改寫層級語義、提供 Canonical 的替代定義」

A.2 Canonical Flow（L1–L11）不可變：ARCH_FLOW 的合法細化範圍
ARCH_FLOW 的細化只允許發生在：

既有 Layer 內部（例如：L4.1 / L7.2 等子流程）

以「檢查點（checks）」「必備產物（artifacts）」「狀態轉移（state transitions）」呈現

ARCH_FLOW 不允許：

以工程方便為由調換順序或合併 Layer

以效率為由省略 Evidence / Audit / Replay

A.3 對齊 MASTER_CANON「L10 人類裁決」的最小一致性
為對齊 MASTER_CANON 的 L10 法源要求，ARCH_FLOW 的 L10「輸出」與「禁止事項」必須被視為：

UI_SPEC 的硬規格前置條件（Decision Trace / Risk Disclosure 必須可回放）

任何不生成 decision_trace 或等價引用者，一律視為 流程不完整（應落於 L9 Governance Gate 的 FlowInvalid/RETURN）

本條為對齊補強，不改寫你原文第 7 節 L10 規格。

A.4 對齊 MASTER_CANON 附錄 Z（L9a / L10 / L11）之非混用原則
若系統/文件/報告存在「L9a 人話敘事（分析師敘事）」之輸出：

必須被標記為：NON_DECISION_REFERENCE（非裁決參考）

不得直接影響：

State Transition Matrix

Risk Gate（L7）裁決

Human Decision（L10）按鈕可用性

其唯一合法位置：

作為 L10 的參考資料（Reference），且必須可回指 Evidence refs（不得僅文字）

本條只為「防止混用」，不新增層級、不改寫 Canonical。

 B｜渲染安全版 Mermaid（，不覆寫原文）
（ · Rendering-Safe Copy · Freeze v1.0）

B.0 補充性質聲明

補充類型：（渲染修復副本；原文保留）

說明：原第 11 節 Mermaid 區塊在 md 中屬「非標準 fenced code」格式；本附錄提供等價可渲染副本，用於工程文件與 UI/README 引用，不替代、不覆寫原文。

B.1 Canonical Flow（含退回/否決）— 渲染安全版
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
 C｜Reason Code / Artifact / Replay 最小集對齊補強
（ · Audit/Replay Hardening · Freeze v1.0）

C.0 補充性質聲明

補充類型：Guideline（最小集補強；不新增制度裁決權）

C.1 中斷事件最小欄位集（Interrupt Event Minimal Fields）
凡屬 STOP / RETURN / VETO / EMERGENCY_STOP 事件，至少必須產生：

correlation_id

layer_id

status：STOP / RETURN / VETO / EMERGENCY_STOP

reason_codes[]

evidence_snapshot_ref（若適用；至少對應 L5 evidence_bundle_id 或等價引用）

version_ref（documents_active_map 或 active_versions 的引用）

timestamp_utc

output_hash（或等價不可否認摘要）

本條不改寫你原文第 4.2 與第 8.1，只是把「必留」具體化為可落地欄位集。

C.2 Replay Bundle 最小集合（與原文第 9 節一致）
Replay Bundle 仍以原文為準，並補強一條一致性檢查：

Replay Loader 必須檢查 documents_active_map 與 version_ref 一致；任一缺漏 → 視為 Replay 不成立（應 BLOCK/STOP）

C.3 版本一致性：ARCH_FLOW 與 VERSION_AUDIT 的引用邊界
ARCH_FLOW：定義「每個層在哪裡必須引用 version_ref」

VERSION_AUDIT：管理「版本如何追溯、回退、變更帳本」
本條僅重申你原文第 10 節分工，並明確禁止以「口頭/對話」替代版本引用。

（ARCH_FLOW｜ 最大完備補強： A–C · Freeze v1.0）
---

## 2025-12-28｜：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：（只可新增，不可刪減／覆寫／偷換既有語義） 
> 適用文件：TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md（doc_key：ARCH_FLOW） 
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0 
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+） 
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 /下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`ARCH_FLOW`
- 版本狀態：ACTIVE（Freeze v1.0；）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=ARCH_FLOW` + `canonical_filename=TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md`。 
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。 
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

# 2025-12-28｜：GLOBAL_ALIGNMENT_PATCH（MASTER_CANON 對齊全域補丁）｜Freeze v1.0

> 補充性質：（只可新增，不可刪減、覆寫、偷換既有語義） 
> 適用文件：TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md（doc_key：ARCH_FLOW） 
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0 
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6） 
> 稽核對位：VERSION_AUDIT｜ A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0018`） 
> 目的：以 MASTER_CANON 為主導，對齊「引用合法性、doc_key 身份、子級標籤（Label）解讀、資料治理別名（alias）封口、最小可稽核引用格式」之全域一致口徑；不改寫任何既有正文條款。

---

## G0. 適用範圍（Hard Boundary）

本 僅處理下列事項（不創造新制度、不改寫主文）：
1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。 
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。 
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。 
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。 

本 **不處理**：
- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準） 
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則 
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款 
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

- 本文件 `doc_key` 既有標示為 `ARCH_FLOW`；本 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

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

- 本 為 ；不改寫本文件任何既有條款。 
- 本 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。 
- 本 目的僅在於消解引用歧義、避免 Gate 因 metadata/格式缺口而誤判，並確保全鏈路可稽核、可回放。

（ 2025-12-28｜｜Freeze v1.0 完）
