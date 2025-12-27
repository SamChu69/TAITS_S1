# TAITS｜GPT 新對話續編編輯 SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228_FINAL

> 文件定位：GPT Project Editing Runbook / SOP（給「只用 ChatGPT 專案」也能長期續編的操作手冊）  
> 文件屬性：SUPPORT / Non-Governance（工程/操作支援文件；**不具治理裁決效力**）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
> 版本日期：2025-12-28  
> 核心目的：讓你每次「開新對話」都能**可靠續編**，不依賴對話記憶；並確保每次輸出都符合 TAITS 最新 AI 制度（Index Gate / 引用最小格式 / Only-Add）。  

---

## 0. 你必須先知道的事（小白也能懂的版本）

### 0.1 為什麼你會「開新對話就接不上」
因為 ChatGPT 的「新對話」**不會自動帶入上一個對話的上下文**。  
TAITS 在 Freeze v1.0 下要求：**不得用猜測補完、不得靠回憶裁決**，你必須用「可稽核、可回放」的方式把上下文放回來。

### 0.2 續編的唯一正道：把上下文放回「檔案」
你每次工作都要把三個東西寫進專案檔案中（只增不減）：

1) **Worklog（進度唯一事實來源）**：你做到哪、下一步是什麼  
2) **ECR（本次變更紀錄）**：你這次到底加了什麼、加在哪  
3) **Evidence（證據鏈/快照）**：讓任何人都能重現你說的結論（如需）

> 只要「檔案」存在，新對話只要讀檔就能 100% 續編；你不用靠記憶，也不怕換對話。

---

## 1. TAITS 最新制度下，你的新對話「必做啟動」是什麼

### 1.1 Index Gate First（唯一裁決來源）
- **ACTIVE 文件集合 / doc_key 合法性 / 治理等級 / 版本有效性**：一律以 DOCUMENT_INDEX 的 Authoritative Index 表格裁決為準。【359:2†TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md†L12-L22】【359:0†TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228M_FINAL.md†L13-L16】
- **不在 DOCUMENT_INDEX 表內＝不具治理效力**（不得拿來當依據）。【359:0†TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228M_FINAL.md†L13-L16】

### 1.2 Minimum Load Set（任何新對話開工前最少要指向 5 份）
你每次開新對話，**在進入任何工作前**，至少要能指向（含版本日期與章節定位）：
1) AI_GOV  
2) DOCUMENT_INDEX  
3) MASTER_ARCH  
4) MASTER_CANON  
5) GOVERNANCE_STATE（Freeze v1.0）  
【359:7†TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md†L5-L13】【359:14†TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md†L12-L22】

> 注意：ACTIVE 清單**不得固化**；任何「文件數量/清單」只能視為快照，裁決仍回 DOCUMENT_INDEX。【359:7†TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md†L15-L22】【359:9†TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md†L16-L27】

### 1.3 最小引用格式（缺一欄位＝未引用＝不得裁決）
任何「依據某文件」的主張，都必須至少包含：
- ref_file（完整檔名）
- ref_doc_key
- ref_version_date
- ref_section
- audit_anchor（對應 VERSION_AUDIT 的稽核錨點；新手可先用既定 placeholder）
缺任一欄位 → 一律視為「未引用」→ 不得裁決性輸出。【359:14†TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md†L26-L38】

---

## 2. GPT 專案續編的「最佳做法」：用「分階段 × 分工作包」切新對話

你問：「要不要分階段分新對話？」  
答案是：**要，但不是隨便分；要用固定規則分**，避免你越做越亂。

### 2.1 最推薦的分法（小白最穩）
- **一個新對話 = 一個工作包（Work Package）**
- 工作包的定義：只做「一件明確輸出」，例如：
  - 只針對某個 doc_key 做一次 Only-Add 增補（新增一段、附插入位置）
  - 只做 Phase 0 盤點報告（只報告、不修改）
  - 只做某個 Gate 的檢核與缺口清單（RETURN items）

這樣做的好處：
- 對話不會太長、上下文不會漂移
- 你每次都能把成果落盤成檔案（Worklog/ECR）
- 新對話只要讀最新檔案就能接續

### 2.2 什麼時候「必須」開新對話（硬規則）
只要遇到任一條，建議直接開新對話：
1) 你要換目標 doc_key（從 A 文件改到 B 文件）  
2) 你要換 Canonical Layer（從 Lx 轉到 Ly）  
3) 你從「盤點/審視」切換到「實際 Only-Add 編輯」  
4) 你要進入 Review Gate / 衝突裁決議題（需要更乾淨的上下文）  
5) 你發現前面對話引用欄位缺漏（需要重來做合規引用）

---

## 3. 小白可直接照抄的「新對話續編」操作步驟（GPT 專案）

> 你不需要懂制度細節；照流程做就不會出錯。

### Step 1｜先在專案檔案裡準備 3 個「續航檔」
如果你的專案目前還沒有，請新增（Only-Add）這三個檔案（名稱可依 repo 慣例，但建議固定）：

- `TAITS_GPT_WORKLOG.md`（進度唯一事實來源；每次工作完要更新）
- `TAITS_GPT_ECR_LEDGER.md`（ECR 清單；每次工作包新增一條）
- `TAITS_GPT_CONTEXT_PACK.md`（新對話要貼的「續編包」模板與最新狀態快照）

> 這三個是「GPT 版 Worklog/ECR」：不用寫程式也能維持工程級可追溯。

### Step 2｜每次開新對話：先貼「啟動確認＋引用標頭」
你在新對話第一則訊息，貼下面這段（照貼即可）。

```text
TAITS 架構已完整載入，我已準備好在此基礎上繼續開發。
已進入嚴格對齊模式（Freeze v1.0 / Only-Add / Index Gate First）。

【任務類型】（三選一）
A) 盤點/審視（Report-only：只報告不修改）
B) Only-Add 編輯（只新增，不刪減、不覆寫）
C) Gate 檢核（PASS/BLOCK/RETURN 缺口清單）

〔TAITS 新手引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228M_FINAL.md
ref_doc_key = DOCUMENT_INDEX
ref_version_date = 2025-12-20
ref_section = <你要引用的章節，例如：§5 Authoritative Index>
ref_notes = 新對話啟動 / ACTIVE 裁決依據
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0013
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 新手引用標頭〕

〔TAITS 新手引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md
ref_doc_key = PROJECT_PROMPT
ref_version_date = 2025-12-20
ref_section = A1（Minimum Load Set）/ A2（最小引用格式）
ref_notes = 新對話載入規格
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0007
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 新手引用標頭〕

〔TAITS 新手引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228K_FINAL.md
ref_doc_key = GOVERNANCE_STATE_FREEZE_V1
ref_version_date = 2025-12-20
ref_section = 1.1（Current State）/ 1.2（Meaning）
ref_notes = Freeze v1.0 生效
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0016
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 新手引用標頭〕

【續編狀態】
- 上一次工作包：ECR-YYYYMMDD-####（貼你的上一筆）
- 上一次目標：doc_key=<某文件> / 插入位置=<某章節末>
- 本次目標：doc_key=<某文件> / 只新增一段 / 不修改其他內容
- 你要我輸出：<完整可貼上的 md 段落 + 插入位置說明 + ECR 條目>
```

> 以上模板的引用標頭欄位與「缺一視為未引用」的規則，必須遵守。【359:3†TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md†L1-L20】

### Step 3｜把「上一個工作包的結果」放回檔案（不靠記憶）
你每次工作包完成後，做 2 件事就好：

1) 更新 `TAITS_GPT_WORKLOG.md`（只追加一條最新狀態）
2) 把本次輸出內容貼回你正在維護的治理檔（Only-Add；插入到指定章節末或 Addendum 區）

> 只要你有做這一步，新對話不會斷線。

### Step 4｜你要切新對話時，先把「續編包」更新
在 `TAITS_GPT_CONTEXT_PACK.md` 末尾追加一段「最新續編包」：
- 本次完成的 doc_key / 插入位置
- 最新 ECR 編號
- 有無 CR（若涉及版本治理）
- 下一步要做什麼（下一個工作包）

---

## 4. 你應該怎麼問我（GPT）才會穩定拿到可用輸出

你是小白，所以你只需要用固定句型問我；不要臨時發明新問法。

### 4.1 盤點/審視（Report-only）句型
```text
嚴格對齊模式。
請只做盤點報告，不做任何修改。
目標：<doc_key 或 文件群>
輸出：差異清單 / 風險點 / 需補的 Only-Add 段落建議（但不實際寫入原文）。
```

### 4.2 Only-Add 編輯（最常用）句型
```text
嚴格對齊模式。
Phase = <0~5 或 Unknown>
doc_key = <目標文件>
編輯範圍 = <哪個章節末 / Addendum 區>
目的 = <你要補什麼>
硬限制：Only-Add，不得刪減／覆寫／偷換語義。
輸出：1) 可直接貼上的新增段落（md） 2) 插入位置說明 3) ECR 條目（摘要＋引用標頭）
```

### 4.3 Gate 檢核（PASS/BLOCK/RETURN）句型
```text
嚴格對齊模式。
請對下列輸出做 Gate 檢核（Index Gate / 引用欄位 / Only-Add）。
輸出只允許：PASS / RETURN(缺口清單) / BLOCK(原因碼)。
```

---

## 5. 最重要的「不踩雷」清單（小白必看）

### 5.1 Freeze v1.0 下，什麼事一定不能做
- 不能覆寫 ACTIVE 版本的語義；若要改，只能走新版本上線流程。【359:10†TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL.md†L1-L5】
- 不能用 README 或任何快照清單裁決 ACTIVE；一律回 DOCUMENT_INDEX。【359:9†TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md†L16-L27】【359:7†TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md†L15-L22】
- 不能缺引用欄位就讓我做裁決性輸出（缺欄位＝未引用）。【359:14†TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md†L26-L38】

### 5.2 你最常遇到的問題與立即修正
- **問題：我忘了上次做到哪**  
  修正：回去看 `TAITS_GPT_WORKLOG.md` 最後一條（它是唯一事實來源）。

- **問題：我不確定哪些文件是 ACTIVE**  
  修正：不要猜，請我「只做 Phase 0 盤點」並引用 DOCUMENT_INDEX 的 Authoritative Index。

- **問題：對話很長，我怕你讀不完**  
  修正：立刻切新對話，帶上「續編包」（引用標頭＋Worklog 最新條目＋本次目標）。

---

## 6. 建議你用的「工作節奏」（每天照做即可）

### 6.1 每天只做一個工作包（最穩）
- 今天只做：某個 doc_key 的一段 Only-Add 增補  
- 完成後更新 Worklog/ECR  
- 明天再做下一個 doc_key 或下一段

### 6.2 Phase 的使用方式（你不必一次理解全部）
- **Phase 0**：盤點與對齊（只報告、不修改）  
- **Phase 1~5**：當你要進入工程落地或更細的系統拆解時再用  
如果你現在主要在「治理文件體系」上做補強，通常先以 Phase 0/Only-Add 編輯為主即可。

---

## Appendix A｜TAITS_GPT_WORKLOG.md（最小模板）
```markdown
# TAITS_GPT_WORKLOG（唯一進度事實來源）

## 最新狀態（只更新這段）
- last_updated: <YYYY-MM-DD HH:MM>
- governance_state: FREEZE_V1
- active_index_ref: DOCUMENT_INDEX:<version_date>
- last_work_package: ECR-YYYYMMDD-####
- last_doc_key: <doc_key>
- last_insert_point: <章節/段落路徑>
- next_work_package: <你下一步要做的事>

## 歷史條目（只追加，不覆寫）
- <YYYY-MM-DD> | ECR-... | doc_key=... | insert=... | output=<檔名/段落標題>
```

## Appendix B｜TAITS_GPT_CONTEXT_PACK.md（續編包模板）
```markdown
# TAITS_GPT_CONTEXT_PACK（新對話必貼）

## 最新續編包（複製貼到新對話第一則訊息）
- governance_state: FREEZE_V1
- minimum_load_set: AI_GOV / DOCUMENT_INDEX / MASTER_ARCH / MASTER_CANON / GOVERNANCE_STATE
- last_work_package: ECR-...
- last_doc_key: ...
- last_insert_point: ...
- this_goal: ...
- output_required: ...
```

---

（END）
