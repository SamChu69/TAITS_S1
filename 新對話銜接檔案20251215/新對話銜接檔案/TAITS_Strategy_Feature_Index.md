# TAITS_Strategy_Feature_Index.md
# 【TAITS 策略 / 指標 / 特徵 全量索引】
## 版本：v2025-12-16
## 性質：Only-Add（追加，不覆蓋既有內容）

本文件是 TAITS 的「工具箱目錄」：
- 不解釋流程（流程在 02 / 07）
- 不下單
- 只回答三件事：**有沒有、用來幹嘛、在哪一層**

---

## 使用標註說明
- 用途：Regime / Filter / Weight / Risk / Exit / Explain
- 層級：L4–L10
- Observe-only：是 / 否

---

## A. K 線與價格結構（Price & Candlestick）

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| A01 | 單根 K 線方向 | Explain | L4/L10 | 否 |
| A02 | K 線實體比例 | Filter | L4 | 否 |
| A03 | 上下影線結構 | Risk | L4 | 否 |
| A04 | 多根 K 線組合 | Filter | L4 | 否 |
| A05 | 高低點結構（HH/HL） | Regime | L4/L6 | 否 |
| A06 | 缺口（Gap） | Risk | L4/L7 | 否 |

---

## B. 趨勢與均線（Trend & MA / GMMA / CBL）

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| B01 | SMA | Filter | L4 | 否 |
| B02 | EMA | Filter | L4 | 否 |
| B03 | WMA | Filter | L4 | 否 |
| B04 | GMMA 短期群 | Regime | L4/L6 | 否 |
| B05 | GMMA 長期群 | Regime | L4/L6 | 否 |
| B06 | GMMA 群擴散/收斂 | Risk | L4/L7 | 否 |
| B07 | 顧比倒數線（CBL） | Exit | L4/L8 | 否 |
| B08 | 趨勢角度 | Weight | L4/L8 | 否 |

---

## C. 動能與振盪（Momentum & Oscillators）

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| C01 | RSI | Filter | L4 | 否 |
| C02 | RSI 背離 | Risk | L4/L7 | 否 |
| C03 | MACD | Filter | L4 | 否 |
| C04 | MACD 背離 | Risk | L4/L7 | 否 |
| C05 | Stochastic | Filter | L4 | 否 |
| C06 | Momentum | Weight | L4/L8 | 否 |

---

## D. 波動與風險（Volatility & Risk）

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| D01 | ATR | Risk | L4/L7 | 否 |
| D02 | 波動率擴張 | Regime | L4/L6 | 否 |
| D03 | 波動率壓縮 | Filter | L4 | 否 |
| D04 | 價量失衡 | Risk | L4/L7 | 否 |

---

## E. 量能與籌碼（Volume & Flow）

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| E01 | 成交量均值 | Filter | L4 | 否 |
| E02 | 量價背離 | Risk | L4/L7 | 否 |
| E03 | 主動買賣量 | Weight | L4/L8 | 否 |
| E04 | 大單比例 | Explain | L4/L10 | 否 |

---

## F. 威科夫（Wyckoff）結構特徵

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| F01 | 吸籌階段 | Regime | L4/L6 | 否 |
| F02 | 推升階段 | Regime | L4/L6 | 否 |
| F03 | 派發階段 | Risk | L4/L7 | 否 |
| F04 | 下跌階段 | Risk | L4/L7 | 否 |
| F05 | 假突破 | Filter | L4 | 否 |
| F06 | 量價確認 | Explain | L4/L10 | 否 |

---

## G. 鮑迪克纏論（結構 / 背離 / 共振）

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| G01 | 結構段落 | Regime | L4/L6 | 否 |
| G02 | 段落推進/回撤 | Filter | L4 | 否 |
| G03 | 高位背離 | Risk | L4/L7 | 否 |
| G04 | 低位背離 | Weight | L4/L8 | 否 |
| G05 | 多級別一致性 | Regime | L4/L6 | 否 |
| G06 | 結構共振 | Weight | L4/L8 | 否 |

---

## H. 題材 / 消息 / 社群（Theme & Narrative）

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| H01 | 重大新聞事件 | Regime | L4/L6 | 否 |
| H02 | 法說 / 公告 | Explain | L4/L10 | 否 |
| H03 | 題材熱度分數 | Weight | L4/L8 | 否 |
| H04 | 擴散鏈（主線→次線） | Regime | L4/L6 | 否 |
| H05 | 謠言風險標籤 | Risk | L4/L7 | 否 |

---

## I. 期貨（Observe-only）

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| I01 | 指數期貨方向 | Regime | L4/L6 | 是 |
| I02 | 期貨急轉折 | Risk | L4/L7 | 是 |
| I03 | 現期背離 | Risk | L4/L7 | 是 |
| I04 | 波動擴張 | Regime | L4/L6 | 是 |

---

## J. 選擇權（Observe-only）

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| J01 | OI 壓力牆 | Risk | L4/L7 | 是 |
| J02 | 結算釘住 | Exit | L4/L8 | 是 |
| J03 | Gamma 風險 | Risk | L4/L7 | 是 |

---

## K. 融資融券（Observe-only）

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| K01 | 融資使用率 | Risk | L4/L7 | 是 |
| K02 | 融券比率 | Risk | L4/L7 | 是 |
| K03 | 踩踏風險 | Exit | L4/L8 | 是 |

---

## L. Universe 與池化控制

| ID | 名稱 | 用途 | 層級 | Observe-only |
|---|---|---|---|---|
| L01 | 穩定池 | Regime | L8 | 否 |
| L02 | 輪動池 | Regime | L8 | 否 |
| L03 | 爆發池 | Weight | L8 | 否 |
| L04 | 僅降權不可刪 | Risk | L8/L7 | 否 |

---

## 驗收條款
- 任一新對話可用本表「點名」所有工具
- 任一工具都能說清楚：幹嘛 / 不幹嘛
- Observe-only 永不下單

---

# 【End of TAITS_Strategy_Feature_Index】
