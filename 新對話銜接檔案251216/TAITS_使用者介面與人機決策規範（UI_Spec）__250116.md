# TAITS_使用者介面與人機決策規範（UI_Spec）__250116.md

> doc_key：UI_SPEC  
> 治理等級：C（人機介面與決策呈現｜受制於 Governance / Risk）  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
> 版本狀態：ACTIVE（Only-Add，可擴充不可縮水）

---

## 0. 文件定位（UI as Decision Boundary）

本文件定義 **TAITS 的使用者介面（UI）與人機互動之唯一規範**。  
在 TAITS 中，UI 的角色不是美觀，而是：

> **人類主權的實體化邊界（Decision Boundary）**

📌 UI 是 **唯一允許人類做出最終決策的層級（L10）**，  
📌 任何未經 UI 呈現與確認的決策，**在治理上視為不存在**。

---

## 1. UI 的核心治理原則（不可違反）

### 1.1 UI 是「呈現層」，不是「推論層」

- UI **不得**：
  - 產生策略
  - 推論買賣方向
  - 自行加權或排序證據
- UI **只能**：
  - 呈現系統已產出的結果
  - 揭露不確定性與風險

---

### 1.2 人類主權不可被隱藏

- 任何可執行行為：
  - 必須有明確的人類確認動作
- 不得：
  - 預設勾選
  - 隱性自動執行

---

### 1.3 風險揭露優先於績效呈現

- UI 排序原則：
  1. 風險與限制
  2. Regime 與不確定性
  3. 證據摘要
  4. 策略建議（若存在）
  5. 績效或歷史參考（最後）

---

## 2. UI 分層架構（UI Layering）

TAITS UI 依功能分為六大區塊：

1. 系統狀態總覽（System Overview）
2. 市場與 Regime 呈現
3. 證據與分析呈現
4. 策略建議區（非指令）
5. 風控與合規提示
6. 人類決策與確認區

---

## 3. 系統狀態總覽（System Overview）

**必須顯示**
- 當前環境等級（E1–E4）
- 系統模式（Simulation / Paper / Live）
- 最近一次 Snapshot 時間
- 風控狀態（Pass / Reject）

📌 若狀態異常：
- UI 必須顯著警示
- 禁止進入決策區

---

## 4. 市場與 Regime 呈現

**必須呈現**
- 當前 Market Regime Label
- Regime 信心度（Confidence）
- Regime 變動歷史

**禁止**
- 將 Regime 呈現為預測
- 用顏色誤導趨勢判斷

---

## 5. 證據與分析呈現（Evidence Visualization）

### 5.1 Evidence Bundle 呈現原則

- 證據需分群顯示：
  - 技術
  - 結構
  - 成交 / 流動性
  - 基本面（若有）
- 必須標註：
  - 一致性
  - 衝突點
  - 缺失證據

---

### 5.2 不確定性揭露（Mandatory）

- 證據不足
- 證據衝突
- Regime 低信心

📌 不確定性不得被隱藏或弱化。

---

## 6. 策略建議呈現（Non-Directive）

**允許呈現**
- 策略名稱
- 適用 Regime
- 使用假設
- 不適用情境

**禁止呈現**
- 買 / 賣指令
- 進出場點位
- 獲利保證語句

---

## 7. 風控與合規提示（Hard Constraints）

**必須顯示**
- 風控狀態（RISK_COMPLIANCE）
- 合規限制（TWSE_RULES）
- 任何否決原因（若存在）

📌 若為 Reject：
- UI 必須鎖定執行區
- 不得提供繞過選項

---

## 8. 人類決策與確認區（Decision Gate）

### 8.1 決策行為規範

- 人類可做：
  - 接受建議（非強制）
  - 拒絕建議
  - 選擇不行動
- 每一決策：
  - 必須產生 Decision ID
  - 必須被記錄

---

### 8.2 高風險二次確認（Mandatory）

以下情況必須二次確認：

- Live Execution
- Regime 低信心
- 風險接近上限

---

## 9. UI 與 Execution 的邊界

- UI **不直接下單**
- UI 僅輸出：
  - Human Decision
  - 決策參數
- 實際下單：
  - 僅能由 EXECUTION_CONTROL 執行

---

## 10. UI 日誌與審計

UI 必須記錄：

- 使用者操作行為
- 決策內容
- 確認時間
- 環境與模式

📌 UI Log 屬於審計資料，不可刪除。

---

## 11. 與其他文件的關係

- 受制於：
  - MASTER_ARCH
  - MASTER_CANON
  - RISK_COMPLIANCE
- 被引用於：
  - EXECUTION_CONTROL
  - Deployment_and_Operation

---

## 12. 擴充與設計原則

- 可新增視覺模組
- 可改善可讀性
- **不可弱化風控與否決呈現**

---

## 13. 最終 UI 治理宣告

> **TAITS 的 UI 不是為了「讓人更想交易」，  
而是為了確保：  
人類是在充分理解風險後，才選擇是否行動。**

---

（End of UI_SPEC）
