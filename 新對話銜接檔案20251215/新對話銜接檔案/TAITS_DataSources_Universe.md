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

# 【TAITS 資料來源全量補齊與用途定位】
## 版本：v2025-12-16
## 性質：Only-Add（追加，不覆蓋既有內容）

本章節用於「一次性說清楚」TAITS **所有資料從哪來、用來幹嘛、在哪一層使用、是否可交易**，
避免新對話或未來擴充時出現「來源不明 / 用途混亂 / 誤用下單」的風險。

---

## 一、資料用途總則（母體硬規則）

### 1. 資料用途分類（四選一或多選）
所有資料在 TAITS 中必須被標註以下用途之一：
- Market Regime Evidence（市場狀態證據）
- Cross-Market Filter（跨市場濾網）
- Weight Adjuster（權重調整）
- Risk Override（風險覆蓋）

### 2. Observe-only 硬規則（你反覆要求）
以下資料 **僅能觀察，不得成為下單標的**：
- 期貨（Futures）
- 選擇權（Options）
- 融資融券（Credit）

任何未來若要交易上述商品，**必須新增獨立授權與合規章節**。

---

## 二、官方市場資料來源（Primary / 官方）

### 2.1 TWSE（台灣證券交易所）
- 名稱：TWSE OpenAPI
- 官方入口：https://openapi.twse.com.tw/
- 資料類型：
  - 股票日資料（OHLCV）
  - 指數資料
  - 成交量/成交額
  - 證交所公告
- 用途定位：
  - Market Regime Evidence
  - Strategy Input
- 使用層級：
  - L1（接入）
  - L2（正規化）
  - L3（快照）
  - L4（特徵）
- 驗收：
  - 任一日資料可回查官方端點 + 日期

---

### 2.2 TPEx（櫃買中心）
- 名稱：TPEx OpenAPI
- 官方入口：https://www.tpex.org.tw/openapi/
- 資料類型：
  - 上櫃股票資料
  - 產業分類
- 用途定位：
  - Strategy Input
  - Universe 建立
- 使用層級：
  - L1 / L2 / L3 / L4
- 驗收：
  - 上櫃標的與上市標的欄位一致

---

### 2.3 TAIFEX（台灣期貨交易所）
- 名稱：TAIFEX OpenAPI
- 官方入口：https://openapi.taifex.com.tw
- 資料類型（Observe-only）：
  - 指數期貨
  - 個股期貨（若可得）
  - 選擇權成交量 / OI
- 用途定位：
  - Market Regime Evidence
  - Risk Override
- 使用層級：
  - L1（接入）
  - L4（Observe-only 特徵）
  - L6（Regime 輔助）
  - L7（風控覆蓋）
- 硬限制：
  - ❌ 不得觸發期貨/選擇權下單
- 驗收：
  - 任一風險覆蓋可回查 TAIFEX 來源

---

### 2.4 MOPS（公開資訊觀測站）
- 名稱：MOPS
- 官方入口：https://mopsov.twse.com.tw/mops/web/index
- 資料類型：
  - 重大訊息
  - 財報
  - 法說
- 用途定位：
  - Fundamental Evidence
  - Event Trigger
- 使用層級：
  - L1 / L2 / L3 / L4 / L5
- 驗收：
  - 任一事件可回查公告原文 URL

---

## 三、新聞與題材資料來源（非官方，但必要）

### 3.1 新聞（News）
- 來源類型：
  - 主流財經媒體
  - 產業新聞
- 資料內容：
  - 標題
  - 發布時間
  - 來源
  - 關聯公司/產業
- 用途定位：
  - Event Flag
  - Narrative Evidence
- 使用層級：
  - L1 / L4 / L5 / L8 / L10
- 驗收：
  - 每則新聞必有來源 URL

---

### 3.2 社群與討論熱度（Social / Forum）
- 來源類型：
  - 社群平台
  - 投資討論區
- 資料內容：
  - 關鍵字頻率
  - 情緒偏向（不要求準確，只要求顯示）
- 用途定位：
  - Heat Score
  - Rumor Risk Tag
- 使用層級：
  - L4 / L5 / L8
- 重要原則：
  - 不用來下單
  - 只用來提示「過熱/謠言風險」

---

## 四、Observe-only 衍生品與信用資料（重點）

### 4.1 期貨（Futures）
- 來源：
  - TAIFEX
- 觀察項目：
  - 趨勢方向
  - 波動擴張
  - 急轉折
- 影響：
  - Regime 判定
  - 禁止追價
- 禁止：
  - ❌ 期貨下單

---

### 4.2 選擇權（Options）
- 來源：
  - TAIFEX
- 觀察項目：
  - OI 壓力
  - 結算釘住風險
- 影響：
  - Exit Priority
  - 波動風險標籤

---

### 4.3 融資融券（Credit）
- 來源：
  - 證交所 / 櫃買
- 觀察項目：
  - 融資使用率
  - 融券比率
- 影響：
  - 槓桿過熱警示
  - 踩踏風險提示

---

## 五、資料完整性與審計要求（強制）

### 5.1 每筆資料必備欄位
- source_ref（來源 URL / API）
- captured_at（抓取時間）
- data_time（資料所屬時間）
- batch_id

### 5.2 快照要求
- 任何影響決策的資料，必須進入 Snapshot
- Snapshot 必須列出：
  - 使用哪些官方/非官方來源
  - 缺失哪些資料

---

## 六、總結（母體約束）

- TAITS **不因資料難用而忽略**
- TAITS **不因資料非官方而否定**
- TAITS **只顯示證據與風險，決策權在你**

---

# 【End of TAITS_DataSources_Universe 補齊】

