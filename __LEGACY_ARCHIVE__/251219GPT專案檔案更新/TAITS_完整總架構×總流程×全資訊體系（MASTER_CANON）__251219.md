# TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219
doc_key：MASTER_CANON  
治理等級：A（Canonical Master｜完整總架構×總流程×全資訊體系｜承接 MASTER_ARCH）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（Canonical Flow 唯一母本；Only-Add 演進）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / DOCUMENT_INDEX（Index 裁決）  
平行參照：ARCH_FLOW / FULL_ARCH / GOVERNANCE_GATE_SPEC / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES / LOCAL_ENV / DEPLOY_OPS / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減／覆寫／改寫語義／偷換定義）  
核心裁決：L1–L11 Canonical Flow 不可跳步（No-Skip）＋ Evidence First（證據先於判斷）＋ Veto Priority（否決優先）

---

## 0. 文件定位（Canonical Master｜何謂「完整總架構×總流程×全資訊體系」）

本文件是 TAITS 的 **Canonical Master**（規範母本），負責回答：

1. **TAITS 系統如何被正確運作（Canonical Flow）**
2. **全系統從資料 → 證據 → 狀態（Regime）→ 風控合規 → 策略建議 → 治理 Gate → 人類裁決 → 執行控制** 的唯一合法順序
3. **Evidence（證據）在制度上的法律地位**：沒有可追溯證據＝制度上視為未發生
4. **不同運行模式一致性**：Research / Backtest / Simulation / Paper / Live 皆不得降級流程與審計語義
5. **與其他權威文件的邊界切分**，避免越權或重疊

📌 本文件不負責（避免越權）：
- 不改寫最高鐵律（由 MASTER_ARCH 裁決）
- 不取代流程細節（由 ARCH_FLOW 裁決，本文件只定義 Canonical 母本與「不得跳步」）
- 不取代風控合規細則（由 RISK_COMPLIANCE / TWSE_RULES 裁決）
- 不取代執行通道細則（由 EXECUTION_CONTROL 裁決）
- 不取代 UI 外觀（由 UI_SPEC 裁決）
- 不產生交易方向、不承諾績效、不形成下單權

---

## 1. Canonical Master 的「不變核心」（Hard Gates｜不可動搖）

### 1.1 五大不可破壞公理
1) **L1–L11 不可跳步（No-Skip Canon）**  
任何模式、任何人、任何 Agent、任何策略，不得跳過任一層。  
允許 RETURN（退回補齊）與 STOP/BLOCK（中止/阻斷），不允許「捷徑」。

2) **證據先於判斷（Evidence First）**  
沒有 Evidence Bundle（L5）不得進入 Regime / Risk / Strategy / Gate。

3) **Regime 高於策略（Regime > Strategy）**  
Regime 是策略啟用的前置條件；策略不得覆寫 Regime。

4) **Risk/Compliance 可否決一切（Supreme Veto）**  
RISK_COMPLIANCE（L7）具最高否決權；否決不得以績效或主觀緊急性辯護。

5) **人類裁決不可被取代（Human-in-the-Loop）**  
L10 的裁決只屬於人類；AI/Agent/策略僅能提供建議與可解釋證據，不得自動批准。

---

## 2. 全系統 Canonical Flow（L1–L11）總覽（唯一合法順序）

> 本節是「母本」：定義 **必經層級** 與 **層級目的**。  
> 細化輸入/輸出/狀態轉移/審計欄位 → 由 ARCH_FLOW 延伸；但不得與本節衝突。

### 2.1 L1–L11 層級定義（Definition）
- **L1 資料來源接入（Data Ingestion）**：取得原始資料（官方優先），建立來源追溯。
- **L2 資料標準化與品質（Normalization & QA）**：清洗、對齊、校驗、建立 canonical 格式。
- **L3 市場快照與狀態（Snapshot & State）**：形成可回放的市場狀態快照（Snapshot）。
- **L4 分析與特徵工程（Analysis & Feature）**：把資料轉成可解釋特徵；不得產生交易方向。
- **L5 證據包組裝（Evidence Bundle）**：多證據合成、衝突處理、可追溯與可回放。
- **L6 市場狀態/場景（Regime）**：判定市場狀態（Regime），作為策略啟用前置條件。
- **L7 風控與合規 Gate（Risk & Compliance Gate）**：PASS/VETO（二元裁決），最高否決權。
- **L8 策略與研究建議（Strategy & Research Proposal）**：僅輸出「建議/假設/情境」，不得直連下單。
- **L9 治理 Gate（Governance Gate）**：PASS/BLOCK/RETURN（三態裁決），保證流程/引用/審計/版本合法性。
- **L10 人類裁決（Human Decision）**：唯一能形成「執行意圖」的裁決節點。
- **L11 交易執行與控制（Execution & Control）**：需 Risk PASS Token + 人類批准 + Kill Switch always available。

### 2.2 Canonical Flow 的最小硬性輸入/輸出（Minimal I/O）
- **最小輸入（啟動一次 Flow 的必要條件）**
  - `universe`（標的集合/範圍）
  - `mode`（Research/Backtest/Simulation/Paper/Live）
  - `time_context`（交易日/回測時間窗口）
  - `documents_active_map`（當下 ACTIVE 文件版本映射）
  - `correlation_id` / `session_id`（全鏈路追溯鍵）

- **最小輸出（一次 Flow 結束後必留下）**
  - `final_status`（STOP / RETURN / PASS_TO_NEXT / EXECUTED 等）
  - `audit_artifacts_refs`（全層審計物引用）
  - `replay_bundle_ref`（回放包引用）
  - `version_ref`（doc/policy/model/rule snapshot）

---

## 3. Evidence（證據）制度地位（Evidence Is Law）

### 3.1 Evidence 的法律地位（制度語義）
- Evidence 是 TAITS 的「制度事實」。
- **沒有 Evidence（或 Evidence 不可回放）＝制度上視為未發生**。
- 任何判斷、建議、裁決（含人類裁決與執行）若缺 Evidence：一律視為治理違規。

### 3.2 Evidence Bundle（L5）最小構成（不可縮減）
- `provenance_map_ref`（來源追溯映射）
- `snapshot_ref`（L3 快照引用）
- `features_ref`（L4 特徵引用）
- `evidence_items[]`（多證據條目，每條可追溯）
- `conflict_resolution_log_ref`（衝突處理記錄）
- `evidence_hash`（完整性）
- `version_ref`（文件/政策/模型/規則快照）

---

## 4. Gate 體系（Two-Gate + Human Decision）與裁決優先序

### 4.1 風控 Gate（L7）
- 輸出：`PASS` 或 `VETO`（Binary Compliance）
- 最高否決權：任何 VETO 直接 STOP，不得以績效辯護

### 4.2 治理 Gate（L9）
- 輸出：`PASS` / `BLOCK` / `RETURN`（三態）
- 目的：保證流程不可跳步、引用合法、審計與版本一致、UI 必須揭露

### 4.3 人類裁決（L10）
- 輸出：`APPROVE` / `REJECT`
- 只有在 L7 PASS 且 L9 PASS 才能進入 L10

---

## 5. 多模式一致性（Research / Backtest / Simulation / Paper / Live）

### 5.1 不變項（所有模式皆相同）
- L1–L11 順序不可改
- Gate 語義不可改
- 審計/回放密度不可降級（No Downgrade）
- 版本引用必須存在（version_ref）

### 5.2 可變項（僅允許三處差異）
- 資料來源（歷史/即時）
- 時間推進（模擬/真實）
- 執行通道（真實/模擬；但執行語義與審計仍必須存在）

---

## 6. 中斷/退回/否決（Interrupt Taxonomy｜制度化）

### 6.1 三類裁決結果
- **STOP/BLOCK**：流程立即終止（含 Risk VETO、治理 BLOCK、緊急停機）
- **RETURN**：退回補齊（不是放行），必須附「補齊清單」
- **PASS**：允許進入下一層

### 6.2 最小審計要求（所有中斷必備）
- 中斷層級（layer_id）
- 原因碼（reason_codes）
- 當下 Evidence/Regime/Risk 快照引用
- 版本引用（version_ref）
- correlation_id / session_id

---

## 7. Mermaid｜MASTER_CANON Canonical Flow（母本總流程圖）

```mermaid
flowchart TB
  L1[L1 Data Ingestion] --> L2[L2 Normalization & QA]
  L2 --> L3[L3 Snapshot & State]
  L3 --> L4[L4 Analysis & Feature]
  L4 --> L5[L5 Evidence Bundle]
  L5 --> L6[L6 Regime Engine]
  L6 --> L7[L7 Risk & Compliance Gate]
  L7 -->|PASS| L8[L8 Strategy & Research Proposal]
  L7 -->|VETO| STOP1[STOP/VETO + Audit + Replay Ref]
  L8 --> L9[L9 Governance Gate]
  L9 -->|PASS| L10[L10 Human Decision]
  L9 -->|RETURN| RET[RETURN + Required Items List]
  L9 -->|BLOCK| STOP2[STOP/BLOCK + Preserve Evidence]
  L10 -->|APPROVE| L11[L11 Execution & Control]
  L10 -->|REJECT| STOP3[STOP/Human Reject + Audit]
  L11 -->|SUCCESS| END[END + Replay Bundle]
  L11 -->|FAIL| EMSTOP[EMERGENCY STOP + Kill Switch + Audit]
  RET --> L4
8. 與其他核心文件的對位（強制一致）
MASTER_ARCH：定義「永不違反」鐵律（本文件不得推翻）

ARCH_FLOW：細化每層「輸入/輸出/狀態轉移/審計欄位」

FULL_ARCH：定義模組地圖與分層映射（本文件定義順序）

GOVERNANCE_GATE_SPEC：定義治理 Gate 的裁決、原因碼、UI 義務

RISK_COMPLIANCE：定義風控合規最高否決與 reason codes

EXECUTION_CONTROL：定義 L11 執行控制與 Kill Switch / Token / 去重 / 對帳

UI_SPEC：定義 UI 必須揭露的裁決結果與證據可視化

VERSION_AUDIT：定義版本帳本、可追溯與可回放的落地

DATA_SOURCES：定義資料來源宇宙、官方優先與 fallback

TWSE_RULES：定義制度規則彙編與觸發映射

LOCAL_ENV / DEPLOY_OPS：定義環境隔離、金鑰保護與營運規範

9. Only-Add 演進規則（MASTER_CANON 專屬）
允許：

新增子層描述（例如 L4.1、L7.2）

新增審計欄位（不可移除舊欄位）

新增回放視角（View），不破壞舊回放

新增模式（如 Sandbox），但不得降級 Gate/審計語義

禁止：

刪除或合併 L1–L11

改寫既有層級語義

以「簡化」為由跳步

以效能為由省略審計或回放

10. （原始內容全文保留｜不刪不改）
以下區塊為你現有 MASTER_CANON 原文，我 一字不刪完整保留，並納入同一份文件中。
若未來需要擴充，只能在本文件追加（Only-Add），不得回頭刪改原文語義。

Taiwan Alpha Intelligence Trading System
Canonical 前言（Why This Canon Exists）
本文件為 TAITS 的 Canonical Master 文件。

若《MASTER_ARCH》回答的是：

「什麼永遠不能被違反？」

那麼《MASTER_CANON》回答的是：

「TAITS 是如何被正確地運作？」

本文件的存在目的不是加速交易，
而是確保 任何一筆交易的生成，都經過可回放、可審計、可否決的完整過程。

1. TAITS Canonical Flow（L1–L11）
TAITS 全系統遵守 11 層 Canonical Flow，不可跳層，不可捷徑。

Layer	名稱	角色
L1	DataSources	資料來源接入
L2	Data Normalize	標準化／清洗
L3	Market Snapshot	狀態快照／可回放
L4	Feature/Indicator	特徵／指標生成
L5	Evidence Bundle	證據包組裝
L6	Regime Engine	市場狀態判定
L7	Risk & Compliance	風控／合規 Gate
L8	Strategy Proposal	策略建議／研究層
L9	Governance Gate	治理 Gate
L10	Human Decision	人類裁決
L11	Execution & Control	執行控制

2. Canonical 的「不可跳步」意義
任何策略、任何 Agent、任何 UI 操作，都必須經過 L1–L11。
理由如下：

避免研究捷徑污染實盤

確保所有決策都有證據可追溯

確保 Risk/Compliance 能否決一切

確保 Human Decision 不可被取代

確保 Execution 永遠在控制下

3. Evidence 的制度地位（Evidence = Legal Truth）
TAITS 定義：

無 Evidence = 未發生

Evidence Bundle 必須可回放、可審計。
任何未能留存證據的交易行為視為非法。

4. Regime 高於策略（Regime > Strategy）
策略必須依 Regime 啟用／停用。
策略不得在 Regime 不明確或禁入狀態下強行輸出下單。

5. Risk / Compliance 最高否決權（Veto Supreme）
Risk/Compliance Gate 具最高否決權。
任何否決必須立即中止流程，不得以績效或主觀辯護。

6. Governance Gate（L9）的存在理由
即使 Risk PASS，仍可能出現：

Evidence 不完整

版本引用不一致

文件引用非法

審計缺失

因此必須存在 L9 Governance Gate 做流程合法性裁決。

7. Human Decision（L10）不可被取代
TAITS 不允許無人值守自動交易。
所有 Execution 必須由人類裁決批准。

8. Execution & Control（L11）必須永遠可中止
Execution 層必須具備：

Risk PASS Token 驗證

Kill Switch 永遠可用

Pre/In/Post 三段審計

去重／冪等保護

對帳一致性檢查

9. 多模式一致性（Research / Backtest / Simulation / Paper / Live）
所有模式必須共用同一 Canonical Flow。
差異僅允許：

資料來源（歷史/即時）

時間推進（模擬/真實）

Execution 通道（真實/模擬）

10. Canonical 的最終目標
TAITS 的目標不是追求交易次數或績效敘事，
而是追求：

可追溯

可回放

可否決

可治理

可長期演進

（MASTER_CANON｜原文保留區 完）

11. 封版宣告（不可更改）
TAITS 的正確運作，必須遵守 L1–L11 Canonical Flow。
任何跳步、捷徑、無證據、無審計、無版本引用的行為，皆屬制度違規。

（MASTER_CANON｜最大完備・治理對齊版 v2025-12-19 完）
