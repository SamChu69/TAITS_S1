# HUMAN SOVEREIGNTY｜最高裁決置頂條款（Top-of-File）


## 全局定錨｜單一口徑（S1）

### 1. 人類最高決策者主權（SOVEREIGNTY）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接，不得卡死更新。

### 2. L9–L11 最終語義（跨文件一致）
- L9（投資報告層）：可追蹤、可更新、可標的化投資報告；必含數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源），並支援事件驅動滾動更新。
- L10（人類裁決層）：由人類最高決策者裁決不動作/回測/模擬/半自動/全自動等；任何交易型態皆以 L10 明確裁決為準。
- L11（工程稽核回放層）：對 L1–L11 全層輸入/處理/輸出/裁決/執行鏈路留痕，供人類與工程端可讀、可查、可回放；L11 非下單決策層。

### 3. HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：Freeze/Only-Add/Gate 不得阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。

生效日：2025-12-29（Asia/Taipei）  
裁決：**人類最高決策者擁有最終裁決權**；任何治理文件、流程條款、Gate/Token/Reason Code、任何 Agent/AI 內規，**不得否決或阻止**人類最高決策者的明確命令。  
文件與流程之角色：提供「可回放／可稽核／可追溯」之制度化表述；不得作為限制器。  
無明確人類命令時：系統依既有治理裁決序位與當前狀態（Freeze v1.0）運作。  

---

# TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260101.md
doc_key：VERSION_AUDIT  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（可追溯治理母文件，Only-Add 演進）  
版本日期：2026-01-01  
變更原則：Only-Add（只可新增，不可刪減/覆寫/回填/偷換語義）  
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

本節提供 TAITS 所依循的主流版本控管/稽核觀念之官方入口（非裁決 TAITS 母法）。

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

一切可追溯治理，從「能唯一識別」開始。

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

本節定義「變更如何被提出、審核、上線、回溯」。

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

實作細節（S3 Object Lock/WORM/Append-only DB 等）由 DEPLOY_OPS 決定；  
本文件只規定「必須不可變更」。

---

## 11. 責任矩陣（RACI｜可追責）

TAITS 治理強制：任何變更與裁決必須可追溯到責任者。

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
- 本次版本：2025-12-19（__251219）

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

（VERSION_AUDIT｜最大完備版 v2025-12-19 完）

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
目的：依 DOCUMENT_INDEX 之「Metadata Discrepancy（中繼資料差異）」要求，提供 VERSION_AUDIT 內可追溯的 **METADATA_FIX 變更帳本**；用於修補「doc_key / 治理等級 / 版本狀態 / 檔名標示 / 名詞別名」等中繼資訊不一致之風險，不新增流程、不改裁決位階、不產生新權力。

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
- `reason`：為何必須修補（必須可稽核；禁止「感覺更好」）
- `risk_impact`：可能影響哪些 Gate/回放/引用（最小需列出：Index / Replay / Audit）
- `approver`：核准者（RACI；缺 approver 不得視為已生效）
- `reviewer`：審核者（可與 approver 同人，但不得省略欄位）
- `notes`：補充說明（可選）

---

## A.3 METADATA_FIX Ledger（Append-only）

本表只增不減；任何新增條目視為 append-only ledger。  
若未在此表留存，治理上視為：未修補、未完成、不得宣稱一致性已恢復。

| metadata_fix_id | created_at (Asia/Taipei) | effective_time (Asia/Taipei) | discrepancy_type | affected_doc_keys | affected_files | index_evidence_ref | fix_action | approver | reviewer | notes |
|---|---|---|---|---|---|---|---|---|---|---|

---

## A.4 本次條目之最小稽核要點（Audit Checklist｜METADATA_FIX）

稽核時至少檢查：

1) DOCUMENT_INDEX 之裁決欄位（doc_key/治理等級/版本狀態）是否被明確引用為 **唯一真相**  
2) 文件內所有 alias/概念名詞是否被明確降格為「閱讀用別名」，且禁止作 doc_key  
3) 若系統或人類在引用/回放中仍使用錯誤 doc_key：必須視為 `GOV-DOC`／`SYS-VERSION` 類阻斷條件（依本文件 13 章 Block Conditions 精神）  
4) 變更帳本是否含 `metadata_fix_id / effective_time / approver` 三要素（缺任一：不得宣稱完成）

---

---

## 治理補強（已整合為正文）

上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+）＋MASTER_ARCH（A）＋MASTER_CANON（A）  
目的：補登 2025-12-27 之 Only-Add 更新批次，使跨文件引用之 `audit_anchor / VA-METADATA_FIX-*` 具備可追溯 Ledger 條目，閉合稽核鏈。

---

## 治理補強（已整合為正文）

本批次為 Freeze v1.0 期間之 Only-Add 修補批次：所有條目僅追加，不覆寫既有 Ledger。

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type | reason | alignment_refs |
|---|---|---|---|---|---|---|---|

## 治理補強（已整合為正文）
- 若 output_artifact 之檔名與 repo 內最終落盤檔名不同：以 repo 落盤為準，但必須保留本 Ledger 條目（不可刪）。
- 本批次所有修補均不改寫 Canonical Flow（L1–L11），僅處理引用端歧義、治理標籤（S/B+/C+）法律定位與 alias 封口。
- 任一 fix_id 若被下游文件引用為 `audit_anchor`，而 Ledger 無對應條目：視為稽核鏈缺口，必須以新條目補齊（append-only）。

---

## 治理補強（已整合為正文）

目的：補登 2025-12-27 批次在收斂階段（含入口級文件一致化與 DOCUMENT_INDEX 映射表）新增之 METADATA_FIX 條目，使跨文件 `audit_anchor` 引用可被 Ledger 查得，閉合稽核鏈。  

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

## 治理補強（已整合為正文）
- 本延伸批次屬於 2025-12-27 主批次之「入口一致化 + Index 收斂」尾段工作；只追加 Ledger，不覆寫先前批次內容。  
- 若 repo 最終落盤檔名與本表不同：以 repo 落盤為準，但本 Ledger 條目不得刪除，需以 Only-Add 方式追加更正條目。  

---

## 治理補強（已整合為正文）

目的：補登 2025-12-28 追加之兩項收斂優化（DOCUMENT_INDEX machine-readable mapping 與 DEPLOY_OPS Trace/Evidence Contract），使各文件 `audit_anchor` 可在 Ledger 查得並閉合稽核鏈。  

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---

## 治理補強（已整合為正文）

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

## 治理補強（已整合為正文）

---

## 治理補強（已整合為正文）

目的：補登 DEPLOY_OPS 新增之 Repo 落盤規範（LATEST/ARCHIVE）對應 fix_id，使 `audit_anchor` 可查並閉合稽核鏈。  

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---

## 治理補強（已整合為正文）
上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
目的：補登本更新包之 METADATA_FIX 條目，使跨文件 audit_anchor 可查，閉合稽核鏈。

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---

## 版本戳記（生成時間）
- generated_at: 2025-12-28 02:14:34 +0800（Asia/Taipei）

---

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
目的：補登本次 P0 全閉合更新之 fix_id，使 AI_GOV / GOVERNANCE_STATE_FREEZE_V1 / DOCUMENT_INDEX / VERSION_AUDIT 之 audit_anchor 可查，完成 Append-only 稽核閉環。

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---

## 版本戳記
- generated_at: 2025-12-28 02:30:24 +0800（Asia/Taipei）

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
目的：在 doc_key 正名／alias 封口後，確保歷史 Ledger（Append-only）查帳時仍可一致解析；禁止把 legacy key 誤視為新文件。

---

## J1. Ledger Resolution Rule（Hard）

### J1.1 原則
- Ledger 內任何 `target_doc_key` 若屬 legacy key：
  - 不得因 legacy key 出現而推導「多一份 ACTIVE 文件」

### J1.2 Legacy → Canonical（最低必要集合）
- `GOVERNANCE_STATE` → `GOVERNANCE_STATE_FREEZE_V1`
- `DATA_UNIVERSE` → `DATA_SOURCES`
- `AI_GOVERNANCE_FULLSPEC` → `AI_GOV`

---

## J2. Machine-Readable Ledger Resolution（YAML）

```yaml
ledger_resolution:
  authoritative_source: "DOCUMENT_INDEX"
  rules:
    - legacy_key: "GOVERNANCE_STATE"
      resolve_to: "GOVERNANCE_STATE_FREEZE_V1"
    - legacy_key: "DATA_UNIVERSE"
      resolve_to: "DATA_SOURCES"
    - legacy_key: "AI_GOVERNANCE_FULLSPEC"
      resolve_to: "AI_GOV"
  hard_rules:
    - "MUST_RESOLVE_TARGET_DOC_KEY_VIA_DOCUMENT_INDEX"
    - "MUST_NOT_INFER_NEW_ACTIVE_DOC_FROM_LEGACY_KEY"
```

---

## J3. METADATA_FIX Ledger（Append-Only）— Extension Batch 2025-12-28（P1-NORMALIZATION）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---

## J4. 版本戳記
- generated_at: 2025-12-28 02:48:55 +0800（Asia/Taipei）

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
目的：補登本輪「v2 mapping 補齊」與「GOVERNANCE_STATE 防誤抄 Banner」之 METADATA_FIX 條目，使 audit_anchor 可查，維持 Append-only 稽核閉環。

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---

## 版本戳記
- generated_at: 2025-12-28 02:56:19 +0800（Asia/Taipei）

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
目的：補登「PROJECT_PROMPT ACTIVE 補登」與「DOCUMENT_INDEX schema_version=3 Canonical Bundle」之 METADATA_FIX 條目，使 audit_anchor 可查，維持 Append-only 稽核閉環。

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---

## 版本戳記
- generated_at: 2025-12-28 03:02:28 +0800（Asia/Taipei）

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
目的：補登「DOCUMENT_INDEX Copy-Safe DocKey List」之 METADATA_FIX 條目，使 audit_anchor 可查，維持 Append-only 稽核閉環。

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---

## 版本戳記
- generated_at: 2025-12-28 03:09:05 +0800（Asia/Taipei）

---

## 治理補強（已整合為正文）

目的：提供「可直接貼用」的稽核/回放條目格式，用於登錄本次類型之變更（檔名映射、doc_key alias、Evidence Chain 模板補齊）所需的最小欄位；不改寫既有 Ledger 制度。

### VA-MF-TEMPLATE. METADATA_FIX（範本）

```text
ledger_id: VA-METADATA_FIX-20251228-0001
change_type: METADATA_FIX
scope: Governance Metadata Alignment (Logical→Physical filename map; doc_key alias; evidence chain template anchor)
governance_state: Freeze v1.0
authoritative_index_ref:
  doc_key: DOCUMENT_INDEX
  ref_section: DI-A1~DI-A3
affected_docs:
  - AI_GOV (alias alignment)
  - DATA_SOURCES (alias alignment)
  - LOCAL_ENV (evidence chain template anchor)
  - DEPLOY_OPS / UI_SPEC / EXECUTION_CONTROL / GOVERNANCE_GATE_SPEC (trace/evidence chain cross-reference)
evidence:
  - mapping_table: DOCUMENT_INDEX:DI-A1
  - alias_table: DOCUMENT_INDEX:DI-A2
  - hashes: DOCUMENT_INDEX:DI-A3
notes: Only-Add appendices added; no semantic overwrite; canonical flow unchanged.
```
---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`VERSION_AUDIT`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=VERSION_AUDIT` + `canonical_filename=TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

## 治理補強（已整合為正文）

上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
目的：以 MASTER_CANON 為主導，對齊「引用合法性、doc_key 身份、子級標籤（Label）解讀、資料治理別名（alias）封口、最小可稽核引用格式」之全域一致口徑；不改寫任何既有正文條款。

---

## G0. 適用範圍（Hard Boundary）

1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。  
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。  
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。  
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。  

- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

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

---

## 治理補強（已整合為正文）

上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX）  
目的：為本次「後稽核修補（Errata / Placeholder Norm）」補登 METADATA_FIX Ledger 條目；不改寫任何既有正文條款。

---

## A. METADATA_FIX Ledger（續增｜Only-Add）

| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|
| VA-METADATA_FIX-20251228-0024 | 2025-12-28 | BATCH-20251228-POSTAUDIT-ERRATA | PROCESS_ANCHOR | Define and gate `VA-PLACEHOLDER-0001` usage; ACTIVE requires replacement by valid Ledger ID | PROCESS_ANCHOR |
| VA-METADATA_FIX-20251228-0025 | 2025-12-28 | BATCH-20251228-POSTAUDIT-ERRATA | VERSION_AUDIT | Ledger continuation appended (0023–0025) | VERSION_AUDIT |

## B. 最終宣告

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|

---

## 治理補強（已整合為正文）

| doc_key | status | canonical_filename（Index/引用） | physical_filename（本專案） | sha256_12 | source_alias（來源/舊檔名） |
|---|---|---|---|---|---|
| `GOVERNANCE_STATE_FREEZE_V1` | ACTIVE | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `443dbd4a27a4` | `—` |
| `DOCUMENT_INDEX` | ACTIVE | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `d407ea013bc5` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md` |
| `LOCAL_ENV` | ACTIVE | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md` | `a7f23ecb108f` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` |

---

## 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- ledger_ref: VA-METADATA_FIX-20251231-0001

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|

---

## 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- ledger_ref: VA-METADATA_FIX-20251231-0002

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|

---

## 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- ledger_ref: VA-METADATA_FIX-20251231-0003

## 治理補強（已整合為正文）

目的：補登 P1C（canonical 引用解析）事件，使 loader 在僅依 alias map 模式下亦能回放解析舊版 canonical 引用。

---

## 治理補強（已整合為正文）

| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|

---

## 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- ledger_ref: VA-METADATA_FIX-20251231-0004
