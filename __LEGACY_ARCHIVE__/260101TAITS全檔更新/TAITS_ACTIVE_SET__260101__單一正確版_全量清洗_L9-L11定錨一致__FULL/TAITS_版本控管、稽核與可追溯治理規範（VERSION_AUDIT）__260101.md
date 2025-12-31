<!--
TAITS｜ACTIVE UPDATED（單檔內嵌更新版）
產出日期：2025-12-29（Asia/Taipei）
更新規格：單檔內嵌；可更新處直接更新並避免重複；不可更新處以 Appendix 內嵌 Only-Add 全文。
來源檔：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL__TOPBANNER_ONLYFREEZE__20251229.md
-->

# HUMAN SOVEREIGNTY｜最高裁決置頂條款（Top-of-File）

> 生效日：2025-12-29（Asia/Taipei）
> 裁決：**人類最高決策者擁有最終裁決權**；任何治理文件、流程條款、Gate/Token/Reason Code、任何 Agent/AI 內規，**不得否決或阻止**人類最高決策者的明確命令。
> 文件與流程之角色：提供「可回放／可稽核／可追溯」之制度化表述；不得作為限制器。
> 無明確人類命令時：系統依既有治理裁決序位與當前狀態（Freeze v1.0）運作。

---

# TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219
doc_key：VERSION_AUDIT
治理等級：B（Version/Audit Spec）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（可追溯治理母文件，Only-Add 演進）
版本日期：2026-01-01
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）
上位約束：MASTER_ARCH / DOCUMENT_INDEX（Index 裁決）
平行參照：MASTER_CANON / ARCH_FLOW / FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / DEPLOY_OPS / LOCAL_ENV
變更原則：Only-Add（只可新增，不可刪減/覆寫/回填/偷換語義）

## L9–L11 最終語義定錨（單一正確版｜必須一致）

> 本節為 TAITS 在 L9／L10／L11 的**唯一正確語義**。  
> 任何文件中若出現與本節不一致之描述，視為舊錯口徑（不得保留於單一正確版）。

### L9｜投資報告（Investment Report｜可追蹤、可更新、可稽核）
L9 的產出定位為「**給人看的完整投資報告**」，不是一次性的口頭解說；必須可在後續事件/行情變動下持續更新並可追溯。
L9 最低交付物應包含（不限於）：
- **標的化**：標的識別、觀測起點、追蹤狀態（open/hold/watch/exit-candidate 等）、版本號與時間戳。
- **數據**：對應 L1–L8 的關鍵數據表（消息/基本/技術/籌碼/風險/制度），含來源、取樣時間、缺漏註記。
- **圖形**：至少包含價格走勢與關鍵技術指標狀態視覺化（例如均線、RSI、MACD；以「狀態」呈現，非主觀敘事）。
- **進出場建議（非下單）**：建議區間/觸發條件/失效條件（停損/停利/風險撤退），並明確標示「此為建議，不構成下單」。
- **情境更新（Regime/Event）**：當市場制度/事件/風險狀態改變，需能產生增量更新（delta）並保留回放鏈。
- **可稽核鏈**：引用到 L11 的 record_id / ledger_id（或等價識別），以確保報告可被回放與驗證。

### L10｜人類裁決與交易授權（Human Decision & Authorization｜唯一決策點）
L10 的定位為「**人類最高決策者的最終裁決介面與授權層**」。  
- **最終決策者永遠是人類**：你決定採取何種模式與是否授權交易。
- L10 可裁決/授權的動作包含（不限於）：**不動作／回測／模擬／半自動／全自動**。
- AI/Agent 在 L10 僅能提供「選項、理由、風險揭露與建議」，**不得自行構成下單行為**；下單/執行屬於 L10 授權後由執行控制規範承接。

### L11｜工程稽核與全層回放（Engineering Audit & Replay｜全層留痕）
L11 的定位為「**工程檢視與稽核回放層**」，不是下單層，也不是只記錄 L10。
- **全層留痕**：L11 必須覆蓋 L1–L11 每一層的關鍵輸入/輸出/裁決/否決/變更理由與時間戳。
- **雙料輸出**：同一筆紀錄需同時具備  
  1) 人話可讀（你能看懂，用於檢視系統是否合理）  
  2) 工程可用（可重現、可驗證、可追溯，用於開發/稽核/回放）
- **目的**：用來檢查每一層的功能是否合理、是否需要調整、以及自動/半自動/全自動在不同時點的決策依據是否一致可回放。

核心鐵律：無版本＝不可執行；無稽核＝未發生；可回放＝可追責

---

## 0. 文件定位（Version & Audit Charter）

本文件定義 TAITS 的「版本控管、稽核與可追溯治理」最高規範，負責確保：

- 所有文件、政策、規則、模型、設定檔、執行紀錄皆可：
 - **被追溯（Traceable）**
 - **被回放（Replayable）**
 - **被審計（Auditable）**
 - **不可抵賴（Non-repudiable）**
- 系統在任何模式下皆遵守：
 - **Only-Add（只增不減）**
 - **Scope Freeze（凍結後不得越界）**
 - **Evidence 法律地位（無證據視為未發生）**

📌 本文件不負責（避免越權）
- 不定義風控否決條文（→ RISK_COMPLIANCE）
- 不定義執行細節（→ EXECUTION_CONTROL）
- 不改寫 Canonical Flow（→ MASTER_CANON / ARCH_FLOW）
- 不定義 UI 外觀（→ UI_SPEC）
- 專注於「版本如何被管理、稽核如何生成、回放如何成立、變更如何可追責」

---

## 1. 官方參考入口（Official References｜版本與稽核依據）

> 本節提供 TAITS 所依循的主流版本控管/稽核觀念之官方入口（非裁決 TAITS 母法）。

- Git 官方文件（Git Documentation）
 https://git-scm.com/doc
- GitHub Docs（版本控管/PR/保護分支/稽核）
 https://docs.github.com/
- Semantic Versioning（語意化版本）
 https://semver.org/
- iCalendar / RFC 5545（若需排程稽核/治理事件）
 https://www.rfc-editor.org/rfc/rfc5545

---

## 2. TAITS 可追溯治理的四大目標（Hard Objectives）

1) **可回放（Replayability）**
 同一組 Replay Bundle 在相同版本映射下，必須可重建同一結論（或可解釋差異）。

2) **可稽核（Auditability）**
 任一決策/否決/執行事件，必須能回到其證據、版本、責任者與過程。

3) **不可抵賴（Non-repudiation）**
 人類裁決、政策變更、上線切換，必須有可驗證簽章或等價的不可否認性記錄。

4) **Only-Add（不可刪改）**
 禁止覆寫與回填；歷史只能被「新增一筆新版本」取代，不得刪除舊版本存在。

---

## 3. 版本治理對象（Versioned Objects Universe）

TAITS 必須納入版本治理的對象（最小集合，可擴充不可縮減）：

### 3.1 文件版本（Docs）
- 所有 `doc_key` 文件（含 MASTER / B / C / D 等級）
- Document Index（文件索引）本身也是版本治理對象（Index 裁決）

### 3.2 政策版本（Policies）
- Risk Policy Profile（風控政策檔）
- Compliance Rulebook Snapshot（制度快照）
- Execution Policy（下單速率/撤單策略/熔斷政策）
- UI Governance Policy（顯示、trace、兩段式確認門檻等）

### 3.3 規則版本（Rules）
- Regime 判定規則版本（不等於策略）
- Evidence Completeness 規則版本
- Governance Gate 規則版本

### 3.4 模型版本（Models｜若存在）
- 任何 AI/ML 模型、Prompt、權重、特徵定義、後處理規則
- 模型不是決策者，但其版本必須可追溯

### 3.5 設定版本（Configs）
- 環境設定（LOCAL_ENV 中的可版本化部分）
- 交易通道設定（不含敏感金鑰本體）
- 資料源設定（DataSources Adapter Map）

### 3.6 審計與回放物（Artifacts）
- Evidence Bundle
- Regime State Snapshot
- Risk Gate Decision + Token
- UI Decision Trace
- Execution Logs（Pre / In / Post）
- Reconciliation Report
- Kill Switch / Circuit Breaker Events

---

## 4. 核心識別碼（Identity System）

> 一切可追溯治理，從「能唯一識別」開始。

### 4.1 doc_key（文件主鍵）
- 全專案唯一
- 必須出現在每份文件 header
- 未列入 DOCUMENT_INDEX 的 doc_key：不得引用（GOV-DOC）

### 4.2 correlation_id（全鏈路關聯鍵）
- 串起一次完整 Canonical Flow（L1–L11）
- 必須出現在：
 - Evidence、Risk、UI、Execution、Audit 全部輸出

### 4.3 session_id（會話鍵）
- UI/使用者操作會話的識別碼
- 用於稽核人類行為軌跡

### 4.4 artifact_id（審計物鍵）
- 每個 artifact（JSON/Parquet/Log/Bundle）必須有唯一 id

---

## 5. 版本映射（Active Version Map｜必須存在）

### 5.1 Active Version Map 的定義
Active Version Map 是「在某一次流程中，所有生效版本的集合」：

- `docs_active_map`：doc_key → doc_version_id
- `policy_active_map`：policy_key → policy_version
- `rulebook_snapshot_id`
- `model_active_map`：model_id → model_version
- `config_active_map`：config_id → config_version
- `code_commit_ref`：git commit hash / tag（若有）

### 5.2 強制規則
- 任何 PASS / APPROVE / EXECUTE：
 - 必須綁定一份 Active Version Map
- 缺 Active Version Map：
 - 視為 SYS-VERSION-01 → VETO / BLOCK

---

## 6. Only-Add 變更制度（Change Governance）

### 6.1 禁止事項（Hard Forbidden）
- 覆寫既有版本內容
- 刪除歷史版本
- 回填（Backfill）稽核紀錄
- 用「修正舊檔」代替「新增新版本」

### 6.2 允許事項（Only-Add Allowed）
- 新增版本：
 - `__YYMMDD` 或 `__251219` 類型日期標記（TAITS 制度優先）
- 新增補充章節（不得刪原章節）
- 新增 reason_code / policy_key / artifact type

### 6.3 Scope Freeze（範圍凍結）
- 當某版本被標記為 ACTIVE 且進入 Live/Paper 供應鏈：
 - 該版本的語義不得被改寫
 - 任何變更只能透過「新版本」上線

---

## 7. 變更流程（Change Lifecycle｜最大完備）

> 本節定義「變更如何被提出、審核、上線、回溯」。

### 7.1 Change Request（CR）
每個變更必須建立 CR（可文件化，不必依賴特定工具）並至少包含：
- `change_id`
- `scope`（doc/policy/rule/model/config）
- `reason`（原因，禁止用「感覺更好」）
- `risk_impact`（可能影響哪些風控/合規/執行）
- `rollback_plan`（回滾策略）
- `approver`（責任者）
- `effective_time`

### 7.2 Review Gate（審核闸門）
- 任何變更若影響：
 - Risk / Compliance / Execution / UI 決策流程
 必須經過對應治理等級的 Review（A 級要求更嚴格）

### 7.3 Activation（生效）
- 生效必須：
 - 生成新的 Active Version Map
 - 記錄切換事件（Activation Event）
 - 保留舊 Active Map 供回放

### 7.4 Rollback（回滾）
- 回滾不是覆寫，而是：
 - 切回舊版本為 Active（新增一筆切換事件）
- 回滾事件必須產生：
 - `rollback_event_id`
 - `from_version` / `to_version`
 - `reason`

---

## 8. 稽核（Audit）制度（「無稽核＝未發生」）

### 8.1 稽核層級
- **System Audit**：流程/版本/完整性
- **Decision Audit**：Evidence/Regime/Risk/Gov/UI
- **Execution Audit**：Pre/In/Post + 對帳 + 急停
- **Ops Audit**：部署/上線/金鑰/權限（DEPLOY_OPS / LOCAL_ENV）

### 8.2 稽核輸出最小集合（Artifacts Must-Have）
- `active_version_map.json`
- `evidence_bundle_ref`
- `regime_state_ref`
- `risk_gate_decision.json` + `risk_pass_token_ref`（PASS 時）
- `governance_report_ref`
- `ui_trace_ref`（有人類裁決時）
- `execution_logs_ref`（有執行時）
- `reconciliation_report_ref`（有執行時）

缺任一項：
- PASS 不成立 / EXEC 不合法（依 RISK/EXEC 規範 BLOCK）

---

## 9. 回放（Replay）規範（Replayability Contract）

### 9.1 Replay Bundle 必備內容
- `active_version_map`
- `input_data_refs`（資料引用，含 provenance）
- `snapshot_state_refs`
- `feature_set_refs`
- `evidence_bundle`
- `regime_state`
- `risk_gate_decision`（含 reason codes）
- `human_decision_trace`（若有）
- `execution_logs`（若有）
- `hash_manifest`（完整性校驗）

### 9.2 Replay 驗證規則（Replay Verification）
- hash 全數驗證成功
- 版本映射可解析（doc/policy/model/config 均可定位）
- 若結果與歷史不同：
 - 必須能指出差異來源（版本不同/資料不同/政策不同）
 - 否則視為污染（SYS-HASH / SYS-VERSION）

---

## 10. 日誌與不可變更儲存（Immutable Storage）

### 10.1 Immutable 的最低要求
- 審計物必須寫入：
 - Append-only（只能追加）
 - 具備防竄改校驗（hash / signature）

### 10.2 禁止
- 允許任意刪除/修改稽核檔
- 用一般可覆寫的路徑存放「唯一稽核真相」

> 實作細節（S3 Object Lock/WORM/Append-only DB 等）由 DEPLOY_OPS 決定；
> 本文件只規定「必須不可變更」。

---

## 11. 責任矩陣（RACI｜可追責）

> TAITS 治理強制：任何變更與裁決必須可追溯到責任者。

### 11.1 最小 RACI 角色
- `Author`（提出者）
- `Reviewer`（審核者）
- `Approver`（核准者）
- `Operator`（上線/切換執行者）
- `Auditor`（稽核查核者）

### 11.2 強制規則
- 沒有 Approver：不得生效
- 沒有 Operator 記錄：不得認定已部署
- 沒有 Auditor 可查：不得宣稱可追溯

---

## 12. 文件命名與版本格式（TAITS 專案規範）

### 12.1 文件命名
- 檔名格式（建議一致）：
 `TAITS_<中文主標題>（<DOC_KEY>）__YYMMDD.md`
 例：`TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md`

### 12.2 版本日期
- 一律使用台灣時區（Asia/Taipei）對應日期
- 本次版本：2026-01-01（__251219）

### 12.3 版本狀態（ACTIVE / DRAFT / ARCHIVED）
- ACTIVE：可用於 Paper/Live 或作為裁決依據
- DRAFT：草案不得作為裁決依據
- ARCHIVED：歷史封存，仍可回放不得刪

---

## 13. 版本與稽核的「硬性阻斷條件」（Block Conditions）

以下任一條件成立，系統必須阻斷（BLOCK / VETO）：

- 缺 `active_version_map`
- doc_key 未列入 DOCUMENT_INDEX 卻被引用（GOV-DOC）
- hash 驗證失敗（SYS-HASH）
- 稽核物不可寫入（SYS-AUDIT）
- Token 與 evidence/regime/account 快照不一致（SYS-VERIFY）
- 發現覆寫或回填行為（GOV-SCOPE / GOV-FLOW）

---

## 14. Mermaid｜版本與回放治理流程圖（可直接放入 md）

```mermaid
flowchart TB
 A[Change Request] --> B[Review Gate]
 B -->|APPROVE| C[Create New Version (Only-Add)]
 C --> D[Activation Event]
 D --> E[Generate Active Version Map]
 E --> F[Run Flow (L1-L11)]
 F --> G[Write Immutable Artifacts]
 G --> H[Assemble Replay Bundle]
 H --> I[Replay Verification]
 I -->|PASS| J[Auditable & Traceable]
 I -->|FAIL| K[Integrity Incident (SYS-HASH/VERSION)]
```
15. Only-Add 演進規則（本文件專屬）
允許新增：

新的 artifact 類型

新的 version_map 欄位

新的 RACI 角色

新的 block condition（更嚴格）

禁止：

刪除任何既有稽核必備輸出

弱化 immutable 要求

允許覆寫或回填

允許「缺版本仍可執行」

16. 終極裁決語句（不可更改）
版本是制度的邊界，稽核是事實的證明，回放是責任的載體。
任何缺一者，都不允許進入執行。

（VERSION_AUDIT｜最大完備版 v2026-01-01 完）


---

# Appendix A｜Only-Add：METADATA_FIX 變更帳本（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219（doc_key：VERSION_AUDIT）
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON
> 目的：依 DOCUMENT_INDEX 之「Metadata Discrepancy（中繼資料差異）」要求，提供 VERSION_AUDIT 內可追溯的 **METADATA_FIX 變更帳本**；用於修補「doc_key / 治理等級 / 版本狀態 / 檔名標示 / 名詞別名」等中繼資訊不一致之風險，不新增流程、不改裁決位階、不產生新權力。

---

## A.1 適用範圍（Scope｜Hard Boundary）

僅適用於下列 **Metadata Discrepancy** 類型（可擴充不可縮減）：

1) `DOC_KEY_MISMATCH`：DOCUMENT_INDEX 裁決之 doc_key 與文件檔頭/內文自述不一致
2) `GOV_LEVEL_MISMATCH`：DOCUMENT_INDEX 裁決之治理等級與文件檔頭標示不一致
3) `STATUS_MISMATCH`：DOCUMENT_INDEX 裁決之版本狀態（ACTIVE/ARCHIVED…）與文件檔頭標示不一致
4) `FILENAME_MISMATCH`：檔名標示與文件檔頭/Index 裁決關係造成可引用性歧義
5) `ALIAS_CONFUSION`：內文使用別名（alias）或概念名詞，可能被誤當成 doc_key（導致引用/稽核/回放鍵錯置）

不適用於（禁止用 METADATA_FIX 變相改寫制度）：

- Canonical Flow（L1–L11）之任何層級語義變更
- Risk/Compliance/Execution/UI 之任何裁決權力變更
- 以 METADATA_FIX 方式「提升」文件治理等級或擴張文件可引用範圍
- 任何涉及「制度內容」之修訂（應走正式 Change Lifecycle：CR→Review→Activation→Rollback）

---

## A.2 METADATA_FIX 變更帳本欄位（Ledger Schema｜最小必填）

每筆 METADATA_FIX 必須至少包含：

- `metadata_fix_id`：唯一識別（建議格式：`VA-METADATA_FIX-YYYYMMDD-####`；不可重用）
- `created_at`：建立時間（Asia/Taipei）
- `effective_time`：生效時間（Asia/Taipei；若為文件更新即為提交/發布時）
- `scope`：`doc`（固定）
- `discrepancy_type`：見 A.1
- `index_evidence_ref`：指向 DOCUMENT_INDEX 的裁決證據（章節/表格定位）
- `affected_doc_keys[]`：受影響 doc_key（以 Index 裁決為準；不可用別名）
- `affected_files[]`：受影響檔名（含舊/新/別名引發之路徑）
- `fix_action`：採用之修補方式（Only-Add；例：新增 Addendum/Guideline/Appendix）
- `reason`：為何必須修補（必須可稽核；禁止「感覺更好」）
- `risk_impact`：可能影響哪些 Gate/回放/引用（最小需列出：Index / Replay / Audit）
- `approver`：核准者（RACI；缺 approver 不得視為已生效）
- `reviewer`：審核者（可與 approver 同人，但不得省略欄位）
- `notes`：補充說明（可選）

---

## A.3 METADATA_FIX Ledger（Append-only）

> 本表只增不減；任何新增條目視為 append-only ledger。
> 若未在此表留存，治理上視為：未修補、未完成、不得宣稱一致性已恢復。

| metadata_fix_id | created_at (Asia/Taipei) | effective_time (Asia/Taipei) | discrepancy_type | affected_doc_keys | affected_files | index_evidence_ref | fix_action | approver | reviewer | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| VA-METADATA_FIX-20251227-0001 | 2025-12-27T04:00:00+08:00 | 2025-12-27T04:00:00+08:00 | DOC_KEY_MISMATCH / GOV_LEVEL_MISMATCH / ALIAS_CONFUSION | [DATA_SOURCES] | TAITS_資料來源全集（DATA_SOURCES）__251219.md | DOCUMENT_INDEX Appendix A.4（Metadata Discrepancy → 必須建立 METADATA_FIX） | 新增 Addendum 0（Only-Add）：鎖定 doc_key 與名詞 alias 邊界；禁止以 alias 作 doc_key | 使用者（產品負責人/架構裁決者） | 使用者（產品負責人/架構裁決者） | 目的：修補「DATA_UNIVERSE（概念名詞）」被誤當 doc_key 之風險；同時強化引用合法性。 |

---

## A.4 本次條目之最小稽核要點（Audit Checklist｜METADATA_FIX）

稽核時至少檢查：

1) DOCUMENT_INDEX 之裁決欄位（doc_key/治理等級/版本狀態）是否被明確引用為 **唯一真相**
2) 文件內所有 alias/概念名詞是否被明確降格為「閱讀用別名」，且禁止作 doc_key
3) 若系統或人類在引用/回放中仍使用錯誤 doc_key：必須視為 `GOV-DOC`／`SYS-VERSION` 類阻斷條件（依本文件 13 章 Block Conditions 精神）
4) 變更帳本是否含 `metadata_fix_id / effective_time / approver` 三要素（缺任一：不得宣稱完成）

---

（Appendix A｜METADATA_FIX Ledger｜Freeze v1.0｜Only-Add 完）

---