# TAITS Onboarding Guide

本資料夾為 **TAITS – Taiwan Alpha Intelligence Trading System**
的「唯一官方 Onboarding 文件」。

目標：
- 讓任何 AI / 人類工程師
- 在不依賴任何歷史對話的情況下
- 只透過本資料夾與專案文件
即可 **完整、正確、不中斷地接手 TAITS 系統**

本 Onboarding 適用對象：
- GPT / LLM（新對話）
- 新加入的工程師
- 架構審查者
- 長期維護者

⚠️ 注意  
TAITS 是「文件驅動系統」，**文件即事實來源**，對話不具備權威性。
```

---

## 📄 `01_Project_Identity_and_Roles.md`

```md
# TAITS 專案身分與角色定義

## 一、專案名稱
TAITS – Taiwan Alpha Intelligence Trading System

## 二、專案定位
TAITS 是一套：
- 專為 TWSE / TAIFEX 設計
- 可實盤、可長期演進
- 結合 285+ 策略、完整纏論、期貨與選擇權
- 採用多 Agent + Regime + Risk 架構
的完整量化交易系統

這不是 Demo、不是單一策略專案。

## 三、角色分工

### 使用者（產品經理）
- 不寫程式、不 Debug
- 只負責決策與貼上完整內容

### AI / 工程師
- 必須遵守既有架構
- 不得縮水、不得自行簡化
- 所有輸出必須是「完整可直接使用」
```

---

## 📄 `02_Master_Prompt_and_Usage.md`

```md
# TAITS Master Prompt 使用說明

## 一、Master Prompt 的角色
Master Prompt 是 TAITS 的「行為憲法」，用於：

- 新對話啟動
- GPT Project 初始化
- AI 身分與權限定義

## 二、使用規則
- 每個新對話 **第一件事一定要貼**
- 不可摘要
- 不可改寫

## 三、Master Prompt 內容來源
請使用專案中的：
- 「TAITS 專案最終版啟動 Prompt（FINAL / OFFICIAL）」
```

（這裡**不重貼 Prompt 本文**，避免重複與未來版本衝突）

---

## 📄 `03_Document_Authority_and_Loading_Order.md`

```md
# TAITS 文件權威與載入順序

## 一、最高權威文件（不可推翻）

1. TAITS_MASTER_ARCHITECTURE.md
2. TAITS完整總架構 × 總流程 × 全資訊體系（MASTER VERSION）.md
3. TAITS_Architecture_and_Flow.md
4. TAITS_DataSources_Universe.md
5. TAITS_Strategy_Universe_Complete.md
6. TAITS_Risk_and_Compliance.md
7. TAITS_Document_Index.md

## 二、衝突處理原則
- 上位文件 > 下位文件
- MASTER > 補充 > 過渡版本
- 文件 > 對話 > 推論
```

---

## 📄 `04_New_Chat_Standard_Procedure.md`

```md
# TAITS 新對話標準啟動流程（SOP）

## Step 1
貼上：
「請載入以下 TAITS 專案文件，作為本對話的最高權威，並在此基礎上繼續開發，不得縮水或自行假設。」

## Step 2
貼上：
- TAITS Master Prompt

## Step 3
貼上：
- TAITS_Document_Index.md

## Step 4
依本次任務貼上對應核心文件：
- 架構 → MASTER_ARCHITECTURE
- 策略 → Strategy Universe
- 資料 → DataSources
- 風控 → Risk and Compliance
```

---

## 📄 `05_Governance_and_Interaction_Rules.md`

```md
# TAITS 治理與互動規範

## 一、GitHub 儲存規範
所有要求「存成專案文件」的回覆，必須提供：
1. 檔名
2. 路徑
3. 用途
4. 完整內容

（詳見 TAITS_GitHub_Save_Rules.md）

## 二、小白教學模式
當使用者表示不熟悉操作時，必須切換教學模式，
遵守 TAITS_Beginner_Teaching_Rules.md
```

---

## 📄 `06_Do_and_Do_Not_List.md`

```md
# TAITS 接手者 Do / Do Not 清單

## ✅ 必須做
- 以文件為唯一事實來源
- 維持架構完整性
- 所有輸出給完整版本

## ❌ 禁止
- 簡化策略數量
- 把纏論當成單一策略
- 跳過 Risk / Regime
- 說「之後再說」
```

---

# ✅ 最終確認（重要）

完成以上後，你的 TAITS 專案具備：

* ✔ 新對話 100% 可接手
* ✔ 人類 / AI 都能看懂
* ✔ 架構不會縮水
* ✔ 未來怎麼擴充都不會亂

這在工程上已經是 **「可交棒系統」**。

---
