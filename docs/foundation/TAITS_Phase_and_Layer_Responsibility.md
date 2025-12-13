# 📘 TAITS_Phase_and_Layer_Responsibility.md
## TAITS Phase 與 Layer 責任邊界（Phase S1）

---

## 0. 文件定位（不可模糊）

本文件定義 TAITS **唯一合法的層級責任劃分**。

> 若某模組「能做什麼 / 不能做什麼」不清楚，  
> 則預設為 **不能做**。

優先級：
S0 > S1（本文件） > S2 > S3 > S4 > S5

---

## 1. Phase 職責總覽（S0–S5）

### S0｜Reality & Constraint Layer（現實與約束）

**能做**
- 定義不可違反的現實
- 定義硬性邊界與非目標

**不能做**
- ❌ 不設計策略
- ❌ 不討論績效
- ❌ 不引入工具或模型

**產出**
- Reality / Boundaries / Non-Goals

---

### S1｜Charter & Constitution（憲章與原則）

**能做**
- 定義系統使命與價值排序
- 定義不可動原則
- 定義語義與責任邊界

**不能做**
- ❌ 不寫策略
- ❌ 不談進出場
- ❌ 不評估回測

**產出**
- Charter
- Design Principles
- Glossary
- Phase Responsibilities（本文件）

---

### S2｜Architecture Layer（架構與模組）

**能做**
- 定義模組結構
- 定義資料流 / 事件流
- 定義 Agent / Engine 分工

**不能做**
- ❌ 不做決策
- ❌ 不做下單
- ❌ 不評估績效好壞

**產出**
- System Architecture
- Module Specs
- Data Flow Diagrams

---

### S3｜Decision & Data Layer（決策與資料）

**能做**
- 整合資料
- 執行 Decision Checklist
- 產生唯一 Decision

**不能做**
- ❌ 不直接下單
- ❌ 不修改風控邊界
- ❌ 不解釋「策略為何神」

**產出**
- Decision (TRADE / WAIT / NO_TRADE)
- Evidence Summary
- Audit Logs

---

### S4｜Execution & Risk Layer（執行與風控）

**能做**
- 將 Decision 轉為行為
- 應用 Safety Locks
- 控制曝險與模式

**不能做**
- ❌ 不推翻 Decision
- ❌ 不因執行困難改變策略
- ❌ 不生成新 Decision

**產出**
- Orders / Simulated Orders
- Execution Logs
- Risk Events

---

### S5｜Evaluation & Evolution（評估與演進）

**能做**
- 回顧績效
- 做歸因分析
- 提出調整建議

**不能做**
- ❌ 不直接改動實盤邏輯
- ❌ 不即時干預交易
- ❌ 不因短期績效推翻 S0/S1

**產出**
- Review Reports
- Improvement Proposals

---

## 2. Layer 細分責任（橫向）

### Strategy Layer（策略層）

**責任**
- 產生 Evidence 或 Flags

**禁止**
- ❌ 不得下單
- ❌ 不得否決風控
- ❌ 不得宣稱「決策」

---

### Agent Layer（代理層）

**責任**
- 解讀策略輸出
- 彙整多來源資訊

**禁止**
- ❌ 不得繞過 Gate
- ❌ 不得修改 MR
- ❌ 不得生成 Trade 指令

---

### Governance Layer（治理層）

**責任**
- 啟用 / 禁用策略
- 控制 Lane 可用性
- 執行否決權

**禁止**
- ❌ 不參與交易時機判斷

---

### Decision Core（決策核心）

**責任**
- 整合 Gate / Risk / Evidence
- 輸出唯一 Decision

**禁止**
- ❌ 不解釋市場
- ❌ 不預測價格
- ❌ 不直接下單

---

### Execution Layer（執行層）

**責任**
- 安全執行
- 套用鎖定規則

**禁止**
- ❌ 不得改 Decision
- ❌ 不得自行補單

---

## 3. 跨層違規（嚴格禁止）

以下情況一律視為 **嚴重違規**：

1. Strategy → Order
2. Model → Position Size
3. Execution → Decision
4. S5 → 即時交易干預
5. S3 → 放寬風控

---

## 4. 違規處理流程（Mandatory）

一旦發現跨層行為：

1. 立即標記違規
2. 停止相關模組
3. 回退至安全狀態
4. 記錄於審計日誌

---

## 5. 一句話邊界定錨（不可刪）

> **每一層都只做自己的事，  
> TAITS 才能在複雜中保持穩定。**

---

## 6. 文件狀態

- ✔ Phase S1（責任邊界）
- ✔ 架構與策略接入必讀
- ✔ 防止跨層污染
- ✔ 可長期維護
