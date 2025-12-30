# TAITS_GOVERNANCE_STATE｜FREEZE v1.0（Active Integrated）

doc_key：GOVERNANCE_STATE_FREEZE_V1  
治理定位：A｜治理狀態文件（State Authority）  
生效狀態：GOVERNANCE_STATE = Freeze v1.0  
裁決序位：DOCUMENT_INDEX → MASTER_ARCH →（本檔）→（其餘文件；AI 行為仍受 AI_GOV 最高約束）  
變更原則：Only-Add（Freeze v1.0 期間僅可新增封口；不得刪減／覆寫／偷換既有語義）  

> 本檔為「Freeze v1.0」之唯一可引用治理狀態文件（以 doc_key=GOVERNANCE_STATE_FREEZE_V1 為準）。  
> 任何 Active 文件清單/數量/快照僅為 Snapshot，不具裁決效力；可引用性與治理分桶一律回歸 DOCUMENT_INDEX。  

---

## 0. 人類最高裁決者（Owner）之權限定位（與鐵律一致）

- 你（產品負責人/架構裁決者）為 TAITS 的**最高人類裁決者**：可對治理規則、文件版本、流程設計提出/批准變更。  
- 但 TAITS 仍保留不可破壞的「系統保險絲」以確保可落地、可稽核、可合規：  
  1) **Risk / Compliance 最高否決權**（任何交易相關授權與執行，不得繞過否決鏈）。  
  2) **治理裁決序位**（衝突裁決依 DOCUMENT_INDEX → MASTER_ARCH → 本檔）。  
  3) **Freeze v1.0 的變更邊界**（本狀態下僅允許 Only-Add 封口；若需結構性改寫/清理，必須走治理閘門切換到非 Freeze 狀態後執行）。  

> 上述定位確保：你具備最高裁決與變更批准權，但系統仍具備風險/合規/稽核的硬防線，避免「可改一切」被誤解為「可繞過否決/安全機制」。

---

## 1. Canonical Identity（引用端唯一合法身份）

- canonical_doc_key：`GOVERNANCE_STATE_FREEZE_V1`  
- canonical_filename（Index 裁決檔名）：`TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md`  
- physical_filename（本專案內實體檔名）：`TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ACTIVE_CLEAN_INLINEAPPENDIX_20251231.md`  

### 1.1 alias 封口（不得作為引用鍵）
- `GOVERNANCE_STATE`：僅為閱讀助記（mnemonic/alias），**不得作為 ref_doc_key**。  

---

## 2. 最小可稽核引用模板（唯一合法，直接貼用）

凡聲稱「依據 Freeze v1.0」之輸出（含 Evidence/Gate/Audit/UI/Execution）必須同時提供：

- `ref_doc_key = GOVERNANCE_STATE_FREEZE_V1`
- `ref_file = TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md`
- `ref_version = Freeze v1.0 / 251220`
- `ref_section = <章節定位（§ / Heading Path）>`
- `ref_purpose = <用途：gate_check / risk_veto / ui_decision / execution_policy / audit_replay>`
- `ref_notes = <可選：alias/Label 解讀備註>`

缺任一欄位：依 DOCUMENT_INDEX §6 採保守處置（不得形成裁決性輸出；必要時 RETURN/BLOCK）。

---

## 3. Freeze v1.0 變更邊界（Hard Boundary）

### 3.1 Freeze v1.0 允許
- Only-Add：新增封口、補齊引用格式、澄清歧義（不得改寫既有正文條款）。  
- 裁決封口：對「占位字元、示例文字、標籤/alias」造成的歧義，僅能以 Only-Add 方式封口。

### 3.2 Freeze v1.0 禁止
- 刪除/覆寫既有正文條款  
- 以「清理格式」為由回寫改文（除非先依治理閘門切換到非 Freeze 狀態並留痕）

---

## 4. Machine-Readable Override（工具鏈強制讀取）

```yaml
governance_state: FREEZE_V1
canonical:
  doc_key: GOVERNANCE_STATE_FREEZE_V1
  filename: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md"
aliases:
  - GOVERNANCE_STATE   # mnemonic only, not a legal ref_doc_key
deprecated_templates:
  - ref_doc_key: GOVERNANCE_STATE
    status: DEPRECATED
legal_templates:
  - ref_doc_key: GOVERNANCE_STATE_FREEZE_V1
    status: LEGAL
index_authority:
  active_list_source: DOCUMENT_INDEX
  bucket_source: DOCUMENT_INDEX
conflict_policy:
  order: ["DOCUMENT_INDEX", "MASTER_ARCH", "GOVERNANCE_STATE_FREEZE_V1"]
  default: "CONSERVATIVE_DISPOSITION"  # STOP/RETURN/BLOCK where applicable
```

---

## Appendix A｜Only-Add Full Text（Freeze v1.0｜原始補充全文）

> 本附錄為本檔之唯一全文來源（Only-Add）。為避免重複紀錄，主線僅保留單一有效口徑；完整條款以本附錄全文為準。



# TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220
doc_key：GOVERNANCE_STATE_FREEZE_V1  
治理等級：A（Governance State Declaration｜Freeze / Unfreeze 裁決文件）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（Freeze v1.0 生效中）  
版本日期：2025-12-20  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：TAITS_AI_行為與決策治理最終規則全集__251217 / MASTER_ARCH / DOCUMENT_INDEX  
平行參照：MASTER_CANON / ARCH_FLOW / FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DEPLOY_OPS / LOCAL_ENV / DATA_SOURCES / TWSE_RULES / STRATEGY_UNIVERSE / STRATEGY_FEATURE_INDEX / BEGINNER_GUIDE / README  
變更原則：Only-Add（本文件生效期間，所有受約束文件僅可新增，不可刪減／覆寫／偷換語義）  
核心裁決：FREEZE=ON（Freeze v1.0）｜任何衝突以本文件裁決為準  

---
---

# Addendum 2025-12-27｜Only-Add：GOVERNANCE_STATE 內「文件清單/數量」快照化 × Index Gate（DOCUMENT_INDEX）唯一裁決 × 狀態檔引用最小格式（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md（doc_key：GOVERNANCE_STATE）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0（本文件即為狀態宣告載體）  
> 上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+｜Authoritative Index）＋MASTER_ARCH（A）＋MASTER_CANON（A）  
> 平行對齊：README｜Addendum 2025-12-27／PROJECT_PROMPT｜Addendum 2025-12-27／VERSION_AUDIT｜Addendum 2025-12-27  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（建議新增條目：`VA-METADATA_FIX-20251227-0016`）  
> 目的：修補狀態檔（GOVERNANCE_STATE）內若出現之「ACTIVE 文件數量/清單」被誤用為裁決依據的風險；固定：ACTIVE/doc_key/治理等級/版本有效性一律以 DOCUMENT_INDEX 表格裁決為準；並提供狀態檔被引用時的最小引用格式，確保 Freeze v1.0 下的「狀態宣告」可回放、可稽核且不導致治理口徑漂移。

---

## S0. 狀態檔定位（Scope Lock）

本文件（GOVERNANCE_STATE）之唯一合法用途為：
- 宣告當前治理狀態（例如：Freeze v1.0）  
- 宣告 Freeze 期間之行為限制（如 Only-Add、不得結構性變更等）  
- 提供外部文件/新對話在啟動確認時可引用的「狀態依據」

本文件 **不得**：
- 裁決 ACTIVE 文件集合  
- 裁決 doc_key 合法性、治理等級、版本有效性  
- 以本文件內任何「清單/數量」覆蓋 DOCUMENT_INDEX 的 Authoritative Index 表格

---

## S1. Snapshot 不裁決（No Hardcoded ACTIVE Set）

### S1.1 統一裁決：清單/數量一律視為 Snapshot
凡本文件中出現：
- 「ACTIVE 文件數 = X」  
- 「目前共有 X 份文件」  
- 任何列舉文件清單（含 ACTIVE 清單）

一律視為 Snapshot（歷史快照/導覽用途），**不具治理裁決效力**。

### S1.2 唯一裁決來源：Index Gate First
凡涉及：
- ACTIVE 文件集合  
- doc_key 合法性  
- 治理等級 bucket（A+/A/B/C；B+/C+ 的 bucket 化）  
- 版本有效性（version_date / freeze 狀態）

一律以 **DOCUMENT_INDEX 的 Authoritative Index 表格**裁決為準。

---

## S2. 狀態檔引用最小格式（Minimum Legal Citation Format）

### S2.1 強制欄位（缺一視為未引用）
凡任何文件/新對話/稽核記錄引用本狀態檔作為「Freeze v1.0 依據」時，必須至少包含：

- `ref_file`：完整檔名  
- `ref_doc_key`：GOVERNANCE_STATE  
- `ref_version_date`：版本日期（__251220 或等價日期）  
- `ref_section`：章節定位（Freeze 條款段落 / 狀態宣告段落）  
- `audit_anchor`：VERSION_AUDIT 稽核錨點（可先用本批次 `VA-METADATA_FIX-20251227-0016`）

缺任一欄位 → 一律視為「未引用」→ 不得以狀態檔做裁決性輸出依據。

### S2.2 可直接貼用的引用標頭
```text
〔TAITS GOVERNANCE_STATE 引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md
ref_doc_key = GOVERNANCE_STATE
ref_version_date = __251220
ref_section = <Freeze v1.0 狀態宣告段落/章節>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0016
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS GOVERNANCE_STATE 引用標頭〕
```

---

## S3. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫本狀態檔既有任何 Freeze 條款語義。  
- 本文件內任何清單/數量一律視為 Snapshot；治理裁決一律回到 DOCUMENT_INDEX。  
- 缺少必要引用欄位時：依 DOCUMENT_INDEX §6 保守處置，並以 VERSION_AUDIT 留痕。

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）


## 0. 文件定位（Governance State Declaration）

本文件為 TAITS 的「治理狀態宣告」文件，職責僅有一項：

- **裁決 TAITS 目前是否處於 Freeze 狀態，以及 Freeze 對各治理等級文件的變更約束。**

本文件不負責（避免越權）：
- 不定義策略、不定義流程、不定義下單、不定義風控條款細節
- 不改寫母法與上位文件（A+ / A）
- 不提供任何績效、承諾、推論或替代裁決

---

## 1. 治理狀態裁決（State Resolution）

### 1.1 當前狀態（Current State）
- **GOVERNANCE_STATE：FREEZE**
- **版本：v1.0**
- **生效：ON**

### 1.2 Freeze 的制度性意義（Meaning）
Freeze 代表：
- TAITS 已進入「治理穩態」  
- 系統所有關鍵文件與流程需要維持可追溯、可回放、可稽核的一致性  
- **任何變更一律採保守策略：能不動就不動；必須動只允許 Only-Add**

---

## 2. Freeze 影響範圍（Scope）

Freeze v1.0 影響：
- 全系統：Research / Backtest / Simulation / Paper / Live  
- 全文件：所有 A / B / C 等級文件（以 DOCUMENT_INDEX 為裁決基準）  
- 全行為：任何會改變「治理語義」「邊界權限」「否決權」「流程步序」「稽核可回放性」之行為

---

## 3. 變更規則（Change Rules Under Freeze）

### 3.1 A+（Supreme Canon）文件
- **禁止任何變更**
- 若需變更：必須先解除 Freeze（依 §6），且需啟動獨立治理程序（以 DOCUMENT_INDEX 裁決）

A+ 典型文件：
- `TAITS_AI_行為與決策治理最終規則全集__251217`

---

### 3.2 A（Constitutional）文件
- **原則禁止變更**
- 例外僅允許：  
  - 勘誤（typo/標點/不影響語義之格式修正）  
  - Only-Add 附錄（不得改寫既有語義、不得削弱否決、不得改動權力邊界）

A 典型文件：
- `MASTER_ARCH`、`MASTER_CANON`、`RISK_COMPLIANCE`、`EXECUTION_CONTROL` 等（以 DOCUMENT_INDEX 為準）

---

### 3.3 B（Governance / Specification）文件
- **僅允許 Only-Add**
- 嚴格禁止：
  - 刪除任何條款
  - 覆寫任何定義
  - 改寫既有語義
  - 弱化否決權或邊界
  - 以「簡化」名義合併、移除、跳步、縮短流程

B 典型文件：
- `ARCH_FLOW`、`FULL_ARCH`、`UI_SPEC`、`VERSION_AUDIT`、`DEPLOY_OPS`、`DATA_SOURCES`、`TWSE_RULES`、`STRATEGY_UNIVERSE`、`STRATEGY_FEATURE_INDEX`、`DOCUMENT_INDEX` 等（以 DOCUMENT_INDEX 為準）

---

### 3.4 C（Operational / Guide）文件
- **允許補強與增補（Only-Add）**
- 允許：
  - 補足操作步驟
  - 補足示例
  - 補足常見錯誤處理
- 禁止：
  - 引入任何新的治理權力或覆寫上位文件
  - 以操作手冊語氣暗示「可跳過風控/可自動下單/可越權」

C 典型文件：
- `README`、`BEGINNER_GUIDE` 等（以 DOCUMENT_INDEX 為準）

---

## 4. Freeze 期間的硬性門檻（Hard Gates）

Freeze v1.0 期間，任何文件變更（即便是 Only-Add）必須同時滿足：

1. **doc_key 不變且唯一（不得改名換 key 以規避治理）**
2. **引用一致性**：新增內容不得引用 DOCUMENT_INDEX 未收錄的文件作為治理依據  
3. **否決權不弱化**：RISK / Compliance / Kill Switch / Governance Gate 之裁決能力不得被任何方式削弱  
4. **可回放性不破壞**：任何新增內容不得使舊版 Replay 失效或不可比較  
5. **審計可追溯**：必須能在 VERSION_AUDIT 中留下可稽核變更紀錄（格式依 VERSION_AUDIT 裁決）

---

## 5. 違規處置（Violation Handling）

### 5.1 違規定義（Freeze Violation）
以下任一項成立，即構成 Freeze 違規：
- 刪減、覆寫、偷換定義
- 任何形式的「摘要化」導致語義縮減
- 引入未納入 DOCUMENT_INDEX 的治理依據
- 弱化否決權、弱化 Human-in-the-Loop、弱化審計/回放義務
- 以「工程方便」「性能」「回測需要」為由跳過治理要求

### 5.2 處置原則（Default Conservative Action）
- **預設：立即停止變更、撤回提交、保全證據**
- 若變更已影響執行環境：  
  - 依 `DEPLOY_OPS` 與 `EXECUTION_CONTROL` 啟動停機／降級程序（以更高位階文件裁決為準）

---

## 6. 解凍程序（Unfreeze Protocol）

### 6.1 解凍前提
解除 Freeze 必須由「治理狀態文件」裁決，且必須是另一份獨立文件：

- `TAITS_GOVERNANCE_STATE__UNFREEZE_v1.x__YYYYMMDD.md`
- doc_key 必須為：`GOVERNANCE_STATE_UNFREEZE_V1X`（版本細則由 DOCUMENT_INDEX 裁決）

### 6.2 解凍最低要求（不可省略）
解凍文件必須明確載明：
- 解凍原因（Reason）
- 解凍範圍（Scope）
- 解凍期間允許變更的文件列表與等級
- 解凍有效期間（Timebox）
- 解凍後再 Freeze 條件（Re-Freeze Conditions）
- 對 VERSION_AUDIT 的審計輸出要求

---

## 7. 審計輸出（Audit Outputs）

Freeze v1.0 生效期間，必須可被審計的最小證據集合：

- `governance_state = FREEZE_V1`
- `effective_doc = TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220`
- `effective_time = 2025-12-20`
- `scope = TAITS 全系統`
- `restrictions = Only-Add`
- `violation_records[]`（若有）
- `change_ledger_refs[]`（VERSION_AUDIT 引用）

---

## 8. 最終裁決宣告（Final Declaration）

> 自本文件版本生效起，  
> TAITS 進入 **Freeze v1.0**。  
> 所有受本文件約束之文件與行為，僅允許 **Only-Add**。  
> 任何削弱治理、否決權、可回放性與人類主權之行為，視為違規並優先處置。  

（GOVERNANCE_STATE_FREEZE_V1｜Freeze v1.0｜2025-12-20｜ACTIVE）

---

# 【C】GOVERNANCE_STATE｜Addendum 2025-12-28-E（Only-Add）
> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md（doc_key：GOVERNANCE_STATE_FREEZE_V1）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0（本文件即為狀態宣告載體）  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
> 稽核對位：VERSION_AUDIT｜建議新增條目：`VA-METADATA_FIX-20251228-0027`  
> 目的：修補本文件內 Addendum 標頭曾出現之 doc_key 別名，避免被工具鏈誤解析為 doc_key。

---

## E1. DOC_KEY_MISMATCH 封口（Hard Rule）
- 依文件檔頭與 DOCUMENT_INDEX 裁決：本文件唯一合法 doc_key = `GOVERNANCE_STATE_FREEZE_V1`
- 任何內文/附錄/舊 Addendum 若出現 `GOVERNANCE_STATE`：
  - 一律視為閱讀用名稱（alias）
  - 不得作為 doc_key 或引用鍵
- 若下游引用仍使用錯誤 doc_key：視為 `GOV-DOC` 類阻斷條件（依 VERSION_AUDIT Block Conditions 精神）

## E2. 最小引用範本（重申）

```text
ref_doc: TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md
ref_doc_key: GOVERNANCE_STATE_FREEZE_V1
ref_version_date: 2025-12-20
ref_status: ACTIVE
ref_section: <章節/條文定位>
audit_anchor: VA-METADATA_FIX-20251228-0027
```

---
---

# Addendum 2025-12-28｜Only-Add：P0 全閉合（狀態檔引用模板作廢 × 新模板固定 × Alias 封口｜Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md（doc_key：GOVERNANCE_STATE_FREEZE_V1）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
> 稽核對位：VERSION_AUDIT｜建議新增條目：`VA-METADATA_FIX-20251228-0030`  
> 目的：閉合本文件內部「舊引用模板仍使用 GOVERNANCE_STATE」與「doc_key 唯一裁決為 GOVERNANCE_STATE_FREEZE_V1」之自相矛盾；以 Only-Add 方式宣告舊模板作廢（保留歷史），並提供唯一合法新模板。

---

## E3. 舊引用模板作廢宣告（Deprecated｜保留但不得再用）

### E3.1 作廢對象（S2-OLD）
凡本文件內或衍生文件中，引用模板出現下列任一形式：
- `ref_doc_key = GOVERNANCE_STATE`
- `doc_key：GOVERNANCE_STATE`（用於引用欄位）
均屬 **S2-OLD（Deprecated Template）**。

### E3.2 作廢後的法律效果（Hard）
- S2-OLD 模板 **不得**用於任何新產物（Evidence / Audit / UI Trace / Deploy Artifact / Gate Proof）。
- 若出現 S2-OLD：
  - 視為「引用不合法／引用不完整」
  - 依 Gate/Policy 必須 **RETURN（補齊）或 BLOCK（若不可補救）**
  - 不得以「沿用舊文件」或「工具預設」作為通融理由

---

## E4. 唯一合法新模板（S2-NEW｜Canonical）

> 自本 Addendum 起，唯一合法引用模板如下（不得改寫語義；可原封貼用）：

```text
ref_doc = TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md
ref_doc_key = GOVERNANCE_STATE_FREEZE_V1
ref_version_date = 2025-12-20
ref_status = ACTIVE
ref_section = <章節/條文定位>
audit_anchor = VA-METADATA_FIX-20251228-0030
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
```

---

## E5. Alias 封口（Mnemonic ≠ doc_key）

- `GOVERNANCE_STATE`：僅允許作為閱讀用名稱／助記（Mnemonic）  
- 任何引用鍵（ref_doc_key / gate_doc_key / audit_doc_key）**一律必須**使用：`GOVERNANCE_STATE_FREEZE_V1`

---

## E6. Template Precedence（同檔多模板衝突時之處置）

本文件內若同時存在多份引用模板（新舊並存）：
- 一律以「版本日期較新」且明確標記為 **S2-NEW / Canonical** 之模板為唯一合法模板
- 舊模板只保留歷史可讀性，不具「可用於新產物」之法律效力

---

## E7. Machine-Readable Override Block（供工具鏈使用，不改制度）

```yaml
doc_key_resolution:
  authoritative_source: "DOCUMENT_INDEX"
  enforced_doc_key: "GOVERNANCE_STATE_FREEZE_V1"
  name_aliases:
    - "GOVERNANCE_STATE"
  deprecated_templates:
    - "ref_doc_key=GOVERNANCE_STATE"
  hard_rules:
    - "MUST_WRITE_ref_doc_key_AS_GOVERNANCE_STATE_FREEZE_V1"
    - "MUST_TREAT_GOVERNANCE_STATE_AS_ALIAS_ONLY"
```

---

## E8. 版本戳記
- generated_at: 2025-12-28 02:30:24 +0800（Asia/Taipei）

（Addendum 2025-12-28｜Only-Add｜GOVERNANCE_STATE_FREEZE_V1｜P0 全閉合 完）
---

# Addendum 2025-12-28｜Only-Add：S2 Template Hard Banner（防誤抄封口｜Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md（doc_key：GOVERNANCE_STATE_FREEZE_V1）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
> 稽核對位：VERSION_AUDIT｜新增條目：`VA-METADATA_FIX-20251228-0037`  
> 目的：降低人工複製貼上誤用舊模板（S2-OLD）之風險；不改寫任何既有段落，僅追加醒目硬規則指引。

---

## K1. HARD BANNER（不得忽略）

- 本文件內若看見任何舊模板（S2-OLD），包含但不限於：
  - `ref_doc_key = GOVERNANCE_STATE`
  - `doc_key：GOVERNANCE_STATE`（作為引用鍵）
- **一律視為已作廢（Deprecated）**，不得用於任何新產物。

✅ 唯一合法引用模板：請一律使用本文件中已明確標記為 **S2-NEW / Canonical** 的模板（`ref_doc_key = GOVERNANCE_STATE_FREEZE_V1`）。  
（若你無法確認位置：以「版本日期較新」且明示 S2-NEW 的區塊為準。）

---

## K2. 版本戳記
- generated_at: 2025-12-28 02:56:19 +0800（Asia/Taipei）

（Addendum 2025-12-28｜Only-Add｜GOVERNANCE_STATE_FREEZE_V1｜S2 Template Hard Banner 完）
---

## Appendix 2025-12-28｜Only-Add：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md（doc_key：GOVERNANCE_STATE_FREEZE_V1）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 Addendum/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md`
- canonical_doc_key（Index 裁決識別碼）：`GOVERNANCE_STATE_FREEZE_V1`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228K_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=GOVERNANCE_STATE_FREEZE_V1` + `canonical_filename=TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。
