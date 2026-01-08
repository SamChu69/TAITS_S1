# TAITS_系統架構與流程細化說明（ARCH_FLOW）

- doc_key：ARCH_FLOW  
- 基線日期：2026-01-08（Asia/Taipei）  
- 版本日期：2026-01-08（Asia/Taipei）  
- 治理裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  

---

## 0. 文件定位（Architecture Flow Specification）

本文件為 TAITS 的「系統架構與流程細化說明（ARCH_FLOW）」：
- 用於把 FULL_ARCH（模組總覽）細化成可落地的跨模組流程、資料流、事件流與治理閘門落點。
- 用於逐段描述 Canonical Flow（L1–L11）在工程實作上的「節點、輸入、輸出、Gate、留痕」。
- 本文件不取代 MASTER_CANON 的 Canonical 定義；僅做工程落地的流程細化。
- 本文件不產生投資建議、不產生策略推薦。

本文件以制度化方式定義：
1) 流程觸發（Trigger）  
2) 各層責任邊界（做什麼／不做什麼）  
3) 中斷、退回、否決與緊急中止之語義  
4) 跨運行模式的一致性（Research / Backtest / Simulation / Paper / Live）  
5) 審計、回放、版本一致性之最低不可降標準

嚴格遵守：
- L1–L11 不可跳步
- 流程 ≠ 策略；流程 ≠ 下單
- 任何中斷必須可解釋、可回放
- Risk / Compliance 具最高否決權
- Human-in-the-Loop 不可被替代

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
L9  Investment Report（投資報告）
L10 UI Decision & Explain（人機決策/可解釋）
L11 Audit Replay（全層工程稽核回放）
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
L9	StrategyReady	ReportReady	ReportInvalid	RETURN L4
L10	ReportReady	HumanApprove	HumanReject	STOP
L11	HumanApprove	ReplayReady	AuditFail	STOP

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

L9｜Investment Report（投資報告）
輸出：investment_report（含數據/圖形/條件式進出場建議〔非指令〕/風險敘述/追蹤欄位）
必含：report_id / report_timestamp / data_refs / price_snapshot / chart_refs / risk_disclosure / update_fields
治理檢核（Governance Gate｜非層級）：對 L9 報告做 completeness/consistency 檢查，產出 governance_status（PASS/RETURN/BLOCK）
禁止：將 L9 視為裁決/批准層；以報告內容直接觸發下單；放行缺證據/缺風控揭露
失敗：RETURN（回寫至 L4/L5/L6 依缺口類型）或 BLOCK（需人工介入）

L10｜UI Decision
輸出：decision_trace / risk_disclosure
禁止：誘導下單 / 隱藏否決
失敗：STOP

L11｜Audit Replay（全層工程稽核回放）
輸出：replay_bundle_ref / audit_index / trace_manifest（含 L1–L11 引用與執行控制引用）
禁止：把 L11 當批准/下單/送單層；缺 replay 卻宣稱已執行；以 console log 取代正式稽核物
失敗：STOP（AuditFail｜視同未可追溯，不得進入任何實盤路徑）

Execution Control（受控執行）為模組（非 Canonical Layer）：僅能由 L10 HumanApprove 授權後啟動；其結果（execution_log/kill_switch_state）必須被 L11 引用收錄。

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
  L8 -->|OK| L9[L9 Report]
  L8 -->|None| L6
  L9 -->|PASS| L10[L10 Human]
  L9 -->|INVALID| L4
  L10 -->|APPROVE| EXE[Execution Control]
  L10 -->|REJECT| STOP3[STOP]
  EXE -->|LOGS| L11[L11 Replay]
  EXE -->|SUCCESS| END[END]
  EXE -->|FAIL| EMERGENCY[EMERGENCY STOP]
  L11 -->|REPLAY READY| END
12. FULL_ARCH 對位
FULL_ARCH：定義「有什麼層/模組」

ARCH_FLOW：定義「如何按序運作」

任一不對位 → 非法

13. 最大完備 演進規則
允許：

新增子流程（L4.1、L7.2）

新增中斷原因碼

新增模式（Sandbox）

禁止：

刪除/合併 L1–L11

改寫中斷語義

以效能為由省略審計

（ARCH_FLOW｜最大完備整合版 完）

A.0 補充性質聲明（不可省略）

變更原則：最大完備（0 刪減 / 0 覆寫 / 0 偷換語義）

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

A.3 對齊 MASTER_CANON「L10 人類裁決」的最小一致性（最大完備）
為對齊 MASTER_CANON 的 L10 法源要求，ARCH_FLOW 的 L10「輸出」與「禁止事項」必須被視為：

UI_SPEC 的硬規格前置條件（Decision Trace / Risk Disclosure 必須可回放）

任何不生成 decision_trace 或等價引用者，一律視為流程不完整（應落於 治理檢核（Governance Gate｜非層級）之 ReportInvalid/RETURN，並依缺口回寫至 L4/L5/L6）。

本條為對齊補強，不改寫你原文第 7 節 L10 規格。

A.4 對齊 MASTER_CANON 附錄 Z（L9a / L10 / L11）之非混用原則（最大完備）
若系統/文件/報告存在「L9a 人話敘事（分析師敘事）」之輸出：

必須被標記為：NON_DECISION_REFERENCE（非裁決參考）

不得直接影響：

State Transition Matrix

Risk Gate（L7）裁決

Human Decision（L10）按鈕可用性

其唯一合法位置：

作為 L10 的參考資料（Reference），且必須可回指 Evidence refs（不得僅文字）

本條只為「防止混用」，不新增層級、不改寫 Canonical。

（最大完備 · Rendering-Safe Copy · 治理狀態 狀態（以 GOVERNANCE_STATE 為準））

B.0 補充性質聲明

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

  L8 -->|OK| L9[L9 Report]
  L8 -->|None| L6

  L9 -->|PASS| L10[L10 Human]
  L9 -->|INVALID| L4

  L10 -->|APPROVE| EXE[Execution Control]
  L10 -->|REJECT| STOP3[STOP]
  EXE -->|LOGS| L11[L11 Replay]
  EXE -->|SUCCESS| END[END]
  EXE -->|FAIL| EMERGENCY[EMERGENCY STOP]
  L11 -->|REPLAY READY| END
（最大完備 · Audit/Replay Hardening · 治理狀態 狀態（以 GOVERNANCE_STATE 為準））

C.0 補充性質聲明

補充類型：Guideline（最小集補強；不新增制度裁決權）

目的：使「中斷必留原因碼 / Evidence Snapshot / Version Reference」可被工程落地為一致的最小集合，並與 VERSION_AUDIT / UI_SPEC / EXECUTION_CONTROL 的引用方式不衝突。

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

C.3 版本一致性：ARCH_FLOW 與 VERSION_AUDIT 的引用邊界（最大完備）
ARCH_FLOW：定義「每個層在哪裡必須引用 version_ref」

VERSION_AUDIT：管理「版本如何追溯、回退、變更帳本」
本條僅重申你原文第 10 節分工，並明確禁止以「口頭/對話」替代版本引用。

---

---

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 正常化：移除正文中與本文件職責無關之「全局定錨／主權／HFI／L9–L11 特別化」段落，避免與 MASTER_ARCH／AI_GOV／MASTER_CANON 重複與混讀。
- 正常化：移除正文中與架構/流程細化無關之「子級標籤（Label）／助記順位（Mnemonic）／alias／引用模板／canonical_filename」等治理補丁性內容，改由各自對應治理文件承接。
- 正常化：保留並收斂本文件之核心流程細化正文（Canonical Flow 總覽、狀態轉移矩陣、流程圖、審計/回放/中斷事件最小欄位集等），不做摘要縮水。
- 版次：版本日期統一為 2026-01-08（Asia/Taipei），並重算正文雜湊。

### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8）
- BODY_SHA256：526d428b5d8e85bbb8b59d74a4be19e4455a2ab6e2003633a194d48b97725ed9

### 3) 適用範圍（Scope）
- scope_doc_key：ARCH_FLOW
- scope_operation：NORMALIZE（正文去重收斂／結構重排／移除非正文補丁內容）
- scope_constraints：不改寫核心語義；不新增跨文件裁決；裁決序位固定為 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- version_date：2026-01-08（Asia/Taipei）

### 4) 裁決承接（Audit Hand-off）
- 本檔為 B 類治理文件，僅承接上位裁決與 Canonical Flow；不反向改寫 MASTER_CANON。
- 若與上位文件發生衝突：以 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV 為最終裁決。
