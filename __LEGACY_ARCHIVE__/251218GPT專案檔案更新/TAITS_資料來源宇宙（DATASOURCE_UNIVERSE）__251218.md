# TAITS_資料來源宇宙（DATASOURCE_UNIVERSE）__251218.md

> doc_key：DATASOURCE_UNIVERSE  
> 治理等級：A（資料治理核心｜官方優先）  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live-Ready）  
> 狀態：ACTIVE（Only-Add｜只能新增不可縮水）  
> 最後更新：2025-12-18（Asia/Taipei）

---

## 0. 文件定位（Data Governance Core）

本文件定義 **TAITS 全系統「資料來源宇宙」與資料治理規範**，  
目標不是「蒐集越多越好」，而是確保：

- **正確性（Correctness）**
- **可回放（Replayability）**
- **可審計（Auditability）**
- **官方優先（Official Source First）**

📌 在 TAITS 中：  
**資料品質與來源可信度，高於任何策略技巧。**

---

## 1. 資料治理最高原則（不可違反）

### 1.1 官方來源優先（Official Source First）

- 所有關鍵資料（價格、成交、交易規則）：
  - **必須優先來自官方或一手來源**
- 非官方來源：
  - 僅能作為補充
  - 必須標註可信度與用途

---

### 1.2 易變動資訊不得寫死

- 交易時間
- 撮合規則
- 限制條件
- API 行為

📌 上述內容 **不得硬編碼於系統邏輯**，  
只能：
- 以「引用官方來源」方式存在
- 由本文件指向官方文件入口

---

### 1.3 資料可回放、可審計

- 任一策略決策：
  - 必須能回溯所使用的資料版本
- 任一執行行為：
  - 必須能對應到資料證據

---

## 2. 資料分層模型（Data Layering Model）

TAITS 將資料分為六層（由下而上）：

1. **Raw Data（原始資料）**
2. **Normalized Data（標準化資料）**
3. **Derived Data（派生資料）**
4. **Feature Data（特徵資料）**
5. **Snapshot / Evidence（決策證據）**
6. **Audit Log（審計紀錄）**

📌 上層資料 **永遠不能回寫覆蓋下層資料**。

---

## 3. 官方市場資料來源（Primary Official Sources）

### 3.1 TWSE（臺灣證券交易所）

- 資料類型：
  - 個股成交資訊
  - 價量資料
  - 公告與制度
- 用途：
  - 市場主資料
  - 回測與驗證基準
- 官方入口（僅引用）：
  - https://www.twse.com.tw/

---

### 3.2 TPEX（櫃買中心）

- 資料類型：
  - 上櫃股票資料
  - 成交與公告
- 官方入口：
  - https://www.tpex.org.tw/

---

### 3.3 MOPS（公開資訊觀測站）

- 資料類型：
  - 財報
  - 重大訊息
- 用途：
  - 基本面分析
  - 事件標記
- 官方入口：
  - https://mops.twse.com.tw/

---

## 4. 券商與交易相關資料

### 4.1 富邦證券 TradeAPI（Primary Broker API）

- 資料類型：
  - 即時報價（依 API 能力）
  - 帳戶狀態
  - 委託 / 成交回報
- 用途：
  - Execution 層
  - 實單 / 模擬
- 官方文件入口（引用）：
  - https://www.fbs.com.tw/TradeAPI/docs/trading/introduction/

📌 **所有 Execution 設計必須符合富邦 API 限制，不得假設不存在的能力。**

---

## 5. 非官方 / 第三方資料（Secondary Sources）

### 5.1 第三方行情與歷史資料

- 可能來源：
  - 商業資料商
  - 開源專案
- 使用限制：
  - 僅限研究與回測
  - 不作為最終執行依據

---

### 5.2 新聞、情緒、事件資料

- 類型：
  - 新聞摘要
  - 情緒指標
- 用途：
  - Regime 補充
  - 風險提示
- 限制：
  - 不可單獨作為交易依據

---

## 6. 零股交易相關資料（Odd Lot Focus）

### 6.1 零股必要資料欄位

- 成交量粒度
- 流動性指標
- 成交分佈

### 6.2 零股特殊限制

- 成交不連續
- 價差敏感
- 容易滑價

📌 **零股資料必須經過額外驗證，否則策略不得啟用。**

---

## 7. 資料品質與異常處理

### 7.1 品質檢查（Data Quality Check）

- 缺值
- 跳價
- 時間錯位

### 7.2 異常處理原則

- 不補假資料
- 不自動修正
- 標記並停用策略

---

## 8. 資料版本控管與保存

- 原始資料：
  - 只讀
- 派生資料：
  - 版本化
- 所有資料：
  - 必須有時間戳
  - 必須可追溯來源

---

## 9. 與其他文件的關係

- 受制於：
  - MASTER_ARCH
  - ARCH_FLOW
- 被引用於：
  - STRATEGY_UNIVERSE
  - RISK_COMPLIANCE
  - EXEC_CONTROL

---

## 10. 演進與擴充原則（Only-Add）

- 可新增：
  - 新官方資料源
  - 新第三方資料
- 不可：
  - 移除既有來源
  - 降低資料治理標準

---

## 11. 一句話總結

> **在 TAITS 中，  
資料不是燃料，  
資料是證據。**

---

（End of DATASOURCE_UNIVERSE）
