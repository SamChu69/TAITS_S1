# TAITS — Taiwan Alpha Intelligence Trading System  
### 世界級智能量化交易系統（Final Full Version）

TAITS（Taiwan Alpha Intelligence Trading System）是一套 **完整的 AI 驅動多因子量化交易平台**，專為 **台灣證券市場（TWSE）與台指期 / 選擇權（TAIFEX）** 所打造。

系統涵蓋：

- 28+ 種資料來源（Yahoo / TWSE / FinMind / TAIFEX / News / Macro / Sentiment…）  
- 355+ 策略（包含完整 V3.1 285 策略 + 纏論 ChanLun 全集）  
- 多智能體決策系統（12+1 Multi-Agent）  
- AI Router（支援 GPT / DeepSeek / Qwen / Gemini）  
- 纏論引擎（分型 / 筆 / 線段 / 中樞 / 背馳）  
- Backtest / Paper Trading / Live Trading（TWSE 合規）  
- 全自動文字報告（TXT / JSON / Markdown）  
- Streamlit 互動式儀表板 UI

---

# 📘 1. 系統定位（What is TAITS?）

TAITS 不只是技術指標堆疊，而是一套 **結合 AI + 量化 + 纏論 + 法規合規** 的完整交易系統。

核心目標：

1. **在台股市場提供可解釋的 AI 交易決策**。  
2. **永不依賴單一資料來源（具備 Fallback + Cache）**。  
3. **通過多智能體（Multi-Agent）融合訊號並量化信心**。  
4. **以 Fusion Engine 輸出可落地的 BUY / SELL / HOLD 決策**。  
5. **遵守台灣市場法規（TWSE & TAIFEX）並提供完整風控。**

---

# 📂 2. 專案結構（Project Directory）

```
TAITS/
│── README.md                 # 專案總介紹（本檔案）
│── requirements.txt          # Python 套件需求
│── LICENSE                   # MIT 授權
│── CONTRIBUTING.md           # 開發者指南
│── CHANGELOG.md              # 更新紀錄
│── .gitignore                # Git 排除設定
│
├── config/
├── data_sources/             # Yahoo/TWSE/FinMind/TAIFEX/Macro/Sentiment
├── indicators/               # 技術指標 + 籌碼 + 纏論（ChanLun）
├── strategies/               # 355 策略全集
├── agents/                   # 12+1 Multi-Agent 系統
├── models/                   # FastBrain/SlowBrain/AI Router
├── engine/                   # Fusion / Regime / Risk / Report / Orchestrator
├── backtest/                 # 回測系統
├── trading/                  # 實盤交易（TWSE 合規）
├── monitoring/               # Log / Metrics / Alerts
└── ui/                       # Streamlit Dashboard
```

---

# 🧠 3. 多智能體決策系統（Multi-Agent System）

TAITS 由 **12+1 個 Agents** 組成，每個負責不同面向：

- 技術面 Agent  
- 籌碼 Agent  
- 基本面 Agent  
- 新聞 Agent（AI 分析）  
- Sentiment Agent（PTT/Dcard/Google）  
- 宏觀 Agent  
- 衍生品 Agent（期權/期貨）  
- 事件 Agent（財報/法說/停牌）  
- 風控 Agent  
- AI Model Agent（GPT/DeepSeek）  
- ChanLun Agent（纏論）  
- Meta Agent（矛盾調節）  
- Summary Agent（自然語言解釋）

所有 Agents 結果將被送入 Fusion Engine。

---

# 🧩 4. 策略宇宙（Strategy Universe）

TAITS 共包含：

### **📌 355 策略**
- 285 策略（TAITS V3.1 原始全集）  
- 102 擴增策略（Trend/Momentum/Chip/Macro/Derivatives…）  
- 35 纏論策略（分型/筆/線段/中樞/背馳）

策略層的輸出標準格式：

```json
{
  "name": "MACD Momentum",
  "signal": "BUY",
  "confidence": 0.72,
  "reason": "MACD 金叉 + 上升動能擴張"
}
```

完整內容請參考：

```
/docs/strategies/TAITS_Strategy_Universe_Complete.md
```

---

# 🔮 5. AI 系統（AI Router / FastBrain / SlowBrain）

TAITS 內建 AI Router，負責：

- 根據任務自動選模型  
- 控制 Token 成本  
- 整合多模型（GPT、DeepSeek、Qwen、Gemini）

用途包含：

- 新聞判斷  
- 法說會摘要  
- 宏觀語意分析  
- 策略理由生成  
- Report Summary（自然語言報告）

詳細規格請見：

```
docs/architecture/TAITS_AI_Design_and_Router.md
```

---

# ⚙️ 6. Fusion Engine（最終決策大腦）

Fusion Engine 接收：

- 所有策略（355）  
- 所有 Agents（12+1）  
- 市場 Regime（12 種）  
- AI Reasoning（SlowBrain 推理）  
- Override（事件、風控、衍生品、纏論）

並輸出：

```json
{
  "final_bias": "BUY",
  "confidence": 0.81,
  "reason": "技術面多頭，籌碼轉強，纏論維持多頭趨勢段"
}
```

是 TAITS 的核心大腦。

---

# 📈 7. 回測（Backtesting）

功能包含：

- 日 / 5 分Ｋ 回測  
- 手續費 / 滑價 / 交易稅  
- 部分成交  
- 多標的 portfolio 回測  
- 存活者偏差修正  
- Streamlit 視覺化績效報告  

---

# 💹 8. 實盤交易（Live Trading）

- 富邦證券 API（Fubon API）  
- TWSE tick size 自動計算  
- 零股制度  
- 下單風控（部位上限、停損、熔斷）  

---

# 📜 9. 自動報告（Report System）

系統可自動輸出：

```
output/
    ├── 2330_20251211_final.json
    ├── 2330_20251211_report.txt
    └── 2330_20251211_TAITS_Report.md
```

Markdown 報告包含：

- 市場狀態  
- 策略信號  
- Agents 意見  
- 五根 K 線摘要  
- JSON 結構  

---

# 🖥 10. UI（Streamlit Dashboard）

包含：

- K 線（含技術指標 + 纏論結構）  
- Agents 面板  
- 策略信號面板  
- 最終交易建議  
- 回測績效圖表  

---

# ▶️ 11. 如何執行（Run TAITS）

安裝套件：

```
pip install -r requirements.txt
```

執行：

```
python main.py
```

---

# 📚 12. 文件（Docs）

所有文件在 `/docs/`：

- architecture/  
- strategies/  
- diagrams/  
- spec_original/（歷史規格）  

---

# 🤝 13. 開發指南

請見：

```
CONTRIBUTING.md
```

---

# 📄 14. 授權（License）

本專案採用 MIT 授權：

```
LICENSE
```

---

# 🎉 結語

TAITS 是一套真正為 **台灣市場量身打造的 AI 量化交易系統**，  
融合：

- AI 推理  
- 多智能體  
- 量價結構  
- 纏論  
- 籌碼  
- 宏觀  
- 衍生品  
- TWSE 法規合規  

未來將持續擴展更多模型、更多策略、更多智能。

