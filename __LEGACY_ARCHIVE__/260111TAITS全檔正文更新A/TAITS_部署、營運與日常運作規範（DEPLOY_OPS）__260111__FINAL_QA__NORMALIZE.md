# TAITS_部署、營運與日常運作規範（DEPLOY_OPS）

- doc_key：DEPLOY_OPS
- 治理位階：治理制度級（部署、營運與日常運作規範）
- 版本日期：2026-01-11（Asia/Taipei）
- 基線日期：2026-01-11（Asia/Taipei）
- 裁決序位（自高至低）：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
- Canonical Flow：doc_key=MASTER_CANON（L1–L11 定義之唯一正文來源）

---

## 0. 文件定位（Deployment & Operations）

本文件規範 TAITS 的部署（Deploy）、營運（Ops）、日常運作（Daily Run）之制度要求：
- 規範環境分層、發布節奏、監控告警、事故處理、回復演練與值班機制。
- 規範與 VERSION_AUDIT（稽核與可追溯）一致的變更/發布留痕格式，確保可回放、可稽核。
- 規範與 RISK_COMPLIANCE / EXECUTION_CONTROL 一致的風險控管與安全機制（Kill Switch／降級／風控保護）。
- 本文件不產生投資建議；僅定義部署與營運制度。

## 1. 全局約束與責任邊界（Hard Boundary）

- 上位裁決與治理約束一律依裁決序位：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV（自高至低）。
- Canonical Flow（L1–L11）之層級定義與語義一律以 doc_key=MASTER_CANON 為唯一正文來源；本文件不得另行重複定義層級語義。
- 部署/營運不得自行裁決 ACTIVE 文件集合、doc_key、治理位階或「最新版本」指向；如需裁決，一律依 DOCUMENT_INDEX 的 Authoritative Index。
- 本文件僅規範部署/營運制度與其產物之最小可稽核格式；不得被誤讀為策略、交易授權或執行指令。

## 2. 適用範圍（Hard Boundary）

1) 部署/營運產物（Release Note、Runbook、Incident、Log、回放包）之最小引用欄位  
2) Evidence Chain 格式對齊 LOCAL_ENV（不改流程，只固定輸出格式）  
3) Index Gate 唯一裁決來源（ACTIVE/doc_key/等級不由營運自行裁決）  
4) 裁決順序字串助記化定位（Mnemonic ≠ Override Rule）

- 不修改既有部署架構、環境策略、SOP 流程、權限模型  
- 不修改 Canonical Flow（L1–L11）  
- 不新增新治理層級  
- 不弱化 Risk/Compliance 否決權（若有張力，回到上位裁決與既有條款）


---


## 3. Index Gate 唯一裁決（營運不得自行裁決 ACTIVE/doc_key）

凡部署/營運流程涉及「依據文件」之裁決（例如：是否可上線、是否符合規範、是否可啟動某模組）：

- ACTIVE 文件集合、doc_key 合法性、治理位階 bucket、版本有效性  
  **一律以 DOCUMENT_INDEX 的 Authoritative Index 表格裁決為準**。  
- Runbook / Release Note / Incident 文檔中的「文件清單、文件數量、快捷載入集合」  
  一律視為 Snapshot（導覽用途），不得作為治理裁決依據。


---


## 4. 部署/營運產物最小引用欄位（Minimum Legal Citation Fields）

### 4.1 強制欄位（缺一視為未引用）
凡部署/營運產物中出現「依據某文件」或「符合某規範」之描述，必須至少包含：

- `ref_file`：完整檔名  
- `ref_doc_key`：doc_key  
- `ref_version_date`：版本日期（YYYY-MM-DD 或 __yymmdd）  
- `ref_section`：章節定位（heading path / §x.y）  
- `audit_anchor`：對應 VERSION_AUDIT 的稽核錨點（可先以本批次 `VA-METADATA_FIX-20251227-0012`）

缺任一欄位時， 一律視為「未引用」時， 不得作為上線/裁決依據；需要裁決時必須 STOP/RETURN 以補齊引用資訊。

### 4.2 建議固定引用標頭（可直接貼用）
```text
〔TAITS Deploy/Ops 引用標頭｜治理狀態（以 GOVERNANCE_STATE 為準）｜最大完備＋累積式更新〕
artifact_id = <release_id / incident_id / run_id>
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0012
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS Deploy/Ops 引用標頭〕
```


---


## 5. Evidence Chain 對齊 LOCAL_ENV（不改流程，只固定輸出格式）

為確保部署/營運產物可回放、可重現、可稽核，本文件後續所有「上線證據/回放包/事故復盤包」的輸出，必須至少包含下列結構（欄位可多不可少）：

### 5.1 環境指紋（Environment Fingerprint）
```text
env_fingerprint:
  os: <例如 Ubuntu 22.04>
  cpu: <型號/核心數>
  ram_gb: <數值>
  gpu: <可選>
  runtime: <例如 python 3.11 / node 20>
  package_manager: <pip/conda/uv/npm>
  repo_commit: <git hash>
  local_env_doc_ref:
    doc_key: LOCAL_ENV
    ref_section: <章節定位>
```

### 5.2 依賴清單（Dependency Manifest）
```text
dependency_manifest:
  lockfile: <requirements.txt / poetry.lock / uv.lock / package-lock.json 等>
  hash: <sha256 可選>
  generated_at: <ISO-8601>
```

### 5.3 執行證據（Run Evidence）
```text
run_evidence:
  command: <實際執行命令>
  start_time: <ISO-8601>
  end_time: <ISO-8601>
  outputs:
    - path: <產物路徑>
      hash: <sha256 可選>
  logs:
    - path: <log 路徑>
      hash: <sha256 可選>
```

### 5.4 失敗與回復（Failure/Recovery）
```text
failure_recovery:
  status: <PASS/FAIL>
  error_summary: <如 FAIL，摘要>
  recovery_action: <回滾/修復行動>
  notes: <可選>
```


---


## 6. 裁決序位字串之定位（助記 ≠ 覆蓋規則）

本文件內若出現任何「裁決順序字串」或箭頭序列（例如：`DOCUMENT_INDEX 時， MASTER_ARCH 時， MASTER_CANON`）：
- 一律視為閱讀/操作助記（Mnemonic）  
- 不得被用作覆蓋規則或裁決權重新分配  
- 若與 DOCUMENT_INDEX §3（覆蓋規則）或 §6（衝突裁決程序）產生張力：一律回到 DOCUMENT_INDEX（不可跳步）


---


## 7. 最終宣告（治理狀態以 GOVERNANCE_STATE 為準）

- 部署/營運產物的引用合法性必須滿足第 4 節之最小引用欄位；Evidence Chain 至少包含第 5 節之最小結構。  
- 缺少必要欄位時：依 DOCUMENT_INDEX §6 採保守處置，並以 VERSION_AUDIT 留痕。

## 8. Correlation Contract 與欄位貫穿規範

上位裁決：AI_GOV＋DOCUMENT_INDEX（Authoritative Index）＋MASTER_ARCH＋MASTER_CANON  
目的：在不改寫既有部署/營運流程的前提下，新增「Trace ID / Evidence Chain 欄位貫穿規範（Correlation Contract）」作為營運側硬性契約，使任一 Run/Release/Incident 均可跨 UI、Canonical Flow（L1–L11 產物）、Deploy/Ops 產物與稽核 Ledger 一鍵關聯、可回放、可追溯。


---


### 8.1 適用範圍（Hard Boundary）
本附錄僅規範「欄位命名、生成規則、貫穿/傳遞要求、最小關聯矩陣」：
- 不修改任何既有 SOP、流程步驟或責任分工  
- 不改寫 Canonical Flow（L1–L11）  
- 不新增新治理層級  
- 不變更 Risk/Compliance 最高否決權的裁決關係  

任何系統/人員可以新增更多欄位，但不得少於本附錄規定之最小欄位集。


---


### 8.2 核心概念（Why）

TAITS 的可回放與可稽核，依賴「同一個業務事件」能在所有產物中被定位與串接。  
因此：每一個 Run（一次完整或部分流程執行）必須有 **唯一的 run_id** 作為主鍵；每一個產物（artifact）必須能帶出 run_id 並可由 run_id 追到：
- DOCUMENT_INDEX 的法源（index_gate）  
- VERSION_AUDIT 的稽核錨點（audit_anchor）  
- Evidence Bundle / Replay Bundle 的路徑或指標（evidence_bundle_id / replay_bundle_id）  
- 環境指紋與依賴清單（env_fingerprint / dependency_manifest）


---


### 8.3 主要識別碼（Primary IDs）與定義

#### 8.3.1 run_id（主關聯鍵｜必填）
- 定義：一次工作執行單元（研究/回測/模擬/紙上/實盤）或一次營運流程執行單元（部署/回滾/事故演練）的唯一識別碼  
- 來源：由 Ops/Orchestrator 生成（或由最上游觸發器生成）；**不得在中途改寫**  
- 唯一性：全域唯一（建議 UUIDv7/ULID；格式由工程自定，但需一致）

#### 8.3.2 trace_id（鏈路追蹤鍵｜必填）
- 定義：細粒度追蹤（如單一步驟、單一 Gate、單一 API 呼叫）用識別碼  
- 規則：同一 run_id 可對應多個 trace_id；trace_id 必須能回溯到 run_id  
- 關係：`trace_id` 不可取代 `run_id`；run_id 為主鍵

#### 8.3.3 artifact_id（產物鍵｜必填）
- 定義：任何落盤產物（log、report、bundle、release note、runbook、incident report、model snapshot 等）的唯一識別碼  
- 規則：artifact_id 必須帶出 `run_id`（直接欄位或可解析欄位）

#### 8.3.4 evidence_bundle_id / replay_bundle_id（證據/回放鍵｜必填於對外裁決/執行）
- evidence_bundle_id：對應 Canonical Flow L5 的證據包主鍵  
- replay_bundle_id：對應稽核回放／營運產生的回放包主鍵（含 hash/manifest）


---


### 8.4 最小欄位集（Minimum Propagated Fields）

凡屬 Deploy/Ops 管轄之任何產物（見第 8.6 節之最小關聯矩陣）至少必須包含：

- `run_id`（必）  
- `trace_id`（必；若產物為聚合摘要，可填 `trace_id=AGGREGATE`，但仍必須有 run_id）  
- `artifact_id`（必）  
- `created_at`（必｜ISO-8601）  
- `actor`（必｜system/service/user）  
- `environment`（必｜prod/paper/sim/backtest/research 等，依你現有分類）  
- `index_gate_ref`（必｜指向 DOCUMENT_INDEX 的引用最小格式：ref_file/ref_doc_key/ref_version_date/ref_section）  
- `audit_anchor`（必｜VERSION_AUDIT:VA-METADATA_FIX-YYYYMMDD-XXXX 或同等可查錨點）  
- `evidence_bundle_id`（條件必｜若該產物與任何裁決性主張/策略提案/執行相關，則必填）  
- `replay_bundle_id`（條件必｜若該產物與任何執行/回放/事故復盤相關，則必填）  
- `env_fingerprint_ref`（條件必｜若可復現性要求適用，則必填；對齊 LOCAL_ENV/DEPLOY_OPS 既有 Evidence Chain）  
- `dependency_manifest_ref`（條件必｜同上）

以上欄位可用 JSON/YAML Header、log structured fields、或文件頂部固定標頭呈現；但不得以純自然語言隱含（必須可機器解析）。


---


### 8.5 生成與傳遞規則（Generation & Propagation Rules）

#### 8.5.1 生成規則（誰產生什麼）
1) run_id：由最上游觸發器/Orchestrator 產生一次，向下游傳遞，不可改寫  
2) trace_id：由各步驟/服務自行產生，但必須帶出 run_id  
3) artifact_id：每個落盤產物產生一次，不可重用；必須可關聯 run_id  
4) evidence_bundle_id：由 L5 產生（Evidence Bundle Assembly）  
5) replay_bundle_id：由稽核回放／營運回放包產生器生成（含 manifest/hash）

#### 8.5.2 傳遞規則（不可斷鏈）
- 任一產物若缺 run_id， 視為不可稽核產物，不得用於上線/裁決依據（RETURN/BLOCK，依 DOCUMENT_INDEX §6 保守處置）  
- 任一裁決性產物（Gate 結果、Risk/Compliance 結果、Human Decision、Execution Report）若缺 evidence_bundle_id， 視為證據鏈缺口  
- 任一執行/事故產物若缺 replay_bundle_id， 視為回放鏈缺口  
- 任一產物若缺 index_gate_ref 或 audit_anchor 時， 視為法源/稽核鏈缺口


---


### 8.6 最小關聯矩陣（Artifacts × Required Fields）

| 產物類型（Deploy/Ops） | run_id | trace_id | artifact_id | index_gate_ref | audit_anchor | evidence_bundle_id | replay_bundle_id | env_fingerprint_ref | dependency_manifest_ref |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Release Note（版本發佈說明） | 必 | 必(AGG可) | 必 | 必 | 必 | 條件必* | 條件必* | 條件必* | 條件必* |
| Runbook（操作手冊/作業指引） | 條件必** | 條件必** | 必 | 必 | 必 | 否 | 否 | 條件必 | 條件必 |
| Deployment Log（部署日誌） | 必 | 必 | 必 | 必 | 必 | 條件必 | 條件必 | 必 | 必 |
| Rollback Log（回滾日誌） | 必 | 必 | 必 | 必 | 必 | 條件必 | 條件必 | 必 | 必 |
| Incident Report（事故報告） | 必 | 必(AGG可) | 必 | 必 | 必 | 條件必 | 條件必 | 必 | 必 |
| Postmortem / RCA（根因分析） | 必 | 必(AGG可) | 必 | 必 | 必 | 條件必 | 條件必 | 必 | 必 |
| Replay Bundle Manifest（回放包清單） | 必 | 必 | 必 | 必 | 必 | 條件必 | 必 | 必 | 必 |

\* 條件必：若該 Release 與任何策略/裁決/執行產物綁定，必填 evidence_bundle_id / replay_bundle_id / env/deps ref。  
\** 條件必：若 Runbook 為某一特定 run/release/incident 的執行記錄或操作輸出載體，必填 run_id/trace_id；若為通用手冊則可不填 run_id，但仍必須有 index_gate_ref/audit_anchor。


---


### 8.7 可直接貼用的「結構化標頭」模板

#### 8.7.1 Deploy/Ops 文檔標頭（YAML）
```yaml
taits_ops_header:
  run_id: "<uuid/ulid>"
  trace_id: "<uuid/ulid or AGGREGATE>"
  artifact_id: "<uuid/ulid>"
  created_at: "<ISO-8601>"
  actor: "<system/service/user>"
  environment: "<research/backtest/sim/paper/live/prod>"
  index_gate_ref:
    ref_file: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260111.md"
    ref_doc_key: "DOCUMENT_INDEX"
    ref_version_date: "__260111"
  audit_anchor: "VERSION_AUDIT:VA-METADATA_FIX-20251227-0020"
  evidence_bundle_id: "<optional-but-required-when-decisionary>"
  replay_bundle_id: "<optional-but-required-when-executionary>"
  env_fingerprint_ref: "<path or id aligned with LOCAL_ENV>"
  dependency_manifest_ref: "<path or id aligned with LOCAL_ENV>"
```

#### 8.7.2 Structured Log Fields（JSON）
```json
{
  "run_id": "<uuid/ulid>",
  "trace_id": "<uuid/ulid>",
  "artifact_id": "<uuid/ulid>",
  "created_at": "<ISO-8601>",
  "actor": "<system/service/user>",
  "environment": "<...>",
  "index_gate_ref": {
    "ref_doc_key": "DOCUMENT_INDEX",
    "ref_version_date": "__260111",
    "ref_section": "<...>"
  },
  "audit_anchor": "VERSION_AUDIT:VA-METADATA_FIX-20251227-0020",
  "evidence_bundle_id": "<...>",
  "replay_bundle_id": "<...>"
}
```


---


### 8.8 驗證與保守處置（Ops Enforcement）

- Deploy/Ops 任何上線/回滾/事故復盤流程若偵測到第 8.4 節最小欄位集缺口：  
  - 依 DOCUMENT_INDEX §6 走保守處置（RETURN/BLOCK）  
  - 必須將缺口寫入 Incident 或 Run Evidence，並補登 VERSION_AUDIT（append-only）  
- 任何「缺 run_id 的產物」視為不可用產物：不得作為裁決依據，亦不得作為回放包的一部分。


---


## 9. Repo 落盤與封存規範

上位裁決：AI_GOV＋DOCUMENT_INDEX（Authoritative Index）＋MASTER_ARCH＋MASTER_CANON  
目的：在 治理狀態（以 GOVERNANCE_STATE 為準） 下，新增「Repo 落盤/封存」的營運規範（不改任何治理裁決），以降低同一 doc_key 多版本並存造成的“選錯檔”風險，並確保工具鏈與人工載入的 latest 行為一致、可回放、可稽核。


---


### 9.1 適用範圍與硬邊界（Hard Boundary）

- 不改寫 DOCUMENT_INDEX 之 Authoritative Index 表格內容與裁決效力  
- 不變更 ACTIVE/doc_key/治理位階/覆蓋規則/衝突裁決程序  
- 不修改 Canonical Flow（L1–L11）  
- 不變更 Risk/Compliance 最高否決權

核心原則：**Index Gate First**。任何“最新版本”指向，法律裁決仍以 DOCUMENT_INDEX 為準；本規範僅降低操作錯誤率。


---


### 9.2 目錄約定（Repository Landing Convention）

在 repo 根目錄（或 `docs/`）新增/採用以下目錄（名稱固定）：

- `LATEST/`：操作層「最新版本」匯總目錄（convenience layer）  
- `ARCHIVE/`：封存目錄（歷史版本，不作預設載入）  
- `RELEASES/`（可選）：每次批次/發佈的集合包（含 manifest）  

#### 9.2.1 LATEST 的角色（Convenience, Not Authority）
- `LATEST/` 只提供「**快速載入入口**」  
- 不得宣稱其具有裁決效力  
- 工具鏈仍必須以 DOCUMENT_INDEX 的 Authoritative Index + latest mapping（machine-readable）為裁決依據

#### 9.2.2 ARCHIVE 的角色（Immutable History）
- 歷史檔案不得被覆寫；如需修正，一律新增新版本並封存舊版本（append-only）


---


### 9.3 檔案命名與版本策略（Naming & Versioning Rules）

#### 9.3.1 doc_key 對齊（必須）
- 檔名可讀且可回推 doc_key（或在檔頭 metadata 明示 doc_key）  
- version_date 可由檔名或 metadata 取得（`__yymmdd` 或 `YYYY-MM-DD` 等）  

#### 9.3.2 “最新版本”形成原則（Latest Formation）
同一 doc_key 若有多個版本並存：
- **法律裁決**：以 DOCUMENT_INDEX 表格為準  
- **操作載入**：以 DOCUMENT_INDEX 的 latest mapping（machine-readable）為準  
- **便捷入口**：`LATEST/` 內僅保留該 doc_key 的一份 latest 檔（或以連結/副本形式）

注意：`LATEST/` 不得私自指向未被 DOCUMENT_INDEX mapping 指認的檔名。


---


### 9.4 落盤作業流程（Operational Procedure）

---

1) 產出文件檔案（可覆寫修正（但禁止摘要縮水；且必留痕承接）歷史版本；若覆寫同檔名，必須可證明為 append-only 且有稽核留痕）  
2) 更新 DOCUMENT_INDEX latest mapping（若檔名更動或 latest 指向更動）  
3) 更新 VERSION_AUDIT｜METADATA_FIX Ledger：  
   - 新增 `fix_id` 條目（append-only）  
   - 指向 output_artifact 檔名  
4) 更新 `LATEST/`：將該 doc_key 的 latest 檔放入或更新連結  
5) 將被替換者移入 `ARCHIVE/`（保留原檔名與原內容，可覆寫修正（但禁止摘要縮水；且必留痕承接））

#### 9.4.2 封存規則（ARCHIVE Policy）
- 封存時推薦以日期分層：`ARCHIVE/YYYYMMDD/<doc_key>/<file>`  
- 封存檔案不得再被工具鏈當作預設載入；工具鏈只讀 `LATEST/` 或 mapping 指向


---


### 9.5 防呆與保守處置（Ops Guardrails）

#### 9.5.1 選錯檔的判定（Selection Error）
若發現任何以下情況，視為「選檔錯誤」：
- 工具鏈/人工載入的檔名與 DOCUMENT_INDEX latest mapping 不一致  
- 使用未在 DOCUMENT_INDEX 表格中列為 ACTIVE 的文件作裁決依據  
- 缺失引用最小欄位（ref_file/ref_doc_key/ref_version_date/ref_section/audit_anchor）而仍作裁決性輸出

#### 9.5.2 保守處置（Conservative Handling）
一律採保守策略（RETURN/BLOCK，依 DOCUMENT_INDEX §6）：
- 停止推進（不得以“猜測”補齊）  
- 生成 Incident/Run Evidence，記錄錯誤載入之檔名與 run_id  
- 補登 VERSION_AUDIT（append-only），留存修正痕跡


---


### 9.6 可直接貼用：落盤 Manifest（YAML）

```yaml
taits_repo_landing_manifest:
  landing_date: "2025-12-28"
  governance_state: "治理狀態（以 GOVERNANCE_STATE 為準）"
  doc_key: "<DOC_KEY>"
  latest_artifact: "<filename>"
  archive_policy:
    archive_root: "ARCHIVE/"
    archive_partition: "ARCHIVE/YYYYMMDD/<doc_key>/"
    immutable: true
  latest_policy:
    latest_root: "LATEST/"
    one_file_per_doc_key: true
    authority_note: "LATEST is convenience only; Index Gate remains DOCUMENT_INDEX."
  audit:
    audit_anchor: "VERSION_AUDIT:VA-METADATA_FIX-20251227-0024"
    required_min_citation_fields:
      - ref_file
      - ref_doc_key
      - ref_version_date
      - ref_section
      - audit_anchor
```


---

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- FINAL_QA：移除正文中夾帶之「舊版英文標頭＋整段重複正文」區塊（避免同檔雙正文混讀）。
- FINAL_QA：移除正文中「歷史完成標記／Legacy 版本字樣」（例如舊版完成括註），避免被誤判為正文。
- FINAL_QA：去除正文章節之標籤化前綴（原附錄/內部助記碼），改為一致之章節編號與交叉引用，不變更條文語義。
- FINAL_QA：合併重複之「治理補強」章節，收斂為兩大主題：① Correlation Contract 與欄位貫穿規範；② Repo 落盤與封存規範。
- FINAL_QA：修正正文中不一致之占位/重複字樣為可讀且一致之用語，不改寫治理邊界。
- 保留：部署／營運制度正文最大完備承接（不做摘要縮水）；僅進行去重收斂、結構重排、標題修復與格式一致化。

### 2) 指紋清單（Hash Manifest）
- HASH_RULE：SHA-256（UTF-8，LF；Body=本檔「稽核區塊」之前全文，含結尾換行）
- BODY_SHA256：9862bc7029836663d5a572912cd9ce6ef6cdbd7255b59a58d959972d5008bb2f

### 3) 適用範圍（Scope）
- scope_doc_key：DEPLOY_OPS
- scope_change_type：FINAL_QA_NORMALIZE（正文乾淨／去重收斂／結構重排／去標籤化／格式修復）
- scope_invariants：
  - 不改寫上位裁決序位：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV（自高至低）
  - 不新增或重複定義 Canonical Flow（L1–L11）；其唯一正文來源維持 doc_key=MASTER_CANON
  - 不新增投資／策略／交易決策內容；不越權至 RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC

### 4) Audit Hand-off（裁決承接）
- governance_order_applied：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV（自高至低）
- canonical_flow_anchor：MASTER_CANON（L1–L11）
- note：本檔正文為可直接覆蓋之最大完備版；稽核區塊屬非正文。