# TAITS｜專案檔案更新包（Only-Add Migration Pack：合併入口×不刪檔）__ADDENDUM_20251228_FINAL

> 文件定位：Project File Update Pack（給你「更新專案檔案」用的貼上包）  
> 文件屬性：SUPPORT / Non-Governance（工程/操作支援；不具治理裁決效力）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
> 版本日期：2025-12-28  
> 核心原則：**只新增，不刪除，不覆寫，不偷換語義**；以「入口合併」達到你想要的「檔案變少、只看一份」效果。  

---

## 0. 你要達成的結果（你說的「更新專案檔案」= 這三件事）

1) 你日常只需要看 **一份入口文件**：  
   - `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`

2) 既有 SOP/錨定檔不刪不改語義，但**加上「已併入合併版」的導流段**（避免你或未來的你走錯文件）。

3) 專案入口（README / Unified Process Anchor）用 Only-Add 加上「從此以合併版為入口」的指引段。

---

## 1. 你要放進專案的「唯一入口文件」

### 1.1 請確保專案已包含下列檔案（若已有可跳過）
- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`

> 之後日常你只看這一份就夠。

---

## 2. 更新入口文件：README（Only-Add 貼上段）

### 2.1 目標檔案
- `TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md`

### 2.2 插入位置（Only-Add）
建議插在 README 的「新手開始/操作方式/如何開新對話」段落**末尾**（或文件最末尾新增「附錄：工程操作入口」章）。

### 2.3 可直接貼上的新增段落（複製貼上即可）
```markdown
---

## 【Only-Add｜新增】工程操作入口（合併版總手冊）

> 本段為 Freeze v1.0（Only-Add）下之「工程操作導流」新增段落，不改寫任何治理文件語義。  
> 本段目的：降低新手閱讀負擔，避免多份 SOP 分散導致流程漂移。

### 日常唯一入口（建議）
從即日起，日常操作（GPT 新對話續編 + Cursor 工程落地 + 雙錨使用）請以以下文件為主：

- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`

### 重要限制（避免誤用）
- 本合併版總手冊屬 SUPPORT（工程/操作支援），不具治理裁決效力。  
- 任何 ACTIVE / doc_key / 版本有效性 / 覆蓋序之裁決，一律回到 `DOCUMENT_INDEX → MASTER_ARCH → AI_GOV`。
```

---

## 3. 更新主流程錨點：Unified Process Anchor（Only-Add 貼上段）

### 3.1 目標檔案（擇一）
- 若你專案使用「主檔」：`TAITS｜程式開發流程定錨文件（Unified Process Anchor）.md`
- 若你專案以「更新版」為準：`TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md`

> 建議：你用哪個當入口，就更新哪個（只要一個入口即可）。

### 3.2 插入位置（Only-Add）
建議插在「如何開新對話 / 如何對齊 / 本文件用途」段落**末尾**，或文件最末尾新增「附錄：日常操作入口」章。

### 3.3 可直接貼上的新增段落
```markdown
---

## 【Only-Add｜新增】日常操作入口（合併版總手冊）

> 本段為 Freeze v1.0（Only-Add）下之導流新增段落，不取代本文件作為「主流程骨架」之定位。  
> 本段目的：把「實作細節」集中到合併版，避免多份 SOP 分散造成流程漂移。

### 合併版總手冊（建議作為日常唯一入口）
- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`

### 本文件與合併版的分工（不可互相取代）
- 本文件（PROCESS_ANCHOR / Unified Process Anchor）：負責「工程節點與對話一致性（主流程骨架）」  
- 合併版總手冊：負責「GPT 新對話續編 + Cursor 任務切片 + 證據鏈與 Gate 落盤」之可操作細節
```

---

## 4. 更新既有 SOP 檔：加上「已併入合併版」導流段（Only-Add）

> 你說檔案太多要合併：最安全的做法是「不刪檔」，而是在舊檔最前/最後新增一段導流，避免你以後看錯檔。  
> 下列導流段，建議貼在每份文件的「最上方（標題後）」或「最末尾」。

---

### 4.1 目標檔案 A（Cursor）
- `TAITS｜Cursor工程落地SOP（雙錨整合：PROCESS_ANCHOR×工程轉譯錨定）__ADDENDUM_20251228_FINAL.md`

**新增導流段（貼在文件最前或最末）**
```markdown
---

## 【Only-Add｜新增】導流聲明（合併版入口）

本文件內容已納入下列「合併版總手冊」作為日常唯一入口；本文件仍保留作歷史快照與追溯參考（Freeze v1.0：Only-Add，不刪檔不覆寫）。

- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`

> 注意：本文件屬 SUPPORT（工程支援），不具治理裁決效力；裁決一律回 `DOCUMENT_INDEX → MASTER_ARCH → AI_GOV`。
```

---

### 4.2 目標檔案 B（GPT）
- `TAITS｜GPT新對話續編編輯SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228_FINAL.md`
- 或你最新修訂版：`TAITS｜GPT新對話續編編輯SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228R_FINAL.md`

**新增導流段**
```markdown
---

## 【Only-Add｜新增】導流聲明（合併版入口）

本文件內容已納入下列「合併版總手冊」作為日常唯一入口；本文件仍保留作歷史快照與追溯參考（Freeze v1.0：Only-Add，不刪檔不覆寫）。

- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`
```

---

### 4.3 目標檔案 C（工程落地拆解錨定）
- `TAITS｜工程落地拆解流程錨定（L1–L11×工程支撐）__ADDENDUM_20251228_FINAL.md`

**新增導流段**
```markdown
---

## 【Only-Add｜新增】導流聲明（合併版入口）

本文件內容已納入下列「合併版總手冊」作為日常唯一入口；本文件仍保留作歷史快照與追溯參考（Freeze v1.0：Only-Add，不刪檔不覆寫）。

- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`
```

---

## 5. 最終你會得到什麼（你要的「檔案變少」實務效果）

- 你日常只需要看：**合併版總手冊**
- README / Unified Process Anchor 會指向合併版（新手入口一致）
- 舊文件不刪除、不覆寫，只加「導流段」讓你不會走錯
- 完全符合 Freeze v1.0（Only-Add）與「不取代既有語義」要求

---

## 6. 小白執行清單（照打勾就完成更新）

- [ ] 把合併版總手冊放進專案檔案池  
- [ ] 在 README 末尾貼上第 2 節新增段落  
- [ ] 在 Unified Process Anchor 末尾貼上第 3 節新增段落  
- [ ] 在三份舊 SOP/錨定檔貼上第 4 節導流段（可選但強烈建議）  
- [ ] 從此你只用合併版工作；舊檔只做追溯參考

---

（END）
