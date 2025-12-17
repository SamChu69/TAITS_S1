# TAITS Data Layer Documentation (S2)

本資料夾為 **TAITS S2：Data Layer（資料層）** 的官方文件入口。  
此處文件定義 TAITS 內部資料的**唯一標準、治理規則與端到端流程**，其權威性高於任何策略、Agent 或 AI 建議。

> ⚠️ 若資料實作與本資料夾文件衝突，**以文件為準**。

---

## 🎯 Data Layer 的一句話目標

> **在不下單的前提下，提供可治理、可稽核、可重現的研究資料底座，  
> 為 Regime / Agents / Backtest 提供一致且可信的資料輸入。**

---

## 🧱 核心原則（不可違反）

- 官方資料優先，多層 fallback（不可靜默切換）
- Schema 固定，擴充需版本治理
- Validator 可否決資料（OK / WARN / BLOCK）
- Audit 必須可追溯（來源、參數、時間、hash、落盤）
- Strategy / Agent **不得**指定資料來源
- Risk / Compliance 具有最高否決權

---

## 📚 文件總覽（由高至低權威）

```

docs/data/
├── README.md                               ← 本檔（入口）
├── TAITS_DataBundle_and_Schema.md          ← 內部資料語言（最高優先）
├── TAITS_DataSource_Priority_and_Fallback.md ← 官方優先與切換規則
├── TAITS_Data_Validation_Rules.md          ← 資料品質 OK/WARN/BLOCK
└── TAITS_DataLayer_Architecture.md         ← 模組邊界與資料流

```

---

## 🧭 建議閱讀順序（S2 必讀）

1. **TAITS_DataBundle_and_Schema.md**  
   - 定義 TAITS 內部資料的「語言」
   - 所有資料最終必須符合此 Schema 與 DataBundle 格式

2. **TAITS_DataSource_Priority_and_Fallback.md**  
   - 定義資料來源的官方優先序
   - 明確 fallback 條件與稽核要求

3. **TAITS_Data_Validation_Rules.md**  
   - 定義資料品質的硬規則
   - Validator 可直接 BLOCK 資料

4. **TAITS_DataLayer_Architecture.md**  
   - 定義模組責任邊界與端到端資料流
   - 規範 Orchestrator 與 Data Layer 的介面

> 📌 實作前若未完整理解上述文件，視為流程違規。

---

## 🧩 Data Layer 模組地圖（概念）

- **DataPolicyEngine**：資料來源決策（官方優先 / fallback）
- **Connector**：資料取用（來源專用）
- **Normalizer**：欄位與語意一致化
- **Validator**：品質檢核（OK/WARN/BLOCK）
- **CacheManager**：落盤與 hash（重現性）
- **AuditTrail**：稽核證據鏈
- **DataBundleBuilder**：統一輸出 DataBundle

> 各模組責任與禁止事項，請以 Architecture 文件為準。

---

## ✅ S2 Research 的最小成功判準（Acceptance）

在 `RESEARCH` 模式下，Data Layer 必須能：

- 產出至少一個 `DataBundle`
- 明確標示使用的資料來源（source）
- 產出 ValidationReport（OK/WARN/BLOCK）
- 產出 AuditRecord（含 params / hash / cache_path 或原因）
- 在資料不可用時，**明確 BLOCK 或啟用 fallback（可查）**

---

## 🔒 與 Risk / Compliance 的關係

- Data Validation ≠ 風控，但皆可否決
- 若 Audit 缺失關鍵欄位（來源、hash、參數），Risk/Compliance 可直接 BLOCK
- S2 僅研究；任何接近交易的需求需另立文件並經核准

---

## ✍️ 文件新增與變更規則（Data Layer）

- 新增 dataset 類型必須：
  - 定義 schema
  - 更新本 README
  - 標註版本影響
- 不得弱化既有 Validation 或 Source Priority 規則
- 破壞性變更需提升 Major 版本並附 Migration 說明

---

## 📌 變更紀錄

- v1.0.0：建立 Data Layer 子索引，完成 S2 文件治理入口。
```

---
