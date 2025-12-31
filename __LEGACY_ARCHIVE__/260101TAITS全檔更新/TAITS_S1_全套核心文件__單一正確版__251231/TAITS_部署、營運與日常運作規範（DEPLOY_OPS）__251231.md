---

# 補強規範
---

## D0. 適用範圍（Hard Boundary）

本 整合段落 僅補強：
1) 部署/營運產物（Release Note、Runbook、Incident、Log、回放包）之最小引用欄位  
2) Evidence Chain 格式對齊 LOCAL_ENV（不改流程，只固定輸出格式）  
3) Index Gate 唯一裁決來源（ACTIVE/doc_key/等級不由營運自行裁決）  
4) 裁決順序字串助記化定位（Mnemonic ≠ Override Rule）

本 整合段落 **不**：
- 不修改既有部署架構、環境策略、SOP 流程、權限模型  
- 不修改 Canonical Flow（L1–L11）  
- 不新增新治理層級  
- 不弱化 Risk/Compliance 否決權（若有張力，回到上位裁決與既有條款）

---

## D1. Index Gate 唯一裁決（營運不得自行裁決 ACTIVE/doc_key）

凡部署/營運流程涉及「依據文件」之裁決（例如：是否可上線、是否符合規範、是否可啟動某模組）：

- ACTIVE 文件集合、doc_key 合法性、治理等級 bucket、版本有效性  
  **一律以 DOCUMENT_INDEX 的 Authoritative Index 表格裁決為準**。  
- Runbook / Release Note / Incident 文檔中的「文件清單、文件數量、快捷載入集合」  
  一律視為 Snapshot（導覽用途），不得作為治理裁決依據。

---

## D2. 部署/營運產物最小引用欄位（Minimum Legal Citation Fields）

### D2.1 強制欄位（缺一視為未引用）
凡部署/營運產物中出現「依據某文件」或「符合某規範」之描述，必須至少包含：

- `ref_file`：完整檔名  
- `ref_doc_key`：doc_key  
- `ref_version_date`：版本日期（YYYY-MM-DD 或 __yymmdd）  
- `ref_section`：章節定位（heading path / §x.y）  
- `audit_anchor`：對應 VERSION_AUDIT 的稽核錨點（可先以本批次 `VA-METADATA_FIX-20251227-0012`）

缺任一欄位 → 一律視為「未引用」→ 不得作為上線/裁決依據；需要裁決時必須 STOP/RETURN 以補齊引用資訊。

### D2.2 建議固定引用標頭（可直接貼用）
```text
〔TAITS Deploy/Ops 引用標頭｜Freeze v1.0｜Only-Add〕
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

## D3. Evidence Chain 對齊 LOCAL_ENV（不改流程，只固定輸出格式）

為確保部署/營運產物可回放、可重現、可稽核，本文件後續所有「上線證據/回放包/事故復盤包」的輸出，必須至少包含下列結構（欄位可多不可少）：

### D3.1 環境指紋（Environment Fingerprint）
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

### D3.2 依賴清單（Dependency Manifest）
```text
dependency_manifest:
  lockfile: <requirements.txt / poetry.lock / uv.lock / package-lock.json 等>
  hash: <sha256 可選>
  generated_at: <ISO-8601>
```

### D3.3 執行證據（Run Evidence）
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

### D3.4 失敗與回復（Failure/Recovery）
```text
failure_recovery:
  status: <PASS/FAIL>
  error_summary: <如 FAIL，摘要>
  recovery_action: <回滾/修復行動>
  notes: <可選>
```

---

## D4. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）

本文件內若出現任何「裁決順序字串」或箭頭序列（例如：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`）：
- 一律視為閱讀/操作助記（Mnemonic）  
- 不得被用作覆蓋規則或裁決權重新分配  
- 若與 DOCUMENT_INDEX §3（覆蓋規則）或 §6（衝突裁決程序）產生張力：一律回到 DOCUMENT_INDEX（不可跳步）

---

## D5. 最終宣告（Freeze v1.0）

- 本 整合段落 為 Only-Add；不改寫任何既有部署/營運流程。  
- 部署/營運產物的引用合法性必須滿足 D2 最小欄位；Evidence Chain 至少包含 D3 結構。  
- 缺少必要欄位時：依 DOCUMENT_INDEX §6 保守處置，並以 VERSION_AUDIT 留痕。
# 📘 TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231

Deployment, Operations & Daily Governance Specification

doc_key：DEPLOY_OPS
治理等級：B（Deployment & Operations Governance｜執行前置治理，不具策略與裁決權）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（部署與營運層最大完備版，僅允許 Only-Add）
P25-12-31
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251231（A+）
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX
平行參照：ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / LOCAL_ENV
變更原則：Only-Add（只可新增，不可刪減／覆寫／弱化治理邊界）

0. 文件定位（Deployment & Operations Charter）

本文件為 TAITS 在「可運行狀態」下的部署與日常營運治理母文件，
其存在目的僅有一個：

確保系統「可以被安全地啟動、持續運行、即時中止、完整追責」。

本文件負責

定義 系統上線前必須通過的部署與營運治理條件

定義 環境切換、版本啟用、凍結、回滾與停線流程

定義 日常營運、異常事件、事故處理的標準治理語義

本文件不負責（避免越權）

不定義策略與交易邏輯（→ STRATEGY_UNIVERSE）

不定義風控否決條文（→ RISK_COMPLIANCE）

不定義下單與執行細節（→ EXECUTION_CONTROL）

不定義 UI 行為與互動（→ UI_SPEC）

不裁決文件位階與衝突（→ DOCUMENT_INDEX）

1. 環境治理分級（Environment Governance）
1.1 官方環境類型（不可自行新增語義）
環境	定位	是否允許實際下單
Research	研究／設計	否
Backtest	歷史回測	否
Simulation	即時模擬	否
Paper	擬真紙交易	否
Live	真實運行	是

📌 任何新環境僅能以 Only-Add 方式新增，不得改寫既有語義。

1.2 環境切換鐵律

環境切換 ≠ 模式切換

環境切換必須：

重新檢查版本鎖定

重新檢查風控 Gate

重新檢查 Kill Switch 可用性

2. 上線前治理門檻（Pre-Deployment Gates）
2.1 進入 Live / Paper 的必要條件（缺一不可）

DOCUMENT_INDEX 可用且未被 Freeze

MASTER_ARCH / MASTER_CANON 版本鎖定

ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL 版本一致

VERSION_AUDIT 已建立可回放帳本

Kill Switch 通過 Preflight 自檢

Execution Channel Health = OK

無未解決 Critical / Major Incident

📌 任一條件未滿足 → 不得啟動系統。

2.2 Preflight Check（硬性）

Preflight 必須可審計，且包含：

檔案版本快照

環境參數快照

Kill Switch 測試結果

通道健康檢查結果

3. 部署流程語義（Deployment Lifecycle）
3.1 標準部署狀態機
BUILD → VALIDATE → STAGE → ACTIVATE → MONITOR

BUILD：產出可部署單元

VALIDATE：治理與版本驗證

STAGE：非生效狀態部署

ACTIVATE：版本正式生效

MONITOR：持續監控

📌 未經 VALIDATE 不得 ACTIVATE。

3.2 啟用（Activate）限制

Activate 僅允許：

已通過治理門檻的版本

已記錄於 VERSION_AUDIT

禁止：

熱修補未留痕

臨時覆寫版本

4. 版本治理與回滾（Rollback Governance）
4.1 回滾的治理定位

回滾是 治理行為，不是技術補救

回滾必須：

明確指定目標版本

留存回滾原因與裁決依據

不破壞既有審計與回放

4.2 回滾觸發條件（示例）

Execution 不一致

Risk Gate 行為異常

嚴重系統錯誤

合規事件

5. 停線與凍結（Stop-the-Line & Freeze）
5.1 停線（Stop-the-Line）

任何 Critical 事件可觸發

停線後：

禁止新交易

保留查詢與審計

等待治理裁決

5.2 凍結（Freeze）

Freeze 期間：

禁止文件結構性變更

僅允許事故修復

Freeze 來源：

RISK_COMPLIANCE

DEPLOY_OPS

DOCUMENT_INDEX 裁決

6. 日常營運規範（Daily Operations）
6.1 每日啟動檢查（Daily Start Checklist）

系統時間同步

通道健康

Kill Switch READY

版本一致性

無未解 Incident

6.2 每日結束檢查（Daily Close Checklist）

對帳完成

審計物寫入完成

異常事件歸檔

狀態快照封存

7. 事件與事故治理（Incident Governance）
7.1 Incident 分級
等級	定義
P0	立即威脅系統／資產
P1	嚴重功能失效
P2	可運行但異常
P3	觀測與改善項
7.2 Incident 必備欄位

incident_id

發生時間

影響範圍

當下版本

採取動作

是否觸發停線 / 凍結

8. Secrets / Key 與敏感設定治理

金鑰不得硬寫於程式碼

必須具備：

權限分級

定期輪替

存取審計

洩漏風險 → 視為 Critical Incident

9. 與其他文件的邊界對齊
文件	DEPLOY_OPS 關係
MASTER_ARCH	服從
MASTER_CANON	服從
ARCH_FLOW	對齊
RISK_COMPLIANCE	觸發與回應
EXECUTION_CONTROL	啟用與停用
UI_SPEC	呈現狀態
VERSION_AUDIT	版本帳本
10. 演進規則（Only-Add）

允許新增：

新環境類型

新 Incident 類型

新 Runbook

禁止：

改寫既有環境語義

弱化上線門檻

省略治理檢查

最終治理宣告（不可改寫）

系統能否運作，
不取決於它有多聰明，
而取決於它是否能被隨時安全地停下來。

（DEPLOY_OPS｜最大完備版 v2025-12-19 完）

---

# 補強規範
---

## 補強規範

### T0. 適用範圍（Hard Boundary）
本附錄僅規範「欄位命名、生成規則、貫穿/傳遞要求、最小關聯矩陣」：
- 不修改任何既有 SOP、流程步驟或責任分工  
- 不改寫 Canonical Flow（L1–L11）  
- 不新增新治理層級  
- 不變更 Risk/Compliance 最高否決權的裁決關係  
---

## T1. 核心概念（Why）
TAITS 的可回放與可稽核，依賴「同一個業務事件」能在所有產物中被定位與串接。  
因此：每一個 Run（一次完整或部分流程執行）必須有 **唯一的 run_id** 作為主鍵；每一個產物（artifact）必須能帶出 run_id 並可由 run_id 追到：
- DOCUMENT_INDEX 的法源（index_gate）  
- VERSION_AUDIT 的稽核錨點（audit_anchor）  
- Evidence Bundle / Replay Bundle 的路徑或指標（evidence_bundle_id / replay_bundle_id）  
- 環境指紋與依賴清單（env_fingerprint / dependency_manifest）

---

## T2. 主要識別碼（Primary IDs）與定義

### T2.1 run_id（主關聯鍵｜必填）
- 定義：一次工作執行單元（研究/回測/模擬/紙上/實盤）或一次營運流程執行單元（部署/回滾/事故演練）的唯一識別碼  
- 來源：由 Ops/Orchestrator 生成（或由最上游觸發器生成）；**不得在中途改寫**  
- 唯一性：全域唯一（建議 UUIDv7/ULID；格式由工程自定，但需一致）

### T2.2 trace_id（鏈路追蹤鍵｜必填）
- 定義：細粒度追蹤（如單一步驟、單一 Gate、單一 API 呼叫）用識別碼  
- 規則：同一 run_id 可對應多個 trace_id；trace_id 必須能回溯到 run_id  
- 關係：`trace_id` 不可取代 `run_id`；run_id 為主鍵

### T2.3 artifact_id（產物鍵｜必填）
- 定義：任何落盤產物（log、report、bundle、release note、runbook、incident report、model snapshot 等）的唯一識別碼  
- 規則：artifact_id 必須帶出 `run_id`（直接欄位或可解析欄位）

### T2.4 evidence_bundle_id / replay_bundle_id（證據/回放鍵｜必填於對外裁決/執行）
- evidence_bundle_id：對應 Canonical Flow L5 的證據包主鍵  
- replay_bundle_id：對應 L11 / Ops 產生的回放包主鍵（含 hash/manifest）

---

## T3. 最小欄位集（Minimum Propagated Fields）

凡屬 Deploy/Ops 管轄之任何產物（見 T5 矩陣）至少必須包含：

- `run_id`（必）  
- `trace_id`（必；若產物為聚合摘要，可填 `trace_id=AGGREGATE`，但仍必須有 run_id）  
- `artifact_id`（必）  
- `created_at`（必｜ISO-8601）  
- `actor`（必｜system/service/user）  
- `environment`（必｜prod/paper/sim/backtest/research 等，依你現有分類）  
- `index_gate_ref`（必｜指向 DOCUMENT_INDEX 的引用最小格式：ref_file/ref_doc_key/ref_version_date/ref_section）  
- `audit_anchor`（必｜VERSION_AUDIT:VA-METADATA_FIX-... 或同等可查錨點）  
- `evidence_bundle_id`（條件必｜若該產物與任何裁決性主張/策略提案/執行相關，則必填）  
- `replay_bundle_id`（條件必｜若該產物與任何執行/回放/事故復盤相關，則必填）  
- `env_fingerprint_ref`（條件必｜若可復現性要求適用，則必填；對齊 LOCAL_ENV/DEPLOY_OPS 既有 Evidence Chain）  
- `dependency_manifest_ref`（條件必｜同上）
---

## T4. 生成與傳遞規則（Generation & Propagation Rules）

### T4.1 生成規則（誰產生什麼）
1) run_id：由最上游觸發器/Orchestrator 產生一次，向下游傳遞，不可改寫  
2) trace_id：由各步驟/服務自行產生，但必須帶出 run_id  
3) artifact_id：每個落盤產物產生一次，不可重用；必須可關聯 run_id  
4) evidence_bundle_id：由 L5 產生（Evidence Bundle Assembly）  
5) replay_bundle_id：由 L11 或 Ops 回放包產生器生成（含 manifest/hash）

### T4.2 傳遞規則（不可斷鏈）
- 任一產物若缺 run_id → 視為不可稽核產物，不得用於上線/裁決依據（RETURN/BLOCK，依 DOCUMENT_INDEX §6 保守處置）  
- 任一裁決性產物（Gate 結果、Risk/Compliance 結果、Human Decision、Execution Report）若缺 evidence_bundle_id → 視為證據鏈缺口  
- 任一執行/事故產物若缺 replay_bundle_id → 視為回放鏈缺口  
- 任一產物若缺 index_gate_ref 或 audit_anchor → 視為法源/稽核鏈缺口

---

## T5. 最小關聯矩陣（Artifacts × Required Fields）

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

## T6. 可直接貼用的「結構化標頭」模板

### T6.1 Deploy/Ops 文檔標頭（YAML）
```yaml
taits_ops_header:
  run_id: "<uuid/ulid>"
  trace_id: "<uuid/ulid or AGGREGATE>"
  artifact_id: "<uuid/ulid>"
  created_at: "<ISO-8601>"
  actor: "<system/service/user>"
  environment: "<research/backtest/sim/paper/live/prod>"
  index_gate_ref:
    ref_file: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
    ref_doc_key: "DOCUMENT_INDEX"
    ref_version_date: "__251231"
    ref_section: "<Authoritative Index / 整合段落 映射表章節>"
  audit_anchor: "VERSION_AUDIT:VA-METADATA_FIX-20251227-0020"
  evidence_bundle_id: "<optional-but-required-when-decisionary>"
  replay_bundle_id: "<optional-but-required-when-executionary>"
  env_fingerprint_ref: "<path or id aligned with LOCAL_ENV>"
  dependency_manifest_ref: "<path or id aligned with LOCAL_ENV>"
```

### T6.2 Structured Log Fields（JSON）
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
    "ref_version_date": "__251231",
    "ref_section": "<...>"
  },
  "audit_anchor": "VERSION_AUDIT:VA-METADATA_FIX-20251227-0020",
  "evidence_bundle_id": "<...>",
  "replay_bundle_id": "<...>"
}
```

---

## T7. 驗證與保守處置（Ops Enforcement）

- Deploy/Ops 任何上線/回滾/事故復盤流程若偵測到 T3 最小欄位缺口：  
  - 依 DOCUMENT_INDEX §6 走保守處置（RETURN/BLOCK）  
  - 必須將缺口寫入 Incident 或 Run Evidence，並補登 VERSION_AUDIT（append-only）  
- 任何「缺 run_id 的產物」視為不可用產物：不得作為裁決依據，亦不得作為回放包的一部分。

---
---

# 補強規範
---

## B1. 適用範圍與硬邊界（Hard Boundary）

本 整合段落 僅規範「檔案落盤與封存」的**營運操作**：
- 不改寫 DOCUMENT_INDEX 之 Authoritative Index 表格內容與裁決效力  
- 不變更 ACTIVE/doc_key/治理等級/覆蓋規則/衝突裁決程序  
- 不修改 Canonical Flow（L1–L11）  
- 不變更 Risk/Compliance 最高否決權
---

## B2. 目錄約定（Repository Landing Convention）

在 repo 根目錄（或 `docs/`）新增/採用以下目錄（名稱固定）：

- `LATEST/`：操作層「最新版本」匯總目錄（convenience layer）  
- `ARCHIVE/`：封存目錄（歷史版本，不作預設載入）  
- `RELEASES/`（可選）：每次批次/發佈的集合包（含 manifest）  

### B2.1 LATEST 的角色（Convenience, Not Authority）
- `LATEST/` 只提供「**快速載入入口**」  
- 不得宣稱其具有裁決效力  
- 工具鏈仍必須以 DOCUMENT_INDEX 的 Authoritative Index + latest mapping（machine-readable）為裁決依據

### B2.2 ARCHIVE 的角色（Immutable History）
- `ARCHIVE/` 用於保留舊版檔案、舊 addendum、歷史快照  
- 歷史檔案不得被覆寫；如需修正，一律新增新版本並封存舊版本（append-only）

---

## B3. 檔案命名與版本策略（Naming & Versioning Rules）

### B3.1 doc_key 對齊（必須）
每份治理文件或其 addendum 落盤時，必須滿足：
- 檔名可讀且可回推 doc_key（或在檔頭 metadata 明示 doc_key）  
- version_date 可由檔名或 metadata 取得（`__yymmdd` 或 `YYYY-MM-DD` 等）  
- Only-Add 增補檔需明確標註 addendum id / date

### B3.2 “最新版本”形成原則（Latest Formation）
同一 doc_key 若有多個版本並存：
- **法律裁決**：以 DOCUMENT_INDEX 表格為準  
- **操作載入**：以 DOCUMENT_INDEX 的 latest mapping（machine-readable）為準  
- **便捷入口**：`LATEST/` 內僅保留該 doc_key 的一份 latest 檔（或以連結/副本形式）
---

## B4. 落盤作業流程（Operational Procedure）

### B4.1 新版產物落盤（新增/更新 addendum）
當產出新 addendum（Freeze v1.0 下必為 Only-Add）時：

1) 產出文件檔案（不可覆寫歷史版本；若覆寫同檔名，必須可證明為 append-only 且有稽核留痕）  
2) 更新 DOCUMENT_INDEX latest mapping（若檔名更動或 latest 指向更動）  
3) 更新 VERSION_AUDIT｜METADATA_FIX Ledger：  
   - 新增 `fix_id` 條目（append-only）  
   - 指向 output_artifact 檔名  
4) 更新 `LATEST/`：將該 doc_key 的 latest 檔放入或更新連結  
5) 將被替換者移入 `ARCHIVE/`（保留原檔名與原內容，不得覆寫）

### B4.2 封存規則（ARCHIVE Policy）
- 封存時推薦以日期分層：`ARCHIVE/YYYYMMDD/<doc_key>/...`  
- 封存檔案不得再被工具鏈當作預設載入；工具鏈只讀 `LATEST/` 或 mapping 指向

---

## B5. 防呆與保守處置（Ops Guardrails）

### B5.1 選錯檔的判定（Selection Error）
若發現任何以下情況，視為「選檔錯誤」：
- 工具鏈/人工載入的檔名與 DOCUMENT_INDEX latest mapping 不一致  
- 使用未在 DOCUMENT_INDEX 表格中列為 ACTIVE 的文件作裁決依據  
- 缺失引用最小欄位（ref_file/ref_doc_key/ref_version_date/ref_section/audit_anchor）而仍作裁決性輸出

### B5.2 保守處置（Conservative Handling）
一律採保守策略（RETURN/BLOCK，依 DOCUMENT_INDEX §6）：
- 停止推進（不得以“猜測”補齊）  
- 生成 Incident/Run Evidence，記錄錯誤載入之檔名與 run_id  
- 補登 VERSION_AUDIT（append-only），留存修正痕跡

---

## B6. 可直接貼用：落盤 Manifest（YAML）

```yaml
taits_repo_landing_manifest:
  landing_date: "2025-12-28"
  governance_state: "Freeze v1.0"
  doc_key: "<DOC_KEY>"
  latest_artifact: "<filename>"
  latest_mapping_source: "DOCUMENT_INDEX machine-readable mapping (整合段落 2025-12-28-D/F)"
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
---

## 補強規範
### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md`
- canonical_doc_key（Index 裁決識別碼）：`DEPLOY_OPS`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231__ADDENDUM_20251228_FINAL (1).md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=DEPLOY_OPS` + `canonical_filename=TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

# 補強規範
---

## G0. 適用範圍（Hard Boundary）

本 整合段落 僅處理下列事項（不創造新制度、不改寫主文）：
1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。  
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。  
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。  
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。  

本 整合段落 **不處理**：
- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

- 本文件 `doc_key` 既有標示為 `DEPLOY_OPS`；本 整合段落 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

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

- 本 整合段落 為 Only-Add；不改寫本文件任何既有條款。  
- 本 整合段落 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。  
- 本 整合段落 目的僅在於消解引用歧義、避免 Gate 因 metadata/格式缺口而誤判，並確保全鏈路可稽核、可回放。