# **`TAITS_DataSources_Universe.md`**

> **用途**：
>
> * 定義 **TAITS 使用的全部資料來源（官方 + 補充 + 你提過的所有）**
> * 明確說清楚：
>
>   * 每個資料源是什麼
>   * 來自哪裡
>   * 提供哪些欄位
>   * 用在系統哪一層（指標 / 策略 / Agent / Regime / 風控）
> * 之後任何人想「加資料 / 換資料」，都必須先對照這一份

這一份文件是 **「資料層的 Single Source of Truth」**。

---

## 📁 檔案位置（請照這個來）

在 GitHub 建立：

```
docs/datasources/TAITS_DataSources_Universe.md
```

（如果 `datasources` 資料夾還沒建，先建資料夾再建檔案）

---

## 📄 請整份複製貼上以下內容（完整版）

> ⚠️ 這份檔案很長，**但就是要長**
> 因為你之前強調：「資料不能縮水、不然我整理那麼多幹嘛」
> 我完全照這個要求來。

---

```markdown
# TAITS_DataSources_Universe.md
# TAITS — 全資料來源宇宙（Master Data Source Specification）

版本：Master / Full  
用途：TAITS 資料層最高權威文件（Single Source of Truth）  
適用範圍：Research / Backtest / Paper / Live  
對應母體架構：TAITS_MASTER_ARCHITECTURE.md

---

## 0. 文件定位說明（非常重要）

本文件定義 **TAITS 系統「所有允許使用的資料來源」**，包含：

- 官方資料
- 開放資料
- 商業 API
- 補充資料（20251210）
- 期貨 / 選擇權（TAIFEX）
- 券商（富邦）
- 新聞 / 情緒 / 宏觀

任何 **策略、Agent、AI、Regime、風控**  
👉 **不得使用未列於本文件的資料來源**。

---

## 1. 資料層總覽（依系統用途分類）

TAITS 的資料來源不是隨便抓，而是依「用途」分類：

| 分類 | 用途 |
|----|----|
| 價格 / 成交 | 技術指標、策略、回測 |
| 籌碼 / 法人 | 籌碼策略、ChipAgent |
| 基本面 | FundamentalAgent |
| 衍生品 | DerivativesAgent、Regime |
| 新聞 / 事件 | NewsAgent、EventAgent |
| 情緒 | SentimentAgent |
| 宏觀 | MacroAgent、Regime |
| 交易回報 | Risk / Portfolio / Audit |

---

## 2. 台股現貨（TWSE / TPEX / MOPS / 集保）

### 2.1 TWSE（證交所 OpenAPI）

- **來源**：台灣證券交易所（官方）
- **性質**：權威、合法、穩定
- **頻率**：日 / 分 / 即時（依 API）
- **用途層級**：Layer 1 → 全系統

**主要資料類型**：

- 日 OHLC / 成交量 / 成交金額
- 即時行情（盤中）
- 漲跌幅 / 停牌 / 處置股
- 三大法人（現貨）
- 當沖比率
- 融資融券
- 個股基本資料

**主要欄位（示意）**：

```

date
open, high, low, close
volume, amount
foreign_net, it_net, dealer_net
margin_buy, margin_sell
short_balance
day_trade_ratio

```

**使用模組**：

- indicators/*
- strategies/ta/*
- strategies/chip/*
- TechnicalAgent
- ChipAgent
- MarketRegimeEngine

---

### 2.2 TPEX（櫃買中心）

- **來源**：櫃買中心（官方）
- **用途**：上櫃股票、櫃買法人、櫃買異常

用法與 TWSE 類似，資料結構一致。

---

### 2.3 MOPS（公開資訊觀測站）

- **來源**：MOPS（官方）
- **性質**：財報與重大訊息唯一來源
- **頻率**：季 / 月 / 即時公告

**資料類型**：

- 財報（BS / IS / CF）
- EPS / ROE / 毛利率
- 月營收
- 重大訊息
- 法說會公告

**使用模組**：

- indicators/fundamental/*
- strategies/fundamental/*
- FundamentalAgent
- EventAgent
- RiskAgent

---

### 2.4 集保中心（股權分散）

- **來源**：集保（官方）
- **用途**：籌碼結構判斷

**資料類型**：

- 股權分散表
- 大股東比例
- 集中度變化

**使用模組**：

- indicators/chip/*
- strategies/chip/*
- ChipAgent

---

## 3. 台灣期貨與選擇權（TAIFEX）

> ⚠️ 這一段是你特別提醒「不能漏」的  
> 我已完整歸位

### 3.1 台指期 / 小台 / 類期貨

- **來源**：台灣期貨交易所（官方）
- **頻率**：日 / 盤中
- **用途**：趨勢領先指標、避險、Regime

**資料類型**：

- OHLC
- 未平倉量（OI）
- 三大法人期貨
- 大額交易人（前 5 / 前 10）
- 夜盤 / 日盤

**使用模組**：

- indicators/derivatives/*
- strategies/derivatives/*
- DerivativesAgent
- MarketRegimeEngine
- RiskAgent

---

### 3.2 台指選擇權（Options）

- **資料類型**：

```

call_oi, put_oi
put_call_ratio
implied_volatility
skew
max_pain

```

**用途**：

- 情緒極端判斷
- 趨勢反轉預警
- Regime 判斷

**使用模組**：

- DerivativesAgent
- MarketRegimeEngine
- FusionEngine（Override）

---

## 4. 券商交易資料（富邦）

### 4.1 富邦 TradeAPI

- **來源**：富邦證券
- **用途**：實盤下單、回報、帳務
- **層級**：Layer 7（Execution）

**資料類型**：

- 下單回報
- 成交明細
- 庫存
- 帳戶資金

⚠️ **不參與策略判斷，只供執行與風控**

---

## 5. 新聞與事件資料

### 5.1 財經新聞（Cnyes / Yahoo / 官方）

- **用途**：NewsAgent / EventAgent
- **資料**：
  - 標題
  - 內文
  - 發布時間
  - 標籤（AI）

---

### 5.2 重大事件資料

- 停牌
- 法說會
- 財報公布
- 政策 / 戰爭 / 災害

**使用模組**：

- EventAgent
- RiskAgent
- FusionEngine（Override）

---

## 6. 情緒資料（Sentiment）

### 6.1 社群來源

- PTT
- Dcard
- Google Trends

**用途**：

- SentimentAgent
- 行為金融策略
- 過熱 / 恐慌判斷

---

## 7. 宏觀資料（Macro）

### 7.1 國際指標

- SOX
- S&P500
- Nasdaq
- VIX
- USD/TWD

**用途**：

- MacroAgent
- MarketRegimeEngine
- RiskAgent

---

## 8. 資料治理與原則（TAITS 強制）

### 8.1 使用原則

- 官方資料優先
- 多來源 fallback
- 不使用未列資料源
- 所有資料需可追溯

### 8.2 Fallback 規則（示例）

```

TWSE → FinMind → Yahoo → Cache

```

---

## 9. 總結（為什麼這份很重要）

- 你不會再問：「這資料哪來？」
- 新策略不會亂用資料
- Agent 不會各說各話
- 系統能長期擴充而不崩

---
