# TAITS_交易執行與控制規範（EXECUTION_CONTROL）
## Taiwan Alpha Intelligence Trading System
### EXECUTION & CONTROL · HUMAN-IN-THE-LOOP
### 版本日期：2025-12-19
### 治理等級：E（執行層，受 RISK_COMPLIANCE 最高否決）
### 狀態：ACTIVE（同版融合更新）
### 覆寫權限：僅人類主權

---

## 0. 文件法律地位（Execution-under-Governance）

本文件定義 **TAITS 唯一合法的交易執行與控制方式**。

在 TAITS 中：

- **Execution 永遠不是自動的**
- **Execution 永遠承接人類明確指令**
- **Execution 永遠受制於 RISK_COMPLIANCE 的即時否決**

> **沒有被治理允許的執行，  
在 TAITS 中視為非法行為。**

---

## 1. Execution 在 Canonical Flow 中的位置

- 對應層級：**L11｜Execution & Control**
- 前置條件（缺一不可）：
  1. Evidence Bundle 完整
  2. Regime 通過
  3. Risk & Compliance Pass
  4. Governance Gate Allow
  5. **人類於 L10 明確確認**

---

## 2. 人類指令的定義（Human Instruction）

### 2.1 合法人類指令必須包含

- 標的（Symbol）
- 交易方向（Buy / Sell）
- 數量
- 委託類型（限價 / 市價等）
- 有效時間
- 下單理由（Evidence Reference）

📌 缺一 → **Execution 不得啟動**

---

### 2.2 不合法的人類指令

- 「幫我看情況下單」
- 「如果漲就追」
- 「交給 AI 決定」

以上語句：
- 在治理上 **視為未下指令**

---

## 3. 執行前的強制檢查（Pre-Execution Checklist）

Execution 啟動前，必須再次確認：

- [ ] Risk & Compliance 狀態仍為 Pass  
- [ ] Regime 未變化為不相容  
- [ ] 標的未進入處置 / 停牌  
- [ ] Tick Size / 委託方式合法  
- [ ] 人類指令未過期  

📌 任一項失效 → **立即中止執行**

---

## 4. 執行過程控制（In-Execution Control）

### 4.1 即時監控項目

- 委託回報
- 成交狀態
- 價格異常
- 系統延遲

### 4.2 即時中止條件（Kill Switch）

以下任一發生，必須即時中止：

- Risk & Compliance 重新否決
- 系統異常
- 人類主動中止
- API 回應異常

---

## 5. Kill Switch 規範（不可妥協）

- Kill Switch：
  - 必須為即時
  - 不得等待成交
- Kill Switch 來源：
  - RISK_COMPLIANCE
  - 人類主權
  - 系統完整性檢測

📌 **Kill Switch 不需理由，立即生效。**

---

## 6. 執行後紀錄與審計（Post-Execution）

### 6.1 必須紀錄內容

- 人類指令原文
- Evidence Reference
- 下單時間
- 成交結果
- 中止原因（若有）

### 6.2 審計要求

- 所有紀錄：
  - 必須可回放
  - 不得覆寫
  - 不得刪除

---

## 7. 禁止行為（Hard No）

- 無人值守自動交易
- AI 代替人類確認
- 自動補單 / 追單
- 事後補寫理由

---

## 8. 與其他文件的治理關係

- 受制於：
  - MASTER_ARCH
  - MASTER_CANON
  - RISK_COMPLIANCE
- 下位於：
  - UI_SPEC
- 互補於：
  - DEPLOY_OPS
  - TWSE_RULES

---

## 9. 變更與演進限制

- 僅允許：
  - 補充執行控制機制
  - 強化審計欄位
- 不允許：
  - 降低人類介入要求
  - 引入自動下單例外

---

## 10. EXECUTION_CONTROL 最終宣告

> **在 TAITS 中，  
執行不是速度問題，  
而是責任問題。**

---

（End of EXECUTION_CONTROL）
