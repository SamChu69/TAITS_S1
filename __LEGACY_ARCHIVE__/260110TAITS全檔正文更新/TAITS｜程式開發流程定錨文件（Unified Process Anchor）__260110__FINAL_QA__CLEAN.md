# TAITS｜程式開發流程定錨文件（Unified Process Anchor）

## 文件頭（Document Header）

- doc_key：PROCESS_ANCHOR
- 文件等級：C（工程支援／操作定錨；不具治理裁決力）
- 版本日期：2026-01-10（Asia/Taipei）
- 基線日期：2026-01-10（Asia/Taipei）
- 治理裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- Canonical 單一來源：L1–L11 之層級定義與語義以 doc_key=MASTER_CANON 為唯一正文來源（本文件不重複定義）

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
2. AI ≠ 決策主體：AI 只能提供分析、建議、整理、工單；交易授權只能由人類裁決層完成（層級語義以 MASTER_CANON 為準）。
3. Regime 高於策略：任何策略必須先受市場狀態（Regime/Context）約束。
4. Risk / Compliance 可否決一切：風險與合規可否決任何策略、任何執行、任何 UI 行為。
5. 正文／稽核邊界：正文不得殘留補丁式語句；所有留痕必須集中於檔尾稽核區塊或獨立稽核檔。
6. 單一現行：每份 doc_key 在 ACTIVE 集合中只能有一個現行版本（以 DOCUMENT_INDEX 指定為準）。
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
| Phase 4 | L9–L10 | Report + Human Decision | 依 MASTER_CANON 產出投資報告與人類裁決所需輸入（本文件不重複定義層級語義） |
| Phase 5 | L11 | Audit / Playback / Ops | 建立全鏈路留痕與回放、變更可追溯、日常可驗收（Auditable） |

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
- 正文／稽核邊界：正文不得殘留補丁式語句；留痕集中於檔尾稽核區塊或獨立稽核檔。

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
- constraints：治理硬限制（例如不可越權、不得跳層、正文／稽核邊界固定）
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

1. 把「報告／建議」寫成「下單指令」：禁止。報告只能形成可裁決的建議（非指令）。
2. 把「稽核回放」當成「下單入口」：禁止。稽核回放只負責留痕、可追溯與回放，不得作為執行入口。
3. 在 B/C 文件宣告「跨文件一律以本檔為準」：禁止（除非明確限定適用範圍，且承接最終裁決序位）。
4. 在正文留下補丁式修補語句：禁止。留痕只能進檔尾稽核區塊或獨立稽核檔。
5. 用占位符（例如 TBD/…/{{hash}}）當作最終交付：禁止（Final QA 必須收斂）。

---

## 8. 你要我怎麼「一路帶你做完」：推薦節奏（最小擴散）

1. Phase 0：先鎖定 ACTIVE=21（DOCUMENT_INDEX），完成 Final QA。
2. Phase 1：先把資料源契約定義（DATA_SOURCES）與清洗/特徵基線落地。
3. Phase 2：先做 Regime/Context，避免策略先跑造成漂移。
4. Phase 3：把風控與合規閘門做成可否決、可追溯的可執行元件。
5. Phase 4：固定投資報告格式與人類裁決模板，確保交易授權只有人類裁決入口。
6. Phase 5：把全留痕與回放做成日常可驗收的 SOP。

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
- 2026-01-10：正文正文化整理：移除補丁式/作業描述語句（例如「覆蓋輸出」「去混讀」等），改為正常制度文字。
- 2026-01-10：收斂層級提及方式：本文件不再特別化 L9–L11；僅保留工程 Phase 與 Canonical Flow 對照所需之最小映射，層級定義一律以 MASTER_CANON 為準。
- 2026-01-10：統一文件頭欄位（doc_key／等級／版本日期／基線日期／裁決序位），並固定稽核四件套格式。

### 2) 指紋清單（Hash Manifest）
- BODY_SHA256（不含本稽核區塊）：02c1c0e6de3f81dbb318cb09ff1db935032cc707ea3714902ef1706ed9d1770a: 99b4626c5e6f9ca1e8f1a65482bba8ccd32977a220e796f7c27846e6d3ad7af5

### 3) 適用範圍（Scope）
- 本文件用途：工程對話定錨、工單輸出規格、交付/驗收節奏（工程支援文件）。
- 本文件不裁決：ACTIVE 文件集合與治理位階、Canonical Flow（L1–L11）層級定義、任何交易授權/下單決策。
- 若與治理文件衝突：依「治理裁決序位」裁決。

### 4) 裁決承接（Audit Hand-off）
- adjudication_order: DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- governance_state: GOVERNANCE_STATE__FREEZE_v1.0（以 DOCUMENT_INDEX 現行為準）
- handoff_notes:
  - 本文件僅作工程流程與對話定錨；不得作為治理條文之裁決依據。
  - 本文件不得產生或暗示任何投資建議、交易指令或授權結果。
