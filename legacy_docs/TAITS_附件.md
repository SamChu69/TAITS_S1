# 📘 TAITS — Taiwan Alpha Intelligence Trading System  
### 世界級智能量化交易系統（Final Full Version）

TAITS（Taiwan Alpha Intelligence Trading System）是一套 **完整的、模組化的、AI 驅動的、專為台股設計的智能量化交易系統**，  
支援：

- 台股現股 / 零股  
- 台指期 / 選擇權  
- 355+ 策略  
- 12+1 Agents  
- 纏論（ChanLun）完整解析  
- 多資料來源（Yahoo / TWSE / FinMind / TAIFEX / News / Sentiment / Macro）  
- GPT / DeepSeek / Qwen / Gemini 等多 AI 模型  
- 回測（Backtest）/ 模擬（Paper）/ 實盤交易（Live）

**這是一套真正可落地的量化交易系統。**

---

## 🚀 功能特色（Features）

### 🧠 1. Multi-Agent Decision System（12+1 Agents）

TAITS 的 AI 決策大腦由多個 Agents 組成：

- TechnicalAgent（技術面）  
- ChipAgent（籌碼：三大法人）  
- FundamentalAgent（基本面）  
- DerivativesAgent（期貨 / 選擇權）  
- NewsAgent（新聞語意分析）  
- SentimentAgent（市場情緒：PTT / Dcard / Google Trend）  
- MacroAgent（宏觀：SOX / VIX / 匯率）  
- EventAgent（財報 / 法說 / 停牌 / 重大事件）  
- RiskAgent（風控 / 法規 / 曝險控制）  
- AIModelAgent（FastBrain / SlowBrain 輸出整合）  
- ChanAgent（纏論結構判斷）  
- SummaryAgent（產生人類可讀的中文解釋）  
- MetaAgent（多 Agent 矛盾調節、權重調整）

---

### 📊 2. 355+ 策略（Strategy Universe）

策略涵蓋 12 大類：

- 趨勢（MA / EMA / GMMA / ADX…）  
- 動能（RSI / MACD / ROC…）  
- 反轉（K 線、背馳）  
- 波動（ATR / 布林帶）  
- 成交量（OBV、量縮/量增）  
- 籌碼（三大法人、集中度）  
- 基本面（EPS、營收 YoY/MoM、毛利率、ROE）  
- 新聞 / Sentiment（AI 語意分類）  
- 宏觀（VIX / SOX / 匯率 / 利率）  
- 衍生品（期貨多空強度、OI、PCR、IV、MaxPain）  
- AI 推理策略（由 LLM 輸出）  
- ⭐ 纏論策略（分型 / 筆 / 線段 / 中樞 / 背馳 / 趨勢段等 ~35 策略）

詳細列表請見：  
`docs/strategies/TAITS_Strategy_Universe_Complete.md`

---

### 🔍 3. 指標層（Indicators + ChanLun）

系統內建多層指標：

- 技術指標：MA、EMA、RSI、MACD、ATR、BBands、OBV…  
- 籌碼指標：外資 / 投信 / 自營商買賣超、集中度等  
- K 線形態：Hammer、Engulfing、Doji 等  
- 成交量與波動性指標  

以及完整 **纏論解析系統（ChanLun Module）**：

- 分型偵測（頂分型 / 底分型）  
- 筆（Bi）生成  
- 線段（Segment）生成  
- 中樞（Zhongshu）偵測  
- 背馳（Divergence）判斷  
- 趨勢段（Trend Segment）分析  

這些結構信號提供給：

- ChanLun Strategies  
- ChanAgent  
- Fusion Engine 進行「結構優先」決策調整。

---

### 🎯 4. Fusion Engine（最終決策大腦）

Fusion Engine 負責整合：

- 所有策略的訊號與信心  
- 所有 Agents 的多空判斷  
- 市場 Regime（市場狀態）  
- AI 推理（AIModelAgent）  
- Override（Event / Risk / Derivatives / ChanLun 結構）  

輸出統一格式：

```json
{
  "final_bias": "BUY",
  "confidence": 0.82,
  "reason": "綜合策略、Agents 與市場結構，目前仍為多頭趨勢，但需留意衍生品與宏觀風險。"
}


---

📈 5. Backtest & Paper Trading

價格事件驅動回測

手續費 / 交易稅 模型

滑價模型（Slippage）

部分成交、撮合模擬

存活者偏差修正（Survivorship Bias Filter）

多標的 Portfolio 回測


Backtest 結果可產出：

CAGR / Max Drawdown / Sharpe / Win Rate

持股分佈 / 回撤曲線

每策略貢獻度



---

💰 6. Live Trading（TWSE 合規）

Trading Layer 支援：

富邦證券 API（Fubon Neo / OpenAPI）

台股價格跳動（Tick Size）

盤中 / 盤後 / 零股 / 整股制度

TAIFEX 台指期 / 選擇權 資料

下單管理（order manager）：

新單 / 改單 / 刪單

重試與補單

委託狀態追蹤


風控（risk manager）：

單股曝險上限

單日最大虧損

整體 Portfolio 熱度控管

觸發熔斷 / 緊急平倉機制




---

🧾 7. 自動報告（TXT / JSON / Markdown）

每次執行 TAITS，可自動產出報告（位於 /output/）：

*.txt：人類可讀簡單摘要

*.json：完整結構化結果（便於整合到其他系統）

*.md：Markdown 報告（含表格、五根 K 線摘要、JSON 段落）


報告內容包括：

最終決策（Bias / Confidence）

市場狀態（Regime）

各策略輸出明細

各 Agent 意見

近期價格摘要（最後 5 根 K 線）

完整 JSON Debug 區塊



---

📁 專案結構（Project Structure）

TAITS/
│── main.py                    # 系統入口：Backtest / Paper / Live
│── config.yaml                # 全域設定
│
├── config/                    # 設定模組（API Key、AI 模型配置...）
├── data_sources/              # 資料來源（Yahoo/TWSE/FinMind/TAIFEX/News...）
├── indicators/                # 技術指標 + 籌碼 + 纏論
├── strategies/                # 355+ 策略（含纏論策略）
├── agents/                    # 12+1 多智能體
├── models/                    # FastBrain / SlowBrain / AI Router
├── engine/                    # Orchestrator / Managers / Fusion / Regime
├── backtest/                  # 回測系統
├── trading/                   # 下單系統（Broker / Risk / Sandbox）
├── monitoring/                # log / metrics / alerts
├── ui/                        # Streamlit Dashboard 與視覺化
└── docs/                      # 所有架構與規格文件

詳細架構說明請見：
docs/architecture/TAITS_Full_System_Architecture.md


---

🔄 系統流程（System Flow）

flowchart TD

    A[Data Sources] --> B[Indicators + ChanLun]
    B --> C[Strategies (355)]
    C --> D[Multi-Agent System (12+1)]
    D --> E[Market Regime Engine]
    E --> F[Fusion Engine]
    F --> G[Risk Engine]
    G --> H{Backtest / Paper / Live}
    H --> I[Reports / UI / Alerts]


---

▶️ 如何執行（Quick Start）

1. 安裝依賴套件

pip install -r requirements.txt

2. 設定環境

編輯 config.yaml，至少確認：

預設模式（backtest / paper / live）

預設標的（例如 2330）

資料期間（start / end）

若使用 API：填入富邦 API、OpenAI / DeepSeek API Key 等（不要 commit 到 public repo）


3. 執行主程式

python main.py

執行完成後，可在 output/ 看到：

*_TAITS_S1_Report.txt

*_TAITS_S1_Report.json

*_TAITS_S1_Report.md



---

📡 資料來源（Data Sources）

TAITS 使用多重資料來源與 fallback 機制，包含（但不限於）：

Yahoo Finance（股價歷史資料）

TWSE / TPEX（官方股價 / 三大法人）

FinMind（延伸財金資料）

TAIFEX（期貨 / 選擇權）

新聞：Cnyes, Yahoo News, MOPS 公開資訊觀測站

Sentiment：PTT / Dcard / Google Trend

Macro：SOX / Nasdaq / S&P500 / VIX / USD/TWD 等


詳細列表與用途請見：
docs/architecture/TAITS_DataSource_and_Reasoning_Map.md


---

🤖 AI 模型（AI Models）

TAITS 支援多種 LLM 與本地模型：

類型	範例模型	用途

FastBrain	DeepSeek, Qwen 系列	新聞分類、情緒分析、大量短文本處理
SlowBrain	GPT-4.1 / GPT-5, Gemini	財報解讀、法說會摘要、宏觀風險評估
Local	Llama / Qwen 本地模型	隱私任務、內部 log 分析（可選）


AI 相關設定集中於：
config/ai_models.yaml
詳細設計請見：
docs/architecture/TAITS_AI_Design_and_Router.md


---

📚 文件（Documentation）

主要文件入口：

系統總體架構：
docs/architecture/TAITS_Full_System_Architecture.md

資料來源與推理地圖：
docs/architecture/TAITS_DataSource_and_Reasoning_Map.md

Multi-Agent 深度規格：
docs/architecture/TAITS_Agent_System_DeepSpec.md

Fusion & Regime 設計：
docs/architecture/TAITS_Fusion_Engine_and_Regime_Spec.md

AI 設計 & Router：
docs/architecture/TAITS_AI_Design_and_Router.md

策略全集（355+）：
docs/strategies/TAITS_Strategy_Universe_Complete.md



---

🤝 貢獻（Contributing）

若要參與 TAITS 的開發，請先閱讀：

CONTRIBUTING.md

CHANGELOG.md


規範包含：

程式風格（Python + 中文註解）

檔案與模組放置位置

策略 / Agent / Indicator 的插件化標準

單元測試需求



---

📄 授權（License）

本專案採用 MIT License。
詳見：LICENSE


---

🎉 結語

TAITS 是一套為 台灣市場 量身打造的智能交易系統，
結合：

嚴謹架構設計

多資料來源

多策略、多智能體

纏論結構分析

AI 語意推理


目標不是短線賭博，而是建立一套 長期可維護、可擴展、可解釋 的專業級交易基礎建設。

若你正在尋找一套可以從「個人專案」成長到「專業資產管理系統」的架構，
TAITS 正是為此而設計。

---

你現在可以先在 GitHub 新增這個 `README.md`。  
完成後跟我說一聲：

> 「README 貼好了」

我就帶你進入下一個檔案：`requirements.txt`。0
