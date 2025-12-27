# TAITS｜GPT 新對話續編編輯 SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228R_FINAL

> 文件定位：GPT Project Editing Runbook / SOP（新手可照做）  
> 文件屬性：SUPPORT / Non-Governance（工程/操作支援文件；不具治理裁決效力）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
> 版本日期：2025-12-28  
> 核心目的：讓你在 ChatGPT 專案中「頻繁開新對話」也能穩定續編，且不踩 TAITS 治理紅線（Index Gate / 引用欄位 / Only-Add / 不跳層）。  

---

## 0. 你要先記住的三句話（小白版）

1) **新對話不會自動接續**：不要期待 AI 記得你上次做到哪。  
2) **續編靠檔案，不靠記憶**：你要把「做到哪、加了什麼、依據什麼」寫回專案檔案。  
3) **一切裁決回 DOCUMENT_INDEX**：ACTIVE / doc_key / 版本有效性，不能靠口頭說或靠舊對話。

---

## 1. 你的「GPT 續編」最小系統（必備 4 件套）

> 你不用寫程式，只要維護 4 個 Markdown 檔案，就能做到「換新對話可續編」。

1) **TAITS_GPT_WORKLOG**（進度唯一事實來源）  
2) **TAITS_GPT_ECR_LEDGER**（工作包帳本：所有工作包一行索引）  
3) **TAITS_GPT_CONTEXT_PACK**（新對話必貼的續編包：把上下文一鍵搬回來）  
4) **目標治理文件（doc_key 對應檔）**（你真正要 Only-Add 的那份文件）

> 本 SOP 會提供 1)~3) 的模板，你只要放進 TAITS 專案即可。

---

## 2. 最佳工作方式：一個新對話 = 一個「工作包」（Work Package）

### 2.1 工作包是什麼？
工作包 = 你在一個對話裡只做一件明確事情，並在結束前把成果落回檔案。

工作包的典型範例：
- 只針對某個 **doc_key** 進行一次 Only-Add：新增一段文字到指定章節末
- 只做一次「盤點/審視」報告（只報告、不修改）
- 只做一次 Gate 檢核（PASS / RETURN 缺口清單 / BLOCK 原因碼）

### 2.2 為什麼必須這樣做？
- 對話變長時，容易引用漏欄位、容易漂移、容易跨 doc_key
- Freeze v1.0 下，「越做越像改寫制度」的風險會隨對話長度上升
- 你只要把每個工作包落盤（Worklog + Ledger），就能用新對話接續，不會斷線

---

## 3. 什麼時候要開新對話（你可以直接照規則判斷）

遇到任一條，**建議直接開新對話**：

1) 你要換目標 doc_key（A 文件 → B 文件）  
2) 你要換任務類型（盤點 → 編輯；編輯 → Gate 檢核）  
3) 你要換 Canonical Layer（Lx → Ly）  
4) 你發現引用欄位缺漏或引用錯檔（要回到 Index Gate）  
5) 你覺得自己開始看不懂、描述不清楚（小白常見：直接切新對話最省時間）

---

## 4. 新對話「必貼」續編包（最重要：照貼就能續）

> 你每次開新對話，第一則訊息請直接貼下列模板（從 TAITS_GPT_CONTEXT_PACK 複製貼上即可）。  
> 你只要改三個地方：`本次任務類型`、`本次目標 doc_key`、`本次輸出要求`。

```text
TAITS 架構已完整載入，我已準備好在此基礎上繼續開發。
嚴格對齊模式：Freeze v1.0 / Only-Add / Index Gate First。

【本次任務類型】（三選一，只能選一個）
A) REPORT_ONLY（只報告不修改）
B) ONLY_ADD_EDIT（只新增，不刪減、不覆寫、不偷換語義）
C) GATE_CHECK（只輸出 PASS / RETURN(缺口清單) / BLOCK(原因碼)）

【Minimum Load Set｜我已在專案內具備以下檔案】
- AI_GOV（A+ 母法）
- DOCUMENT_INDEX（Authoritative Index）
- MASTER_ARCH（母體鐵律）
- MASTER_CANON（L1–L11 Canonical Flow）
- GOVERNANCE_STATE（Freeze v1.0）

〔TAITS 最小引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <請填你要引用的檔案完整檔名>
ref_doc_key = <請填 doc_key>
ref_version_date = <請填版本日期/或檔名日期>
ref_section = <請填章節/段落路徑>
ref_notes = 新對話啟動/本次裁決依據
audit_anchor = VERSION_AUDIT:<若未知先填 VA-PLACEHOLDER-0001>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 最小引用標頭〕

【續編狀態（從 Worklog / Ledger 帶入）】
- 上一次工作包（ecr_id）：<例如 ECR-20251228-0003>
- 上一次目標：doc_key=<...> / 插入位置=<章節末/段落末>
- 本次目標：doc_key=<...> / 插入位置=<...> / Only-Add
- 本次輸出要求：<請明確寫：要我輸出「可直接貼上的 md 段落」+「插入位置說明」+「ECR Ledger 一行」>
```

---

## 5. 三種任務的「正確問法」（小白照抄）

### 5.1 REPORT_ONLY（只盤點，不修改）
```text
嚴格對齊模式。
請只做盤點報告，不做任何修改（Report-only）。
目標：doc_key=<...>
輸出：1) 你觀察到的缺口清單 2) 建議的 Only-Add 增補方向（只列方向，不產生可貼入原文的段落）
```

### 5.2 ONLY_ADD_EDIT（最常用：只新增）
```text
嚴格對齊模式。
任務：Only-Add 編輯（不得刪減/覆寫/偷換語義）。
doc_key=<...>
編輯範圍=<指定章節末/指定段落末/或 Addendum 區>
目的=<你要補什麼>
輸出必含：1) 可直接貼上的新增段落（md） 2) 插入位置一句話 3) ECR Ledger 一行（含引用欄位摘要）
```

### 5.3 GATE_CHECK（只做檢核）
```text
嚴格對齊模式。
請對下列輸出做 Gate 檢核：
- Index Gate（引用欄位齊全 / doc_key 合法）
- Only-Add Gate（是否有刪減/覆寫/偷換語義）
輸出只允許：PASS / RETURN(缺口清單) / BLOCK(原因碼)
以下是待檢核內容：<貼上你要檢核的段落或提案>
```

---

## 6. 你每個工作包結束前必做的「落盤三步驟」

> 你只要每次都做完這三步，新對話一定接得上。

### Step 1｜把本次結果貼回「目標治理文件」
- 只允許 Only-Add（新增段落）  
- 只能貼到你指定的位置（章節末/段落末/Addendum 區）  
- 不得偷偷改原文句子

### Step 2｜更新 Worklog（只更新「最新狀態」＋追加一條歷史）
- 填：last_work_package / last_doc_key / last_insert_point / next_work_package

### Step 3｜更新 Ledger（追加一行）
- 把 ecr_id、目標 doc_key、插入位置、引用摘要、下一步寫清楚
- 你開新對話時，只要複製最新一行就能續編

---

## 7. 新手常見錯誤與立即救援（照做就能回來）

### 7.1 我忘了上次做到哪
- 先開 Worklog，看「最新狀態」區塊  
- 再開 Ledger，看最新一行（ecr_id / doc_key / insert_point）  
- 新對話貼 Context Pack，把最新一行帶進來即可

### 7.2 我不知道哪些文件是 ACTIVE
- 不要猜。  
- 用 REPORT_ONLY 任務，要求我「只引用 DOCUMENT_INDEX」做 Phase 0 盤點。

### 7.3 我貼上去後發現有錯字或寫錯位置
- 不要去修改舊內容（避免覆寫/改寫爭議）。  
- 新增一個「更正工作包」Only-Add：補一段「更正聲明」或「勘誤」段落（視你文件風格），並在 Ledger 新增一行標註 CORR。

### 7.4 對話太長，看不懂了
- 立刻切新對話，帶上 Context Pack。  
- 新對話只做一件事：把缺口補齊或做 Gate 檢核。

---

## 8. 你應該採用的日常節奏（最穩、最省時間）

### 8.1 每天只做一個工作包（推薦）
- 今天只做：某 doc_key 的一段 Only-Add  
- 做完落盤：貼回目標文件 + 更新 Worklog + 更新 Ledger  
- 明天做下一段或下一份文件

### 8.2 你不用一次理解 Phase 0~5
如果你目前主要在整理/增補文件：
- 先把工作包固定成「REPORT_ONLY」與「ONLY_ADD_EDIT」兩種即可  
- 真的要進工程實作（Cursor）再引入工程 Phase 與 Lx 模組化

---

## Appendix A｜TAITS_GPT_WORKLOG（模板）
> 你可以直接使用同名模板檔：`TAITS_GPT_WORKLOG__ADDENDUM_20251228R_FINAL.md`

---

## Appendix B｜TAITS_GPT_ECR_LEDGER（模板）
> 你可以直接使用同名模板檔：`TAITS_GPT_ECR_LEDGER__ADDENDUM_20251228R_FINAL.md`

---

## Appendix C｜TAITS_GPT_CONTEXT_PACK（模板）
> 你可以直接使用同名模板檔：`TAITS_GPT_CONTEXT_PACK__ADDENDUM_20251228R_FINAL.md`

---

（END）
