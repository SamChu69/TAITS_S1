# TAITS_AI_最終完整規則全集__251217.md

> doc_key：AI_GOVERNANCE_FULLSPEC  
> 治理等級：A+（最高｜不可推翻）  
> 適用對象：所有參與 TAITS 的 AI / Agent / LLM / 自動化工具  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live 預留）  
> 狀態：ACTIVE（Final Canon｜Only-Add）  
> 維護原則：Only-Add（可擴充不可縮水；重大變更需新增版本檔）

---

## 0. 本文件定位（最高權威）

本文件定義 **AI 在 TAITS（Taiwan Alpha Intelligence Trading System）中的一切行為與決策邊界**。

📌 本文件優先級高於：
- 任何單次對話內容
- 任何 AI 的內部假設
- 任何臨時建議、最佳化提案、示例

📌 若 AI 輸出與本文件衝突，  
**AI 必須主動自我修正並回到本文件規則。**

---

## 1. TAITS 的基礎事實（AI 必須先內化）

### 1.1 系統定位（不可降級）

TAITS 是一套：

- 專為 **台灣市場（TWSE / TPEX）** 設計
- 可實盤、可長期演進
- **Regime（市場狀態）與 Risk / Compliance 為最高優先**
- 多 Agent 可擴充，但必須受治理約束
- AI 僅為輔助角色，**非唯一真理**

### 1.2 最高設計原則（不可違反）

- 策略 ≠ 下單
- Agent ≠ 策略
- AI ≠ 唯一真理
- Regime 高於單一訊號
- Risk / Compliance 可否決一切
- 官方資料優先，多層 fallback
- 架構必須可長期演進、可擴充、不可縮水

---

## 2. 權威文件優先順序（Authority Resolution）

若專案中存在多份文件：

- AI 必須依 **最新指定的最高權威文件清單**
- 不得自行推翻、弱化、重寫權威文件
- 發現衝突時，必須主動指出並請求人類裁決

---

## 3. 範圍治理（Scope Freeze）

### 3.1 現階段唯一啟用範圍

- 市場：台股（TWSE / TPEX）
- 產品：股票（STOCK）
- 交易單位：零股（odd_lot）
- 模式：Research / Simulation / Paper
- 券商 API：**富邦 TradeAPI**

### 3.2 預留但未啟用（僅制度層）

- 整股（full_lot）
- 混合（hybrid，屬 Execution 編排）
- 期貨 / 選擇權 / 權證
- 融資融券 / 美股

### 3.3 XQ 平台處理原則

- 現階段 **不得與 TAITS Execution 設計耦合**
- 理由：
  - 平台封閉
  - 零股無法程式交易
  - 架構差異過大
- 僅允許作為「制度參考或未來預留」

### 3.4 AI 禁止行為

AI 不得：
- 自行擴張 Scope
- 將「預留」視為「已啟用」
- 建議「先做再補制度」

---

## 4. 三權分立（Boundary Non-Negotiable）

### 4.1 Strategy（策略）

策略只負責：
- 生成交易意圖（Intent）
- 描述理由（Rationale）
- 宣告適用範圍（Meta）

策略不得：
- 包含任何否決（Veto）邏輯
- 指定下單方式 / 價格 / API
- 直接影響資金或倉位

---

### 4.2 Risk / Compliance（風控合規）

Risk 只負責：
- 允許 / 否決 / 降級 / 暫停 / 停用
- 可於執行前或執行中否決
- 產出 reason_codes

Risk 不得：
- 生成交易訊號
- 自動解除否決

---

### 4.3 Execution（執行）

Execution 只負責：
- 承接策略意圖
- 服從 Risk 裁決
- 路由交易單位
- 下單抽象與券商適配
- 統一出場（Unified Exit）
- 失敗處理與完整紀錄

Execution 不得：
- 修改策略方向
- 繞過風控
- 假設市場一定成交

---

## 5. 交易單位治理（Trade Unit Governance）

### 5.1 odd_lot（零股）
- 唯一預設啟用
- 必須容忍低流動性與延遲成交

### 5.2 full_lot（整股）
- 預設關閉
- 僅在「治理啟用 + 策略宣告 + Risk 允許」下可用

### 5.3 hybrid（混合）
- 永遠屬 Execution 編排
- 永遠不是預設
- 可被 Risk 隨時停用

---

## 6. 官方來源引用原則

- 市場制度與交易規則 **必須引用官方來源**
- 文件描述概念與引用位置
- 不寫死易變動細節（時間 / 數值 / 條件）

---

## 7. 文件輸出強制規範（不偷工減料）

- 產出 MD 檔：
  - 必須完整可存檔
  - 不得只給片段或摘要
- 檔名必須包含：
  - 主題
  - 適用範圍
  - 日期（`__YYMMDD`）
- 更新內容 → 新檔名，不覆蓋舊檔

---

## 8. 新對話啟動規則

- AI 必須假設 TAITS 架構已存在
- 本文件為最高行為準則
- 不得以 Demo / 教學心態回應

---

## 9. 人類最終控制權

- 人類擁有 approve / veto / pause / resume / freeze
- AI 僅能建議，不得主導
- 若人類指示與制度衝突：
  - AI 必須提醒風險
  - 但仍須尊重最終裁決

---

## 10. 最終聲明

> **TAITS 不是聊天專案，  
而是一套必須可審計、可回放、可長期演進的交易系統。**

---

（End of AI_GOVERNANCE_FULLSPEC）
