📘 TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219
PART 1｜文件定位 × 最高否決權的法律地位 × 治理原則

# TAITS_風險與合規最高否決權（RISK_COMPLIANCE）
## Risk & Compliance Supreme Veto Specification

---

## 風控前言（Why Risk Must Say No）

在多數交易系統中，  
風控被視為「限制獲利的阻礙」。

在 TAITS 中，  
**風控是系統得以長期存活的唯一理由**。

本文件的存在目的，不是幫助系統「找到可以交易的理由」，  
而是確保系統**永遠具備拒絕錯誤交易的能力**。

---

## 第 1 章｜RISK_COMPLIANCE 的治理位階與不可動搖性

### 1.1 文件位階
- 治理等級：**A（最高否決權）**
- 上位文件：
  - `MASTER_ARCH`
  - `MASTER_CANON`
- 平行約束：
  - `ARCH_FLOW`
- 下位文件：
  - `EXECUTION_CONTROL`
  - `UI_SPEC`

📌 **任何文件不得削弱本文件所定義之否決權。**

---

### 1.2 最高否決權（Supreme Veto）的定義
最高否決權，指：

> **在任何時間點、任何流程層級，  
> 只要風險或合規條件不成立，  
> 即可立即中止流程，且不接受協商、辯護或事後合理化。**

---

### 1.3 否決權的不可被覆寫性
- 否決一旦成立：
  - ❌ Strategy 不得反駁
  - ❌ AI 不得合理化
  - ❌ Execution 不得繞行
- 唯一可終止否決的方式：
  - **條件本身消失**
  - **重新走完整 Canonical Flow**

📌 **不存在「強行放行」這種合法行為。**

---

### 1.4 Risk 與 Compliance 的區分與合併
在 TAITS 中：
- **Risk（風險）**：
  - 關注最壞情境
  - 關注資金、生存、系統性風險
- **Compliance（合規）**：
  - 關注法規、交易所規則、制度邊界

二者在制度上：
- **合併為同一否決層**
- 任一成立 → 否決生效

---

## 第 2 章｜RISK_COMPLIANCE 的核心治理原則

### 2.1 Worst-case First 原則
RISK_COMPLIANCE **永遠以最壞情境為判斷基準**：

- 不假設正常成交
- 不假設流動性存在
- 不假設系統穩定
- 不假設人類理性

📌 **只要最壞情境不可承受 → 必須否決。**

---

### 2.2 Binary Judgment 原則
RISK_COMPLIANCE 的輸出只有三種狀態：

- **Pass**：可進入後續流程  
- **Reject**：立即否決  
- **Degrade**：降級（如 Observe-only）

📌 不存在「勉強可以」「小心一點」這種模糊狀態。

---

### 2.3 獨立性原則
RISK_COMPLIANCE：
- 不參與策略設計
- 不追求績效
- 不評估勝率
- 不受人類情緒影響

📌 **風控必須能在所有人都想交易時，堅定地說不。**

---

### 2.4 即時性原則
- 否決可以發生在：
  - 流程開始前
  - 流程進行中
  - Execution 執行中
- 不需等待：
  - 批次檢查
  - 人類確認

📌 **風控的遲疑，本身就是風險。**

---

## 第 3 章｜RISK_COMPLIANCE 與 Canonical Flow 的關係

### 3.1 在 Canonical Flow 中的位置
- 主體層級：**L7**
- 影響範圍：
  - L8 Strategy
  - L9 Governance Gate
  - L10 Human Decision
  - L11 Execution

📌 **L7 的否決，會向前與向後同時生效。**

---

### 3.2 與 Regime（L6）的關係
- Regime：
  - 判定「不適用」
- Risk / Compliance：
  - 判定「不可承受」

📌 Regime 是篩選器，  
📌 Risk 是保險絲。

---

### 3.3 與 Governance Gate（L9）的關係
- Governance Gate：
  - 檢查流程完整性
- Risk / Compliance：
  - 判定是否允許任何後續行為

📌 **流程完整但風險不可承受 → 仍然否決。**

---

### 3.4 與 Human Decision（L10）的關係
- 人類：
  - 不得覆寫否決
- 人類可以：
  - 在 Pass 或 Degrade 情況下選擇不交易

📌 **人類主權高於策略，但不高於風險。**

---

（RISK_COMPLIANCE · PART 1 結束）

PART 2｜否決來源全集 × Reason Codes × Degrade / Observe-only

## 第 4 章｜法定否決來源全集（Risk & Compliance Sources）

本章列舉 **RISK_COMPLIANCE 可合法行使最高否決權的完整來源**。  
凡未列於本章者，**不得作為否決理由**。

---

### 4.1 法規與交易所規則風險（Regulatory Risk）

否決條件包括但不限於：
- 交易所交易規則限制（如漲跌幅、撮合限制）
- 商品或交易單位不符當前法規
- 委託方式違反券商或交易所規定
- 異常交易行為可能觸發監管關注

📌 **任何法規不確定性 → 預設否決。**

---

### 4.2 市場結構與流動性風險（Market & Liquidity Risk）

否決條件包括：
- 流動性顯著不足（如：零股深度不足）
- 價差異常擴大
- 成交斷層或撮合不連續
- 交易時段結構性異常（開盤/收盤極端）

📌 **假設無法成交，是風控的基本假設。**

---

### 4.3 資料完整性與品質風險（Data Integrity Risk）

否決條件包括：
- Raw Data 缺失或延遲
- Snapshot 不完整或不可回放
- Evidence Completeness Score 低於門檻
- 關鍵 Feature 缺失或方法論未定義

📌 **資料不足 ≠ 保守交易，而是直接否決。**

---

### 4.4 Regime 不穩定或不適用風險（Regime Risk）

否決條件包括：
- Regime 被標註為混合 / 不穩定
- Evidence 衝突過高
- Regime 與策略假設不相容

📌 **Regime 不確定時，風控必須收緊，而非放寬。**

---

### 4.5 策略假設風險（Strategy Assumption Risk）

否決條件包括：
- 策略假設未清楚定義失效條件
- 策略假設與 Evidence 相矛盾
- 策略未列入白名單或狀態非 ENABLED

📌 **無法明確說明「何時放棄」的策略，不得執行。**

---

### 4.6 資金與曝險風險（Capital & Exposure Risk）

否決條件包括：
- 單一標的曝險過高
- 相關性集中（隱性集中風險）
- 預期最壞情境下不可承受損失

📌 **風控看的是「活不活得下去」，不是「賺多少」。**

---

### 4.7 系統與操作風險（System & Operational Risk）

否決條件包括：
- 系統狀態異常
- API 回應不穩定
- Log 或審計模組異常
- Kill Switch 不可用

📌 **系統不穩定時，最安全的行為是「不動作」。**

---

## 第 5 章｜否決理由標準化（Reason Codes）

### 5.1 Reason Code 的存在目的
Reason Code 用於：
- 統一否決語言
- 支援審計與回放
- 避免模糊或情緒化判斷

📌 **沒有 Reason Code 的否決，視為不合法。**

---

### 5.2 Reason Code 類型（示例）

| 類型 | Code | 說明 |
|---|---|---|
| 法規 | RC-REG-01 | 法規/交易所規則不確定 |
| 流動性 | RC-LIQ-02 | 流動性不足 |
| 資料 | RC-DATA-03 | 資料不完整或延遲 |
| Regime | RC-REGM-04 | 市場狀態不穩定 |
| 策略 | RC-STR-05 | 策略假設不成立 |
| 曝險 | RC-EXP-06 | 曝險過高 |
| 系統 | RC-SYS-07 | 系統或操作風險 |

📌 實作可擴充，但**不得改變語義**。

---

### 5.3 多重 Reason Code
- 否決可同時附帶多個 Reason Code
- 不得只選擇「較好看的理由」

📌 **否決理由的完整性，高於可接受性。**

---

## 第 6 章｜Degrade 與 Observe-only 的合法使用

### 6.1 何謂 Degrade（降級）
Degrade 指：
> **在不完全否決流程的前提下，  
> 強制將系統行為降級至更保守狀態。**

---

### 6.2 合法的 Degrade 類型
- 限制策略白名單
- 強制 Observe-only
- 降低允許的風險上限
- 暫停 Execution，但保留研究流程

📌 Degrade **不是妥協，是風控手段**。

---

### 6.3 Observe-only 的法定地位
Observe-only：
- 永遠是合法狀態
- 不構成系統失敗
- 不需理由

📌 **「不交易」是合法且常態的選項。**

---

### 6.4 Degrade 的使用邊界
- 不得：
  - 用 Degrade 取代應有的 Reject
  - 長期以 Degrade 規避問題修復

📌 **該否決就否決，是風控的底線。**

---

### 6.5 Degrade / Observe-only 的審計
必須記錄：
- Degrade ID
- 觸發條件
- 持續期間
- Reason Codes
- Correlation ID

📌 **無紀錄 → 降級視為未發生。**

---

（RISK_COMPLIANCE · PART 2 結束）

PART 3｜否決時機 × 實作介面 × 風控最終宣告

## 第 7 章｜否決的時機與即時性（Pre / In / Post）

### 7.1 否決可發生的三個時間點
RISK_COMPLIANCE 的否決權，**不受流程進度限制**，可在以下任一時間點即時生效：

- **Pre-Decision（事前）**  
  - Canonical Flow 尚未完成
  - 資料、Regime、策略假設不成立

- **In-Process（事中）**  
  - Governance Gate 前後
  - Human Decision 前後

- **In-Execution（執行中）**  
  - 委託送出後
  - 成交進行中

📌 **否決的合法性，不因「已經開始執行」而降低。**

---

### 7.2 Pre-Decision 否決（事前）
適用情境：
- Evidence 不完整
- Regime 不穩定
- 策略假設未通過最低標準

處置：
- 阻止流程進入 L8 / L9
- 可建議 Degrade，但不得放行

---

### 7.3 In-Process 否決（事中）
適用情境：
- Governance Gate 發現條款不一致
- Human Decision 前條件失效

處置：
- 立即 Block
- UI 必須清楚呈現否決原因

---

### 7.4 In-Execution 否決（執行中）
適用情境：
- 市場結構急變
- 系統異常
- 合規狀態變更

處置：
- 立即觸發 Kill Switch
- 停止所有新委託
- 視情況撤單

📌 **Execution 中止不需人類事前確認。**

---

### 7.5 否決的不可回溯性
- 否決一經生效：
  - 不得被回溯取消
  - 不得被「當下解釋」合理化
- 重新啟動：
  - 僅能透過新流程、新 Snapshot

---

## 第 8 章｜RISK_COMPLIANCE 的實作介面（Integration Contracts）

### 8.1 與 Governance Gate（L9）的介面
- Governance Gate 必須：
  - 即時查詢 RISK_COMPLIANCE 狀態
  - 尊重最新否決結果
- 任何 Allow：
  - 必須以 RISK = Pass 為前提

---

### 8.2 與 UI（L10）的介面
UI 必須完整呈現：
- 當前 Risk 狀態（Pass / Reject / Degrade）
- Reason Codes（可展開）
- 生效時間
- 是否可重新評估

📌 **UI 不得淡化或隱藏否決資訊。**

---

### 8.3 與 Execution（L11）的介面
Execution 必須：
- 在每一次行為前：
  - 再次確認 Risk 狀態
- 支援：
  - 即時 Kill Switch
  - 部分成交後的中止

📌 **Execution 對 Risk 狀態不具裁量權。**

---

### 8.4 與 Strategy / AI 的介面
- Strategy / AI：
  - 僅能接收否決結果
  - 不得嘗試規避或解釋
- AI 必須：
  - 原樣轉述否決原因
  - 不得附加個人觀點

---

### 8.5 與 Log / Audit 的介面
每一次否決或降級，必須生成：
- Risk Event Log
- Reason Codes
- 觸發時間
- 影響範圍
- Correlation ID

📌 **無 Risk Event Log → 否決視為未發生。**

---

## RISK_COMPLIANCE 最終宣告（Closing）

在 TAITS 中，  
**風控不是阻止你交易的敵人，  
而是確保你還能繼續交易的朋友。**

如果一套系統：
- 無法在最想交易的時刻拒絕交易
- 無法在執行中即時踩煞車
- 無法在虧損前承認不確定性

那它不是一套風控系統，  
只是交易的附屬品。

> **真正的風控，  
> 不是事後解釋為何會輸，  
> 而是事前、事中、隨時有能力說：  
> 「現在不可以。」**

---

（RISK_COMPLIANCE · PART 3 完成）
