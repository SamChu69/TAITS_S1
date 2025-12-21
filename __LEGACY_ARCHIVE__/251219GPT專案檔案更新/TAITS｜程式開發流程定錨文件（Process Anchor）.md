# 📌 TAITS｜程式開發流程定錨文件（Process Anchor）

**文件定位**：工程流程定錨（Read-Only / Non-Governance）  
**適用範圍**：TAITS 全部開發活動（Research / Backtest / Simulation / Paper / Live）  
**治理狀態**：Freeze v1.0  
**最後更新**：YYYY-MM-DD（手動填寫）

---

## 一、裁決性聲明（必讀）

本文件之定位與權限如下：

- **唯一具有治理裁決力的流程定義**：
  - `MASTER_CANON`（L1–L11）
  - `ARCH_FLOW`
- 本文件 **不具治理效力**
- 本文件 **不新增、不修改任何制度**
- 本文件之唯一用途為：
  > **作為 TAITS 工程開發時的「流程定位錨點」**

若本文件與任何 Canonical 文件出現理解衝突：

> **一律以 MASTER_CANON / ARCH_FLOW 為最終裁決依據**

---

## 二、為什麼需要「流程定錨文件」

在 TAITS 專案中：

- AI 對話不具治理效力  
- 不同對話可能出現不同流程敘述方式  

若無流程定錨，將導致：

- 新對話反覆討論流程
- 工程順序理解漂移
- 無法明確回答「目前做到哪」

**本文件的存在目的**：

> **不管換多少新對話、新 AI，  
所有討論只能在同一個流程座標系中進行。**

---

## 三、流程定錨的核心原則

### 1️⃣ 流程裁決只有一條

- Canonical Flow：**L1–L11**
- 工程流程不得覆蓋 Canonical

### 2️⃣ Phase 僅為工程敘述

- Phase 0–5 只是回答：
  >「工程現在進行到哪一段」
- Phase **不具 PASS / VETO / 裁決權**

### 3️⃣ 所有工程行為必須能被定位

每一行程式碼，都必須回答：

1. 屬於哪一個 **Phase**
2. 對應哪一個 **Canonical Layer（Lx）**
3. 能否指回對應治理文件

---

## 四、Canonical × Engineering 對位定錨

### 4.1 Canonical Layer × Phase 對照（固定）

| Canonical Layer | 名稱 | 對應 Phase |
|-----------------|------|-----------|
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

> 📌 本對位表僅為工程理解使用，不構成流程裁決。

---

## 五、工程 Phase 定義（定錨版）

### Phase 0｜治理與版本鎖定（Pre-Development Lock）

- **性質**：治理前置，不屬於任何 L 層
- **目的**：確保後續所有開發不越權

包含但不限於：
- DOCUMENT_INDEX 鎖定
- Freeze v1.0 確認
- doc_key / version_ref / hash 固定

---

### Phase 1｜資料與狀態骨架（L1–L3）

- 只處理資料、正規化、狀態
- 不得出現任何分析、策略、交易語義

---

### Phase 2｜分析到證據（L4–L5）

- 只允許描述性分析
- 所有輸出必須可被質疑、可回放
- 不得產生方向、訊號、績效語義

---

### Phase 3｜Regime 與 Risk（L6–L7）

- 系統必須能「拒絕交易」
- Risk 僅輸出 PASS / VETO
- VETO 不可被覆寫

---

### Phase 4｜策略提案與治理檢查（L8–L9）

- 策略僅為 Proposal / Scenario
- 不得產生任何實際行為
- Governance Gate 可 RETURN / STOP

---

### Phase 5｜人類裁決與執行（L10–L11）

- UI 為唯一 APPROVE / REJECT 入口
- 無 Risk PASS Token → Execution 必須 BLOCK
- Execution 全程可審計、可中止

---

## 六、目前工程狀態標示（非常重要）

> 🔒 **此區為流程定錨的「狀態座標」**

請由專案負責人手動維護：

```text
Current Phase        : Phase 0
Completed Phases     : Phase 0
Next Target Phase    : Phase 1（L1–L3 Data / State Skeleton）
Blocked Layers       : L4–L11（依法不可實作）
Last Review Date     : YYYY-MM-DD
七、正確使用方式（新對話必遵守）
未來任何新對話，只允許以下提問方式：

「在此流程定錨下，我們現在要完成 Phase X 的哪些 Layer？」

「目前 Phase 是否可以進入下一階段？」

「這段實作是否越權觸碰到尚未開放的 Layer？」

不允許再討論：

哪個流程比較好

是否要改流程

是否換一種流程說法

八、最終定錨語（可引用）
TAITS 的流程不會因對話而改變，
只會因治理文件而裁決。
本文件的存在，是為了讓所有人站在同一個位置開發。
