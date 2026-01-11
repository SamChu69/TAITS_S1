# TAITS_專案總覽與快速開始（README）

## 文件頭（Document Header）

- doc_key：README
- 治理等級：C（操作／啟動級）
- 版本日期：2026-01-10（Asia/Taipei）
- 基線日期：2026-01-10（Asia/Taipei）
- 裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- Canonical Flow（L1–L11）之唯一正文來源：doc_key=MASTER_CANON

---

## 0. 本 README 的唯一職責（Scope Lock）

本 README 僅作為 TAITS 專案的「入口導覽與快速開始」，其目的在於：

- 提供新進讀者的閱讀順序（以裁決序位與依賴關係為核心）
- 提供常見工作場景的文件入口（不改寫任何上位制度）
- 提供工程落地與操作的最小導覽（指向既有制度文件）

本 README 不具有裁決力，不得被用作治理條文之替代來源；任何衝突與裁決，回到 doc_key=DOCUMENT_INDEX。

---

## 1. TAITS 是什麼（入口版）

TAITS（Taiwan Alpha Intelligence Trading System）是一套面向台灣市場（TWSE／TAIFEX）的可實盤、可長期演進之量化交易系統母體。其核心特徵：

- 系統由 Canonical Flow（L1–L11）與治理／風控／合規／執行控制共同構成
- Regime（市場狀態／情境）高於策略；Risk／Compliance 具最高否決權
- AI 僅為輔助，不是決策主體；策略 ≠ 下單；Agent ≠ 策略
- 所有可落盤產物必須可回放、可稽核、可追溯（見 VERSION_AUDIT／DEPLOY_OPS）

---

## 2. 最高裁決入口（必讀）

以下三份文件構成本專案的固定裁決序位與行為邊界；任何不一致或混讀，一律依序裁決：

1) **DOCUMENT_INDEX**：治理有效文件集合（ACTIVE）與衝突裁決程序之唯一權威索引  
2) **MASTER_ARCH**：母體總憲法與核心鐵律（不可反向改寫）  
3) **AI_GOV**：AI 行為與決策治理最終規則（AI 的允許與禁止邊界）

---

## 3. Canonical Flow（L1–L11）之唯一正文來源

- Canonical Flow（L1–L11）的層級定義、輸入輸出、責任邊界，一律以 **doc_key=MASTER_CANON** 為唯一正文來源。  
- 其他文件僅能「承接與引用」MASTER_CANON，不得重複定義、不得特別化任何子集合（包含不得特別化 L9–L11）。

---

## 4. 22 份文件快速地圖（導航版）

> 說明：以下為導覽用途之「導航版」摘要，不具有裁決力；裁決以 DOCUMENT_INDEX 為準。

### 4.1 A+（最高母法／索引裁決）
- DOCUMENT_INDEX：治理有效文件集合與衝突裁決
- AI_GOV：AI 行為與決策治理最終規則

### 4.2 A（憲法級／主幹與最高否決）
- MASTER_ARCH：母體總憲法與核心鐵律
- MASTER_CANON：完整總架構×總流程×全資訊體系（含 Canonical Flow L1–L11 唯一正文）
- RISK_COMPLIANCE：風險與合規最高否決權
- EXECUTION_CONTROL：交易執行與控制規範
- GOVERNANCE_GATE_SPEC：治理閘門與裁決規範
- GOVERNANCE_STATE：治理狀態（Freeze 等）
- VERSION_AUDIT：版本控管、稽核與可追溯治理規範

### 4.3 B（制度級／架構、流程、環境、營運）
- FULL_ARCH：全系統架構總覽
- ARCH_FLOW：系統架構與流程細化說明
- LOCAL_ENV：本地執行與運算環境規範
- DEPLOY_OPS：部署、營運與日常運作規範
- UI_SPEC：使用者介面與人機決策規範
- DATA_SOURCES：資料來源全集
- TWSE_RULES：TWSE 交易規則參考彙編
- STRATEGY_UNIVERSE：策略宇宙全集
- STRATEGY_FEATURE_INDEX：策略特徵與因子索引

### 4.4 C（操作／啟動級）
- BEGINNER_GUIDE：新手教學與操作引導總則
- README：本檔（入口導覽）
- TAITS_PROJECT_PROMPT：專案專屬啟動規範（對話/協作的行為約束）
- Unified Process Anchor：程式開發流程定錨文件（工程 Phase 導覽）

---

## 5. 建議閱讀順序（最快收斂、最小混讀）

1) DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（先確立裁決序位與邊界）  
2) MASTER_CANON（確立 Canonical Flow L1–L11 唯一正文來源）  
3) RISK_COMPLIANCE → GOVERNANCE_GATE_SPEC → EXECUTION_CONTROL（風控/合規/閘門/執行控制）  
4) VERSION_AUDIT（稽核與可追溯）  
5) LOCAL_ENV → DEPLOY_OPS（環境與營運落地）  
6) FULL_ARCH → ARCH_FLOW（架構總覽與流程細化）  
7) DATA_SOURCES → TWSE_RULES（資料與市場規則參考）  
8) STRATEGY_UNIVERSE → STRATEGY_FEATURE_INDEX（策略宇宙與特徵/因子索引）  
9) UI_SPEC（人機決策介面規範）  
10) BEGINNER_GUIDE（操作引導）  
11) Unified Process Anchor（工程定錨）／TAITS_PROJECT_PROMPT（協作定錨）

---

## 6. 常見工作場景入口（以文件為入口，不以對話為入口）

### 6.1 我想做「整編驗收／正文乾淨化」
- 先讀：DOCUMENT_INDEX（ACTIVE 與裁決）、MASTER_ARCH（鐵律）、AI_GOV（AI 邊界）
- 再處理：各 doc_key 逐一 FINAL QA（每次只處理一份，完成即落盤，保留稽核四件套）

### 6.2 我想做「工程落地／寫程式」
- 先讀：Unified Process Anchor（工程 Phase 與輸出物）
- 同時固定：LOCAL_ENV（本地環境）、VERSION_AUDIT（稽核留痕）、DEPLOY_OPS（落盤與回放）
- 與交易相關的任何觸發，必須承接：RISK_COMPLIANCE／GOVERNANCE_GATE_SPEC／EXECUTION_CONTROL

### 6.3 我想新增或擴充策略（僅限制度層面）
- 入口：STRATEGY_UNIVERSE（策略分類與治理定位）、STRATEGY_FEATURE_INDEX（特徵與因子索引）
- 所有策略落地與驗收流程，必須承接：MASTER_CANON（L1–L11）與上位裁決序位

### 6.4 我想確認資料可用性與規則限制
- 入口：DATA_SOURCES（資料源全集）、TWSE_RULES（交易規則參考）
- 與回放／留痕相關：VERSION_AUDIT、DEPLOY_OPS

---

## 7. 快速開始（最小可行導覽）

1) 先確認：DOCUMENT_INDEX 之 ACTIVE 集合、doc_key 唯一性、衝突裁決程序  
2) 再確認：MASTER_ARCH 的核心鐵律（Regime 高於策略；Risk/Compliance 可否決一切）  
3) 固定 AI 行為邊界：AI_GOV  
4) 僅在 MASTER_CANON 內閱讀 Canonical Flow（L1–L11）正文  
5) 任何涉及上線/執行/風控的工程變更，必須同時滿足：
   - RISK_COMPLIANCE（否決權）
   - GOVERNANCE_GATE_SPEC（閘門裁決）
   - EXECUTION_CONTROL（執行控制）
   - VERSION_AUDIT（可追溯）
   - LOCAL_ENV / DEPLOY_OPS（環境與營運落地）

---

## 8. 重要提醒（避免混讀）

- README/BEGINNER_GUIDE 屬導覽性文件；不得取代上位制度文件之裁決內容。  
- 任何文件若出現與 DOCUMENT_INDEX／MASTER_ARCH／AI_GOV 不一致之敘述：一律依裁決序位處置。  
- Canonical Flow（L1–L11）只在 MASTER_CANON 定義；其他文件不得重複或特別化任何子集合。  

---

## 稽核區塊（Audit Section｜非正文）

### 1) Changelog（變更紀錄）
- 2026-01-10：FINAL_QA_NORMALIZE（修補正文缺口：移除省略占位符、補齊入口導覽內容、對齊基線日期與裁決序位口徑；不新增制度裁決條文，僅提供導覽與指引；保留稽核四件套。）

### 2) Hash Manifest（指紋清單）
- HASH_RULE：SHA-256（UTF-8，LF；Body=本檔「稽核區塊」之前全文，含結尾換行）
- BODY_SHA256：b1d2d5efa071b5a8083c714a1f47b1390f0351ed097469595e3f8dde96fd8605

### 3) Scope（適用範圍）
- scope_doc_key：README
- scope_change_type：FINAL_QA_NORMALIZE（正文乾淨／去重收斂／結構重排／導覽補齊）
- scope_invariants：
  - README 僅作入口導覽，不得作為裁決條文來源
  - 裁決序位固定：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
  - Canonical Flow 唯一正文來源維持：MASTER_CANON
  - 不新增投資建議、個股分析、策略交易指令與回測/模擬內容

### 4) Audit Hand-off（裁決承接）
- governance_order_applied：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- active_set_authority：DOCUMENT_INDEX（Authoritative Index）
- canonical_flow_anchor：MASTER_CANON（L1–L11 唯一正文來源）