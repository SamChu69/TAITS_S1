# TAITS_Strategy_Universe_Complete.md
# TAITS — 全策略宇宙（Master Strategy Specification）

版本：Master / Full  
文件角色：**策略治理最高權威（Single Source of Truth）**  
對應文件：
- TAITS_DataSources_Universe.md
- TAITS_MASTER_ARCHITECTURE.md

---

## 0. 文件定位（不可省略）

本文件定義 **TAITS 系統中允許存在的「全部策略集合」**。

任何策略必須：
1. 列名於本文件  
2. 明確標註策略類型  
3. 對應合法資料來源  
4. 服從 Regime 與 Risk 規則  

---

## 1. 策略宇宙總覽

| 類別 | 說明 | 數量 |
|---|---|---|
| 技術分析（TA） | 趨勢 / 動能 / 反轉 | 112 |
| 籌碼策略（Chip） | 法人 / 融資券 | 48 |
| 基本面（Fundamental） | 財報 / 成長 | 36 |
| 產業 / 類股 | 輪動 / 相對強度 | 22 |
| 行為金融 | 過熱 / 恐慌 | 14 |
| 新聞 / 事件 | 公告 / 政策 | 18 |
| 衍生品 | 期貨 / 選擇權 | 28 |
| AI 輔助 | 投票 / 語意 | 12 |
| **纏論（ChanLun）** | 結構 / 背馳 | **35+** |
| 補充策略（20251210） | Regime / Macro | **30+** |

👉 **總計：355+ 策略（不含參數變體）**

---

## 2. 技術分析策略（TA）

- MA / EMA / GMMA
- Donchian / SuperTrend
- Ichimoku
- RSI / MACD / ADX
- Bollinger / ATR

資料來源：TWSE / TPEX  
Agent：TechnicalAgent  
適用 Regime：TREND / RANGE

---

## 3. 籌碼策略（Chip）

- 三大法人同步 / 背離
- 融資增減
- 借券 / 當沖
- 股權集中度

資料來源：TWSE / 集保  
Agent：ChipAgent

---

## 4. 基本面策略（Fundamental）

- EPS QoQ / YoY
- ROE + 成長
- 月營收動能
- 財報 Surprise

資料來源：MOPS  
Agent：FundamentalAgent

---

## 5. 產業 / 類股策略

- 族群輪動
- 相對強度（RS）
- 領先股

---

## 6. 行為金融策略

- 過熱成交量
- 恐慌拋售
- 波動反轉

---

## 7. 新聞 / 事件策略

- 財報公告
- 法說會
- 政策衝擊

Agent：NewsAgent / EventAgent

---

## 8. 衍生品策略

### 8.1 期貨

- OI 變化
- 法人期貨偏多 / 空
- 夜盤背離

### 8.2 選擇權

- Put/Call Ratio
- IV Skew
- Max Pain

Agent：DerivativesAgent  
Regime：Risk-On / Risk-Off

---

## 9. AI 輔助策略

- 多策略投票
- 信心加權
- 非線性調整

⚠️ **AI 不得直接下單**

---

## 10. 纏論策略（ChanLun）

### 10.1 結構指標

- 分型
- 筆
- 線段
- 中樞
- 背馳

### 10.2 策略範例

- 一買 / 二買 / 三買
- 中樞突破
- 趨勢背馳轉折
- 類二買

Agent：TechnicalAgent（纏論子模組）

---

## 11. 補充策略（20251210）

- Macro + Derivatives 混合
- Regime-aware 策略
- 風險優先策略

---

## 12. 策略治理原則（強制）

- 策略 ≠ 下單
- 所有策略只輸出 Signal / Confidence / Reason
- 最終決策必經 Fusion + Risk

---

## 13. 一句話總結

> **TAITS 的強，不在於策略多，  
> 而在於策略被嚴格治理。**

---
