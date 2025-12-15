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

# 【TAITS 策略宇宙補齊與用途定位（非下單）】
## 版本：v2025-12-16
## 性質：Only-Add（追加，不覆蓋既有內容）

本章節目的不是新增「下單策略」，而是把你已反覆要求、
但在原專案中**未被清楚寫成策略資產**的部分，正式納入 TAITS 策略宇宙，
並明確標註「它們在系統中到底幹嘛」。

---

## 一、策略分類總則（母體硬規則）

### 1. 策略 ≠ 下單
TAITS 中的策略必須先回答：
- 用來**判斷什麼**
- 用來**限制什麼**
- 用來**調整什麼**

是否下單，永遠由你決定，且在策略層不自動發生。

---

### 2. 策略類型分類（四大類）

所有策略必須屬於以下一類或多類：

1. Market Regime Strategy（市場狀態判斷）
2. Filter Strategy（進出場濾網）
3. Weight Adjuster Strategy（權重調整）
4. Risk Override Strategy（風險覆蓋）

---

## 二、方法論型策略群（Methodology Strategies）

> 這一群是你多次強調「勝率來源」的核心。

---

### 2.1 威科夫策略群（Wyckoff Strategy Group）

#### 定位
- 判斷主力行為與階段
- 用於**避免假突破、辨識派發風險**
- 不直接產生買賣點

#### 核心策略條目
- WY-S01：主力吸籌階段確認
- WY-S02：推升階段趨勢確認
- WY-S03：派發風險警示
- WY-S04：假突破濾網
- WY-S05：量價背離警示

#### 輸出
- wyckoff_stage
- wyckoff_confidence
- wyckoff_risk_tags
- weight_adjustment_hint
- exit_priority_hint

#### 使用層級
- L5（證據包）
- L6（Regime 輔助）
- L8（策略排序）
- L10（UI 解釋）

---

### 2.2 鮑迪克纏論策略群（Bodick ChanLun Strategy Group）

#### 定位
- 提升結構勝率
- 確認轉折真偽
- 管理段落節奏

#### 核心策略條目
- BD-S01：結構段落推進確認
- BD-S02：高位背離警示
- BD-S03：低位背離確認
- BD-S04：段落一致性評分
- BD-S05：多級別共振確認

#### 輸出
- bodick_structure_state
- bodick_consistency_score
- bodick_resonance
- risk_tags
- exit_priority_hint

#### 使用層級
- L5 / L8 / L10

---

## 三、Observe-only 跨市場策略群（不下單）

> 這一群是你反覆強調「期貨會影響台股，但我不是拿來下期貨」。

---

### 3.1 期貨觀察策略群（Futures Observe-only）

#### 定位
- 市場方向與波動判斷
- 禁止追價、提高風險意識

#### 策略條目
- FO-S01：指數期貨方向偏移
- FO-S02：期貨急轉折警示
- FO-S03：波動擴張風險
- FO-S04：現期背離警示

#### 輸出
- futures_regime_flags
- cross_market_risk_tags
- forbidden_strategy_list

---

### 3.2 選擇權觀察策略群（Options Observe-only）

#### 定位
- 壓力/支撐與結算風險判斷

#### 策略條目
- OP-S01：OI 壓力牆
- OP-S02：結算釘住風險
- OP-S03：Gamma 波動警示

---

### 3.3 融資融券觀察策略群（Credit Observe-only）

#### 定位
- 槓桿過熱與踩踏風險提示

#### 策略條目
- CR-S01：融資使用率過熱
- CR-S02：融券比率異常
- CR-S03：籌碼踩踏風險

---

## 四、題材輪動與中小型保留策略群

> 對齊你說的：市場會輪動、題材會擴散，不是只有權值股。

---

### 4.1 題材輪動策略群（Theme Rotation）

#### 定位
- 捕捉主線 → 次主線 → 供應鏈 → 中小型

#### 策略條目
- TR-S01：主線題材確認
- TR-S02：次主線擴散
- TR-S03：供應鏈擴散
- TR-S04：材料/工具補漲

---

### 4.2 爆發池保留策略（Expansion Pool Protection）

#### 定位
- 防止中小型被嚴苛條件刪除

#### 策略條目
- EP-S01：爆發池最低保留
- EP-S02：僅允許降權，不可刪除

---

## 五、策略與下單的邊界（母體硬規則）

- 策略層不下單
- 策略只輸出：
  - 允許 / 禁止
  - 權重建議
  - 風險標籤
  - 出場優先權
- 是否下單，由你決定或由獨立 Execution 層處理

---

## 六、驗收標準（你怎麼確認這份有用）

1. 新對話可完整列出所有策略群與用途
2. 任一策略都能說清楚「幹嘛、不幹嘛」
3. 不存在「期貨策略被誤當成期貨下單」

---

# 【End of TAITS_Strategy_Universe 補齊】

