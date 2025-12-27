# TAITS｜程式開發流程定錨文件（Unified Process Anchor）

文件類型：Engineering Process Anchor（Read-Only / Non-Governance）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
治理狀態：Freeze v1.0  
最後更新：2025-01-XX  

---
---

# Addendum 2025-12-27｜Only-Add：流程定錨文件之「清單/數量」快照化 × Index Gate（DOCUMENT_INDEX）唯一裁決 × Phase 對齊引用最小格式（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS｜程式開發流程定錨文件（Unified Process Anchor）.md（doc_key：PROCESS_ANCHOR）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+｜Authoritative Index）＋MASTER_ARCH（A）＋MASTER_CANON（A）  
> 平行對齊：PROJECT_PROMPT｜Addendum 2025-12-27／README｜Addendum 2025-12-27／BEGINNER_GUIDE｜Addendum 2025-12-27／VERSION_AUDIT｜Addendum 2025-12-27  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（建議新增條目：`VA-METADATA_FIX-20251227-0017`）  
> 目的：在 Freeze v1.0 期間，避免工程流程定錨文件被誤用為「ACTIVE 文件集合/文件數量/治理等級」之裁決來源；固定：ACTIVE/doc_key/治理等級/版本有效性一律以 DOCUMENT_INDEX 表格裁決為準；同時補強 Phase（0–5）在引用 Canonical/治理文件時的最小引用格式，使工程對齊可回放、可稽核且不引入口徑漂移。

---

## P0. 本文件定位（Scope Lock）

本文件（PROCESS_ANCHOR）之唯一合法用途為：
- 固定工程 Phase（0–5）之工作節點與輸入/輸出契約（Contract）  
- 指引新對話/新分支在工程軌道下「如何對齊」治理文件與 Canonical Flow（L1–L11）  
- 提供工程活動的引用模板（doc_key/version/section/audit_anchor）

本文件 **不得**：
- 裁決 ACTIVE 文件集合  
- 裁決 doc_key 合法性、治理等級、版本有效性  
- 以本文件內任何「文件清單/數量」覆蓋 DOCUMENT_INDEX 的 Authoritative Index 表格

---

## P1. Snapshot 不裁決（No Hardcoded ACTIVE Set）

凡本文件中出現：
- 「目前共有 X 份文件」  
- 「ACTIVE 文件數 = X」  
- 任何列舉文件清單、推薦清單、工程必備清單  

自本 Addendum 起，一律視為 Snapshot（歷史快照/導覽用途），**不具治理裁決效力**。  
凡涉及 ACTIVE/doc_key/等級/版本有效性，一律以 **DOCUMENT_INDEX 表格**裁決為準。

---

## P2. Phase 對齊引用最小格式（Minimum Legal Citation Format）

### P2.1 強制欄位（缺一視為未引用）
凡工程 Phase 文檔/Issue/PR/Commit message/回放包中出現「依據某文件」或「對齊某規範」的描述，必須至少包含：

- `ref_file`：完整檔名  
- `ref_doc_key`：doc_key  
- `ref_version_date`：版本日期（YYYY-MM-DD 或 __yymmdd）  
- `ref_section`：章節定位（heading path / §x.y）  
- `audit_anchor`：VERSION_AUDIT 稽核錨點（可先用本批次 `VA-METADATA_FIX-20251227-0017`）

缺任一欄位 → 一律視為「未引用」→ 不得形成裁決性輸出；需裁決時必須 STOP/RETURN 以補齊引用資訊。

### P2.2 可直接貼用：工程對齊引用標頭
```text
〔TAITS 工程對齊引用標頭｜Freeze v1.0｜Only-Add〕
phase = <0/1/2/3/4/5>
work_item = <issue_id / task_id / pr_id>
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0017
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 工程對齊引用標頭〕
```

---

## P3. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）

本文件內若出現任何「裁決順序字串」或箭頭序列（例如：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`）：
- 一律視為閱讀/操作助記（Mnemonic）  
- 不得被用作覆蓋規則或裁決權重新分配  
- 若與 DOCUMENT_INDEX §3（覆蓋規則）或 §6（衝突裁決程序）產生張力：一律回到 DOCUMENT_INDEX（不可跳步）

---

## P4. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫本文件既有工程流程內容。  
- 本文件內任何清單/數量一律視為 Snapshot；治理裁決一律回到 DOCUMENT_INDEX。  
- 缺少必要引用欄位時：依 DOCUMENT_INDEX §6 保守處置，並以 VERSION_AUDIT 留痕。

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）


## 1. 文件定位與權限聲明

> **裁決性聲明**

- 唯一具有治理裁決力之流程定義：
  - MASTER_CANON（L1–L11）
  - ARCH_FLOW
- 本文件：
  - 不具治理裁決力
  - 不新增、不修改任何制度
  - 不覆寫 Canonical Flow
- 本文件之唯一用途：
  - 作為 TAITS 工程開發之「流程定錨文件」
  - 固定工程流程座標，終止流程歧義
  - 明確標示目前實作進度

若本文件與 Canonical 文件存在任何衝突：

> **一律以 MASTER_CANON / ARCH_FLOW 為最終裁決依據**

---

## 2. 定錨文件存在目的

在 TAITS 專案中：

- AI 對話不具治理效力
- 不同對話可能出現不同流程敘述方式

若缺乏流程定錨，將導致：

- 新對話反覆討論流程
- 工程順序理解漂移
- 無法一致回答「目前做到哪一階段」

本文件存在目的為：

> **不論新對話或新 AI，  
所有工程討論皆必須回到同一流程座標系。**

---

## 3. 流程定錨核心原則

### 3.1 流程裁決唯一性

- Canonical Flow 僅有一條：L1–L11
- 工程敘述不得覆蓋 Canonical

### 3.2 Phase 的正確定位

- Phase 0–5 為工程敘述語言
- Phase 僅用於描述「工程進度」
- Phase 不具 PASS / VETO / 裁決權

### 3.3 程式碼可定位性要求

任何工程實作，必須能回答：

1. 屬於哪一個 Phase  
2. 對應哪一個 Canonical Layer（Lx）  
3. 能否指回對應治理文件  

---

## 4. Canonical Layer × Engineering Phase 對位表

| Canonical Layer | Layer 名稱 | 對應 Phase |
|-----------------|------------|------------|
| L1 | Data Source | Phase 1 |
| L2 | Normalization | Phase 1 |
| L3 | Snapshot & State | Phase 1 |
| L4 | Analysis | Phase 2 |
| L5 | Evidence | Phase 2 |
| L6 | Regime | Phase 3 |
| L7 | Risk & Compliance | Phase 3 |
| L8 | Strategy & Research | Phase 4 |
| L9 | Governance Gate | Phase 4 |
| L10 | Human Decision | Phase 5 |
| L11 | Execution & Control | Phase 5 |

---

## 5. Engineering Phase 定義（定錨版）

### 5.1 Phase 0｜治理與版本鎖定

性質：治理前置階段（不屬於任何 L 層）

必須完成項目：

- DOCUMENT_INDEX ACTIVE 文件確認
- GOVERNANCE_STATE = Freeze v1.0
- doc_key / version_ref / hash 固定
- 模組 L 層標註規則確立

禁止事項：

- 使用對話作為治理依據
- 未標註 L 層即開始實作

---

### 5.2 Phase 1｜資料與狀態骨架（L1–L3）

允許事項：

- 官方資料來源
- 正規化處理
- Snapshot / State 落盤與回放

禁止事項：

- 指標與訊號
- 策略與交易語義

---

### 5.3 Phase 2｜分析與證據（L4–L5）

允許事項：

- 描述性分析
- Evidence Bundle（可追溯、可回放）

禁止事項：

- buy / sell
- signal / trigger
- 績效、勝率、排序

---

### 5.4 Phase 3｜Regime 與 Risk（L6–L7）

必須成立條件：

- Regime 可標示不可交易狀態
- Risk 僅輸出 PASS / VETO
- VETO 附 reason codes
- Risk PASS Token 機制存在

禁止事項：

- Soft Pass
- 人類或 AI 覆寫 VETO

---

### 5.5 Phase 4｜策略提案與治理檢查（L8–L9）

允許事項：

- Strategy Proposal / Scenario
- Governance Gate RETURN / STOP

禁止事項：

- 策略即行為
- 策略直連 Execution
- AI 自動批准

---

### 5.6 Phase 5｜人類裁決與執行（L10–L11）

必須成立條件：

- UI 為唯一 APPROVE / REJECT 入口
- 無 Risk PASS Token → Execution BLOCK
- Execution 全程可審計、可中止

禁止事項：

- 無 UI 自動批准
- 無 Token 下單

---

## 6. 工程進度狀態標示（流程座標）

> **本區為流程定錨之唯一狀態來源**

```text
Current Phase        : Phase 0
Completed Phases     : Phase 0
Next Target Phase    : Phase 1（L1–L3 Data / State Skeleton）
Blocked Layers       : L4–L11（依法不可實作）
Last Review Date     : YYYY-MM-DD
