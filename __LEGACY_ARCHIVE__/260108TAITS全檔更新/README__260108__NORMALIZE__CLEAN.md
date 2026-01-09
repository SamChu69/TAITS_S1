# TAITS（README）

## 文件頭（Document Header）

- doc_key：README  
- 治理等級：C（操作／啟動級）  
- 版本日期：2026-01-08（Asia/Taipei）  
- 基線日期：2026-01-08（Asia/Taipei）  
- 治理裁決序位（固定）：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  

---

## 0. 本 README 的唯一職責（Scope Lock）

本 README 僅作為 **TAITS 專案入口導覽**，提供：

- 新對話啟動方式與最小載入清單（Minimum Load Set）
- 正確閱讀順序（入口提示）
- 使用本專案文件之基本規則（避免混讀/越權）
- 最小引用合法性格式（方便稽核與回放）

本 README **不裁決**：ACTIVE 文件集合、文件位階、任何制度內容之衝突版本；相關裁決一律以 doc_key=DOCUMENT_INDEX 為準。

---

## 1. 全局定錨（入口版提醒）

### 1.1 治理裁決序位（固定）

任何文件、任何 Agent、任何 UI 呈現不得自創或改寫裁決序位；裁決序位固定為：

- DOCUMENT_INDEX → MASTER_ARCH → AI_GOV

### 1.2 Canonical Flow（L1–L11）之唯一正文來源

- L1–L11（Canonical Flow）之層級定義與邊界：**以 doc_key=MASTER_CANON 為唯一正文來源**。  
- 本 README 僅做入口提示，不重複定義任何層級內容。

### 1.3 最高優先原則（入口版）

- Regime（市場狀態/情境）高於策略  
- Risk / Compliance（風險/合規）具最高否決權  
- 策略 ≠ 下單；Agent ≠ 策略；AI ≠ 決策主體  

---

## 2. 新對話啟動（必讀）

### 2.1 啟動確認語（新對話第一句）

新對話第一則訊息貼上 TAITS 專案啟動 Prompt 後，系統回覆必須先回覆且只回覆以下一句作為啟動確認：

「TAITS 架構已完整載入，我已準備好在此基礎上繼續開發。」

### 2.2 新對話載入最小規格（Minimum Load Set）

為避免新對話混讀或越權，最低必載入並對齊以下文件（依治理序位優先）：

1) doc_key=DOCUMENT_INDEX  
2) doc_key=MASTER_ARCH  
3) doc_key=MASTER_CANON  
4) doc_key=AI_GOV  
5) doc_key=RISK_COMPLIANCE  
6) doc_key=GOVERNANCE_GATE_SPEC  
7) doc_key=EXECUTION_CONTROL  
8) doc_key=VERSION_AUDIT  

---

## 3. 正確閱讀順序（入口提示）

### 3.1 最小必讀（不得跳過）

1) DOCUMENT_INDEX（ACTIVE 與位階裁決）  
2) MASTER_ARCH（母體總憲法與核心鐵律）  
3) MASTER_CANON（Canonical Flow 主幹）  
4) AI_GOV（AI 行為與輸出治理）  
5) RISK_COMPLIANCE（風險與合規最高否決權）

### 3.2 視需求擴展（在治理框架下）

依需求閱讀：GOVERNANCE_GATE_SPEC、EXECUTION_CONTROL、VERSION_AUDIT、FULL_ARCH、ARCH_FLOW、DEPLOY_OPS、LOCAL_ENV、DATA_SOURCES、TWSE_RULES、STRATEGY_UNIVERSE、STRATEGY_FEATURE_INDEX、UI_SPEC、GOVERNANCE_STATE、Unified Process Anchor、BEGINNER_GUIDE、TAITS_PROJECT_PROMPT。

---

## 4. 角色分工（強制遵守）

- **人類最高決策者（產品負責人／架構裁決者）**：唯一可做最終裁決與授權之主體。  
- **AI / Agent / LLM**：僅能在治理邊界內協助產出、整理、檢核與可追溯留痕；不得越權成為決策主體。  
- **Risk / Compliance**：具最高否決權（其規則與介面以 RISK_COMPLIANCE 為準）。  

---

## 5. 使用本專案文件的基本規則（入口版）

1) 僅以治理有效文件為準：ACTIVE 與位階以 DOCUMENT_INDEX 裁決。  
2) 不得混讀：若同一主題存在多份版本，以裁決序位與 DOCUMENT_INDEX 為準，不得自行拼接。  
3) 不得越權：任何輸出不得越過 Canonical Flow 的層級邊界與治理閘門。  
4) 產出必須可追溯：引用、依據、結論、裁決與執行之關聯必須可被稽核回放（相關規則以 VERSION_AUDIT / AI_GOV 為準）。

---

## 6. 引用合法性最小格式（Minimum Legal Citation Format）

為確保可稽核、可回放、可追責，引用治理文件時最小必須包含：

- doc_key  
- 章節路徑（例如：`§2.3`、`## 3.1`、`條款 4-2`）  
- 版本日期（以文件頭為準）  
- 如涉及裁決：補上裁決序位依據（DOCUMENT_INDEX → MASTER_ARCH → AI_GOV）

---

## 7. 最終聲明（入口版，不可刪）

TAITS 的核心價值不在於「多聰明」，而在於：

- 不亂來  
- 不越權  
- 可回放  
- 可追責  
- 可長期演進  

只要存在不可接受風險，就算錯過機會，也必須選擇不交易（裁決依 doc_key=RISK_COMPLIANCE）。


## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 2026-01-08：README 正文化（正文乾淨／去重收斂／結構重排），移除補丁式文字與歷史殘留，並統一以 MASTER_CANON 承接 L1–L11 之唯一正文來源。

### 2) 指紋清單（Hash Manifest）
- BODY_SHA256: 11681e6530a239de18d87c828b0fb7030d2295e4223e1db302efe219a5dab985

### 3) 適用範圍（Scope）
- 本檔為 doc_key=README 之入口導覽文件（治理等級 C）。
- 正文範圍：自檔首 `# TAITS（README）` 起，至 `## 稽核區塊（Audit Section｜非正文）` 前一行止。
- 本稽核區塊不屬正文，不得作為制度內容之裁決依據。

### 4) 裁決承接（Audit Hand-off）
- 治理裁決序位固定：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- ACTIVE 文件集合與位階裁決：doc_key=DOCUMENT_INDEX
