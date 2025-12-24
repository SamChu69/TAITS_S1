# 09_canonical_flow_overview__Canonical流程總覽.md
doc_key：CANONICAL_FLOW_OVERVIEW（工程拆解對位：Batch 2｜Canonical Definition）  
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
- MASTER_CANON：§1（法律地位與使用規則）、§2（L1–L11 Canonical Flow 全文）、§3（5 Axioms）、§4（多模式一致性 Invariant / 可變項）、§5（Evidence 法律地位）、§6（Veto 法律地位）
- MASTER_ARCH：全文中「不可跳層 / 分層隔離 / 三權分立 / 人類主權 / Risk&Compliance 最高否決」之定義段落
- DOCUMENT_INDEX：§1（Hard Laws）、§3（治理等級與覆蓋規則）、§4（ACTIVE 唯一性）
-->

---

## 0. 文件定位（Definition Scope）

本工程檔用於把 **MASTER_CANON 所定義之 Canonical Flow（L1–L11）** 做「可引用的定義總覽」：
- 僅包含：名詞/實體定義、枚舉、狀態、欄位骨架、生命週期語義
- 不包含：策略邏輯、風控裁決細則、下單/執行實作、UI 行為或技術細節 

---

## 1. Canonical Flow（唯一合法交易生成路徑）定義

### 1.1 Canonical Flow（定義）
- 定義：TAITS 的唯一合法交易生成路徑，固定由 L1 至 L11 順序組成；任何人、任何 Agent、任何模組不得以效率或績效為由跳層或越權。 

### 1.2 Forward-only（定義）
- 定義：流程僅允許「前進」或「中止/退回（依 Gate 語義）」；不得以隱性回寫方式修正上游輸出。 :contentReference[oaicite:2]{index=2}

---

## 2. Canonical Layer 枚舉與命名（Enums）

### 2.1 CanonicalLayerCode（枚舉）
- `L1_DATA_SOURCE`
- `L2_NORMALIZATION`
- `L3_SNAPSHOT_STATE`
- `L4_ANALYSIS`
- `L5_EVIDENCE`
- `L6_REGIME`
- `L7_RISK_COMPLIANCE`
- `L8_STRATEGY_RESEARCH`
- `L9_GOVERNANCE_GATE`
- `L10_HUMAN_DECISION`
- `L11_EXECUTION_CONTROL` :contentReference[oaicite:3]{index=3}

### 2.2 LayerName（中英對照）
| LayerCode | 中文名 | 英文名 |
|---|---|---|
| L1_DATA_SOURCE | 資料取得 | Data Source |
| L2_NORMALIZATION | 資料清洗與標準化 | Normalization |
| L3_SNAPSHOT_STATE | 狀態快照 | Snapshot & State |
| L4_ANALYSIS | 分析層 | Analysis |
| L5_EVIDENCE | 證據層 | Evidence |
| L6_REGIME | 市場狀態判定 | Regime |
| L7_RISK_COMPLIANCE | 風險與合規最高否決 | Risk & Compliance |
| L8_STRATEGY_RESEARCH | 策略與研究（提案） | Strategy & Research |
| L9_GOVERNANCE_GATE | 流程治理 Gate | Governance Gate |
| L10_HUMAN_DECISION | 人類裁決 | Human Decision |
| L11_EXECUTION_CONTROL | 執行與控制 | Execution & Control | :contentReference[oaicite:4]{index=4}

---

## 3. 每層輸入/輸出/禁止事項（Definition Summary）

> 下列為「定義摘要」：用於建立跨文件一致的最小詞彙；細部定義於後續 L1–L11 分層工程檔（10–12）。 :contentReference[oaicite:5]{index=5}

### 3.1 Layer I/O 定義表（最小集合）
| Layer | 目的（Purpose） | 輸入（Input） | 輸出（Output） | 禁止（Prohibition） |
|---|---|---|---|---|
| L1 | 取得官方/授權資料 | 無 | Raw Data | 非官方裁決制度；單一來源作唯一依據（需 fallback 設計） |
| L2 | 正規化為 Canonical 格式 | Raw Data | Canonical Data | 隱性補值；以模型猜測取代缺值（除非明確標記可追溯） |
| L3 | 產生可回放快照 | Canonical Data | Snapshot + State Cache | 只存在記憶體；缺 version_ref |
| L4 | 產生可解釋特徵 | Snapshot | Feature Set | 直接產生交易方向；輸出下單參數 |
| L5 | 組裝證據包 | Feature Set | Evidence Bundle | 缺 provenance；無 Evidence 進入下游 |
| L6 | 判定 Regime | Evidence Bundle | Regime State | 單一訊號決定；Regime 不明仍往下推進（可 STOP） |
| L7 | PASS/VETO 裁決 | Regime+Evidence+Account+Rules | PASS/VETO + reason codes + token(PASS only) | Soft Pass；以績效辯護否決 |
| L8 | 產生策略提案 | Risk PASS + Regime | Strategy Proposal | 直連下單；覆寫風控條件 |
| L9 | 檢查流程完整性 | Proposal + Flow Trace | PASS/RETURN/STOP | 任何捷徑；未入 Index 之文件引用 |
| L10 | 人類最終裁決 | PASS Proposal + 風控輸出 + UI evidence | APPROVE/REJECT | AI 代替裁決；模糊化否決原因 |
| L11 | 嚴格執行與可中止 | APPROVE + PASS Token | Orders + Audit + Replay refs | 無 token 下單；Kill Switch 不可用仍執行；缺審計物仍執行 | :contentReference[oaicite:6]{index=6}

---

## 4. Canonical Axioms（不可破壞公理）定義（Enums）

### 4.1 CanonicalAxiomCode（枚舉）
- `AXIOM_FORWARD_ONLY`
- `AXIOM_LAYER_ISOLATION`
- `AXIOM_EVIDENCE_FIRST`
- `AXIOM_VETO_OVER_PROPOSAL`
- `AXIOM_HUMAN_NOT_REPLACEABLE` :contentReference[oaicite:7]{index=7}

### 4.2 Axiom 定義
- `AXIOM_FORWARD_ONLY`：流程只能前進或中止，不得偷偷回寫修正。 :contentReference[oaicite:8]{index=8}  
- `AXIOM_LAYER_ISOLATION`：每層只做該層責任，不得越權。 :contentReference[oaicite:9]{index=9}  
- `AXIOM_EVIDENCE_FIRST`：沒有 Evidence 不得判斷/不得放行。 :contentReference[oaicite:10]{index=10}  
- `AXIOM_VETO_OVER_PROPOSAL`：否決優先於建議（Veto > Proposal）。 :contentReference[oaicite:11]{index=11}  
- `AXIOM_HUMAN_NOT_REPLACEABLE`：L10 必須由人類完成。 :contentReference[oaicite:12]{index=12}  

---

## 5. Canonical Flow 狀態機語義（State / Lifecycle）

> 本節僅定義「狀態與轉移語義」；不定義任何 Gate 內部裁決細則與條件。 

### 5.1 FlowRunState（枚舉）
- `FLOW_CREATED`
- `FLOW_RUNNING`
- `FLOW_STOPPED`
- `FLOW_RETURNED`
- `FLOW_COMPLETED`
- `FLOW_INVALIDATED`

### 5.2 GateDecision（枚舉）
- `DECISION_PASS`
- `DECISION_VETO`
- `DECISION_RETURN`
- `DECISION_STOP`
- `DECISION_APPROVE`
- `DECISION_REJECT`

### 5.3 轉移語義（Transition Semantics）
- `DECISION_VETO`：一旦成立，流程不得進入 L8+（語義後果：STOP/INVALIDATE 依政策呈現，但否決不得被覆寫）。   
- `DECISION_RETURN`：流程退回補齊；不得跳層回補。 :contentReference[oaicite:15]{index=15}  
- `DECISION_STOP`：流程中止；不得以策略或績效理由強行續推。   
- `DECISION_APPROVE/REJECT`：屬 L10 人類裁決輸出語義；AI 不得生成或繞過 UI 產生此輸出。   

---

## 6. 多模式一致性（Cross-Mode Consistency）定義

### 6.1 ModeCode（枚舉）
- `MODE_RESEARCH`
- `MODE_BACKTEST`
- `MODE_SIMULATION`
- `MODE_PAPER`
- `MODE_LIVE` :contentReference[oaicite:18]{index=18}

### 6.2 Invariant（不變項）定義
在所有 Mode 下，不變項如下（不可降級）：  
- L1–L11 順序不可變  
- Risk/Compliance Gate 不可降級  
- Human-in-the-loop 不可移除  
- Audit/Replay 不可降低密度 :contentReference[oaicite:19]{index=19}

### 6.3 Variant（可變項）定義（Only 3）
- 資料來源（歷史/即時）
- 時間推進（模擬/真實）
- Execution 開關（真實/模擬） :contentReference[oaicite:20]{index=20}

---

## 7. 引用合法性與裁決位階（Index & Hierarchy Definition）

### 7.1 Canonical 裁決唯一性（Definition）
- Canonical Flow 的順序與分層責任由 MASTER_CANON 定義；下位文件不得推翻。 

### 7.2 未列入 Index＝無治理效力（Definition）
- 任何未被 DOCUMENT_INDEX 收錄為治理有效之內容，不得作為系統/AI/人類裁決依據。 :contentReference[oaicite:22]{index=22}

---

# ✅ 本檔輸出結束（Batch 2｜第 3/7 檔：09）
