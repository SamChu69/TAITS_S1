# 10_canonical_layer_l1_l3__Canonical層級L1–L3定義.md
doc_key：CANONICAL_LAYER_L1_L3（工程拆解對位：Batch 2｜Canonical Definition）  
工程類型：Canonical Definition（定義層）  
治理前提：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
Canonical 來源允許：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX（皆須為 ACTIVE）  
版本狀態：ENGINEERING_TRANSLATION（不具新增治理效力；僅做原文定義結構化轉譯）

<!--
SOURCE_TAG
Canonical 來源（ACTIVE）：
- TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md（doc_key=MASTER_ARCH）
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md（doc_key=MASTER_CANON）
- TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251219.md（doc_key=DOCUMENT_INDEX）
原文範圍：
- MASTER_CANON：§2（L1–L11 Canonical Flow）之 L1/L2/L3 段落；§3（5 Axioms）之 Layer Isolation / Forward-only；§4（多模式一致性 Invariant）
- MASTER_ARCH：全文中「Only-Add / 不可跳層 / 證據可回放 / 語義不可偷換」之定義段落
- DOCUMENT_INDEX：§1（Hard Laws：Only-Add / 無審計＝未發生 / Index 裁決）、§2（doc_key）、§4（ACTIVE 唯一性）
-->

---

## 0. 文件定位（Definition Scope）

本工程檔定義 Canonical Flow 之 **L1–L3**（資料取得 → 正規化 → 狀態快照）三層：
- 僅輸出：名詞/實體定義、枚舉、Schema/欄位骨架、State/Lifecycle 語義、禁止事項（原文明示）
- 不輸出：任何策略邏輯、風控裁決細則、下單/執行實作、UI 行為或技術細節 

---

## 1. L1｜Data Source（資料取得）— 定義

### 1.1 Layer 定義
- `layer_code`：`L1_DATA_SOURCE`
- `layer_name_zh`：資料取得
- `layer_name_en`：Data Source
- `purpose`（目的）：取得官方/授權資料，形成 Raw Data。 :contentReference[oaicite:1]{index=1}

### 1.2 I/O 定義（最小集合）
- `input`：無（External Pull / Ingest 觸發不屬於本檔範圍）
- `output`：`RawData` :contentReference[oaicite:2]{index=2}

### 1.3 禁止事項（原文明示）
- `L1_PROHIBIT_NON_OFFICIAL_ADJUDICATION`：禁止以非官方裁決制度。 :contentReference[oaicite:3]{index=3}
- `L1_PROHIBIT_SINGLE_SOURCE_SINGLE_TRUTH`：禁止單一來源作唯一依據；必須設計 fallback。 :contentReference[oaicite:4]{index=4}

### 1.4 核心實體定義（Entities）

#### 1.4.1 RawData（原始資料）
- 定義：由資料來源取得、尚未正規化之原始資料集合；其語義可能仍依來源而異。 :contentReference[oaicite:5]{index=5}

#### 1.4.2 Source（資料來源）
- 定義：一個具可識別身份、可追溯入口、可被版本化引用之資料供給者（官方/授權/第三方僅作 fallback）。 

### 1.5 L1 最小證據欄位（Schema / Fields）
> 目的：確保後續 L2 能建立 provenance 與審計可追溯；本節僅定義欄位，不定義實作。 

#### 1.5.1 RawDataRecord（最小欄位，不可縮減）
- `source_id`
- `captured_at`
- `raw_payload_ref`
- `hash_manifest_ref`（或等價不可否認性引用）
- `schema_hint`（若未知則標記 unknown，不得假定）
- `notes_ref`（僅供追溯；不得作為裁決） :contentReference[oaicite:8]{index=8}

---

## 2. L2｜Normalization（資料清洗與標準化）— 定義

### 2.1 Layer 定義
- `layer_code`：`L2_NORMALIZATION`
- `layer_name_zh`：資料清洗與標準化
- `layer_name_en`：Normalization
- `purpose`（目的）：將 Raw Data 轉為可比較、可回放的 Canonical 格式。 :contentReference[oaicite:9]{index=9}

### 2.2 I/O 定義（最小集合）
- `input`：`RawData`
- `output`：`CanonicalData` :contentReference[oaicite:10]{index=10}

### 2.3 禁止事項（原文明示）
- `L2_PROHIBIT_SILENT_IMPUTATION`：禁止隱性補值。 :contentReference[oaicite:11]{index=11}
- `L2_PROHIBIT_MODEL_GUESS_AS_MISSING_REPLACEMENT`：禁止以模型猜測取代缺值（除非明確標記並可追溯）。 :contentReference[oaicite:12]{index=12}

### 2.4 核心實體定義（Entities）

#### 2.4.1 CanonicalData（正規化資料）
- 定義：已轉換為 TAITS 可比較、可回放、可追溯之統一語義格式的資料。 :contentReference[oaicite:13]{index=13}

#### 2.4.2 Normalization（正規化）
- 定義：從來源語義映射到 Canonical 語義之處理；必須保留映射與版本參照以避免語義偷換。 

### 2.5 L2 最小欄位（Schema / Fields）
> 僅定義「必須可追溯/可回放」所需之欄位骨架，不定義欄位細表。 

#### 2.5.1 CanonicalDataRecord（最小欄位，不可縮減）
- `canonical_schema_id`
- `normalization_ruleset_version`
- `field_map_ref`（來源欄位 → canonical 欄位）
- `quality_flags_ref`（品質旗標引用）
- `source_snapshot_ref`（引用 L1 的抓取快照證據）
- `canonical_payload_ref`
- `hash_manifest_ref`
- `captured_at`
- `asof_timestamp` :contentReference[oaicite:16]{index=16}

---

## 3. L3｜Snapshot & State（狀態快照）— 定義

### 3.1 Layer 定義
- `layer_code`：`L3_SNAPSHOT_STATE`
- `layer_name_zh`：狀態快照
- `layer_name_en`：Snapshot & State
- `purpose`（目的）：建立「當下市場狀態」快照，且必須可回放。 :contentReference[oaicite:17]{index=17}

### 3.2 I/O 定義（最小集合）
- `input`：`CanonicalData`
- `output`：`Snapshot` + `StateCache` :contentReference[oaicite:18]{index=18}

### 3.3 禁止事項（原文明示）
- `L3_PROHIBIT_MEMORY_ONLY`：禁止只存在記憶體（必須可回放、可重建引用）。 :contentReference[oaicite:19]{index=19}
- `L3_PROHIBIT_NO_VERSION_REF`：禁止缺少 `version_ref`。 :contentReference[oaicite:20]{index=20}

### 3.4 核心實體定義（Entities）

#### 3.4.1 Snapshot（快照）
- 定義：在特定時間點（as-of）封存的市場狀態資料集合；後續層的分析/證據必須以 Snapshot 為輸入，以確保可回放。 :contentReference[oaicite:21]{index=21}

#### 3.4.2 StateCache（狀態快取）
- 定義：與 Snapshot 關聯之狀態緩存，用於維持流程一致性；其存在不得取代快照之可回放性要求。 :contentReference[oaicite:22]{index=22}

#### 3.4.3 version_ref（版本引用）
- 定義：能指向當次使用之治理文件/規則/資料結構版本（至少可追溯至 doc_key 與版本狀態），以支援審計與回放重建。 

### 3.5 L3 最小欄位（Schema / Fields）
> 僅定義欄位骨架；不定義存放介質/技術方案。 

#### 3.5.1 SnapshotRecord（最小欄位，不可縮減）
- `snapshot_id`
- `asof_timestamp`
- `canonical_data_refs[]`（指向 L2 輸出）
- `state_cache_ref`
- `version_ref_map`（文件/規則/Schema 的版本映射引用）
- `hash_manifest_ref`
- `replay_bundle_hint`（可為 ref 或 key；不得為空） 

---

## 4. 跨層不變公理對位（Axioms Mapping｜Definition Only）

> 本節僅做「定義對位索引」，不新增任何條款。 :contentReference[oaicite:26]{index=26}

- `AXIOM_FORWARD_ONLY`：適用 L1–L3（不得回寫修正上游輸出）。 :contentReference[oaicite:27]{index=27}  
- `AXIOM_LAYER_ISOLATION`：適用 L1–L3（不得越權產出 L4+ 語義）。 :contentReference[oaicite:28]{index=28}  
- `AXIOM_EVIDENCE_FIRST`：L1–L3 是 Evidence 上游基礎；必須保證 provenance/版本/可回放，才能支撐 L5+ 的裁決鏈。   

---

## 5. 最終鎖定聲明（Final Lock｜State）

本檔為 L1–L3 定義層工程轉譯，僅允許 Only-Add（新增原文已明示但尚未收錄之定義/欄位/枚舉），不得刪減、不得覆寫、不得偷換語義；若與上位文件衝突，一律以上位（DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON）之裁決順序為準。 

---

# ✅ 本檔輸出結束（Batch 2｜第 4/7 檔：10）
