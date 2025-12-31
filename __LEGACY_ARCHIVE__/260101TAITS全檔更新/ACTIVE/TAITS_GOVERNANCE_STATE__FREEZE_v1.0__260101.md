# TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220

doc_key：GOVERNANCE_STATE  
治理等級：A  
版本狀態：ACTIVE（單一正確版｜全量重排版｜保留原文附錄）  
版本日期：2026-01-01  
檔案日期碼：260101  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
變更原則：**不刪減原文**；錯誤口徑不在正文混留，改以「附錄：原文保留」承接（避免混讀）。  

---
## 0. SOVEREIGNTY｜人類最高決策者唯一主權（不可牴觸）

- TAITS 之唯一最高主權屬於：**人類最高決策者（產品負責人／架構裁決者）**。
- 任何文件治理等級（A+／A／B／C）、任何治理閘門（Gate）、任何 Agent、任何 AI 規則、任何流程條款，**不得與人類最高決策者之明確命令牴觸**。
- 系統之責任為：在不阻擋命令的前提下，提供風險揭露、合規告警、替代方案，並強制完成稽核留痕與可回放紀錄。

### 0.1 HFI｜人類最終命令（Human Final Instruction）格式（本版定錨）
> 本段為**可執行觸發機制**：用以避免「主權存在但實務被 Freeze/Only-Add 卡死」。

**Valid HFI 最低要件：**
- `hfi_id`：HFI-YYYYMMDD-###
- `authority_actor`：人類最高決策者識別
- `authority_time`：Asia/Taipei 時戳
- `scope`：doc_key / 章節路徑 / 全檔（明確指定）
- `action`：overwrite / rewrite / reformat / replace / publish_s1 / publish_s2（至少一項）
- `intent`：目的（例如：修正錯誤定位、全量重排版、統一 L9–L11 語義）
- `acknowledgement`：最終裁決確認（「我已閱讀風險揭露並確認執行」或等價語句）

### 0.2 HFI Override（放行原則）
當 Valid HFI 存在時：
- **Freeze / Only-Add / Gate 限制不得阻止** HFI `scope` 範圍內之更新、覆寫、重排版或全量替換。
- Risk/Compliance 必須輸出完整風險揭露與反對理由，但其結果不得升格為阻止人類命令之否決；以「強制揭露＋確認＋全紀錄」承接。


## 1. Canonical Flow（L1–L11）｜L9–L11 最終語義定錨（本版唯一裁決口徑）

### 1.1 L1–L8（資訊收集與篩選層）
- **L1–L8**定位為：資料與訊號之**收集、清洗、特徵化、策略候選生成、風險/合規前置約束、Regime/Context 判讀、資金配置草案與執行前檢查**。
- 其產出不直接構成下單；其定位為 L9/L10 的輸入（Inputs）。

### 1.2 L9（投資報告層）｜必須「可讀、可追蹤、可更新」
L9 不只是解說；其定位為「**可操作的投資報告**」，至少包含：
- **數據與圖形**（可視化、統計摘要、關鍵時間序列）
- **進出場價格建議與條件**（區間/觸發條件/風險情境）
- **交易標的化追蹤**（同一標的可跨事件/跨時間更新報告；需能追溯每次更新原因）
- **買與賣的全週期**：可長抱、提早出場、停損、停利、動態調整（市場隨事件與 Regime 變動而更新）

### 1.3 L10（人類裁決／交易決策層）｜下單唯一入口
- L10 是你（人類最高決策者）做最後裁決的層：**不動作／半自動／全自動／回測／模擬／實盤**的選擇皆在 L10。
- **下單屬於 L10**；AI/策略/報告都不得自動等同於下單。

### 1.4 L11（工程稽核回放層）｜全層紀錄（非下單）
- L11 定位為：**工程稽核、可回放、可追溯**的全層記錄（涵蓋 L1–L10）。
- L11 的紀錄必須同時滿足：
  - 你能看懂的「人話版」摘要與關鍵證據鏈
  - 工程能用的「機讀版」結構化紀錄（Hash/事件流/參數/版本/輸入輸出）
- L11 **不做下單**；其作用是檢視系統每一層是否合理、是否需要調整（含半自動/全自動交易流程的可稽核性）。


## 2. 稽核承接（Mandatory Audit Artifacts）

任何由 HFI 放行的更新/覆寫/重排版/全量替換，必須同步產生：
1. **VERSION_AUDIT｜HFI Ledger**（含 change_id、scope、影響清單、套用順序、責任確認）
2. **HASH_MANIFEST**（全檔 SHA256 指紋清單）
3. **CHANGELOG**（逐檔變更摘要：改了什麼、為何改、影響範圍）

> 稽核要求用於回放與追責，不構成對人類主權命令的否決。
---

## 99. 附錄｜原文全文保留（不刪減｜供追溯與對照）
> 說明：以下為 `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` 之原文全文，為避免舊標示/舊備註干擾裁決，本版將「單一正確口徑」置於正文；原文作為歷史證據保留。

# TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220
doc_key：GOVERNANCE_STATE_FREEZE_V1  
治理等級：A（Governance State｜治理狀態裁決文件）  
適用範圍：TAITS 全系統（對所有 B/C 文件施加 Freeze v1.0 之變更門檻與 Only-Add 約束）  
版本狀態：ACTIVE（Freeze v1.0 生效）  
版本日期：2025-12-20  
上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ AI_GOV（A+）  
平行參照：VERSION_AUDIT / GOVERNANCE_GATE_SPEC / DEPLOY_OPS  
變更原則：Only-Add（本文件為狀態宣告；任何狀態切換必須以「新 GOVERNANCE_STATE_* 文件」形式新增並納入 DOCUMENT_INDEX）  

---

## 0. 文件定位（State Declaration）

本文件為 TAITS 的「治理狀態宣告文件」，用於宣告：

- 當前治理狀態 = **Freeze v1.0**
- Freeze v1.0 對「文件變更」之最小限制與門檻
- Freeze v1.0 與 Only-Add 的適用邊界（避免誤解為可任意改寫）

本文件不定義（避免越權）：
- 不定義任何交易策略、不定義下單、不定義風控/合規細節（其裁決仍以各母文件為準）
- 不重排治理等級覆蓋規則（A+ > A > B > C 由 DOCUMENT_INDEX 裁決）

---

## 1. Freeze v1.0 宣告（Binding）

### 1.1 Freeze v1.0 生效
自本文件版本日期起，TAITS 進入：

- `GOVERNANCE_STATE = Freeze v1.0`

### 1.2 適用範圍
Freeze v1.0 對下列文件之「變更方式」生效：

- 所有 **B / C** 治理有效文件（以 DOCUMENT_INDEX｜Authoritative Index 表格為準）
- 對 **A / A+** 文件：不得以 Freeze v1.0 作為弱化或改寫之理由（A/A+ 之變更仍須走其既有最嚴門檻）

---

## 2. Freeze v1.0 期間的變更規則（Hard Rules）

### 2.1 Only-Add 強制
Freeze v1.0 期間：

- **只可新增（Only-Add）**
- 禁止：刪減／覆寫／偷換語義／摘要化導致語義縮減
- 若需修補歧義、補充引用口徑、補充稽核欄位：以「新增章節 / 附錄 / Addendum（Only-Add）」方式處理

### 2.2 結構性變更禁止（Structural Change Ban）
Freeze v1.0 期間，禁止下列變更（即使以新增方式也不允許）：

- 新增或調整治理位階（A+/A/B/C）之覆蓋規則
- 變更 Canonical Flow（L1–L11）之順序或語義（MASTER_CANON 為準）
- 變更 Risk/Compliance 最高否決權（RISK_COMPLIANCE 為準）
- 變更 Execution 安全機制（EXECUTION_CONTROL/DEPLOY_OPS 為準）

### 2.3 版本與稽核必備（Audit Anchor Required）
任何在 Freeze v1.0 期間的新增內容，必須：

- 可定位到 ref_doc_key / ref_file / ref_version / ref_section
- 於 VERSION_AUDIT 留存變更帳本（至少：change_id、範圍、理由、批准者、影響面）

---

## 3. 狀態切換規則（Freeze → Unfreeze）

### 3.1 狀態切換不得覆寫本文件
未來若需解除 Freeze v1.0：

- 必須新增新文件：`TAITS_GOVERNANCE_STATE__UNFREEZE_vX.Y__<date>.md`
- 並在 DOCUMENT_INDEX 內完成 ACTIVE 切換（同 doc_key 僅能一份 ACTIVE）
- 本文件不得被覆寫；僅能由新狀態文件「覆蓋其效力」

### 3.2 保守處置
如狀態切換文件缺失、或 ACTIVE 切換不完整：

- 一律視為 Freeze v1.0 仍生效（保守處置）

---

## 4. 最終宣告（Final）

- Freeze v1.0 生效：B/C 文件僅可 Only-Add。
- 任何牴觸：以 DOCUMENT_INDEX §6（衝突裁決程序）處置。
- 本文件之角色為「狀態宣告」，不創造新治理權力。

（TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220｜ACTIVE）

