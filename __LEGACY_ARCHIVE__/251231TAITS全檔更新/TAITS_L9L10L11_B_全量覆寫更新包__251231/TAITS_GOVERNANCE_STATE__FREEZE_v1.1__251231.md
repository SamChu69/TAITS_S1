# TAITS_GOVERNANCE_STATE__FREEZE_v1.1__251231
doc_key：GOVERNANCE_STATE_FREEZE_V1  
治理等級：A（Governance State｜治理狀態裁決文件）  
適用範圍：TAITS 全系統（對所有 B/C 文件施加 Freeze v1.1 之變更門檻與語義鎖定）  
版本狀態：ACTIVE（Freeze v1.1 生效）  
版本日期：2025-12-31  
上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ AI_GOV（A+）  
平行參照：VERSION_AUDIT / GOVERNANCE_GATE_SPEC / DEPLOY_OPS  
變更原則：Only-Add（僅可新增；禁止刪減、摘要化縮減、偷換語義；必要之「正文重編」僅可採 **整併式覆寫** 且必須保留舊文於 DEPRECATED 附錄）  

---

## 0. 文件定位（State Declaration）

本文件宣告 TAITS 進入 Freeze v1.1：  
在 Freeze v1.0 的基礎上，新增「L9–L11 語義鎖定」與「防 AI 腦補」的硬性門檻。

---

## 1. Freeze v1.1 鎖定項（Locked Semantics）

### 1.1 Canonical L9–L11（B 路徑）鎖定
自 2025-12-31（Asia/Taipei） 起，下列定義為唯一有效口徑（見各文件內之 Binding 段落）：
- L9：投資報告層（必含數據/圖形/進出建議/追蹤鍵；不得下單）
- L10：人類裁決與交易授權（模式切換：不動作/回測/模擬/半自動/全自動）
- L11：工程稽核（全層留痕 + 雙料輸出；不得作執行入口）

### 1.2 反腦補硬性規則（Anti-Hallucination Gate）
- 未在文件內明載之功能：一律視為未授權。
- 若文件中仍存舊口徑：必須標記 DEPRECATED，不得作為現行解讀依據。

---

## 2. 變更門檻（Change Threshold）

### 2.1 允許
- Only-Add 新增（不影響既有語義）
- 補強稽核與回放所需欄位（不引入新權力）

### 2.2 禁止
- 刪除/摘要化/縮減既有規範
- 將策略直連下單
- 將 L11 作為執行入口（任何形式）

---

## 3. 回溯與留痕（Audit）

任何變更必須：
- 更新 DOCUMENT_INDEX（ACTIVE 唯一性）
- 在 VERSION_AUDIT 留痕（含 approver/reviewer/影響範圍/工件 hash）
