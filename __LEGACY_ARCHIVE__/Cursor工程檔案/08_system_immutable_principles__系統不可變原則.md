# 08_system_immutable_principles__系統不可變原則.md
doc_key：SYSTEM_IMMUTABLE_PRINCIPLES（工程拆解對位：Batch 2｜Canonical Definition）  
工程類型：Canonical Definition（定義層）  
治理前提：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
Canonical 來源允許：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX（皆須為 ACTIVE）  
版本狀態：ENGINEERING_TRANSLATION（不具新增治理效力；僅做原文定義結構化轉譯）

<!--
SOURCE_TAG
Canonical 來源（ACTIVE）：
- TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md（doc_key=MASTER_ARCH）
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md（doc_key=MASTER_CANON）
- TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251219/251220.md（doc_key=DOCUMENT_INDEX）
原文範圍：
- MASTER_CANON：§2（L1–L11 定義）、§3（5 Axioms）、§4（多模式一致性 Invariant）、§5（Evidence 必備屬性）、§6（Veto 法律地位）
- MASTER_ARCH：全文中「人類主權 / 三權分立 / Only-Add / Regime-First / Risk/Compliance 最高否決 / 禁止事項」之定義段落
- DOCUMENT_INDEX：§1（Hard Laws）、§2（doc_key 制度）、§3（治理等級與覆蓋規則）、§4（ACTIVE 唯一性）
-->

---

## 0. 文件定位（Definition Scope）

本工程檔之目的：把 TAITS 在 Canonical 文件中明示為「不可被任何工程、模組、Agent、策略、AI、模式切換所改寫」之規範，抽出成 **不可變原則（Immutable Principles）** 的定義清單，供下游工程檔一致引用。  
本檔僅做定義轉譯：不新增制度、不提供實作、不引入新規則。 

---

## 1. 不可變原則的定義（Immutable Principle｜Definition）

### 1.1 Immutable Principle（不可變原則）
- 定義：在 TAITS 中，被上位 Canonical 文件明示為「不可改寫、不可降級、不可用例外繞過」之系統硬約束；其效力跨越所有模式（Research / Backtest / Simulation / Paper / Live）且對所有模組、Agent 與使用者行為生效。 

---

## 2. 不可變原則全集（ImmutablePrincipleSet｜Enum）

> 本節為「定義集合」：將 Canonical 原文中的不可變條款，以可引用的枚舉鍵名整理；不新增任何原文未含之原則。 

### 2.1 ImmutablePrincipleCode（枚舉）

#### A. Canonical Flow 與分層隔離（Flow & Layer Isolation）
- `IP_FLOW_L1_L11_FIXED`：Canonical Flow 固定為 L1–L11，任何流程不得跳層、不得跨層合併。 :contentReference[oaicite:3]{index=3}
- `IP_FORWARD_ONLY`：流程只能前進或中止；不得以隱性回寫方式「偷偷修正」上游輸出。 :contentReference[oaicite:4]{index=4}
- `IP_LAYER_ISOLATION`：每一層只做該層責任；不得越權產出下一層語義（尤其不得由分析/特徵直接產生交易方向或下單參數）。 :contentReference[oaicite:5]{index=5}

#### B. Evidence 與可回放（Evidence & Replayability）
- `IP_EVIDENCE_FIRST`：沒有 Evidence 不得判斷、不得放行；Evidence 為判斷與裁決的法律基礎。 :contentReference[oaicite:6]{index=6}
- `IP_EVIDENCE_HAS_PROVENANCE`：Evidence 必須包含來源鏈（provenance），缺失即不成立。 :contentReference[oaicite:7]{index=7}
- `IP_EVIDENCE_HAS_COMPLETENESS`：Evidence 必須可表達完整性（completeness）；不得以缺證據硬判。 :contentReference[oaicite:8]{index=8}
- `IP_EVIDENCE_IMMUTABLE`：Evidence 必須不可變（immutability）；不得事後改寫。 :contentReference[oaicite:9]{index=9}
- `IP_EVIDENCE_REPLAYABLE`：Evidence 必須可回放（replayability）；無法回放則不得作為裁決依據。 
- `IP_AUDIT_SUPREMACY`：無審計＝未發生；任何聲稱依據文件或流程之行為，必須可追溯至版本與章節定位。 :contentReference[oaicite:11]{index=11}

#### C. Regime-First（市場狀態優先）
- `IP_REGIME_FIRST`：Regime 高於單一訊號、模型或策略；Regime 不符時，策略不得啟用或不得推進。 
- `IP_REGIME_NOT_SINGLE_SIGNAL`：Regime 不得由單一訊號決定；Regime 不明確時允許 STOP，不得硬推進。 :contentReference[oaicite:13]{index=13}

#### D. Risk / Compliance 最高否決（Supreme Veto）
- `IP_VETO_SUPREME`：Risk/Compliance 具最高否決權；任何否決一旦成立必須立即生效。 
- `IP_VETO_NOT_OVERRIDABLE`：Veto 不可被覆寫（包含 Human 不得覆寫風控/合規否決）。 :contentReference[oaicite:15]{index=15}
- `IP_NO_PERFORMANCE_OVERRIDE_VETO`：不得以績效、勝率、回測結果辯護以弱化或推翻否決。 

#### E. Human Sovereignty（人類主權不可移除）
- `IP_HUMAN_IN_LOOP_REQUIRED`：L10 人類裁決不可被移除；Human-in-the-Loop 為不可變結構。 
- `IP_AI_NOT_DECIDER`：AI 不得成為裁決主體；AI 僅為輔助。 :contentReference[oaicite:18]{index=18}

#### F. 三權分立與邊界鐵律（Separation & Hard Boundaries）
- `IP_STRATEGY_NEQ_EXECUTION`：策略 ≠ 下單；策略不得直連 Execution。 
- `IP_AGENT_NEQ_STRATEGY`：Agent ≠ 策略；不得以 Agent 串聯形成隱性策略鏈。 
- `IP_AI_NEQ_TRUTH`：AI ≠ 唯一真理；不得以 AI 推薦取代制度、證據或否決。 :contentReference[oaicite:21]{index=21}
- `IP_NO_HIDDEN_STRATEGY`：不得存在隱性策略鏈（跨層回寫、私下串聯、將特徵當方向、將建議當指令）。 

#### G. 多模式一致性（Cross-Mode Invariants）
- `IP_MODE_INVARIANTS`：在 Research/Backtest/Simulation/Paper/Live 中，不變項不可改：L1–L11 順序、Risk/Compliance Gate 不可降級、Human-in-the-loop 不可移除、Audit/Replay 不可降低密度。 :contentReference[oaicite:23]{index=23}

#### H. 文件治理不可變（Document Governance Invariants）
- `IP_INDEX_RESOLUTION_SUPREME`：未列入 DOCUMENT_INDEX＝不具治理效力；衝突裁決以 Index 規則與上位覆蓋為準。 :contentReference[oaicite:24]{index=24}
- `IP_GOV_LEVEL_OVERRIDE_RULES`：A+/A/B/C 治理等級覆蓋規則不可被下位文件推翻。 :contentReference[oaicite:25]{index=25}
- `IP_ONLY_ADD`：Only-Add 為治理有效文件的演進唯一合法方式。 
- `IP_DOC_KEY_UNIQUENESS`：doc_key 為文件身份證；同一 doc_key 在 ACTIVE 範圍不可重複。 :contentReference[oaicite:27]{index=27}
- `IP_ACTIVE_UNIQUENESS`：同 doc_key 僅能有一份 ACTIVE；更換 ACTIVE 必須以新增版本並可稽核。 :contentReference[oaicite:28]{index=28}

---

## 3. 不可變原則之結構化資料模型（Schema）

> 本節僅提供「不可變原則」作為可引用實體的最小欄位集合；用途為審計與引用一致性（定義層），不涉及任何執行實作。 

### 3.1 ImmutablePrincipleRecord（最小欄位，不可縮減）
- `principle_code`：ImmutablePrincipleCode（本檔 2.1）
- `principle_name_zh`：繁中正式名
- `source_doc_keys[]`：來源文件（MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX）
- `source_sections[]`：可追溯章節定位（文字定位，不含推論）
- `scope`：SYSTEM / FLOW / EVIDENCE / REGIME / RISK / HUMAN / DOC_GOV（枚舉）
- `applies_to_modes[]`：RESEARCH / BACKTEST / SIMULATION / PAPER / LIVE（必含全部或明示子集）
- `violation_effect`：STOP / RETURN / INVALIDATE（僅作語義分類；不定義流程細節）
- `notes`：僅允許補充「定義澄清」，不得新增規則

---

## 4. 違反不可變原則的語義後果（State Semantics）

> 本節只做「語義後果」的狀態定義；不引入風控裁決細則、不引入執行控制實作。 

### 4.1 ImmutableViolationOutcome（枚舉）
- `OUTCOME_STOP`：必須停止（不允許往下推進）
- `OUTCOME_RETURN`：必須退回補齊（不得跳層）
- `OUTCOME_INVALIDATE`：引用或輸出視為無效（治理上不承認）

---

## 5. 最終鎖定聲明（Final Lock｜State）

本檔所列不可變原則，係由上位 Canonical 文件明示之硬約束集合；在 GOVERNANCE_STATE = Freeze v1.0 下，僅允許 **Only-Add 擴充**（新增原文已明示但未收錄之條目），不得刪減、不得覆寫、不得改寫語義。 

---

# ✅ 本檔輸出結束（Batch 2｜第 2/7 檔：08）
