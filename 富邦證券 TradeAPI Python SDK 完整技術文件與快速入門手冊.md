# 富邦證券 TradeAPI Python SDK 完整技術文件與快速入門手冊

**文件編撰：** Manus AI
**編撰日期：** 2025年12月10日
**資料來源：** 富邦證券 TradeAPI 官方文件網站 [1]

---

## 目錄 (Table of Contents)

1.  [概述與特色](#1-概述與特色)
    1.1. [版本支援](#11-版本支援)
    1.2. [主要功能](#12-主要功能)
2.  [Python SDK 安裝與設定](#2-python-sdk-安裝與設定)
    2.1. [SDK 下載資訊](#21-sdk-下載資訊)
    2.2. [Python SDK 安裝方式](#22-python-sdk-安裝方式)
    2.3. [初始化與認證方式](#23-初始化與認證方式)
3.  [交易 API 彙總與範例](#3-交易-api-彙總與範例)
    3.1. [交易 API 彙總表](#31-交易-api-彙總表)
    3.2. [下單、改單、刪單 示範程式碼](#32-下單改單刪單-示範程式碼)
        3.2.1. [建立委託單 (place\_order)](#321-建立委託單-place_order)
        3.2.2. [修改委託價格 (modify\_price)](#322-修改委託價格-modify_price)
        3.2.3. [修改委託單數量 (modify\_quantity)](#323-修改委託單數量-modify_quantity)
        3.2.4. [刪除委託單 (cancel\_order)](#324-刪除委託單-cancel_order)
    3.3. [委託查詢功能](#33-委託查詢功能)
        3.3.1. [取得委託單結果 (get\_order\_results)](#331-取得委託單結果-get_order_results)
        3.3.2. [取得委託單結果 (含歷程) (get\_order\_results\_detail)](#332-取得委託單結果-含歷程-get_order_results_detail)
4.  [帳務查詢 API 彙總與範例](#4-帳務查詢-api-彙總與範例)
    4.1. [庫存查詢 (inventories)](#41-庫存查詢-inventories)
    4.2. [交割資訊查詢 (query\_settlement)](#42-交割資訊查詢-query_settlement)
    4.3. [未實現損益查詢 (unrealized\_gains\_and\_loses)](#43-未實現損益查詢-unrealized_gains_and_loses)
5.  [主動回報 (Callback) 機制](#5-主動回報-callback-機制)
    5.1. [訂閱委託回報 (set\_on\_order)](#51-訂閱委託回報-set_on_order)
    5.2. [訂閱改價/改量/刪單回報 (set\_on\_order\_changed)](#52-訂閱改價改量刪單回報-set_on_order_changed)
    5.3. [訂閱成交回報 (set\_on\_filled)](#53-訂閱成交回報-set_on_filled)
    5.4. [訂閱事件通知 (set\_on\_event)](#54-訂閱事件通知-set_on_event)
    5.5. [Python 主動回報例外處理](#55-python-主動回報例外處理)
6.  [資料格式與參數對照表](#6-資料格式與參數對照表)
    6.1. [核心物件欄位定義](#61-核心物件欄位定義)
        6.1.1. [Account 帳號資訊](#611-account-帳號資訊)
        6.1.2. [OrderObject 委託內容](#612-orderobject-委託內容)
        6.1.3. [OrderResult 委託資訊](#613-orderresult-委託資訊)
        6.1.4. [FilledData 成交回報物件](#614-filleddata-成交回報物件)
        6.1.5. [Inventory 庫存資訊](#615-inventory-庫存資訊)
    6.2. [常數 (Constants) 欄位對應數值](#62-常數-constants-欄位對應數值)
        6.2.1. [BSAction 買賣別](#621-bsaction-買賣別)
        6.2.2. [MarketType 盤別與數量限制](#622-markettype-盤別與數量限制)
        6.2.3. [PriceType 價格類型](#623-pricetype-價格類型)
        6.2.4. [TimeInForce 委託條件](#624-timeinforce-委託條件)
        6.2.5. [OrderType 委託類別](#625-ordertype-委託類別)
        6.2.6. [Status 委託單狀態代碼](#626-status-委託單狀態代碼)
        6.2.7. [Function\_type 功能類別代碼](#627-function_type-功能類別代碼)
7.  [下單限制與風控規則](#7-下單限制與風控規則)
    7.1. [速率限制](#71-速率限制)
    7.2. [憑證、簽章、加密、Hash、Token 規範](#72-憑證簽章加密hash-token-規範)
    7.3. [需要注意事項與容易踩到的坑](#73-需要注意事項與容易踩到的坑)
8.  [Python Developer 快速入門手冊](#8-python-developer-快速入門手冊)

---

## 1. 概述與特色

富邦新一代 API 提供了完善的交易與行情 API，旨在滿足開發者的量化與自動化交易需求。它支援多種主流開發語言，其中 **Python** 是官方重點支援的語言之一 [1]。

### 1.1. 版本支援

富邦 TradeAPI Python SDK 支援多個 Python 版本，確保開發者能使用較新的環境進行開發 [1] [2]。

| 語言 | 支援版本 | 備註 |
| :--- | :--- | :--- |
| **Python** | **3.8, 3.9, 3.10, 3.11, 3.12** | v2.0.1 後停止支援 Python 3.7 [2]。 |
| Node.js | 16 以上版本 | |
| C# | .NET Standard 2.0 (建議 .netcoreapp 3.1 或 .NETFramework 4.7.2 以上) | |

### 1.2. 主要功能

API 的主要功能涵蓋了交易、帳務與行情資訊 [1]：

*   **直接管理交易：** 建立、修改、取消委託單，查詢委託單狀態、歷史委託紀錄和成交明細等。
*   **查看帳戶資訊：** 取得帳戶內的庫存損益、已實現損益、未實現損益、維持率等。
*   **接收即時行情：** 股票、權證、期權價格等多種行情資訊。

---

## 2. Python SDK 安裝與設定

### 2.1. SDK 下載資訊

富邦官方提供 SDK 的下載點，並建議透過 `pip` 進行安裝 [2]。

| 項目 | 說明 |
| :--- | :--- |
| **SDK 版本** | 最新版本為 **v2.2.5** [2]。 |
| **下載方式** | 需至 [SDK 下載頁面](https://www.fbs.com.tw/TradeAPI/docs/download/download-sdk) 下載對應版本的 `.whl` 檔案 [3]。 |
| **範例程式碼** | 官方提供 **Python 範例程式碼** (.ipynb 格式)，需搭配 SDK 使用 [2]。 |
| **下載連結** | Windows 64 位元、MacOs (Arm 64 位元/X86 64 位元)、Linux 64 位元皆有提供專屬 SDK 檔案下載 [2]。 |

### 2.2. Python SDK 安裝方式

下載對應的 `.whl` 檔案後，使用 `pip` 指令安裝 [3]：

```bash
pip install fubon_neo-<version>-cp37-abi3-win_amd64.whl
```

### 2.3. 初始化與認證方式

**憑證與連線**

在使用 SDK 進行登入前，需確保憑證檔案 (`.pfx`) 已放置在程式可存取的位置 [3]。

**登入 API (login)**

登入是使用所有交易和帳務功能的第一步。登入成功後，會回傳 `Account` 物件列表，包含所有歸戶的帳號資訊 [4]。

| 參數 | 類別 | 說明 |
| :--- | :--- | :--- |
| `personal_id` | String | 登入的 ID (身分證字號) |
| `password` | String | 登入的密碼 |
| `cert_path` | String | **憑證路徑** |
| `cert_pass` | String | **憑證密碼** |

**請求範例：**

```python
from fubon_neo.sdk import FubonSDK, Order
from fubon_neo.constant import TimeInForce, OrderType, PriceType, MarketType, BSAction

sdk = FubonSDK()
   
# 登入，若有歸戶，則會回傳多筆帳號資訊
accounts = sdk.login("您的身分證字號", "您的登入密碼", "您的憑證位置", "您的憑證密碼") 

# 若憑證選用＂預設密碼＂, SDK v1.3.2與較新版本適用
# accounts = sdk.login("您的身分證號", "您的登入密碼", "您的憑證路徑位置") 

acc = accounts.data[0] # 取第一個帳號進行操作
```

**回傳範例：**

```json
Result {
    "is_success": True,
    "message": None,
    "data" : [
        {
            "name" : "富邦Bill",      # 客戶姓名 (string)
            "account" :  "28",       # 客戶帳號 (string)
            "branch_no" : "6460",     # 分公司代號  (string)
            "account_type" : "stock"  # 帳號類型 (string)
        }
    ]
}
```

**登出 API (logout)**

結束操作後，應呼叫 `logout` 函式登出 [5]。

**請求範例：**

```python
sdk.logout()
```

**回傳範例：**

```
True
```

---

## 3. 交易 API 彙總與範例

### 3.1. 交易 API 彙總表

| 功能 | 方法名稱 | 說明 | 請求/回傳物件 |
| :--- | :--- | :--- | :--- |
| **建立委託單** | `sdk.stock.place_order(account, order_object)` | 送出新的委託單 | `OrderObject` / `OrderResult` |
| **取得委託單結果** | `sdk.stock.get_order_results(account)` | 查詢當日所有委託單狀態 | `Account` / `List<OrderResult>` |
| **取得委託單結果 (含歷程)** | `sdk.stock.get_order_results_detail(account)` | 查詢當日所有委託單狀態，包含改單、刪單歷程 | `Account` / `List<OrderResult>` |
| **修改委託價格** | `sdk.stock.modify_price(account, modify_price_obj)` | 修改未成交委託單的價格 | `ModifyPriceObj` / `OrderResult` |
| **修改委託單數量** | `sdk.stock.modify_quantity(account, modify_qty_obj)` | 修改未成交委託單的數量 | `ModifyQuantityObj` / `OrderResult` |
| **刪除委託單** | `sdk.stock.cancel_order(account, order_result)` | 取消未成交的委託單 | `OrderResult` / `OrderResult` |

> **注意：** 由於權限限制，部分交易 API (如歷史委託、歷史成交、批次委託等) 的詳細文件未能成功爬取。請參考官方文件以獲取完整資訊。

### 3.2. 下單、改單、刪單 示範程式碼

#### 3.2.1. 建立委託單 (place\_order)

使用 `Order` 類別建立委託內容，然後呼叫 `sdk.stock.place_order` 進行下單 [6]。

**請求範例：**

```python
# 範例：以限價買入富邦金(2881) 1張 (1000股)，價格為 66 元
order = Order(
    buy_sell = BSAction.Buy,
    symbol = "2881",
    price =  "66",
    quantity =  1000,
    market_type = MarketType.Common,
    price_type = PriceType.Limit,
    time_in_force = TimeInForce.ROD,
    order_type = OrderType.Stock,
    user_def = "From_Py" # 自訂欄位，可選
)

sdk.stock.place_order(account, order)
```

#### 3.2.2. 修改委託價格 (modify\_price)

需要先取得 `OrderResult` 物件，然後使用 `make_modify_price_obj` 建立修改物件 [7]。

**請求範例：**

```python
# 假設 order_result 是欲修改的委託單物件
# 將價格調整成 41.1 元
modify_price_obj = sdk.stock.make_modify_price_obj(order_result, "41.1") 

# 執行改價
sdk.stock.modify_price(account, modify_price_obj)
```

> **注意事項：** 當 `price` 欄位有填入值時，`price_type` 欄位需為空值或 `None`；反之亦然 [7]。

#### 3.2.3. 修改委託單數量 (modify\_quantity)

需要先取得 `OrderResult` 物件，然後使用 `make_modify_quantity_obj` 建立修改物件 [8]。

**請求範例：**

```python
# 假設 target_order 是欲修改的委託單物件
# 將委託量修改為 1000 股 (修改後數量包含此委託單已成交部份)
modify_qty_obj = sdk.stock.make_modify_quantity_obj(target_order, 1000)

# 執行改量
sdk.stock.modify_quantity(account, modify_qty_obj)
```

#### 3.2.4. 刪除委託單 (cancel\_order)

需要傳入欲取消的 `OrderResult` 物件 [9]。

**請求範例：**

```python
# 假設 cancel_order 是欲取消的委託單物件
sdk.stock.cancel_order(account, cancel_order)
```

### 3.3. 委託查詢功能

#### 3.3.1. 取得委託單結果 (get\_order\_results)

查詢當日所有委託單的狀態 [10]。

**請求範例：**

```python
order_results = sdk.stock.get_order_results(accounts.data[0])
print(order_results)
```

#### 3.3.2. 取得委託單結果 (含歷程) (get\_order\_results\_detail)

查詢當日所有委託單的狀態，並包含改價、改量、刪單等操作的歷程記錄 [11]。

**請求範例：**

```python
sdk.stock.get_order_results_detail(accounts.data[0])
```

---

## 4. 帳務查詢 API 彙總與範例

### 4.1. 庫存查詢 (inventories)

查詢帳號內的股票庫存資訊，包含昨日餘額、今日買賣數量、可委託數量等 [12]。

**請求範例：**

```python
inventories = sdk.accounting.inventories(account)
print(inventories)
```

**回傳範例 (部分欄位)：**

```json
{
    "is_success": True,
    "message": None,
    "data" : [
        {
            "date": "2023/10/16",     # 交易日期 (string)
            "stock_no": "1101",       # 股票代號 (string)
            "order_type": "Stock",      # 委託單類型 (OrderType)
            "lastday_qty": 2000,      # 昨日庫存餘額 (int)
            "today_qty": 2000,        # 今日庫存餘額 (int)
            "tradable_qty": 2000,     # 可委託股數 (int)
            "odd": {                  # 零股庫存
                "today_qty": 0,
                "tradable_qty": 0
            }
        }
    ]
}
```

### 4.2. 交割資訊查詢 (query\_settlement)

查詢今日或近三日的應收付交割金額 [13]。

**請求範例：**

```python
# 查詢當日交割資訊
settlement = sdk.accounting.query_settlement(accounts.data[0],"0d")
print(settlement.data)
```

### 4.3. 未實現損益查詢 (unrealized\_gains\_and\_loses)

查詢帳號內持股的未實現損益 [13]。

**請求範例：**

```python
unrealized_pnl = sdk.accounting.unrealized_gains_and_loses(accounts.data[0])
print(unrealized_pnl.data)
```

---

## 5. 主動回報 (Callback) 機制

富邦 TradeAPI 支援主動回報機制，允許開發者設定回呼函式 (Callback Function) 來接收委託、成交和系統事件的即時通知 [14]。

### 5.1. 訂閱委託回報 (set\_on\_order)

接收新單的委託資料 [14]。

```python
# A callback to receive order data
def on_order(code, content):
    print("==Order==")
    print(code)
    print(content)
    # print(content.seq_no)  # 印出委託單流水號
    print("========")

sdk.set_on_order(on_order) 
# 回傳物件說明，可參照 OrderResult Object
```

### 5.2. 訂閱改價/改量/刪單回報 (set\_on\_order\_changed)

接收委託單被修改或刪除的資料 [14]。

```python
def on_order_changed(code, content):
    print("=Modified==")
    print(code)
    print(content)
    # print(content.seq_no)  # 印出委託單流水號
    print("========")
    
sdk.set_on_order_changed(on_order_changed) 
# 回傳物件說明，可參照 OrderResult Object
```

### 5.3. 訂閱成交回報 (set\_on\_filled)

接收成交資料 [14]。

```python
def on_filled(code, content):
    print("==Filled==")
    print(code)
    print(content)
    # print(content.filled_no)  # 印出成交流水號
    print("========")
    
sdk.set_on_filled(on_filled)
# 回傳物件說明，可參照 FilledData Object
```

### 5.4. 訂閱事件通知 (set\_on\_event)

接收系統事件通知，例如連線狀態、登入警示等 [14]。

```python
def on_event(code, content):
    print("===event=====")
    print(code)
    print(content)
    print("========")
    
sdk.set_on_event(on_event) 
```

| 回傳代碼 | 意義 |
| :--- | :--- |
| `100` | 連線建立成功 |
| `200` | 登入成功 |
| `201` | 登入警示 (Ex: 90天未更換密碼) |
| `300` | 斷線 |
| `301` | 未收到連線 pong 回傳 |
| `302` | 登出，並斷線 |
| `500` | 錯誤 |

### 5.5. Python 主動回報例外處理

此部分文件未能成功爬取，但根據文件結構，應有專門頁面說明 Python SDK 在主動回報機制中的例外處理方式。請參考官方文件以獲取完整資訊。

---

## 6. 資料格式與參數對照表

### 6.1. 核心物件欄位定義

#### 6.1.1. Account 帳號資訊 [4]

| 參數 | 類別 | 說明 |
| :--- | :--- | :--- |
| `name` | String | 客戶姓名 |
| `account` | String | 客戶帳號 |
| `branch_no` | String | 分公司代號 |
| `account_type` | String | 帳號類型 (`stock` 證券, `futopt` 期貨) |

#### 6.1.2. OrderObject 委託內容 [15]

| 參數 | 類別 | 說明 |
| :--- | :--- | :--- |
| `buy_sell` | `BSAction` | 買賣別 (`Buy` 買, `Sell` 賣) |
| `symbol` | string | 股票代號 |
| `price` | string | 委託價格 (若非 `Limit` 限價，此欄代入 `None`) |
| `quantity` | int | 委託數量 |
| `market_type` | `MarketType` | 盤別 (整股、零股等) |
| `price_type` | `PriceType` | 價格旗標 (限價、市價、漲停等) |
| `time_in_force` | `TimeInForce` | 委託條件 (ROD, FOK, IOC) |
| `order_type` | `OrderType` | 委託類別 (現股、融資、現沖先賣等) |
| `user_def` (optional) | string | 用戶自定義 (最長10個字元，不支援特殊字元及中文、不適用興櫃) |

#### 6.1.3. OrderResult 委託資訊 [15]

| 參數 | 類別 | 說明 |
| :--- | :--- | :--- |
| `function_type` | int | 功能別 (0 新單, 15 改價, 30 刪單, 90 失敗等) |
| `seq_no` | string | 委託單流水序號 |
| `order_no` | string | 委託書號 |
| `stock_no` | string | 股票代號 |
| `buy_sell` | `BSAction` | 買賣別 |
| `price` | float | 原始委託價格 |
| `quantity` | int | 原始委託股數 |
| `status` | int | 委託單狀態 (詳見 6.2.6) |
| `after_price` | float | 有效委託價格 |
| `after_qty` | int | 有效委託股數（包含已成交部分） |
| `filled_qty` | int | 成交股數 |
| `filled_money` | int | 成交價金 |
| `before_qty` | int | 改單前有效量 |
| `before_price` | float | 改單前有效價 |
| `error_message` | string | 錯誤訊息 |
| `details` | list | 委託歷程 (僅 `get_order_results_detail` 有值) |

#### 6.1.4. FilledData 成交回報物件 [15]

| 參數 | 類別 | 說明 |
| :--- | :--- | :--- |
| `filled_no` | string | 成交流水號 |
| `filled_avg_price` | float | 成交均價 |
| `filled_qty` | int | 成交股數 |
| `filled_price` | float | 成交單價 |
| `filled_time` | string | 成交時間 |
| `user_def` | string | 用戶自定義 (只有主動回報才回傳) |
| `seq_no` | string | 委託單流水序號 (只有主動回報才回傳) |

#### 6.1.5. Inventory 庫存資訊 [12]

| 參數 | 類別 | 說明 |
| :--- | :--- | :--- |
| `stock_no` | string | 股票代號 |
| `order_type` | `OrderType` | 委託單類型 (現股、融資等) |
| `lastday_qty` | int | 昨日庫存餘額 |
| `today_qty` | int | 今日庫存餘額 |
| `tradable_qty` | int | 可委託股數 |
| `odd` | Object | 零股庫存資訊 (包含 `today_qty`, `tradable_qty` 等) |

### 6.2. 常數 (Constants) 欄位對應數值

#### 6.2.1. BSAction 買賣別 [15]

| Name | Meaning |
| :--- | :--- |
| `Buy` | 買 |
| `Sell` | 賣 |

#### 6.2.2. MarketType 盤別與數量限制 [15]

| Name | Meaning | Quantity Unit | Quantity Ranges |
| :--- | :--- | :--- | :--- |
| `Common` | 整股 | 千股 | 1000 ~ 499000 |
| `Fixing` | 定盤 | 千股 | 1000 ~ 499000 |
| `IntradayOdd` | 盤中零股 | 股 | 1 ~ 999 |
| `Odd` | 盤後零股 | 股 | 1 ~ 999 |
| `Emg` | 興櫃 | 千股 | 1000 ~ 499000 |
| `EmgOdd` | 興櫃零股 | 股 | 1 ~ 999 |

**MarketType 可用 PriceType 與 TimeInForce 對照表：**

| MarketType | Available PriceType | Available TimeInForce |
| :--- | :--- | :--- |
| `Common` | `Limit`、`LimitUp`、`LimitDown`、`Market`、`Reference` | `ROD`、`IOC`、`FOK` |
| `Fixing` | `Reference` | `ROD` |
| `IntradayOdd` | `Limit`、`LimitUp`、`LimitDown`、`Reference` | `ROD` |
| `Odd` | `Limit`、`LimitUp`、`LimitDown`、`Reference` | `ROD` |
| `Emg` | `Limit` | `ROD` |
| `EmgOdd` | `Limit` | `ROD` |

#### 6.2.3. PriceType 價格類型 [15]

| Name | Meaning |
| :--- | :--- |
| `Limit` | 限價 |
| `LimitUp` | 漲停 |
| `LimitDown` | 跌停 |
| `Market` | 市價 |
| `Reference` | 參考價 (定盤時為定盤價) |

#### 6.2.4. TimeInForce 委託條件 [15]

| Name | Meaning |
| :--- | :--- |
| `ROD` | 當日有效 (Rest of Day) |
| `FOK` | 全部成交否則取消 (Fill-or-Kill) |
| `IOC` | 立即成交否則取消 (Immediate-or-Cancel) |

#### 6.2.5. OrderType 委託類別 [15]

| Name | Meaning |
| :--- | :--- |
| `Stock` | 現股 |
| `Margin` | 融資 |
| `Short` | 融券 |
| `DayTrade` | 現沖先賣 |
| `SBL` | 借券 |

#### 6.2.6. Status 委託單狀態代碼 (錯誤代碼與例外處理) [15]

| Value | Name | 說明 |
| :--- | :--- | :--- |
| `0` | 預約單 | |
| `4` | 系統將委託送往後台 | (請用 `GetOrderResult` 查詢狀態) |
| `8` | 後台傳送中 | (請用 `GetOrderResult` 查詢狀態) |
| `9` | 連線逾時 | (請稍後再使用 `GetOrderResult` 查詢狀態 or 聯絡您的營業員) |
| `10` | **委託成功** | |
| `30` | 未成交刪單成功 | |
| `40` | 部分成交，剩餘取消 | |
| `50` | **完全成交** | |
| `90` | **失敗** | |
| `14` | 改價 ACK | (委託單歷程查詢標示) |
| `24` | 改量 ACK | (委託單歷程查詢標示) |
| `34` | 刪單 ACK | (委託單歷程查詢標示) |
| `15` | 改價成功 | (歷史委託單查詢) |
| `20` | 改量成功 | (歷史委託單查詢) |
| `19` | 改價失敗 | (主動回報) |
| `29` | 改量失敗 | (主動回報) |
| `39` | 刪單失敗 | (主動回報) |

#### 6.2.7. Function\_type 功能類別代碼 [15]

| Value | Name |
| :--- | :--- |
| `0` | 新單 |
| `10` | 新單執行 |
| `15` | 改價 |
| `20` | 改量 |
| `30` | 刪單 |
| `50` | 完全成交 (for 委託單歷程查詢) |
| `90` | 失敗 |

---

## 7. 下單限制與風控規則

### 7.1. 速率限制

*   **查詢 API 限制：** 查詢發送的次數為 **每秒 5 次**，若超出上限，請稍後再試 [13]。
*   **交易限制：** 文件中未明確指出交易 API 的速率限制，但建議遵循金融交易系統的常規，避免在短時間內發送過多交易請求。

### 7.2. 憑證、簽章、加密、Hash、Token 規範

富邦 TradeAPI 採用 **憑證** (`.pfx` 檔案與密碼) 進行身份驗證和連線建立 [4]。

*   **憑證：** 登入時需提供憑證路徑 (`cert_path`) 和憑證密碼 (`cert_pass`)。
*   **Token/Session：** SDK 內部處理連線與 Session 維護，使用者無需直接操作 Token 或 Session。
*   **加密/簽章/Hash：** 這些安全機制由 SDK 內部封裝處理，確保交易安全，使用者無需手動處理。

### 7.3. 需要注意事項與容易踩到的坑

1.  **Python 版本支援：** 確保 Python 版本在 3.8 到 3.12 之間，**v2.0.1 後不支援 Python 3.7** [1] [2]。
2.  **憑證路徑與密碼：** 登入時必須提供正確的憑證路徑和密碼。若憑證使用預設密碼，新版 SDK 支援省略密碼參數 [3]。
3.  **`user_def` 欄位限制：**
    *   僅可使用 **ASCII 33-126 範圍中字元**，最多 **10 個字元** [2]。
    *   若字元合規但長度超過 10 字元，將自動縮減至 10 字元並帶入下單 [2]。
    *   若字元不合規 (如中文或特殊字元)，則自動將 `user_def` 帶入空值 [2]。
    *   此欄位**不適用於興櫃** [15]。
4.  **改價/改量參數互斥：** 在建立 `ModifyPriceObj` 時，`price` 和 `price_type` 欄位只能擇一填入，另一個必須為空值或 `None` [7]。
5.  **零股與整股數量單位：** 不同的 `MarketType` (盤別) 對應的 `quantity` 單位和範圍不同，例如整股單位是**千股**，零股單位是**股** [15]。
6.  **API 權限問題：** 在爬取過程中，部分 API 頁面 (如歷史查詢、配額查詢、批次委託等) 遭遇 **HTTP ERROR 403** 權限不足，這可能意味著這些頁面需要特定的 IP 或登入狀態才能存取。請確保您的環境符合富邦證券的存取要求。

---

## 8. Python Developer 快速入門手冊

本手冊旨在提供 Python 開發者快速上手富邦 TradeAPI 的核心步驟。

### 步驟 1: 環境準備與 SDK 安裝

1.  **確認 Python 版本：** 確保您的 Python 版本為 3.8 ~ 3.12。
2.  **下載 SDK：** 從富邦 TradeAPI 網站下載對應作業系統的 `fubon_neo-*.whl` 檔案。
3.  **安裝套件：**
    ```bash
    pip install fubon_neo-<version>-cp37-abi3-win_amd64.whl
    ```

### 步驟 2: 登入與初始化

將您的憑證檔案 (`.pfx`) 放在程式目錄下，並使用以下程式碼登入：

```python
from fubon_neo.sdk import FubonSDK, Order
from fubon_neo.constant import TimeInForce, OrderType, PriceType, MarketType, BSAction

# 1. 初始化 SDK
sdk = FubonSDK()

# 2. 登入 (替換為您的真實資訊)
accounts = sdk.login(
    "您的身分證字號", 
    "您的登入密碼", 
    "您的憑證路徑", 
    "您的憑證密碼"
)

# 3. 取得第一個帳號物件
account = accounts.data[0]

print(f"登入成功！帳號：{account.account} ({account.name})")
```

### 步驟 3: 核心交易操作 (下單、查詢)

#### 3.3.1. 買入股票 (Place Order)

```python
# 範例：以限價 66 元買入富邦金(2881) 2張 (2000股)
order = Order(
    buy_sell = BSAction.Buy,
    symbol = "2881",
    price =  "66",
    quantity =  2000,
    market_type = MarketType.Common, # 整股
    price_type = PriceType.Limit,    # 限價
    time_in_force = TimeInForce.ROD, # 當日有效
    order_type = OrderType.Stock,    # 現股
    user_def = "My_Trade"
)

result = sdk.stock.place_order(account, order)
print("下單結果:", result)
```

#### 3.3.2. 查詢委託單狀態 (Get Order Results)

```python
# 查詢當日所有委託單
order_results = sdk.stock.get_order_results(account)

if order_results.is_success and order_results.data:
    print("當日委託單列表:")
    for order in order_results.data:
        print(f"  - 股票: {order.stock_no}, 狀態: {order.status}, 委託書號: {order.order_no}")
        
    # 取得第一個委託單物件，用於後續改單/刪單
    target_order = order_results.data[0]
else:
    print("無委託單或查詢失敗。")
```

#### 3.3.3. 修改委託價格 (Modify Price)

```python
# 假設 target_order 是上一步取得的委託單物件
if target_order:
    # 建立改價物件：將價格改為 66.5 元
    modify_price_obj = sdk.stock.make_modify_price_obj(target_order, "66.5") 
    
    # 執行改價
    modify_result = sdk.stock.modify_price(account, modify_price_obj)
    print("改價結果:", modify_result)
```

#### 3.3.4. 刪除委託單 (Cancel Order)

```python
# 假設 target_order 是欲刪除的委託單物件
if target_order:
    cancel_result = sdk.stock.cancel_order(account, target_order)
    print("刪單結果:", cancel_result)
```

### 步驟 4: 查詢帳務資訊

```python
# 查詢庫存
inventory_result = sdk.accounting.inventories(account)
print("庫存查詢結果:", inventory_result)

# 查詢未實現損益
pnl_result = sdk.accounting.unrealized_gains_and_loses(account)
print("未實現損益查詢結果:", pnl_result)
```

### 步驟 5: 登出

```python
sdk.logout()
print("已安全登出。")
```

---

## 參考資料 (References)

[1] 富邦新一代API 簡介. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/introduction
[2] SDK 下載. URL: https://www.fbs.com.tw/TradeAPI/docs/download/download-sdk
[3] 快速開始. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/quickstart
[4] 登入 API. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/library/python/login
[5] 登出 API. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/library/python/logout
[6] 建立委託單 API. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/library/python/trade/placeOrder
[7] 修改委託價格 API. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/library/python/trade/modifyPrice
[8] 修改委託單數量 API. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/library/python/trade/modifyQuantity
[9] 刪除委託單 API. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/library/python/trade/cancelOrder
[10] 取得委託單結果 API. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/library/python/trade/getOrderResults
[11] 取得委託單結果 (含歷程) API. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/library/python/trade/getOrderResultsDetail
[12] 庫存查詢 API. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/library/python/accountManagement/inventories
[13] 帳務範例. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/guide/account_example
[14] 主動回報範例. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/guide/report_example
[15] 參數對照表. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/library/python/EnumMatrix
[16] 交易範例. URL: https://www.fbs.com.tw/TradeAPI/docs/trading/guide/trade_example
