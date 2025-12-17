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

# 【TAITS 核心文件全覽索引（12 份）｜從開始到落地】
## 版本：v2025-12-16
## 性質：Only-Add（追加，不覆蓋既有內容）

本章節用來回答一個關鍵問題：

> 為什麼是這 12 份？  
> 它們是否真的涵蓋 TAITS「從資料進來 → 你做決定」的全部流程？

答案是：**是，而且每一份都不可省略。**

---

## 文件總覽（高層對照）

| 編號 | 檔名 | 核心角色 |
|---|---|---|
| 01 | TAITS_MASTER_ARCHITECTURE.md | 母體原則與最高設計約束 |
| 02 | TAITS_Architecture_and_Flow.md | 資料與決策流程圖 |
| 03 | TAITS_DataSources_Universe.md | 所有資料從哪來、怎麼用 |
| 04 | TAITS_Strategy_Universe_Complete.md | 策略宇宙與用途定義 |
| 05 | TAITS_Risk_and_Compliance.md | 最高否決與合規鐵律 |
| 06 | TAITS_UI_Spec.md | 你看到什麼、為什麼 |
| 07 | TAITS_Full_System_Architecture.md | 10 層主架構落地藍圖 |
| 08 | TAITS_Document_Index.md | 文件治理與完整性說明 |
| 09 | TAITS_Strategy_Feature_Index.md | 策略 / 指標 / 特徵全集索引 |
| 10 | TAITS_Execution_and_Control.md | 執行邊界與人工控制 |
| 11 | TAITS_Versioning_and_Audit.md | 版本 / 回溯 / 審計 |
| 12 | TAITS_Deployment_and_Operation.md | 落地、維運與實務 |

---

## 逐檔存在理由（不可刪減）

### 01｜TAITS_MASTER_ARCHITECTURE.md
**為什麼存在**
- 定義不可動搖的系統鐵律
- 防止後續「偷改精神」

**如果沒有**
- 架構會被慢慢改歪
- 新人或新 AI 會誤解系統本質

---

### 02｜TAITS_Architecture_and_Flow.md
**為什麼存在**
- 回答「資料怎麼走、判斷怎麼產生」

**如果沒有**
- 只剩名詞，沒有運作方式

---

### 03｜TAITS_DataSources_Universe.md
**為什麼存在**
- 防止「資料從哪來？通靈嗎？」

**如果沒有**
- 系統不可審計
- 官方與非官方界線模糊

---

### 04｜TAITS_Strategy_Universe_Complete.md
**為什麼存在**
- 明確區分：策略 / 方法論 / 觀察

**如果沒有**
- 期貨會被誤用來下期貨
- 方法論會被誤當買賣點

---

### 05｜TAITS_Risk_and_Compliance.md
**為什麼存在**
- 確保任何時候「活下來優先」

**如果沒有**
- 所有策略最終都會變成賭博

---

### 06｜TAITS_UI_Spec.md
**為什麼存在**
- 你必須看得懂、而不是相信黑箱

**如果沒有**
- 系統變成不可控 AI

---

### 07｜TAITS_Full_System_Architecture.md
**為什麼存在**
- 把前面所有文件整合成一張全圖

**如果沒有**
- 文件彼此正確，但整體看不懂

---

### 08｜TAITS_Document_Index.md
**為什麼存在**
- 防止文件爆炸後失控
- 定義「什麼是完整」

---

### 09｜TAITS_Strategy_Feature_Index.md
**為什麼存在**
- 讓新對話、新人、新 AI
  能「一次看到全部工具箱」

---

### 10｜TAITS_Execution_and_Control.md
**為什麼存在**
- 明確「策略 ≠ 自動下單」
- 保留你最後決定權

---

### 11｜TAITS_Versioning_and_Audit.md
**為什麼存在**
- 任何一次修改都能追溯
- 防止「改了但沒人知道」

---

### 12｜TAITS_Deployment_and_Operation.md
**為什麼存在**
- 讓系統真的能跑、能維護
- 不只停在紙上談兵

---

## 覆蓋審計結論（重點）

- ✅ 從資料 → 特徵 → 證據 → 狀態 → 風控 → 策略 → 治理 → UI → 人
- ✅ 沒有單點黑箱
- ✅ 沒有未定義來源
- ✅ 沒有越權下單

> **這 12 份，就是 TAITS 從開始到落地的完整母體。**

---

# 【End of TAITS_Document_Index 追加章節】

