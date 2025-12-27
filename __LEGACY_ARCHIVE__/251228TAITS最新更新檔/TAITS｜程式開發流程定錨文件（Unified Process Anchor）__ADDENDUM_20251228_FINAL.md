# TAITS｜程式開發流程定錨文件（Unified Process Anchor）

文件類型：Engineering Process Anchor（Read-Only / Non-Governance）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
治理狀態：Freeze v1.0  
最後更新：2025-01-XX  

---

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


---

# 【Only-Add｜新增】日常操作入口（合併版總手冊）

> 新增日期：2025-12-28  
> 生效前提：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
> 本段為「導流/入口」用途之新增內容：**不取代、不覆寫**本文件既有語義；僅提供新手與日常使用的單一入口，以降低多文件分散造成的流程漂移。

## 1) 日常唯一入口（建議）
從即日起，日常操作（包含：GPT 開新對話續編、Cursor 工程落地、雙錨使用、證據鏈與 Gate 落盤）建議以以下文件作為**唯一入口**：

- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`

## 2) 分工聲明（不可互相取代）
- 本文件（Unified Process Anchor）：維持「主流程骨架」定位，用於固定工程節點、固定新對話/新任務的定位語言、固定進度座標。
- 合併版總手冊：提供「可操作細節」與「新手照做流程」，包含 GPT 續編三件套（Worklog/Ledger/Context Pack）與 Cursor 單層落地（Minimum Deliverables、Gate logs、Trace/Evidence）。

## 3) 使用限制（避免誤用）
- 合併版總手冊屬 SUPPORT（工程/操作支援），不具治理裁決效力。  
- 任何涉及 ACTIVE / doc_key / 版本有效性 / 覆蓋序的裁決，一律回到 `DOCUMENT_INDEX → MASTER_ARCH → AI_GOV` 的裁決序。

---

# 【Only-Add｜新增】Cursor 工程落地（雙錨整合）參考入口

> 本段提供 Cursor 工程落地的直接參考入口；不改寫本文件原有流程節點語義。

- `TAITS｜Cursor工程落地SOP（雙錨整合：PROCESS_ANCHOR×工程轉譯錨定）__ADDENDUM_20251228_FINAL.md`
- `TAITS｜工程落地拆解流程錨定（L1–L11×工程支撐）__ADDENDUM_20251228_FINAL.md`

（END OF ONLY-ADD APPENDIX）
