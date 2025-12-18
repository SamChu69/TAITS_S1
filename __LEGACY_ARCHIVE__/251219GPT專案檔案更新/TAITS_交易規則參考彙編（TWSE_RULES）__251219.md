# TAITS_交易規則參考彙編（TWSE_RULES）
## TWSE / TPEx Trading Rules Reference (Governance-Aligned)

版本日期：2025-12-19  
適用狀態：S0 / S1（Freeze 前後）  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217

---

## 前言｜Why Rules Are References, Not Assumptions

在 TAITS 中，交易規則是**即時合規觸發的來源**，  
而不是被寫死的常數。

> **制度會變，  
> 合規必須即時反應。**

因此，本文件的角色是：
- 彙整規則「類型」
- 定義合規「觸發點」
- 規範「變動時的系統反應」

📌 **本文件不寫死數值、不替代官方公告。**

---

## 第 1 章｜文件位階、適用範圍與限制

### 1.1 文件位階
- 治理等級：**C（制度參考／即時合規）**
- 上位文件：
  - `RISK_COMPLIANCE`
  - `EXECUTION_CONTROL`
  - `DATA_SOURCES`
- 受限規則：
  - 不得新增交易權力
  - 不得放寬任何合規門檻

### 1.2 適用市場
- TWSE（臺灣證券交易所）
- TPEx（櫃買中心）

📌 **期貨、選擇權不在本文件範圍。**

---

## 第 2 章｜Hard Gates（硬性門檻）

### 2.1 即時合規觸發（AI_GOV §6, §10）
- 任何規則觸發：
  - **立即通知 Risk & Compliance**
  - 可能導致：
    - Strategy 禁用
    - Execution 阻斷

### 2.2 禁止寫死制度（AI_GOV §10）
- 禁止：
  - 將制度參數硬編碼
  - 假設規則永不變動

📌 **規則只作參考，判斷權在治理模組。**

---

## 第 3 章｜交易時間與撮合規則（類型化）

### 3.1 交易時段（Type）
- 集合競價
- 連續交易
- 收盤集合

**治理用途：**
- 驗證 Execution 是否在合法時段
- 風控對盤中／盤後行為的即時否決

### 3.2 撮合方式（Type）
- 價格優先
- 時間優先

📌 **不得據此推論成交機率或策略優勢。**

---

## 第 4 章｜價格限制與漲跌幅（類型化）

### 4.1 漲跌幅限制（Type）
- 一般股票
- 特殊處置股票

**合規觸發：**
- 價格接近限制時：
  - 提高風險等級
  - 可能暫停 Execution

### 4.2 異常價格（Type）
- 跳空
- 連續無成交

📌 **異常 ≠ 可交易機會。**

---

## 第 5 章｜交易單位、下單限制與類型

### 5.1 交易單位
- 整股
- 零股

**治理用途：**
- 驗證下單單位合法性
- 與 Scope Freeze 對齊（零股優先）

### 5.2 訂單類型（Type）
- 限價
- 市價（如適用）

📌 **Execution 不得因策略需求選擇非法訂單類型。**

---

## 第 6 章｜異常交易與處置（Type）

### 6.1 異常交易型態
- 量價異常
- 頻繁撤單

### 6.2 處置措施（Reference）
- 警示
- 暫停交易
- 處置股

**合規反應：**
- 立即通報 Risk
- 禁用相關 Strategy

---

## 第 7 章｜Rule Trigger Map（審計輸出）

### 7.1 最小 Trigger 欄位
- `rule_type`
- `market`
- `trigger_time`
- `affected_assets`
- `system_action`
- `risk_level`
- `audit_ref`

### 7.2 與其他文件的連動
- `RISK_COMPLIANCE`：否決依據
- `EXECUTION_CONTROL`：阻斷執行
- `VERSION_AUDIT`：記錄制度變更影響

---

## 第 8 章｜規則變動的處理方式

### 8.1 官方公告優先
- 任何制度更新：
  - 以官方公告為準
  - 本文件僅更新「類型／觸發邏輯」

### 8.2 變動處理流程
1. 官方公告出現
2. DATA_SOURCES 更新
3. Risk 評估影響
4. 必要時 Freeze / Disable

📌 **不得預測或提前套用未生效規則。**

---

## 第 9 章｜禁止事項（黑名單）

- 以規則為由放寬風控
- 將處置視為交易機會
- 規則缺失時自行假設
- 用規則替代 Evidence

---

## 結語｜Closing

交易規則的價值，不在於背誦，  
而在於**即時尊重它的存在**。

> **合規不是限制策略，  
> 而是確保系統能活得夠久。**

## 附錄 A｜官方交易規則與制度權威來源（Authority References）

本附錄僅列出 **官方、第一手、具法律效力或準法律效力** 之資料來源。  
所有即時合規判斷、制度變更確認，**必須以以下來源為準**。

📌 本附錄用途：
- 作為 **制度查核與人工審計的權威依據**
- 作為 **DATA_SOURCES → RISK_COMPLIANCE** 的來源參考
- **不得**作為硬編碼、爬蟲依賴或策略假設

---

### A.1 臺灣證券交易所（TWSE）

**官方網站（主站）**  
- https://www.twse.com.tw

**交易制度與規章專區**  
- https://www.twse.com.tw/zh/page/trading/rules.html  
（交易規則、撮合制度、漲跌幅、處置措施）

**市場公告（即時制度異動）**  
- https://www.twse.com.tw/zh/news/newsList

**交易資訊與市場說明**  
- https://www.twse.com.tw/zh/trading/tradingInfo

📌 治理定位：  
- **制度定義權威**
- 規則變動的「生效來源」

---

### A.2 櫃買中心（TPEx）

**官方網站（主站）**  
- https://www.tpex.org.tw

**交易制度與業務規章**  
- https://www.tpex.org.tw/web/regular_emerging/regulation.php  
（櫃買市場交易規則、處置股制度）

**公告與最新消息**  
- https://www.tpex.org.tw/web/bulletin/announcement.php

📌 治理定位：  
- 櫃買市場（上櫃、興櫃）之 **制度裁定來源**

---

### A.3 金融監督管理委員會（FSC）

**官方網站**  
- https://www.fsc.gov.tw

**法規查詢系統**  
- https://law.fsc.gov.tw  
（證券交易法、相關子法）

📌 治理定位：  
- **最高監理機關**
- 當交易所規則與法規出現衝突時，以 FSC 法規為最終依據

---

### A.4 法規資料庫（交叉驗證）

**全國法規資料庫（法務部）**  
- https://law.moj.gov.tw

📌 治理定位：  
- 法律條文的最終版本查核
- 用於審計與爭議處理，不用於即時交易邏輯

---

## 附錄 B｜TAITS 對官方來源的使用原則（Hard Rules）

1. **官方公告優先於任何內部文件**
2. 官方網址僅用於：
   - 查核
   - 人工審計
   - 治理對照
3. 禁止行為：
   - 直接爬取網頁作為即時交易依據
   - 將網址內容視為固定不變
   - 用摘要取代原文規章
4. 制度變動處理：
   - DATA_SOURCES 更新標記
   - RISK_COMPLIANCE 重新評估
   - 必要時啟動 Freeze

📌 **網址是權威來源，不是系統參數。**

（TWSE_RULES 完）
