# TAITS_專案總覽與快速開始（README）

## 文件頭（Document Header）

- doc_key：README
- 治理位階：操作／啟動級（入口導覽文件）
- 版本日期：2026-01-11（Asia/Taipei）
- 基線日期：2026-01-11（Asia/Taipei）
- 裁決序位（自高至低）：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
- Canonical Flow（L1–L11）之唯一正文來源：doc_key=MASTER_CANON
- 本文件性質：入口導覽與快速開始；不承擔制度裁決條文效力

---

## 0. 本 README 的唯一職責（Scope Lock）

本 README 僅作為 TAITS 專案的「入口導覽與快速開始」，唯一職責如下：

1. 協助你在 22 份文件中快速定位：哪一份是裁決權威、哪一份是主幹正文、哪一份是制度規範、哪一份是操作手冊。
2. 提供一致的起手式：如何啟動一輪工程或制度檢核，並確保不混讀、不跳層、不越權。
3. 明確聲明邊界：本 README 不新增或改寫任何治理條文；若與更高位階文件衝突，以裁決序位為準。

本 README 不包含、也不得被視為以下內容：
- 個股分析、投資建議、標的推薦
- 策略回測、模擬績效展示、下單指令
- Canonical Flow（L1–L11）的制度定義或任何子集合特別化（包含不得特別化 L9–L11）

---

## 1. 你現在要做什麼：三種常見起手式

### 1.1 做「正文整編與驗收」（Final QA）
適用情境：你要將某一份 doc_key 整理為「正文乾淨、無重複、無混讀、可長期維護」的最大完備覆蓋版。

建議起手式：
- 先以 doc_key=DOCUMENT_INDEX 確認該檔案治理位階與裁決鏈
- 若涉及 Canonical Flow（L1–L11），只允許引用 doc_key=MASTER_CANON 之正文，不得在下位文件再定義
- 逐檔處理：一次只處理一個 doc_key，產出可直接覆蓋的完整 md（含檔尾稽核四件套）

### 1.2 做「工程開發流程定錨」（Engineering Anchor）
適用情境：你要用固定的工程節奏與關卡，在 Cursor 或本地環境落地。

建議起手式：
- 以 doc_key=TAITS｜程式開發流程定錨文件（Unified Process Anchor）作為工程節奏定錨
- 以 doc_key=GOVERNANCE_GATE_SPEC、RISK_COMPLIANCE、EXECUTION_CONTROL 作為工程關卡與阻斷條件來源
- 以 doc_key=DEPLOY_OPS、LOCAL_ENV 作為環境與運維規範來源

### 1.3 做「快速了解系統全貌」
適用情境：你想先掌握 TAITS 是什麼、有哪些制度邊界、有哪些文件扮演什麼角色。

建議起手式：
- 先讀 doc_key=MASTER_CANON（主幹：完整總架構、總流程、全資訊體系；含 Canonical Flow 正文）
- 再讀 doc_key=DOCUMENT_INDEX（權威索引：治理位階、ACTIVE、引用邊界）
- 再依需求選讀：FULL_ARCH（全系統總覽）、ARCH_FLOW（流程細化）、各治理制度文件（風控／合規／Gate／執行／UI）

---

## 2. 不混讀的閱讀法（權威層級與引用邊界）

請遵守以下閱讀與引用順序，以避免「同一概念在不同文件被重複定義」而引發混讀：

1. 權威索引與裁決基準：doc_key=DOCUMENT_INDEX
2. 母體憲法級與鐵律：doc_key=MASTER_ARCH
3. AI 行為與決策治理：doc_key=AI_GOV
4. Canonical Flow（L1–L11）唯一正文：doc_key=MASTER_CANON

除 doc_key=MASTER_CANON 外，其他文件若需提及 L1–L11：
- 只能引用 MASTER_CANON 的章節與語義
- 只能描述「承接責任、接口契約、稽核欄位、阻斷條件」
- 不得以任何方式重寫、再定義或特別化 L1–L11 的子集合

---

## 3. 快速開始（不越權的最小路徑）

### 3.1 最小有效閱讀清單（建議順序）
1. DOCUMENT_INDEX：確認 ACTIVE、治理位階與引用邊界
2. MASTER_ARCH：確認母體鐵律與不可違反原則
3. AI_GOV：確認 AI 可做與不可做，以及回覆與引用規範
4. MASTER_CANON：確認 Canonical Flow（L1–L11）正文與全資訊體系

### 3.2 最小有效落地清單（工程必備）
1. GOVERNANCE_GATE_SPEC：治理 Gate 與裁決規範
2. RISK_COMPLIANCE：風險與合規最高否決權
3. EXECUTION_CONTROL：交易執行與控制規範
4. DEPLOY_OPS：部署、營運與日常運作規範
5. LOCAL_ENV：本地執行與運算環境規範
6. VERSION_AUDIT：版本控管、稽核與可追溯規範

---

## 4. 22 份文件快速地圖（導航版）

> 說明：以下為導覽用途，僅陳述「文件扮演的角色」與「何時應該引用」。制度裁決與語義以各文件正文為準。

### 4.1 權威索引與主幹正文
- DOCUMENT_INDEX：權威索引；ACTIVE 集合、治理位階、引用邊界與裁決基準
- MASTER_CANON：主幹正文；完整總架構、總流程、全資訊體系；含 Canonical Flow（L1–L11）唯一正文來源

### 4.2 母體鐵律與治理最高規則
- MASTER_ARCH：母體總憲法與核心鐵律（不可違反的總原則）
- AI_GOV：AI 行為與決策治理最終規則（AI 的回覆邊界、行為約束、引用規範）

### 4.3 架構與流程制度
- FULL_ARCH：全系統架構總覽（全域模組、責任邊界、接口概覽）
- ARCH_FLOW：系統架構與流程細化（流程細節、工程落地接口字典；不得再定義 L1–L11）
- DATA_SOURCES：資料來源全集（資料治理、來源註冊、失敗處置與資料契約）
- TWSE_RULES：TWSE 交易規則參考彙編（規則參考與合規對齊素材）

### 4.4 風控、合規、治理 Gate 與執行控制
- RISK_COMPLIANCE：風險與合規最高否決權（任何層級均可阻斷）
- GOVERNANCE_GATE_SPEC：治理閘門與裁決規範（Gate 形態、reason_code、PASS/RETURN/BLOCK 規範）
- EXECUTION_CONTROL：交易執行與控制規範（下單前置校驗、執行保護、控管欄位）

### 4.5 人機介面與營運環境
- UI_SPEC：使用者介面與人機決策規範（展示、決策追溯、交互邊界）
- DEPLOY_OPS：部署、營運與日常運作規範（運維、封存、回放、告警與值守）
- LOCAL_ENV：本地執行與運算環境規範（環境準備、依賴、配置與最小執行基線）

### 4.6 版本、稽核、可追溯治理
- VERSION_AUDIT：版本控管、稽核與可追溯治理規範（變更留痕、Hash、交付與稽核流程）
- GOVERNANCE_STATE__FREEZE_v1.0：治理狀態（Freeze）文件（結構性變更限制與生效狀態）

### 4.7 策略宇宙與特徵索引（策略內容不等於下單）
- STRATEGY_UNIVERSE：策略宇宙全集（策略分類、模板、生命週期；不直接下單）
- STRATEGY_FEATURE_INDEX：策略特徵與因子索引（特徵字典、因子命名與引用對位）

### 4.8 操作手冊與工程定錨
- BEGINNER_GUIDE：新手教學與操作引導總則（操作流程、使用說明、常見情境）
- TAITS｜程式開發流程定錨文件（Unified Process Anchor）：工程 Phase 定錨（0–5）、交付節奏與關卡口徑
- TAITS_PROJECT_PROMPT：專案啟動提示文件（新對話啟動、角色與約束宣告）

---

## 5. 使用 README 的紅線（禁止事項）

- 不得引用 README 作為任何制度裁決依據
- 不得在 README 重複定義 Canonical Flow（L1–L11）
- 不得在 README 插入任何投資建議、個股分析、標的推薦、回測或模擬內容
- 不得以 README 覆寫更高位階文件之語義；若有衝突，以裁決序位為準

---

# 稽核區塊（Audit Section｜非正文）

### 1) Changelog（變更清單）
- 2026-01-11：Final QA 正文化（正文乾淨、去重收斂、結構重排、導覽補齊；不新增制度裁決條文）

### 2) Hash Manifest（指紋清單）

### 3) Scope（適用範圍）
- scope_doc_key：README
- scope_change_type：FINAL_QA_NORMALIZE
- scope_invariants：
  - README 僅作入口導覽，不得作為裁決條文來源
  - 裁決序位固定：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
  - Canonical Flow 唯一正文來源維持：MASTER_CANON
  - 不新增投資建議、個股分析、策略交易指令與回測或模擬內容

### 4) Audit Hand-off（裁決承接）
- governance_order_applied：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
- active_set_authority：DOCUMENT_INDEX（Authoritative Index）
- canonical_flow_anchor：MASTER_CANON（L1–L11 唯一正文來源）

---

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- FINAL_QA_NORMALIZE：補齊檔尾稽核四件套（Changelog／Hash Manifest／Scope／Audit Hand-off），將稽核資訊自正文抽離至非正文區塊，確保正文乾淨且可長期維護。
- FINAL_QA_NORMALIZE：移除正文中可能殘留之補丁／Legacy／Hash 散落行（若存在），並依 HASH_RULE 重新計算 BODY_SHA256。

### 2) Hash Manifest（指紋清單）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：e83c0cecf7d595098d0fe8de58d74279ea48d7e0d56385fb68e0f9c432cfa602
### 3) Scope（適用範圍）
- scope_doc_key：README
- scope_files_output：TAITS_專案總覽與快速開始（README）__260113__FINAL_QA__NORMALIZE.md
- scope_mode：FINAL QA MODE（正文去重收斂／結構重排／正文乾淨化／檔尾稽核四件套固定）
- version_date：2026-01-11（Asia/Taipei）

### 4) Audit Hand-off（裁決承接）
- adjudication_chain：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- canonical_flow_source：MASTER_CANON
- note：本檔為 README 現行唯一可引用正文（入口導覽與快速開始）；不承擔制度裁決條文效力。若與治理文件存在衝突，裁決序位固定為 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。
