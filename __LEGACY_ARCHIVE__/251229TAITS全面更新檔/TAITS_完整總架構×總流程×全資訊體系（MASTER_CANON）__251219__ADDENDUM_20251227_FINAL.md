# TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219
doc_key：MASTER_CANON  
治理等級：A（Canonical｜最高裁決母體）  
版本標籤：S（Supreme Canon｜整合 Canon 標籤）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（以本版本為準）  
版本日期：2025-12-29  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
平行參照：FULL_ARCH / ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / GOVERNANCE_GATE_SPEC / VERSION_AUDIT / DATA_SOURCES / TWSE_RULES / STRATEGY_UNIVERSE / STRATEGY_FEATURE_INDEX / LOCAL_ENV / DEPLOY_OPS / README / PROJECT_PROMPT / PROCESS_ANCHOR / GOVERNANCE_STATE_FREEZE_V1 / DOCUMENT_INDEX  
變更原則：本版本為「整併重編（Consolidated Rewrite）」：以最新補充內容取代舊版重複段落，形成單一一致正文（不再以附錄/附加章節分裂閱讀路徑）。

---

## 0. 文件定位與裁決基線（Index Gate）
- 本文件之治理身份（doc_key / 等級 / ACTIVE）以 DOCUMENT_INDEX 為唯一裁決來源（Index Gate）。
- 子級標籤（如 S）僅為閱讀/版本標籤，不得取代治理等級裁決。

---

## 1. Canonical Flow（L1–L11）— 最新一致正文
### L1｜Data Source（資料取得）
目的：取得官方/授權資料，形成 Raw Data。

輸入：無  
輸出：Raw Data  
禁止：
- 以非官方裁決制度
- 以單一來源作唯一依據（必須設計 fallback）

---

### L2｜Normalization（資料清洗與標準化）
目的：將 Raw Data 轉為可比較、可回放的 Canonical 格式。

輸入：Raw Data  
輸出：Canonical Data  
禁止：
- 隱性補值
- 以模型猜測取代缺值（除非明確標記並可追溯）

---

### L3｜Snapshot & State（狀態快照）
目的：建立「當下市場狀態」快照，必須可回放。

輸入：Canonical Data  
輸出：Snapshot + State Cache  
禁止：
- 只存在記憶體
- 無 version_ref

---

### L4｜Analysis（分析層）
目的：將資料轉為可解釋特徵（Indicators / Factors / Structures）

輸入：Snapshot  
輸出：Feature Set  
禁止：
- 直接產生交易方向
- 直接輸出下單參數

---

### L5｜Evidence（證據層）
目的：組裝 Evidence Bundle（證據包），形成可審計基礎。

輸入：Feature Set  
輸出：Evidence Bundle  
禁止：
- 沒 Evidence 進入 Regime/Risk
- Evidence 缺 provenance

---

### L6｜Regime（市場狀態判定）
目的：判定市場狀態（Regime），作為策略啟用前置條件。

輸入：Evidence Bundle  
輸出：Regime State  
禁止：
- Regime 由單一訊號決定
- Regime 不明確仍往下推進（可 STOP）

---

### L7｜Risk & Compliance（最高否決 Gate）
目的：對所有意圖做 PASS/VETO 裁決。

輸入：Regime State + Evidence + Account/Portfolio + Rules  
輸出：PASS / VETO + reason codes + token (PASS only)  
禁止：
- 任何形式的 Soft Pass
- 以績效辯護否決

---

### L8｜Strategy & Research（策略與研究層）
目的：提出策略候選（Proposal），並映射到適用條件。

輸入：Risk PASS + Regime State  
輸出：Strategy Proposal  
禁止：
- 策略直連下單
- 策略覆寫風控條件

---
### L9｜Governance Gate（流程治理 Gate）
目的：檢查流程完整性與文件一致性。

輸入：Strategy Proposal + Flow Trace  
輸出：PASS / RETURN / STOP  
禁止：
- 任何捷徑
- 未入 Index 文件引用

#### L9a｜Analyst Narrative & Investment Rationale（分析師人話敘事）
（分析師人話整合報告層）

#### 定位說明
L9a 為 **分析師敘事層（Human-Readable Investment Narrative）**，  
其存在目的不是流程裁決，而是對人類輸出可理解、可查證的投資分析敘事。

**L9a 僅能在 L9（Governance / Decision Gate）通過後啟動，  
不具流程裁決權，亦不具任何交易授權能力。**

L9a 的核心問題是：

> **「為什麼這個標的值得被人類進一步考慮？」**

---

#### 核心職責（必須具備）
L9a 輸出的分析報告，必須以白話方式完整說明：

1. **前因事由**
   - 為何該標的進入觀察或分析名單
   - 觸發來源為何（消息 / 基本 / 技術 / 籌碼 / 策略）

2. **現況判斷**
   - 目前市場與個股所處 Regime
   - 現行價位是否合理，是否偏離結構或歷史區間

3. **投資假設**
   - 若進場，核心邏輯與成立條件為何
   - 假設成立時可能對應的時間尺度（短線 / 波段 / 長期）

4. **風險與不確定性**
   - 主要風險來源
   - 哪些情境發生時，原分析將失效或需重新評估

5. **可能的行動方向（非指令）**
   - 僅描述偏向觀察、偏向短線或偏向長期之分析傾向
   - 不構成任何交易指令、價格、數量或批准

---

#### Evidence 要求
- L9a 中所有關鍵敘述，**必須可回指至 L4–L8 所產生之 Evidence**
- 必須能被人類查證、質疑與反駁

---

#### 明確禁止
- L9a **不是下單層**
- L9a **不自動形成交易決策**
- L9a 的任何敘事，**僅作為 L10 人類決策之參考依據**

---
### L10｜Human Decision（人類裁決｜Authority）
（人類最終裁決層）

#### 定位說明
L10 為 TAITS **唯一且不可取代的人類決策層**。

所有交易相關行為，必須由人類在 L10 明確裁決後，
系統方可進入任何執行或模擬流程。

---

#### 人類可做的裁決
- 不進行任何行動
- 進行回測
- 進行模擬交易
- 進行半自動交易
- 進行全自動交易（需明確授權）

📌 **未經 L10 明確裁決，流程不得進入任何執行狀態。**

---
### L11｜Execution & Control（執行｜稽核｜維護）
（執行、稽核與系統維修層）

#### 定位說明
L11 為 **純系統層（Machine-Oriented Layer）**，  
其目的在於執行已授權行為、完整記錄、回放、診斷與維修系統。

L11 **不是分析層、不是人話報告層，也不是決策層**。

---

#### 核心職責
- 僅在 L10 明確授權後執行行為
- 記錄所有 Execution / Decision Trace / System State
- 產出完整 Audit Log
- 作為系統診斷與後續調整之依據

---

---

## 2. 全紀錄原則（Global Traceability Principle）
### 全紀錄原則（Global Traceability Principle）

TAITS 在所有層級（L1–L11）所產生的：

- 原始資料快照
- 分析結果與 Evidence
- L9a 分析師敘事報告
- L10 人類裁決紀錄
- L11 系統執行、稽核與維修工件

**皆必須完整保存、可追溯、可回放、可稽核。**

📌 **無紀錄者，制度上視為未發生，不具任何決策或執行效力。**

---

---

## 3. Canonical Boundary Declaration（最終聲明）
### Canonical Boundary Declaration（最終聲明）

- **流程裁決只存在於 L9**
- **分析敘事只存在於 L9a**
- **決策權只存在於 L10**
- **執行與系統維修只存在於 L11**

任何層級越權，皆視為違反 MASTER_CANON 架構母法。
---

---

## 4. 引用合法性最小規則（Minimum Legal Citation Format）
## G0. 適用範圍（Hard Boundary）

本 Addendum 僅處理下列事項（不創造新制度、不改寫主文）：
1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。  
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。  
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。  
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。  

本 Addendum **不處理**：
- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

- 本文件 `doc_key` 既有標示為 `MASTER_CANON`；本 Addendum 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

並統一裁決：
- 任何文件「是否可引用」＝以 DOCUMENT_INDEX 之 Authoritative Index（ACTIVE 表格）為準  
- 任何文件「治理等級 bucket」＝以 DOCUMENT_INDEX 之 A+ / A / B / C 分桶為準  
- 文件內自述之等級/狀態若與 Index 有張力：依 DOCUMENT_INDEX §6 採「保守處置」（STOP/RETURN/BLOCK；以既有 Gate/風控規範語義為準）

---

## G2. 子級標籤（Label）之唯一合法解讀（S / B+ / C+）

凡本文件或引用鏈中出現：
- `S`：視為「Supreme Canon 的顯示標籤」或「完備度標籤」，**不構成**新的治理等級 bucket。  
- `B+` / `C+`：視為「嚴格度/完備度子級標籤」，**不構成**新的治理等級 bucket。  

治理覆蓋規則仍固定為：**A+ > A > B > C**（以 DOCUMENT_INDEX 為準）。  

---

## G3. DATA_UNIVERSE（alias）封口（資料治理引用回歸 DATA_SOURCES）

統一裁決：
- 任何出現之 `DATA_UNIVERSE` 一律視為「資料宇宙（Data Universe）」概念別名（alias），**不得**作為 doc_key。  
- 任何需要引用資料來源治理時，唯一合法 doc_key：`DATA_SOURCES`。  
- 若 Evidence/Audit/UI Trace/Gate 引用欄位出現 `doc_key=DATA_UNIVERSE`：  
  - 一律視為「引用非法」→ 依 GOVERNANCE_GATE_SPEC 進行 BLOCK/RETURN（依其既有語義；不得補救）。

---

## G4. 最小可稽核引用格式（Minimum Legal Citation Format｜可直接貼用）

凡聲稱「依據治理文件」之輸出（含：Evidence、Risk/Compliance、Governance Gate、UI Decision、Execution Control、Audit）一律必須同時提供：

```text
ref_doc_key = <DOC_KEY>
ref_file = <完整檔名>
ref_version = <版本日期或檔名日期碼>
ref_section = <章節定位（§ / Heading Path）>
ref_purpose = <用途：例如 gate_check / risk_veto / ui_decision / execution_policy / audit_replay>
ref_notes = <可選：alias/Label 解讀備註>
```

缺任一欄位：
- 依 DOCUMENT_INDEX §6 採保守處置：不得形成裁決性輸出（PASS/APPROVE/EXECUTE 等）；必要時 RETURN/BLOCK。

---

## G5. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫本文件任何既有條款。  
- 本 Addendum 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。  
- 本 Addendum 目的僅在於消解引用歧義、避免 Gate 因 metadata/格式缺口而誤判，並確保全鏈路可稽核、可回放。

（Addendum 2025-12-28｜Only-Add｜Freeze v1.0 完）

---

# Addendum 2025-12-28｜Only-Add：ERRATA_PATCH_0001（占位行「...」非規範性宣告）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md（doc_key：MASTER_CANON）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0023`）  
> 目的：消解本文件「Addendum 2025-12-28｜GLOBAL_ALIGNMENT_PATCH」中出現之單行占位字元（`...`）可能造成的裁決/稽核歧義；不改寫任何既有正文條款。

---

---

## 5. 本版整併紀錄（Consolidation Record）
- 本版已將「L9a / L10 Authority / L11 Audit & Maintenance」由原附錄/附加章節模式，整併進 L9–L11 正文，避免閱讀與權限混用歧義。
- 本版已移除「占位字元（...）」並以可稽核內容替換，避免誤讀為缺漏條款或待授權占位。
- 原先散落於附錄之治理識別、Index Gate、最小引用格式等條款，已集中收斂為本版 §0 與 §4，形成單一路徑。
