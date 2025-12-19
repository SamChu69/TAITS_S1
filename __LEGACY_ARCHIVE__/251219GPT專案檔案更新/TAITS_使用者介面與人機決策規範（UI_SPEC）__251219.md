# TAITS_使用者介面與人機決策規範（UI_SPEC）__251219
doc_key：UI_SPEC  
治理等級：A（Human-in-the-Loop Interface Charter｜人類主權唯一入口）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（介面與人機決策最高規範，Only-Add 演進）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：FULL_ARCH / ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / VERSION_AUDIT / DEPLOY_OPS / LOCAL_ENV  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化人類主權/否決可視化/審計義務）  
核心鐵律：UI 是人與系統唯一交界面；風險揭露優先於績效；否決不可被模糊化

---

## 0. 文件定位（UI & Human Decision Charter）

本文件是 TAITS 的「使用者介面與人機決策」最高規範，目的在於：

- 定義 **TAITS UI 的治理地位**：人類主權唯一入口（Human-in-the-Loop）
- 定義 **UI 必須呈現的事實**：Evidence / Regime / Risk / Governance / Execution Trace
- 定義 **UI 必須遵守的行為**：不得誘導、不得模糊、不得自動化越權
- 定義 **可追溯性**：UI 必須生成 Decision Trace 與審計證據（Artifacts）
- 定義 **安全控制**：Kill Switch、阻斷（Block）、回放（Replay）、版本對齊（Version Ref）

📌 本文件不負責（避免越權）：
- 不定義風控否決條文全集（→ RISK_COMPLIANCE）
- 不定義執行細節/券商適配（→ EXECUTION_CONTROL）
- 不改寫 Canonical Flow（→ MASTER_CANON / ARCH_FLOW）
- 不定義系統模組地圖（→ FULL_ARCH）

---

## 1. UI 的治理地位（Human Sovereignty）

### 1.1 UI 的唯一性（Single Entry Point）
- **任何「進入 L10 人類裁決」的動作，只能透過 UI 完成。**
- 禁止：
  - 背景自動批准
  - 預設批准（Default Approve）
  - 任何 API 或腳本繞過 UI 直接產生 `human_decision=APPROVE`

### 1.2 UI 的角色是「呈現事實」不是「替人決策」
UI 必須：
- 呈現 Evidence（證據）
- 呈現 Regime（市場狀態）
- 呈現 Risk/Compliance 的 PASS/VETO 與原因碼
- 呈現 Governance 的 PASS/RETURN 與缺口清單
- 呈現 Execution 的可執行意圖（Intent）與預期後果（風險揭露）

UI 不得：
- 以「AI 建議」包裝成「應該買/賣」
- 以績效、勝率、回測曲線誘導越過風險揭露
- 以模糊詞（例如「可考慮」「大致安全」）替代 PASS/VETO

### 1.3 風險揭露優先序（Risk Disclosure Priority）
UI 的排序必須遵守：
1) 風險與合規（RISK/COMPLIANCE）
2) Regime（可交易/不可交易）
3) 證據完整性（Evidence Completeness）
4) 策略建議（Strategy Proposal）
5) 績效呈現（Performance）— 僅能放在後面，且不得掩蓋風險

---

## 2. UI 與 Canonical Flow 的對位（L10）

### 2.1 UI 所在層級
- UI 是 **L10：Decision Interface（人類裁決）** 的實體化。

### 2.2 UI 的輸入（必須具備）
- `evidence_bundle_ref`（L5）
- `regime_state_ref`（L6）
- `risk_gate_decision` + `veto_reason_codes[]` + `policy_version`（L7）
- `strategy_proposal_ref`（L8）
- `governance_pass_or_return` + `missing_items[]`（L9）
- `version_ref_map`（doc/policy/model/rulebook snapshots）
- `correlation_id` / `session_id`

### 2.3 UI 的輸出（必須產生、必須可回放）
- `human_decision`：APPROVE / REJECT / ABORT（禁止空白）
- `human_decision_reason`（至少選擇式原因碼或備註，但不得取代風控原因碼）
- `ui_trace_ref`（完整交互軌跡）
- `decision_signature`（確認動作的不可否認性：至少包含 user_id + timestamp + hash）

---

## 3. UI 核心頁面與資訊架構（IA｜Information Architecture）

> 本節定義「必須存在的 UI 區塊」。  
> 具體視覺風格可自由，但不得刪減以下功能區塊。

### 3.1 全域固定區（Global Persistent）
- 全域狀態列（System Status Bar）
  - 模式：Research / Backtest / Simulation / Paper / Live
  - 通道健康：OK / DEGRADED / DOWN
  - Kill Switch：READY / ARMED / TRIGGERED
  - 版本：Active doc_key map（至少顯示 AI_GOV / RISK policy / EXEC version）
  - 時間：交易日/交易時段狀態（可交易/不可交易）
- 全域警示面板（Global Alerts）
  - VETO（紅）
  - RETURN（橘）
  - WARNING（黃；僅提示，不得取代否決）

### 3.2 核心工作台（Decision Workbench）
必須分為 6 大區塊（不可合併造成不可讀）：

1) Evidence Panel（證據面板）
2) Regime Panel（市場狀態）
3) Risk/Compliance Panel（最高否決）
4) Governance Panel（流程守門）
5) Strategy/Research Panel（建議與情境）
6) Execution Preview Panel（執行預覽：僅在可執行時顯示）

### 3.3 稽核與回放（Audit & Replay）
- Decision Trace Viewer（決策追溯）
- Replay Loader（回放載入器：以 correlation_id / replay_bundle_ref 載入）
- Change Ledger Viewer（版本變更帳本視圖：只讀）

---

## 4. 必須呈現的「事實」欄位（UI Must-Show Fields）

> 下列欄位為 UI 最小必備集合：可擴充，不可縮減。  
> UI 不得隱藏，不得以摘要遮蔽關鍵風險資訊。

### 4.1 共同必備（全頁面）
- `correlation_id`
- `session_id`
- `mode`
- `timestamp`
- `active_versions`（doc/policy/model/rulebook）
- `data_provenance_summary_ref`（資料來源摘要引用，點開可見細節）

### 4.2 Evidence Panel 必備
- Evidence Completeness（完整度：百分比/等級）
- Evidence List（證據清單：每項可展開）
  - 證據來源（官方/第三方/內部計算）
  - 時間戳
  - hash/ref
- Evidence Conflicts（衝突標記：不得隱藏）

### 4.3 Regime Panel 必備
- `regime_label`（明確標籤）
- `regime_confidence`
- `regime_allowed_actions`（允許/禁止哪些策略類型）
- `regime_change_log`（最近變化）

### 4.4 Risk/Compliance Panel 必備（最重要）
- `risk_gate_decision`：PASS / VETO（必須用硬字）
- `veto_reason_codes[]`（若 VETO 必顯示）
- `policy_version`
- `risk_pass_token_status`（PASS 時顯示可驗證狀態）
- 風險揭露摘要（曝險、滑價估計、流動性等）
- 合規狀態摘要（交易時段/標的可交易性/制度快照）

### 4.5 Governance Panel 必備
- `governance_status`：PASS / RETURN
- `missing_items[]`（若 RETURN 必顯示需補齊清單）
- `flow_integrity_checks`（跳層檢測結果）

### 4.6 Strategy/Research Panel 必備
- Strategy Proposal（建議清單：必須標註「非指令」）
- Scenario（情境）
- Assumptions（假設）
- Limitations（限制）
- Backtest/Sim Evidence refs（如有）

### 4.7 Execution Preview Panel 必備（僅在可執行狀態顯示）
- Execution Intent（可執行意圖預覽）
  - 標的、方向、數量、價格、委託類型、有效時間
- Preconditions Checklist（進入 L11 的前置條件）
  - Risk Token 驗證：PASS/FAIL
  - Channel Health：OK/DEGRADED/DOWN
  - Kill Switch：READY/ARMED/TRIGGERED
  - Reconciliation status（若先前不一致則必顯示阻斷）
- Estimated Cost & Risk Disclosure（成本/風險揭露，不得用單一數字掩蓋區間）

---

## 5. UI 的硬性禁止事項（Forbidden Behaviors｜一票否決）

### 5.1 禁止「模糊化否決」
- 不得用「建議暫停」「不太建議」替代 VETO
- VETO 必須顯示 reason_code

### 5.2 禁止「暗示自動交易」
- 不得提供「一鍵全自動」或「無人值守」模式入口
- Live 模式必須顯示 Human-in-the-Loop 提示與責任聲明

### 5.3 禁止「AI 主體化」語句
- UI 文案不得出現「我決定」「我認為」「我幫你下單」
- 允許：「系統偵測」「證據顯示」「風控否決」

### 5.4 禁止「績效壓過風險」
- 任何績效圖表不得置頂壓過 Risk Panel
- 任何績效陳述必須伴隨風險提示（且不得弱化否決）

### 5.5 禁止「遮蔽版本與來源」
- 不得隱藏 active_versions
- 不得隱藏 data provenance（至少要能點開）

---

## 6. 人類裁決（Human Decision）流程規格

### 6.1 裁決狀態機（Decision State Machine）
- `DRAFT`：尚未裁決
- `READY`：可裁決（Gate PASS 且資訊完整）
- `BLOCKED`：不可裁決（VETO 或 RETURN 或缺資料）
- `APPROVED`：人類批准（進入 L11 前仍需執行層檢核）
- `REJECTED`：人類拒絕
- `ABORTED`：流程取消（例如使用者離開/超時）

### 6.2 何時可以按下 APPROVE（硬條件）
UI 必須強制檢查：
- Risk = PASS（否則按鈕 disabled）
- Governance = PASS（否則按鈕 disabled）
- Regime = 可交易（否則 disabled 或顯示阻斷）
- Evidence Completeness 達最低門檻（門檻由政策檔定義，但必須顯示）
- 版本資訊完整（缺 version_ref 直接阻斷）

### 6.3 APPROVE 的「雙重確認」（Two-step Confirmation）
為避免誤觸或誘導，APPROVE 必須兩段式：
1) 顯示「將要執行」的 Intent 摘要（標的/方向/數量/價格/有效時間）
2) 顯示風險揭露（主要風險項目 + 規則快照版本）
3) 使用者再次確認（確認後才產生 decision_signature）

---

## 7. UI 與風控否決的互動（Veto UX Rules）

### 7.1 VETO 的 UI 呈現（不可省略）
- 顯示 `VETO`（紅色狀態，文字不可替換）
- 顯示 `veto_reason_codes[]`（可展開含描述與對應證據 ref）
- 顯示「不可執行」並鎖定 APPROVE
- 提供「回放當下證據」入口（Replay）

### 7.2 RETURN（退回）呈現
- 顯示 `RETURN`（橘色）
- 顯示 `missing_items[]`（需補齊清單）
- 提供「跳轉到缺口所在面板」功能（例如缺 Evidence → 直接跳 Evidence Panel）

---

## 8. UI Decision Trace（決策追溯）規範

### 8.1 Decision Trace 的定義
Decision Trace 是「UI 交互行為 → 決策結果」的不可否認記錄，用於：
- 稽核
- 回放
- 追責
- 故障排查（非唯一用途）

### 8.2 Trace 最小欄位（不可縮減）
- `ui_trace_id`
- `correlation_id`
- `user_id`
- `mode`
- `opened_at`, `closed_at`
- `view_events[]`（使用者看過哪些面板、停留時間）
- `expand_events[]`（展開哪些證據/原因碼）
- `decision_action`（APPROVE/REJECT/ABORT）
- `decision_signature`（hash）
- `active_versions`（完整映射）
- `risk_gate_snapshot_ref`
- `evidence_bundle_ref`
- `regime_state_ref`
- `strategy_proposal_ref`
- `governance_report_ref`

### 8.3 Trace 存放與不可變更性
- Trace 必須寫入不可變更儲存（Immutable / Append-only）
- 禁止：
  - 覆寫
  - 刪除
  - 事後補填（Backfill）

---

## 9. UI 與 Execution 的握手（Handshake）規範

### 9.1 UI → Execution 的輸出物（必須）
UI 在 APPROVE 後必須生成：
- `execution_intent_draft`（草案，尚未送券商）
- `ui_trace_ref`
- `decision_signature`
- `risk_pass_token_ref`（引用）

Execution 層（EXECUTION_CONTROL）在送單前必須再次驗證：
- token 有效
- channel 健康
- kill switch READY
- idempotency key 未重複
- 審計器可寫入

若任一驗證失敗：
- UI 必須收到 `BLOCK` 回覆並顯示原因碼（不可靜默）

### 9.2 UI 對 Execution 狀態的可視化義務
UI 必須能即時顯示：
- intent 狀態機
- broker ACK/REJECT
- fills（成交）
- circuit breaker events
- kill switch events
- reconciliation 結果

---

## 10. Kill Switch（急停）UI 規範（最高優先）

### 10.1 Kill Switch UI 必備
- 全域固定按鈕（不可藏在子頁）
- 必須具備：
  - 觸發確認（避免誤觸）
  - 觸發後回饋（TRIGGERED + timestamp）
  - 觸發原因（manual/system/compliance）
  - 影響範圍（阻斷新單/是否撤單等，依政策顯示）

### 10.2 Kill Switch 觸發後 UI 行為
- 立即：
  - 鎖定 APPROVE
  - 停止所有「送新單」操作
- 顯示：
  - 未完成委託清單
  - 系統進入 Safe Mode 的狀態

---

## 11. 權限與角色（RBAC｜Role-Based Access Control）規範

> UI 必須支援最少 4 類角色，且權限不可混用。
> 角色可以擴充，但不得縮減或弱化隔離。

- `Viewer`：只讀（看 Evidence/Regime/Risk，不可裁決）
- `Operator`：可操作回放、查詢、但不可 APPROVE
- `Trader`：可在 PASS 狀態下 APPROVE（受所有 Gate 限制）
- `Admin`：管理系統設定（但仍不可覆寫風控否決；管理 ≠ 裁決）

必備規則：
- 所有裁決行為必須綁定 user_id 與角色
- 任何角色變更必須記錄（VERSION_AUDIT）

---

## 12. 國際化與語言規範（繁中優先）

- UI 主語言：繁體中文
- 專有名詞可保留英文，但必須提供中譯（至少首次出現）
  - Evidence（證據）
  - Regime（市場狀態）
  - Veto（否決）
  - Replay（回放）
  - Audit（稽核）
  - Intent（執行意圖）
- UI 不得以英文縮寫掩蓋關鍵風險資訊

---

## 13. UI 錯誤/異常處理（UI Error Handling）

UI 必須能區分並明示：
- `BLOCKED_BY_RISK`（被風控否決）
- `BLOCKED_BY_GOVERNANCE`（流程缺口）
- `DATA_INCOMPLETE`（證據不足）
- `CHANNEL_DEGRADED/DOWN`（通道不健康）
- `TOKEN_INVALID/EXPIRED`（token 不可用）
- `SYSTEM_INTEGRITY_FAIL`（版本/審計完整性失敗）

任何錯誤不可：
- 靜默吞掉
- 以「再試一次」掩蓋原因
- 以「看起來成功」假象替代真實狀態

---

## 14. Mermaid｜UI 決策與否決可視化流程圖（必須能放入 md）

### 14.1 UI Decision Flow（含否決/退回）

```mermaid
flowchart TB
  A[Load Decision Workbench] --> B[Show Evidence/Regime/Risk/Gov/Strategy]
  B --> C{Risk Gate?}
  C -->|VETO| V[UI: VETO Banner + Codes + Replay]
  C -->|PASS| D{Governance Gate?}
  D -->|RETURN| R[UI: RETURN + Missing Items + Jump Links]
  D -->|PASS| E{Regime Allowed?}
  E -->|NO| X[UI: BLOCKED by Regime]
  E -->|YES| F[Enable APPROVE (Two-step Confirm)]
  F --> G{Human Decision}
  G -->|REJECT| H[Record Trace + STOP]
  G -->|APPROVE| I[Send Intent Draft + Trace Ref]
  I --> J{Execution Preflight}
  J -->|BLOCK| K[UI: BLOCK + Reason Codes]
  J -->|OK| L[Show Execution Live Status]
14.2 Veto Visualization Map（否決可視化地圖）
mermaid
複製程式碼
flowchart LR
  VETO[VETO] --> C1[CMP 合規]
  VETO --> S1[SYS 系統完整性]
  VETO --> M1[MKT 市場]
  VETO --> L1[LIQ 流動性]
  VETO --> P1[PTF 組合曝險]
  VETO --> E1[EXE 執行安全]
  C1 --> CODE1[veto_reason_codes[]]
  S1 --> CODE1
  M1 --> CODE1
  L1 --> CODE1
  P1 --> CODE1
  E1 --> CODE1
15. Only-Add 演進規則（UI_SPEC 專屬）
允許新增：

新面板（例如：事件面板、宏觀面板）

新欄位（更多可視化、更多 trace）

新角色（RBAC 擴充）

新的回放視角（Replay Views）

禁止：

移除或弱化 Risk/Compliance Panel

移除 VETO reason_code 顯示

讓 APPROVE 在 VETO/RETURN 狀態可按

移除 correlation_id / version_ref / provenance 入口

任何形式的「自動批准」「無人值守」入口

16. UI_SPEC 終極裁決語句（不可更改）
UI 的使命不是讓交易變快，
而是讓每一次交易在發生前都可被理解、被否決、被追溯。

（UI_SPEC｜最大完備版 v2025-12-19 完）
