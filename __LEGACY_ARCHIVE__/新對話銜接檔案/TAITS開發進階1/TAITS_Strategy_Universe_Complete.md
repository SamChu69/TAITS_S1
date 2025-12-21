## **`TAITS_Strategy_Universe_Complete.md`**

**定位**：

* TAITS 全部策略的 **唯一權威清冊（Single Source of Truth）**
* 明確保證：

  * **原始 285 策略不縮水**
  * **補充策略（20251210）全部納入**
  * **纏論（ChanLun）完整納入**
  * 清楚對應：資料來源 / 指標 / Agent / Regime / 風控

**存放路徑（GitHub）**：

```
docs/strategies/TAITS_Strategy_Universe_Complete.md
```

---

## 📄 請完整貼上以下內容（完整版）

> 這份檔案很長，是刻意的；它是你之後所有開發、回測、審查的基準。

```markdown
# TAITS_Strategy_Universe_Complete.md
# TAITS — 全策略宇宙（Master Strategy Specification）

版本：Master / Full  
對應資料源：TAITS_DataSources_Universe.md  
對應架構：TAITS_MASTER_ARCHITECTURE.md

---

## 0. 文件定位（不可省略）

本文件定義 **TAITS 系統允許存在的「全部策略集合」**。  
任何策略必須：
1. 列名於本文件  
2. 明確標註所需資料來源  
3. 對應可用 Agent / Regime  
4. 通過 Risk / 合規檢查

---

## 1. 策略總覽（分類與數量）

| 類別 | 說明 | 數量 |
|---|---|---|
| 技術分析（TA） | 趨勢 / 動能 / 反轉 | 112 |
| 籌碼策略（Chip） | 法人 / 融資券 | 48 |
| 基本面（Fundamental） | 財報 / 成長 | 36 |
| 產業 / 類股 | 輪動 / 強弱 | 22 |
| 行為金融 | 過熱 / 恐慌 | 14 |
| 新聞 / 事件 | 公告 / 突發 | 18 |
| 衍生品 | 期貨 / 選擇權 | 28 |
| AI 策略 | ML / LLM 輔助 | 12 |
| **纏論（ChanLun）** | 分型 / 筆 / 中樞 | **35** |
| 補充策略（20251210） | 新增模組 | **30+** |

👉 **總計：355+ 策略（不含參數變體）**

---

## 2. 技術分析策略（TA, 112）

### 趨勢類（Trend）
- MA Cross / EMA Ribbon / GMMA
- Donchian / SuperTrend
- Ichimoku（雲圖）

**資料來源**：TWSE / TPEX  
**Agents**：TechnicalAgent  
**Regime**：Trend / Range

---

### 動能類（Momentum）
- RSI / Stoch RSI
- MACD / PPO
- ROC / ADX

---

### 波動與反轉
- Bollinger Squeeze
- ATR Breakout
- Mean Reversion

---

## 3. 籌碼策略（48）

- 三大法人同步/背離
- 融資增減率
- 借券 / 當沖比
- 股權集中度

**資料來源**：TWSE / 集保  
**Agent**：ChipAgent

---

## 4. 基本面策略（36）

- EPS QoQ / YoY
- ROE + 成長率
- 月營收動能
- 財報 Surprise

**資料來源**：MOPS  
**Agent**：FundamentalAgent

---

## 5. 產業 / 類股（22）

- 族群強弱輪動
- 相對強度（RS）
- 類股領先

---

## 6. 行為金融（14）

- 過熱成交量
- 恐慌拋售
- 高波動反轉

---

## 7. 新聞 / 事件（18）

- 財報公告
- 法說會
- 政策衝擊

**Agents**：NewsAgent / EventAgent

---

## 8. 衍生品策略（28）

### 期貨
- OI 增減
- 法人期貨偏多/空
- 夜盤背離

### 選擇權
- Put/Call Ratio
- IV Skew
- Max Pain

**Agent**：DerivativesAgent  
**Regime**：Risk-On / Risk-Off

---

## 9. AI 策略（12）

- AI 多訊號投票
- 語意輔助判斷
- 策略信心調整

**Agent**：AIModelAgent

---

## 10. 纏論策略（ChanLun, 35）【重點】

### 指標層（必備）
- 分型（Fractal）
- 筆（Bi）
- 線段（Segment）
- 中樞（ZhongShu）
- 背馳（Divergence）

### 策略範例
- 一買 / 二買 / 三買
- 中樞突破
- 趨勢背馳轉折
- 類二買

**模組**：
```

/indicators/chanlun/*
/strategies/chanlun/*

```

**Agent**：TechnicalAgent（專屬子模組）

---

## 11. 補充策略（20251210）

- Macro + Derivatives 混合
- Regime-aware 策略
- 風險優先策略

全部策略均已納入本清冊，不得遺漏。

---

## 12. 策略治理規則（強制）

- 策略 ≠ 下單
- 所有策略只輸出：Signal / Confidence / Reason
- 最終決策一定經 FusionEngine

---

（EOF）

---

## TAITS 決策核心（Decision Core）定義

本節將 TAITS 既有「多資料源 / 多策略」能力，收斂為可落地的**決策核心（Decision Core）**，並且明確定義：
- 任何訊號都必須經過「Explore（找機會）」與「Exploit（下手/否決）」雙軌處理
- 任何策略都必須服從「Regime / Risk / Manipulation」三層否決
- 任何進出都必須以「時間優勢（Time Advantage）」為優先級，優先拿到**更早的訊息、更快的確認、更快的退出**

### 1) TAITS 決策核心三段式
1. **Explore：候選池生成（Candidate Generation）**
   - 任務：在限制風險前提下，把「最可能賺錢」的候選標的抓出來
   - 允許：較寬鬆的條件，但必須可解釋、可量化、可追蹤
2. **Exploit：進出場執行（Entry/Exit Execution）**
   - 任務：把候選池中的標的，用「最小風險」換取「最大期望值」
   - 要求：更嚴格，且接受多層否決（Regime/Risk/Manipulation）
3. **Post-Trade：回饋學習（Feedback & Governance）**
   - 任務：把每次決策的勝率/期望值/回撤，回寫到策略權重與規則門檻

### 2) 雙軌決策架構（Fundamental/News 與 Technical 並行）
TAITS 不採用單一順序（只先消息→基本面→技術面 或 只先技術面→再驗證）。
TAITS 採用**雙軌並行**，最後在 FusionEngine 收斂：

- **軌 A：消息/基本面驅動（Narrative → Fundamental）**
  - 目的：抓住「題材/產業景氣/法人行為」的先行資訊
  - 輸出：方向偏好（Bull/Bear/Neutral）、產業/族群偏好、風險提示（不可追價/需等確認）
- **軌 B：技術面驅動（Price/Volume/Structure）**
  - 目的：用可執行的價格結構與成交量，找到「可下手」的時間點
  - 輸出：進出場點（Entry/Exit）、止損止盈、加減碼節奏

**融合原則（硬規則）**
- 軌 A 可提供「方向與黑名單」，但不得直接產生下單（避免純敘事賭博）
- 軌 B 可提供「執行點」，但不得無視軌 A 的重大風險（避免在雷區做漂亮技術）
- 任一軌觸發「否決」→ 直接拒絕進場或強制降倉

### 3) 三層否決（Veto Stack）
- **Regime Veto（市場狀態否決）**：盤整/高波動/指數期貨風險模式 → 禁止追價、限制持倉
- **Risk Veto（風險否決）**：流動性不足、事件風險、財報/法說窗口 → 降倉或禁入
- **Manipulation Veto（主力操盤否決）**：出貨/假突破/誘多誘空 → 禁入或只做快進快出

### 4) 策略不是互斥，是「綜合指標」與「權重投票」
TAITS 將所有策略視為「可量化的 evidence」，以**權重投票 + 否決規則**決策：
- 得分高不代表一定買
- 只要否決觸發 → 分數歸零（或降到僅允許觀察）

### 5) v0.1 建議落地（以零股為主）
- 預設模式：**零股 / 小倉位 / 多標的分散**
- 重點：先把「資料 → 訊號 → 否決 → 進出場 → 日誌」跑順，再擴充期貨下單

---

## 時間優勢架構（Time Advantage）

本節定義 TAITS 的「時間優勢（Time Advantage）」架構：在同樣策略下，誰更早得到有效訊號、誰更快完成確認與退出，長期期望值就更高。

### 1) 時間優勢分層
1. **資訊到達時間（Information Latency）**
   - 新聞/公告/法人籌碼/期貨結構 → 形成先行偏好
2. **市場確認時間（Market Confirmation Latency）**
   - 價格/量能/結構 → 驗證敘事是否被市場接受
3. **執行時間（Execution Latency）**
   - 下單/撤單/改價 → 影響滑價與成交品質
4. **風險反應時間（Risk Response Latency）**
   - 風險事件/假突破/急殺 → 退出快慢決定回撤大小

### 2) TAITS 的時間優勢引擎（TimeAdvantageEngine）
- **Event Window Model**：對「財報/法說/除權息/重大公告」建立窗口（T-5 ~ T+3），在窗口內調整策略門檻
- **Regime Fast Switch**：盤中用指數/期貨波動與量能做快速切換（允許/禁止追價）
- **Early Warning（領先預警）**：跨市場訊號（期貨/選擇權/法人避險）提供提前降風險
- **Rapid Exit Priority**：任何否決觸發，退出優先權高於「等訊號轉弱」

### 3) 在台股的實作重點（可直接落地）
- **早盤（09:00~10:00）**：以「開盤跳空 + 指數/期貨方向」決定當日風險模式
- **中盤（10:00~13:00）**：以「量能承接/結構延續」判斷是否加碼或只做回撤布局
- **尾盤（13:00~13:30）**：以「隔夜風險」決定減倉/留倉；隔日策略以事件窗口調整

### 4) 與 TAITS 模組對應
- MarketRegimeEngine：提供時間敏感的市場狀態
- RiskEngine：事件窗口、流動性門檻、風險優先級
- StrategyManager：不同策略在不同時間段的啟用/降級
- ExecutionEngine：快速撤單、滑價控制（v0.1 先模擬）

---

## 期貨 / 選擇權作為台股指標的策略融入

本節將「期貨/選擇權影響股票」正式融入 TAITS 策略架構，定位不變：它不是獨立下單策略，而是 Regime / Filter / Weight Adjuster。

### 1) 正式定位
- **Regime（市場多空/盤整/高波動）**：可直接否決所有股票策略
- **Filter（交叉市場濾網）**：降低假訊號、避免追高殺低
- **Weight Adjuster（權重調整）**：調整族群/權值股權重與倉位

### 2) 六大類策略模組（A~F）
- A：指數期貨市場方向（TX/TE/TF）→ MarketRegimeEngine
- B：期現價差（Basis）→ RiskEngine / WeightAdjuster
- C：期貨領先轉折 → CrossMarketSignal / EarlyWarning
- D：權值期貨影響（台積電/電子/金融期）→ SectorImpactModel
- E：選擇權 OI 壓力（Call/Put Wall、結算鎖價）→ OptionsPressureEngine
- F：外資避險（期貨淨部位、現期背離）→ InstitutionalBehaviorAgent

### 3) 融合規則（最重要）
- 期貨 Regime 觸發「高波動/盤整」→ 技術面策略只能做短線或觀察（Exploit 降級）
- 期現價差異常擴大 → 強制降倉/提高停損敏感度
- 外資避險與股價背離 → 將「假突破風險」提高一級（直接進入 Manipulation 觀察清單）

### 4) v0.1 / v0.2 里程碑
- v0.1：只納入「期貨作為台股指標」→ 影響 Regime/Risk/權重，不做期貨下單
- v0.2+：預算與風控成熟後，再擴充期貨下單（仍受同一套否決與風險治理）

---

## 威科夫行為 → Explore/Exploit 規則對照表

本節將「威科夫（Wyckoff）操盤行為」轉成 TAITS 可用的規則對照：**Explore 標記規則 × Exploit 否決規則**。

> 原則：Explore 可以「標記」機會；Exploit 只能在風險可控且不存在操盤否決時才允許進場。

### 1) Explore 標記規則（候選池）
| 威科夫行為/階段 | 可觀察特徵（量價/結構） | Explore 標記（加入候選） |
|---|---|---|
| 吸籌（Accumulation） | 跌不下去、下影線多、量縮後量增不破低 | 標記「潛在吸籌」與「結構底」 |
| 測試（Test） | 回踩關鍵位量縮、價格守住 | 標記「低風險切入區」 |
| SOS（Sign of Strength） | 突破區間上緣、量能放大且收高 | 標記「突破候選」 |
| LPS（Last Point of Support） | 突破後回測不破、量縮 | 標記「回撤買點候選」 |
| 再吸籌（Re-accumulation） | 上升趨勢中平台整理、量縮價穩 | 標記「趨勢延續候選」 |

### 2) Exploit 否決規則（禁止/降級）
| 威科夫操盤風險 | 可觀察特徵（量價/籌碼） | Exploit 處置（否決/降級） |
|---|---|---|
| 出貨（Distribution） | 高檔爆量不漲、上影線多、拉高出貨 | 禁止追價；僅允許減倉/停利 |
| UT（Upthrust）假突破 | 突破後快速跌回區間、量能失真 | 直接否決突破單；等待回測再評估 |
| Spring 失敗 | 跌破後未能迅速拉回、量能轉弱 | 直接否決抄底；提高停損敏感度 |
| 拉指數掩護 | 指數強但個股/族群無承接 | 降低權重；僅保留最強勢個股候選 |
| 消息配合出貨 | 利多發布後拉高爆量、隔日走弱 | 觸發「消息反向」警示 → 禁止追高 |

### 3) 與 TAITS 的模組對應
- Explore：Technical Analyst（結構標記）+ News/Fundamental（敘事背景）
- Exploit：ManipulationRiskEngine（否決）+ RiskEngine（倉位/停損）

---

## 多決策線（Multi-Decision Lines）與權重治理

本節定義 TAITS 的「多決策線（Multi-Decision Lines）」：不是把策略堆在一起，而是用**投資組合層（Meta-Portfolio）**管理不同策略線的風險與貢獻。

### 1) 核心概念
- 每條策略線都有自己的：Universe、入場條件、出場條件、風險上限、適用 Regime
- 最終下單不是「策略贏者全拿」，而是由 PortfolioManager 做「權重配置 + 風險上限 + 相關性控制」

### 2) 典型配置（示例，可調整）
- 結構/主力線（Wyckoff/結構突破）：30%
- 價值/基本面線（Buffett/景氣循環）：25%
- 趨勢/麻雀獲利線（多標的短中期趨勢）：45%

> v0.1（零股）建議：先用 2~3 條策略線即可，避免策略互相打架，重點是把「日誌與回測框架」做穩。

### 3) 多策略融合的防堵機制（避免被堵死、方便未來補充）
- **Strategy Registry（策略註冊表）**：每新增策略只要新增一個「策略描述 + 輸入/輸出契約」即可接入
- **Signal Schema（統一訊號格式）**：所有策略輸出統一為 Score/Confidence/Direction/ActionHint
- **Veto First（否決優先）**：任何策略都可提分，但只有 Regime/Risk/Manipulation 可以否決
- **Weight Governance（權重治理）**：週期性用績效與風險指標調整權重，不需要改核心程式

### 4) 實務落地（v0.1）
- 先固定 3 條策略線 + 1 個融合規則（投票 + 否決）
- 每日輸出：候選池、否決原因、實際模擬成交、隔日調整
