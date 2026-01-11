# TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）

## 文件頭（Document Header）
- doc_key：VERSION_AUDIT
- 治理等級：B（治理／制度級｜版本控管、稽核與可追溯治理規範）
- 基線日期：2026-01-10（Asia/Taipei）
- 版本日期：2026-01-10（Asia/Taipei）
- 適用範圍：TAITS 全系統（版本命名/封版/變更留痕/稽核資料結構/重現與回放/Hash Manifest/交付格式）
- 裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- 參照文件：GOVERNANCE_STATE／GOVERNANCE_GATE_SPEC／RISK_COMPLIANCE／EXECUTION_CONTROL／MASTER_CANON／UI_SPEC

## 0. 文件定位
- 所有版本/變更必須可被追溯（Traceable）、可被回放（Replayable）、可被審計（Auditable）、不可抵賴（Non-repudiable）。  
- 治理狀態（Freeze/Unfreeze）僅由 GOVERNANCE_STATE 宣告；任何文件內自述僅視為資訊，不得凌駕上位裁決。  
- 本文件不定義交易授權；交易授權與執行之權限邊界以 MASTER_CANON 定義，並受 RISK_COMPLIANCE 最高否決權約束。  

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
- 不定義風控否決條文（參見 RISK_COMPLIANCE）
- 不定義執行細節（參見 EXECUTION_CONTROL）
- 不改寫 Canonical Flow（參見 MASTER_CANON / ARCH_FLOW）
- 不定義 UI 外觀（參見 UI_SPEC）
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
- 串起一次完整 Canonical Flow（L1–全層稽核回放層）
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

- `docs_active_map`：doc_key 、 doc_version_id
- `policy_active_map`：policy_key 、 policy_version
- `rulebook_snapshot_id`
- `model_active_map`：model_id 、 model_version
- `config_active_map`：config_id 、 config_version
- `code_commit_ref`：git commit hash / tag（若有）

### 5.2 強制規則
- 任何 PASS / APPROVE / EXECUTE：
  - 必須綁定一份 Active Version Map
- 缺 Active Version Map：
  - 視為 SYS-VERSION-01 、 VETO / BLOCK

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
- **以 全層稽核回放層/回放作批准**：回放與記錄不構成批准；批准僅能由 人類裁決與交易授權層 人類裁決。

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
  例：`TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260108.md`

### 12.2 版本日期
- 一律使用台灣時區（Asia/Taipei）對應日期
- 本次版本：2026-01-10（__260108）

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
  E --> F[Run Flow (L1-全層稽核回放層)]
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


## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- FINAL_QA_NORMALIZE：正文正常化（去重收斂、去補丁/對話痕跡、移除標籤/助記定位；不改寫制度條文語義）。
- 更新：版本日期／基線日期統一為 2026-01-10（Asia/Taipei）。
- 固定：檔尾稽核四件套為唯一非正文留痕。

### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：815a4a7ab3f51f47435ae656a6ae97bb07745595dd9c73e32ac672fea8b9fad4
- LEGACY_AUDIT_SHA256：692b27da5eb70264e2c98b3f75433f5063e3d5b0edea2e61efdb022c73602684

### 3) 適用範圍（Scope）
- 本次變更僅針對 doc_key=VERSION_AUDIT 之文件正文進行正常化整理；不新增新制度、不改寫治理裁決序位之語義。

### 4) 裁決承接（Audit Hand-off）
- 裁決序位依 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV 承接。
- L1–L11 定義與層級說明以 MASTER_CANON 為唯一正文來源；本檔不重複分層定義。
