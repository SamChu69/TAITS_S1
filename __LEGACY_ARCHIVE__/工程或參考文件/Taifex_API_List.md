# 臺灣期貨交易所 (Taifex) OpenAPI 完整介面清單

> **文件來源**: [臺灣期貨交易所 OpenAPI](https://openapi.taifex.com.tw/)
> **Base URL**: `https://openapi.taifex.com.tw/v1`
> **資料格式**: JSON
> **核心商品**: 台指期 (TX), 小台指 (MTX), 台指選擇權 (TXO), 個股期貨 (Stock Futures)

本文件整理了期交所 OpenAPI 平台提供的所有資料接口，按交易策略功能分類。

---

## 1. 每日交易行情 (Daily Market Data)
*期貨與選擇權的開高低收 (OHLC)、成交量與未平倉量 (Open Interest)。這是最基礎的價格數據。*

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/DailyMarketReportFut` | **期貨每日交易行情** (含台指期、電子期、金融期等) |
| GET | `/DailyMarketReportOpt` | **選擇權每日交易行情** (含台指選擇權買賣權) |
| GET | `/DailyOptionsDelta` | **選擇權每日 Delta 值** (希臘字母風險參數) |
| GET | `/PutCallRatio` | **臺指選擇權 Put/Call Ratio** (多空判斷重要指標) |
| GET | `/TimeAndSalesData` | 每日期貨每筆成交資料 (Tick Data) |
| GET | `/OptionsTimeAndSalesData` | 每日選擇權每筆成交資料 (Tick Data) |
| GET | `/DailyVolumeReportOnCalendarSpreadOrders` | 每日期貨價差委託成交概況表 (Spread Trading) |
| GET | `/STFTop10` | 每日股票期貨交易量前十大統計表 |

## 2. 三大法人與大額交易人 (Institutional & Large Traders)
*分析「聰明錢 (Smart Money)」流向的核心數據，包含外資多空單部位。*

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/MarketDataOfMajorInstitutionalTradersGeneralBytheDate` | **三大法人-總表** (區分期貨/選擇權) |
| GET | `/MarketDataOfMajorInstitutionalTradersDetailsOfFuturesContractsBytheDate` | **三大法人-區分各期貨契約** (細分台指期、小台指) |
| GET | `/MarketDataOfMajorInstitutionalTradersDetailsOfOptionsContractsBytheDate` | **三大法人-區分各選擇權契約** |
| GET | `/MarketDataOfMajorInstitutionalTradersDetailsOfCallsAndPutsBytheDate` | **三大法人-選擇權買賣權分計** (分析外資 Call/Put 布局) |
| GET | `/OpenInterestOfLargeTradersFutures` | **期貨大額交易人未沖銷部位** (前5大/前10大交易人) |
| GET | `/OpenInterestOfLargeTradersOptions` | **選擇權大額交易人未沖銷部位** |

## 3. 保證金與結算 (Margin & Settlement)
*計算交易成本、槓桿倍數，以及到期結算價格。*

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/FinalSettlementPrice` | **最後結算價** (一般查詢) |
| GET | `/IndexFuturesAndOptionsMargining` | **保證金一覽表-股價指數類** (查詢台指期保證金) |
| GET | `/SingleStockFuturesMargining` | 保證金一覽表-股票類 (個股期貨) |
| GET | `/FuturesAndOptionsFeeSchedule` | 期貨暨選擇權商品相關費用表 |
| GET | `/SettledPositionsOfContractsOnExpirationDate` | 到期契約履約交割資訊 |
| GET | `/AcceptableCollateralStock` | 有價證券保證金之可抵繳標的-股票(含 ETF) |

## 4. 鉅額交易 (Block Trading)
*法人大額換手數據，通常暗示潛在的趨勢改變。*

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/BlockTrade` | 鉅額交易各商品成交資訊 |
| GET | `/BlockTradeContinuousMatchingSingleOrder` | 鉅額交易逐筆撮合之單式委託成交 |
| GET | `/DailySummaryOfBlockTradeFutures` | 鉅額交易成交量統計-期貨商品 |
| GET | `/DailySummaryOfBlockTradeOptions` | 鉅額交易成交量統計-選擇權商品 |

## 5. 商品與契約資訊 (Product Specifications)

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/SSFLists` | 股票期貨交易標的 (查看哪些股票有期貨) |
| GET | `/SSOLists` | 股票選擇權交易標的 |
| GET | `/ContractAdj` | 股票期貨/選擇權契約調整一覽事項 (除權息調整) |
| GET | `/SSFAdjustedInfo` | 股票期貨/選擇權調整型契約資訊 |
| GET | `/PositionLimitEquity` | 交易人部位限制-個股類 |
| GET | `/MarketMakerListsFut` | 期貨商品造市者清單 |

## 6. 其他統計 (Others)

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/DailyForeignExchangeRates` | 每日外幣參考匯率 |
| GET | `/MarketParticipants` | 市場參與者統計 |
| GET | `/va01` | 每日股價指數類選擇權未平倉量增減 |
| GET | `/va04` | 股價指數類期貨商品每月平均成交金額 |

---
*注意：期貨資料通常包含日盤 (Regular) 與夜盤 (After-hours)，使用 API 時請留意資料欄位是否區分盤別。*

### 💡 開發者重點提示 (For TAITS\_S1)

1.  **三大法人 vs 大額交易人**：

      * 在期貨市場，除了看 **三大法人 (`InstitutionalTraders`)** 外，更要看 **大額交易人 (`LargeTraders`)**。
      * 這兩者的數據交叉比對，是判斷台股短線多空非常準確的指標（例如：外資多單增加 + 前十大交易人多單增加 = 強力看多）。

2.  **Put/Call Ratio**：

      * API 路徑：`/PutCallRatio`
      * 這是一個現成的市場情緒指標，數值 \> 100% 通常偏多，\< 100% 通常偏空，非常適合直接作為量化策略的一個因子 (Factor)。

3.  **個股期貨 (Single Stock Futures)**：

      * 如果您想做「現貨 vs 期貨」的套利，可以利用 `/SSFLists` 找出有期貨的股票，再搭配證交所 API 的現貨價格來計算價差。
