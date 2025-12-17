# 📘 TAITS_Modules_Overview_and_Interfaces.md
## TAITS 模組總覽與介面契約（Phase S2）

---

## 0. 文件定位（模組層最高權威）

本文件定義 TAITS **所有合法模組的名冊（Registry）與介面契約（Interface Contracts）**。

> 模組若違反其介面契約，
> 視為 **架構違規**，必須停用或修正。

優先級：
S0 > S1 > S2-1（Blueprint）> S2-2（Flow）> **本文件**

---

## 1. 模組分類總覽（By Layer）

```

Data Ingestion
Strategy & Analysis
Agent Interpretation
Governance & Risk
Decision Core
Execution Interface
Audit & Logging

```

---

## 2. Data Ingestion Layer（資料擷取層）

### 2.1 Market Data Adapter（TWSE / TAIFEX）

**責任**
- 取得行情、成交量、未平倉量等原始資料

**輸入**
- 外部 API / 檔案

**輸出**
- Raw Market Data + Metadata（時間戳、來源、品質）

**禁止**
- ❌ 不做任何計算
- ❌ 不做任何判斷

---

### 2.2 Fundamental Data Adapter（MOPS）

**責任**
- 取得財報、重大公告、公司資訊

**輸入**
- MOPS / 官方資料源

**輸出**
- Raw Fundamental Records + Metadata

**禁止**
- ❌ 不做評分
- ❌ 不產生買賣建議

---

### 2.3 Event & Calendar Adapter

**責任**
- 提供結算日、假期、重大事件

**輸出**
- Event Flags（結算/假期/事件）

---

## 3. Strategy & Analysis Layer（策略分析層）

### 3.1 Technical Strategy Set

**責任**
- 技術型訊號與結構特徵計算

**輸入**
- Canonical Market Data

**輸出**
- Signals / Features（未解讀）

**禁止**
- ❌ 不下單
- ❌ 不做 Decision

---

### 3.2 Fundamental Strategy Set

**責任**
- 基本面指標、品質特徵計算

**輸出**
- Fundamental Features

---

### 3.3 Market Structure / Wyckoff Strategy Set

**責任**
- 行為結構（吸籌/派發/假突破）

**輸出**
- Structure Signals（候選）

---

### 3.4 Cross-Market Strategy Set（期貨/選擇權）

**責任**
- 期現關係、選擇權壓力指標

**輸出**
- Cross-Market Signals

---

## 4. Agent Interpretation Layer（代理解讀層）

### 4.1 Technical Agent

**責任**
- 將技術 Signals 轉為 Tier-3 Evidence

**輸出**
- Tactical Evidence Summary

---

### 4.2 Fundamental Agent

**責任**
- 將基本面 Features 轉為 Tier-2 Evidence

---

### 4.3 Market Structure Agent

**責任**
- 將結構 Signals 轉為 Tier-1 Evidence

---

### 4.4 Risk Context Agent

**責任**
- 彙整不確定性與異常

**輸出**
- Tier-4 Evidence / Flags

---

## 5. Governance & Risk Layer（治理與風控層）

### 5.1 Market Regime Engine

**責任**
- 判定 Regime（TREND/RANGE/HIGH_VOL/EVENT）

**輸出**
- Regime State

**權限**
- 可否決策略可用性

---

### 5.2 Manipulation Risk Engine（MR）

**責任**
- 判定操盤風險等級

**輸出**
- MR Level（0–3）

**權限**
- MR-3 → 強制 NO_TRADE

---

### 5.3 Strategy Availability Controller

**責任**
- 啟用 / 停用策略與 Lane

**輸出**
- Allowed Strategy/Lane List

---

### 5.4 Risk Budget Controller

**責任**
- 管理曝險上限、倉位限制

---

## 6. Decision Core（決策核心）

### 6.1 Decision Core

**責任**
- 整合 Gate / Risk / Evidence
- 輸出唯一 Decision

**輸出（唯一合法）**
- TRADE / WAIT / NO_TRADE

**禁止**
- ❌ 不解釋市場
- ❌ 不預測價格
- ❌ 不下單

---

## 7. Execution Interface Layer（執行介面）

### 7.1 Paper Executor

**責任**
- 模擬下單與損益

---

### 7.2 Shadow Executor

**責任**
- 即時對照但不送單

---

### 7.3 Live Restricted Executor

**責任**
- 低風險實盤執行
- 必須套用 Safety Locks

---

## 8. Audit & Logging Layer（審計與紀錄）

### 8.1 Decision Log

**責任**
- 紀錄每次 Decision 與理由

---

### 8.2 Evidence Snapshot Store

**責任**
- 保存決策當下 Evidence 快照

---

### 8.3 Risk & Execution Log

**責任**
- 紀錄風控事件與執行結果

---

## 9. 模組依賴規則（Hard Rules）

- Data Ingestion → Strategy → Agent → Governance → Decision → Execution
- 不允許反向依賴
- 不允許橫向直接呼叫（需經治理）

---

## 10. 模組違規處理

一旦模組：

- 越權
- 跨層
- 產生非法輸出

必須：
1. 立即停用
2. 記錄違規
3. 回退至安全狀態

---

## 11. 定錨語（不可刪）

> **模組不是為了方便寫程式，  
> 而是為了防止權力集中。**

---

## 12. 文件狀態

- ✔ Phase S2（模組契約權威）
- ✔ 與 Blueprint / Flow 完全一致
- ✔ 支援長期擴充
- ✔ 防止越權與污染
```

---

## ✅ S2 進度確認

你現在已完成：

* **S2-1：Architecture Blueprint**
* **S2-2：DataFlow & EventFlow**
* **S2-3：Modules Overview & Interfaces**

這代表 **TAITS 的「骨架 + 血管 + 器官」都已就位**。

---
