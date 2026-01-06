# TAITS｜程式開發流程定錨文件（Unified Process Anchor）

- doc_key：PROCESS_ANCHOR  
- 基線日期：2026-01-06（Asia/Taipei）  
- 覆蓋輸出：單一正確正文版／最終覆蓋版（FINALQA）  
- 去混讀狀態：已收斂（正文不含 Addendum／Appendix／Freeze 補丁語句；留痕僅於檔尾稽核區塊）  
- 強制定錨：Regime／Risk／Compliance 高於策略；L9=投資報告；L10=人類裁決；L11=全層稽核回放（非下單層）  
- 治理裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  

---
> 文件層級：C（工程支援／操作定錨；不具治理裁決力）  
> doc_key：PROCESS_ANCHOR  
> 版本日期：2026-01-06（Asia/Taipei）  
> 版本狀態：FINAL QA 覆蓋輸出（單一正確正文版／最終覆蓋版）  
> 去混讀要求：本文件正文不得改寫治理母法；若與治理文件衝突，仍以 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV 為最終裁決序位。

---

## 0. 文件定位（必讀）

本文件用於「工程開發流程」的**對話與工單定錨**，目的在於：

1. 讓你在 GPT／Cursor 的新對話中，始終以同一套工程節奏推進（避免每次對話流程漂移）。
2. 讓任何工程改動，都能用可追溯的方式落到 TAITS Canonical Flow（L1–L11）與工程 Phase（0–5）之上。
3. 讓「治理（Governance）」與「工程（Engineering）」分離：  
   - 治理文件負責裁決與約束（不可被本文件覆寫）。  
   - 工程流程負責產出可落地的程式與驗收物（依治理邊界運作）。

> 重要：本文件不是策略文件、不是投資建議文件，也不是用來變更治理條文的入口。

---

## 1. 使用範圍（Scope in Plain Language）

本文件適用於下列情境：

- 你要在 Cursor 內開始/持續開發 TAITS 程式碼（從 0 到落地）。
- 你要在 GPT 新對話中，要求我產出「可直接貼給 Cursor 的工單」或「可直接覆蓋的文件」。
- 你要進行 Final QA 前後的工程收斂（含版本基線、檔名口徑、稽核留痕規格）。

不適用於：

- 個股分析、回測、模擬、下單建議。
- 任何試圖以本文件覆寫治理裁決序位的需求。

---

## 2. 核心工程鐵律（Engineering Invariants）

1. 策略 ≠ 下單：策略輸出只能形成「可裁決的建議」，不得形成交易指令。
2. AI ≠ 決策主體：AI 只能提供分析、建議、整理、工單；交易授權唯一入口為 L10（人類裁決）。
3. Regime 高於策略：任何策略必須先受市場狀態（Regime/Context）約束。
4. Risk / Compliance 可否決一切：風險與合規可否決任何策略、任何執行、任何 UI 行為。
5. 去混讀：正文不得殘留補丁語句；所有留痕必須集中在「稽核區塊」或獨立稽核檔。
6. 單一現行：每份 doc_key 在 ACTIVE 集合中只能有「一個」現行覆蓋輸出版本。
7. 可追溯：每次交付必須含（Scope／Changelog／Hash Manifest／Audit Hand-off）。

---

## 3. 工程 Phase（0–5）與 Canonical Flow（L1–L11）對照

> 本表用於「我現在做到哪」的唯一工程定位方法。  
> 你只要說：「進入 Phase X」或「封板 Phase X」，我就以此表定錨產出工單與驗收項。

| 工程 Phase | 對應 Canonical Layer（L1–L11） | 工程輸出焦點 | 典型驗收點（最小集合） |
|---|---|---|---|
| Phase 0 | 前置（未進入 L 層） | 治理基線與版本鎖定 | ACTIVE=21 對齊、裁決序位一致、檔名口徑與基線日期一致 |
| Phase 1 | L1–L3 | Data Ingestion / Cleaning / Feature Base | 資料源契約、欄位定義、延遲/缺值策略、可重播（Replayable） |
| Phase 2 | L4–L6 | Signal / Model / Regime | 模型/訊號邊界清楚、Regime 先行、可解釋輸出（Explainable Output） |
| Phase 3 | L7–L8 | Portfolio / Risk / Compliance Gate | 風控與合規閘可否決、理由碼、降級策略（Degrade Mode） |
| Phase 4 | L9–L10 | Report + Human Decision | L9 報告含數據/圖形/條件式建議（非指令）；L10 具唯一授權流程 |
| Phase 5 | L11 | Audit / Playback / Ops | 全留痕可回放、變更可追溯、可稽核（Auditable） |

---

## 4. 新對話定錨：你應該怎麼開始一個工程對話

### 4.1 工程開發模式（Engineering Mode）啟動語（可直接貼）
```md
嚴格對齊模式｜ENGINEERING MODE（程式開發／落地工單／驗收定錨）

【對話目的（嚴格限定）】
本對話僅用於 TAITS 程式開發之工單產出、介面/資料契約定義、驗收規格、與落地步驟。
不進行任何個股分析、回測、模擬或投資建議。

【基線與裁決】
- ACTIVE=21 以 doc_key=DOCUMENT_INDEX 為準。
- 若有衝突：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV 為最終裁決序位。
- 去混讀：正文不得殘留補丁語句；留痕集中稽核區塊。

【開始指令】
我會貼上：Phase X、目標模組（或檔案/節點）、與要你輸出的交付物格式。
```

### 4.2 Final QA 模式（Final QA Mode）啟動語（可直接貼）
若你要做「文件最後檢視＋必要融合更新」，使用本專案既定的 FINAL QA MODE 開場白即可（以 DOCUMENT_INDEX 的基線為準）。

---

## 5. Cursor 工單輸出規格（你要我怎麼寫，Cursor 才能直接做）

### 5.1 工單必備欄位（不可少）
每一張工單（Ticket）至少包含：

- ticket_id：例如 `P2-L5-REGIME-001`
- phase：Phase 0–5
- target：模組/檔案/資料表/節點
- objective：一句話目標（可驗收）
- constraints：治理硬限制（例如 Only-Add、不可越權、去混讀）
- acceptance_criteria：可測、可驗收清單
- implementation_steps：可貼給 Cursor 的步驟（逐條）
- rollback_plan：若失敗如何回復
- audit_notes：需要留痕的關鍵點（理由碼、決策鏈、版本）

### 5.2 Cursor 指令風格（建議）
- 用「明確可執行」語句：新增/修改哪個檔、哪個函式、哪個介面。
- 避免抽象形容詞（例如「更好」、「更乾淨」），改成可測條件（例如「單元測試通過」、「lint 無 error」）。
- 每個改動都要指向其治理依據（doc_key + 章節）。

---

## 6. 交付與驗收（Definition of Done）

### 6.1 工程交付（對程式）
- 產出可執行的模組/節點（或最小可運行骨架）。
- 對外介面（API/Schema）有明確契約與版本。
- 有最小測試：單元測試/整合測試至少一種。
- 具備回放（Replay）能力：可以用同一份資料重現同一份輸出（同版本、同參數）。

### 6.2 文件交付（對治理/規範文件）
- 一次只處理一個檔案（除非你授權多檔同步）。
- 輸出「可直接覆蓋」完整 md 檔（不是差異片段）。
- 檔尾稽核區塊必含：Scope / Changelog / Hash Manifest / Audit Hand-off。
- 若取代正文內容：被取代者必須由稽核區塊（Archive）承接（不得遺失）。

---

## 7. 常見錯誤與防呆（Do-Not）

1. 把 L9 寫成「下單指令」：禁止。L9 只能是投資報告＋條件式建議（非指令）。
2. 把 L11 寫成「下單層」：禁止。L11 是全層留痕與回放層。
3. 在 B/C 文件宣告「跨文件一律以本檔為準」：禁止（除非明確限定適用範圍，且承接最終裁決序位）。
4. 在正文留下 Addendum/Appendix/Freeze 補丁語句：禁止。留痕只能進稽核區塊或稽核檔。
5. 用占位符（例如 TBD/…/{{hash}}）當作最終交付：禁止（Final QA 必須收斂）。

---

## 8. 你要我怎麼「一路帶你做完」：推薦節奏（最小擴散）

1. Phase 0：先鎖定 ACTIVE=21（DOCUMENT_INDEX），完成 Final QA。
2. Phase 1：先把資料源契約定義（DATA_SOURCES）與清洗/特徵基線落地。
3. Phase 2：先做 Regime/Context，避免策略先跑造成漂移。
4. Phase 3：把風控與合規閘門做成可否決、可追溯的可執行元件。
5. Phase 4：把 L9 報告格式與 L10 裁決模板固定，確保唯一交易授權入口。
6. Phase 5：把 L11 全留痕/回放做成日常可驗收的 SOP。

---

## 9. 附錄｜標準提問模板（可直接貼）

### 9.1 產出一張可貼給 Cursor 的工單
```md
Phase = {0-5}
target = {模組/檔案/節點}
objective = {一句話目標}
constraints = {治理限制}
交付格式：請輸出一張工單（含 ticket_id、acceptance_criteria、implementation_steps、rollback_plan、audit_notes）
```

### 9.2 要求我檢查「節點是否符合 Canonical Layer 邊界」
```md
Phase = {0-5}
我已在 Cursor 產生/修改節點：{節點名與檔案路徑}
請依 MASTER_CANON + ARCH_FLOW 的 Layer 邊界，做檢核報告（只報告缺口與風險點），並給出可貼給 Cursor 的修正工單。
```

### 9.3 要求我產出「可直接覆蓋」的文件（Final QA）
```md
嚴格對齊模式｜FINAL QA MODE
目標檔案：{doc_key / 檔名}
要求：
1) 先輸出 Final QA 檢核結果（只報告缺口與風險點，引用章節定位）
2) 再輸出可直接覆蓋的完整 md 檔（最大完備）
3) 最後列出尚未更新檔案優先順序
```

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 修正：將文件內「治理裁決序位」表述統一收斂為唯一箭頭鏈口徑：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。
- 修正：若本檔存在「全局定錨（S1）」之 L9/L10/L11 定義，已一致化為 Final QA 強制語義定錨口徑。
- 修正：本檔若引用其他治理文件檔名，統一指向現行覆蓋輸出檔名（優先 __CLEAN_260107）。
- 修正：若原檔存在稽核區塊或補丁式標記，已以 Legacy Snapshot 承接於檔尾稽核區塊，避免正文／稽核邊界混讀。
- 保留：PROCESS_ANCHOR 全文流程定錨內容全量承接，不做摘要縮水；僅做去混讀與引用一致化。


### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：042cdaaea9bc5e843e1bd9328dfe894aadd2ea38b6a46631bcb414f1c480fd57
- LEGACY_AUDIT_SHA256：a8d860aa104d37660fe25649c927ec891dd5b50bdc6988c5dfe144336dcef081

### 3) 適用範圍（Scope）
本次覆蓋版修正範圍僅限於 doc_key=PROCESS_ANCHOR：
- 治理裁決序位表示法一致化（箭頭鏈口徑）
- 全局定錨（S1）之 L9/L10/L11 定義一致化（若該段存在）
- 正文／稽核邊界去混讀（檔尾稽核區塊固定化；既有稽核內容以 Legacy Snapshot 承接）
- 引用檔名一致化（僅更新本檔提及之檔名字串；不修改其他 doc_key 正文內容）


### 4) 裁決承接（Audit Hand-off）
- 本檔為 PROCESS_ANCHOR 現行唯一可引用正文（工程 Phase 定錨）。
- 本檔僅定錨「程式開發流程」與「工程 Phase」對齊；不得取代 MASTER_CANON 的 Canonical Flow 定錨與 MASTER_ARCH 的治理鐵律。
- 若與其他治理文件存在衝突，裁決序位固定為：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。


### Legacy Audit Snapshot（被本次覆蓋版承接／非正文）

> # 稽核區塊（Audit Section｜非正文）
> 
> ## A. Scope（適用範圍）
> - doc_key: PROCESS_ANCHOR
> - document_tier: C（工程支援／操作定錨；不具治理裁決力）
> - version_date: 2026-01-06（Asia/Taipei）
> - scope_type: FINAL_QA_COVER
> - scope_files_output:
>   - TAITS｜程式開發流程定錨文件（Unified Process Anchor）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md
> - scope_files_source:
>   - TAITS｜程式開發流程定錨文件（Unified Process Anchor）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106__PATCH1.md
> - change_id: PROCESS_ANCHOR__FINALQA_260106__COVER
> - change_intent: 檔名與 doc_key 對齊 DOCUMENT_INDEX §10.1（PROCESS_ANCHOR）；移除 __PATCH1 檔名漂移作為現行引用；補強去混讀聲明與稽核留痕格式；重算指紋以支援可追溯性。
> 
> ## B. Changelog（變更清單）
> 1. 修正範例段落的括號/引號/程式區塊邊界，避免照抄造成格式破損或混讀。
> 2. 明確化「本文件不具治理裁決力」與最終裁決序位承接語句，避免工程文件越權。
> 3. 補強 Cursor 工單輸出規格（欄位、驗收點、回復計畫、稽核備註）。
> 4. 更新並回填 Hash Manifest（BODY_ONLY / FULL_EXCLUDING_HASH_VALUES）。
> 
> ## C. Hash Manifest（指紋清單）
> - hash_algo: SHA-256
> - hash_scope:
>   - BODY_ONLY（不含本稽核區塊）
>   - FULL_EXCLUDING_HASH_VALUES（全文但排除本節的 hash 值行）
> - hash_body_only_sha256: 3aa8b53f02b411e516b4b72dd2bd8d084f206868fe66843a3ada53010d9ea865
> - hash_full_excluding_hash_values_sha256: 689ea8dddbbf05fcaa036acbb37ce6961f1e839dccb95495ca063b84d7499c04
> 
> ## D. Audit Hand-off（裁決承接）
> - adjudication_order: DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
> - governance_state: GOVERNANCE_STATE__FREEZE_v1.0（依 DOCUMENT_INDEX 現行）
> - handoff_notes:
>   - 本文件僅作工程流程與對話定錨，不得作為治理條文之裁決依據。
>   - 若工程流程與治理文件語義衝突，依 adjudication_order 裁決。
> 
> ## E. Archive（留存）
> - replaced_or_moved_content: 無（本次為工程支援文件之修補與一致化，不包含治理條文）。
