# 13_document_governance_hierarchy__文件治理位階與裁決順序.md
doc_key：DOCUMENT_GOVERNANCE_HIERARCHY（工程拆解對位：Batch 2｜Canonical Definition）  
工程類型：Canonical Definition（定義層）  
治理前提：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
Canonical 來源允許：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX（皆須為 ACTIVE）  
版本狀態：ENGINEERING_TRANSLATION（不具新增治理效力；僅做原文定義結構化轉譯）

<!--
SOURCE_TAG
Canonical 來源（ACTIVE）：
- TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251219.md（doc_key=DOCUMENT_INDEX）
- TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md（doc_key=MASTER_ARCH）
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md（doc_key=MASTER_CANON）
原文範圍：
- DOCUMENT_INDEX：全文（治理等級、裁決順序、doc_key、ACTIVE 規則、衝突處理、引用規則）
- MASTER_ARCH：全文中「上位約束 / 鐵律 / Only-Add / 不得偷換語義」之定義段落
- MASTER_CANON：全文中「Canonical 法律地位 / 衝突裁決聲明」之定義段落
-->

---

## 0. 文件定位（Definition Scope）

本工程檔將「文件治理位階與裁決順序」以定義層形式固定化，目的為：
- 讓任何工程/對話/模組在遇到文件衝突或引用爭議時，可用一致的 **治理名詞、枚舉、狀態與最小欄位** 回答「誰說了算」。
- 本檔僅做定義轉譯：不新增制度、不補推論、不提供操作流程或實作細節。

---

## 1. 核心名詞定義（Definitions）

### 1.1 Governance Document（治理文件）
- 定義：被 DOCUMENT_INDEX 收錄且標示治理等級與狀態之文件；其內容可作為 TAITS 裁決依據（依其治理等級與狀態）。

### 1.2 Canonical Document（Canonical 文件）
- 定義：承載 TAITS Canonical Flow（L1–L11）、核心憲法語義、或治理裁決秩序之文件集合；其法律地位高於一般工程說明或對話內容。

### 1.3 DOCUMENT_INDEX（文件索引與治理對照表）
- 定義：全系統文件治理的「唯一索引來源」；負責定義 doc_key、治理等級、文件狀態、裁決順序與衝突處理規則。

### 1.4 doc_key（文件身份識別碼）
- 定義：每一份治理文件的唯一身份鍵；用於版本控管、審計追溯、引用定位與 ACTIVE 唯一性約束。

### 1.5 ACTIVE（治理生效狀態）
- 定義：代表該文件版本在當下具有治理效力，可被系統/人類/AI 引用作為裁決依據。

### 1.6 Freeze（治理凍結狀態）
- 定義：治理狀態鎖定；Only-Add 生效；不得進行刪減/覆寫/偷換語義的變更。

### 1.7 Only-Add（只可新增）
- 定義：治理有效文件的唯一合法演進方式；任何刪減、覆寫、語義縮減、摘要化造成語義缺失皆屬違規。

---

## 2. 治理等級（Governance Level）定義（Enums）

> 本節僅將 DOCUMENT_INDEX 所定義之治理位階，以枚舉形式結構化，供引用與審計一致性使用。

### 2.1 GovernanceLevel（枚舉）
- `LEVEL_A_PLUS`：A+（最高母法）
- `LEVEL_A`：A（母體／憲法級）
- `LEVEL_B`：B（治理／制度級）
- `LEVEL_C`：C（操作／啟動級）
- `LEVEL_NON_GOV`：Non-Governance（非治理文件；不得作為裁決依據）

### 2.2 GovernanceLevel 語義（Definition Notes）
- `LEVEL_A_PLUS`：最高裁決來源；其規則可否決一切下位內容。
- `LEVEL_A`：憲法級治理；在非 A+ 衝突時具最高裁決力。
- `LEVEL_B`：制度級治理；不得推翻 A+/A，但可補充具體制度範圍。
- `LEVEL_C`：操作指引；不得推翻 A+/A/B，僅作流程或使用說明。
- `LEVEL_NON_GOV`：工程說明、對話、備忘等；不具治理效力。

---

## 3. 文件狀態（Document Status）定義（Enums）

### 3.1 DocumentStatus（枚舉）
- `STATUS_ACTIVE`
- `STATUS_FREEZE`
- `STATUS_DEPRECATED`
- `STATUS_ARCHIVED`
- `STATUS_DRAFT`
- `STATUS_UNKNOWN`

### 3.2 DocumentStatus 語義（Definition Notes）
- `STATUS_ACTIVE`：可引用、可裁決。
- `STATUS_FREEZE`：在 Freeze v1.0 下，仍可引用裁決，但變更受 Only-Add 嚴格限制（不得刪改語義）。
- `STATUS_DEPRECATED`：不得作為最新裁決依據（除非 Index 明示仍具效力的例外，但本檔不補任何例外條款）。
- `STATUS_ARCHIVED`：封存歷史用途，不作裁決依據。
- `STATUS_DRAFT`：草案，除非 Index 明示可裁決，否則不具裁決效力。
- `STATUS_UNKNOWN`：狀態不明；不得用於裁決。

---

## 4. 裁決順序（Adjudication Order）定義（Enums）

> 裁決順序用於「文件衝突」或「引用權威爭議」的最終決定。

### 4.1 AdjudicationOrder（枚舉｜固定序）
- `ORDER_1_DOCUMENT_INDEX`
- `ORDER_2_MASTER_ARCH`
- `ORDER_3_AI_GOVERNANCE_RULESET`（AI 行為與決策治理最終規則全集）
- `ORDER_4_MASTER_CANON`
- `ORDER_5_LOWER_GOV_DOCS`（其餘 B/C 文件依 Index 設定）

> 註：本檔僅做「順序枚舉化」，不展開各文件內部條款。

### 4.2 裁決原則（Definition Notes）
- 衝突出現時：以上位順序先決。
- 下位文件不得推翻上位文件。
- 若未列入 Index：視為 Non-Governance，不得作為裁決依據。

---

## 5. 覆蓋/衝突規則（Override & Conflict Rules）定義（Schema）

### 5.1 ConflictType（衝突類型｜Enum）
- `CONFLICT_SEMANTIC`（語義衝突）
- `CONFLICT_SCOPE`（範圍衝突）
- `CONFLICT_VERSION`（版本衝突）
- `CONFLICT_STATUS`（狀態衝突）
- `CONFLICT_REFERENCE`（引用合法性衝突）
- `CONFLICT_UNKNOWN`

### 5.2 ConflictResolutionOutcome（處置結果｜Enum）
- `OUTCOME_APPLY_SUPERIOR`（採用上位文件）
- `OUTCOME_INVALIDATE_INFERIOR`（下位內容無效）
- `OUTCOME_REQUIRE_INDEX_CLARIFICATION`（需以 Index 釐清；在釐清前不得裁決）
- `OUTCOME_STOP_USE`（停止使用該引用/結論）

### 5.3 ConflictRecord（最小欄位，不可縮減）
- `conflict_id`
- `conflict_type`（ConflictType）
- `claim_a_doc_key`
- `claim_a_version_ref`
- `claim_b_doc_key`
- `claim_b_version_ref`
- `adjudication_order_applied`（AdjudicationOrder）
- `resolution_outcome`（ConflictResolutionOutcome）
- `resolution_basis_ref`（章節定位引用；不得空泛描述）
- `created_at`
- `hash_manifest_ref`

---

## 6. 引用合法性（Citation Legality）定義（Schema）

### 6.1 CitationLegality（引用合法性｜Enum）
- `CITE_OK_ACTIVE`
- `CITE_OK_FREEZE_ACTIVE`
- `CITE_INVALID_NOT_IN_INDEX`
- `CITE_INVALID_NOT_ACTIVE`
- `CITE_INVALID_STATUS_UNKNOWN`
- `CITE_INVALID_VERSION_UNRESOLVED`

### 6.2 CitationRecord（最小欄位，不可縮減）
- `citation_id`
- `doc_key`
- `doc_title`
- `governance_level`（GovernanceLevel）
- `document_status`（DocumentStatus）
- `version_ref`
- `section_ref`（可追溯章節定位）
- `legality`（CitationLegality）
- `checked_at`

---

## 7. ACTIVE 唯一性（Active Uniqueness）定義

### 7.1 ActiveUniquenessRule（定義）
- 定義：同一 `doc_key` 在同一時間範圍內僅允許 **一份**文件版本為 `STATUS_ACTIVE`；若存在多份 ACTIVE，視為治理異常，需以 Index 規則處理；在異常解除前，相關引用不得作裁決依據。

### 7.2 ActiveSetRecord（最小欄位，不可縮減）
- `doc_key`
- `active_version_ref`
- `effective_from`
- `effective_to`（若未知則標記 unknown，不得臆測）
- `hash_manifest_ref`

---

## 8. Freeze v1.0 下之變更語義（Only-Add Semantics）

### 8.1 ChangeType（變更類型｜Enum）
- `CHANGE_ONLY_ADD`
- `CHANGE_DELETE`（禁止）
- `CHANGE_OVERWRITE`（禁止）
- `CHANGE_SEMANTIC_SHIFT`（禁止）
- `CHANGE_SUMMARY_SHRINK`（禁止）

### 8.2 OnlyAddChangeRecord（最小欄位，不可縮減）
- `change_id`
- `target_doc_key`
- `base_version_ref`
- `new_version_ref`
- `change_type`（必須為 CHANGE_ONLY_ADD）
- `added_sections_ref`（新增段落定位）
- `justification_ref`（僅引用上位文件依據；不得臆測）
- `created_at`
- `hash_manifest_ref`

---

## 9. 最終鎖定聲明（Final Lock｜State）

本檔為「文件治理位階與裁決順序」之定義層工程轉譯，在 GOVERNANCE_STATE = Freeze v1.0 下：
- 僅允許 Only-Add（新增 Index 原文已明示但尚未收錄之定義/枚舉/欄位）
- 禁止刪減、覆寫、偷換語義、摘要化導致語義縮減
- 發生衝突時，以裁決順序（AdjudicationOrder）先決

---

# ✅ 本檔輸出結束（Batch 2｜第 7/7 檔：13）
