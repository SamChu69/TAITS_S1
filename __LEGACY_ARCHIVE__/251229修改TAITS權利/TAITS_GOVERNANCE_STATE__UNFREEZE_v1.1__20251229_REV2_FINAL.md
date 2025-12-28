# TAITS_GOVERNANCE_STATE__UNFREEZE_v1.1__20251229

doc_key：GOVERNANCE_STATE_UNFREEZE_V1X  
治理等級：A（治理狀態文件｜State-of-Governance）  
生效狀態：ACTIVE（Timebox 內）  
授權來源：Human Sovereignty（人類最高決策者）  
時區：Asia/Taipei  
生效日期：2025-12-29  
版本備註：REV2（強化「人類主權置頂」與「文件不得否決人類命令」之裁決語義；同時保留可稽核/可回放要求）

---

## 0. 最高裁決條款（Human Sovereignty Supreme Clause｜置頂）

1. **人類最高決策者擁有最終裁決權。**  
   - 任何治理文件、流程條款、Gate/Token/Reason Code、或任何 Agent/AI 內規，**不得否決或阻止**人類最高決策者的明確命令。  
2. **文件與流程的角色為「可回放/可稽核的制度化表述」，不是對人類主權的限制器。**  
   - 當人類最高決策者下達「覆寫/改寫/刪除」級別命令時，系統義務是：**執行＋留痕＋可追溯**。  
3. **無明確人類命令時，系統才依既有治理裁決序位運行。**  
   - 裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（其餘文件依各自治理等級與 Index Gate 判定）

---

## 1. 文件定位（Governance State Declaration）

本文件為 **獨立治理狀態文件**，用於在指定期間內解除 `GOVERNANCE_STATE = Freeze v1.0` 的限制，
以允許對 **全部 ACTIVE 治理文件** 進行「結構性重編」與「正文覆寫更新」作業（含去附錄化、正文整併重編、刪除被最新內容取代之舊段落），
並在期滿後依本文件規範進行 **Re-Freeze（再封版）**。

---

## 2. 解凍原因（Reason）

- 目標：將 TAITS 全部 ACTIVE 文件更新為「最新架構＋最新流程」的 **單一一致正文**。
- 必要性：在 Freeze v1.0 之 Only-Add 限制下，補充內容只能疊加，導致閱讀路徑分裂、重複段落累積與治理歧義。
- 命令：依人類最高決策者授權，本次於 Timebox 內執行「去附錄化＋正文整併重編（該刪就刪、該改就改）」。

---

## 3. 解凍範圍（Scope）

### 3.1 允許變更的文件集合（Reference Set）
- 以 `DOCUMENT_INDEX` 內標記為 **ACTIVE** 的文件集合為準（包含 A+ / A / B / C 等級文件）。
- 若任何文件未被 `DOCUMENT_INDEX` 標記為 ACTIVE，則本次 UNFREEZE 不授權其結構性重編。

### 3.2 允許的變更型態（Allowed Change Types）
在本 UNFREEZE v1.1 Timebox 內，允許對上述 ACTIVE 文件進行以下變更：

1) **去附錄化（De-Appendix）**  
- 將原本以 `附錄 / Appendix / Addendum` 形式存在、但屬於「實質規範」的內容，直接整併至其應歸屬之正文章節位置。

2) **正文整併重編（Consolidated Rewrite）**  
- 合併重複章節、統一章節命名與結構導航；以最新內容 **取代** 舊版重複段落（非追加疊加）。

3) **舊版重複段落移除（Remove Superseded Content）**  
- 對於已被最新內容完整取代、或造成歧義/衝突的舊段落，允許移除；但必須滿足 §6 的可稽核要求。

4) **術語與引用格式統一（Terminology & Citation Normalization）**  
- 依 `AI_GOV`、`DOCUMENT_INDEX`、`MASTER_ARCH` 既有裁決語義，統一術語、裁決描述與最小引用格式。

### 3.3 禁止事項（Forbidden Even Under UNFREEZE）
> 下列禁止事項為「制度性保護欄」，其目的不是限制人類主權，而是防止系統在無明確人類命令時失去可治理性。

- 不得弱化或取消 `Risk / Compliance` 最高否決權（含任何降格、軟化、例外化）**在無明確人類覆寫命令時**。
- 不得取消或降級 `L10 Human Decision`（人類最終裁決權）。
- 不得破壞 Canonical Flow（L1–L11）之「可追溯、可回放、可稽核」基本特性。
- 不得破壞 `DOCUMENT_INDEX` 作為 **Index Gate（裁決唯一入口）** 的權威地位（在無明確人類命令時）。

---

## 4. 解凍有效期間（Timebox）
- 起始：2025-12-29 00:00（Asia/Taipei）
- 結束：2025-12-31 23:59（Asia/Taipei）

---

## 5. Re-Freeze（再封版）條件（Re-Freeze Conditions）
期滿欲 Re-Freeze，必須同時滿足：

1) 全部 ACTIVE 文件完成「去附錄化＋正文整併重編」並形成 **單一一致正文**。  
2) `DOCUMENT_INDEX` 完成最新版本指向（ACTIVE / latest_artifact）與裁決口徑同步。  
3) `VERSION_AUDIT` 完成 Ledger 留痕（每份文件的 rewrite 事件可追溯）。  
4) 無未裁決之治理衝突或歧義；衝突裁決序位：`DOCUMENT_INDEX → MASTER_ARCH → AI_GOV`。  

---

## 6. VERSION_AUDIT 審計輸出要求（Audit Outputs）
本次 UNFREEZE v1.1 必須產出可稽核證據鏈，至少包含：

- `batch_id`：本次全量重編批次識別碼  
- `audit_anchor`：本次批次在 `VERSION_AUDIT` 中的 Ledger 起點  
- `per-file rewrite record`：每份文件須記錄  
  - 被移除之段落/章節（摘要級）  
  - 取代來源（最新段落定位）  
  - 合併後章節定位（章節路徑）  
  - 與 `DOCUMENT_INDEX` 的 doc_key/版本指向對齊  
  - **指令來源：Human Sovereignty（人類最高決策者）**  

---

## 7. 裁決與適用（Decision）
- 本文件在 Timebox 內授權「可刪可改」之全文重編作業；但 AI/Agent **不得自行啟動**，必須由人類最高決策者明確下令。  
- Timebox 外若未完成 Re-Freeze，後續結構性變更須回到 `DOCUMENT_INDEX` 與 `VERSION_AUDIT` 進行裁決與留痕。  

---
