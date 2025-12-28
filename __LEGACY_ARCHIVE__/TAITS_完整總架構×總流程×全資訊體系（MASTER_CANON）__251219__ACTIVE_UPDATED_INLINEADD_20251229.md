> 【ACTIVE 更新版｜ADD 內嵌修訂】本檔已將最新 Addendum 之有效口徑內嵌至正文（閱讀主線只保留最新有效規則）。
> 原始附錄／稽核留痕仍保留於文末（如存在），僅供追溯，不作為正文裁決口徑。
> 若出現單獨一行且內容完全等於 `...` 者，依本文件內之 ERRATA 規則視為 Non-Normative Artifact（不參與裁決）。

> 【整合輸出｜ACTIVE 版本】本檔為「ADDENDUM 融合後之最新有效版本」。
> 合併規則：若 ADDENDUM 與舊內容牴觸，以 ADDENDUM 為準。
> 產出日期：2025-12-29（Asia/Taipei）
> 來源檔案：TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md

# TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219
doc_key：MASTER_CANON  
治理等級：S（Supreme Canon｜最高裁決母體）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（最高母法，Only-Add 演進）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / DOCUMENT_INDEX  
平行參照：FULL_ARCH / ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES / STRATEGY_UNIVERSE / STRATEGY_FEATURE_INDEX / LOCAL_ENV / DEPLOY_OPS / TWSE_RULES / README  
變更原則：Only-Add（僅可新增，不可刪減／覆寫／改寫語義）  

---

---

# Addendum 2025-12-27｜Only-Add：治理等級對齊（S 標籤定位）× 裁決順序字串消歧 × 章內等級標示回歸 Index（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md（doc_key：MASTER_CANON）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：Index Gate（DOCUMENT_INDEX）＋治理等級覆蓋（A+ > A > B > C）＋衝突裁決程序（DOCUMENT_INDEX §6）＋AI_GOV（A+）最高約束  
> 口徑對齊：DOCUMENT_INDEX｜Addendum 2025-12-27（裁決順序字串統一 × 歧義消解）  
> Gate 對齊：GOVERNANCE_GATE_SPEC｜Addendum 2025-12-27（字串助記定位 × 雙軌裁決消歧）  
> 目的：在不改寫既有正文的前提下，消弭本文件內外「治理等級／裁決順序字串／章內等級標示」的歧義來源，確保後續引用（含新對話啟動、Gate 裁決、稽核回放）具一致且可回放之口徑。

---

## 0. 適用範圍（Hard Boundary）

本 Addendum 僅處理三類歧義，不新增任何新制度權力：

1) 文件檔頭中出現「治理等級：S」與 DOCUMENT_INDEX 之 A+/A/B/C 治理等級體系的對位解釋  
2) 文件內出現之「裁決順序字串」（箭頭排序／高→低順位）的法律定位（助記 ≠ 覆蓋規則）  
3) 文件內部段落對其他文件所標示的括號等級（A+/A/B/C/S/…）之權威來源回歸（以 Index 表格裁決為準）

---

## 1. 「S（Supreme Canon）」之法律定位（Label ≠ Governance Grade）

### 1.1 定義：S 為「版本/敘事標籤」，非治理等級
本文件檔頭所載「治理等級：S（Supreme Canon｜最高裁決母體）」在 Freeze v1.0 下之唯一合法解讀為：

- **S 僅為本文件之敘事/版本定位標籤（Label）**：表示「整合版 Canon」之編纂目的與閱讀定位  
- **S 不屬於治理等級**，不得被用於覆蓋或改寫 A+/A/B/C 的治理等級覆蓋規則  
- 文件之「治理等級 / ACTIVE 狀態 / doc_key」等身份性中繼資料，**一律以 DOCUMENT_INDEX 表格裁決為準（Index Gate）**

> 兼容說明（不改原文）：本文件正文 §1.1 已載「治理等級：A（Canonical）」之敘述；  
> 本 Addendum 將其確立為「治理等級之唯一可採用口徑」，而 S 退位為版本標籤（Label）。

---

## 2. 「裁決順序字串」之法律定位（Mnemonic ≠ Override Rule）

### 2.1 統一原則：所有排序字串一律視為助記
凡本文件內出現之以下類型表述：

- `X → Y → Z` 之箭頭排序（例如：Index / Arch / Canon 之排列）  
- 「高 → 低」之順位清單（例如：章內所列衝突裁決秩序）

一律視為 **閱讀／操作助記（Mnemonic）**，不得被解讀為：

- 治理等級覆蓋規則（A+ > A > B > C）之替代品  
- 裁決權重新分配（例如「某文件凌駕 AI_GOV」或「Index 凌駕 A+」）  
- 跳過 DOCUMENT_INDEX §6 衝突裁決程序之依據

### 2.2 張力處置：遇衝突一律回到 DOCUMENT_INDEX（不可跳步）
若任何字串與 DOCUMENT_INDEX 正文之治理等級覆蓋或衝突裁決程序產生張力：
- 一律以 DOCUMENT_INDEX 正文（§3／§6／§7／§9）為準  
- 該字串在張力範圍內不具裁決力  
- 必要時以 VERSION_AUDIT 留痕（Append-only）

---

## 3. 章內「括號等級標示」之權威來源（Index-First）

### 3.1 統一原則：括號等級僅作閱讀提示，非裁決依據
本文件內部（包含但不限於 §15「衝突裁決秩序」）對他文件所標示的括號等級（例如：A+ / A / B / S / B+ / C+ 等）：

- 一律視為「閱讀提示／歷史標記／敘事標籤」  
- 不得作為裁決依據或覆蓋規則依據  
- 任何裁決時，該文件之治理等級與 ACTIVE 狀態 **以 DOCUMENT_INDEX 表格裁決為準**

### 3.2 保守規則（Safety）：等級不明則不得裁決
若引用端無法取得該文件在 DOCUMENT_INDEX 中之治理等級／ACTIVE 狀態：
- 僅允許 Descriptive Output（描述/列缺口）
- 禁止裁決性輸出（PASS/VETO/RETURN/STOP）
- 必須返回補齊 Index 引用（doc_key / version_date / section_path）

---

## 4. 最終宣告（針對本 Addendum）

- 本 Addendum 僅作歧義消解與口徑統一，不改寫 Canonical Flow（L1–L11）與既有正文任何條款。  
- 在 Freeze v1.0（Only-Add）期間，本文件對外引用與對內裁決，一律遵循：  
  **Index Gate（DOCUMENT_INDEX）→ 治理等級覆蓋（A+ > A > B > C）→ 衝突裁決程序（DOCUMENT_INDEX §6）→ 稽核留痕（VERSION_AUDIT）**  
- S（Supreme Canon）保留為「整合版 Canon」之版本/敘事標籤，不構成治理等級、也不構成覆蓋規則之例外。

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）


## 0. 文件定位（Canonical Master｜最大完備整合版）

本檔為 **MASTER_CANON 的「最終整合單檔版」**（Final Integrated Edition）。  
本版本的整合原則為：

- **原有正文內容「原封不動保留」**（不刪、不縮、不改義）  
- 僅以 **Only-Add** 方式補齊：文件宇宙分類、引用合法性、衝突裁決、以及「新對話/新 AI 啟動行為規範」  
- 所有新增章節均以本檔的 **治理等級 S** 進行裁決性落地，供 `DOCUMENT_INDEX` 建立引用與衝突裁決秩序

---

## 【Canonical 使用與解讀指引（Normative Reading Guide）】

本文件（MASTER_CANON）為 TAITS 之最高架構母法（Canonical Constitution），
其目的在於：

1. 定義 TAITS 各層級（L1–L11）之存在性、責任邊界與不可越權原則  
2. 鎖定人類、AI 與系統之分工關係與治理裁決順序  
3. 防止任何角色（人或系統）對層級職責產生混用、誤用或越權解讀  

### 重要解讀原則（強制）

- 本文件中所描述之分析項目、敘事責任與品質要求，  
  屬於「合格標準與語義邊界定義（Normative Boundary）」，  
  **不代表每次實際運行時，必須完整逐項輸出。**

- 實際分析輸出之深度、形式與篇幅，  
  得依市場情境、風險等級與人類決策需求彈性調整，  
  **惟不得違反本 Canon 所定義之層級語義與不可越權原則。**

- 任何文件、模組、AI 行為或工程實作，  
  若與本文件之語義邊界發生衝突，  
  **一律以 MASTER_CANON 為最終裁決依據。**

本指引為解讀與使用說明，  
不構成新增流程、層級或權限之修改。

---

## 附錄A｜原始正文（保留不改）

# TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）
## Taiwan Alpha Intelligence Trading System

---

## Canonical 前言（Why This Canon Exists）

本文件為 **TAITS 的 Canonical Master 文件**。

若《MASTER_ARCH》回答的是：
> **「什麼永遠不能被違反？」**

那麼《MASTER_CANON》回答的是：
> **「TAITS 是如何被正確地運作？」**

本文件的存在目的不是加速交易，  
而是確保 **任何一筆交易的生成，都經過可回放、可審計、可否決的完整過程**。

---

## 第 1 章｜MASTER_CANON 的法律地位與使用規則

### 1.1 文件位階
- 治理等級：**A（Canonical）**
- 位階關係：
  - 受制於：`MASTER_ARCH`
  - 上位於：`ARCH_FLOW`、`FULL_ARCH`、`RISK_COMPLIANCE`、`EXECUTION_CONTROL`

📌 下位文件**不得推翻**本文件定義之 Canonical 順序與責任分層。

---

### 1.2 Canonical 的唯一裁決權
本文件具有以下裁決功能：

- 定義全流程 Canonical 順序（L1–L11）
- 定義每層不可跳步與不可越權條款
- 定義 Evidence 與 Veto 的法律地位
- 定義多模式一致性（Research / Backtest / Simulation / Paper / Live）

---

### 1.3 使用規則（Mandatory）
使用 TAITS 的任何人、任何 Agent、任何模組：

- **必須依 Canonical 順序運作**
- 不得以「效率」為由跳層
- 不得以「策略」為由越權至 Execution
- 不得以「績效」為由弱化 Risk/Compliance

---

## 第 2 章｜TAITS Canonical Flow（L1–L11）

> Canonical Flow 是 TAITS 的唯一合法交易生成路徑。

---

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
（內嵌修訂：依 Addendum／若牴觸以最新附加口徑為準）

目的：檢查流程完整性與文件一致性。

輸入：Strategy Proposal + Flow Trace  
輸出：PASS / RETURN / STOP  
禁止：
- 任何捷徑
- 未入 Index 文件引用

---

### L9a｜Analyst Narrative & Investment Rationale
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

### L10｜Human Decision Authority
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

### L11｜Execution, Audit & System Maintenance
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

### Canonical Boundary Declaration（最終聲明）

- **流程裁決只存在於 L9**
- **分析敘事只存在於 L9a**
- **決策權只存在於 L10**
- **執行與系統維修只存在於 L11**

任何層級越權，皆視為違反 MASTER_CANON 架構母法。
---

## 第 3 章｜Canonical Flow 的不可破壞公理（5 Axioms）

1. **Forward-only**：流程只能前進或中止，不得偷偷回寫修正。  
2. **Layer Isolation**：每層只做該層責任，不得越權。  
3. **Evidence First**：沒有 Evidence 不得判斷/不得放行。  
4. **Veto > Proposal**：否決優先於建議。  
5. **Human不可被取代**：L10 必須由人類完成。

---

## 第 4 章｜多模式一致性（Research / Backtest / Simulation / Paper / Live）

### 4.1 不變項（Invariant）
- L1–L11 順序不可變
- Risk/Compliance Gate 不可降級
- Human-in-the-loop 不可移除
- Audit/Replay 不可降低密度

### 4.2 可變項（Only 3）
- 資料來源（歷史/即時）
- 時間推進（模擬/真實）
- Execution 開關（真實/模擬）

---

## 第 5 章｜Evidence 的法律地位

### 5.1 Evidence ≠ 指標
Evidence 是可審計、可追溯、可回放的證據組合。

### 5.2 Evidence 的必備屬性
- provenance（來源鏈）
- completeness（完整性）
- immutability（不可變）
- replayability（可回放）

---

## 第 6 章｜Veto 的法律地位（最高否決權）

### 6.1 Veto 不可被覆寫
- 任何 VETO：流程必須停止或退回
- Human 不得覆寫 Risk/Compliance 的 VETO（不得為例外）

### 6.2 Veto 必須具 reason codes
禁止以「注意」「建議」取代否決理由。

---

## 第 7 章｜Canonical 與策略宇宙的關係

### 7.1 策略只是候選，不是指令
策略輸出只能是 Proposal。

### 7.2 策略不可跳過 Canonical
任何策略若試圖跳過 L1–L11，視為違規。

---

## 第 8 章｜AI 在 Canonical 中的角色（非主體）

### 8.1 AI 的合法位置
AI 可出現在：
- L4（特徵/分析輔助）
- L5（證據組裝輔助）
- L6（Regime 判讀輔助）
- L8（策略候選生成輔助）
- L10（解釋與可視化輔助）

### 8.2 AI 的禁止位置
AI 不得：
- 代替 L10 裁決
- 直達 L11 下單
- 覆寫否決

---

## 第 9 章｜Audit / Replay 的母體規則

### 9.1 無紀錄 = 未發生
任何層級若無審計物，制度上視為未發生。

### 9.2 Replay 必須可重建
相同 Replay Bundle 必須可重建相同結論；否則視為污染。

---

## 第 10 章｜版本一致性與 Only-Add 演進

### 10.1 Only-Add
- 允許新增章節、條款、欄位
- 禁止刪減、覆寫、改義

### 10.2 舊回放必須可讀
新版本不得破壞舊 Replay 可驗證性。

---

## 第 11 章｜下位文件一致性要求（Mapping）

### 11.1 Canonical 條款 → 文件責任對位
| Canonical 條款 | 下位文件 |
|---|---|
| L1-L2 Data | DATA_SOURCES / LOCAL_ENV |
| L3 Snapshot | ARCH_FLOW / VERSION_AUDIT |
| L4 Analysis | STRATEGY_FEATURE_INDEX |
| L5 Evidence | ARCH_FLOW / VERSION_AUDIT |
| L6 Regime | STRATEGY_UNIVERSE / ARCH_FLOW |
| L7 Veto | RISK_COMPLIANCE / TWSE_RULES |
| L8 Proposal | STRATEGY_UNIVERSE |
| L9 Gate | DOCUMENT_INDEX / UI_SPEC |
| L10 Human | UI_SPEC / EXECUTION_CONTROL |
| L11 Execution | EXECUTION_CONTROL |

📌 下位文件若與本表不一致，**以本表為準**。

---

### 12.2 下位文件的最低責任
每一份下位文件，**至少**必須回答：
1. 我實作了哪一條 Canonical 條款？
2. 我在哪個流程層級生效？
3. 我的審計輸出是什麼？

---

...
而是為了讓系統**永遠保持可問責**。

在 TAITS 中：

- 快速但不可審計 → **不可接受**  
- 聰明但不可否決 → **不可接受**  
- 有績效但違反流程 → **不可接受**

> **只有當一套系統，  
> 能在誘惑、壓力與績效面前，  
> 仍然選擇遵守流程與責任，  
> 它才配被稱為「Canonical」。**

---

---

## 13. 文件宇宙的最終分類（Document Ontology｜為 DOCUMENT_INDEX 鋪路）

TAITS 的所有文件，**必須被歸入以下四類之一**。  
此分類是「引用合法性」與「衝突裁決」的根基，並將被 `DOCUMENT_INDEX` 作為 Index 裁決與審計輸出的核心欄位。

### 13.1 Normative（規範性文件｜具約束力）
定義：直接產生「必須 / 禁止 / 否決 / 裁決」制度效果。任何實作若與之衝突，視為違規。  
典型範圍：MASTER_ARCH、MASTER_CANON、RISK_COMPLIANCE、EXECUTION_CONTROL、VERSION_AUDIT（含其明確裁決條文）。

### 13.2 Procedural（程序性文件｜操作與落地程序）
定義：規範「怎麼做」的程序與作業標準，但不得推翻 Normative 的鐵律與否決權。  
典型範圍：DEPLOY_OPS、LOCAL_ENV、BEGINNER_GUIDE（新手教學）等。

### 13.3 Descriptive（描述性文件｜系統說明與架構地圖）
定義：描述系統如何組成、如何流動、如何呈現；不直接裁決「可/不可」，但必須與 Normative 一致。  
典型範圍：FULL_ARCH、ARCH_FLOW（其流程規範屬 Canon 之落地，仍具規範性但主要呈現方式為描述+規格）、UI_SPEC（介面規格承載規範義務）。

### 13.4 Reference（參考性文件｜外部制度/資料入口/備忘）
定義：提供來源、條文入口、外部規則彙整或查詢指引；本身不構成 TAITS 內部裁決，但可作為 Evidence/Compliance 來源引用。  
典型範圍：TWSE_RULES（含官方入口）、資料來源官方 API 入口與第三方資料補充等。

---

## 14. 引用合法性（Citation Legality｜新對話與實作的共同硬門檻）

### 14.1 Index 先決（Index-First）
- **任何裁決性輸出（含 PASS/VETO/RETURN/STOP）必須引用 DOCUMENT_INDEX 中 ACTIVE 的 doc_key。**
- 引用未入 Index 或非 ACTIVE 文件：視為 `GOV-DOC-01` 類違規。

### 14.2 引用最小格式（Minimum Citation Format）
任何裁決性輸出至少包含：
- `doc_key`
- `version_date`
- `section_path`（至少到章節）
- `why_used`（用於裁決什麼）

缺任一項：不得做裁決性輸出，只能做描述或列出缺口。

### 14.3 官方來源優先（Official-First for Rules）
涉及制度/交易規則/合規裁決時：
- **官方入口為最終裁決來源**（TWSE/TAIFEX/FSC/SFB/TDCC 等）
- 第三方僅可作補充與提示，不得作最終裁決依據

---

## 15. 衝突裁決秩序（Conflict Resolution Order｜母體級裁決）

當文件、模組或 Agent 之間產生衝突時，裁決順序如下（高 → 低）：

1) TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
2) MASTER_ARCH（A+）  
3) MASTER_CANON（S，本文件）  
4) DOCUMENT_INDEX（A，Index 裁決與 ACTIVE 管理）  
5) RISK_COMPLIANCE（A，最高否決權）  
6) EXECUTION_CONTROL（A，執行與控制硬門檻）  
7) VERSION_AUDIT（A，版本與回放一致性）  
8) ARCH_FLOW（B+，Canonical Flow 細化）  
9) FULL_ARCH（B，架構地圖）  
10) UI_SPEC / DEPLOY_OPS / LOCAL_ENV / DATA_SOURCES / STRATEGY_* / TWSE_RULES / README 等（依 Index 的治理等級與性質裁決）

任何「低位階文件」不得推翻「高位階文件」的語義或否決權。

---

## 16. Canonical Flow（L1–L11）與權限邊界的母法對位（母體級）

> 本節為 MASTER_CANON 的最終對位：確保「策略 ≠ 決策 ≠ 下單」在制度上不可被偷換。

### 16.1 L1–L11 不可跳步（Non-Skippable）
- L1–L11 之順序不可跳步（ARCH_FLOW 定義細節）
- 任何模式（Research/Backtest/Sim/Paper/Live）不得以方便為由跳層

### 16.2 三權分立（Decision Separation）
- **策略（Strategy）**：只產生「條件與情境」，不得直連下單（L8）
- **裁決（Decision）**：必須由 Human-in-the-loop 完成（L10）
- **執行（Execution）**：必須持有 Risk PASS Token 且通過執行層硬門檻（L11）

---

## 17. 新對話 / 新 AI 的啟動行為規範（Canonical Onboarding & Guardrails）

### 17.1 啟動目的（Purpose）
新對話 / 新 AI 的啟動，不是為了快速結論或快速交易，而是確保：
1) 不走偏（No Drift）  
2) 不越權（No Overreach）  
3) 可追責（Accountable）  
4) 一致性（Consistency）

### 17.2 啟動必經程序（Mandatory Boot Procedure）
若未完成 Boot Procedure，任何「建議/結論/策略候選」輸出均視為不合規。

#### Boot Step 0｜身份與邊界宣告（必做）
必須宣告：
- 系統身份：TAITS（台灣市場、Regime 優先、Risk/Compliance 最高否決）
- 權限邊界：策略 ≠ 下單；AI ≠ 裁決；Risk 可否決一切
- 文件主權：所有裁決以 DOCUMENT_INDEX + 上位母法為準

#### Boot Step 1｜Canon Set 裝載確認（必做）
必須建立 Documents Active Map，最少包含：
- AI 母法（A+）
- MASTER_CANON（S）
- MASTER_ARCH（A+）
- DOCUMENT_INDEX（A）
- RISK_COMPLIANCE（A）
- EXECUTION_CONTROL（A）
- VERSION_AUDIT（A）
- ARCH_FLOW（B+）
- FULL_ARCH（B）
- UI_SPEC（Normative 義務）

若缺任一項：
- 必須標示：`Missing Canon: <doc_key>`
- 並限制輸出範圍（不可自行補洞）

#### Boot Step 2｜模式宣告（必做）
必須宣告 Mode（Research/Backtest/Simulation/Paper/Live），並承諾不改變 L1–L11、公理、否決權與 Human-in-the-loop。

#### Boot Step 3｜引用規範啟動（必做）
一旦做裁決性輸出，必須附帶：
- doc_key / version_date / section_path / why_used  
否則只能描述或列缺口。

---

## 18. 新對話輸出類型的合法分級（Output Legality Tiers）

### 18.1 Tier-0｜描述（Descriptive Output）
允許：轉述、梳理、建立地圖、指出缺口。  
禁止：產生交易方向、形成執行意圖。

### 18.2 Tier-1｜候選建議（Proposal Candidates）
允許：策略候選（僅 L8 語義）、Regime 範圍（含不確定性）、風險映射（可能觸發條款）。  
硬限制：必須標示適用/禁用條件；必須聲明未經 L10 不可執行；必須可追溯 Evidence。

### 18.3 Tier-2｜流程裁決（Flow Decision for System Only）
允許：RETURN/STOP 判定（依 ARCH_FLOW），缺審計/缺版本引用阻斷（依 VERSION_AUDIT）。  
禁止：裁決是否應交易。

### 18.4 Tier-3｜執行相關輸出（Execution-Adjacent）
裁決：新對話不得輸出任何可被直接轉成下單的內容（價格/數量/時間等作為建議、立即買賣指令、暗示已批准等）。  
若使用者要求：必須導向 UI_SPEC 與 EXECUTION_CONTROL 的 Human-in-the-loop 流程，並要求完成 L7/L10/L11 前置條件。

---

## 19. 新對話常見偏移模式（Drift Patterns）與硬阻斷

### 19.1 文件偏移（Doc Drift）
- 引用未入 Index 或非 ACTIVE  
- 以「我記得」替代引用  
處置：STOP（GOV-DOC-01 / GOV-FLOW-01），要求補齊 Index 或改為描述性輸出。

### 19.2 邊界偏移（Boundary Drift）
- 策略輸出變決策（例如「所以就買」）  
- AI 自己批准  
- 風控否決被弱化成提醒  
處置：STOP（RISK / GOV），UI 必須標示違規建議（UI_SPEC）。

### 19.3 模式偏移（Mode Drift）
- Research 省略風控語義  
- Backtest 跳過審計  
- Simulation 改寫流程順序  
處置：STOP + Audit 記錄（VERSION_AUDIT）；「模式不同」辯護無效。

---

## 20. 新對話的最小證據法則（Minimum Evidence Law）

新對話若要提出 Tier-1（候選建議），必須具備最小 Evidence Bundle：
- snapshot_ref（L3）
- feature_set_ref（L4）
- evidence_provenance_ref（L5）
- regime_state_ref（L6）
- risk_gate_status_ref（L7：至少能說明尚未放行或已放行）

缺任一項：只能 Tier-0 或 Tier-2，禁止候選策略輸出。

---

## 21. 新對話的提問規範（When Must Ask for Instruction）

### 21.1 必須請示（Hard Ask Conditions）
- 文件缺失或版本不明  
- 需要新增 doc_key 或新增文件類型  
- 需要新增策略白名單或策略分類  
- 需要新增風控門檻政策（policy profile）  
- 需要修改衝突裁決順序或治理等級  

### 21.2 可自治（Allowed Autonomy）
- 文字更清晰（不改義）  
- 增加章節、補齊 checklist、補齊 reason codes（Only-Add）  
- 補充官方網址入口（Reference 擴充）  
- 補充審計欄位（不刪舊）  

---

## 22. 新對話審計輸出最小格式（Conversation Audit Stub）

新對話每次產出 Tier-1 或 Tier-2 內容，必須附帶最小審計 stub（供 UI/Log 捕捉）：
- conversation_id（或等價）
- timestamp_utc
- mode
- output_tier
- docs_active_map_ref
- citations[]（doc_key@version_date#section_path）
- missing_items[]（若有）
- reason_codes[]（若含阻斷/否決/退回）

---

## 23. 新對話與 DOCUMENT_INDEX 的對接規則（Index Coupling Rules）

DOCUMENT_INDEX 必須做到：
1) 新對話能快速得知 ACTIVE 文件與治理等級  
2) 新對話能判斷允許引用哪些文件來做裁決，以及衝突裁決順序  
3) 新對話能快速生成 citations[]（doc_key@version_date#section_path）

---

## 24. Only-Add 演進規則（本整合版新增章節專屬）

允許新增：
- 新的 Output Tier（不得弱化既有禁止）  
- 新的 Drift Pattern 與 reason_code  
- 更嚴格的 Boot Procedure（不可放寬）  
- 更完整的 Conversation Audit Stub 欄位  

禁止：
- 刪除 Boot Procedure 任一步  
- 允許 AI 自行批准或越權到 L11  
- 允許未入 Index 文件被引用作裁決  
- 允許模式降級審計密度  

（MASTER_CANON｜Final Integrated Edition v2025-12-19 完）
---

## Appendix 2025-12-28｜Only-Add：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md（doc_key：MASTER_CANON）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 Addendum/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`MASTER_CANON`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=MASTER_CANON` + `canonical_filename=TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

# Addendum 2025-12-28｜Only-Add：GLOBAL_ALIGNMENT_PATCH（MASTER_CANON 對齊全域補丁）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md（doc_key：MASTER_CANON）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0008`）  
> 目的：以 MASTER_CANON 為主導，對齊「引用合法性、doc_key 身份、子級標籤（Label）解讀、資料治理別名（alias）封口、最小可稽核引用格式」之全域一致口徑；不改寫任何既有正文條款。

---

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

## E1. 問題描述（僅限本文件內之字面占位）
在本文件既有內容中，出現一行單獨的三點占位字元：

- `...`

該行屬於**編排/輸出過程的字面占位殘留**，不承載治理語義、亦不構成任何缺漏之暗示。

## E2. 裁決（Non-Normative Artifact）
自本 Addendum 生效起，對本文件之任何讀取、稽核、回放、或 Gate 解析：

- 凡遇到**單獨一行且內容完全等於 `...`**者，均視為 **Non-Normative Artifact（非規範性編排殘留）**。  
- 該行在裁決鏈中應被**忽略**，不得被解讀為：缺失段落、待補條款、或可由任何人/任何 Agent 自行補完之授權。  
- 本文件其餘內容之可讀性與完整性不受影響；既有條款仍以原文為準。

## E3. Freeze v1.0 下之處置邊界（Only-Add）
- Freeze v1.0 期間：**不得**以「刪除該行」方式改寫既有正文；僅以本 Addendum 形式完成裁決封口。  
- 非 Freeze（未來版本）若需進行格式層級清理，必須走 DOCUMENT_INDEX 定義之治理閘門與版本稽核流程，不得在 Freeze v1.0 內回溯改寫。

## E4. 最終宣告
- 本 Addendum 為 Only-Add；不改寫本文件任何既有條款。  
- 本 Addendum 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。

（Addendum 2025-12-28｜Only-Add｜Freeze v1.0 完）
