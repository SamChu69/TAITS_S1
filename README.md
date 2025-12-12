# TAITS — Taiwan Alpha Intelligence Trading System  
**台灣阿爾法智能交易系統**

---

## 🚨 重要聲明（請先閱讀）

TAITS 是一套 **交易決策作業系統（Trading Decision Operating System）**，  
而不是單一策略、單一 AI、或一鍵自動交易工具。

TAITS **不保證獲利**，  
但嚴格設計為：

> **可解釋、可審計、可長期演進、不輕易出事的交易系統母體**

---

## 🧠 TAITS 是什麼？

TAITS（Taiwan Alpha Intelligence Trading System）是一套：

- 專為 **台灣市場（TWSE / TPEX / TAIFEX）** 設計
- 結合：
  - **355+ 策略宇宙**
  - **完整纏論（ChanLun，作為結構因子）**
  - **多智能體（Agents）**
  - **Market Regime（市場狀態）**
  - **AI 輔助（非唯一真理）**
  - **風控與合規（最高否決權）**
- 支援：
  - Research / Backtest / Paper / Live
- 強調：
  - **策略 ≠ 下單**
  - **AI ≠ 唯一真理**
  - **Risk / Compliance 可否決一切**

---

## ❌ TAITS 不是什麼？

TAITS 不是：

- ❌ 單一技術指標
- ❌ 單模型 AI 猜盤
- ❌ 一鍵跟單工具
- ❌ 快速致富系統
- ❌ 教學 Demo 專案

---

## 🧱 系統總體架構（概覽）

TAITS 採用 **9 層分層架構**：

```

Layer 0 ─ Infrastructure / Runtime
Layer 1 ─ Data Layer
Layer 2 ─ Feature / Indicator / Factor
Layer 3 ─ Strategy Layer（355+）
Layer 4 ─ Agents（多智能體）
Layer 5 ─ Regime + Fusion
Layer 6 ─ Portfolio + Risk
Layer 7 ─ Execution
Layer 8 ─ UI / Reporting / Audit

```

👉 詳細內容請閱讀：  
`docs/architecture/TAITS_MASTER_ARCHITECTURE.md`

---

## 📁 專案結構導覽（只列治理層）

```

docs/
├── TAITS_Document_Index.md        ← 專案文件總入口（必讀）
│
├── architecture/                  ← 系統母體與流程
├── datasources/                   ← 資料 Single Source of Truth
├── strategies/                    ← 策略 Single Source of Truth
├── risk/                          ← 風控與合規（最高否決權）
├── ui/                            ← 操作與防呆規範
└── onboarding/                    ← 新手 / 新 AI 接手規範

```

---

## 📚 建議閱讀順序（非常重要）

**第一次接觸 TAITS，請照此順序：**

1. `docs/TAITS_Document_Index.md`
2. `docs/architecture/TAITS_MASTER_ARCHITECTURE.md`
3. `docs/architecture/TAITS_Full_System_Architecture.md`
4. `docs/datasources/TAITS_DataSources_Universe.md`
5. `docs/strategies/TAITS_Strategy_Universe_Complete.md`
6. `docs/risk/TAITS_Risk_and_Compliance.md`
7. `docs/ui/TAITS_UI_Spec.md`

---

## 🛡 核心設計原則（不可違反）

- 策略 ≠ 下單
- Agent ≠ 策略
- AI ≠ 唯一真理
- Regime 高於單一訊號
- **Risk / Compliance 可否決一切**
- 官方資料優先，多層 fallback
- 架構必須可長期演進

---

## 🔧 開發與使用狀態

目前專案狀態：

- ✅ 文件治理層（docs）已完整
- ⏳ 程式骨幹（S1）準備中
- ⏳ 回測 / 模擬 / 實盤逐步落地

---

## 👥 適合誰使用？

TAITS 適合：

- 想建立 **可長期演進交易系統** 的個人或團隊
- 重視 **風控、合規、可解釋性** 的交易者
- 想把 AI 放在「輔助角色」而非黑盒決策的人

不適合：

- 想快速跟單、無風控交易
- 不願閱讀文件、只想要答案

---

## ⚠️ 免責聲明

本專案僅為研究與系統設計用途，  
任何交易行為所產生之盈虧，  
需由使用者自行承擔。

---

## 🧭 一句話總結

> **TAITS 不是為了「賺快錢」，  
> 而是為了「在市場裡活得久」。**

---

## 📊 Project Status

![Status](https://img.shields.io/badge/status-active_development-blue)
![Docs](https://img.shields.io/badge/docs-100%25_complete-brightgreen)
![Architecture](https://img.shields.io/badge/architecture-master_ready-green)
![Risk](https://img.shields.io/badge/risk-hard_gate-red)
![Market](https://img.shields.io/badge/market-TWSE%20%7C%20TAIFEX-orange)
![AI](https://img.shields.io/badge/AI-assisted_not_autonomous-yellow)

---

## 🗺 Roadmap

### ✅ Phase 0 — Governance & Architecture（已完成）
- [x] 文件治理層（docs）完整建立
- [x] Master Architecture / Flow / Risk / UI
- [x] Data & Strategy Single Source of Truth
- [x] README 專案門面完成

---

### 🚧 Phase 1 — Core System Skeleton（S1，進行中）
- [ ] main.py（系統啟動入口）
- [ ] Orchestrator（流程調度核心）
- [ ] Mode 切換（Research / Backtest / Paper）
- [ ] 基礎 Logger / Audit Trail
- [ ] Dummy Pipeline（不下單，只走流程）

---

### ⏳ Phase 2 — Strategy & Agent Wiring
- [ ] 策略註冊機制（355+ 掛接）
- [ ] Agent Manager
- [ ] Regime Engine v1
- [ ] Fusion Engine v1

---

### ⏳ Phase 3 — Risk / Backtest / Paper Trading
- [ ] Risk Engine（Hard Gate）
- [ ] 事件驅動回測
- [ ] Paper Trading 撮合
- [ ] 績效 / 回撤報告

---

### 🔒 Phase 4 — Live Execution（嚴格受限）
- [ ] 券商 API（富邦）
- [ ] Live 模式雙重確認
- [ ] 即時熔斷
- [ ] 審計回放

---

> **Roadmap 原則**  
> - 文件先於程式  
> - Risk 先於 Execution  
> - 可跑 ≠ 可下單  

---
