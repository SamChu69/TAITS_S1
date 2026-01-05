# TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260104（單一正確正文版｜最終覆蓋版）

doc_key：VERSION_AUDIT  
治理等級：B（治理／制度級｜版本控管、稽核與可追溯治理規範）  
適用範圍：TAITS 全系統（版本命名/封版/變更留痕/稽核資料結構/重現與回放/Hash Manifest/交付格式）  
版本狀態：ACTIVE（單一正確正文版｜最終覆蓋版｜去混讀＋留痕分離＋章節去重）  
版本日期：2026-01-04（Asia/Taipei）  
裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（最終裁決序位；本檔受其約束，不得與之衝突）  
平行參照：GOVERNANCE_STATE／GOVERNANCE_GATE_SPEC／RISK_COMPLIANCE／EXECUTION_CONTROL／MASTER_CANON／UI_SPEC  
變更原則：**正文不得混入留痕**；Scope/Changelog/Hash/Audit Hand-off 一律置於檔尾「稽核區塊」。

---

## 全局定錨｜單一口徑（S1）

- 所有版本/變更必須可被追溯（Traceable）、可被回放（Replayable）、可被審計（Auditable）、不可抵賴（Non-repudiable）。  
- 治理狀態（Freeze/Unfreeze）僅由 GOVERNANCE_STATE 宣告；任何文件內自述僅視為資訊，不得凌駕上位裁決。  
- 本文件不定義交易授權；交易授權唯一入口為 L10，且受 RISK_COMPLIANCE 最高否決權約束。  

---

本文件定義 TAITS 的「版本控管、稽核與可追溯治理」最高規範，負責確保：

- 所有文件、政策、規則、模型、設定檔、執行紀錄皆可：
  - **被追溯（Traceable）**
  - **被回放（Replayable）**
  - **被審計（Auditable）**
  - **不可抵賴（Non-repudiable）**
- 系統在任何模式下皆遵守：
  - **最大完備＋累積式更新（累積式保留（未明確取代者必保留））**
  - **Scope 治理狀態（凍結後不得越界）**
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

4) **最大完備＋累積式更新（不可刪改）**  
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

## 6. 最大完備＋累積式更新制度（Change Governance｜Single Correct Body）

本章定義 TAITS 的「文件／政策／規則／模型／設定／審計物」更新哲學與硬性邊界。  
本制度之目標是在 **可追溯、可稽核、可回放** 的前提下，允許形成「**單一正確正文版（Single Correct Body）**」並持續提升完備度。

### 6.1 禁止事項（Hard Forbidden）
- **摘要化縮水**：不得以「只保留重點／只留精華」方式刪除有效資訊。
- **無留痕覆寫**：任何覆寫修正都必須伴隨稽核留痕（Scope／Changelog／Hash Manifest／Audit Hand-off），不得只改正文不留痕。
- **回填（Backfill）稽核紀錄**：禁止在裁決/執行後事後補寫或改寫審計物以偽造一致性。
- **刪除可追溯鏈**：不得刪除能追溯版本、責任者、證據與時間戳之關鍵資訊。
- **混用互斥版本**：同一 correlation/session 不得混用互斥的 doc/policy/rule snapshot。
- **以 L11/回放作批准**：回放與記錄不構成批准；批准僅能由 L10 人類裁決。

### 6.2 允許事項（Max-Complete Allowed）
- **融合更新（Fusion Update）**：允許將多版本/多段落整併為「單一正確正文版」，並可重排章節、合併重複、修正錯誤敘述。
- **覆寫修正（Overwrite Correction）**：允許對正文進行覆寫修正以形成正確口徑；但必須同步：
  - 升版（以版本日期/檔名或等價版本鍵表示）
  - 明確列出變更清單（Changelog）
  - 提供正文指紋（Hash Manifest；至少 BODY_ONLY）
  - 提供適用範圍（Scope）與裁決承接（Audit Hand-off）
- **舊內容保留原則（Cumulative Retention Rule）**：未被新版本明確更新之有效內容，一律保留並持續累積；不得因重排而省略。
- **被取代內容之處置（Superseded Handling）**：若新版本已明確取代舊資訊：
  - 舊資訊可自正文移除以避免混讀
  - 但必須在稽核留痕中記錄：被取代段落/條文位置、取代理由、對應新段落位置、版本映射方式（可回溯）

### 6.3 治理狀態 狀態（狀態約束，不等於禁止修正）
治理狀態 的意義是「限制未授權之結構性變更與範圍擴張」，不是把系統鎖死在錯誤口徑。  
治理狀態 狀態下仍允許在 **人類明確命令（HFI）** 的 scope 內進行融合更新／覆寫修正／重排版，以形成單一正確正文；但必須完成本文件規定之稽核留痕與版本承接。  
若無 HFI，則依 GOVERNANCE_STATE 與 DOCUMENT_INDEX 的裁決程序採保守處置（RETURN/BLOCK/STOP）。


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
  - 累積式（只能追加）
  - 具備防竄改校驗（hash / signature）

### 10.2 禁止
- 允許任意刪除/修改稽核檔
- 用一般可覆寫的路徑存放「唯一稽核真相」

實作細節（S3 Object Lock/WORM/累積式 DB 等）由 DEPLOY_OPS 決定；  
本文件只規定「必須不可變更」。

---

### 10.X 環境指紋引用（Env Fingerprint Reference｜不保存個人硬體備忘）

- 本文件（VERSION_AUDIT）的角色是「版本與稽核治理」，不保存特定單一設備的硬體規格，以避免將設備備忘誤讀為執行門檻或制度條款。
- 審計鏈所需之環境資訊，應以 **環境指紋（env_fingerprint）** 與 **引用（env_fingerprint_ref）** 表達，並指向：
  - `doc_key=LOCAL_ENV`（本地執行與運算環境規範）之可重建環境定義
  - 如需人員設備基線備註，應放置於 `doc_key=MASTER_ARCH` 或 `doc_key=LOCAL_ENV` 的專章（不得混入本檔正文）
- 最低要求：任何宣稱「可回放」的流程都必須包含 `env_fingerprint` 與 `env_fingerprint_ref`，以滿足可追溯與可重建要求。

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
  B -->|APPROVE| C[Create New Version (最大完備＋累積式更新)]
  C --> D[Activation Event]
  D --> E[Generate Active Version Map]
  E --> F[Run Flow (L1-L11)]
  F --> G[Write Immutable Artifacts]
  G --> H[Assemble Replay Bundle]
  H --> I[Replay Verification]
  I -->|PASS| J[Auditable & Traceable]
  I -->|FAIL| K[Integrity Incident (SYS-HASH/VERSION)]
```
15. 最大完備＋累積式更新 演進規則（本文件專屬）
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
上位裁決：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
目的：依 DOCUMENT_INDEX 之「Metadata Discrepancy（中繼資料差異）」要求，提供 VERSION_AUDIT 內可追溯的 **METADATA_FIX 變更帳本**；用於修補「doc_key / 治理等級 / 版本狀態 / 檔名標示 / 名詞別名」等中繼資訊不一致之風險，不新增流程、不改裁決位階、不產生新權力。

---

## 15. METADATA_FIX 治理更正制度（A1–A4）

### 15.1 適用範圍（Scope｜Hard Boundary）

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

### 15.2 METADATA_FIX 變更帳本欄位（Ledger Schema｜最小必填）

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

### 15.3 METADATA_FIX Ledger（累積式）

本表累積式保留（未明確取代者必保留）；任何新增條目視為 累積式 ledger。  
若未在此表留存，治理上視為：未修補、未完成、不得宣稱一致性已恢復。

| metadata_fix_id | created_at (Asia/Taipei) | effective_time (Asia/Taipei) | discrepancy_type | affected_doc_keys | affected_files | index_evidence_ref | fix_action | approver | reviewer | notes |
|---|---|---|---|---|---|---|---|---|---|---|

---

### 15.4 本次條目之最小稽核要點（Audit Checklist｜METADATA_FIX）

稽核時至少檢查：

1) DOCUMENT_INDEX 之裁決欄位（doc_key/治理等級/版本狀態）是否被明確引用為 **唯一真相**  
2) 文件內所有 alias/概念名詞是否被明確降格為「閱讀用別名」，且禁止作 doc_key  
3) 若系統或人類在引用/回放中仍使用錯誤 doc_key：必須視為 `GOV-DOC`／`SYS-VERSION` 類阻斷條件（依本文件 13 章 Block Conditions 精神）  
4) 變更帳本是否含 `metadata_fix_id / effective_time / approver` 三要素（缺任一：不得宣稱完成）

---

---
上位裁決：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
目的：補登 2025-12-27 之 最大完備＋累積式更新 更新批次，使跨文件引用之 `audit_anchor / VA-METADATA_FIX-*` 具備可追溯 Ledger 條目，閉合稽核鏈。

---
本批次為 治理狀態 v1.0 期間之 最大完備＋累積式更新 修補批次：所有條目僅追加，不覆寫既有 Ledger。

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type | reason | alignment_refs |
|---|---|---|---|---|---|---|---|
- 若 output_artifact 之檔名與 repo 內最終落盤檔名不同：以 repo 落盤為準，但必須保留本 Ledger 條目（不可刪）。
- 本批次所有修補均不改寫 Canonical Flow（L1–L11），僅處理引用端歧義、治理標籤（S/B+/C+）法律定位與 alias 封口。
- 任一 fix_id 若被下游文件引用為 `audit_anchor`，而 Ledger 無對應條目：視為稽核鏈缺口，必須以新條目補齊（累積式）。

---
目的：補登 2025-12-27 批次在收斂階段（含入口級文件一致化與 DOCUMENT_INDEX 映射表）新增之 METADATA_FIX 條目，使跨文件 `audit_anchor` 引用可被 Ledger 查得，閉合稽核鏈。  

---
| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|
- 本延伸批次屬於 2025-12-27 主批次之「入口一致化 + Index 收斂」尾段工作；只追加 Ledger，不覆寫先前批次內容。  
- 若 repo 最終落盤檔名與本表不同：以 repo 落盤為準，但本 Ledger 條目不得刪除，需以 最大完備＋累積式更新 方式追加更正條目。  

---
目的：補登 2025-12-28 追加之兩項收斂優化（DOCUMENT_INDEX machine-readable mapping 與 DEPLOY_OPS Trace/Evidence Contract），使各文件 `audit_anchor` 可在 Ledger 查得並閉合稽核鏈。  

---
| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---
---
| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|
---
目的：補登 DEPLOY_OPS 新增之 Repo 落盤規範（LATEST/ARCHIVE）對應 fix_id，使 `audit_anchor` 可查並閉合稽核鏈。  

---
| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---
上位裁決：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
目的：補登本更新包之 METADATA_FIX 條目，使跨文件 audit_anchor 可查，閉合稽核鏈。

---
| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---

## 16. Ledger 解析與機讀對齊（J1–J3）

### 16.1 Ledger Resolution Rule（Hard）

### J1.1 原則
- Ledger 內任何 `target_doc_key` 若屬 legacy key：
  - 不得因 legacy key 出現而推導「多一份 ACTIVE 文件」

### J1.2 Legacy → Canonical（最低必要集合）
- `GOVERNANCE_STATE` → `GOVERNANCE_STATE_FREEZE_V1`
- `DATA_UNIVERSE` → `DATA_SOURCES`
- `AI_GOVERNANCE_FULLSPEC` → `AI_GOV`

---

### 16.2 Machine-Readable Ledger Resolution（YAML）

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

### 16.3 METADATA_FIX Ledger（累積式）— Extension Batch 2025-12-28（P1-NORMALIZATION）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

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



### 歷史承接註記｜GLOBAL_ALIGNMENT_PATCH（2025-12-28）

- 補充性質：台帳新增（只可新增，不可刪減、覆寫、偷換既有語義）
- 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__HISTORY_20251228M_FINAL.md（doc_key：VERSION_AUDIT）
- 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）
- 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）
- 稽核對位：VERSION_AUDIT｜台帳批次 A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0015`）
- 目的：以 MASTER_CANON 為主導，對齊「引用合法性、doc_key 身份、子級標籤（Label）解讀、資料治理別名（alias）封口、最小可稽核引用格式」之全域一致口徑；不改寫任何既有正文條款。

---

## 17. 引用一致化規範（G1–G5）

### 17.1 Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

並統一裁決：
- 任何文件「是否可引用」＝以 DOCUMENT_INDEX 之 Authoritative Index（ACTIVE 表格）為準  
- 任何文件「治理等級 bucket」＝以 DOCUMENT_INDEX 之 A+ / A / B / C 分桶為準  
- 文件內自述之等級/狀態若與 Index 有張力：依 DOCUMENT_INDEX §6 採「保守處置」（STOP/RETURN/BLOCK；以既有 Gate/風控規範語義為準）

---

### 17.2 子級標籤（Label）之唯一合法解讀（S / B+ / C+）

凡本文件或引用鏈中出現：
- `S`：視為「Supreme Canon 的顯示標籤」或「完備度標籤」，**不構成**新的治理等級 bucket。  
- `B+` / `C+`：視為「嚴格度/完備度子級標籤」，**不構成**新的治理等級 bucket。  

治理覆蓋規則仍固定為：**A+ > A > B > C**（以 DOCUMENT_INDEX 為準）。  

---

### 17.3 DATA_UNIVERSE（alias）封口（資料治理引用回歸 DATA_SOURCES）

統一裁決：
- 任何出現之 `DATA_UNIVERSE` 一律視為「資料宇宙（Data Universe）」概念別名（alias），**不得**作為 doc_key。  
- 任何需要引用資料來源治理時，唯一合法 doc_key：`DATA_SOURCES`。  
- 若 Evidence/Audit/UI Trace/Gate 引用欄位出現 `doc_key=DATA_UNIVERSE`：  
  - 一律視為「引用非法」→ 依 GOVERNANCE_GATE_SPEC 進行 BLOCK/RETURN（依其既有語義；不得補救）。

---

### 17.4 最小可稽核引用格式（Minimum Legal Citation Format｜可直接貼用）

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

### 17.5 最終宣告（治理狀態 v1.0）

---
上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX）  
目的：為本次「後稽核修補（Errata / Placeholder Norm）」補登 METADATA_FIX Ledger 條目；不改寫任何既有正文條款。

---

## 18. METADATA_FIX Ledger（治理更正台帳｜累積式）
| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|
| VA-METADATA_FIX-20251228-0024 | 2025-12-28 | BATCH-20251228-POSTAUDIT-ERRATA | PROCESS_ANCHOR | Define and gate `VA-PLACEHOLDER-0001` usage; ACTIVE requires replacement by valid Ledger ID | PROCESS_ANCHOR |
| VA-METADATA_FIX-20251228-0025 | 2025-12-28 | BATCH-20251228-POSTAUDIT-ERRATA | VERSION_AUDIT | Ledger continuation appended (0023–0025) | VERSION_AUDIT |

## 19. 終局宣告
上位裁決：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  

---
| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|

---
| doc_key | status | canonical_filename（Index/引用） | physical_filename（本專案） | sha256_12 | source_alias（來源/舊檔名） |
|---|---|---|---|---|---|
| `GOVERNANCE_STATE_FREEZE_V1` | ACTIVE | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `443dbd4a27a4` | `—` |
| `DOCUMENT_INDEX` | ACTIVE | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `d407ea013bc5` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md` |
| `LOCAL_ENV` | ACTIVE | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md` | `a7f23ecb108f` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` |

---


## 20. METADATA_FIX 台帳資料集（S1 歷史條目整併｜累積式）

> 本章為歷史台帳條目資料集之整併收錄，用於可追溯性與工程回放；不作為新增治理規則。
> 已移除 歷史台帳條目/補充資料集/最大完備＋累積式更新 等差分式標籤，以避免新舊混讀；其內容語義由本文件正文與 DOCUMENT_INDEX 裁決承接。

### 20.1 台帳批次｜A｜METADATA_FIX Ledger（累積式）— Extension Batch 2025-12-28（P0-CLOSURE）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|
| VA-METADATA_FIX-20251228-0029 | 2025-12-28 | BATCH-20251228-P0-CLOSURE | AI_GOV | `TAITS_AI_行為與決策治理最終規則全集__251217__HISTORY_20251228H_FINAL.md` | 台帳新增｜P0 全閉合：Index-First doc_key 解析鍵封口＋machine-readable override |
| VA-METADATA_FIX-20251228-0030 | 2025-12-28 | BATCH-20251228-P0-CLOSURE | GOVERNANCE_STATE_FREEZE_V1 | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__HISTORY_20251228H_FINAL.md` | 台帳新增｜P0 全閉合：舊模板作廢（保留歷史）＋唯一合法新模板固定＋alias 封口 |
| VA-METADATA_FIX-20251228-0031 | 2025-12-28 | BATCH-20251228-P0-CLOSURE | DOCUMENT_INDEX | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__HISTORY_20251228H_FINAL.md` | 台帳新增｜P0 全閉合：GOVERNANCE_STATE 正名封口＋mapping override delta（delta） |
| VA-METADATA_FIX-20251228-0032 | 2025-12-28 | BATCH-20251228-P0-CLOSURE | VERSION_AUDIT | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__HISTORY_20251228H_FINAL.md` | 台帳新增｜P0 全閉合：Ledger 補登（累積式） |

---

### 版本戳記｜2025-12-28 02:30:24 +0800（Asia/Taipei）
- generated_at: 2026-01-04 00:00:00 +0800（Asia/Taipei）

（歷史台帳條目 2025-12-28｜台帳新增｜VERSION_AUDIT｜P0 全閉合 完）
---

## 歷史台帳條目｜2025-12-28｜台帳新增：P2 Completeness／Banner Ledger（稽核補登｜（歷史狀態記錄））

> 補充性質：台帳新增（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
> 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
> 目的：補登本輪「v2 mapping 補齊」與「GOVERNANCE_STATE 防誤抄 Banner」之 METADATA_FIX 條目，使 audit_anchor 可查，維持 累積式 稽核閉環。

---

### 20.2 台帳批次｜A｜METADATA_FIX Ledger（累積式）— Extension Batch 2025-12-28（P2-COMPLETENESS）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|
| VA-METADATA_FIX-20251228-0036 | 2025-12-28 | BATCH-20251228-P2-COMPLETENESS | DOCUMENT_INDEX | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__HISTORY_20251228K_FINAL.md` | 台帳新增｜v2 latest_mapping 全量補齊（ACTIVE 全覆蓋＋入口/定錨文件補登） |
| VA-METADATA_FIX-20251228-0037 | 2025-12-28 | BATCH-20251228-P2-COMPLETENESS | GOVERNANCE_STATE_FREEZE_V1 | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__HISTORY_20251228K_FINAL.md` | 台帳新增｜S2 Template Hard Banner（防誤抄封口） |
| VA-METADATA_FIX-20251228-0038 | 2025-12-28 | BATCH-20251228-P2-COMPLETENESS | VERSION_AUDIT | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__HISTORY_20251228K_FINAL.md` | 台帳新增｜Ledger 補登（累積式） |

---

### 版本戳記｜2025-12-28 02:56:19 +0800（Asia/Taipei）
- generated_at: 2026-01-04 00:00:00 +0800（Asia/Taipei）

（歷史台帳條目 2025-12-28｜台帳新增｜VERSION_AUDIT｜P2 Completeness／Banner Ledger 完）
---

## 歷史台帳條目｜2025-12-28｜台帳新增：P3 Canonical Bundle Ledger（稽核補登｜（歷史狀態記錄））

> 補充性質：台帳新增（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
> 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
> 目的：補登「PROJECT_PROMPT ACTIVE 補登」與「DOCUMENT_INDEX schema_version=3 Canonical Bundle」之 METADATA_FIX 條目，使 audit_anchor 可查，維持 累積式 稽核閉環。

---

### 20.3 台帳批次｜A｜METADATA_FIX Ledger（累積式）— Extension Batch 2025-12-28（P3-CANONICAL-BUNDLE）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|
| VA-METADATA_FIX-20251228-0039 | 2025-12-28 | BATCH-20251228-P3-CANONICAL-BUNDLE | DOCUMENT_INDEX | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__HISTORY_20251228L_FINAL.md` | 台帳新增｜schema_version=3 Canonical Bundle（單一可載入束：legacy 解析＋完整 mapping） |
| VA-METADATA_FIX-20251228-0040 | 2025-12-28 | BATCH-20251228-P3-CANONICAL-BUNDLE | DOCUMENT_INDEX | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__HISTORY_20251228L_FINAL.md` | 台帳新增｜PROJECT_PROMPT ACTIVE 補登（Authoritative Index Amendment，append-only） |
| VA-METADATA_FIX-20251228-0041 | 2025-12-28 | BATCH-20251228-P3-CANONICAL-BUNDLE | VERSION_AUDIT | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__HISTORY_20251228L_FINAL.md` | 台帳新增｜Ledger 補登（累積式） |

---

### 版本戳記｜2025-12-28 03:02:28 +0800（Asia/Taipei）
- generated_at: 2026-01-04 00:00:00 +0800（Asia/Taipei）

（歷史台帳條目 2025-12-28｜台帳新增｜VERSION_AUDIT｜P3 Canonical Bundle Ledger 完）
---

## 歷史台帳條目｜2025-12-28｜台帳新增：P4 Copy-Safe DocKey Ledger（稽核補登｜（歷史狀態記錄））

> 補充性質：台帳新增（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
> 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
> 目的：補登「DOCUMENT_INDEX Copy-Safe DocKey List」之 METADATA_FIX 條目，使 audit_anchor 可查，維持 累積式 稽核閉環。

---

### 20.4 台帳批次｜A｜METADATA_FIX Ledger（累積式）— Extension Batch 2025-12-28（P4-COPYSAFE）

| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|
| VA-METADATA_FIX-20251228-0042 | 2025-12-28 | BATCH-20251228-P4-COPYSAFE | DOCUMENT_INDEX | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__HISTORY_20251228M_FINAL.md` | 台帳新增｜Copy-Safe DocKey List（人因防呆：表格省略禁用＋完整鍵清單） |
| VA-METADATA_FIX-20251228-0043 | 2025-12-28 | BATCH-20251228-P4-COPYSAFE | VERSION_AUDIT | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__HISTORY_20251228M_FINAL.md` | 台帳新增｜Ledger 補登（累積式） |

---

### 版本戳記｜2025-12-28 03:09:05 +0800（Asia/Taipei）
- generated_at: 2026-01-04 00:00:00 +0800（Asia/Taipei）

（歷史台帳條目 2025-12-28｜台帳新增｜VERSION_AUDIT｜P4 Copy-Safe DocKey Ledger 完）
---

## 台帳批次 2025-12-28｜台帳新增：METADATA_FIX Ledger 條目範本（檔名映射 × doc_key Alias 對齊）（（歷史狀態記錄））

> 補充性質：台帳新增（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
> 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）  
> 目的：提供「可直接貼用」的稽核/回放條目格式，用於登錄本次類型之變更（檔名映射、doc_key alias、Evidence Chain 模板補齊）所需的最小欄位；不改寫既有 Ledger 制度。

### VA-MF-TEMPLATE. METADATA_FIX（範本）

```text
ledger_id: VA-METADATA_FIX-20251228-0001
change_type: METADATA_FIX
scope: Governance Metadata Alignment (Logical→Physical filename map; doc_key alias; evidence chain template anchor)
governance_state: （歷史狀態記錄）
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
notes: 台帳新增 appendices added; no semantic overwrite; canonical flow unchanged.
```
---

## 台帳批次 2025-12-28｜台帳新增：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（（歷史狀態記錄））

> 補充性質：台帳新增（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
> 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）  
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 歷史台帳條目/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`VERSION_AUDIT`
- 版本狀態：ACTIVE（（歷史狀態記錄）；台帳新增）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__HISTORY_20251228M_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=VERSION_AUDIT` + `canonical_filename=TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

## 歷史台帳條目｜2025-12-28｜台帳新增：METADATA_FIX Ledger 續增（0023–0025）｜（歷史狀態記錄）

> 補充性質：台帳新增（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__HISTORY_20251228M_FINAL.md（doc_key：VERSION_AUDIT）  
> 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX）  
> 目的：為本次「後稽核修補（Errata / Placeholder Norm）」補登 METADATA_FIX Ledger 條目；不改寫任何既有正文條款。

---

## A. METADATA_FIX Ledger（續增｜台帳新增）

> 本段為 台帳批次 A（METADATA_FIX Ledger）之續增；不回填、不改寫既有表格內容。

| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|
| VA-METADATA_FIX-20251228-0023 | 2025-12-28 | BATCH-20251228-POSTAUDIT-ERRATA | MASTER_CANON | Declare standalone line `...` as non-normative artifact (errata) | MASTER_CANON |
| VA-METADATA_FIX-20251228-0024 | 2025-12-28 | BATCH-20251228-POSTAUDIT-ERRATA | PROCESS_ANCHOR | Define and gate `VA-PLACEHOLDER-0001` usage; ACTIVE requires replacement by valid Ledger ID | PROCESS_ANCHOR |
| VA-METADATA_FIX-20251228-0025 | 2025-12-28 | BATCH-20251228-POSTAUDIT-ERRATA | VERSION_AUDIT | Ledger continuation appended (0023–0025) | VERSION_AUDIT |

## B. 最終宣告
- 本 歷史台帳條目 為 台帳新增；不改寫本文件任何既有條款。  
- 本 歷史台帳條目 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。

（歷史台帳條目 2025-12-28｜台帳新增｜（歷史狀態記錄） 完）

## 歷史台帳條目｜2025-12-31｜台帳新增：Bundle 251231 Physical Map × Hash Ledger 補登（（歷史狀態記錄））

> 補充性質：台帳新增（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
> 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）  
> 上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：將 2025-12-31（Bundle 251231）之「實體檔案映射（Physical Artifact Map）」與「sha256_12 hash ledger」以稽核條目形式補登，確保 repo 落盤檔案可被回放與追溯；本 歷史台帳條目 **不改寫**既有 Ledger/章節內容。

---

### 20.5 台帳批次｜A｜METADATA_FIX Ledger（累積式）— Extension Batch 2025-12-31（P0-PHYSICAL-ARTIFACT-MAP）

| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|
| VA-METADATA_FIX-20251231-0001 | 2025-12-31 | BATCH-20251231-P0-PHYSICAL-ARTIFACT-MAP | Physical Artifact Map × Hash Ledger（__251231 落盤對齊） | 將 repo 內 22 份實體檔（含 21 ACTIVE + 1 SUPPORT）以 mapping + sha256_12 補登；供 Gate/Loader/稽核回放使用。對應 DOCUMENT_INDEX｜歷史台帳條目 2025-12-31（N1–N4）。 | DOCUMENT_INDEX, VERSION_AUDIT |

---

### 20.6 台帳批次｜P0｜Bundle 251231｜Physical Artifact Hash Ledger（sha256_12）

| doc_key | status | canonical_filename（Index/引用） | physical_filename（本專案） | sha256_12 | source_alias（來源/舊檔名） |
|---|---|---|---|---|---|
| `README` | ACTIVE | `TAITS_專案總覽與使用說明（README）__251220.md` | `README__251231.md` | `11d42db1475e` | `TAITS_專案總覽與使用說明（README）__251220__HISTORY_20251227_FINAL.md` |
| `AI_GOV` | ACTIVE | `TAITS_AI_行為與決策治理最終規則全集__251217.md` | `TAITS_AI_行為與決策治理最終規則全集__251231.md` | `53354789820b` | `TAITS_AI_行為與決策治理最終規則全集__251217__HISTORY_20251228H_FINAL.md` |
| `GOVERNANCE_STATE_FREEZE_V1` | ACTIVE | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `443dbd4a27a4` | `—` |
| `PROJECT_PROMPT` | ACTIVE | `TAITS_PROJECT_PROMPT.md` | `TAITS_PROJECT_PROMPT__251231.md` | `c58e3fde8f97` | `TAITS_PROJECT_PROMPT__HISTORY_20251227_FINAL.md` |
| `TWSE_RULES` | ACTIVE | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md` | `3dfe33220600` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__HISTORY_20251227_FINAL.md` |
| `EXECUTION_CONTROL` | ACTIVE | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md` | `b6a3ede344e7` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__HISTORY_20251227_FINAL.md` |
| `UI_SPEC` | ACTIVE | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md` | `e60eb4446ae6` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ACTIVE_CLEAN_INLINE歷史參考_20251229.md` |
| `FULL_ARCH` | ACTIVE | `TAITS_全系統架構總覽（FULL_ARCH）__251219.md` | `TAITS_全系統架構總覽（FULL_ARCH）__251231.md` | `494d5b689e51` | `TAITS_全系統架構總覽（FULL_ARCH）__251219__HISTORY_20251227_FINAL.md` |
| `MASTER_CANON` | ACTIVE | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md` | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md` | `ecd9ce9c918b` | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ACTIVE_CLEAN_INLINE歷史參考_20251229.md` |
| `DOCUMENT_INDEX` | ACTIVE | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `d407ea013bc5` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md` |
| `BEGINNER_GUIDE` | ACTIVE | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md` | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md` | `2ea9efdfcc4c` | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__HISTORY_20251227_FINAL.md` |
| `LOCAL_ENV` | ACTIVE | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md` | `a7f23ecb108f` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` |
| `MASTER_ARCH` | ACTIVE | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md` | `0c0495f757da` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ACTIVE_CLEAN_INLINE歷史參考_20251229.md` |
| `GOVERNANCE_GATE_SPEC` | ACTIVE | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md` | `d3b7ab7fbaab` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__HISTORY_20251227_FINAL.md` |
| `VERSION_AUDIT` | ACTIVE | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `1f3dfb7b29e0` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__HISTORY_20251228M_FINAL__TOPBANNER_ONLYFREEZE__20251229.md` |
| `STRATEGY_UNIVERSE` | ACTIVE | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md` | `4b7f6c871f4f` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__HISTORY_20251227_FINAL.md` |
| `STRATEGY_FEATURE_INDEX` | ACTIVE | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md` | `01d564ba369e` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__HISTORY_20251227_FINAL.md` |
| `ARCH_FLOW` | ACTIVE | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md` | `d702e88c6000` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__HISTORY_20251227_FINAL.md` |
| `DATA_SOURCES` | ACTIVE | `TAITS_資料來源全集（DATA_SOURCES）__251219.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `0a197c01b6c8` | `TAITS_資料來源全集（DATA_SOURCES）__251219__HISTORY_0_2C_FINAL.md` |
| `DEPLOY_OPS` | ACTIVE | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md` | `4cee1444c6c3` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__HISTORY_20251228_FINAL.md` |
| `RISK_COMPLIANCE` | ACTIVE | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md` | `344cd3cb642d` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__HISTORY_20251227_FINAL.md` |
| `PROCESS_ANCHOR` | SUPPORT | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__HISTORY_20251228_ALLINONE_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `ee5ae3eb19bb` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__HISTORY_20251228_ALLINONE_FINAL.md` |

---

### 版本戳記｜2025-12-31 00:00:00 +0800（Asia/Taipei）
- generated_at: 2026-01-04 00:00:00 +0800（Asia/Taipei）
- ledger_ref: VA-METADATA_FIX-20251231-0001

（歷史台帳條目 2025-12-31｜台帳新增｜（歷史狀態記錄） 完）

## 歷史台帳條目｜2025-12-31｜台帳新增：P1｜Reference Alias Expansion 補登（（歷史狀態記錄））

> 補充性質：台帳新增（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
> 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）  
> 上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：補登 P1 之 legacy 引用解析（Reference Alias Expansion）事件，使 Gate/Loader/稽核回放在 （歷史狀態記錄） 期間可穩定解析舊檔名/工程路徑/舊 HISTORY/樣板引用。

---

### 20.7 台帳批次｜A｜METADATA_FIX Ledger（累積式）— Extension Batch 2025-12-31（P1-REFERENCE-ALIAS-EXPANSION）

| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|
| VA-METADATA_FIX-20251231-0002 | 2025-12-31 | BATCH-20251231-P1-REFERENCE-ALIAS-EXPANSION | Reference Alias Map（legacy refs → physical） | 補登 90 筆 legacy 引用檔名解析（含舊版版本戳、README.md、工程路徑、舊 HISTORY 檔名、樣板檔名）。對應 DOCUMENT_INDEX｜歷史台帳條目 2025-12-31｜P1（P1.1–P1.3）。 | DOCUMENT_INDEX, VERSION_AUDIT |

---

### 版本戳記｜2025-12-31 00:00:00 +0800（Asia/Taipei）（#2）
- generated_at: 2026-01-04 00:00:00 +0800（Asia/Taipei）
- ledger_ref: VA-METADATA_FIX-20251231-0002

（歷史台帳條目 2025-12-31｜台帳新增｜P1 完）

## 歷史台帳條目｜2025-12-31｜台帳新增：P1B｜Reference Alias Extension 補登（（歷史狀態記錄））

> 補充性質：台帳新增（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
> 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）  
> 上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：補登 P1B 之 Reference Alias Extension 事件，使 稽核檢核 v4 新發現之 legacy 引用（多為 HISTORY/inline歷史參考/工程路徑）可回放解析。

---

### 20.8 台帳批次｜A｜METADATA_FIX Ledger（累積式）— Extension Batch 2025-12-31（P1B-REFERENCE-ALIAS-EXTENSION）

| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|
| VA-METADATA_FIX-20251231-0003 | 2025-12-31 | BATCH-20251231-P1B-REFERENCE-ALIAS-EXTENSION | Reference Alias Extension（v4 補登） | 補登 21 筆 legacy 引用解析（多為 HISTORY/inline歷史參考/工程路徑）。對應 DOCUMENT_INDEX｜歷史台帳條目 2025-12-31｜P1B（P1B.1–P1B.3）。 | DOCUMENT_INDEX, VERSION_AUDIT |

---

### 版本戳記｜2025-12-31 00:00:00 +0800（Asia/Taipei）（#3）
- generated_at: 2026-01-04 00:00:00 +0800（Asia/Taipei）
- ledger_ref: VA-METADATA_FIX-20251231-0003

（歷史台帳條目 2025-12-31｜台帳新增｜P1B 完）

## 歷史台帳條目｜2025-12-31｜台帳新增：P1C｜Canonical Ref Alias Map 補登（（歷史狀態記錄））

> 補充性質：台帳新增（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
> 生效狀態：GOVERNANCE_STATE = （歷史狀態記錄）  
> 目的：補登 P1C（canonical 引用解析）事件，使 loader 在僅依 alias map 模式下亦能回放解析舊版 canonical 引用。

---

### 20.9 台帳批次｜A｜METADATA_FIX Ledger（累積式）— Extension Batch 2025-12-31（P1C-CANONICAL-REF-ALIAS）

| fix_id | date | batch_id | scope | note | touched_docs |
|---|---:|---|---|---|---|

---

### 版本戳記｜2025-12-31 00:00:00 +0800（Asia/Taipei）（#4）
- generated_at: 2026-01-04 00:00:00 +0800（Asia/Taipei）
- ledger_ref: VA-METADATA_FIX-20251231-0004

（歷史台帳條目 2025-12-31｜台帳新增｜P1C 完）

# 稽核區塊（Audit Section｜非正文）

> 本區塊為「本次融合更新」之留痕（Changelog／Hash Manifest／Scope／Audit Hand-off）。  
> 為避免新舊混讀：本區塊不參與正文裁決；正文以本檔案開頭至本區塊前之內容為準。

## A. Scope（適用範圍）
- scope_doc_key: VERSION_AUDIT
- scope_files_output: TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260104__單一正確正文版__最終覆蓋版__覆蓋輸出.md
- scope_files_source: TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260104__單一正確正文版__覆蓋版.md
- scope_mode: FILE UPDATE MODE（去混讀／章節去重／留痕分離／Final QA）
- version_date: 2026-01-04（Asia/Taipei）

## B. Changelog（變更清單）
1) **章節去重**：將散落重複之同名章節（如「版本戳記」「G0」「A/B/C/D」）整併為單一路徑或改名（保留內容、移除重複標題）。  
2) **去混讀修正**：將「歷史台帳條目」以中性標題承接；移除會造成新舊混讀之補丁式標記語句於正文。  
3) **稽核段落統一**：正文末端重複之稽核段落已移除，僅保留本檔尾「稽核區塊」作為唯一留痕入口。  
4) **版本一致化**：統一版本日期為 2026-01-04（Asia/Taipei）。

## E. 歷史留痕摘錄（由正文移入稽核區塊｜非正文）

> 下列內容為先前版本融合過程中產生之「生成戳記/補登表格」留痕，為避免新舊混讀，已自正文移入本稽核區塊保存。

```text
## 版本戳記（生成時間）
- generated_at: 2025-12-28 02:14:34 +0800（Asia/Taipei）

---

---
上位裁決：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
目的：補登本次 P0 全閉合更新之 fix_id，使 AI_GOV / GOVERNANCE_STATE_FREEZE_V1 / DOCUMENT_INDEX / VERSION_AUDIT 之 audit_anchor 可查，完成 累積式 稽核閉環。

---
| fix_id | date | batch_id | target_doc_key | output_artifact | change_type |
|---|---|---|---|---|---|

---
```


## C. Hash Manifest（指紋清單）
- hash_alg: sha256
- body_only:
  - scope: BODY_ONLY（不含本稽核區塊）
  - hash_value_sha256: 6cceefd39af037160400634d10ed8de9453222fa3d882a1e9bf4cc18286baad0
- full_excluding_hash_line:
  - scope: FULL_EXCLUDING(hash_value_sha256)（含稽核區塊；但不含實際 hash_value 行，以避免自指）
  - hash_value_sha256: 1a5bb35731510dc52e688eb53e6c4fa4c6d5fbd9866e40386e1b57920a1ccab0

## D. Audit Hand-off（裁決承接）
- change_id: VA-FIX-260104-0060
- authority_basis: HFI（人類最高決策者明確命令｜scope=VERSION_AUDIT｜Final QA）
- governance_order_applied: DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- notes:
  - 建議 ACTIVE 集合僅保留本最終覆蓋版；原檔 `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260104__單一正確正文版__覆蓋版.md` 封存以避免混讀。
