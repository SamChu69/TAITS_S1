# TAITS_DataSources_Universe.md
（TAITS 資料來源全集｜官方優先｜免費優先｜多層備援｜可審計可回放）

> 文件定位：母體資料層最高規格（對齊 00/01/02）
> 核心目標：
> 1) 任何新對話/新工程師都不需要通靈，知道「資料從哪來」
> 2) 資料來源必須可追溯、可替換、可備援、可降級
> 3) 免費優先，但不犧牲「可靠度與可回放性」

---

## 0. 名詞與中譯（避免看不懂）

- Data Source：資料來源
- Official Source：官方來源（最高可信）
- OpenAPI：開放介接 API（以 OAS / Swagger 為主）
- Fallback：備援來源
- Snapshot：快照（可回放的同一份事實）
- Data Quality：資料品質（缺值、延遲、異常、落後）
- SLA：服務水準（可用性、延遲、頻率；此處為內部目標）
- Rate Limit：頻率限制（呼叫上限）
- OAS：OpenAPI Specification（開放 API 規格）
- Evidence：證據（可審計的依據）

---

## 1. TAITS 資料治理最高原則（不可違反）

1) **官方優先**：TWSE / TPEx / MOPS / TAIFEX 之資料為第一層權威  
2) **免費優先**：在不影響「可回放」與「關鍵字段」前提下，優先使用免費來源  
3) **多層備援**：任何關鍵資料必須至少 2 層來源（主/備）  
4) **資料不足即降級**：關鍵資料缺失 → Regime 必須可進入 R10（不判斷/僅觀察）  
5) **觀察型衍生品**（期貨/選擇權/融資融券）在 TAITS 內定位為：
   - Regime Evidence（狀態證據）
   - Cross-Market Filter（跨市場濾網）
   - Weight Adjuster（權重調整器）
   - Risk Override（風險覆蓋）
   > **不是用來「交易那些商品」的策略。**

---

## 2. 官方資料來源（Tier-0 / Tier-1：必接）

> 下列為台灣市場母體級資料來源。只要它們存在，就必須作為第一優先。

### 2.1 TWSE 臺灣證券交易所 OpenAPI（上市）
- 名稱：TWSE OpenAPI（證交所開放資料 API）
- 入口（Base）：https://openapi.twse.com.tw/
- Swagger（範例）：https://openapi.twse.com.tw/v1/swagger.json
- 類型：市場交易資料、公司/產品資訊、公告類資料（依 TWSE 提供範圍）
- 頻率：依各端點（多為日/盤後；部分可近即時）
- TAITS 用途：
  - 股票/ETF 基本交易資訊（OHLCV、成交量、成交額）
  - 市場統計（大盤、類股、排行）
  - 公司層面資料（依 API 提供）

### 2.2 TPEx 證券櫃檯買賣中心 OpenAPI（上櫃/興櫃/創櫃）
- 入口：https://www.tpex.org.tw/openapi/
- Swagger（範例）：https://www.tpex.org.tw/openapi/swagger.json
- 類型：上櫃/興櫃/創櫃/債券等資料（依 TPEx 提供範圍）
- TAITS 用途：
  - 中小型題材股、輪動股之 Universe 建立
  - 上櫃市場結構特徵（波動、成交額、族群擴散）

### 2.3 MOPS 公開資訊觀測站（公司公告 / 財報 / 重大訊息）
- 入口：https://mopsov.twse.com.tw/mops/web/index
- 類型：公告、重大訊息、財報、股東會、董監事、股權等
- 介接策略：
  - 若官方提供可用結構化接口則優先
  - 若無完整 OpenAPI，需以「可回放」的抓取方式建立標準化資料（寫入 Snapshot）
- TAITS 用途：
  - Fundamental / Event：財報事件、法說、重大訊息、處分資產、增資減資等
  - Governance：公司治理與資訊揭露行為本身也是風險訊號

### 2.4 TAIFEX 臺灣期貨交易所 OpenAPI（期貨/選擇權：只觀察）
- OpenAPI 入口：https://openapi.taifex.com.tw/
- Swagger（範例）：https://openapi.taifex.com.tw/swagger.json
- 類型：期貨、選擇權、保證金、結算相關資訊（依 TAIFEX 公告範圍）
- TAITS 用途（Observe-only）：
  - 指數期貨（例：TX）對股市方向與波動的狀態證據
  - 選擇權 OI / 壓力帶（支撐/壓力）作為風險與出場優先權條件
  - 結算週/結算日「鎖價/釘住（Pinning）」風險旗標
  - 外資避險行為（若可得）作為真偽趨勢判斷

---

## 3. 政府資料開放平台（Tier-1：免費且可長期）
- 入口：https://data.gov.tw/
- 特性：多為「日/週/月」頻率；但穩定、合法、可回放
- TAITS 用途：
  - 宏觀：物價、產業、能源、交通、人口、景氣指標（作為 regime 長週期背景）
  - 金融：利率、匯率、債券等（視可得資料）

---

## 4. 券商/行情來源（Tier-2：即時行情主力，但不取代官方）

> 你已指定：**以 API 為主**。券商/報價源在工程上通常提供即時性，但 TAITS 的「可回放權威」仍以快照管理。

### 4.1 即時行情（Real-time Quotes）
- 用途：盤中即時判斷、風控、追蹤
- 要求：
  - 必須寫入 Snapshot（哪個時間點看到的價格/量）
  - 必須有延遲監測（latency monitor）
- 風險：
  - 斷線、延遲、異常跳價 → 必須觸發降級（Observe-only/R10）

### 4.2 委託/成交回報（Order/Trade Reports）
- 這部分屬實作層（13+），但資料仍需進 Audit Store
- TAITS 母體要求：
  - 每次送單前的 evidence bundle 必須被保存
  - 每次成交回報必須可回放與對帳

---

## 5. 新聞 / 社群 / 情緒（Tier-2/3：多源交叉驗證，禁止單源真理）

> 你已明確要求：「消息面不能消失」，且「不懂不能不碰，要先解釋由你決定」。

### 5.1 消息面來源分級（建議）
- Tier-2（較可靠）：主流媒體、官方新聞稿、法說會文字稿
- Tier-3（可用但需降權）：論壇、社群、KOL、短影音

### 5.2 TAITS 使用規則
- 不直接當作「買賣依據」
- 只能作為：
  - Event Flag（事件旗標）
  - Narrative Evidence（題材/敘事證據）
  - Risk Flag（假消息/過熱風險）
- 必須附：
  - source
  - timestamp
  - confidence
  - cross-check（是否有第二來源印證）

---

## 6. 替代數據（Alternative Data：可選但需合規與回放）

可用於「題材輪動/供應鏈/產業景氣」的先行訊號，但必須：
- 有明確授權/可用性
- 可定期取得
- 可回放（同時間能重建）

---

## 7. 觀察型衍生品與信用槓桿（必納入，但不得下單）

### 7.1 期貨（Futures）— Observe-only
- 功能定位：
  - Market Regime Determination（市場狀態）
  - Cross-Market Filter（跨市場濾網）
  - Weight Adjustment（權重調整）
- 例：
  - 指數期貨趨勢/波動
  - 期現價差（Basis）
  - 外資避險/部位變化（若可得）

### 7.2 選擇權（Options）— Observe-only
- 功能定位：
  - 壓力/支撐帶（OI Wall）
  - Gamma/Volatility 風險
  - 結算週釘住（Pinning）風險
- 主要用途：提高出場優先權、限制追價策略

### 7.3 融資融券（Margin / Short）— Observe-only
- 功能定位：
  - 槓桿風險溫度計（過熱/踩踏）
  - 籌碼脆弱度判斷
- 使用方式：只作為風險與 regime 證據，不能當作唯一做多/做空理由

---

## 8. Data Quality（資料品質）與降級策略（必做）

### 8.1 必備 Data Quality 欄位
- completeness：完整性（缺哪些欄位/標的）
- timeliness：即時性（延遲秒數/分鐘）
- anomaly_flags：異常旗標（跳價、量暴衝、資料回補）
- source_health：來源健康狀態（UP/DOWN/DEGRADED）

### 8.2 降級規則（摘要）
- 關鍵來源 DOWN：Regime → R10 或置信度降權
- 即時行情延遲：禁止追價、禁止短線高頻策略
- 事件衝擊：強制風控模式（SOFT_BLOCK/HARD_BLOCK）

---

## 9. Snapshot 與可回放（可審計的核心）

TAITS 每一次決策必須保存：
- snapshot_id
- 原始來源版本（source + endpoint + query + timestamp）
- 標準化後資料（Normalized）
- FeatureVector
- RegimeResult
- GovernanceDecision
- RiskDecision
- 最終建議（與是否允許送單）

> 沒有 Snapshot 的系統，不能稱為 TAITS。

---

## 10. 最終結論（不偷工的承諾）

TAITS 的資料層不是「列一堆網站」而已，而是：
- 有分級（官方優先）
- 有備援（主/備）
- 有品質（延遲/缺失/異常）
- 有降級（R10/Observe-only）
- 有回放（snapshot）

本文件後續如需擴增，可新增附錄：02A（官方端點全集）、02B（新聞社群清單）、02C（宏觀與替代數據清單）。
