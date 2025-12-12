# TAITS_UI_Spec.md
# TAITS — 使用者介面與操作規範白皮書（Master UI Specification）

版本：Master / Full  
文件角色：**操作防呆與可視風控規範**  
對應文件：
- TAITS_MASTER_ARCHITECTURE.md
- TAITS_Risk_and_Compliance.md

---

## 0. 文件定位（必讀）

本文件定義 **TAITS 的 UI 與操作規範**，目的不是美觀，而是：

- 防止誤操作  
- 防止錯誤解讀  
- 防止越權行為  
- 防止忽略風險  

> **UI 是風控的一部分，而不是外觀層。**

---

## 1. 使用者角色與權限（RBAC）

### 1.1 角色定義

| 角色 | 權限 |
|---|---|
| Viewer | 僅查看報告 |
| Analyst | 研究 / 回測 |
| Operator | Paper / Live 操作 |
| Admin | 系統設定 |

❌ **任何角色不得繞過 Risk & Compliance**

---

## 2. 系統主畫面固定區塊

### 2.1 Header（不可隱藏）

必須顯示：

- 當前模式（Research / Backtest / Paper / Live）
- 市場 Regime
- 風控狀態（Active / Blocked）
- 系統時間（TWSE）

---

### 2.2 左側導覽（固定）

```

Dashboard
Market Overview
Strategies
Agents
Regime
Risk Status
Backtest
Trading
Reports
System Log

```

---

## 3. 顏色與語意規範（不可混用）

### 3.1 漲跌顏色（台股慣例）

- 上漲：紅
- 下跌：綠
- 中立：灰

---

### 3.2 狀態顏色（全系統一致）

| 狀態 | 顏色 |
|---|---|
| BULL | 紅 |
| BEAR | 綠 |
| NEUTRAL | 灰 |
| WARNING | 橘 |
| BLOCKED | 深紅 |

---

## 4. 策略顯示規則

- 顯示 Strategy Name
- 顯示 Signal / Confidence
- 顯示 Reason（文字）

❌ **禁止一鍵跟單**

---

## 5. Agent 顯示規則

- 各 Agent 獨立顯示
- 可展開查看判斷依據
- 不得合併為單一分數

---

## 6. Regime 與 Fusion 顯示（高優先）

### 6.1 Regime 區塊

- 當前 Regime
- Regime 信心值
- Regime 來源（期貨 / 波動 / 結構）

---

### 6.2 Fusion 結果

- Final Bias
- Final Confidence
- 是否被 Risk 覆蓋
- 覆蓋原因

---

## 7. 風控狀態顯示（常駐）

- 是否允許交易
- 阻擋原因
- 解除條件

⚠️ Risk = Blocked → 所有交易按鈕失效

---

## 8. 下單防呆機制（強制）

任何實盤操作必須：

1. 顯示策略來源  
2. 顯示風控檢查結果  
3. 顯示資金影響  
4. 二次確認  

---

## 9. 模式硬隔離

- Research / Backtest / Paper / Live
- 不得共用狀態
- Live 模式需明顯警示

---

## 10. 報告與稽核連結

UI 必須能追溯：

- 策略
- Agent
- Regime
- Fusion
- Risk

---

## 11. 錯誤與警示處理

- 警告不可靜默
- 重大錯誤必須顯示
- 系統異常 → 自動降級

---

## 12. 一句話總結

> **在 TAITS 中：  
> UI 的責任不是好看，  
> 而是讓人不會做錯事。**

---
