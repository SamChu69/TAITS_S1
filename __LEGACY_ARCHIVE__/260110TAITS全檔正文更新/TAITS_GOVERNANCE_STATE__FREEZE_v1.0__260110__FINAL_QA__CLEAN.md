# TAITS_治理狀態宣告（GOVERNANCE_STATE）

- doc_key：GOVERNANCE_STATE
- 治理等級：A（治理狀態文件｜FREEZE v1.0）
- 適用範圍：TAITS 全專案（治理狀態宣告、是否允許結構性變更、整編/更新作業界線、封存/上線門檻）
- 版本狀態：ACTIVE（單一正確正文版）
- 版本日期：2026-01-10（Asia/Taipei）
- 基線日期：2026-01-10（Asia/Taipei）
- 裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- 平行參照：VERSION_AUDIT／GOVERNANCE_GATE_SPEC／MASTER_CANON
- 正文規則：正文不得混入留痕或對話痕跡；稽核四件套（Changelog／Hash Manifest／Scope／Audit Hand-off）固定置於檔尾「稽核區塊（非正文）」。

---

## 0. 文件定位（State Declaration）

本文件用於宣告 TAITS 目前治理狀態為 **FREEZE v1.0**。  
治理狀態是全專案的「變更邊界開關」：在 FREEZE 期間，以預設保守門檻限制所有會造成語義漂移、結構性改寫、治理位階重排、或未審核擴散的變更。

本文件僅宣告狀態與邊界，不具備改寫裁決序位之權限；若產生衝突，一律以裁決序位上位文件裁決（DOCUMENT_INDEX → MASTER_ARCH → AI_GOV）。

---

## 1. 名詞與範圍定義（Definitions）

### 1.1 治理狀態（Governance State）

「治理狀態」用於描述專案在特定期間允許的變更型態與變更門檻。  
治理狀態的目的在於：在制度穩定性與可演進性之間，提供可審計、可裁決、可追溯的開關。

### 1.2 結構性變更（Structural Change）

在本文件中，下列任一類型屬「結構性變更」：

- 改寫治理位階、裁決序位或其語義（包含把非上位文件納入裁決序位、改動覆蓋規則）
- 改寫 Canonical Flow（L1–L11）的定義、邊界或層級責任（其唯一正文來源為 MASTER_CANON）
- 刪除或覆寫既有制度條文，或以替換方式造成既有語義消失
- 新增/移除 doc_key、重命名 doc_key、改變 ACTIVE 文件集合之裁決來源
- 改動 Gate 的裁決權力配置（例如風控/合規否決權、Gate 封鎖條件、裁決流程分支）
- 改動資安/權限邊界，使執行或資料存取的安全模型弱化
- 改動「封存/上線」的必要條件，或使稽核回放鏈條中斷

### 1.3 非結構性變更（Non-structural Change）

下列類型一般不視為結構性變更（但仍必須可稽核、可追溯）：

- 排版、錯字、段落順序調整（不改語義）
- 同檔去重收斂（保留單一一致版本，不保留被取代正文）
- 正文乾淨化（移除補丁語句、對話痕跡、占位符、重複標頭、格式破損）
- 交付一致化（基線日期對齊、稽核四件套格式統一、Hash Manifest 重算）

---

## 2. FREEZE v1.0 核心規則（Core Rules）

FREEZE v1.0 期間採「預設禁止、例外放行」的保守原則：

1) **不得進行結構性變更**（定義見 §1.2）。  
2) **不得改寫裁決序位**：裁決序位固定為 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。  
3) **不得重複定義 Canonical Flow**：L1–L11 的唯一正文來源為 MASTER_CANON；其他文件僅能承接、不得特別化子集合（包含不得特別化 L9–L11）。  
4) **Risk / Compliance 最高否決權不可被削弱**：任何變更不得在語義或流程上使其否決失效、延後或可被繞過。  
5) **可回放、可稽核、可追溯為硬約束**：任何允許的非結構性變更必須維持 VERSION_AUDIT 所要求的留痕與重現能力。

---

## 3. FREEZE v1.0 允許的變更類型（Allowed Changes）

在 FREEZE v1.0 下，僅允許以下類型之變更（且必須符合 VERSION_AUDIT 與 GOVERNANCE_GATE_SPEC 的門檻）：

### 3.1 正文整編與乾淨化（FINAL QA / Normalize）

允許對 ACTIVE 文件進行：
- 去重收斂（同檔重複內容收斂為單一版本；被取代內容不得留在正文）
- 結構重排（提升可讀性與可維護性；不改語義）
- 清理對話痕跡、補丁語句、占位符、省略符號與格式破損
- 基線日期對齊（本輪基線：2026-01-10）
- 稽核四件套固定化與 Hash Manifest 重算

### 3.2 事故導向的安全修復（Safety Hotfix｜限制性）

若且唯若符合下列條件，允許進行「最小範圍」的安全修復：
- 由 RISK_COMPLIANCE 或同等級治理裁決要求之安全性修復
- 修復目的為避免資產風險、合規風險、資安風險或不可回放風險擴散
- 修復不得引入新語義結構；僅允許以最小變動恢復既有制度可運行性
- 必須在 VERSION_AUDIT 留痕，並可被稽核回放

---

## 4. FREEZE v1.0 禁止的變更類型（Prohibited Changes）

FREEZE v1.0 期間，明確禁止下列變更：

- 任何結構性變更（§1.2）
- 新增/刪除/重命名 doc_key，或改變 ACTIVE 文件集合裁決方式
- 改寫 MASTER_CANON 的層級定義或把 L 層責任轉移到其他文件
- 改寫 RISK_COMPLIANCE 的否決權條文或使其可被繞過
- 改寫 EXECUTION_CONTROL 的執行授權邊界，導致「策略 ≠ 下單」被破壞
- 以摘要方式縮水制度條文，或保留被取代正文（導致混讀）
- 任何無法回放/無法稽核/無法追溯的修改（包含缺少必要引用欄位或缺少 Hash Manifest）

---

## 5. 例外申請與狀態變更（Exception & State Transition）

若確有必要進行結構性變更，必須先變更治理狀態，且遵守：

1) **先變更本文件（GOVERNANCE_STATE）**：以新版本宣告解除或調整 FREEZE 規則。  
2) **變更必須可稽核**：包含 Changelog、Scope、Hash Manifest、Audit Hand-off。  
3) **裁決不得跳階**：任何狀態變更若與上位裁決文件衝突，一律回到裁決序位裁決。  
4) **保守處置**：在狀態變更完成前，維持 FREEZE v1.0 原則。

---

## 6. 封存與上線門檻（Archive & Go-Live Thresholds｜Governance View）

在 FREEZE v1.0 下，任何「對外宣告完成」「可上線」或「可作為長期基線」的里程碑，至少必須滿足：

- DOCUMENT_INDEX 的 ACTIVE 集合可被一致解析，且 doc_key/版本日期/裁決序位一致
- MASTER_ARCH、AI_GOV、MASTER_CANON 已完成 FINAL QA（正文乾淨、無混讀、無 Legacy Snapshot）
- VERSION_AUDIT 的稽核結構可用（含 Hash Manifest 與 Scope）
- Risk/Compliance Gate 的否決權在流程上不可被繞過
- 可回放與可追溯鏈條成立（Evidence → Audit → Replay 的最小鏈條不斷裂）

---

## 7. 與其他文件之邊界（Boundary）

- 本文件不定義 Canonical Flow（L1–L11）；其唯一正文來源為 MASTER_CANON。
- 本文件不定義風控與合規條文；其唯一正文來源為 RISK_COMPLIANCE。
- 本文件不定義 Gate 細則；其唯一正文來源為 GOVERNANCE_GATE_SPEC。
- 本文件不定義版本與稽核資料結構；其唯一正文來源為 VERSION_AUDIT。
- 本文件僅宣告治理狀態與變更邊界；若與上位裁決文件衝突，一律依裁決序位裁決。

---

# 稽核區塊（Audit Section｜非正文）
## 1) Changelog（變更紀錄）
- 2026-01-10：FINAL_QA_NORMALIZE（補齊 FREEZE v1.0 正文為可維護制度文本；清理占位符與不完整段落；統一基線日期與裁決序位口徑；固定稽核四件套；不改寫上位裁決與 Canonical Flow 錨定。）

## 2) Hash Manifest（指紋清單）
- HASH_RULE：SHA-256（UTF-8，LF；Body=本檔「稽核區塊」之前全文，含結尾換行）
- BODY_SHA256：8c02079804daebea8b8a0cb212189337871c656bfee179048a5bd17e0a00593b

## 3) Scope（適用範圍）
- scope_doc_key：GOVERNANCE_STATE
- scope_change_type：FINAL_QA_NORMALIZE（正文乾淨／去占位符／結構與格式正常化／基線日期對齊）
- scope_invariants：
  - 裁決序位維持：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
  - Canonical Flow（L1–L11）之唯一正文來源維持：MASTER_CANON
  - Risk/Compliance 最高否決權不被削弱
  - 不新增結構性變更之權限，不改寫 FREEZE v1.0 的核心禁止邊界（僅明文化與可維護化）

## 4) Audit Hand-off（裁決承接）
- governance_order_applied：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- canonical_flow_anchor：MASTER_CANON（L1–L11）
- note：本檔僅宣告治理狀態與變更邊界；稽核區塊屬非正文。
