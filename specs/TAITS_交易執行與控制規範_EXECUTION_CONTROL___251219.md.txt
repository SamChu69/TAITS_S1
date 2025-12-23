<<<<<<< HEAD
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

## 1. 執行層最高鐵律（Hard Gates｜一票否決）

### 1.1 策略永不直連下單（Strategy ≠ Order）
- 任何策略/Agent/分析模組不得直接呼叫券商下單介面。
- 任何「暗通道」或「快捷腳本」視為嚴重違規（Critical）。

### 1.2 風控放行憑證必須存在（Risk PASS Token Required）
- 未取得 `risk_pass_token`（且驗證成功）：
  - **不得建立 Execution Intent**
  - **不得送出任何委託**
- Token 驗證失敗：等同 VETO（SYS-VERIFY / SYS-VERSION），並觸發保護動作。

### 1.3 人類裁決不可被取代（Human-in-the-Loop）
- L10 的 `APPROVE` 是進入執行層的唯一入口。
- 禁止：
  - 背景自動批准
  - 預設批准
  - 以提示/推薦誘導替代裁決

### 1.4 Kill Switch 必須「永遠可用」
- 任何模式（Paper/Live 特別重要）：
  - Kill Switch 必須可立即生效
  - Kill Switch 觸發後必須阻斷新單、並進入保護狀態
- 若 Kill Switch 不可用：直接觸發 **EXE-KILL-01** 類否決（不得執行）。

### 1.5 「無審計 = 未執行」
- 任何委託行為（含撤單/改單/補單）若缺 Pre/In/Post 任一類審計物：
  - 視為非法執行（Critical），必須停機並保全證據。

---

## 2. 官方制度入口（執行層合規依據之官方來源）

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

## 3. 執行層在 Canonical Flow 的定位（L11）

### 3.1 進入條件（Entry Conditions｜必須全部成立）
- `governance_gate = PASS`（L9）
- `human_decision = APPROVE`（L10）
- `risk_gate_decision = PASS`（L7）且 `risk_pass_token` 驗證成功
- `version_ref` 完整（文件/政策/模型/規則快照可回放）
- `execution_channel_health = OK`（通道健康檢查通過）
- `kill_switch_status = READY`（急停就緒且可驗證）

任何一項不成立：不得執行。

### 3.2 輸出（Outputs）
- `order_requests`（委託請求集合，含 idempotency key）
- `broker_ack`（券商回報）
- `fills`（成交回報）
- `execution_audit_artifacts`（Pre/In/Post 完整審計物）
- `post_trade_state_update`（事後狀態快照，僅供記錄，不得回寫策略）

---

## 4. 執行控制模組（Execution Control Modules｜最大完備）

> FULL_ARCH 定義模組地圖；本節定義執行層必須具備的「控制面」模組與邊界。

### 4.1 Execution Orchestrator（執行編排器）
- 職責：將 Execution Intent 轉換為可執行序列（提交、確認、監控、終止）
- 禁止：自行生成交易方向；自行改寫人類意圖

### 4.2 Intent Compiler（意圖編譯器）
- 職責：把人類批准的「執行意圖」編譯成標準化委託模板（不含策略推論）
- 產出：Order Plan（分批/分段僅能依政策與意圖允許）

### 4.3 Broker Adapter（券商介面/適配器）
- 職責：與券商 API 交互（下單/撤單/查詢），並做必要的格式轉換
- 禁止：藏規則、黑箱改單、默默重送不留痕

### 4.4 Channel Health Monitor（通道健康監測）
- 職責：延遲、斷線、回報一致性、重送風險偵測
- 觸發：不健康立即升級風控或觸發急停（按政策）

### 4.5 Idempotency & De-dup Guard（去重與冪等保護）
- 職責：避免重複下單、重複撤單、狀態錯亂下的重送
- 核心：`idempotency_key` + `order_intent_hash`

### 4.6 Kill Switch Controller（急停控制器）
- 職責：一鍵中止、阻斷新單、進入安全模式
- 要求：必須有「硬阻斷」能力（不依賴 UI 顯示成功）

### 4.7 Circuit Breaker（熔斷器）
- 職責：在異常速率、異常損失、異常回報延遲時停止執行
- 觸發：依政策門檻（由 RISK Policy 管）

### 4.8 Execution Auditor（執行審計器）
- 職責：生成 Pre / In / Post Execution Logs 與回放資料包引用
- 禁止：事後補寫、覆寫、刪除

---

## 5. 執行意圖（Execution Intent）規範

### 5.1 Execution Intent 的定義
Execution Intent 是「人類批准後、仍需風控 token 放行才可被執行的結構化意圖」，其本質：
- 不等於策略
- 不等於券商委託
- 是「可審計、可回放」的執行前狀態

### 5.2 Intent 最小欄位（不可縮減）
- `intent_id`
- `correlation_id`
- `created_at`
- `user_id`（批准者）
- `instrument`（標的）
- `side`（買/賣；此為意圖方向，來源必須是人類裁決，不得由 AI 推論）
- `order_type`（市價/限價等；依制度與政策允許）
- `quantity`（數量）
- `price`（若限價）
- `time_in_force`（有效時間）
- `risk_pass_token_ref`（必填）
- `policy_version_ref`（必填）
- `evidence_snapshot_ref`（必填）
- `regime_state_ref`（必填）
- `ui_trace_ref`（必填）
- `intent_hash`（完整性）
- `idempotency_key`（冪等）

### 5.3 Intent 不可包含內容（禁止）
- 任何策略內部參數推導
- 任何 AI 自動建議的「默認批准」
- 任何未在 UI 明示的人類決策內容

---

## 6. 風控 PASS Token 驗證（Execution 前硬門檻）

### 6.1 驗證清單（全部通過才可執行）
- token 存在且未過期
- token `correlation_id` 與 intent 一致
- token `policy_version` 存在且可回放
- token `input_hash_ref` 與 evidence/regime/account 快照一致
- token `signature/hash` 驗證成功

### 6.2 驗證失敗處理
- 立即阻斷下單
- 記錄 `EXE-BLOCK` 類事件
- 通知 UI 顯示：阻斷原因碼（對照 RISK_COMPLIANCE / SYS 類）
- 若疑似狀態污染：觸發 Kill Switch（依政策）

---

## 7. 通道健康（Channel Health）與券商回報一致性

### 7.1 健康指標（最小集合）
- API 延遲（request/ack latency）
- 斷線/重連頻率
- 回報序列完整性（ack → fill → status）
- 委託查詢一致性（broker state vs local state）
- 重送風險指標（duplicate ack/fill）

### 7.2 不健康處置（最低要求）
- 降級：停止送新單、僅允許查詢/撤單（依政策）
- 升級：觸發 Circuit Breaker
- 極端：觸發 Kill Switch

---

## 8. 冪等與去重（Idempotency / De-dup）規範

### 8.1 核心原則
- 同一 `idempotency_key` 的委託請求：
  - 只允許「最多一次」被送達券商
- 系統重啟、斷線重連後：
  - 必須先「對帳」再恢復送單

### 8.2 去重流程（高階）
1) 生成 `order_intent_hash`
2) 建立 `idempotency_key = hash(intent_id + broker + session_id + nonce)`
3) 送出前查詢本地執行帳本（Execution Ledger）
4) 若已存在且狀態未終結：禁止重送（除非走明確的「恢復流程」並留痕）

---

## 9. 下單前檢查（Pre-Execution Checks｜最大完備）

> 注意：合規與風控條文由 RISK_COMPLIANCE 管；本節定義執行層「必做檢查項目」。

### 9.1 Pre-Execution 必做檢查清單
- 交易時段合法（依制度快照）
- 標的可交易（停牌/處置/分盤狀態）
- 送單參數合法（價格、數量、委託類型）
- 通道健康 OK
- Kill Switch READY
- Idempotency 檢查通過
- Risk PASS Token 驗證通過
- 審計器就緒（可寫入不可變儲存）

任何一項失敗：不得送單。

---

## 10. 執行中控制（In-Execution Controls）

### 10.1 In-Execution 必備監控
- 委託狀態機（Order State Machine）
- 成交回報一致性
- 滑價與成本偏離監控（若政策要求）
- 取消率/送單速率監控（Circuit Breaker）
- 通道延遲監控（延遲升高時停止送單）

### 10.2 Order State Machine（最小狀態）
- `CREATED`
- `VALIDATED`
- `SUBMITTED`
- `ACKED`
- `PARTIALLY_FILLED`
- `FILLED`
- `CANCEL_REQUESTED`
- `CANCEL_ACKED`
- `REJECTED`
- `EXPIRED`
- `ERROR`

狀態轉移必須可審計；不得跳轉或事後修正。

---

## 11. 執行後控制（Post-Execution Controls）

### 11.1 Post-Execution 必備輸出
- 成交彙總（fills summary）
- 委託/成交對帳結果（reconciliation）
- 事後狀態快照（post_trade_snapshot）
- 風險曝險更新（僅作記錄與供風控下一輪使用；不得回寫策略結論）
- 審計包引用（replay refs）

### 11.2 對帳（Reconciliation）最低要求
- 本地 order ledger 與券商查詢結果一致
- 若不一致：
  - 立即停止送新單
  - 進入「對帳修復流程」
  - 必須留痕與通知 UI（不可靜默）

---

## 12. Kill Switch（急停）規範（最高優先）

### 12.1 Kill Switch 類型
- **Manual Kill**：人類在 UI 一鍵觸發
- **System Kill**：系統檢測到嚴重異常自動觸發（依政策）
- **Compliance Kill**：合規事件觸發（例如制度禁止狀態）

### 12.2 Kill Switch 觸發後的硬性行為
- 立即阻斷新單（Hard Block）
- 將系統切換到安全模式（Safe Mode）：
  - 僅允許查詢、撤單（視政策）
- 記錄：
  - 觸發來源（manual/system/compliance）
  - 時間戳
  - 當下未完成委託清單
  - 通道狀態

### 12.3 Kill Switch 可用性自檢（Preflight）
- 每次進入 Live/Paper 前必做：
  - 觸發測試（dry-run）
  - 回報確認
  - 審計留痕
- 自檢失敗：EXE-KILL-01 → 不得啟動執行

---

## 13. Circuit Breaker（熔斷）規範

### 13.1 熔斷觸發類型（示例）
- 送單速率超標（EXE-RATE）
- 取消率異常（疑似追價/錯單風險）
- 通道延遲劇增（EXE-CHANNEL）
- 連續拒單（可能參數或制度錯誤）
- 對帳不一致

### 13.2 熔斷後處置
- 暫停送新單
- 通知 UI 顯示原因碼與建議處置（建議不等於放行）
- 產生事件審計物（CircuitBreakerEvent）

---

## 14. 執行審計（Pre / In / Post Execution Logs）

> 本節是硬性要求：必須能輸出「三段式」審計，並可回放。

### 14.1 Pre-Execution Log（送單前）
- intent_id / correlation_id
- risk_pass_token_ref（驗證結果）
- channel_health_snapshot
- kill_switch_status
- validation_result（PASS/FAIL）與 reason_codes
- input_hash / output_hash（Intent → Order Plan）

### 14.2 In-Execution Log（執行中）
- order_requests（含 idempotency_key）
- broker_ack（原始回報）
- order_state_transitions（狀態機）
- latency metrics
- circuit breaker events（若有）

### 14.3 Post-Execution Log（執行後）
- fills（成交明細引用）
- reconciliation report
- post_trade_snapshot_ref
- exceptions / errors（若有）
- replay_bundle_ref（回放包引用）

---

## 15. UI 呈現義務（Execution 專屬）

> UI 詳規由 UI_SPEC 管；本節定義執行層必交付 UI 的必要資訊。

UI 必須可呈現：
- intent 狀態（validated/submitted/filled…）
- token 驗證結果（PASS/FAIL 與 reason codes）
- 通道健康狀態（OK/DEGRADED/DOWN）
- Kill Switch 狀態（READY/ARMED/TRIGGERED）
- 熔斷事件（若有）
- 對帳結果（一致/不一致）

禁止：
- 以「看起來成功」取代券商 ack/fill
- 隱藏拒單原因
- 靜默重送

---

## 16. 模式差異（Research / Backtest / Simulation / Paper / Live）— 不得降級

### 16.1 不變項（所有模式相同）
- 仍需 Risk Gate（在 Backtest/Sim 以語義方式生效）
- 仍需審計與回放
- 仍需去重/狀態機語義

### 16.2 可變項（僅三處）
- 資料來源（歷史/即時）
- 時間推進（模擬/真實）
- 券商通道（真實/模擬）

---

## 17. 禁止事項（Forbidden｜一票否決）

- 無 Risk PASS Token 送單
- 無 Human APPROVE 送單
- Kill Switch 不可用仍執行
- 缺 Pre/In/Post 任一審計物仍執行
- 靜默重送/靜默改單/黑箱補單
- 對帳不一致仍繼續送新單
- Execution 反向回寫策略/Regime（違反邊界）

---

## 18. Mermaid｜執行控制總流程圖（Execution Control Map）

```mermaid
flowchart TB
  A[Entry Check<br/>L10 APPROVE + Risk PASS Token] --> B{Pre-Execution Checks}
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

19. Only-Add 演進規則（本文件專屬）
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
=======
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

## 1. 執行層最高鐵律（Hard Gates｜一票否決）

### 1.1 策略永不直連下單（Strategy ≠ Order）
- 任何策略/Agent/分析模組不得直接呼叫券商下單介面。
- 任何「暗通道」或「快捷腳本」視為嚴重違規（Critical）。

### 1.2 風控放行憑證必須存在（Risk PASS Token Required）
- 未取得 `risk_pass_token`（且驗證成功）：
  - **不得建立 Execution Intent**
  - **不得送出任何委託**
- Token 驗證失敗：等同 VETO（SYS-VERIFY / SYS-VERSION），並觸發保護動作。

### 1.3 人類裁決不可被取代（Human-in-the-Loop）
- L10 的 `APPROVE` 是進入執行層的唯一入口。
- 禁止：
  - 背景自動批准
  - 預設批准
  - 以提示/推薦誘導替代裁決

### 1.4 Kill Switch 必須「永遠可用」
- 任何模式（Paper/Live 特別重要）：
  - Kill Switch 必須可立即生效
  - Kill Switch 觸發後必須阻斷新單、並進入保護狀態
- 若 Kill Switch 不可用：直接觸發 **EXE-KILL-01** 類否決（不得執行）。

### 1.5 「無審計 = 未執行」
- 任何委託行為（含撤單/改單/補單）若缺 Pre/In/Post 任一類審計物：
  - 視為非法執行（Critical），必須停機並保全證據。

---

## 2. 官方制度入口（執行層合規依據之官方來源）

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

## 3. 執行層在 Canonical Flow 的定位（L11）

### 3.1 進入條件（Entry Conditions｜必須全部成立）
- `governance_gate = PASS`（L9）
- `human_decision = APPROVE`（L10）
- `risk_gate_decision = PASS`（L7）且 `risk_pass_token` 驗證成功
- `version_ref` 完整（文件/政策/模型/規則快照可回放）
- `execution_channel_health = OK`（通道健康檢查通過）
- `kill_switch_status = READY`（急停就緒且可驗證）

任何一項不成立：不得執行。

### 3.2 輸出（Outputs）
- `order_requests`（委託請求集合，含 idempotency key）
- `broker_ack`（券商回報）
- `fills`（成交回報）
- `execution_audit_artifacts`（Pre/In/Post 完整審計物）
- `post_trade_state_update`（事後狀態快照，僅供記錄，不得回寫策略）

---

## 4. 執行控制模組（Execution Control Modules｜最大完備）

> FULL_ARCH 定義模組地圖；本節定義執行層必須具備的「控制面」模組與邊界。

### 4.1 Execution Orchestrator（執行編排器）
- 職責：將 Execution Intent 轉換為可執行序列（提交、確認、監控、終止）
- 禁止：自行生成交易方向；自行改寫人類意圖

### 4.2 Intent Compiler（意圖編譯器）
- 職責：把人類批准的「執行意圖」編譯成標準化委託模板（不含策略推論）
- 產出：Order Plan（分批/分段僅能依政策與意圖允許）

### 4.3 Broker Adapter（券商介面/適配器）
- 職責：與券商 API 交互（下單/撤單/查詢），並做必要的格式轉換
- 禁止：藏規則、黑箱改單、默默重送不留痕

### 4.4 Channel Health Monitor（通道健康監測）
- 職責：延遲、斷線、回報一致性、重送風險偵測
- 觸發：不健康立即升級風控或觸發急停（按政策）

### 4.5 Idempotency & De-dup Guard（去重與冪等保護）
- 職責：避免重複下單、重複撤單、狀態錯亂下的重送
- 核心：`idempotency_key` + `order_intent_hash`

### 4.6 Kill Switch Controller（急停控制器）
- 職責：一鍵中止、阻斷新單、進入安全模式
- 要求：必須有「硬阻斷」能力（不依賴 UI 顯示成功）

### 4.7 Circuit Breaker（熔斷器）
- 職責：在異常速率、異常損失、異常回報延遲時停止執行
- 觸發：依政策門檻（由 RISK Policy 管）

### 4.8 Execution Auditor（執行審計器）
- 職責：生成 Pre / In / Post Execution Logs 與回放資料包引用
- 禁止：事後補寫、覆寫、刪除

---

## 5. 執行意圖（Execution Intent）規範

### 5.1 Execution Intent 的定義
Execution Intent 是「人類批准後、仍需風控 token 放行才可被執行的結構化意圖」，其本質：
- 不等於策略
- 不等於券商委託
- 是「可審計、可回放」的執行前狀態

### 5.2 Intent 最小欄位（不可縮減）
- `intent_id`
- `correlation_id`
- `created_at`
- `user_id`（批准者）
- `instrument`（標的）
- `side`（買/賣；此為意圖方向，來源必須是人類裁決，不得由 AI 推論）
- `order_type`（市價/限價等；依制度與政策允許）
- `quantity`（數量）
- `price`（若限價）
- `time_in_force`（有效時間）
- `risk_pass_token_ref`（必填）
- `policy_version_ref`（必填）
- `evidence_snapshot_ref`（必填）
- `regime_state_ref`（必填）
- `ui_trace_ref`（必填）
- `intent_hash`（完整性）
- `idempotency_key`（冪等）

### 5.3 Intent 不可包含內容（禁止）
- 任何策略內部參數推導
- 任何 AI 自動建議的「默認批准」
- 任何未在 UI 明示的人類決策內容

---

## 6. 風控 PASS Token 驗證（Execution 前硬門檻）

### 6.1 驗證清單（全部通過才可執行）
- token 存在且未過期
- token `correlation_id` 與 intent 一致
- token `policy_version` 存在且可回放
- token `input_hash_ref` 與 evidence/regime/account 快照一致
- token `signature/hash` 驗證成功

### 6.2 驗證失敗處理
- 立即阻斷下單
- 記錄 `EXE-BLOCK` 類事件
- 通知 UI 顯示：阻斷原因碼（對照 RISK_COMPLIANCE / SYS 類）
- 若疑似狀態污染：觸發 Kill Switch（依政策）

---

## 7. 通道健康（Channel Health）與券商回報一致性

### 7.1 健康指標（最小集合）
- API 延遲（request/ack latency）
- 斷線/重連頻率
- 回報序列完整性（ack → fill → status）
- 委託查詢一致性（broker state vs local state）
- 重送風險指標（duplicate ack/fill）

### 7.2 不健康處置（最低要求）
- 降級：停止送新單、僅允許查詢/撤單（依政策）
- 升級：觸發 Circuit Breaker
- 極端：觸發 Kill Switch

---

## 8. 冪等與去重（Idempotency / De-dup）規範

### 8.1 核心原則
- 同一 `idempotency_key` 的委託請求：
  - 只允許「最多一次」被送達券商
- 系統重啟、斷線重連後：
  - 必須先「對帳」再恢復送單

### 8.2 去重流程（高階）
1) 生成 `order_intent_hash`
2) 建立 `idempotency_key = hash(intent_id + broker + session_id + nonce)`
3) 送出前查詢本地執行帳本（Execution Ledger）
4) 若已存在且狀態未終結：禁止重送（除非走明確的「恢復流程」並留痕）

---

## 9. 下單前檢查（Pre-Execution Checks｜最大完備）

> 注意：合規與風控條文由 RISK_COMPLIANCE 管；本節定義執行層「必做檢查項目」。

### 9.1 Pre-Execution 必做檢查清單
- 交易時段合法（依制度快照）
- 標的可交易（停牌/處置/分盤狀態）
- 送單參數合法（價格、數量、委託類型）
- 通道健康 OK
- Kill Switch READY
- Idempotency 檢查通過
- Risk PASS Token 驗證通過
- 審計器就緒（可寫入不可變儲存）

任何一項失敗：不得送單。

---

## 10. 執行中控制（In-Execution Controls）

### 10.1 In-Execution 必備監控
- 委託狀態機（Order State Machine）
- 成交回報一致性
- 滑價與成本偏離監控（若政策要求）
- 取消率/送單速率監控（Circuit Breaker）
- 通道延遲監控（延遲升高時停止送單）

### 10.2 Order State Machine（最小狀態）
- `CREATED`
- `VALIDATED`
- `SUBMITTED`
- `ACKED`
- `PARTIALLY_FILLED`
- `FILLED`
- `CANCEL_REQUESTED`
- `CANCEL_ACKED`
- `REJECTED`
- `EXPIRED`
- `ERROR`

狀態轉移必須可審計；不得跳轉或事後修正。

---

## 11. 執行後控制（Post-Execution Controls）

### 11.1 Post-Execution 必備輸出
- 成交彙總（fills summary）
- 委託/成交對帳結果（reconciliation）
- 事後狀態快照（post_trade_snapshot）
- 風險曝險更新（僅作記錄與供風控下一輪使用；不得回寫策略結論）
- 審計包引用（replay refs）

### 11.2 對帳（Reconciliation）最低要求
- 本地 order ledger 與券商查詢結果一致
- 若不一致：
  - 立即停止送新單
  - 進入「對帳修復流程」
  - 必須留痕與通知 UI（不可靜默）

---

## 12. Kill Switch（急停）規範（最高優先）

### 12.1 Kill Switch 類型
- **Manual Kill**：人類在 UI 一鍵觸發
- **System Kill**：系統檢測到嚴重異常自動觸發（依政策）
- **Compliance Kill**：合規事件觸發（例如制度禁止狀態）

### 12.2 Kill Switch 觸發後的硬性行為
- 立即阻斷新單（Hard Block）
- 將系統切換到安全模式（Safe Mode）：
  - 僅允許查詢、撤單（視政策）
- 記錄：
  - 觸發來源（manual/system/compliance）
  - 時間戳
  - 當下未完成委託清單
  - 通道狀態

### 12.3 Kill Switch 可用性自檢（Preflight）
- 每次進入 Live/Paper 前必做：
  - 觸發測試（dry-run）
  - 回報確認
  - 審計留痕
- 自檢失敗：EXE-KILL-01 → 不得啟動執行

---

## 13. Circuit Breaker（熔斷）規範

### 13.1 熔斷觸發類型（示例）
- 送單速率超標（EXE-RATE）
- 取消率異常（疑似追價/錯單風險）
- 通道延遲劇增（EXE-CHANNEL）
- 連續拒單（可能參數或制度錯誤）
- 對帳不一致

### 13.2 熔斷後處置
- 暫停送新單
- 通知 UI 顯示原因碼與建議處置（建議不等於放行）
- 產生事件審計物（CircuitBreakerEvent）

---

## 14. 執行審計（Pre / In / Post Execution Logs）

> 本節是硬性要求：必須能輸出「三段式」審計，並可回放。

### 14.1 Pre-Execution Log（送單前）
- intent_id / correlation_id
- risk_pass_token_ref（驗證結果）
- channel_health_snapshot
- kill_switch_status
- validation_result（PASS/FAIL）與 reason_codes
- input_hash / output_hash（Intent → Order Plan）

### 14.2 In-Execution Log（執行中）
- order_requests（含 idempotency_key）
- broker_ack（原始回報）
- order_state_transitions（狀態機）
- latency metrics
- circuit breaker events（若有）

### 14.3 Post-Execution Log（執行後）
- fills（成交明細引用）
- reconciliation report
- post_trade_snapshot_ref
- exceptions / errors（若有）
- replay_bundle_ref（回放包引用）

---

## 15. UI 呈現義務（Execution 專屬）

> UI 詳規由 UI_SPEC 管；本節定義執行層必交付 UI 的必要資訊。

UI 必須可呈現：
- intent 狀態（validated/submitted/filled…）
- token 驗證結果（PASS/FAIL 與 reason codes）
- 通道健康狀態（OK/DEGRADED/DOWN）
- Kill Switch 狀態（READY/ARMED/TRIGGERED）
- 熔斷事件（若有）
- 對帳結果（一致/不一致）

禁止：
- 以「看起來成功」取代券商 ack/fill
- 隱藏拒單原因
- 靜默重送

---

## 16. 模式差異（Research / Backtest / Simulation / Paper / Live）— 不得降級

### 16.1 不變項（所有模式相同）
- 仍需 Risk Gate（在 Backtest/Sim 以語義方式生效）
- 仍需審計與回放
- 仍需去重/狀態機語義

### 16.2 可變項（僅三處）
- 資料來源（歷史/即時）
- 時間推進（模擬/真實）
- 券商通道（真實/模擬）

---

## 17. 禁止事項（Forbidden｜一票否決）

- 無 Risk PASS Token 送單
- 無 Human APPROVE 送單
- Kill Switch 不可用仍執行
- 缺 Pre/In/Post 任一審計物仍執行
- 靜默重送/靜默改單/黑箱補單
- 對帳不一致仍繼續送新單
- Execution 反向回寫策略/Regime（違反邊界）

---

## 18. Mermaid｜執行控制總流程圖（Execution Control Map）

```mermaid
flowchart TB
  A[Entry Check<br/>L10 APPROVE + Risk PASS Token] --> B{Pre-Execution Checks}
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

19. Only-Add 演進規則（本文件專屬）
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
>>>>>>> b86b67594931d531a6ecfabca56380f4bf2b48ef
