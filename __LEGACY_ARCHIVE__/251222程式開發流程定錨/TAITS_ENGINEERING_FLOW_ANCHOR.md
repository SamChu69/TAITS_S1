# TAITS_ENGINEERING_FLOW_ANCHOR.md

## 程式開發流程定錨文件  
（Engineering Flow Anchor｜Freeze v1.0 Compatible）

---

## 0. 文件定位（非常重要）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）之「工程開發流程定錨文件」**，  
目的在於：

- 固定「工程實作時的流程座標系」
- 避免因新對話 / 新 AI / 不同敘事順序，導致流程理解漂移
- 讓任何時刻都能清楚回答：
  >「目前系統做到哪一個階段？」

📌 **裁決聲明（不可忽略）**

- ❌ 本文件 **不是治理文件**
- ❌ 本文件 **不具裁決力**
- ❌ 本文件 **不可覆寫 Canonical Flow**
- ✅ **唯一具治理裁決力之流程：MASTER_CANON（L1–L11）**
- ✅ 本文件僅作為「工程實作順序與進度定錨」

---

## 1. 治理定錨（不可動）

### 1.1 唯一治理裁決來源

- DOCUMENT_INDEX（A+）
- MASTER_CANON（A）
- ARCH_FLOW（B+）
- GOVERNANCE_STATE：Freeze v1.0

📌 若工程流程理解與治理文件衝突，**一律以治理文件為準**。

---

## 2. 工程流程定錨總覽（Phase 0–5）

| 工程 Phase | 對應 Canonical Layer | 工程定位一句話 |
|-----------|----------------------|----------------|
| Phase 0 | 前置（未進入 L 層） | 鎖定文件與版本，防止走歪 |
| Phase 1 | L1–L11（空殼） | 讓流程「存在且能跑」 |
| Phase 2 | L7 / L9 / L11 | 先讓系統會拒絕 |
| Phase 3 | L10 | 確立人類主權入口 |
| Phase 4 | L1–L6 | 補齊證據與 Regime |
| Phase 5 | L8 | 最後才接策略 |

📌 **Phase 不是流程，只是工程落地順序說明。**

---

## 3. Phase 0｜治理與版本基線（Mandatory）

### 3.1 目的
確保後續每一行程式碼，都能指回明確治理依據。

### 3.2 必須完成（全部完成才能進 Phase 1）

- [ ] 確認 DOCUMENT_INDEX 中 ACTIVE 文件清單
- [ ] 確認 GOVERNANCE_STATE = Freeze v1.0
- [ ] 建立 doc_key → 檔案 → hash / version_date 對照
- [ ] 標註治理文件為 read-only
- [ ] 決定所有模組必須標註對應 Canonical Layer（Lx）

🚫 禁止：
- 使用對話內容作為治理依據
- 未標註 L 層就開始寫程式

---

## 4. Phase 1｜Canonical Flow 空殼（流程先存在）

### 4.1 對應 Canonical
L1–L11（全部）

### 4.2 最低完成條件（逐層）

每一層（L1–L11）必須至少具備：

- 能接收上一層輸入
- 能檢查「是否有權執行」
- 能輸出標準事件（PASS / VETO / RETURN / STOP）
- 具備 correlation_id / version_ref

🚫 禁止：
- 策略
- 指標
- 下單
- AI 判斷

---

## 5. Phase 2｜硬 Gate 優先（系統先會拒絕）

### 5.1 對應 Canonical（重點）

- L7｜Risk & Compliance
- L9｜Governance Gate
- L11｜Execution & Control

### 5.2 必須可實際運作

- [ ] L7 能輸出 PASS / VETO + reason codes
- [ ] 僅 PASS 產生 Risk PASS Token
- [ ] L9 可 RETURN / STOP
- [ ] L11 無 Token → BLOCK

🚫 禁止：
- Soft Pass
- 人類 / AI 覆寫 VETO

---

## 6. Phase 3｜UI（人類主權）最小實體

### 6.1 對應 Canonical
- L10｜Human Decision

### 6.2 最小 UI 必須包含

- 顯示 Risk 結果
- 顯示 Regime 狀態
- APPROVE / REJECT
- 決策 trace / log

🚫 禁止：
- 預設批准
- 背景自動批准

---

## 7. Phase 4｜資料 → Evidence → Regime

### 7.1 對應 Canonical
- L1–L6

### 7.2 必須成立

- 資料可追溯
- Snapshot 可回放
- Evidence Bundle 完整
- Regime 可標註「可 / 不可交易」

🚫 禁止：
- 交易訊號
- 多空判斷
- 策略選擇

---

## 8. Phase 5｜策略宇宙接線（最後）

### 8.1 對應 Canonical
- L8｜Strategy & Research

### 8.2 策略模組只能

- 輸出 Proposal
- 輸出 Scenario / Hypothesis
- 接收 Regime / Risk 結果

🚫 絕對禁止：
- 策略直連 L11
- 策略覆寫風控
- 策略自動批准

---

## 9. Commit 前自我檢查（必做）

每次提交前，必須能回答：

1. 這段程式屬於哪一個 Phase？
2. 對應哪一個 Canonical Layer（Lx）？
3. 若沒有 AI、沒有對話，文件能否證明它合法？

三個都能回答，才能 commit。

---

## 10. 定錨總結（一句話）

> **TAITS 的流程由 L1–L11 裁決；  
> Phase 0–5 只是工程上「如何把這條流程做出來」的說明。**

---

## 11. 使用方式（新對話標準）

任何新對話，請先聲明：

>「本對話工程流程請以  
> TAITS_ENGINEERING_FLOW_ANCHOR.md  
> 作為唯一工程定錨文件。」

