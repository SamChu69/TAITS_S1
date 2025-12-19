# TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219
doc_key：ARCH_FLOW  
治理等級：B+（Canonical Flow Specification｜承接 MASTER_CANON / FULL_ARCH）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（流程層細化，允許 Only-Add 擴充）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
變更原則：Only-Add（僅可新增，不可刪減／覆寫／改寫語義）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT  

---

## 0. 文件定位（Architecture Flow Specification）

本文件為 **TAITS Canonical Flow 的「最大完備流程細化說明」**，  
負責回答四個工程與治理層都必須清楚的問題：

1. **流程何時被觸發（Trigger）**
2. **流程在每一層做什麼、不做什麼**
3. **流程在哪些條件下必須中斷、退回或終止**
4. **流程如何在不同運行模式下（Research / Backtest / Simulation / Paper / Live）保持一致性**

📌 本文件嚴格遵守：
- **L1–L11 不可跳步**
- **任何中斷都必須可解釋、可回放**
- **流程 ≠ 策略**
- **流程 ≠ 下單權限**

---

## 1. Canonical Flow 的「不變核心」

### 1.1 五個不可破壞的流程公理

1. **單向性（Forward-only）**  
   流程只能前進或中斷，不存在「偷偷回寫修正」。

2. **層級隔離（Layer Isolation）**  
   每一層只處理該層責任，不得越權。

3. **證據先於判斷（Evidence First）**  
   沒有 Evidence，不得進入 Regime / Risk。

4. **否決優先於建議（Veto > Proposal）**  
   任一否決，流程立即停止或退回。

5. **人類裁決不可被模擬（Human不可被取代）**  
   L10 只能由人類完成。

---

## 2. L1–L11「輸入 / 輸出 / 狀態轉移」矩陣（最大完備）

> 本節補齊前文未展開的「狀態轉移語義」，  
> 用於工程實作、回測模擬與流程審計。

| Layer | 輸入狀態 | 成功輸出狀態 | 失敗狀態 | 失敗後去向 |
|---|---|---|---|---|
| L1 | NoData | RawDataReady | SourceFail | STOP |
| L2 | RawDataReady | CanonicalReady | QAFail | STOP |
| L3 | CanonicalReady | SnapshotReady | SnapshotFail | STOP |
| L4 | SnapshotReady | FeatureReady | AnalysisFail | STOP |
| L5 | FeatureReady | EvidenceReady | EvidenceInsufficient | RETURN L4 |
| L6 | EvidenceReady | RegimeReady | RegimeUnclear | STOP |
| L7 | RegimeReady | RiskPass | RiskVeto | STOP |
| L8 | RiskPass | StrategyReady | NoStrategy | RETURN L6 |
| L9 | StrategyReady | FlowValid | FlowInvalid | RETURN L4 |
| L10 | FlowValid | HumanApprove | HumanReject | STOP |
| L11 | HumanApprove | Executed | ExecFail | EMERGENCY_STOP |

---

## 3. 多模式一致性設計（Research / Backtest / Simulation / Paper / Live）

### 3.1 為什麼所有模式必須共用同一 Canonical Flow？

- 避免「回測能跑、實盤不能跑」
- 避免「研究捷徑」污染實盤邏輯
- 確保所有決策都有一致的審計語義

### 3.2 模式差異只允許存在於以下三點

| 項目 | 可變動 | 說明 |
|---|---|---|
| 資料來源 | ✅ | 歷史 / 即時 |
| 時間推進 | ✅ | 模擬時間 / 真實時間 |
| Execution 開關 | ✅ | 真實下單 / 模擬 |

🚫 以下不可因模式而改變：
- L1–L11 順序
- Risk / Governance Gate
- Human Decision 存在性

---

## 4. 流程中斷類型（Interrupt Taxonomy）

### 4.1 中斷分類

1. **Hard Stop（硬性中止）**
   - Risk Veto
   - Compliance Violation
   - Kill Switch

2. **Soft Return（可退回）**
   - Evidence 不足
   - Strategy 不適用
   - Flow 完整性不足

3. **Emergency Stop（緊急中止）**
   - Execution 異常
   - 系統錯誤
   - 外部風險事件

### 4.2 中斷後的最小要求

任何中斷必須留下：
- 中斷層級
- 中斷原因碼
- 當下 Evidence Snapshot
- Version Reference

---

## 5. 與風控、治理文件的責任切分（避免重疊）

### 5.1 ARCH_FLOW 負責
- **流程路徑**
- **觸發點**
- **中斷與退回邏輯**

### 5.2 ARCH_FLOW 不負責
- 否決條文細節（→ RISK_COMPLIANCE）
- 下單細節（→ EXECUTION_CONTROL）
- 治理鐵律（→ MASTER_ARCH）

---

## 6. 流程完整性檢查點（Flow Integrity Checkpoints）

在以下節點必須做完整性檢查：

- L5：Evidence Completeness
- L7：Risk Gate Completeness
- L9：Flow Validator
- L11：Post-Execution Integrity

任何一個檢查點失敗：
- 不得進入下一層
- 必須記錄並可回放

---

## 7. Canonical Flow Mermaid（完整版，含退回路徑）

flowchart TB
  L1[L1 Data Source] --> L2[L2 Normalization]
  L2 --> L3[L3 Snapshot & State]
  L3 --> L4[L4 Analysis]
  L4 --> L5[L5 Evidence Builder]

  L5 -->|OK| L6[L6 Regime Engine]
  L5 -->|Insufficient| L4

  L6 -->|OK| L7[L7 Risk & Compliance]
  L6 -->|Unclear| STOP1[STOP]

  L7 -->|PASS| L8[L8 Strategy & Research]
  L7 -->|VETO| STOP2[STOP]

  L8 -->|OK| L9[L9 Governance Gate]
  L8 -->|None| L6

  L9 -->|PASS| L10[L10 Human Decision]
  L9 -->|INVALID| L4

  L10 -->|APPROVE| L11[L11 Execution]
  L10 -->|REJECT| STOP3[STOP]

  L11 -->|SUCCESS| END[END]
  L11 -->|FAIL| EMERGENCY[EMERGENCY STOP]
8. 與 FULL_ARCH 的對位說明（強制一致）
FULL_ARCH 定義 「有哪一層、有哪一模組」

ARCH_FLOW 定義 「它們怎麼按順序動起來」

任何實作：

若流程存在但架構無對應模組 → 非法

若架構存在但流程跳過 → 非法

9. 演進規則（Only-Add）
允許：

新增子流程（例如 L4.1、L7.2）

新增中斷類型與原因碼

新增模式支援（如 Sandbox）

禁止：

刪除或合併 L1–L11

改寫既有中斷語義

以「簡化流程」為由跳層

（ARCH_FLOW｜最大完備版 · Part 1 完）

 TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219
## Part 2｜審計・回放・版本一致性（Audit / Replay / Version Alignment）

doc_key：ARCH_FLOW  
治理等級：B+（Canonical Flow Specification｜承接 MASTER_CANON / FULL_ARCH）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（流程層細化，允許 Only-Add 擴充）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
變更原則：Only-Add（僅可新增，不可刪減／覆寫／改寫語義）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT  

---

## 10. 審計（Audit）總則｜「無紀錄＝未發生」

### 10.1 審計的治理定位
- 審計不是除錯工具，而是 **治理事實的唯一證據**。
- 任何流程節點若無審計物（Artifact），該節點在制度上 **視為未發生**。

### 10.2 審計覆蓋範圍（必覆蓋）
- L1–L11 **每一層**  
- 所有 **中斷 / 退回 / 否決 / 急停**  
- 所有 **模式差異（Research / Backtest / Simulation / Paper / Live）**

### 10.3 審計不可被替代
- 不得以 Console Log、暫存檔、即時記憶體狀態替代正式審計物。
- 不得以「結果正確」合理化「缺審計」。

---

## 11. 全鏈路審計欄位（Mandatory Audit Fields）

> 下列欄位為 **最小必備集合**；可擴充，不可縮減。

### 11.1 通用欄位（所有層級）
- `correlation_id`（串起一次完整流程）
- `session_id`（一次操作會話）
- `layer_id`（L1–L11）
- `module_id`
- `timestamp_utc`
- `version_ref`（文件／政策／模型版本）
- `input_hash`
- `output_hash`
- `status`（SUCCESS / FAIL / RETURN / VETO）
- `reason_codes`（若非 SUCCESS 必填）

### 11.2 層級專屬補充
- **L3（Snapshot）**：`snapshot_id`, `market_time`
- **L5（Evidence）**：`evidence_id`, `provenance_map_ref`
- **L6（Regime）**：`regime_label`, `confidence`
- **L7（Risk）**：`policy_version`, `veto_reason_codes`
- **L10（Human）**：`user_id`, `ui_trace_ref`
- **L11（Execution）**：`order_id_map`, `kill_switch_events`

---

## 12. 回放（Replay）規範｜可重建、可驗證

### 12.1 回放的定義
回放（Replay）是指：  
> **在不接觸即時系統、不連動外部世界的前提下，完整重建某一次決策當下的上下文。**

### 12.2 Replay Bundle（最小集合）
- `documents_active_map`（當下生效文件版本）
- `evidence_bundle`
- `regime_state`
- `risk_gate_decision`
- `human_decision`（若有）
- `execution_logs`（若有）
- `all_hashes`（完整性校驗）

### 12.3 回放一致性要求
- 相同 Replay Bundle → 必須產生 **相同結論**  
- 若結果不同 → 視為 **版本或資料污染**

---

## 13. 版本一致性（Version Alignment）

### 13.1 版本引用原則
- 所有流程輸出 **必須綁定 version_ref**
- version_ref 至少包含：
  - 文件版本（doc_key@version）
  - 風控政策版本
  - 模型／規則版本（若有）

### 13.2 Only-Add 與回放相容
- 新版本上線不得破壞舊 Replay
- 舊 Replay 必須能在新系統中被載入、檢視、驗證

### 13.3 與 VERSION_AUDIT 的關係
- ARCH_FLOW：定義「流程在哪裡產生版本引用」
- VERSION_AUDIT：定義「版本如何被管理、追溯、回退」

---

## 14. 流程中斷與否決的審計語義

### 14.1 否決（VETO）
- 必須記錄：
  - 否決層級
  - 否決原因碼
  - 相關 Evidence / Regime 快照
- 不得以摘要取代原始證據

### 14.2 退回（RETURN）
- 必須記錄：
  - 退回起點與目標層
  - 需補齊項目清單
- 退回不是重跑；是 **補齊後再前進**

### 14.3 緊急中止（EMERGENCY STOP）
- 觸發條件：
  - 系統錯誤
  - 市場異常
  - 人工 Kill Switch
- 必須：
  - 立即中止 Execution
  - 完整留存事發前後審計物

---

## 15. 不同運行模式下的審計一致性

| 模式 | 是否需要審計 | 說明 |
|---|---|---|
| Research | 是 | 防止研究捷徑污染 |
| Backtest | 是 | 可對齊實盤回放 |
| Simulation | 是 | 驗證流程完整 |
| Paper | 是 | 與 Live 同構 |
| Live | 是 | 法遵與追責 |

📌 **審計密度不可因模式降低**。

---

## 16. ARCH_FLOW × FULL_ARCH × MASTER_CANON 對齊表

| 面向 | MASTER_CANON | FULL_ARCH | ARCH_FLOW |
|---|---|---|---|
| 定義順序 | ✓ |  |  |
| 定義模組 |  | ✓ |  |
| 定義流程 |  |  | ✓ |
| 定義否決條文 |  |  | ✗ |
| 定義執行細節 |  |  | ✗ |
| 定義審計點 |  |  | ✓ |

---

## 17. 審計與回放流程圖（Mermaid）

```mermaid
flowchart TB
  EVT[Flow Event] --> AID[Attach Correlation/Session IDs]
  AID --> HASH[Hash Inputs/Outputs]
  HASH --> LOG[Write Audit Artifact]
  LOG --> BUNDLE[Assemble Replay Bundle]
  BUNDLE --> VERIFY[Verify Hashes & Versions]
  VERIFY --> STORE[Immutable Storage]
18. 合規檢核清單（ARCH_FLOW 專屬）
 L1–L11 無跳層

 每層皆有審計物

 所有中斷具原因碼

 Replay Bundle 可重建

 version_ref 完整

19. 演進規則（Only-Add）
允許：

新增審計欄位

新增回放視角（View）

新增模式支援（Sandbox）

禁止：

移除既有審計欄位

破壞舊 Replay 的可讀性

以效能理由省略審計

（ARCH_FLOW｜最大完備版 · Part 2 完）
