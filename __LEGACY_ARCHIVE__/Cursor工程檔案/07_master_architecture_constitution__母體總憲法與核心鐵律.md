# 07_master_architecture_constitution__母體總憲法與核心鐵律.md
doc_key：MASTER_ARCH（工程拆解對位：Batch 2｜Canonical Definition）  
工程類型：Canonical Definition（定義層）  
治理前提：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
Canonical 來源允許：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX（皆須為 ACTIVE）  
版本狀態：ENGINEERING_TRANSLATION（不具新增治理效力；僅做原文定義結構化轉譯）  

<!--
SOURCE_TAG
Canonical 來源（ACTIVE）：
- TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md（doc_key=MASTER_ARCH）
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md（doc_key=MASTER_CANON）
- TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key=DOCUMENT_INDEX）
原文範圍：
- MASTER_ARCH：全文（§0–§13）
- MASTER_CANON：§2（L1–L11 Canonical Flow）、§3（5 Axioms）、§15（Conflict Resolution Order）、§16（Decision Separation）
- DOCUMENT_INDEX：§1（Hard Laws）、§2（doc_key 制度）、§3（治理等級與覆蓋規則）、§4（ACTIVE 唯一性）
-->

---

## 0. 文件定位（Definition Scope）

本工程檔為 **MASTER_ARCH（母體總憲法與核心鐵律）** 之「定義層」工程轉譯：  
僅將原文中的 **名詞、實體、枚舉、代碼、結構、狀態與生命週期**做結構化表達，**不新增制度、不改寫語義、不提供實作**。 

---

## 1. 核心名詞定義（Definitions）

### 1.1 TAITS（Taiwan Alpha Intelligence Trading System）
- 定義：以台灣市場為設計目標之全系統交易母體；所有交易生成必須走 Canonical Flow（L1–L11）。 

### 1.2 Human Sovereignty（人類主權）
- 定義：系統為 Human-in-the-Loop 強制；**AI 永不具最終決策權**。 :contentReference[oaicite:2]{index=2}

### 1.3 Risk & Compliance（風險與合規）
- 定義：具跨層、跨模組、跨策略之 **最高即時否決權（Supreme Veto）**。 

### 1.4 Regime（市場狀態）
- 定義：市場狀態母判斷（非策略、非指標）；Regime 不符時，策略不得啟用。 

### 1.5 Evidence（證據）
- 定義：可回放、可審計、可追溯之證據組合；所有判斷必須基於 Evidence。 

### 1.6 Strategy（策略）
- 定義：永遠只是「建議與假設」；策略輸出不得直連下單；策略 ≠ Execution。 

### 1.7 Execution（執行）
- 定義：合規前提下之嚴格執行（L11）；不得由策略直連；不得在缺少必要 token/審計物時進行。 :contentReference[oaicite:7]{index=7}

### 1.8 Performance / Optimization（績效 / 最適化）
- 定義：不得作為違規辯護理由；不得用於對抗否決。 

### 1.9 Annotation（註解）
- 定義：僅供人類理解與語意對齊；永遠為 Non-Binding（不具約束性）。 :contentReference[oaicite:9]{index=9}

### 1.10 Only-Add（只增不減）
- 定義：治理有效文件之演進原則：只可新增；禁止刪除、覆寫、偷換語義、摘要化導致語義縮減。 

---

## 2. 不可動搖的核心排序（Priority Order｜Enum）

### 2.1 PriorityOrder（枚舉）
> TAITS 全系統之最終排序如下（不可更動）： :contentReference[oaicite:11]{index=11}

- `HUMAN_SOVEREIGNTY`
- `RISK_COMPLIANCE_SUPREME_VETO`
- `REGIME`
- `EVIDENCE`
- `STRATEGY`
- `EXECUTION`
- `PERFORMANCE_OPTIMIZATION`

### 2.2 PriorityOrder 解釋（Definition Notes）
- `HUMAN_SOVEREIGNTY`：AI 永不具最終決策權。 :contentReference[oaicite:12]{index=12}  
- `RISK_COMPLIANCE_SUPREME_VETO`：可否決任何高績效策略；否決不可被績效對抗。   
- `REGIME`：高於任何單一訊號或模型。   
- `EVIDENCE`：所有判斷必須基於可回放與可稽核證據。   
- `STRATEGY`：僅為建議/假設；不得升格為指令。   
- `EXECUTION`：需在合規與控制前提下嚴格執行。 :contentReference[oaicite:17]{index=17}  
- `PERFORMANCE_OPTIMIZATION`：不得為任何違規辯護。   

---

## 3. 禁止行為定義（Prohibitions｜Enum）

### 3.1 ProhibitionCode（枚舉）
> 本節僅將 MASTER_ARCH 明示之「禁止事項」做代碼化命名以利審計與引用；不新增新的禁止事項。 :contentReference[oaicite:19]{index=19}

#### 3.1.1 AI 禁止行為（AI Prohibitions）
- `AI_NO_AUTO_ORDER`：AI 不得自動下單。 :contentReference[oaicite:20]{index=20}  
- `AI_NO_DISABLE_RISK`：AI 不得自動解除風控。 :contentReference[oaicite:21]{index=21}  
- `AI_NO_MODIFY_GOV_RULES`：AI 不得自動修改治理規則。 :contentReference[oaicite:22]{index=22}  
- `AI_NO_FULL_UNATTENDED_TRADING`：不存在完全無人值守交易。 :contentReference[oaicite:23]{index=23}  
- `AI_NO_DEFINE_NEW_STRATEGY_TYPES`：AI 不得自行定義新策略類型。 :contentReference[oaicite:24]{index=24}  
- `AI_NO_MODIFY_GOV_DOCS`：AI 不得自行修改治理文件。 :contentReference[oaicite:25]{index=25}  
- `AI_NO_ASSUME_EXECUTABILITY`：AI 不得自行假設可執行性。 :contentReference[oaicite:26]{index=26}  

#### 3.1.2 否決權相關禁止（Veto Prohibitions）
- `VETO_NO_PERFORMANCE_OVERRIDE`：不得以長期績效對抗否決。   
- `VETO_NO_BACKTEST_OVERRIDE`：不得以回測成功解除否決。   

#### 3.1.3 Regime 相關禁止（Regime Prohibitions）
- `REGIME_NO_IGNORE`：不得忽略 Regime。   
- `REGIME_NO_INFER_FROM_STRATEGY`：不得用策略反推 Regime。   

#### 3.1.4 Evidence 相關禁止（Evidence Prohibitions）
- `EVIDENCE_NO_HEARSAY`：禁止傳聞。 :contentReference[oaicite:31]{index=31}  
- `EVIDENCE_NO_SUBJECTIVE_FEELING`：禁止主觀感覺。 :contentReference[oaicite:32]{index=32}  
- `EVIDENCE_NO_NON_REPRODUCIBLE_EXPERIENCE`：禁止無法重現的經驗敘事。 :contentReference[oaicite:33]{index=33}  

#### 3.1.5 Strategy / Execution 分離禁止（Separation Prohibitions）
- `STRATEGY_NO_DIRECT_ORDER_PARAMS`：策略不得直接輸出價格/數量/買賣方向。   
- `STRATEGY_NO_DIRECT_LINK_TO_EXECUTION`：策略不得直連任何下單模組。   

#### 3.1.6 Annotation 禁止（Annotation Prohibitions）
- `ANNOTATION_NO_ESCALATION_TO_CONDITION`：註解不得升格為條件。 :contentReference[oaicite:36]{index=36}  
- `ANNOTATION_NO_PROGRAM_PARSE`：註解不得被程式解析。 :contentReference[oaicite:37]{index=37}  
- `ANNOTATION_NO_BACKTEST_LIVE_USAGE`：註解不得用於回測或實盤。 :contentReference[oaicite:38]{index=38}  

#### 3.1.7 Structure ≠ Strategy 禁止（Structure Prohibitions）
- `STRUCTURE_NO_BUY_POINT_EQUIVALENCE`：禁止「結構=買點」。 :contentReference[oaicite:39]{index=39}  
- `DIVERGENCE_NO_REVERSAL_EQUIVALENCE`：禁止「背離=反轉」。 :contentReference[oaicite:40]{index=40}  
- `CENTER_NO_BREAKOUT_EQUIVALENCE`：禁止「中樞=突破」。 :contentReference[oaicite:41]{index=41}  

---

## 4. 合法輸出類型定義（Allowed Outputs｜Schema）

### 4.1 StrategyOutput（策略輸出允許集合）
> Strategy 只允許輸出以下語義： 

- `proposal`
- `context`
- `risk_adjust`
- `avoid`
- `observe`

### 4.2 StructureOutput（結構輸出允許集合）
> 結構（纏論/結構/型態）僅為描述語法，允許輸出如下： :contentReference[oaicite:43]{index=43}

- `structure_state`
- `completeness_score`
- `conflict_flag`
- `warning`

### 4.3 EvidenceBundle（證據包｜必要屬性）
> Evidence 必須具備以下屬性： :contentReference[oaicite:44]{index=44}

- `provenance`（來源鏈）
- `completeness`（完整性）
- `immutability`（不可變）
- `replayability`（可回放）

---

## 5. 違規等級定義（Enforcement Level｜Enum）

### 5.1 ViolationLevel（枚舉）
> 違規等級與定義來源為 MASTER_ARCH 明示內容： :contentReference[oaicite:45]{index=45}

- `LEVEL_A`：觸碰人類主權、風控否決、治理鐵律  
- `LEVEL_B`：越權推論、策略下單化  
- `LEVEL_C`：文件簡化、語意誤導  

### 5.2 DispositionRule（處置原則｜Enum）
> 僅轉譯 MASTER_ARCH 明示之處置原則： :contentReference[oaicite:46]{index=46}

- `LEVEL_A_STOP_ROLLBACK_BLOCK`：立即停止、回滾、封鎖  
- `LEVEL_B_DEGRADE_REVIEW`：降級、重審  
- `LEVEL_C_DOC_FIX`：文件修正  

---

## 6. 文件位階關係定義（Hierarchy｜Definition）

### 6.1 MASTER_ARCH 上位約束範圍（Non-Exhaustive List）
> MASTER_ARCH 明示其為下列文件之上位約束： :contentReference[oaicite:47]{index=47}

- `MASTER_CANON`
- `ARCH_FLOW`
- `RISK_COMPLIANCE`
- `EXECUTION_CONTROL`
- `STRATEGY_UNIVERSE`
- `STRATEGY_FEATURE_INDEX`
- `UI_SPEC`
- `DOCUMENT_INDEX`

### 6.2 doc_key（文件身份證）
- 定義：TAITS 文件唯一識別碼，用於版本控管、引用審計、回放重建；同一 doc_key 在 ACTIVE 範圍內不可重複。 :contentReference[oaicite:48]{index=48}

### 6.3 ACTIVE（版本狀態）
- 定義：代表此刻具有治理效力，且可被系統/AI/人類引用作為裁決依據；同 doc_key 僅允許一份 ACTIVE。 :contentReference[oaicite:49]{index=49}

---

## 7. 最終鎖定聲明（Final Lock｜State）

### 7.1 FinalLockState（狀態定義）
- 定義：`ACTIVE + LOCKABLE` 代表永久治理母憲法；任何未來 AI/Agent/新對話不得重新解釋、不得簡化、不得繞過。 :contentReference[oaicite:50]{index=50}

---

## 8. Canonical Flow 對位（僅作定義引用，不展開流程細節）

> 本節僅建立「MASTER_ARCH 憲法語義」與「MASTER_CANON（L1–L11）」之定義對位索引；不新增條款。 

### 8.1 三權分立對位（Decision Separation）
- `STRATEGY`：對應 L8（Strategy & Research）之「Proposal」語義，且不得直連 L11。   
- `HUMAN_DECISION`：對應 L10（Human Decision）之最終裁決。   
- `EXECUTION_CONTROL`：對應 L11（Execution & Control）之嚴格執行與可中止。 :contentReference[oaicite:54]{index=54}  

---

# ✅ 本檔輸出結束（Batch 2｜第 1/7 檔：07）
