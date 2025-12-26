<div id="577dd91d-778c-40c3-9b29-dcd18a1fe716" class="cell markdown">

# **富邦新一代API - Python範例程式碼**

</div>

<div id="1ba16873-3a63-4abc-b977-444048c1b43c" class="cell markdown">

# 安裝

</div>

<div id="caa5740d-46d4-4845-83fb-759116b36c95" class="cell markdown"
tags="[]">

## 若已安裝過 SDK，可**忽略**此部分

</div>

<div id="56a6dfab-c332-461b-94cc-3d61fc816a38" class="cell markdown">

### 安裝新一代API Python SDK

此範例使用Windows版本檔案 <br> ***註:*** SDK檔案名稱 (ex.
fubon_neo-1.0.3-cp37-abi3-win_amd64.whl) 請根據實際下載.whl名稱修改 <br>
***註2:*** SDK檔案需與本jupyter
notebook檔案至於同一資料夾內，或是修改以下指令之SDK檔案路徑

</div>

<div id="d4f1146c-7532-4f54-9c1b-0d7d95fc4e99" class="cell code"
scrolled="true">

``` python
# Pip install SDK
!pip install --force-reinstall --no-cache fubon_neo-1.0.3-cp37-abi3-win_amd64.whl
```

</div>

<div id="d510c5aa-566d-4510-a09a-b332f834e026" class="cell markdown">

# SDK 版本檢視

</div>

<div id="fa29cddf-bef8-4661-9968-9adce5b12504" class="cell code">

``` python
import fubon_neo
```

</div>

<div id="cf7103fe-f52e-481a-aba2-838e491e8def" class="cell code">

``` python
fubon_neo.__version__
```

</div>

<div id="dea75f51-6a9c-42c5-9a50-71360e0c770d" class="cell markdown">

# 準備

</div>

<div id="dc1e496b" class="cell code" scrolled="true">

``` python
 # 匯入 SDK Library
from fubon_neo.sdk import FubonSDK, Order
from fubon_neo.constant import TimeInForce, OrderType, PriceType, MarketType, BSAction
```

</div>

<div id="c522db59-9ffa-42ba-bb83-a92364dc8308" class="cell code">

``` python
# 連結 API Server
sdk = FubonSDK()
```

</div>

<div id="5e0afd79-950b-4787-b3c0-21c87d6330ea" class="cell markdown"
tags="[]">

## 登入

</div>

<div id="9bd136f1-f514-4cb1-9dfa-6d2874aefb88" class="cell code">

``` python
accounts = sdk.login("H123oooooo", "oooooooo", "./H123oooooo.pfx", "oooooooo")   # 登入帳號 輸入:帳號、密碼、憑證路徑、憑證密碼
print(accounts)
```

</div>

<div id="fc145f59-37d2-4cc4-8db7-c365c235a4c4" class="cell markdown"
jp-MarkdownHeadingCollapsed="true" tags="[]">

# 行情元件

</div>

<div id="0153a787-a51d-4ab4-974f-c10827adfe18" class="cell markdown">

## **建立行情元件連線**

</div>

<div id="dd9f7618-843b-40f1-a59c-faffd834be84" class="cell code">

``` python
sdk.init_realtime() # 建立行情元件連線
```

</div>

<div id="b727a01f-70ca-485d-ad93-3742c72f2248" class="cell markdown"
tags="[]">

## 行情 WebSocket 報價

</div>

<div id="bb54b560-91bf-4ea1-956c-891df7cc8534" class="cell markdown">

### WebSocket callback functions 設定

</div>

<div id="c860f49a" class="cell code">

``` python
import json
import traceback

subscribe_ids = []  # 訂閱頻道 id 列表

def handle_connect():  # 連線成功 callback
    print("行情連接成功")

def handle_disconnect(code, message):  # 連接斷線 callback
    print(f"行情連接斷線: {code}, {message}")

def handle_message(message): # 處理接收訊息 callback
    try:
        msg = json.loads(message)
        event = msg["event"]
        data = msg["data"]
    
        if event == "pong":
            return
        
        if event == "subscribed":
            id = data["id"]
            
            if id in subscribe_ids:
                print(f"Error: 訂閱 id {id} 已存在列表中")
            else:
                subscribe_ids.append(id)
    
        elif event == "unsubscribed":
            id = data["id"]
            
            try:
                subscribe_ids.remove(id)
            except:
                print(f"Error: 查無此筆訂閱 id 資料, id {id}")
    
        print(f'market data message: {message}')           
        
    except Exception as e:
        handle_error(f'Error parsing JSON: {e}', traceback.format_exc())

def handle_error(error,traceback_info=None):  # 處理程式錯誤訊息 callback
    print(f'market data error: {error}')
    if traceback_info:
        print(f'Traceback:\n{traceback_info}')

stock = sdk.marketdata.websocket_client.stock
stock.on("connect", handle_connect)
stock.on("message", handle_message)
stock.on("disconnect", handle_disconnect)
stock.on("error", handle_error)

stock.connect()  # WebSocket 連線
```

</div>

<div id="69db80eb-abc6-4b2a-9f43-09ff7cdfbc06" class="cell markdown">

###### 訂閱商品資料

</div>

<div id="68e66a3d" class="cell code">

``` python
# 訂閱股票最新成交資訊
stock.subscribe({ 
        "channel": 'trades', 
        "symbol": '1101',
        "intradayOddLot": True,
        })
```

</div>

<div id="b4f9bb87" class="cell code" scrolled="true">

``` python
# 訂閱股票最新最佳五檔委買委賣資訊
stock.subscribe({ 
    'channel': 'books', 
    'symbol': '2330'
})
```

</div>

<div id="ba061802" class="cell code">

``` python
# 訂閱股票最新指數行情資料
stock.subscribe({ 
    'channel': 'indices', 
    'symbol': 'IR0001'
})
```

</div>

<div id="7c9af698" class="cell code">

``` python
target_id = "Dn90D2VM2McNXqzJx9gpsz5q8A460Qu2MA"  #欲取消訂閱之頻道編號(id)

result = stock.unsubscribe(
        {
          "id": target_id
        }
)
```

</div>

<div id="028e7d68-3771-482d-97df-7a8bd9cbfe92" class="cell markdown">

### 斷開 WebSocket 連線

</div>

<div id="8cabf594" class="cell code">

``` python
stock.disconnect()
```

</div>

<div id="8e3b8caf-b2c9-4f3f-aab5-862f191953fc" class="cell markdown"
tags="[]">

## 行情 WebAPI 查詢

</div>

<div id="b3f284cc-7db2-43e3-87cd-72ee5780398c" class="cell code">

``` python
# 建立行情查詢 WebAPI 連線 Object Instance
restStock = sdk.marketdata.rest_client.stock  
```

</div>

<div id="9cde4cd9-fdfc-42c0-b691-95e3c0e46e00" class="cell markdown">

### 日內行情

</div>

<div id="43aaf226" class="cell code">

``` python
# 股票或指數列表（依條件查詢）
result = restStock.intraday.tickers(type='EQUITY', exchange="TWSE", market="TSE")
stock_list = ["8467", "9103", "2330"]  # 抽樣查詢之股票 symbols

print(f"資料長度: {len(result['data'])}\n")

for ticker in result["data"]:
    if ticker["symbol"] in stock_list:
        print(ticker)
```

</div>

<div id="ec070e7a" class="cell code">

``` python
# 取得股票資訊 (依股票代碼查詢)
result = restStock.intraday.ticker(symbol='2330')
print(result)
```

</div>

<div id="e45f4aa6" class="cell code">

``` python
# 股票即時報價（依代碼查詢）
result = restStock.intraday.quote(symbol="2330")
print(result)
```

</div>

<div id="80a245c5" class="cell code" scrolled="true">

``` python
# 股票價格Ｋ線（依代碼查詢）
result = restStock.intraday.candles(symbol='2330', timeframe=5)
print(result)
```

</div>

<div id="8281fa99" class="cell code" scrolled="true">

``` python
# 股票成交明細（依代碼查詢）
result = restStock.intraday.trades(symbol='2330')
print(result)
```

</div>

<div id="17e2d969" class="cell code">

``` python
# 股票分價量表（依代碼查詢）
result = restStock.intraday.volumes(symbol='2330')
print(result)
```

</div>

<div id="a152745f-3ab8-4d12-bbdc-8b4cec434c70" class="cell markdown">

### 行情快照

</div>

<div id="8a5c2364" class="cell code" scrolled="true">

``` python
# 股票行情快照（依市場別）
result = restStock.snapshot.quotes(market='TSE')
print(result)
```

</div>

<div id="246f32b9" class="cell code" scrolled="true">

``` python
# 股票漲跌幅排行（依市場別）
result = restStock.snapshot.movers(market='TSE', direction='up', change='percent')
print(result)
```

</div>

<div id="ebd25cd7" class="cell code" scrolled="true">

``` python
# 股票成交量值排行（依市場別）
result = restStock.snapshot.actives(market='TSE', trade='volume')
print(result)
```

</div>

<div id="2df4a4e6-c642-4cb5-b183-9f2687460610" class="cell markdown">

### 歷史行情

</div>

<div id="27b9c4b2" class="cell code" scrolled="true">

``` python
# 取得 1 年內歷史股價（依代碼查詢）
# P.S. 目前分Ｋ無法指定開始日期（from） 與 結束日期（to），一律回傳近五日資料，並且無法選擇 turnover 與 change 的欄位
result = restStock.historical.candles(**{"symbol": "2330", "from": "2023-07-26", "to": "2024-01-30"})
print(result)
```

</div>

<div id="93273863" class="cell code">

``` python
# 取得近 52 週股價數據（依代碼查詢）
result = restStock.historical.stats(symbol="2330")
print(result)
```

</div>

<div id="878c57ed-1936-4927-a497-12793f0da641" class="cell markdown"
jp-MarkdownHeadingCollapsed="true" tags="[]">

# 交易 (單筆)

</div>

<div id="0a4a324c-9732-4d73-8a2d-a4c52e91120b" class="cell markdown"
tags="[]">

### 建立委託單

</div>

<div id="53a4543a" class="cell code">

``` python
# 定義訂單內容
order = Order(
    buy_sell = BSAction.Buy,
    symbol = "2330",
    price = None,
    quantity = 1000, # 股數; 1000為一張
    market_type = MarketType.Common,
    price_type = PriceType.Reference,
    time_in_force = TimeInForce.ROD,
    order_type = OrderType.Stock,
    user_def = None, # optional field
);

# 列印訂單內容
print(order)
```

</div>

<div id="76fb7221-7485-4bd4-bfd4-916ed4a45fed" class="cell code">

``` python
# 下單
order_reponse = sdk.stock.place_order(accounts.data[0], order)
print(order_reponse)
```

</div>

<div id="3e9c16e4-cedb-4216-a765-cf77f0f7a1a8" class="cell markdown"
tags="[]">

### 取得委託單結果

</div>

<div id="428f9001-9b71-411a-85f0-305ca36af160" class="cell code">

``` python
result = sdk.stock.get_order_results(accounts.data[0])
print(f"筆數: {len(result.data)}")
i = 0
for order_result in result.data:
    print(f"第 {i+1} 筆:")
    print(order_result, end="\n\n")
    i += 1
```

</div>

<div id="3d033533-2fbf-4b10-9398-428e2a450510" class="cell markdown"
tags="[]">

#### 使用範例：使用委託書或流水序號取得特定委託單物件

</div>

<div id="b4c15525-0768-4d14-8c05-62781e50dd18" class="cell code"
scrolled="true">

``` python
def get_order_by_no(orders, order_or_seq_no, use_order_no=True):
    if orders.data is None:
        print(f"查無委託單資訊")
        return None

    for order in orders.data:
        if use_order_no:  # 以委託書號查詢
            if order.order_no is not None and order.order_no == order_or_seq_no:
                # print(f"提取委託單: {order}")
                return order
        else:  # 以委託單流水序號查詢
            if order.seq_no is not None and order.seq_no == order_or_seq_no:
                # print(f"提取委託單: {order}")
                return order

    # 查無委託單
    field_name = "委託書號" if use_order_no else "委託單流水序號"
    print(f"{field_name} {order_or_seq_no} 查無委託單")
    return None

# 使用範例 1: 以委託書號查詢
orders = sdk.stock.get_order_results(accounts.data[0])  # 查詢所有委託單
order = get_order_by_no(orders, "x0003", use_order_no=True)  # x0016 為目標委託書號
print(f"使用範例 1: 結果委託單 {order}\n")

# # 使用範例 2: 以委託單流水序號查詢
# orders = sdk.stock.get_order_results(accounts.data[0])  # 查詢所有委託單
# order2 = get_order_by_no(orders, "00000237234", use_order_no=False)  # 00000237234 為目標委託單流水序號
# print(f"使用範例 2: 結果委託單 {order2}")
```

</div>

<div id="669fc3e2-1042-439f-9951-9ba2678a2366" class="cell markdown"
tags="[]">

### 改價

</div>

<div id="bd30bdec-42c1-44f1-8d51-3b6fd019ea28" class="cell code"
scrolled="true" tags="[]">

``` python
# 使用範例：使用委託單號取得欲修改之委託單物件
target_order = None
target_order_number = "l0001"  # 欲查找之委託單號

response = sdk.stock.get_order_results(accounts.data[0])

if response.is_success:
    for order in response.data:
        if order.order_no == target_order_number:  # 取第一個狀態為成功的委託單為例
            target_order = order

    if target_order is not None:
        print(target_order)
    else:
        print(f"單號 {target_order_number}，查無委託單")

else:
    print("查無資料")
    print(f"response: {response}")
```

</div>

<div id="b99e005c-4138-42e1-9b47-ea46f2a18ede" class="cell code"
scrolled="true">

``` python
# 單筆改價
target_order = order
modify_price_obj = sdk.stock.make_modify_price_obj(target_order, "542",)  # 改價
response = sdk.stock.modify_price(accounts.data[0], modify_price_obj)  # 送出改價單

# 印出回應
# print(f"目標委託單:\n{target_order}\n")
print(f"修改回覆:\n{response}")
```

</div>

<div id="8980f604-0d1f-4596-bf03-a8302bc7f675" class="cell markdown"
tags="[]">

### 改量

</div>

<div id="ccafd6de" class="cell code" tags="[]">

``` python
#單筆改量
target_order = order
modify_quantity_obj = sdk.stock.make_modify_quantity_obj(target_order, 1000)  # 改量
response = sdk.stock.modify_quantity(accounts.data[0], modify_quantity_obj)  # 送出改量單

# 印出回應
# print(f"目標委託單:\n{target_order}\n")
print(f"修改回覆:\n{response}")
```

</div>

<div id="a4cdf911-b34a-4b67-a589-d96ee34abc51" class="cell markdown"
jp-MarkdownHeadingCollapsed="true" tags="[]">

#### 刪單

</div>

<div id="23a66423-b486-43db-aed5-12f907ca244c" class="cell code">

``` python
# 函數: 刪單 by 單號
def del_order(order_no, account):
    if not isinstance(order_no, str):
        print(f"請輸入單號字串，例如\"x0001\"")
        return None

    # 取得委託單 object
    target_order = None
    orders = sdk.stock.get_order_results(account)

    for order in orders.data:
        if order.order_no == order_no:
            target_order = order

    if target_order is None:
        print(f"查無目標委託單, 目標委託單號 {order_no}. 帳號:\n{account}")
        return None
    else:
        response = sdk.stock.cancel_order(account, target_order)
        print(f"刪單回報:\n{response}\n\n")
        return response

# 刪單
response = del_order("x0005", accounts.data[0])  # 可修改單號及帳號

if response is None:
    print("刪單函數執行錯誤")

else:
    target_order_number = response.data.order_no
    # 取得新的委託單資訊
    target_order = None
    orders = sdk.stock.get_order_results(accounts.data[0])
    for order in orders.data:
        if order.order_no == target_order_number:
            target_order = order
            
    if target_order is None:
        print(f"查無目標委託單。目標委託單號 {target_order_number}")
    else:
        print(f"新委託單資訊(單筆):\n{target_order}\n\nstatus: {target_order.status}")  # status 30 代表刪單成功
```

</div>

<div id="4865b6ac-ea6d-40e7-bacc-dea82d518d7f" class="cell markdown"
tags="[]">

### 查詢歷史委託

</div>

<div id="55b3f868" class="cell code" scrolled="true">

``` python
# 歷史委託
response = sdk.stock.order_history(accounts.data[0], "20240313", "20240313")  # 只供查詢兩日內之歷史資料

if response.is_success:
    
    order_history = response.data
    
    print(f"筆數: {len(order_history)}\n")

    i = 0
    for order_his in order_history:
        i += 1
        print(f"第 {i} 筆:\n{order_his}\n")
        
else:
    print("查尋錯誤")
    print(f"response: {response}")
```

</div>

<div id="595455a1-ec81-40f7-9a44-c5a45d534b55" class="cell markdown"
tags="[]">

### 查詢歷史成交

</div>

<div id="1a2447f3" class="cell code">

``` python
# 歷史成交
result = sdk.stock.filled_history(accounts.data[0], "20240313", "20240313")  # 只供查詢兩日內之歷史資料
print(result)
```

</div>

<div id="6a56429b-2cde-4b32-ad14-988f91259eb2" class="cell markdown"
tags="[]">

### 資券配額查詢

</div>

<div id="27d4b068-bc06-4eef-8aca-6bcd1cf6487b" class="cell code">

``` python
# 資券配額查詢
result = sdk.stock.margin_quota(accounts.data[0], "2330")
print(result)
```

</div>

<div id="ed17d7ae-429c-48ab-b5dd-32862cc61cde" class="cell markdown"
tags="[]">

### 現冲券配額查詢

</div>

<div id="c61fb8cf-094a-4c3a-b8ce-dafa0d6f3211" class="cell code">

``` python
# 現冲券配額查詢
result = sdk.stock.daytrade_and_stock_info(accounts.data[0], "2330")
print(result)
```

</div>

<div id="d2b33dc2-f779-4761-b103-5f04c2b8c355" class="cell markdown"
jp-MarkdownHeadingCollapsed="true" tags="[]">

# 交易 (批次)

</div>

<div id="2834077d-09cd-4afb-88d1-b96be5781627" class="cell markdown"
tags="[]">

### 建立批次委託單

</div>

<div id="883a77de-95f4-4798-91d1-5f384199300e" class="cell code">

``` python
# 建立欲委託清單
orders = [
  Order(
    buy_sell = BSAction.Buy,
    symbol = "2881",
    price = None,
    quantity = 2000,
    market_type = MarketType.Common,
    price_type = PriceType.LimitDown,
    time_in_force = TimeInForce.ROD,
    order_type = OrderType.Stock,
    user_def = "batch1" # optional field
), Order(
    buy_sell = BSAction.Buy,
    symbol = "1101",
    price = None,
    quantity = 1000,
    market_type = MarketType.Common,
    price_type = PriceType.LimitDown,
    time_in_force = TimeInForce.ROD,
    order_type = OrderType.Stock,
    user_def = "batch2" # optional field
) ]

orders
```

</div>

<div id="b45b6a66-aa5e-4a66-b636-526330e10489" class="cell code"
scrolled="true">

``` python
# 建立批次委託單
result = sdk.stock.batch_place_order(accounts.data[0], orders)
print(result)
```

</div>

<div id="bc21a7d2-8d38-4af6-b980-5b89ebabdcc4" class="cell markdown"
tags="[]">

### 取得批次委託送單紀錄

</div>

<div id="e0a80372-0705-4203-b50c-58c08527bda5" class="cell markdown">

***註：*** 此僅為送單紀錄，無交易狀態更新

</div>

<div id="7bc4fcdf-115a-452b-a946-1477e542779f" class="cell code">

``` python
# 取得批次委託列表
result = sdk.stock.batch_order_lists(accounts.data[0])
print(result)
```

</div>

<div id="4491e9d0-e812-448a-8801-1de8c86e9571" class="cell markdown"
tags="[]">

### 取得批次委託送單紀錄明細

</div>

<div id="f81b7e5e-97db-4e13-bfaf-b6a1101c9311" class="cell markdown">

***註：*** 此僅為送單紀錄，無交易狀態更新

</div>

<div id="7e5852a8-1909-44fc-945b-575a1280822f" class="cell code"
scrolled="true">

``` python
# 取得批次委託列表
batch_list = sdk.stock.batch_order_lists(accounts.data[0])

# 取得單筆批次委託明細
target_batch_result = batch_list.data[0]  # 單筆批次委託結果
result = sdk.stock.batch_order_detail(accounts.data[0], target_batch_result)

print(result)
```

</div>

<div id="6947e684-a301-484d-a5d9-5a16cf5f8c9c" class="cell markdown"
tags="[]">

### 批次修改

</div>

<div id="d0e7eb5f-a8d1-4bbb-9b60-07b54c57d037" class="cell code">

``` python
# 查詢委託單
response = sdk.stock.get_order_results(accounts.data[0])

# 取得此前批次下單(同Timestamp)成功之委託單
result_orders = []

if not response.is_success:
    print(f"委託單查詢失敗, 查詢結果:\n{orders}")

else:  # 委託單查詢成功
    for order in response.data:
        if (order.user_def is not None) and (str(timestamp) in order.user_def):
            result_orders.append(order)

# 列印
print(f"取得委託單結果:\n{result_orders}")
```

</div>

<div id="7c33cb24-1cf0-4a68-9a47-6d15ed21bfe1" class="cell markdown"
tags="[]">

#### 批次修改委託價格

</div>

<div id="23d04e4a-2500-4f22-a782-0339345d5227" class="cell code">

``` python
# 建立批次委託修改物件
modify_objects = []

for order in result_orders:
    the_price = order.after_price

    # 設定擬改價格 (自動設定預修改，僅為測試範例)
    if (the_price * 100) % 10 > 0:
        to_be_price = round(the_price + 0.05, 2)
    elif (the_price * 10) % 10 > 0:
        to_be_price = round(the_price + 0.1, 1)
    else:
        to_be_price = round(the_price + 1)

    # 建立改價 obj
    the_modify_price_obj = sdk.stock.make_modify_price_obj(order, str(to_be_price))
    print(f"委託單編號 {order.order_no}, 現價 {the_price}, 擬改價 {to_be_price}")

    # 放入批次列表
    modify_objects.append(the_modify_price_obj)

# 開始批次改價
if len(modify_objects) > 0:
    modified_results = sdk.stock.batch_modify_price(accounts.data[0], modify_objects)
    
    # 處理批次修改委託價格回傳結果
    if modified_results.is_success:
        print("修改成功")
        print(modified_results.data)
    else:
        print("修改失敗", modified_results.message)

else:
    print("改價列表為空白")
```

</div>

<div id="e35cbc3f-7cb6-40da-971e-6f6092bcce62" class="cell markdown"
jp-MarkdownHeadingCollapsed="true" tags="[]">

#### 批次修改委託數量

</div>

<div id="ae3d2076-078f-4c84-a8e6-5dd82b7dd87d" class="cell code">

``` python
# 查詢委託單
response = sdk.stock.get_order_results(accounts.data[0])

# 取得此前批次下單(同Timestamp)成功之委託單
result_orders = []

if not response.is_success:
    print(f"委託單查詢失敗, 查詢結果:\n{orders}")

else:  # 委託單查詢成功
    for order in response.data:
        if (order.user_def is not None) and (str(timestamp) in order.user_def):
            result_orders.append(order)

# 列印
print(f"取得委託單結果:\n{result_orders}")
```

</div>

<div id="58376016-c9bd-4c49-a53d-19e416f5a4b2" class="cell code">

``` python
# 建立批次委託修改物件
modify_objects = []

for order in result_orders:
    the_qty = order.after_qty

    if the_qty > 1000:
        to_be_qty = the_qty - 1000
        
        # 建立改價 obj
        the_modify_price_obj = sdk.stock.make_modify_quantity_obj(order, int(to_be_qty))
        print(f"委託單編號 {order.order_no}, 現量 {the_qty}, 擬改量 {to_be_qty}")
    
        # 放入批次列表
        modify_objects.append(the_modify_price_obj)

    else:
        print(f"委託單編號 {order.order_no}, 現量 {the_price}, 現量不足，略過")

# 開始批次改量
if len(modify_objects) > 0:
    modified_results = sdk.stock.batch_modify_quantity(accounts.data[0], modify_objects)
    
    # 處理批次修改委託量回傳結果
    if modified_results.is_success:
        print("修改成功")
        print(modified_results.data)
    else:
        print("修改失敗", modified_results.message)

else:
    print("改價列表為空白，出問題了!")
```

</div>

<div id="8c1de77d-6f56-4f16-b092-41af744ddef4" class="cell markdown"
tags="[]">

#### 刪除批次委託單

</div>

<div id="826c9e99-37a1-4b49-a2ef-f61bd8e95d69" class="cell code">

``` python
# 查詢委託單
response = sdk.stock.get_order_results(accounts.data[0])

# 取得此前批次下單(同Timestamp)成功之委託單
result_orders = []

if not response.is_success:
    print(f"委託單查詢失敗, 查詢結果:\n{orders}")

else:  # 委託單查詢成功
    for order in response.data:
        if (order.user_def is not None) and (str(timestamp) in order.user_def):
            result_orders.append(order)

# 列印
print(f"取得委託單結果:\n{result_orders}")
```

</div>

<div id="9ef4028e-925e-4bce-afce-d0bf6e1d4f60" class="cell code">

``` python
for order in result_orders:
    print(f"擬刪除之委託單編號 {order.order_no}\n")

# 開始批次刪除
if len(result_orders) > 0:
    cancel_result = sdk.stock.batch_cancel_order(accounts.data[0], result_orders)
    
    # 處理批次刪除回傳結果
    if cancel_result.is_success:
        print("刪除成功")
        print(cancel_result.data)
    else:
        print("刪除失敗", cancel_result.message)
```

</div>

<div id="154c979c-6c4b-4e7e-a602-5a472543db9a" class="cell markdown"
jp-MarkdownHeadingCollapsed="true" tags="[]">

# 帳務

</div>

<div id="0c166e3b-cdcd-492d-bbd1-be442b96647e" class="cell code">

``` python
# 顯示帳號資訊
accounts.data[0]
```

</div>

<div id="1d36bd14-2175-43e6-9677-c485e8886c2b" class="cell markdown"
tags="[]">

### 庫存查詢

</div>

<div id="cbe35ae8-4849-4a17-99bf-457bc222b15e" class="cell code"
scrolled="true">

``` python
# 庫存查詢
result = sdk.accounting.inventories(accounts.data[0])

if result.is_success:
    print(f"資料筆數: {len(result.data)}\n")
    i = 0
    for inv in result.data:
        i += 1
        print(f"第 {i} 筆\n")
        print(f"{inv}\n")
        
else:
    print("查詢失敗")
    print(result)
```

</div>

<div id="49cd1076-b293-4032-8c08-a5204d613e2e" class="cell markdown"
tags="[]">

### 未實現損益

</div>

<div id="73d842eb-5544-447d-87d0-d8f0f63d6596" class="cell code"
tags="[]">

``` python
# 未實現損益
result = sdk.accounting.unrealized_gains_and_loses(accounts.data[0])
print(result)
```

</div>

<div id="d308ffda-1d28-473b-83d4-8402d19c285c" class="cell markdown"
tags="[]">

### 已實現損益

</div>

<div id="50d74ac0-e6f0-48dc-beaf-5a481ed87221" class="cell code">

``` python
# 已實現損益
result = sdk.accounting.realized_gains_and_loses(accounts.data[0])
print(result)
```

</div>

<div id="9c0bad21-c075-4a5c-b041-150c858aea21" class="cell markdown">

### 維持率查詢

</div>

<div id="13ca8cdd-d871-4629-9fe2-121f754f7f94" class="cell code"
scrolled="true">

``` python
# 維持率
result = sdk.accounting.maintenance(accounts.data[0])
print(result)
```

</div>

<div id="9f94fdfa-b9a5-4b13-833e-c398b94eb853" class="cell markdown">

### 交割款查詢

</div>

<div id="688d07e0-6e38-433c-94ab-7343d1365405" class="cell code"
scrolled="true">

``` python
# 交割款
result = sdk.accounting.query_settlement(accounts.data[0],"3d")
print(result)
```

</div>

<div id="ea7dd084-622b-4ca8-bcc6-33ffb25386d1" class="cell markdown">

### 銀行餘額查詢

</div>

<div id="3928b7bf-0fbf-48ce-9c51-555c9f4e85b3" class="cell code">

``` python
# 銀行餘額
result = sdk.accounting.bank_remain(accounts.data[0])
print(result)
```

</div>

<div id="58314799-8bb0-4760-8bb5-bce1ed24fc5b" class="cell markdown"
jp-MarkdownHeadingCollapsed="true" tags="[]">

# 交易/帳務 主動回報

</div>

<div id="8e58dad4" class="cell code">

``` python
import time
import os 

# A callback to receive quote data
def on_order(err, content):
    print("==下單主動回報==")
    print(f"錯誤訊息 {err}")
    print(f"內容 {content}")
    print("========")
    
sdk.set_on_order(on_order) 

# A callback to receive quote data
def on_order_changed(err, content):
    print("==改單主動回報==")
    print(f"錯誤訊息 {err}")
    print(f"內容 {content}")
    print("========")
    
sdk.set_on_order_changed(on_order_changed) 

def on_filled(err, content):
    print("==成交主動回報==")
    print(f"錯誤訊息 {err}")
    print(f"內容 {content}")
    print("========")
    
sdk.set_on_filled(on_filled)

# A callback to receive quote data
def on_event(err, content):
    print("==事件主動回報==")
    print(f"錯誤訊息 {err}")
    print(f"內容 {content}")
    print("========")
    
sdk.set_on_event(on_event) 
```

</div>
