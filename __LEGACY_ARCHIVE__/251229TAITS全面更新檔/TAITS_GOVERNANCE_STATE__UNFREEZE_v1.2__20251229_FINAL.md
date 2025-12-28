# TAITS_GOVERNANCE_STATE__UNFREEZE_v1.2__20251229
doc_key：GOVERNANCE_STATE_UNFREEZE_V1X
治理等級：A（Governance State Declaration｜Freeze / Unfreeze 裁決文件）
生效狀態：UNFREEZE（Timeboxed）

> 本文件係由人類最高決策者（Human Sovereignty）下令授權，依 Freeze v1.0 所載《解凍程序（Unfreeze Protocol）》之最低要求，發布受控解凍（UNFREEZE）裁決。
> 目的：允許對 ACTIVE 文件進行「結構整併（Consolidation）」與「章節重排（Re-structure）」以形成單一完整正文，消除附錄/補充分散造成之引用歧義。
> 注意：本次解凍僅為「結構性整併」；不得新增制度、不得刪減規範、不得偷換既有語義。

---

## 1. 解凍原因（Reason）
- 既有 ACTIVE 文件因歷次補充/附錄/修補段落分散，造成：
  - 讀者與工具鏈對「哪一段才是正文」之歧義
  - L9 / L9a / L10 / L11（Gate / Narrative / Authority / Audit）邊界被混讀之風險
  - 文件引用時需跨檔跨附錄，稽核成本過高
- 因此需一次性「整併為單一完整正文」，以利落地與長期演進。

## 2. 解凍範圍（Scope）
- 範圍：DOCUMENT_INDEX 列為 ACTIVE 之全數文件（含 Process Anchor 類定錨文件）。
- 允許變更類型（僅限）：
  - 章節重排（Reorder）
  - 段落合併（Merge）
  - 標題去附錄化（Remove “Addendum/Appendix/附錄”標示語）
  - 內容搬移（Relocation）以降低歧義
  - 格式統一（Formatting Normalization）
- 禁止事項（Hard Prohibitions）：
  - 新增任何未授權制度或新語義
  - 刪減或覆寫既有規範內容
  - 修改 MASTER_CANON 的 Canonical Flow（L1–L11）之語義

## 3. 解凍期間允許變更文件清單與等級
- A+：AI_GOV（僅允許結構整併，不得改寫規則）
- A：MASTER_ARCH / MASTER_CANON / GOVERNANCE_STATE（僅允許結構整併）
- B / C：其餘 ACTIVE 文件（僅允許結構整併）

## 4. 解凍有效期間（Timebox）
- 起始：2025-12-29（Asia/Taipei）
- 終止：本批次整併包交付即刻結束（同日完成），並立即回復 Freeze v1.0。

## 5. 再 Freeze 條件（Re-Freeze Conditions）
- 交付「整併直覆蓋版」更新包（同名覆蓋）後，系統狀態立即回復：
  - GOVERNANCE_STATE = Freeze v1.0
- Re-Freeze 觸發同時必須完成：
  - DOCUMENT_INDEX 更新（latest_artifact / ACTIVE 快照）
  - VERSION_AUDIT Ledger 條目（批次可追溯）

## 6. VERSION_AUDIT 審計輸出要求
- 必須新增 Ledger 條目並包含：
  - batch_id
  - scope（ACTIVE 文件清單）
  - 變更類型（Reorder/Merge/Relocation/Formatting）
  - 變更禁止與驗證（No-new-semantics / No-deletion）
  - 可回放錨點（audit_anchor）
