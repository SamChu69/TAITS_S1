# 📘 TAITS_Decision_Lanes_and_Time_Horizon.md
## TAITS 決策通道與時間尺度（Phase S3）

---

## 0. 文件定位（Lane 與時間的最高權威）

本文件定義 TAITS 中 **Decision Lane 與 Time Horizon 的唯一合法對應關係**。

> Lane 不是策略分類，  
> Lane 是 **風險與時間的治理工具**。

優先級：
S0 > S1 > S2 > S3-1 ~ S3-2 > **本文件**

---

## 1. 為何 TAITS 需要 Lane（設計動機）

市場的錯誤，常來自以下混用：

- 用短線訊號做長線投資
- 用基本面理由承受短線回撤
- 用結構假設做當沖決策

TAITS 的解法是：

> **先決定「你在做哪一條 Lane 的事」，  
> 再談是否交易。**

---

## 2. Decision Lane 總覽

| Lane | 核心目的 | 主要風險 | 時間尺度 |
|---|---|---|---|
| A | 結構 / 行為 | 結構誤判 | 中長期 |
| B | 價值 / 基本面 | 價值陷阱 | 中期 |
| C | 執行 / 短線 | 波動與噪音 | 短期 |

📌 同一筆 Decision **只能屬於一條 Lane**。

---

## 3. Lane A｜Structure / Behavior Lane

### 3.1 定位

- 關注：市場結構、主力行為、Regime
- 目標：避免被「結構性錯誤」淘汰

### 3.2 合法 Evidence

- Tier-1（結構性證據）為核心
- Tier-2 作為輔助
- Tier-3 僅用於進場時機微調

### 3.3 時間尺度（Time Horizon）

- 週 → 月
- 決策頻率低
- 容忍短期噪音，不容忍結構破壞

### 3.4 風險與否決

- 任一 Tier-1 否決 → NO_TRADE
- MR ≥ 2 → 禁止新進場
- 回撤期間 → 降頻，不加碼

---

## 4. Lane B｜Value / Fundamental Lane

### 4.1 定位

- 關注：基本面、財報、產業循環
- 目標：在合理風險下承接價值

### 4.2 合法 Evidence

- Tier-2（背景 / 基本面）為主
- Tier-1 用於避免結構性陷阱
- Tier-3 僅作為執行輔助

### 4.3 時間尺度（Time Horizon）

- 月 → 季
- 容忍整理與震盪
- 不容忍結構轉空與治理風險

### 4.4 風險與否決

- 結構轉壞 → 停止加碼
- 基本假設失效 → 退出 Lane
- MR ≥ 2 → 降權或暫停

---

## 5. Lane C｜Execution / Tactical Lane

### 5.1 定位

- 關注：執行效率、短期節奏
- 目標：在「被允許的情境」中捕捉短期機會

### 5.2 合法 Evidence

- Tier-3（戰術 / 技術）為主
- Tier-1 / Tier-4 為硬性約束
- Tier-2 僅作背景參考

### 5.3 時間尺度（Time Horizon）

- 分鐘 → 日
- 決策頻率高於 A / B
- 必須嚴格受 Gate 與 MR 約束

### 5.4 風險與否決

- MR ≥ 1 → 明顯降權
- MR ≥ 2 → 禁止 Lane C
- 高不確定性 → WAIT

---

## 6. Lane 切換規則（Hard Rules）

### 6.1 禁止即時切換

- 不允許同一 Decision 在 A/B/C 間切換
- 不允許「本來是 C，套牢後說是 B」

📌 **這是散戶最常犯、也最致命的錯誤**

---

### 6.2 合法切換（僅限 S5）

Lane 切換只能在：

- 事後檢討（S5）
- 新一輪 Decision Request
- 完整重新評估 Evidence

---

## 7. Lane 與 Decision Core 的關係

- Lane 是 Decision 的屬性
- Decision Core 不為任何 Lane 破例
- Lane 只影響：
  - 可用 Evidence
  - 時間尺度
  - 風險容忍度

---

## 8. Lane 與倉位（重要聲明）

- Lane ≠ 倉位大小
- Lane ≠ 報酬期待
- Lane 只定義「你在做什麼樣的事」

📌 倉位只在 S4 依 Risk Budget 決定。

---

## 9. 常見錯誤（Explicitly Forbidden）

- ❌ 用 C Lane 的訊號長抱
- ❌ 用 B Lane 的理由做短線
- ❌ 用 A Lane 的敘事忽略回撤
- ❌ Lane 混用來合理化虧損

---

## 10. 定錨語（不可刪）

> **選錯時間尺度，  
> 再好的策略都是錯的。**

---

## 11. 文件狀態

- ✔ Phase S3（Lane & Time Horizon）
- ✔ 與 Evidence / Decision Core 完全對齊
- ✔ 防止時間錯配
- ✔ 可長期演進
