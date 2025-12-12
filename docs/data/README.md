# TAITS Documentation Hub

歡迎進入 **TAITS – Taiwan Alpha Intelligence Trading System** 文件中心。

本資料夾為 TAITS 的 **唯一官方文件治理入口**，所有架構、資料、風控、策略、流程規範，皆以此處文件為最高依據。

> ⚠️ 若文件內容與程式碼實作衝突，以文件為準（文件即規格）。

---

## 📚 文件治理總原則（必讀）

- 策略 ≠ 下單
- Agent ≠ 策略
- AI ≠ 唯一真理
- **Regime 高於單一訊號**
- **Risk / Compliance 具有最高否決權**
- 官方資料優先，多層 fallback
- 架構需可長期演進、可擴充、不縮水

---

## 🗂 文件結構總覽

```

docs/
├── README.md                      ← 文件入口（本檔）
│
├── architecture/                  ← 系統總架構與流程
│   ├── TAITS_MASTER_ARCHITECTURE.md
│   ├── TAITS_Architecture_and_Flow.md
│   └── TAITS_System_Design_Principles.md
│
├── data/                          ← S2 資料層（Data Layer）
│   ├── TAITS_DataBundle_and_Schema.md
│   ├── TAITS_DataSource_Priority_and_Fallback.md
│   ├── TAITS_Data_Validation_Rules.md
│   └── TAITS_DataLayer_Architecture.md
│
├── strategy/                      ← 策略宇宙（不等於下單）
│   └── TAITS_Strategy_Universe_Complete.md
│
├── risk/                          ← 風控與合規（最高否決權）
│   └── TAITS_Risk_and_Compliance.md
│
├── ui/                            ← UI / UX 規範
│   └── TAITS_UI_Spec.md
│
└── ops/                           ← 操作與治理（Git / Onboarding）
├── TAITS_GitHub_Save_Rules.md
└── TAITS_Beginner_Teaching_Rules.md

```

---

## 🧭 建議閱讀順序（依階段）

### 🔹 新接手 / 新 AI（必讀順序）
1. `docs/README.md`（本檔）
2. `architecture/TAITS_MASTER_ARCHITECTURE.md`
3. `risk/TAITS_Risk_and_Compliance.md`
4. `architecture/TAITS_Architecture_and_Flow.md`

---

### 🔹 S1：系統骨架（Bootstrap）
- 系統入口與流程：
  - `architecture/TAITS_Architecture_and_Flow.md`
- Git 與文件治理：
  - `ops/TAITS_GitHub_Save_Rules.md`

---

### 🔹 S2：資料層（Data Layer，僅 Research）
**閱讀順序非常重要：**

1. `data/TAITS_DataBundle_and_Schema.md`  
   → 內部資料語言與資料包格式（最高優先）
2. `data/TAITS_DataSource_Priority_and_Fallback.md`  
   → 官方優先與 fallback 決策規則
3. `data/TAITS_Data_Validation_Rules.md`  
   → 資料品質 OK / WARN / BLOCK 規範
4. `data/TAITS_DataLayer_Architecture.md`  
   → 模組邊界與端到端資料流

> 📌 任何資料實作若違反上述文件，視為系統錯誤。

---

### 🔹 S3（未來）：Regime / Agents / Execution
- Regime Engine（市場狀態）
- Agent 協作（分析 ≠ 下單）
- Execution 僅在 Compliance 核准後啟用

> ⚠️ S3 相關文件未齊備前，不得實作下單邏輯。

---

## 🏛 文件權威等級（由高至低）

1. **Risk / Compliance**
2. **Master Architecture**
3. **Data Layer（Schema / Policy / Validation）**
4. **System Architecture & Flow**
5. Strategy / Agent 說明文件
6. UI / UX 規範
7. 操作說明（Ops）

---

## ✍️ 文件新增與修改規則

- 新文件必須放在正確分類資料夾
- 必須在本 README 更新目錄與說明
- 不得弱化或推翻高權威文件
- 重大變更需標註版本與影響範圍

---

## 🎯 本 README 的角色

- TAITS 文件的 **入口**
- 文件治理的 **導航地圖**
- AI / 人類接手的 **第一理解點**
- 防止架構與實作失控的 **護欄**

---

## 📌 變更紀錄

- v1.0.0：建立 TAITS Docs Hub，完成 S1 / S2 文件治理索引。
```
