# TAITS_Document_Index.md
# TAITS — 文件總索引（Master Table of Contents）

版本：Master / Full  
適用對象：產品經理 / 架構師 / 工程師 / 研究員 / AI  
專案名稱：TAITS – Taiwan Alpha Intelligence Trading System

---

## 0. 本文件用途（必讀）

本文件為 **TAITS 專案所有文件的唯一總索引入口**。

任何人（包含 AI）在：
- 接手專案
- 開新對話
- 開始實作
- 回顧架構
- 檢查合規

👉 **必須先閱讀本文件，再依指引閱讀其他文件。**

---

## 1. TAITS 文件體系總覽（分層治理）

TAITS 文件分為五大治理層級：

```

Layer 1：系統架構（Architecture）
Layer 2：資料治理（Data Governance）
Layer 3：策略治理（Strategy Governance）
Layer 4：風控與合規（Risk & Compliance）
Layer 5：介面與操作（UI & Operations）

```

---

## 2. Layer 1 — 系統架構（不可推翻）

📍 **閱讀優先級：最高**

### 2.1 系統藍圖（Master Architecture）

- 📄 `docs/architecture/TAITS_Full_System_Architecture.md`
  - 定義 TAITS 的完整體架構
  - 全模組邊界、資料流、決策流
  - 纏論 / 期貨 / 選擇權 / AI / Regime / Fusion
  - 不分開發階段（即最終藍圖）

👉 **任何設計不得違反此文件**

---

## 3. Layer 2 — 資料治理（Single Source of Truth）

📍 **閱讀優先級：極高**

### 3.1 資料來源宇宙

- 📄 `docs/datasources/TAITS_DataSources_Universe.md`
  - 列出 TAITS 允許使用的所有資料來源
  - TWSE / TPEX / MOPS / 集保 / TAIFEX / 富邦
  - 新聞 / 情緒 / 宏觀
  - Fallback 與合法性規範

👉 **未列資料來源不得使用**

---

## 4. Layer 3 — 策略治理（不縮水核心）

📍 **閱讀優先級：極高**

### 4.1 全策略宇宙（Master）

- 📄 `docs/strategies/TAITS_Strategy_Universe_Complete.md`
  - 原始 285 策略（完整保留）
  - 補充策略（20251210）
  - 纏論 ChanLun（35+）
  - 總計 355+ 策略
  - 明確對應資料 / Agent / Regime

👉 **策略不得刪減、不得任意改類**

---

## 5. Layer 4 — 風控與法規（最終否決權）

📍 **閱讀優先級：高**

### 5.1 風控與合規白皮書

- 📄 `docs/risk/TAITS_Risk_and_Compliance.md`
  - TWSE / TPEX 交易規則
  - Tick Size / 漲跌幅 / 交易時間
  - 部位 / 資金 / 流動性風控
  - 事件 / 極端風險
  - AI 使用限制
  - **具備否決權（Veto Power）**

👉 **高於策略、Agent、Fusion、AI**

---

## 6. Layer 5 — 介面與操作（防呆層）

📍 **閱讀優先級：中高**

### 6.1 UI 與操作規範

- 📄 `docs/ui/TAITS_UI_Spec.md`
  - 使用者角色與權限
  - 顯示規則（顏色、語意）
  - 操作流程與防呆
  - Risk 與 Regime 顯示強制規則
  - Audit 與回溯

👉 **UI 是風控的一部分**

---

## 7. 專案入口文件（世界觀）

### 7.1 專案門面

- 📄 `README.md`
  - 專案定位
  - 系統簡介
  - 新手理解入口

---

## 8. 新對話 / AI 接手指引（非常重要）

### 8.1 新對話啟動方式

- 使用 **TAITS 專案啟動 Prompt（最終版）**
- 新對話第一則訊息必須貼上
- 若 AI 回覆未對齊上述文件 → 視為未初始化成功

---

## 9. 文件閱讀建議順序（快速上手）

### 🔰 新接手（人 / AI）

1. README.md
2. TAITS_Document_Index.md
3. TAITS_Full_System_Architecture.md
4. TAITS_DataSources_Universe.md
5. TAITS_Strategy_Universe_Complete.md
6. TAITS_Risk_and_Compliance.md
7. TAITS_UI_Spec.md

---

## 10. 文件治理原則（不可忽略）

- 文件高於程式碼
- 架構高於實作
- 合規高於策略
- Risk 高於 AI
- 本索引文件高於「口頭說明」

---

## 11. 一句話總結

> **TAITS 不是靠記憶運作，  
> 而是靠文件治理。**

---

---

## 本次對話更新摘要

更新日期：2025-12-13

已新增（融入既有文件）：
- `TAITS_Strategy_Universe_Complete.md`：新增 Decision Core、時間優勢、期貨/選擇權作為指標、威科夫 Explore/Exploit、多決策線治理
- `TAITS_Risk_and_Compliance.md`：新增主力操盤風險（M0~M4）與每日/每週風險檢查流程
- `TAITS_Full_System_Architecture.md`：補充 DecisionCore/TimeAdvantage/ManipulationRisk/PortfolioManager 模組定位
- `TAITS_Architecture_and_Flow.md`：補充端到端決策流程（含雙軌與否決）
- `TAITS完整總架構 × 總流程 × 全資訊體系（MASTER VERSION）.md`：加入「最新策略融合補丁」索引
