# TAITS_DataSources_Universe.md
# TAITS — 全資料來源宇宙（Master Data Source Specification）

版本：Master / Full  
文件角色：**資料治理最高權威（Single Source of Truth）**  
對應架構文件：
- TAITS_MASTER_ARCHITECTURE.md
- TAITS_Full_System_Architecture.md

---

## 0. 文件定位（非常重要）

本文件定義 **TAITS 系統中所有「被允許使用的資料來源」**。

任何：
- 策略
- Agent
- AI 模型
- Regime 判斷
- 風控邏輯

👉 **只能使用本文件中列出的資料來源**。

---

## 1. 資料治理核心原則

1. 官方資料優先
2. 合法、可長期取得
3. 可追溯來源
4. 多來源 fallback
5. 不得私接未登記資料

---

## 2. 資料分類總覽

| 分類 | 用途 |
|---|---|
| 價格 / 成交 | 技術指標、策略、回測 |
| 籌碼 / 法人 | 籌碼策略、ChipAgent |
| 基本面 | FundamentalAgent |
| 衍生品 | Regime、DerivativesAgent |
| 新聞 / 事件 | News / EventAgent |
| 情緒 | SentimentAgent |
| 宏觀 | MacroAgent |
| 交易回報 | Risk / Portfolio / Audit |

---

## 3. 台股現貨資料（TWSE / TPEX / MOPS / 集保）

### 3.1 TWSE（證交所）

- 來源：台灣證券交易所（官方）
- 資料：
  - OHLC / 成交量 / 成交金額
  - 即時行情
  - 三大法人（現貨）
  - 融資融券
  - 當沖比率
  - 停牌 / 處置
- 使用層級：
  - Indicators
  - Strategies
  - TechnicalAgent
  - ChipAgent
  - MarketRegimeEngine

---

### 3.2 TPEX（櫃買中心）

- 上櫃股票對應資料
- 結構與 TWSE 一致

---

### 3.3 MOPS（公開資訊觀測站）

- 資料：
  - 財報（BS / IS / CF）
  - EPS / ROE / 毛利率
  - 月營收
  - 重大訊息 / 法說會
- 使用：
  - FundamentalAgent
  - EventAgent
  - RiskAgent

---

### 3.4 集保中心

- 資料：
  - 股權分散
  - 集中度
- 使用：
  - ChipAgent

---

## 4. 台灣期貨與選擇權（TAIFEX）

### 4.1 期貨

- 資料：
  - 台指期 / 小台
  - OI
  - 三大法人期貨
  - 大額交易人
  - 夜盤
- 使用：
  - DerivativesAgent
  - MarketRegimeEngine
  - RiskAgent

---

### 4.2 選擇權

- 資料：
  - Put/Call Ratio
  - IV / Skew
  - Max Pain
- 使用：
  - Regime 判斷
  - 風險預警

---

## 5. 券商交易資料（Execution Only）

### 5.1 富邦證券 API

- 資料：
  - 下單回報
  - 成交
  - 庫存
  - 帳務
- 使用限制：
  - **僅 Execution / Risk**
  - 不得參與策略判斷

---

## 6. 新聞與事件資料

- 來源：
  - 鉅亨（Cnyes）
  - Yahoo
  - 官方公告
- 使用：
  - NewsAgent
  - EventAgent
  - Fusion Override

---

## 7. 情緒資料（Sentiment）

- 來源：
  - PTT
  - Dcard
  - Google Trends
- 使用：
  - SentimentAgent
  - 行為金融策略

---

## 8. 宏觀資料（Macro）

- 資料：
  - SOX
  - 美股指數
  - VIX
  - USD/TWD
- 使用：
  - MacroAgent
  - MarketRegimeEngine
  - RiskAgent

---

## 9. Fallback 與 Cache 規則

```text
官方來源 → 次級來源 → 本地快取
````

資料中斷 → 降級運行或暫停交易。

---

## 10. 治理總結

* 新資料 → 先更新本文件
* 文件未列 → 禁止使用
* 文件高於程式碼

---

## 11. 一句話總結

> **在 TAITS 中，
> 資料不是「拿來就用」，
> 而是「被治理後才准用」。**

---
