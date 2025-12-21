# TAITS_UI_Spec.md
# TAITS — 使用者介面與操作規範白皮書（Master UI Specification）

版本：Master / Full  
適用範圍：Research / Backtest / Paper / Live  
對應文件：
- TAITS_Full_System_Architecture.md
- TAITS_Risk_and_Compliance.md

---

## 0. 文件定位（必讀）

本文件定義 **TAITS 的 UI 與操作規範**，目的不是美觀，而是：

- 防止誤操作
- 防止錯誤解讀
- 防止越權行為
- 防止忽略風險

在 TAITS 中：
> **UI 是風控的一部分，而不是外觀層。**

---

## 1. 使用者角色與權限（RBAC）

### 1.1 角色定義

| 角色 | 權限 |
|---|---|
| Viewer | 只讀（查看報告、結果） |
| Analyst | 研究 / 回測 / 策略分析 |
| Operator | Paper / Live 操作 |
| Admin | 系統設定 / 權限管理 |

❌ 任何角色 **不得繞過 Risk & Compliance**

---

## 2. 系統主畫面分區（固定結構）

### 2.1 全域資訊區（Header）

**必須顯示**：
- 當前模式：Research / Backtest / Paper / Live
- 市場狀態（Regime）
- 風控狀態（Active / Blocked）
- 系統時間（TWSE）

---

### 2.2 左側導航（不可隱藏）

```

* Dashboard
* Market Overview
* Strategies
* Agents
* Regime
* Risk Status
* Backtest
* Trading
* Reports
* System Log

```

---

## 3. 顏色與語意規範（不可更改語意）

### 3.1 漲跌顏色（亞洲市場慣例）

- 上漲：紅色
- 下跌：綠色
- 中立 / 無變化：灰色

📌 **顏色不可與語意衝突**

---

### 3.2 狀態顏色（全系統一致）

| 狀態 | 顏色 |
|---|---|
| BULL | 紅 |
| BEAR | 綠 |
| NEUTRAL | 灰 |
| WARNING | 橘 |
| BLOCKED | 黑 / 深紅 |

---

## 4. 策略與 Agent 顯示規則

### 4.1 策略顯示（不可直接下單）

每一策略必須顯示：

- Strategy Name
- Signal（BUY / SELL / HOLD）
- Confidence
- Reason（文字）

❌ **禁止「一鍵跟單」**

---

### 4.2 Agent 顯示（分析層）

- 各 Agent 必須獨立顯示
- 不得合併為單一分數
- 必須能展開查看判斷依據

---

## 5. Regime 與 Fusion 顯示（關鍵）

### 5.1 Regime 區塊（高優先）

- 當前 Regime
- Regime 可信度
- Regime 來源（期貨 / 波動 / 結構）

📌 **Regime 需固定顯示於主畫面**

---

### 5.2 Fusion 結果

- Final Bias
- Final Confidence
- 是否被 Risk 覆蓋（Yes / No）
- 覆蓋原因（若有）

---

## 6. 風控顯示（不可忽略）

### 6.1 風控狀態 Panel（常駐）

- 是否允許交易
- 阻擋原因
- 解除條件

❌ 若 Risk = Blocked：
- 所有交易按鈕必須失效
- 顯示原因（不可隱藏）

---

## 7. 下單與操作防呆（強制）

### 7.1 下單前確認（多層）

任何實盤動作必須：

1. 顯示策略來源
2. 顯示風控檢查結果
3. 顯示資金影響
4. 二次確認

---

### 7.2 模式區隔（硬性）

- Research / Backtest / Paper / Live
- 不得混用
- Live 模式需明顯警示

---

## 8. 報告與回溯（Audit-friendly）

### 8.1 報告類型

- TXT（快速查看）
- JSON（系統回溯）
- Markdown（人類閱讀）

---

### 8.2 可追溯性

UI 必須能連結：

- 策略輸出
- Agent 判斷
- Regime
- Fusion
- Risk 決策

---

## 9. 錯誤、警示與異常處理

- 警告不可靜默
- 重大錯誤必須顯示
- 系統異常 → 自動降級或暫停

---

## 10. 本文件的地位（重要）

- 本文件優先於 UI 實作細節
- 若 UI 設計與本文件衝突：
  👉 **以本文件為準**
- 本文件不得被 UI 美術需求推翻

---

## 11. 一句話總結

> **在 TAITS 中：  
> UI 的責任不是「好看」，  
> 而是「讓人不會做錯事」。**

---
