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
---

# 【TAITS UI 可解釋決策與審計顯示規格】
## 版本：v2025-12-16
## 性質：Only-Add（追加，不覆蓋既有內容）

本章節定義：  
TAITS 的任何畫面，不只是「顯示結果」，而是必須回答三個問題：

1. 為什麼現在是這個判斷？
2. 依據是什麼？
3. 哪些風險正在限制你？

---

## 一、UI 總原則（不可違反）

### 1. 結果必須有原因
- 禁止只顯示「建議 / 不建議」
- 必須同時顯示 **證據來源與風險限制**

### 2. 任何結論都可回放
- UI 必須顯示 snapshot_ref
- 點擊 snapshot_ref 可查看當時資料摘要

---

## 二、核心畫面模組（必備）

### 2.1 市場總覽面板（Market Overview）

**必顯示**
- Regime 狀態（多頭 / 盤整 / 空頭 / 高風險）
- Regime 信心度（0–100）
- Regime 證據摘要（來自 Evidence Bundle）
- snapshot_ref

**目的**
讓你一眼知道：
> 現在整體市場，適不適合積極做股票？

---

### 2.2 標的分析面板（Instrument Analysis）

**必顯示區塊**
1. 技術摘要（趨勢 / 動能 / 波動 / 量能）
2. Wyckoff 模組
   - 階段
   - 事件點
   - 信心度
3. 鮑迪克纏論模組
   - 結構狀態
   - 背離類型
   - 段落一致性
4. 題材與消息模組
   - 事件旗標
   - 敘事證據（逐條）
   - 熱度分數
5. Observe-only 跨市場警示
   - 期貨
   - 選擇權
   - 融資融券

---

### 2.3 策略與限制面板（Strategy & Constraints）

**必顯示**
- 目前允許的策略清單
- 被禁止的策略清單（附原因）
- 權重調整結果
- 出場優先權調整

**目的**
避免你看到訊號卻不知道：
> 為什麼系統現在不讓你做？

---

### 2.4 風控與合規面板（Risk & Compliance）

**必顯示**
- 風控狀態（正常 / 警示 / 否決）
- Risk Audit Bundle 摘要
- 被阻擋的行為
- 觸發規則清單
- snapshot_ref

---

### 2.5 證據包詳情頁（Evidence Bundle Detail）

**必顯示**
- trigger_rules（逐條）
- technical_summary
- event_flags
- narrative_evidence
- heat_score
- rumor_risk_tags
- wyckoff_bundle
- bodick_bundle
- cross_market_flags

**重要原則**
- 不准合併、不准一句話
- 缺失資料要顯示「缺失」

---

## 三、互動與審計（你一定會用到）

### 3.1 快照回放（Snapshot Replay）
- 可選擇 snapshot_ref
- 重現當時市場狀態與證據

### 3.2 決策歷史（Decision History）
- 每一筆決策必顯示：
  - 時間
  - 使用的策略
  - 被哪個風控限制
  - snapshot_ref

---

## 四、驗收標準（UI 是否合格）

1. 任何一筆建議，你都能說出「為什麼」
2. 任何一次被擋，你都能看到「誰擋、為什麼」
3. 新對話只看 UI 規格就能理解系統邏輯

---

# 【End of TAITS_UI_Spec 追加章節】

