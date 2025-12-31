# TAITS_S1｜交易執行與控制規範（EXECUTION_CONTROL）

doc_key：EXECUTION_CONTROL  
版本：TAITS_S1_v1.0__251231  
生效日期：2025-12-31  
治理定位：S1（Engineering Single Source｜工程唯一口徑）  
適用範圍：TAITS 工程實作（Cursor / Codebase / Prompt / Agent Wiring）  
裁決說明：本 S1 套件用於「工程一致口徑」；母法裁決位階不變（DOCUMENT_INDEX → MASTER_ARCH → AI_GOV）。  
禁止事項：工程端不得引用任何歷史舊版內容作為解釋依據，以避免語義漂移與腦補。

---
## S1｜L9–L11 終局定位（唯一正確口徑）

> 本節為 **TAITS_S1** 的「終局語義鎖定」，適用於所有工程實作、提示詞、文件解釋與程式生成。
> 任何文件（含歷史版本）若與本節不一致，皆視為無效；工程端不得引用或回填錯誤語義。

### L9｜投資報告層（Investment Report Layer）
- **目的**：產出「人類可讀」且「可追蹤」的完整投資報告，用於你在 L10 做最終裁決之前的資訊理解與方案評估。
- **必備內容（不可省略）**  
  1. **數據**：關鍵指標數值、區間變化、統計摘要（來源與時間戳須可追溯）  
  2. **圖形**：至少包含趨勢/區間/事件標註等可視化（可為文字描述的圖形規格，工程端可再渲染）  
  3. **進出價格建議（僅建議，非下單）**：  
     - 進場/加碼/減碼/出場/停損/停利的「價格區間」與「觸發條件」  
     - 必須附上假設、風險點、失效條件  
  4. **標的化追蹤（Tracking）**：  
     - `tracking_id`（唯一鍵）＋ `report_version`＋ `as_of`（資料截點）  
     - 明確記錄「本次報告」對同一標的的延續關係（不是一次性解說）
- **輸出定位**：L9 是「你要看的報告」，不是 Gate、不是下單、不是稽核。

### L10｜人類裁決與交易授權層（Human Decision & Trade Authorization）
- **目的**：由你（人類最高決策者）對 L9 報告與全系統輸入做最終裁決，並決定執行模式與授權邊界。
- **L10 必須輸出**  
  - `decision`：NO_ACTION / BACKTEST / SIMULATION / PAPER / LIVE  
  - `automation_mode`：MANUAL / SEMI_AUTO / FULL_AUTO（只是一種授權模式，不改變「人類為最終裁決者」之治理原則）  
  - `authorization_envelope`：允許的標的範圍、下單上限、風控條件、撤銷條件、有效期限  
  - `rationale`：裁決理由（需可稽核、可追溯）
- **邊界**：L10 是裁決與授權；實際執行仍受 **Risk/Compliance 最高否決權**與執行控制規範約束。

### L11｜工程稽核回放層（Engineering Audit & Replay）
- **目的**：對 **L1–L11 全層**進行工程稽核、回放與可追溯驗證，用於你檢視系統是否合理、是否需要調整。
- **L11 必須是「雙料輸出」**  
  1. **人類可讀（Human-Readable）**：讓你能看懂每層做了什麼、為什麼、依據是什麼、哪裡不確定  
  2. **工程可用（Machine-Readable）**：可被程式回放與對帳（hash、版本、參數、輸入輸出索引）
- **覆蓋範圍**：不是只稽核 L10；而是 **每一層都要留痕**，才能評估層級功能是否合理、是否要調整。
- **邊界**：L11 僅做稽核/回放/對帳，**禁止作為下單或執行入口**。

## S1｜本地運算環境基線（User Local Compute Baseline）

> 本節為 TAITS 工程端「固定基線」，用於避免對話或文件遺失導致 AI 重新腦補硬體條件。

- 裝置：ASUS FX504GE（筆電）
- 作業系統：Windows 11
- CPU：Intel Core i7-8750H（6C/12T）
- 記憶體（RAM）：32GB（已升級）
- GPU：NVIDIA GeForce GTX 1050 Ti
- GPU VRAM：4GB
- 儲存：256GB SSD + 750GB HDD（依實際可用空間調整）
- 建議本地推理定位（在此硬體條件下）：
  - 優先：L11 稽核摘要、L1/L2 抽取與欄位化、L5 證據包整理（使用 3B–7B 量化模型）
  - 不建議本地硬扛：高品質長篇 L9 報告主力、重推理整合（可採雲端主力＋本地稽核/抽取池）

## 規範正文（S1 重新整編｜僅保留正確口徑）

<!--
TAITS｜ACTIVE UPDATED（單檔內嵌更新版）
產出日期：2025-12-29（Asia/Taipei）
更新規格：單檔內嵌；可更新處直接更新並避免重複；不可更新處以 Appendix 內嵌 Only-Add 全文。
來源檔：TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md
-->

# TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219
doc_key：EXECUTION_CONTROL  
治理等級：A（Execution & Control Specification｜嚴格執行層最高規範）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（執行控制規範，Only-Add 演進）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：FULL_ARCH / ARCH_FLOW / RISK_COMPLIANCE / UI_SPEC / VERSION_AUDIT / DEPLOY_OPS / LOCAL_ENV / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化安全機制/偷換定義）  
核心鐵律：Human-in-the-Loop + Risk PASS Token Required + Kill Switch Always Available  

---

---

# Addendum 2025-12-27｜Only-Add：MASTER_CANON「S」標籤定位 × 母法對位口徑修補 × 引用合法性鎖定（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、弱化裁決權、偷換既有語義）  
> 適用文件：TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md（doc_key：EXECUTION_CONTROL）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：Index Gate（DOCUMENT_INDEX）＋治理等級覆蓋（A+ > A > B > C）＋衝突裁決程序（DOCUMENT_INDEX §6）＋AI_GOV（A+）最高約束  
> 口徑對齊：  
> - DOCUMENT_INDEX｜Addendum 2025-12-27（裁決順序字串統一 × 歧義消解）  
> - MASTER_CANON｜Addendum 2025-12-27（治理等級對齊：S 標籤定位）  
> - GOVERNANCE_GATE_SPEC｜Addendum 2025-12-27（字串助記定位 × 雙軌裁決消歧）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（建議新增條目：`VA-METADATA_FIX-20251227-0002`）  
> 目的：修補本文件內部對「MASTER_CANON（治理等級 S）」的引用語句，避免在 Freeze v1.0 期間造成治理等級體系漂移與 doc_key/等級誤用；並固定引用端的唯一合法口徑，使 Gate / Audit / UI Trace 可一致回放。

---

## 0. 適用範圍（Hard Boundary）

本 Addendum 僅處理「母法對位與治理等級標示」之歧義消解，**不改寫**本文件任何執行控制規則、委託流程、Kill Switch、回報格式或風控閘門語義。

- 不修改 Canonical Flow（L1–L11）  
- 不新增新的治理層級  
- 不改寫 A+ / A / B / C 覆蓋規則  
- 不弱化風險與合規否決權（如有適用）

---

## 1. MASTER_CANON「S」之法律定位（Label ≠ Governance Grade）

### 1.1 統一裁決：S 僅為敘事/版本標籤
凡本文件（含附錄）出現「MASTER_CANON（治理等級 S）」之表述，於 Freeze v1.0 下之唯一合法解讀為：

- **S（Supreme Canon）僅為 MASTER_CANON 的敘事/版本定位標籤（Label）**  
- MASTER_CANON 之「治理等級 / ACTIVE 狀態 / doc_key」等身份性中繼資料，**一律以 DOCUMENT_INDEX 表格裁決為準**  
- 因此，在治理等級體系中，MASTER_CANON 應視為 DOCUMENT_INDEX 裁決之 **A（Constitutional）｜ACTIVE**（不因 S 標籤而改變覆蓋規則）

> 兼容處理（不改原文）：本文件既有「治理等級 S」字樣保留為歷史敘事標籤；其治理等級法律效力由本 Addendum 限定並對齊 Index。

---

## 2. 母法對位引用口徑（Gate-Friendly Reference）

### 2.1 引用端唯一合法口徑（可直接貼用）
凡本文件需要引用 MASTER_CANON 作為「流程語義／層級邊界／越權判定」母法時，引用端應採以下最小合規格式：

```text
ref_doc_key = MASTER_CANON
ref_gov_grade = A            # 以 DOCUMENT_INDEX 表格裁決為準；S 僅為 Label
ref_doc_name = TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md
ref_section = <例如：§15 / §16 / Lx 對位段落>
ref_notes = S（Supreme Canon）僅為敘事/版本標籤；治理等級回歸 A+ / A / B / C 體系
```

### 2.2 禁止誤用（不可放寬）
- 禁止將 `ref_gov_grade = S` 作為任何裁決依據  
- 禁止以「S 標籤」推導 MASTER_CANON 可凌駕 DOCUMENT_INDEX 或 AI_GOV  
- 若引用端無法取得 DOCUMENT_INDEX 的治理等級裁決（例如缺少 Index 版本或 doc_key 不明）：僅允許描述缺口，禁止裁決性輸出（STOP/RETURN）

---

## 3. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）

本文件內若存在任何「裁決順序字串」或「高→低順位」的助記表述：
- 一律視為閱讀/操作助記（Mnemonic）  
- 若與 DOCUMENT_INDEX 正文 §3（治理等級覆蓋）或 §6（衝突裁決程序）產生張力：**一律回到 DOCUMENT_INDEX**（不可跳步）

---

## 4. 本 Addendum 對既有段落的適用方式（不改原文，只限縮解讀）

為維持 Freeze v1.0 之 Only-Add 原則：
- 本 Addendum 不覆寫任何既有段落  
- 僅對既有「治理等級 S」與「母法對位」用語給出**唯一可採用**之法律解讀口徑  
- 後續若需把「S」完整移除或重寫，必須在非 Freeze 狀態下走正式版本升級與全面審計流程

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）

## 0. 文件定位（Execution & Control Charter｜「怎麼執行」的最高規範）

本文件定義 TAITS 的「交易執行與控制」母規範，負責回答：

- 在 **Risk/Compliance 放行** 且 **人類裁決批准** 之後，系統如何**形成可執行意圖**並**嚴格執行**
- 如何在任何異常下 **即時中止（Kill Switch）** 與 **防止重複/錯誤下單**
- 如何落地 **Pre / In / Post Execution Logs**，確保可回放、可追責

📌 本文件的邊界（避免越權）
- 不定義交易制度法規條文全集（由 TWSE_RULES / 官方來源裁決）
- 不定義風控否決規則（由 RISK_COMPLIANCE 裁決）
- 不改寫 Canonical Flow（由 MASTER_CANON / ARCH_FLOW 裁決）
- 不定義 UI 外觀（由 UI_SPEC 裁決）
- 專注於「執行層如何確保：不該發生的交易不會發生；該中止時能立即中止」

---

## 1. 執行控制的核心目標（Execution Control Objectives）

1. **安全性優先（Safety First）**  
   任何情況下，避免錯誤下單/重複下單/超額下單/越權下單。

2. **可追溯性（Traceability）**  
   所有執行行為必須可回放、可追責、可稽核。

3. **可中止性（Abortability）**  
   Kill Switch 必須永遠可用，且可在任何狀態立即停止新單。

4. **一致性（Consistency Across Modes）**  
   Research / Backtest / Simulation / Paper / Live 的執行控制語義一致，差異僅在「是否連接真實券商」與「時間推進方式」。

---

## 2. 執行層輸入與輸出（Execution I/O Contract）

### 2.1 必要輸入（Required Inputs）
- `risk_pass_token`：Risk/Compliance 放行令牌（PASS Token）
- `intent_payload`：可執行意圖（symbol/side/qty/price/tif 等）
- `version_ref`：治理與策略版本參照（不可缺）
- `correlation_id`：端到端追溯 ID
- `mode`：Research / Backtest / Simulation / Paper / Live

### 2.2 必要輸出（Required Outputs）
- `order_plan`：下單計畫（可拆分、可驗證）
- `order_id_map`：券商回傳委託 ID 對照
- `execution_log`：Pre / In / Post 三段稽核物
- `replay_bundle_ref`：可回放包引用（包含所有必要工件與 hash）

---

---

## 4. Pre-Execution Checks（送單前檢核）

### 4.1 Gate 檢核（硬阻斷）
- Risk PASS Token 存在且有效
- Human APPROVE 簽章存在且可驗證
- version_ref 完整且可追溯
- mode 合法（不可偽裝為 Live）
- 交易時間/商品制度符合（引用官方制度入口）
- Kill Switch 目前可用（可立即觸發）

### 4.2 Idempotency Guard（去重防重送）
- 同一 `correlation_id + intent_hash` 不得重複送單
- 若重複請求 → 直接 BLOCK & AUDIT（不得靜默重送）

### 4.3 Circuit Breaker / Throttle（熔斷與節流）
- 風險事件（連續下單失敗、異常回報、延遲爆炸）觸發熔斷
- 熔斷後停止新單並進入 SAFE MODE

---

## 5. In-Execution Control（執行中控制）

### 5.1 Order State Machine（委託狀態機）
狀態示意：
- `PLAN_READY` → `SUBMITTED` → `ACKED` → `PARTIAL_FILLED` → `FILLED`
- 失敗/例外：
  - `REJECTED` / `CANCELLED` / `ERROR`

### 5.2 Kill Switch（緊急中止）
- 任何狀態可觸發 Kill Switch
- 觸發後：
  - 停止新單
  - 嘗試撤單/取消未成交委託（依券商能力）
  - 產生不可省略的稽核紀錄

---

## 6. Post-Execution Reconciliation（事後對帳與一致性）

### 6.1 對帳範圍
- 委託狀態、成交回報、資金/部位變動
- 與券商/帳務回傳一致

### 6.2 不一致處理（Hard Block）
- 對帳不一致 → STOP NEW ORDERS + REPAIR FLOW + AUDIT
- 禁止「先繼續送單再說」

---

## 7. 審計（Audit）三段式（Pre / In / Post）

### 7.1 Pre-Execution Log（送單前）
- Gate 檢核結果（含 reason_codes）
- Token/Signature/Version 驗證結果
- intent_hash / input_hash

### 7.2 In-Execution Log（送單中）
- 券商 API request/response 摘要（含 ack）
- order_state 轉移紀錄
- kill_switch_events（若有）

### 7.3 Post-Execution Log（送單後）
- 對帳結果（reconcile_report）
- fill 明細摘要
- output_hash / all_hashes

---

## 8. Broker Adapter（券商適配器）最低要求

- 必須可回報 ACK / REJECT / FILL
- 必須可撤單（若券商支援）
- 必須有重試策略但不可造成重複下單
- 必須可在 SAFE MODE 下被切斷

---

## 9. 模式差異（Mode Differences｜但語義一致）

- Research / Backtest：不連真實券商，仍需產出完整審計工件（可用模擬 ack/fill）
- Simulation / Paper：可連模擬撮合或券商模擬環境
- Live：連真實券商，所有硬條件更嚴格，不得降級

---

## 10. Kill Switch 的觸發條件（示例｜可 Only-Add 擴充）

- 人工手動觸發（最高優先）
- 券商連線異常
- 回報延遲超時
- 連續拒單/錯誤
- 對帳不一致
- 異常成交（價格/數量偏離合理範圍）

---

## 11. 必要的事件碼（Reason / Event Codes｜最小集）

- `E_NO_RISK_TOKEN`
- `E_NO_HUMAN_APPROVE`
- `E_INVALID_VERSION_REF`
- `E_IDEMPOTENCY_DUPLICATE`
- `E_BROKER_REJECT`
- `E_EXEC_ERROR`
- `E_KILL_SWITCH_TRIGGERED`
- `E_RECONCILE_FAIL`

---

## 12. 官方制度入口（執行層合規依據之官方來源）

> 執行層判定交易制度/時段/限制，必須能追溯到官方入口。

- TWSE 規章（Regulations）  
  https://twse-regulation.twse.com.tw/
- TWSE 交易制度（Trading Mechanism）  
  https://www.twse.com.tw/en/products/system/trading.html
- TAIFEX 規章（Rules & Regulations）  
  https://www.taifex.com.tw/enl/eng6/ruleRegulation
- FSC 金管會法規（Laws & Regulations）  
  https://www.fsc.gov.tw/en/home.jsp?id=3&parentpath=0
- SFB 證期局入口  
  https://www.sfb.gov.tw/en/

---

## 13. 版本與可追溯性（Version & Trace）

- 所有執行必綁 `version_ref`
- `version_ref` 缺失 → 直接阻斷
- 新版不得破壞舊 Replay（可回放性不得下降）

---

## 14. Replay Bundle（回放包）最低要求

- `documents_active_map`
- `intent_payload + intent_hash`
- `risk_pass_token`（可用引用與摘要，不得洩漏敏感內容）
- `human_approve_signature`
- `order_plan`
- `broker_ack/fill` 摘要
- `reconcile_report`
- `execution_logs`
- `all_hashes`

---

## 15. 緊急事件（Emergency）處置準則

- 一律先停止新單
- 產生稽核物
- 切 SAFE MODE
- 由人類決定是否恢復（不得自動恢復）

---

## 16. 禁止事項（Forbidden｜一票否決）

- 無 Risk PASS Token 送單
- 無 Human APPROVE 送單
- Kill Switch 不可用仍執行
- 缺 Pre/In/Post 任一審計物仍執行
- 靜默重送/靜默改單/黑箱補單
- 對帳不一致仍繼續送新單
- Execution 反向回寫策略/Regime（違反邊界）

---

## 17. 實作最小化建議（Implementation Minimums｜不可降標準）

- Idempotency Guard 必備
- Circuit Breaker 必備
- Kill Switch 必備
- Pre/In/Post Audit 必備
- Post Reconcile 必備
- Replay Bundle 必備

---

## 18. Mermaid｜執行控制總流程圖（Execution Control Map）

```mermaid
flowchart TB
  B -->|FAIL| X[BLOCK & AUDIT]
  B -->|PASS| C[Compile Intent -> Order Plan]
  C --> D{Idempotency Guard}
  D -->|DUPLICATE| X
  D -->|OK| E[Submit to Broker Adapter]
  E --> F[Receive ACK]
  F --> G[Order State Machine]
  G --> H{Circuit Breaker?}
  H -->|YES| CB[STOP NEW ORDERS + AUDIT]
  H -->|NO| I[Monitor Fills/Status]
  I --> J{Kill Switch Triggered?}
  J -->|YES| KS[HARD BLOCK + SAFE MODE + AUDIT]
  J -->|NO| K[Post-Execution Reconciliation]
  K --> L{Reconcile OK?}
  L -->|NO| R[STOP NEW ORDERS + REPAIR FLOW + AUDIT]
  L -->|YES| END[Complete + Replay Bundle Ref]
Only-Add 演進規則（本文件專屬）
允許新增：

更多狀態機狀態（但不得改既有語義）

更多熔斷條件與事件碼

更多審計欄位與回放視角

更多券商適配器（Broker Adapter）

禁止：

刪除或弱化 Token 驗證

刪除或弱化 Kill Switch

刪除 Pre/In/Post 任一段審計

以效能理由省略對帳或省略去重

（EXECUTION_CONTROL｜最大完備版 v2025-12-19 完）

補充性質：Only-Add（僅新增，不刪減／不覆寫／不偷換既有語義）
適用文件：EXECUTION_CONTROL（本文件）
對位母法：MASTER_CANON（治理等級 S）
生效狀態：GOVERNANCE_STATE = Freeze v1.0

A.1 Canonical 邊界對位（不可混用｜最終聲明）

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

Canonical Boundary Declaration（最終聲明）：

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

且 UI 層必須先完成「可裁決」硬條件檢查（Risk / Governance / Regime / Evidence / 版本資訊完整），否則不得進入 APPROVE。
TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

risk_pass_token：Risk/Compliance 放行令牌（PASS Token）

TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

intent_summary：即將執行之意圖摘要（標的/方向/數量/價格/有效時間）。
TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

risk_disclosure_snapshot：本次執行之風險揭露快照（主要風險項目 + 規則快照版本）。
TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

version_ref：本次運行所引用之治理文件版本參照（缺 version_ref 直接阻斷）。
TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

correlation_id / session_id：端到端追溯識別（用於全紀錄與回放）

mode：Research / Backtest / Simulation / Paper / Live（僅作為執行開關與記錄分流，不得改寫語義）

為避免將「執行層」誤用為敘事或決策層，本文件所有輸出與工件（Artifacts）必須符合：

僅輸出機器可驗證工件（例如：order_plan、order_id_map、ack、fill、state_transition、reconcile_report、audit_logs、kill_switch_events）。

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

不得反向回寫策略／Regime／流程裁決（本文件既有禁止事項已明示：Execution 反向回寫策略/Regime 屬違反邊界）。
TAITS_交易執行與控制規範（EXECUTION_CONTR…

A.4 全紀錄對位（Global Traceability Principle → Execution Artifacts）
MASTER_CANON 定義全紀錄原則：L1–L11 所產生之原始資料快照、Evidence、L9a 報告、L10 裁決紀錄、L11 執行與稽核工件，皆必須完整保存、可追溯、可回放、可稽核；無紀錄者制度上視為未發生。
TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

因此，EXECUTION_CONTROL 的審計與回放要求，在 Freeze v1.0 下補強為：

本文件既有「Pre / In / Post Execution Logs」要求，於此附錄對位為：

documents_active_map（本次運行所用 ACTIVE 文件版本映射）

evidence_bundle（引用之 Evidence 快照集合）

regime_state（Regime 判定狀態快照）

risk_decision（Risk/Compliance 判定與 PASS/VETO 快照）

execution_logs（Pre/In/Post + broker ack/fill + reconcile）

all_hashes（輸入/輸出/工件 hash 鏈）

以上最小集合之缺失，視同「不可回放」；依全紀錄原則，制度上視為未發生，不具任何執行效力。
TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

A.5 UI_SPEC × EXECUTION_CONTROL 的責任切割（避免重複與錯位）
本附錄將 UI 與執行控制之責任切割，固化為：

裁決狀態機（DRAFT/READY/BLOCKED/APPROVED/REJECTED/ABORTED）。
TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

APPROVE 前的硬條件檢查與兩段式確認。
TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

接收並驗證 risk_pass_token + decision_signature + version_ref 等最小接面

形成可執行 order plan、執行去重、下單、監控、熔斷、Kill Switch

產出 Pre/In/Post 審計物與 Replay Bundle

原則：UI 不得替代執行層檢核；執行層不得替代人類裁決。

A.6 與本文件既有條文的對位索引（不改正文，僅建立對照）
為避免「看起來重複」或「被誤解為新增制度」，本附錄僅建立對照索引：

本文件「核心鐵律：Human-in-the-Loop + Risk PASS Token Required + Kill Switch Always Available」
TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

本文件「禁止事項（Forbidden｜一票否決）」
→ 對位 MASTER_CANON：Canonical Boundary Declaration + 全紀錄原則（無紀錄＝未發生）。
TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

→ 對位 UI_SPEC：APPROVE 按鈕硬條件與兩段式確認。
TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

（附錄 A｜Only-Add：MASTER_CANON 對位補強 v2025-12-27 · Freeze v1.0 生效）
---

## Appendix 2025-12-28｜Only-Add：Trace ID / Evidence Chain 最小欄位貫穿（EXECUTION_CONTROL）對齊 DEPLOY_OPS（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md（doc_key：EXECUTION_CONTROL）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：RISK_COMPLIANCE（A）＋EXECUTION_CONTROL（A）＋DOCUMENT_INDEX（A+）＋AI_GOV（A+）  
> 平行對齊：DEPLOY_OPS｜Addendum 2025-12-27（D2/D3：Evidence Chain 最小欄位與結構）  
> 目的：將 Trace ID / Evidence Chain 的「最小可回放欄位」貫穿到本文件所管轄的產物/紀錄/裁決輸出；不改既有流程，只固定最低輸出格式。

### EC1. 最小引用標頭（Minimum Legal Citation Header）
本文件所生成或要求的任何「決策/裁決/執行/呈現」紀錄，至少必須包含下列引用標頭（欄位可多不可少）：

```text
trace_id = <全域唯一>
session_id = <本次對話/流程>
event_id = <本次事件/操作>
actor = <human/agent/module>
timestamp = <ISO-8601>
doc_key = EXECUTION_CONTROL
doc_title = TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:<對應條目（若有）>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
```

### EC2. Evidence Chain 最小結構（對齊 DEPLOY_OPS D3）
當本文件涉及「可回放產物」或「稽核必需證據」時，Evidence Chain 至少包含：

- `env_fingerprint`（環境指紋）  
- `dependency_manifest`（依賴清單）  
- `run_evidence`（執行證據：命令/時間/產物/日誌）  
- `failure_recovery`（失敗與回復：PASS/FAIL 與處置）

> 欄位定義與格式以 DEPLOY_OPS｜D3 為準；本附錄不重複改寫其語義，僅宣告「必帶」。

### EC3. Gate 行為（缺欄位之保守處置）
- 若缺少 EC1/EC2 最小欄位：不得視為「可回放/可稽核」輸出。  
- 涉及風險/合規裁決時：依 RISK_COMPLIANCE 與 GOVERNANCE_GATE_SPEC 之保守處置機制，採 **STOP/RETURN** 以補齊引用資訊（不得以推測補值）。
---

## Appendix 2025-12-28｜Only-Add：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md（doc_key：EXECUTION_CONTROL）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 Addendum/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`EXECUTION_CONTROL`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=EXECUTION_CONTROL` + `canonical_filename=TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

# Addendum 2025-12-28｜Only-Add：GLOBAL_ALIGNMENT_PATCH（MASTER_CANON 對齊全域補丁）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md（doc_key：EXECUTION_CONTROL）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0005`）  
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

- 本文件 `doc_key` 既有標示為 `EXECUTION_CONTROL`；本 Addendum 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

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

```

