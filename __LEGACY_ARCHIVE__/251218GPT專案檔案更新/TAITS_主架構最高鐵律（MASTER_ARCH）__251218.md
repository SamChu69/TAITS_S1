# TAITS_主架構最高鐵律（MASTER_ARCH）__251218.md

> doc_key：MASTER_ARCH  
> 治理等級：A+（母體鐵律｜不可違反｜全系統最高架構約束）  
> 適用範圍：TAITS 全系統（文件/架構/資料/策略/風控/執行/UI/治理）  
> 交易市場：TWSE / TPEX（台灣股票為主）  
> 券商 API：富邦證券 TradeAPI（現階段唯一授權執行）  
> 交易單位：零股（核心）、整股（預留）、混合（預留）  
> 狀態：ACTIVE（Only-Add｜只能新增不可縮水）  
> 最後更新：2025-12-18（Asia/Taipei）

---

## 0. 文件定位（Constitution of TAITS）

本文件是 TAITS 的「憲法」。  
任何文件、任何模組、任何策略、任何 AI 行為，只要與本文件衝突，**一律以本文件為準**。

TAITS 的目標不是「今天賺多少」，而是確保：

- **可重現（Reproducibility）**
- **可審計（Auditability）**
- **可否決（Veto-able）**
- **可回放（Replayable）**
- **可長期演進（Evolvable）**

---

## 1. TAITS 五大鐵律（不可違反）

### 1.1 策略 ≠ 下單（Strategy ≠ Order）
- 策略只能輸出：訊號、情境、理由、信心、參數建議
- 策略不得輸出：直接呼叫下單、繞過風控、強制成交

### 1.2 Agent ≠ 策略（Agent ≠ Strategy）
- Agent 是「分析/彙整/建議」的角色
- 策略是「可被回測/可被驗證」的決策模型
- Agent 不得自行創造策略定義或替策略下判斷結論

### 1.3 AI ≠ 唯一真理（AI ≠ Truth）
- AI 只能做輔助、不能做最終裁決
- AI 必須接受文件與風控約束
- AI 不能自行調整治理等級、不能自行縮寫文件

### 1.4 Regime 高於單一訊號（Regime > Signal）
- 任何單一指標/訊號都必須受市場狀態（Regime）約束
- Regime 不明確時，預設為「不交易/觀察」

### 1.5 Risk / Compliance 可否決一切（Risk Veto All）
- 風控與合規（RISK_COMPLIANCE）具有最高否決權
- 任何輸出、任何流程、任何執行，只要被否決，**立刻終止**

---

## 2. 官方規則優先（Official-First，禁止寫死細節）

### 2.1 官方制度高於系統假設
- TWSE / TPEX 的交易制度、盤別、時間、限制等，隨時可能變更
- TAITS 的規則設計必須是「引用導向」，而非寫死數值/條文

### 2.2 易變動資訊禁止硬編碼
以下禁止寫死在策略或程式中（只能在 OFFICIAL_REF 以「引用入口＋對應 Gate」呈現）：
- 交易時間與盤別細節
- 撮合機制差異
- 漲跌幅/處置/暫停等制度細節

---

## 3. 系統最高優先順序（衝突裁決）

當任何文件/模組/指令衝突，依以下順序裁決（由高到低）：

1) OFFICIAL_REF（官方制度引用）  
2) RISK_COMPLIANCE（最高否決權）  
3) DOCUMENT_INDEX（全文件唯一索引）  
4) MASTER_ARCH（本文件，母體鐵律）  
5) MASTER_VERSION（最大整合母體）  
6) ARCH_FLOW（架構＋資料流＋決策流）  
7) FULL_ARCH（全景架構藍圖）  
8) STRATEGY_UNIVERSE（策略宇宙）  
9) FEATURE_INDEX（特徵索引）  
10) EXEC_CONTROL（執行與控制）  
11) UI_SPEC（UI 規範）  
12) DEPLOY_OPS / LOCAL_ENV / VERSION_AUDIT / SAVE_RULES / BEGINNER_RULES

> 註：若 DOCUMENT_INDEX 內定義了更細的優先關係，以 DOCUMENT_INDEX 為準。

---

## 4. TAITS 的「交易產品與路線」鐵律（現階段鎖定）

### 4.1 現階段產品鎖定：股票 Stock
- 目前 TAITS 的可落地執行目標：**台灣股票（TWSE/TPEX）**
- 其他商品（期貨/選擇權/海外）：架構可預留，但不得混入主流程造成污染

### 4.2 交易單位鐵律：零股優先（Odd Lot First）
- 目前因資金與策略路線，**零股交易為核心**
- 必須明確把「零股」當成：
  - 獨立盤別/流動性/成交特性
  - 獨立風控 Gate
  - 獨立績效/滑價/成交風險評估
- 整股與混合屬預留：可設計接口，但不得讓零股邏輯被整股假設污染

### 4.3 券商 API 鐵律：富邦 TradeAPI 為唯一授權執行
- 現階段只允許以「富邦 TradeAPI」作為 Execution 連接
- 不得引入 XQ 平台特性或限制，避免架構污染
- 若未來要支援其他平台/券商：必須以「新增產品線/新增適配層」方式 Only-Add

---

## 5. 架構核心：分層、分權、可否決

TAITS 必須符合以下分層與分權原則：

### 5.1 分層（Layering）
最小必備層次（不可合併成黑箱）：

- Data Layer（資料層）
- Feature Layer（特徵層）
- Regime Layer（市場狀態層）
- Strategy Layer（策略層）
- Risk/Compliance Layer（風控合規層）
- Execution Layer（執行層）
- Audit/Replay Layer（審計回放層）
- UI/Human Layer（人類介入層）
- Governance Layer（文件與版本治理層）

### 5.2 分權（Separation of Powers）
- Strategy 不能下單
- Execution 不能決策
- AI 不能裁決
- Risk 能否決全部
- Human 擁有最終控制權（可否決、可延後、可關閉）

---

## 6. 事件驅動與證據鏈（Event + Evidence Chain）

### 6.1 事件驅動（Event-Driven）
TAITS 的流程必須可用事件描述（可追溯）：

- Data Ingested
- Feature Built
- Regime Determined
- Strategy Signal Produced
- Risk Decision Made
- Execution Authorized
- Order Sent / Filled / Rejected
- Post-Trade Logged

### 6.2 證據鏈（Evidence Chain）
每一次可能導致交易的行為，都必須留下證據鏈：

- 輸入資料版本（snapshot）
- 特徵版本（feature set）
- Regime 判定結果（含理由）
- 策略輸出（含理由/參數/信心）
- 風控判定（通過/否決與原因）
- 人類介入記錄（如有）
- 執行回報（委託/成交/拒單）
- 系統狀態（環境、版本、時間）

---

## 7. 風控與合規鐵律（Risk as Authority）

### 7.1 任何時點都可否決
- 風控可在：
  - 策略輸出後
  - 下單前
  - 下單後（中止後續行為）
  - 系統異常時
  即時否決

### 7.2 Kill Switch 必須存在且可用
- Kill Switch 觸發後必須：
  - 立即停止執行層
  - 保留狀態與證據
  - 通知人類

### 7.3 零股專屬風控必須存在
零股必備 Gate（不可省略）：
- 流動性 Gate（低量即停）
- 成交不確定性 Gate（允許不成交）
- 滑價/價差 Gate（過大即停）
- 時段 Gate（盤內不同時段限制）

---

## 8. AI 行為鐵律（Strict Alignment，不能偷工減料）

### 8.1 文件輸出不得縮水
- 使用者要求「完整」時：
  - 必須輸出完整全文
  - 若太長：分批輸出
  - 不得用摘要替代全文

### 8.2 不得腦補
- 未列於文件或 Canon 中的內容：
  - 必須標註為「待新增文件」
  - 不得直接當成既定事實

### 8.3 新對話必讀 Canon
- 新對話開始，AI 必須以 DOCUMENT_INDEX 為入口載入 Canon
- 未完成載入不得進行實質討論

---

## 9. 文件治理鐵律（Docs-First + Only-Add）

### 9.1 Docs-First
- 文件是 TAITS 的最高權威載體
- 程式碼不得自創規則與文件衝突

### 9.2 Only-Add
- 不覆寫舊檔
- 新版本用日期區分（YYMMDD）
- 變更必可追溯（VERSION_AUDIT）

---

## 10. 最終宣告（不可違反的系統本質）

TAITS 不追求「看起來會賺」，而追求：

- 不確定時能停手
- 錯誤時能中止
- 事後能回放
- 長期能演進

> **在 TAITS 中，不能被否決的交易，就是不被允許的交易。**

---

（End of MASTER_ARCH）
