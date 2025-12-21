# TAITS — 台灣阿爾法智慧交易系統  
**Taiwan Alpha Intelligence Trading System**

文件類型：Project Entry & Governance Overview  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
治理狀態：Freeze v1.0  
版本狀態：ACTIVE  
最後更新：2025-12-22  

---

## 一、專案定位（Project Positioning）

TAITS（**台灣阿爾法智慧交易系統**，Taiwan Alpha Intelligence Trading System）是一套：

- 專為 **台灣市場（TWSE / TAIFEX）** 設計  
- 可實盤、可長期演進  
- 以 **治理（Governance）與風控（Risk / Compliance）為最高優先權**  
- 採用 **Canonical Flow（L1–L11）** 作為唯一合法流程定義  

本專案並非策略集合、回測工具或自動下單系統，  
而是一套 **可被審計、可被否決、可由人類最終裁決的交易系統母體架構**。

---

## 二、不可違反的核心設計原則（Core Principles）

TAITS 全系統嚴格遵守以下原則：

- 策略 ≠ 下單  
- Agent ≠ 策略  
- AI ≠ 決策主體  
- **Regime 高於策略**  
- **Risk / Compliance 具最高否決權**  
- **Only-Add：只可新增，不可刪減或改寫語義**  
- **Freeze 狀態下不得進行結構性變更**

任何文件、程式碼、對話或實作，皆不得違反上述原則。

---

## 三、治理文件體系與裁決順序（Governance Hierarchy）

TAITS 採用分級治理文件體系，並以以下順序作為最終裁決依據：

1. DOCUMENT_INDEX  
2. MASTER_ARCH  
3. MASTER_CANON  
4. 其餘治理／架構／執行文件  

若文件之間存在任何衝突，  
**一律依上述順序裁決，不得以對話或實作取代文件權威。**

---

## 四、Canonical Flow（唯一合法流程）

TAITS 的唯一合法流程定義為：

> **Canonical Flow：L1–L11**

- L1–L3：資料取得、正規化、狀態固化  
- L4–L5：分析與證據組裝  
- L6：Regime 判定  
- L7：Risk / Compliance（最高否決權）  
- L8–L9：策略提案與治理閘門  
- L10：人類最終裁決  
- L11：合規執行與控制  

任何工程 Phase、流程圖或說明文件，  
**皆不得取代 Canonical Flow 的裁決地位**。

---

## 五、工程流程定錨（Engineering Process Anchor）

本專案已啟用專屬工程流程定錨文件：

> **《TAITS｜程式開發流程定錨文件（Unified Process Anchor）》**

用途僅限於：

- 標示工程開發進度（Phase 0–5）  
- 防止新對話、新 AI 導致流程敘述漂移  
- 作為工程實作時的流程座標參考  

📌 該文件 **不具治理裁決力**，僅為工程輔助定錨。

---

## 六、目前專案狀態（Current Status）

- 治理文件：已齊備  
- 工程流程定錨：已入庫  
- 工程環境：已鎖定  
- 歷史檔案：已封存（_LEGACY_ARCHIVE_）  

目前專案階段：

> **Engineering Phase 0 — 治理與版本鎖定**

---

## 七、Repository 結構說明（Overview）

```text
TAITS_S1/
├─ _LEGACY_ARCHIVE_/        # 歷史封存（AI 不讀、不參與主線）
├─ docs/
│  └─ engineering/
│     └─ TAITS_程式開發流程定錨文件.md
├─ .cursorignore            # 控制 Cursor / AI 掃描範圍
├─ .gitignore               # 控制 Git 版本追蹤
└─ README.md                # 本文件
八、重要聲明（Notice）
本專案不構成任何投資建議

不保證任何獲利結果

所有交易行為皆須通過 人類最終裁決（L10）

AI 僅為輔助分析角色，不具任何決策或執行權限

九、專案使用提醒（Meta）
若在任何對話、工具或實作中發現：

流程被重新定義

裁決來源不明

規則與文件不一致

請立即回到治理文件體系，
以文件為準，而非以對話為準。

TAITS — 建立一套在「不該交易時，會阻止你交易」的系統。
Build the system that prevents you from trading when you should not.
