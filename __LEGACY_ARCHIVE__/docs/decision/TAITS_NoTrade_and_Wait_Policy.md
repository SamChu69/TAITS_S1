# 📘 TAITS_NoTrade_and_Wait_Policy.md
## TAITS 不交易與等待政策（Phase S3）

---

## 0. 文件定位（決策層安全機制）

本文件定義 TAITS 中 **NO_TRADE 與 WAIT 的唯一合法語義與使用規則**。

> 在 TAITS 中：
> - 不交易不是失敗
> - 等待不是浪費
> - 勉強交易才是風險

優先級：
S0 > S1 > S2 > S3-1 ~ S3-3 > **本文件** > S4 / S5

---

## 1. NO_TRADE 與 WAIT 的正式定義

### 1.1 NO_TRADE（禁止交易）

**定義**  
系統判定「**在目前狀態下，不允許任何交易行為**」。

**特性**
- 硬性結果
- 具有否決權
- 不因訊號強弱而改變

---

### 1.2 WAIT（暫停觀察）

**定義**  
系統判定「**目前資訊不足或不確定性偏高，暫不交易，但持續觀察**」。

**特性**
- 保守結果
- 可隨事件更新而轉換
- 不等於即將交易

---

## 2. NO_TRADE 的強制觸發條件（Hard Triggers）

以下任一成立，**Decision Core 必須輸出 NO_TRADE**：

### 2.1 Gate / Governance 類

- Regime 不允許交易
- MR Level = 3
- 風控鎖定（Risk Budget Exhausted）
- 系統維護 / 模式禁止

---

### 2.2 結構性否決（Tier-1）

- 主力操盤風險成立
- 結構假突破
- 行為階段不匹配 Lane

---

### 2.3 合規與完整性

- 關鍵資料缺失（無法判定 Regime / MR）
- 決策快照不完整
- 無法回放決策

📌 **NO_TRADE 一旦成立，不得進入任何支持度彙整流程**

---

## 3. WAIT 的觸發條件（Soft Triggers）

以下任一成立，**Decision Core 應偏向 WAIT**：

### 3.1 不確定性偏高（Tier-4）

- 事件風險臨近（結算、公告）
- 波動異常但方向不明
- 資料延遲或可信度下降

---

### 3.2 支持不足

- Tier-2 與 Tier-3 支持度不足
- 多策略結論分歧
- Lane 可用但信心帶偏低

---

### 3.3 回撤與恢復期

- 回撤期間（Recovery Mode）
- 近期錯誤密集（Error Clustering）

---

## 4. NO_TRADE / WAIT 的優先權規則

### 4.1 否決優先於支持

- 任一 NO_TRADE 條件成立 → 忽略所有支持 Evidence
- WAIT 不得被單一強訊號推翻

---

### 4.2 不可被績效推翻

以下理由 **一律無效**：

- 「最近沒賺錢」
- 「市場在漲」
- 「訊號看起來很強」
- 「錯過就沒了」

📌 **機會成本不是風險理由**

---

## 5. 與 Decision Lane 的互動

### Lane A（結構）

- 結構未完成 → NO_TRADE
- 行為階段模糊 → WAIT

### Lane B（價值）

- 基本假設未確認 → WAIT
- 結構轉壞 → NO_TRADE

### Lane C（執行）

- MR ≥ 2 → NO_TRADE
- 高波動無結構 → WAIT

---

## 6. 與 Execution 的關係（Hard Rule）

- NO_TRADE → Execution Layer 不得產生任何訂單
- WAIT → Execution 僅能監控，不得預下單
- Execution 不得以任何理由要求重決策

---

## 7. 審計與回放（Auditability）

每一次 NO_TRADE / WAIT 必須記錄：

- 觸發原因（Gate / Tier-1 / Tier-4）
- 相關 Evidence 摘要
- 資料品質狀態
- 系統狀態（Regime / MR）

📌 **必須能回答：「為什麼沒交易？」**

---

## 8. 人類介面（Human Override 聲明）

TAITS 明確規定：

- NO_TRADE 不接受人工覆蓋
- WAIT 僅能要求「重新評估」，不可強制交易
- 所有人工行為必須被記錄

---

## 9. 常見錯誤（Explicitly Forbidden）

- ❌ 用 WAIT 當成「快要進場」
- ❌ 用 NO_TRADE 合理化事後追單
- ❌ 因連續 WAIT 而放寬條件
- ❌ 因錯過行情而修改政策

---

## 10. 定錨語（不可刪）

> **不交易，是 TAITS 最常見、  
> 也是最健康的決策。**

---

## 11. 文件狀態

- ✔ Phase S3（NO_TRADE / WAIT 制度）
- ✔ 與 Decision Core / Evidence / Lane 完全對齊
- ✔ 抗績效壓力
- ✔ 可長期演進
