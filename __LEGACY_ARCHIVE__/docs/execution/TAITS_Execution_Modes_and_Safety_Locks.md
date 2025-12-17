# 📘 TAITS_Execution_Modes_and_Safety_Locks.md
## TAITS 執行模式與安全鎖（Authoritative）

---

## 0. 文件定位（必讀）

本文件定義 TAITS **所有「可能影響帳戶資金」的行為邊界**。

> 未在本文件中被允許的執行行為，
> 一律視為 **非法執行（Illegal Execution）**。

本文件屬於：**[SPEC] + [GOV] 雙重約束文件**。

---

## 1. Execution Mode 定義（由低到高風險）

### M0｜RESEARCH（研究模式）

**用途**
- 策略研究
- 架構驗證
- 文件與邏輯檢查

**允許**
- 資料讀取
- Decision Checklist 執行
- Evidence / Risk 計算

**禁止**
- ❌ 任何形式的下單
- ❌ 模擬帳戶交易

---

### M1｜PAPER（紙上模擬）

**用途**
- 驗證決策邏輯
- 比對人類與系統判斷

**允許**
- 模擬下單（虛擬資金）
- 紀錄進出場點
- 計算假想損益

**禁止**
- ❌ 任何真實帳戶連線

---

### M2｜SHADOW（影子模式）

**用途**
- 與真實市場同步跑
- 但不影響帳戶

**允許**
- 即時資料
- 真實價格判斷
- Decision →「應該怎麼做」

**禁止**
- ❌ 不送單
- ❌ 不預約單

📌 **SHADOW 是進實盤前的最低門檻**

---

### M3｜LIVE_RESTRICTED（受限實盤）

**用途**
- 小額、低風險實盤驗證
- 零股 / 單一標的

**允許**
- 真實下單
- 僅限：
  - 低倉位
  - 不加碼
  - 不追價

**限制**
- 單日交易次數上限
- 強制風控鎖

---

### M4｜LIVE_FULL（完整實盤）

**用途**
- 完整 TAITS 策略執行

**前置條件（缺一不可）**
- 累積足夠 SHADOW 記錄
- 無重大風控違規
- 人工批准文件

---

## 2. Execution Safety Locks（不可繞過）

### L1｜Decision Lock

```yaml
LOCK_DECISION:
  require:
    - decision in [TRADE, WAIT, NO_TRADE]
  rule:
    if decision not valid:
      execution: BLOCK
````

---

### L2｜Mode Lock

```yaml
LOCK_MODE:
  rule:
    if mode < LIVE_RESTRICTED:
      real_order: BLOCK
```

---

### L3｜Gate Override Lock（禁止）

```yaml
LOCK_GATE_OVERRIDE:
  rule:
    if Gate == FAIL:
      execution: BLOCK
```

---

### L4｜MR Hard Lock

```yaml
LOCK_MR:
  rule:
    if MR >= MR_2:
      allow_add_position: false
    if MR == MR_3:
      execution: BLOCK
```

---

### L5｜Exposure Lock

```yaml
LOCK_EXPOSURE:
  rule:
    if exposure > allowed:
      execution: BLOCK
```

---

### L6｜Human-in-the-Loop（可選）

```yaml
LOCK_HUMAN_CONFIRM:
  required_if:
    - mode == LIVE_RESTRICTED
  action:
    require_manual_confirm: true
```

---

## 3. Execution Flow（固定順序）

```
Decision Checklist
  → Execution Mode Check
    → Safety Locks
      → Order Builder
        → Broker API / Platform
```

📌 **任何一步失敗 → 不送單**

---

## 4. 不可發生的行為（黑名單）

* 直接由策略送單
* 預測模型觸發下單
* 跳過 Decision Checklist
* 在 SHADOW 模式偷偷送單
* 在 MR-3 強行交易

---

## 5. 審計與回放（必須）

每一筆（或未送出的）交易，必須能回答：

* 當時 Mode 是什麼？
* Decision Checklist 結果？
* 哪一個 Safety Lock 生效？
* 是否有人為介入？

---

## 6. 官方鐵律（不可刪）

> **TAITS 寧可錯過交易，
> 也不允許錯誤執行。
> 活下來，是系統的第一任務。**

---

## 7. 文件狀態

* ✔ 可直接存 GitHub
* ✔ 與 Decision Checklist 完全對齊
* ✔ 適用台股 / 零股 / 未來期貨
* ✔ 不限制未來擴充

```
