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
