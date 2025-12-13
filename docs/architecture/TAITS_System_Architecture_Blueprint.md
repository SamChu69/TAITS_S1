# 📘 TAITS_System_Architecture_Blueprint.md
## TAITS 系統總體架構藍圖（Phase S2）

---

## 0. 文件定位（S2 最高權威）

本文件定義 TAITS **唯一合法的系統總體架構**。

> 本文件必須同時服從：
> - Phase S0（Reality & Constraints）
> - Phase S1（Charter & Constitution）

任何模組、Agent、資料流設計，
**不得違反本文件定義之層級與流向**。

---

## 1. 架構總覽（Top-Level View）

TAITS 採用 **嚴格分層、單向流動** 的架構：

```

┌────────────────────────────┐
│ S0 / S1  憲法與約束層       │
└─────────────▲──────────────┘
│（約束）
┌─────────────┴──────────────┐
│ S2  Architecture Layer     │
│  ├─ Data Ingestion         │
│  ├─ Strategy & Analysis    │
│  ├─ Agent Interpretation   │
│  ├─ Governance & Risk      │
│  ├─ Decision Core          │
│  ├─ Execution Interface    │
│  └─ Audit & Logging        │
└─────────────▼──────────────┘
│（決策）
┌─────────────┴──────────────┐
│ S3 / S4  Decision & Exec   │
└────────────────────────────┘

```

📌 **原則**：  
- 上層只能「約束」下層  
- 下層不得「反向影響」上層  

---

## 2. 核心模組分層（Modules by Layer）

### 2.1 Data Ingestion Layer（資料擷取層）

**責任**
- 接收所有外部資料
- 不做判斷、不做決策

**模組**
- Market Data Adapter（TWSE / TAIFEX）
- Fundamental Data Adapter（MOPS / 財報）
- Event & Calendar Adapter（結算 / 事件）

**禁止**
- ❌ 不得計算策略
- ❌ 不得產生 Evidence

---

### 2.2 Strategy & Analysis Layer（策略分析層）

**責任**
- 將原始資料轉為「候選 Evidence」
- 不做治理、不做決策

**模組**
- Technical Strategy Set
- Fundamental Strategy Set
- Behavioral / Structure Strategy Set
- Cross-Market (Futures / Options) Strategy Set

**輸出**
- Raw Signals
- Preliminary Evidence

---

### 2.3 Agent Interpretation Layer（代理解讀層）

**責任**
- 解讀多策略輸出
- 轉譯為 TAITS 標準 Evidence

**模組**
- Technical Agent
- Fundamental Agent
- Market Structure Agent
- Risk Context Agent

**輸出**
- Tiered Evidence Summary
- Uncertainty Flags

---

### 2.4 Governance & Risk Layer（治理與風控層）

**責任**
- 執行 Gate / Regime / MR
- 啟用 / 禁用策略與 Lane
- 風險否決

**模組**
- Market Regime Engine
- Manipulation Risk Engine
- Strategy Availability Controller
- Risk Budget Controller

**權限**
- 可否決任何下游行為

---

### 2.5 Decision Core（決策核心）

**責任**
- 整合所有允許的輸入
- 輸出唯一 Decision

**輸出（唯一合法）**
- TRADE
- WAIT
- NO_TRADE

**禁止**
- ❌ 不下單
- ❌ 不解釋市場
- ❌ 不預測價格

---

### 2.6 Execution Interface Layer（執行介面層）

**責任**
- 將 Decision 轉為行為（依 Mode）
- 套用 Safety Locks

**模組**
- Paper Executor
- Shadow Executor
- Live Restricted Executor

---

### 2.7 Audit & Logging Layer（審計紀錄層）

**責任**
- 紀錄所有決策與否決
- 支援回放與檢討

**模組**
- Decision Log
- Evidence Snapshot
- Risk Event Log

---

## 3. 資料與決策流向（Hard Rules）

### 合法流向

```

Data → Strategy → Agent → Governance → Decision → Execution

```

### 嚴格禁止

- ❌ Strategy → Execution
- ❌ Model → Decision
- ❌ Execution → Decision
- ❌ Audit → 即時干預

---

## 4. 可擴充點（Designed Extension Points）

TAITS 允許在以下位置擴充：

- 新資料來源 → Data Ingestion
- 新策略 → Strategy Layer
- 新解讀邏輯 → Agent Layer
- 新風控規則 → Governance Layer

📌 **不可擴充的位置**
- Decision Core 的輸出型態
- Gate / MR 的否決權結構

---

## 5. 與 S0 / S1 的對齊聲明

- 本架構 **不假設高頻**
- 本架構 **預設 NO_TRADE 為正常輸出**
- 本架構 **以治理優先於策略**
- 本架構 **以人類可理解為前提**

---

## 6. 架構定錨語（不可刪）

> **TAITS 的架構不是為了跑得快，  
> 而是為了跑得久、跑得穩。**

---

## 7. 文件狀態

- ✔ Phase S2（架構藍圖）
- ✔ 受 S0 / S1 完整約束
- ✔ 所有模組設計必須引用
- ✔ 可長期演進
```

---

## ✅ S2 進度確認

你現在已完成：

* **S2-1：System Architecture Blueprint（完成）**

這代表 **TAITS 的「骨架」已經立好**。
