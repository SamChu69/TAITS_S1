# TAITS_風控與合規（RISK_COMPLIANCE）__251218.md

> doc_key：RISK_COMPLIANCE  
> 治理等級：A+（最高否決權｜Veto Power）  
> 適用範圍：TAITS 全系統（所有策略、所有流程、所有環境）  
> 狀態：ACTIVE（Only-Add｜只能新增不可縮水）  
> 最後更新：2025-12-18（Asia/Taipei）

---

## 0. 文件定位（Risk Is Authority）

本文件定義 **TAITS（Taiwan Alpha Intelligence Trading System）之風控與合規最高治理規範**。  

📌 在 TAITS 中：  
**Risk / Compliance 不是輔助模組，而是具備「最高否決權」的權力中心。**

任何策略、流程、AI 建議、執行行為，  
**只要被本文件否決，即刻失效，不得上訴、不得繞過。**

---

## 1. 風控與合規的最高原則（不可違反）

### 1.1 最高否決權（Veto Power）

- Risk / Compliance 可在任何時間點：
  - 否決任何策略輸出
  - 中止任何執行流程
  - 觸發 Kill Switch
- 否決：
  - **不需要即時對外解釋**
  - 但 **必須留下完整審計紀錄**

---

### 1.2 風控優先順序

在所有決策衝突中，優先順序固定為：

Risk / Compliance
＞ Regime
＞ Strategy
＞ Execution
＞ AI / Agent

yaml
複製程式碼

---

### 1.3 官方規則優先（Official First）

- 任何與：
  - TWSE / TPEX 交易制度
  - 券商（富邦 TradeAPI）限制
- 發生衝突時：
  - **以官方為準**
  - TAITS 文件必須更新為「引用說明」

---

## 2. 風控分層模型（Risk Layering）

TAITS 的風控採 **多層 Gate** 設計：

1. **Regime Gate**（市場狀態）
2. **Strategy Gate**（策略適配）
3. **Liquidity Gate**（流動性，零股重點）
4. **Position Gate**（部位與資金）
5. **Execution Gate**（執行限制）
6. **Human Gate**（人類介入）

📌 **任一 Gate 失敗，流程立即停止。**

---

## 3. Regime 風控（Regime Gate）

### 3.1 Regime 必須已識別

- 未識別 Regime：
  - 禁止交易
- Regime 不明確：
  - 僅允許「觀察、不做」

---

### 3.2 Regime 不相容否決

- 策略標註 Regime ≠ 當前 Regime：
  - **立即否決**

---

## 4. 策略風控（Strategy Gate）

### 4.1 策略狀態檢查

策略必須處於：

- Enabled（已啟用）
- 非 Draft / Paused / Retired

---

### 4.2 策略生命週期合規

- 未完成回測 / 模擬：
  - 禁止進入 Execution
- 新策略：
  - 必須通過觀察期

---

## 5. 流動性與零股專用風控（Liquidity Gate）

### 5.1 零股核心限制（強制）

- 最低成交量門檻
- 允許不成交
- 禁止追價

📌 **零股策略在流動性不足時必須停用，而不是強行交易。**

---

### 5.2 滑價與價差控制

- 預估滑價超過門檻：
  - 否決
- 價差異常擴大：
  - 觸發保護

---

## 6. 部位與資金風控（Position Gate）

### 6.1 資金使用原則

- 單筆交易風險上限
- 單一標的曝險上限
- 總曝險比例限制

---

### 6.2 零股特殊考量

- 零股：
  - 分批進出
  - 嚴禁一次性重倉

---

## 7. 執行風控（Execution Gate）

### 7.1 API 與系統限制

- 僅允許使用：
  - 核准 API（富邦 TradeAPI）
- API 異常：
  - 禁止交易
  - 進入保護模式

---

### 7.2 交易時間與制度限制

- 非交易時段：
  - 禁止下單
- 制度限制（漲跌幅、暫停）：
  - 必須遵守官方規則

---

## 8. 人類介入風控（Human Gate）

### 8.1 必須介入的情境

- 新策略首次啟用
- 異常市場狀態
- 重大事件期
- 系統異常後首次交易

---

### 8.2 人類權限

- 確認
- 延後
- 否決（最高）

📌 人類否決同樣需留下紀錄。

---

## 9. Kill Switch（緊急停止）

### 9.1 觸發條件

- 系統錯誤
- 資料錯誤
- 連續異常交易
- 人類手動觸發

---

### 9.2 行為

- 立即停止所有 Execution
- 保留當下狀態
- 通知人類

---

## 10. 事後審計與回放

### 10.1 必留紀錄

- Regime 判斷
- 策略輸出
- 風控決策
- 執行結果

---

### 10.2 可回放要求

- 每一筆交易：
  - 必須能完整回放
  - 必須能被第三方理解

---

## 11. 不可接受的風控違規（Anti-Patterns）

- 無 Regime 即交易
- 繞過任何 Gate
- AI 自行調整風控參數
- 無 Log 的交易行為

---

## 12. 與其他文件的關係

- 高於：
  - STRATEGY_UNIVERSE
  - EXEC_CONTROL
- 受制於：
  - 官方制度（TWSE / 券商）

---

## 13. 演進與擴充原則（Only-Add）

- 可新增：
  - 新風控 Gate
  - 新保護機制
- 不可：
  - 移除否決權
  - 降低風控標準

---

## 14. 最終宣告

> **在 TAITS 中，  
> 任何不能被否決的交易，  
> 都是不被允許的交易。**

---

（End of RISK_COMPLIANCE）
