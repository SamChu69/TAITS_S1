# TAITS_程式開發流程定錨文件

## 工程流程定錨（Engineering Flow Anchor）  
治理對齊：Freeze v1.0｜Canonical-Aligned

---

## 0. 文件定位（必讀）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）之工程開發流程定錨文件**。

本文件的唯一目的為：

> 固定工程實作時的流程座標系，  
> 避免因新對話、新 AI、不同敘事順序，導致流程理解漂移。

---

### 裁決性聲明（Read-Only）

- 本文件 **不是治理文件**
- 本文件 **不具裁決力**
- 本文件 **不可覆寫 Canonical Flow**
- 唯一具治理裁決力之流程為：
  - `MASTER_CANON（L1–L11）`
  - `ARCH_FLOW`

若本文件與任何治理文件產生理解衝突：

> **一律以 DOCUMENT_INDEX / MASTER_CANON / ARCH_FLOW 為最終裁決依據**

---

## 1. 治理定錨（不可動）

### 1.1 唯一治理裁決來源

- DOCUMENT_INDEX（A+）
- MASTER_CANON（A）
- ARCH_FLOW（B+）
- GOVERNANCE_STATE：Freeze v1.0

工程層不得以任何理由改寫、取代或簡化以上文件。

---

## 2. 為什麼需要流程定錨文件

在 TAITS 專案中：

- AI 對話不具治理效力  
- 不同對話必然產生不同流程敘述方式  

若無流程定錨，將導致：

- 新對話反覆討論流程  
- 工程順序理解漂移  
- 無法清楚回答「目前做到哪」  

---

## 3. 工程流程定錨總覽（Phase 0–5）

> 注意：Phase 不是流程，只是工程落地順序說明  
> 合法性裁決一律回 Canonical（L1–L11）

| 工程 Phase | 對應 Canonical Layer | 工程定位一句話 |
|-----------|----------------------|----------------|
| Phase 0 | 前置（未進入 L 層） | 鎖定文件與版本 |
| Phase 1 | L1–L11（空殼） | 讓流程存在且能跑 |
| Phase 2 | L7 / L9 / L11 | 系統先會拒絕 |
| Phase 3 | L10 | 確立人類主權 |
| Phase 4 | L1–L6 | 補齊證據與 Regime |
| Phase 5 | L8 | 最後才接策略 |

---

## 4. Canonical × Engineering 對位表（固定）

| Canonical Layer | 名稱 | 工程 Phase |
|-----------------|------|-----------|
| L1 | Data Source | Phase 1 / Phase 4 |
| L2 | Normalization | Phase 1 / Phase 4 |
| L3 | Snapshot & State | Phase 1 / Phase 4 |
| L4 | Analysis | Phase 4 |
| L5 | Evidence | Phase 4 |
| L6 | Regime | Phase 4 |
| L7 | Risk & Compliance | Phase 2 |
| L8 | Strategy & Research | Phase 5 |
| L9 | Governance Gate | Phase 2 |
| L10 | Human Decision | Phase 3 |
| L11 | Execution & Control | Phase 2 |

---

## 5. Phase 0｜治理與版本基線（Mandatory）

### 目的

確保後續每一行程式碼，都能指回明確治理依據。

### 必須完成項目

- [ ] 確認 DOCUMENT_INDEX 中 ACTIVE 文件清單  
- [ ] 確認 GOVERNANCE_STATE = Freeze v1.0  
- [ ] 建立 doc_key → 檔案 → hash / version_date 對照  
- [ ] 標註治理文件為 read-only  
- [ ] 所有模組必須標註對應 Canonical Layer（Lx）

---

## 6. Phase 1｜Canonical Flow 空殼

### 對應 Canonical
- L1–L11（全部）

### 最低完成條件

每一層必須具備：

- 可接收上一層輸入  
- 可檢查是否有權執行  
- 可輸出標準事件（PASS / VETO / RETURN / STOP）  
- 具備 correlation_id / version_ref  

---

## 7. Phase 2｜硬 Gate 優先

### 對應 Canonical
- L7｜Risk & Compliance  
- L9｜Governance Gate  
- L11｜Execution & Control  

### 必須成立

- L7 輸出 PASS / VETO + reason codes  
- 僅 PASS 產生 Risk PASS Token  
- 無 Token → L11 必須 BLOCK  

---

## 8. Phase 3｜UI（人類主權）

### 對應 Canonical
- L10｜Human Decision  

### 最小需求

- 顯示 Risk 結果  
- 顯示 Regime 狀態  
- APPROVE / REJECT  
- 決策 trace / log  

---

## 9. Phase 4｜資料 → Evidence → Regime

### 對應 Canonical
- L1–L6  

### 必須成立

- 資料可追溯  
- Snapshot 可回放  
- Evidence Bundle 完整  
- Regime 可標註可 / 不可交易  

---

## 10. Phase 5｜策略宇宙接線

### 對應 Canonical
- L8｜Strategy & Research  

### 策略模組限制

- 僅輸出 Proposal / Scenario  
- 不得直連 L11  
- 不得覆寫風控  

---

## 11. 目前工程狀態標示（手動維護）

```text
Current Phase        : Phase 0
Completed Phases     : Phase 0
Next Target Phase    : Phase 1
Last Review Date     : YYYY-MM-DD
12. Commit 前自我檢查
屬於哪一個 Phase

對應哪一個 Canonical Layer

文件是否能證明其合法性

13. 最終定錨語
TAITS 的流程由 L1–L11 裁決；
Phase 0–5 只是工程上如何把流程做出來的說明。

14. 新對話標準開場語
以下對話請以
TAITS_程式開發流程定錨文件.md
作為唯一工程流程定錨文件。
