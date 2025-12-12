# TAITS — Taiwan Alpha Intelligence Trading System  
### 世界級智能量化交易系統（Final Full Version）

TAITS（Taiwan Alpha Intelligence Trading System）是一套  
**專為台股 + 台指期 + 選擇權打造的 AI 驅動智能量化交易系統**。

它結合：

- 多資料來源（Yahoo / TWSE / FinMind / TAIFEX / Cnyes / Sentiment / Macro…）
- 355+ 策略（含 纏論 ChanLun 完整策略）
- 12+1 Multi-Agent 決策系統
- AI 模型（GPT / DeepSeek / Qwen / Gemini）
- Backtest / Paper Trading / Live Trading（支援 TWSE / TAIFEX 規則）
- 自動報告（TXT / JSON / Markdown）
- 可視化儀表板（Streamlit UI）

目標是為 **台灣市場** 提供一套「真正可落地的世界級智能交易系統」。

---

## 🔍 系統特色（Key Features）

### 🧠 1. Multi-Agent Decision System（12+1 Agents）

TAITS 不依賴單一模型，而是由多個專業 Agent 協作完成決策：

- TechnicalAgent：技術面（MA / EMA / RSI / MACD / 趨勢結構）
- ChipAgent：三大法人籌碼（外資 / 投信 / 自營）
- FundamentalAgent：基本面（營收 / EPS / ROE / 財報）
- NewsAgent：新聞情緒（AI 分析新聞與重訊）
- SentimentAgent：市場情緒（PTT / Dcard / Google Trend）
- MacroAgent：宏觀環境（SOX / VIX / 匯率 / 指數）
- DerivativesAgent：期貨 / 選擇權（OI / PCR / IV / MaxPain）
- EventAgent：重大事件（財報、法說會、停牌、戰爭、災害）
- RiskAgent：風控與曝險管理
- AIModelAgent：FastBrain / SlowBrain AI 輸出整合
- ChanAgent：纏論結構判讀（分型 / 筆 / 線段 / 中樞 / 背馳）
- SummaryAgent：把決策過程翻譯成「人類讀得懂的中文」
- MetaAgent：在多 Agent 意見矛盾時做高階協調（可選）

每個 Agent 都輸出標準結構：

```python
{
  "name": "TechnicalAgent",
  "bias": "BULL" / "BEAR" / "NEUTRAL",
  "confidence": 0.0 ~ 1.0,
  "comment": "中文摘要說明"
}
````

---

### 📊 2. 策略宇宙（Strategy Universe，355+）

策略涵蓋 12 大族群，包含：

* 趨勢策略（MA / EMA / GMMA / ADX …）
* 動能策略（RSI / MACD / ROC …）
* 反轉策略（K 線反轉 / 背馳 / 超買超賣）
* 波動策略（ATR / 布林帶）
* 成交量策略（OBV / 量縮 / 量增）
* 籌碼策略（三大法人、集中度、分點結構）
* 基本面策略（EPS、營收 YoY / MoM、毛利率、ROE）
* 新聞策略（AI 標記利多 / 利空 / 中性）
* 行為 / Sentiment 策略（散戶情緒過熱 / 恐慌）
* 宏觀策略（SOX / VIX / 指數聯動 / 匯率）
* 衍生品策略（期貨多空強度 / OI / PCR / IV / MaxPain）
* ⭐ 纏論策略（分型 / 筆 / 線段 / 中樞 / 趨勢段 / 背馳 等）

詳細策略列表請參考：

`docs/strategies/TAITS_Strategy_Universe_Complete.md`

---

### 🔍 3. 指標層（Indicators + ChanLun）

TAITS 指標層涵蓋：

* 一般技術指標（MA / EMA / RSI / MACD / ATR / BBands / OBV…）
* 籌碼指標（三大法人買賣超、集中度）
* K 線型態（Hammer / Engulfing / Doji…）
* 波動與風險指標
* 纏論（ChanLun）專屬指標與結構標記：

  * 分型偵測（頂分型 / 底分型）
  * 筆（Bi）生成
  * 線段生成
  * 中樞辨識
  * 背馳判定（價 vs 量 vs 指標）
  * 趨勢段（Trend Segment）分析

這些欄位會寫回 DataFrame，提供策略與 Agents 使用。

---

### 🎯 4. Fusion Engine（最終決策大腦）

Fusion Engine 會整合：

1. 355+ 策略的輸出
2. 12+1 Agents 的判斷
3. 市場 Regime（12 類市場狀態）
4. AIModelAgent 的語意推理
5. Override 信號：

   * Event Override（重大利空 / 黑天鵝）
   * Risk Override（風險超標 / 市場高風險）
   * Derivatives Override（期權結構極端）
   * ChanLun Override（中樞背馳 / 趨勢段結束）

最終輸出標準結構：

```python
{
  "final_bias": "BUY" / "SELL" / "HOLD",
  "confidence": 0.0 ~ 1.0,
  "reason": "中文綜合說明",
  "debug": { ... 各模組貢獻度 ... }
}
```

---

### 📈 5. Backtest / Paper Trading / Live Trading

TAITS 支援三種模式：

* Backtest：歷史回測
* Paper Trading：模擬撮合（不下真單）
* Live Trading：實盤（支援富邦 API）

回測層具備：

* 價格事件驅動（Event-driven）
* 手續費 / 交易稅模型（含台股、台指期）
* 滑價模型
* 部分成交模擬
* 存活者偏差處理（退市 / 成分變化）
* 多標的 Portfolio 測試

---

### 💰 6. TWSE / TAIFEX 合規交易層

Trading Layer 嚴格遵守台灣市場規則：

* 台股：

  * 交易時間 / 漲跌幅限制
  * 價格跳動（tick size）
  * 整股 / 零股制度
* 期貨 / 選擇權（TAIFEX）：

  * 保證金 / 乘數
  * 結算週期
  * 交易時間與熔斷制度

搭配：

* `OrderManager`：統一下單與委託管理
* `RiskManager`：實盤級風控（單筆 / 單日 / 總體風險）
* `broker_fubon.py`：富邦 API 封裝（未來接戰略交易）

---

### 🧾 7. 自動報告輸出（TXT / JSON / Markdown）

Orchestrator 執行後，會產生標準化 `result` 結構，
並由 ReportFormatter / MarkdownReportFormatter 生成：

* 純文字報告（TXT）
* 結構化資料（JSON）
* 觀察用 Markdown 報告（MD）

內容包含：

* 標的資訊與市場 Regime
* 策略層結果（表格）
* Agents 層結果（表格）
* 最後 5 根 K 線摘要
* 完整 JSON Debug 區段

---

## 📁 專案結構（Project Structure）

專案主體目錄如下（簡化版）：

```text
TAITS/
│── main.py
│── config.yaml
│── README.md
│── requirements.txt
│
├── config/
├── data_sources/
├── indicators/
├── strategies/
├── agents/
├── models/
├── engine/
├── backtest/
├── trading/
├── monitoring/
└── ui/
```

詳細架構說明請見：

`docs/architecture/TAITS_Full_System_Architecture.md`

---

## ▶️ 如何啟動（Quick Start）

### 1. 安裝依賴套件

```bash
pip install -r requirements.txt
```

### 2. 設定 `config.yaml`

* 預設交易模式（backtest / paper / live）
* 預設標的（例如 2330）
* 日期區間
* API 金鑰（若使用 FinMind / 富邦）

### 3. 執行主流程

```bash
python main.py
```

執行後，系統會：

1. 讀取資料（Yahoo / TWSE / FinMind / TAIFEX…）
2. 檢查資料品質
3. 計算所有指標（含纏論）
4. 執行 355+ 策略
5. 執行 Multi-Agent 系統
6. 判定市場 Regime
7. 由 Fusion Engine 產生最終決策
8. 產生報告（TXT / JSON / Markdown）

---

## 📡 資料來源（Data Sources）

TAITS 使用多種資料來源，包括但不限於：

* Yahoo Finance（台股歷史價）
* TWSE / TPEX（成交量、三大法人）
* FinMind（延伸技術與財務資料）
* TAIFEX（台指期 / 選擇權 / OI / PCR / IV）
* Cnyes / Yahoo 新聞
* PTT / Dcard / Google Trend（情緒）
* SOX / Nasdaq / S&P500 / VIX / USD/TWD（宏觀）

詳細清單與用途對應請見：

`docs/architecture/TAITS_DataSource_and_Reasoning_Map.md`

---

## 🤖 AI 模型與 Router

TAITS 支援多模型組合：

* FastBrain：DeepSeek / Qwen（大量新聞與情緒分析）
* SlowBrain：GPT / Gemini（法說、財報、宏觀報告與決策解釋）
* Local Models（可選）：LLaMA / Qwen 本地版（隱私任務）

AI Router 會根據：

* 任務類型（新聞分類 / 財報解讀 / 風險評估 / 策略解釋）
* 成本限制
* 敏感資料保護規則

來動態選擇使用哪一個模型。

詳細設計請見：

`docs/architecture/TAITS_AI_Design_and_Router.md`

---

## 📚 文件（Documentation）

所有 TAITS 核心設計文件放在 `docs/` 目錄：

* `docs/architecture/TAITS_Full_System_Architecture.md`
* `docs/architecture/TAITS_Agent_System_DeepSpec.md`
* `docs/architecture/TAITS_Fusion_Engine_and_Regime_Spec.md`
* `docs/architecture/TAITS_DataSource_and_Reasoning_Map.md`
* `docs/architecture/TAITS_AI_Design_and_Router.md`
* `docs/strategies/TAITS_Strategy_Universe_Complete.md`
* `docs/diagrams/*.md`（Mermaid 系統圖）

---

## 🤝 貢獻（Contributing）

若未來有其他工程師參與，請參考：

`CONTRIBUTING.md`

裡面定義了：

* 程式風格與註解規範
* 單元測試要求
* 分支與 PR 流程
* 檔案與模組命名風格

---

## 📄 授權（License）

本專案預設採用 MIT License（可依實際需要調整）。
請見根目錄 `LICENSE`。

---

## 🎯 結語

TAITS 是一套以「**台灣市場實戰**」為核心出發設計的智能交易系統，
不只是回測用玩具，而是：

* 有完整架構
* 有明確風控
* 有 AI + 傳統量化混合
* 有 纏論 ChanLun 結構支援
* 有能力接券商 API 走向實盤

未來你可以在此基礎持續擴充：

* 新策略
* 新資料源
* 新 Agent
* 新 AI 模型

TAITS 的設計目標，是可以長期演進，而不是一次寫完就放著。

```
