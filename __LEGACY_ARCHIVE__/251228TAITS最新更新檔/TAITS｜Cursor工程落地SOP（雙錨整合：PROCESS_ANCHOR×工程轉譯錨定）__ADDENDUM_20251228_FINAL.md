# TAITS｜Cursor 工程落地 SOP（雙錨整合：PROCESS_ANCHOR × 工程轉譯錨定）__ADDENDUM_20251228_FINAL

> 文件定位：Engineering Runbook / SOP（工程操作手冊）  
> 文件屬性：SUPPORT / Non-Governance（工程支援文件；**不具治理裁決效力**）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
> 版本日期：2025-12-28  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
> 使用前提：僅能引用 DOCUMENT_INDEX 中 **ACTIVE** 的治理文件作為工程依據；其餘視為無治理效力。  

---

## 0. Scope Lock（必讀｜Freeze v1.0 下的硬邊界）

### 0.1 本文件**可以**做什麼
- 給你一套「不靠對話記憶」也能長期續編的 **Cursor 工程落地流程**
- 把 TAITS 的 Canonical（L1–L11）落成可編輯、可測試、可回放、可稽核的工程單元
- 定義「雙錨整合」使用方式：
  - `PROCESS_ANCHOR`（Unified Process Anchor）：**主流程骨架（工程節點 / 對話一致性）**
  - `工程落地拆解流程錨定（L1–L11×工程支撐）`：**層級落地手冊（每層最小交付 / Cursor 任務切片 / 證據鏈）**

### 0.2 本文件**不得**做什麼（硬禁止）
- 不得裁決：ACTIVE 文件集合、doc_key 合法性、治理等級、版本有效性、覆蓋順位
- 不得改寫／重排 Canonical Flow（L1–L11）或任何治理文件語義
- 不得弱化或繞過 Risk/Compliance 的最高否決權
- 不得以工程便利偷換制度語義（包括「把工程文件當治理裁決」）

> 涉及裁決（ACTIVE / doc_key / 衝突 / 生效狀態 / 覆蓋序）一律回：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。

---

## 1. 你要採用的「最佳開發方式」：雙錨整合（主流程＋落地手冊）

### 1.1 雙錨分工（不可互相取代）
- **PROCESS_ANCHOR（Unified Process Anchor）**  
  用途：固定工程節點、固定新對話開工流程、固定「現在做到哪」的座標語言  
  你用它來回答：**本次工作在什麼工程節點 / 哪個階段 / 何時可進下一步**

- **工程落地拆解錨定（L1–L11×工程支撐）**  
  用途：把每一層（L1–L11）落成可交付的工程單元（contracts/runner/artifacts/evidence/gate/version_ref/trace_ref/tests）  
  你用它來回答：**本層要改哪些檔案、要交付什麼、要如何可回放**

> 原則：**主流程骨架不能被取代；落地手冊不能被誤用為裁決文件。**  
> Freeze v1.0 下，一律 Only-Add：保留既有錨點、以新增並列方式演進。

---

## 2. 「不怕新對話」的核心機制：工程續航三件套（Worklog / ECR / Evidence）

你要放棄依賴對話記憶，改用 repo 內的「可回放工程紀錄」作為唯一事實來源：

1) **Worklog（進度唯一事實來源）**  
   - 檔案：`engineering/worklog/ENGINEERING_STATUS.md`  
   - 用來紀錄：目前做到哪個 L 層、完成度、關聯的 ECR/CR、產物索引、Gate 結果

2) **ECR（每次工程變更一份）**  
   - 目錄：`engineering/ecr/`  
   - 用來紀錄：本次改動範圍、引用依據、檔案清單、Gate 結果、證據鏈索引

3) **Evidence / Trace（證據鏈與回放束）**  
   - 目錄：`engineering/trace/`  
   - 用來紀錄：`run_id / trace_id / artifact_id` 對應，以及 replay bundle

> 只要這三件套存在，新對話只要「讀 Worklog + 指向最新 ECR」就能 100% 續編，不需要你或 AI 記得之前說過什麼。

---

## 3. Repo 結構（最小可落地，且支援雙錨）

```
/docs/
  /governance/                  # ACTIVE 治理文件原文（只讀快照）
  /governance/_index/           # DOCUMENT_INDEX / README / BEGINNER_GUIDE（入口與行為規範）
/engineering/
  /worklog/                     # ENGINEERING_STATUS.md（唯一進度事實來源）
  /ecr/                         # ECR（每次工程變更一份）
  /cr/                          # CR（需要版本治理變更時）
  /gates/                       # Gate 執行紀錄（PASS/BLOCK/RETURN/VETO + reason_codes）
  /trace/                       # 證據鏈與回放束（run_id/trace_id/artifact_id）
/src/
  /l01/ ... /l11/               # 一層一目錄（不得跨層合併）
/tests/
  /l01/ ... /l11/
/ops/
  /runbooks/                    # 部署/回滾/停機/演練（對齊 DEPLOY_OPS）
```

---

## 4. 每次「開工」的標準流程（任何新對話、新分支、新任務都一樣）

> 這一節是你每天真正要照做的流程。  
> **流程順序不可換**：Index Gate → 定位（Lx）→ 交付（Minimum Deliverables）→ Gate → 記錄（Worklog/ECR/Evidence）。

### Step 0｜新對話啟動（嚴格對齊模式）
把下面這段貼在新對話開頭（每次都貼）：

```text
請進入嚴格對齊模式（Freeze v1.0 / Only-Add / Index Gate First）。

〔TAITS 引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
audit_anchor = VERSION_AUDIT:<change_id 或變更錨點>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 引用標頭〕

本次工作定位：
- Canonical Layer = <Lx>
- Engineering Unit = <一句話交付物>
- 續編依據（Worklog）= engineering/worklog/ENGINEERING_STATUS.md（最新條目：<ID/日期>）
- 本次 ECR = engineering/ecr/ECR-<id>.md
```

### Step 1｜Index Gate（引用合法性）
你要確保本次工作引用的是：
- DOCUMENT_INDEX 列為 ACTIVE 的 doc_key
- 引用標頭欄位齊全（ref_file / ref_doc_key / ref_version_date / ref_section / audit_anchor）

Fail 原則：
- 缺欄位 → RETURN（先補欄位再做事）
- 引用非 ACTIVE 或不存在 → BLOCK（停止；回到 DOCUMENT_INDEX 修正引用）

### Step 2｜主流程定位（用 PROCESS_ANCHOR 只做「現在在哪」）
你只做三件事：
1) 宣告本次工程節點（例如：Phase 0 / Phase 1…）  
2) 宣告本次 Canonical Layer（只能一層：Lx）  
3) 宣告交付物（只能一件：Minimum Deliverables 的一輪）

> PROCESS_ANCHOR 的用途到這裡就夠了：它負責讓每次對話都不漂移。

### Step 3｜層級落地（用「工程落地拆解錨定」交付最小一輪）
在你選定的 Lx 目錄內，只做該層的最小交付物一輪（不得跨層）：

- `contracts/`：IO Contract（輸入/輸出契約）
- `runner/`：可重跑入口
- `artifacts/`：產物（含摘要）
- `evidence/`：證據快照索引（指向 artifact_id）
- `gate/`：該層 Gate 結果與 reason_codes
- `version_ref/`：Active Version Map 引用
- `trace_ref/`：run_id / trace_id / artifact_id 對應
- `tests/`：最小可重跑測試

### Step 4｜Gate 結果（必須存檔，不得只口頭說）
你要產出至少三個 Gate 的結果並落地成檔案：

- `engineering/gates/<run_id>/index_gate.json`
- `engineering/gates/<run_id>/layer_gate.json`
- `engineering/gates/<run_id>/<layer>/layer_gate_result.json`

若涉及交易路徑／風控：
- `engineering/gates/<run_id>/risk_gate.json`（PASS/VETO）

若涉及治理完整性：
- `engineering/gates/<run_id>/gov_gate.json`（PASS/BLOCK/RETURN）

### Step 5｜記錄（Worklog + ECR + Trace）＝「可續編」的唯一保障
- 更新 `engineering/ecr/ECR-<id>.md`
- 更新 `engineering/worklog/ENGINEERING_STATUS.md`
- 在 `engineering/trace/<run_id>/...` 放入產物索引與 replay bundle（或資料夾束）

---

## 5. 三份核心文件模板（你可以直接複製使用）

### 5.1 ENGINEERING_STATUS.md（Worklog｜唯一進度事實來源）
> 建議放在：`engineering/worklog/ENGINEERING_STATUS.md`

```markdown
# ENGINEERING_STATUS（唯一進度事實來源）

## 最新狀態（必填）
- last_updated: <YYYY-MM-DD HH:MM>
- governance_state: Freeze v1.0
- active_index_ref: DOCUMENT_INDEX:<version_date>
- current_phase: <Phase 0~5 或 Unknown>
- current_layer: <L01~L11 或 Unknown>
- current_unit: <一句話交付物>
- current_run_id: <run_id>
- latest_ecr: engineering/ecr/ECR-<id>.md
- latest_cr: engineering/cr/CR-<id>.md（若無則填 N/A）
- last_gate_summary:
  - index_gate: PASS/BLOCK/RETURN
  - layer_gate: PASS/BLOCK
  - risk_gate: PASS/VETO（若無則 N/A）
  - gov_gate: PASS/BLOCK/RETURN（若無則 N/A）
- artifacts_index:
  - artifact_id: <artifact_id>
  - path: engineering/trace/<run_id>/<layer>/<artifact_id>/
  - hash: <hash>

## 歷史條目（追加，不覆寫）
- <YYYY-MM-DD> | <Phase> | <Layer> | <ECR> | <run_id> | <Gate 結果摘要> | <artifact_id>
```

### 5.2 ECR 模板（工程變更紀錄｜每次改動一份）
> 建議放在：`engineering/ecr/ECR-YYYYMMDD-####.md`

```markdown
# ECR-YYYYMMDD-####

〔TAITS 引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
audit_anchor = VERSION_AUDIT:<change_id 或 N/A>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 引用標頭〕

## 1) 工作定位
- phase: <Phase 0~5 或 Unknown>
- canonical_layer: <L01~L11>
- engineering_unit: <一句話交付物>
- run_id: <run_id>

## 2) Only-Add 聲明（必填）
- 本次變更僅新增：是/否
- 是否刪除任何內容：否（必須為否）
- 是否覆寫任何語義：否（必須為否）

## 3) 變更清單（檔案級）
- added:
  - <path>
- modified:
  - <path>（若修改，需說明「修改屬工程層補強，未改寫治理語義」）
- deleted:
  - （必須為空）

## 4) Gate 結果（必填）
- index_gate: PASS/BLOCK/RETURN
- layer_gate: PASS/BLOCK
- risk_gate: PASS/VETO（若無填 N/A）
- gov_gate: PASS/BLOCK/RETURN（若無填 N/A）
- reason_codes:
  - <code>: <描述>

## 5) Evidence / Artifacts（必填）
- trace_ref:
  - run_id: <run_id>
  - trace_id: <trace_id>
  - artifact_id: <artifact_id>
- artifacts_path: engineering/trace/<run_id>/<layer>/<artifact_id>/
- replay_bundle: engineering/trace/<run_id>/replay_bundle.<zip|dir>

## 6) 下一步（必填）
- next_layer_or_unit: <Lx / unit>
- missing_items_if_return: [ ... ]
```

### 5.3 CR 模板（VERSION_AUDIT 對齊｜需要治理級變更時才用）
> 建議放在：`engineering/cr/CR-YYYYMMDD-####.md`

```markdown
# CR-YYYYMMDD-####

## change_id
CR-YYYYMMDD-####

## scope
doc / policy / rule / model / config / code（擇一或多選）

## reason
（不得使用「感覺更好」；需可稽核原因）

## risk_impact
- affects_risk_compliance: yes/no
- affects_execution: yes/no
- affects_ui: yes/no
- affects_audit_replay: yes/no
- notes: ...

## rollback_plan
（如何回滾到上一版本；回滾以切換事件為準，不覆寫舊內容）

## approver
（授權者）

## effective_time
<YYYY-MM-DD HH:MM>

## references（最小引用格式）
〔TAITS 引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
audit_anchor = VERSION_AUDIT:<change_id>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 引用標頭〕
```

---

## 6. Cursor 的「一鍵任務」模板（直接貼給 Cursor 用）

### 6.1 Cursor 開工 Prompt（單層單元、必含 ECR）
```text
〔TAITS Cursor 工程任務｜Freeze v1.0｜Only-Add〕
硬性約束：
1) 僅能依 docs/governance 內 ACTIVE 文件作依據；引用必帶 ref_file/ref_doc_key/ref_version_date/ref_section/audit_anchor。
2) Only-Add：不可刪減、不可覆寫、不可偷換語義。
3) 嚴格層級邊界：本次只允許修改 /src/lXX/** 與 /tests/lXX/**（XX = 指定層）。
4) 先建立 engineering/ecr/ECR-<id>.md（使用 ECR 模板），並在完成後更新 engineering/worklog/ENGINEERING_STATUS.md。
5) 必須生成 run_id / trace_id / artifact_id，並落地 gate logs 與 artifacts index。

本次目標：
- phase = <Phase>
- layer = LXX
- deliverable = 完成 Minimum Deliverables 一輪（contracts/runner/artifacts/evidence/gate/version_ref/trace_ref/tests）
〔/TAITS Cursor 工程任務〕
```

### 6.2 Cursor 完工前自檢 Prompt（Fail 任一條就停）
```text
請逐條驗證並輸出 PASS/FAIL：
- Index Gate：ECR 引用標頭欄位是否齊全？ref_doc_key 是否為 ACTIVE？
- Only-Add：是否有任何刪除/覆寫/語義替換？
- Layer Gate：是否只改動 /src/lXX 與 /tests/lXX？是否跨層 import 或耦合？
- Evidence：是否生成 run_id/trace_id/artifact_id 並建立 artifacts index？
- Replay：是否能用 runner 入口重跑並得到一致輸出（hash 或摘要一致）？
FAIL 任一項：停止，提出最小補強（只增補，不重構）。
```

---

## 7. 你每天照做的「最短正路」（推薦節奏）

> 你不需要一次做完全部 L1–L11。你只需要「每天完成一個 Lx 的最小交付一輪」，系統就會穩定成長且可續編。

1) 開新對話 → 貼「嚴格對齊模式」模板  
2) 讀 Worklog（ENGINEERING_STATUS） → 確認目前 Lx / ECR / run_id  
3) 選定本次只做一層（Lx）  
4) 依「工程落地拆解錨定」完成 Minimum Deliverables 一輪  
5) 存 Gate logs + artifacts index  
6) 更新 ECR + Worklog  
7) 結束

---

## 8. 常見失敗模式與硬性修正方式（Freeze v1.0）

### 8.1 失敗：換新對話接不起來
- 修正：以 Worklog 為唯一事實來源；新對話只要求「讀 Worklog + 指向最新 ECR」，禁止「憑印象補完」

### 8.2 失敗：跨層混寫（L3 的東西跑去改 L4）
- 修正：Layer Gate 必須 BLOCK；拆成兩個任務，分別完成兩層 Minimum Deliverables

### 8.3 失敗：先寫功能，最後補審計
- 修正：先把 Evidence/Trace/Gate logs 做起來；否則最後會卡在「無法回放」而難以補救

### 8.4 失敗：把工程文件拿去裁決治理
- 修正：Scope Lock 必須寫死：工程文件不具裁決效力；裁決一律回 DOCUMENT_INDEX

---

## Appendix A｜命名建議（可回放友善）

- Worklog：`engineering/worklog/ENGINEERING_STATUS.md`
- ECR：`engineering/ecr/ECR-YYYYMMDD-####.md`
- CR：`engineering/cr/CR-YYYYMMDD-####.md`
- Gate logs：`engineering/gates/{run_id}/<gate>.json`
- Artifacts：`engineering/trace/{run_id}/{layer}/{artifact_id}/*`
- Replay Bundle：`engineering/trace/{run_id}/replay_bundle.<zip|dir>`

> 以上為工程命名建議；不得與治理 doc_key 概念混淆。

