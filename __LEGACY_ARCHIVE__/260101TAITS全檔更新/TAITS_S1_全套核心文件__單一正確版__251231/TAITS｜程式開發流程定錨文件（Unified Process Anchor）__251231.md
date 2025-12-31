# TAITS｜程式開發流程定錨文件（Unified Process Anchor）

doc_key：PROCESS_ANCHOR
治理等級：C｜操作／啟動級（Operation / Onboarding）
版本狀態：ACTIVE（Freeze v1.0；Only-Add）
裁決序位：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（本檔不覆蓋上位治理裁決）

文件類型：Engineering Process Anchor（Read-Only / Non-Governance）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
治理狀態：Freeze v1.0  
最後更新：2025-12-29  

---

## 1. 文件定位與權限聲明
- 唯一具有治理裁決力之流程定義：
  - MASTER_CANON（L1–L11）
  - ARCH_FLOW
- 本文件：
  - 不具治理裁決力
  - 不新增、不修改任何制度
  - 不覆寫 Canonical Flow
- 本文件之唯一用途：
  - 作為 TAITS 工程開發之「流程定錨文件」
  - 固定工程流程座標，終止流程歧義
  - 明確標示目前實作進度

若本文件與 Canonical 文件存在任何衝突：
---

## 2. 定錨文件存在目的

在 TAITS 專案中：

- AI 對話不具治理效力
- 不同對話可能出現不同流程敘述方式

若缺乏流程定錨，將導致：

- 新對話反覆討論流程
- 工程順序理解漂移
- 無法一致回答「目前做到哪一階段」

本文件存在目的為：

> **不論新對話或新 AI，  
所有工程討論皆必須回到同一流程座標系。**

---

## 3. 流程定錨核心原則

### 3.1 流程裁決唯一性

- Canonical Flow 僅有一條：L1–L11
- 工程敘述不得覆蓋 Canonical

### 3.2 Phase 的正確定位

- Phase 0–5 為工程敘述語言
- Phase 僅用於描述「工程進度」
- Phase 不具 PASS / VETO / 裁決權

### 3.3 程式碼可定位性要求

任何工程實作，必須能回答：

1. 屬於哪一個 Phase  
2. 對應哪一個 Canonical Layer（Lx）  
3. 能否指回對應治理文件  

---

## 4. Canonical Layer × Engineering Phase 對位表

| Canonical Layer | Layer 名稱 | 對應 Phase |
|-----------------|------------|------------|
| L1 | Data Source | Phase 1 |
| L2 | Normalization | Phase 1 |
| L3 | Snapshot & State | Phase 1 |
| L4 | Analysis | Phase 2 |
| L5 | Evidence | Phase 2 |
| L6 | Regime | Phase 3 |
| L7 | Risk & Compliance | Phase 3 |
| L8 | Strategy & Research | Phase 4 |
| L9 | Governance Gate | Phase 4 |
| L10 | Human Decision | Phase 5 |
| L11 | Execution & Control | Phase 5 |

---

## 5. Engineering Phase 定義（定錨版）

### 5.1 Phase 0｜治理與版本鎖定

性質：治理前置階段（不屬於任何 L 層）

必須完成項目：

- DOCUMENT_INDEX ACTIVE 文件確認
- GOVERNANCE_STATE = Freeze v1.0
- doc_key / version_ref / hash 固定
- 模組 L 層標註規則確立

禁止事項：

- 使用對話作為治理依據
- 未標註 L 層即開始實作

---

### 5.2 Phase 1｜資料與狀態骨架（L1–L3）

允許事項：

- 官方資料來源
- 正規化處理
- Snapshot / State 落盤與回放

禁止事項：

- 指標與訊號
- 策略與交易語義

---

### 5.3 Phase 2｜分析與證據（L4–L5）

允許事項：

- 描述性分析
- Evidence Bundle（可追溯、可回放）

禁止事項：

- buy / sell
- signal / trigger
- 績效、勝率、排序

---

### 5.4 Phase 3｜Regime 與 Risk（L6–L7）

必須成立條件：

- Regime 可標示不可交易狀態
- Risk 僅輸出 PASS / VETO
- VETO 附 reason codes
- Risk PASS Token 機制存在

禁止事項：

- Soft Pass
- 人類或 AI 覆寫 VETO

---

### 5.5 Phase 4｜策略提案與治理檢查（L8–L9）

允許事項：

- Strategy Proposal / Scenario
- Governance Gate RETURN / STOP

禁止事項：

- 策略即行為
- 策略直連 Execution
- AI 自動批准

---

### 5.6 Phase 5｜人類裁決與執行（L10–L11）

必須成立條件：

- UI 為唯一 APPROVE / REJECT 入口
- 無 Risk PASS Token → Execution BLOCK
- Execution 全程可審計、可中止

禁止事項：

- 無 UI 自動批准
- 無 Token 下單

---

## 6. 工程進度狀態標示（流程座標）
```text
Current Phase        : Phase 0
Completed Phases     : Phase 0
Next Target Phase    : Phase 1（L1–L3 Data / State Skeleton）
Blocked Layers       : L4–L11（依法不可實作）
Last Review Date     : YYYY-MM-DD

---

# 【Only-Add｜新增】All-in-One 內嵌附錄（為減檔與新手便利而設）
---

## 附錄 A｜工程操作總手冊（合併版）全文內嵌

# TAITS｜工程操作總手冊（合併版：GPT 續編 × Cursor 落地 × 雙錨）__ADDENDUM_20251228_FINAL
---

## 0. Scope Lock（Freeze v1.0 下的硬邊界）

### 0.1 本合併手冊可以做什麼
- 給你一套「**不用靠記憶**」也能長期續編的 GPT 編輯流程
- 給你一套可落地的 Cursor 工程開發流程（不跳層、不跨層合併）
- 把「雙錨」使用方式一次說清楚，並附上模板與檢核清單
- 在檔案過多時，提供「**合併而不取代**」的治理合規做法

### 0.2 本合併手冊不得做什麼
- 不得裁決：ACTIVE 文件集合、doc_key 合法性、治理等級、版本有效性、覆蓋順位
- 不得改寫／重排 Canonical Flow（L1–L11）或任何治理文件語義
- 不得弱化或繞過 Risk/Compliance 的最高否決權
- 不得以「合併」名義取代既有 PROCESS_ANCHOR 或覆寫既有治理文件
---

## 1. 你現在的問題：檔案太多，要合併——最佳作法（合規且最省事）

### 1.1 Freeze v1.0 下「合併」的正確定義
- **允許**：新增一份「合併版總手冊」（本文件），把操作流程集中，作為日常唯一入口
- **不允許**：把舊文件刪掉／用新文件覆蓋舊文件／宣稱「舊文件失效」而不留痕

### 1.2 最佳落地策略（推薦）
你只要做 3 件事：

1) **保留既有文件不動**（不刪、不覆寫）  
2) **新增本合併手冊**作為日常入口（你之後只看這一份）  
3) 只在「入口文件」做 **Only-Add 指向**（可選，但推薦）：  
   - 在 Unified Process Anchor 的附錄區 Only-Add 一段「日常操作以本合併手冊為主」  
   - 在 README 的操作區 Only-Add 一段「新手從本合併手冊開始」
---

## 2. 雙錨整合（你要記住的核心）

### 2.1 兩個錨點各司其職（不可互相取代）
- **PROCESS_ANCHOR（Unified Process Anchor）**：主流程骨架  
  用途：固定工程節點、固定「現在做到哪」、固定新對話/新任務的定位語言

- **工程轉譯/落地錨定（L1–L11×工程支撐）**：層級落地手冊  
  用途：每一層要交付哪些東西、Cursor 任務切片怎麼做、證據鏈與 Gate 怎麼落盤

### 2.2 本合併手冊的定位
- 本文件 = 「**把 GPT 續編流程 + Cursor 落地流程 + 雙錨**」統一到一份可照做的 SOP
- 本文件仍是 SUPPORT（非治理裁決），任何裁決問題依然回 DOCUMENT_INDEX

---

# PART A｜GPT 專案：開新對話如何穩定續編（小白照做）

## A1. GPT 續編的唯一正道：不靠記憶，靠 3 個檔案
1) **TAITS_GPT_WORKLOG**：進度唯一事實來源（做到哪/下一步）  
2) **TAITS_GPT_ECR_LEDGER**：工作包帳本（一行索引每次工作）  
3) **TAITS_GPT_CONTEXT_PACK**：新對話必貼續編包（把上下文一鍵搬回來）
---

## A2. 最推薦節奏：一個新對話 = 一個工作包（Work Package）

### A2.1 工作包三種類型（只能選一種）
- REPORT_ONLY：只盤點/審視（不修改）
- ONLY_ADD_EDIT：只新增（不刪/不覆寫/不偷換語義）
- GATE_CHECK：只檢核（只輸出 PASS / RETURN(缺口) / BLOCK(原因碼)）

### A2.2 什麼時候必須開新對話（新手最常用）
遇到任一條就切：
1) 換 doc_key（A 文件 → B 文件）  
2) 換任務類型（盤點 → 編輯／編輯 → 檢核）  
3) 換 Canonical Layer（Lx → Ly）  
4) 發現引用欄位缺漏/引用錯檔（回 Index Gate）  
5) 對話太長開始看不懂（直接切最省時間）

---

## A3. 新對話第一則必貼：續編包（直接照貼）
```text
TAITS 架構已完整載入，我已準備好在此基礎上繼續開發。
嚴格對齊模式：Freeze v1.0 / Only-Add / Index Gate First。

【本次任務類型】（三選一，只能選一個）
A) REPORT_ONLY（只報告不修改）
B) ONLY_ADD_EDIT（只新增，不刪減、不覆寫、不偷換語義）
C) GATE_CHECK（只輸出 PASS / RETURN(缺口清單) / BLOCK(原因碼)）

【Minimum Load Set（專案內具備）】
- AI_GOV
- DOCUMENT_INDEX
- MASTER_ARCH
- MASTER_CANON
- GOVERNANCE_STATE（Freeze v1.0）

〔TAITS 最小引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <版本日期/檔名日期>
ref_section = <章節/段落路徑>
ref_notes = 新對話啟動/本次裁決依據
audit_anchor = VERSION_AUDIT:<若未知先填 VA-PLACEHOLDER-0001>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 最小引用標頭〕

【續編狀態（從 Worklog / Ledger 帶入）】
- 上一次工作包（ecr_id）：<ECR-...>
- 上一次目標：doc_key=<...> / 插入位置=<...>
- 本次目標：doc_key=<...> / 插入位置=<...> / Only-Add
- 本次輸出要求：<可直接貼上的 md 段落 + 插入位置 + Ledger 一行>
```

---

## A4. 每個工作包結束前必做：落盤三步驟（保證可續編）

1) 把成果貼回「目標文件」（Only-Add）  
2) 更新 Worklog（最新狀態 + 追加歷史條目）  
3) 更新 Ledger（追加一行）
---

# PART B｜Cursor 工程：從拆解到落地（不跳層、不跨層合併）

## B1. Repo 最小結構（工程落地可回放）

```
/docs/governance/               # 治理文件原文快照（只讀）
/engineering/worklog/           # ENGINEERING_STATUS.md（工程進度唯一事實）
/engineering/ecr/               # ECR（每次工程變更一份）
/engineering/cr/                # CR（需要版本治理變更時）
/engineering/gates/             # Gate logs（PASS/BLOCK/RETURN/VETO）
/engineering/trace/             # 證據鏈（run_id/trace_id/artifact_id + replay bundle）
/src/l01 ... /src/l11           # 一層一目錄（不得跨層合併）
/tests/l01 ... /tests/l11
/ops/runbooks/                  # 部署/回滾/演練
```

---

## B2. 每層（L1–L11）最小交付（Minimum Deliverables）
- contracts/（IO Contract）
- runner/（可重跑入口）
- artifacts/（輸出產物＋摘要）
- evidence/（證據快照索引）
- gate/（該層 Gate 結果＋reason_codes）
- version_ref/（Active Version Map 引用）
- trace_ref/（run_id/trace_id/artifact_id）
- tests/（最小可重跑測試）

---

## B3. Cursor 任務開工 Prompt（單層單元）

```text
〔TAITS Cursor 工程任務｜Freeze v1.0｜Only-Add〕
硬性約束：
1) 僅能依 docs/governance 內 ACTIVE 文件作依據；引用必帶 ref_file/ref_doc_key/ref_version_date/ref_section/audit_anchor。
2) Only-Add：不可刪減、不可覆寫、不可偷換語義。
3) 嚴格層級邊界：本次只允許修改 /src/lXX/** 與 /tests/lXX/**（XX = 指定層）。
4) 先建立 engineering/ecr/ECR-<id>.md（含引用標頭），完成後更新工程 worklog。
5) 必須生成 run_id / trace_id / artifact_id，並落地 gate logs 與 artifacts index。

本次目標：
- layer = LXX
- deliverable = 完成 Minimum Deliverables 一輪
〔/TAITS Cursor 工程任務〕
```

---

# PART C｜合併後你要怎麼「減檔」

## C1. 你日常只看「一份」：本合併手冊
- 你之後新手操作只看本文件即可（GPT 續編 + Cursor 落地）

## C2. 你在 ChatGPT 專案內建議保留的「最小必要集合」（新手友善）
- AI_GOV（A+）
- DOCUMENT_INDEX（Authoritative Index）
- MASTER_ARCH
- MASTER_CANON
- GOVERNANCE_STATE（Freeze v1.0）
- 本合併手冊（本檔）
---

# APPENDIX｜三個 GPT 續編必備模板（可直接複製建立）

## 補強規範
```markdown
# TAITS_GPT_WORKLOG（唯一進度事實來源）

## 最新狀態（只更新本區；其餘只追加）
- last_updated: <YYYY-MM-DD HH:MM Asia/Taipei>
- governance_state: FREEZE_V1
- active_index_ref: DOCUMENT_INDEX:<version_date>
- last_work_package (ecr_id): <ECR-YYYYMMDD-####>
- last_doc_key: <doc_key>
- last_insert_point: <章節/段落路徑>
- last_output: <檔名/段落標題/產出檔>
- next_work_package: <下一步一句話>

## 歷史條目（只追加，不覆寫）
- <YYYY-MM-DD> | <ECR-...> | doc_key=<...> | insert=<...> | output=<...> | next=<...>
```

## 補強規範
```markdown
# TAITS_GPT_ECR_LEDGER（GPT 編輯工作包帳本｜Append-only）

| ecr_id | created_at | work_type | target_doc_key | target_file | insert_point | change_summary | ref_min_citation | gate_result | output_artifact | next_step |
|---|---|---|---|---|---|---|---|---|---|---|
| ECR-YYYYMMDD-0001 | YYYY-MM-DD HH:MM | ONLY_ADD_EDIT | <doc_key> | <file>.md | <位置> | 新增：... | ref_file=...; ref_doc_key=...; ref_version_date=...; ref_section=...; audit_anchor=... | N/A | <段落/檔> | 下一包：... |
```

## 補強規範
```markdown
# TAITS_GPT_CONTEXT_PACK（新對話續編包｜複製貼到新對話第一則）

（把本文件 A3 的續編包整段貼在這裡，並在每次工作包後 Only-Add 一段歷史快照）
```

---

（END）

---

## 附錄 B｜Cursor 工程落地 SOP（雙錨整合）全文內嵌

# TAITS｜Cursor 工程落地 SOP（雙錨整合：PROCESS_ANCHOR × 工程轉譯錨定）__ADDENDUM_20251228_FINAL
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
---

## 1. 你要採用的「最佳開發方式」：雙錨整合（主流程＋落地手冊）

### 1.1 雙錨分工（不可互相取代）
- **PROCESS_ANCHOR（Unified Process Anchor）**  
  用途：固定工程節點、固定新對話開工流程、固定「現在做到哪」的座標語言  
  你用它來回答：**本次工作在什麼工程節點 / 哪個階段 / 何時可進下一步**

- **工程落地拆解錨定（L1–L11×工程支撐）**  
  用途：把每一層（L1–L11）落成可交付的工程單元（contracts/runner/artifacts/evidence/gate/version_ref/trace_ref/tests）  
  你用它來回答：**本層要改哪些檔案、要交付什麼、要如何可回放**
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

## 補強規範

- Worklog：`engineering/worklog/ENGINEERING_STATUS.md`
- ECR：`engineering/ecr/ECR-YYYYMMDD-####.md`
- CR：`engineering/cr/CR-YYYYMMDD-####.md`
- Gate logs：`engineering/gates/{run_id}/<gate>.json`
- Artifacts：`engineering/trace/{run_id}/{layer}/{artifact_id}/*`
- Replay Bundle：`engineering/trace/{run_id}/replay_bundle.<zip|dir>`
---

## 附錄 C｜GPT 新對話續編 SOP（最新版）全文內嵌

# TAITS｜GPT 新對話續編編輯 SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228R_FINAL
---

## 0. 你要先記住的三句話（小白版）

1) **新對話不會自動接續**：不要期待 AI 記得你上次做到哪。  
2) **續編靠檔案，不靠記憶**：你要把「做到哪、加了什麼、依據什麼」寫回專案檔案。  
3) **一切裁決回 DOCUMENT_INDEX**：ACTIVE / doc_key / 版本有效性，不能靠口頭說或靠舊對話。

---

## 1. 你的「GPT 續編」最小系統（必備 4 件套）
1) **TAITS_GPT_WORKLOG**（進度唯一事實來源）  
2) **TAITS_GPT_ECR_LEDGER**（工作包帳本：所有工作包一行索引）  
3) **TAITS_GPT_CONTEXT_PACK**（新對話必貼的續編包：把上下文一鍵搬回來）  
4) **目標治理文件（doc_key 對應檔）**（你真正要 Only-Add 的那份文件）
---

## 2. 最佳工作方式：一個新對話 = 一個「工作包」（Work Package）

### 2.1 工作包是什麼？
工作包 = 你在一個對話裡只做一件明確事情，並在結束前把成果落回檔案。

工作包的典型範例：
- 只針對某個 **doc_key** 進行一次 Only-Add：新增一段文字到指定章節末
- 只做一次「盤點/審視」報告（只報告、不修改）
- 只做一次 Gate 檢核（PASS / RETURN 缺口清單 / BLOCK 原因碼）

### 2.2 為什麼必須這樣做？
- 對話變長時，容易引用漏欄位、容易漂移、容易跨 doc_key
- Freeze v1.0 下，「越做越像改寫制度」的風險會隨對話長度上升
- 你只要把每個工作包落盤（Worklog + Ledger），就能用新對話接續，不會斷線

---

## 3. 什麼時候要開新對話（你可以直接照規則判斷）

遇到任一條，**建議直接開新對話**：

1) 你要換目標 doc_key（A 文件 → B 文件）  
2) 你要換任務類型（盤點 → 編輯；編輯 → Gate 檢核）  
3) 你要換 Canonical Layer（Lx → Ly）  
4) 你發現引用欄位缺漏或引用錯檔（要回到 Index Gate）  
5) 你覺得自己開始看不懂、描述不清楚（小白常見：直接切新對話最省時間）

---

## 4. 新對話「必貼」續編包（最重要：照貼就能續）
```text
TAITS 架構已完整載入，我已準備好在此基礎上繼續開發。
嚴格對齊模式：Freeze v1.0 / Only-Add / Index Gate First。

【本次任務類型】（三選一，只能選一個）
A) REPORT_ONLY（只報告不修改）
B) ONLY_ADD_EDIT（只新增，不刪減、不覆寫、不偷換語義）
C) GATE_CHECK（只輸出 PASS / RETURN(缺口清單) / BLOCK(原因碼)）

【Minimum Load Set｜我已在專案內具備以下檔案】
- AI_GOV（A+ 母法）
- DOCUMENT_INDEX（Authoritative Index）
- MASTER_ARCH（母體鐵律）
- MASTER_CANON（L1–L11 Canonical Flow）
- GOVERNANCE_STATE（Freeze v1.0）

〔TAITS 最小引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <請填你要引用的檔案完整檔名>
ref_doc_key = <請填 doc_key>
ref_version_date = <請填版本日期/或檔名日期>
ref_section = <請填章節/段落路徑>
ref_notes = 新對話啟動/本次裁決依據
audit_anchor = VERSION_AUDIT:<若未知先填 VA-PLACEHOLDER-0001>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 最小引用標頭〕

【續編狀態（從 Worklog / Ledger 帶入）】
- 上一次工作包（ecr_id）：<例如 ECR-20251228-0003>
- 上一次目標：doc_key=<...> / 插入位置=<章節末/段落末>
- 本次目標：doc_key=<...> / 插入位置=<...> / Only-Add
- 本次輸出要求：<請明確寫：要我輸出「可直接貼上的 md 段落」+「插入位置說明」+「ECR Ledger 一行」>
```

---

## 5. 三種任務的「正確問法」（小白照抄）

### 5.1 REPORT_ONLY（只盤點，不修改）
```text
嚴格對齊模式。
請只做盤點報告，不做任何修改（Report-only）。
目標：doc_key=<...>
輸出：1) 你觀察到的缺口清單 2) 建議的 Only-Add 增補方向（只列方向，不產生可貼入原文的段落）
```

### 5.2 ONLY_ADD_EDIT（最常用：只新增）
```text
嚴格對齊模式。
任務：Only-Add 編輯（不得刪減/覆寫/偷換語義）。
doc_key=<...>
編輯範圍=<指定章節末/指定段落末/或 整合段落 區>
目的=<你要補什麼>
輸出必含：1) 可直接貼上的新增段落（md） 2) 插入位置一句話 3) ECR Ledger 一行（含引用欄位摘要）
```

### 5.3 GATE_CHECK（只做檢核）
```text
嚴格對齊模式。
請對下列輸出做 Gate 檢核：
- Index Gate（引用欄位齊全 / doc_key 合法）
- Only-Add Gate（是否有刪減/覆寫/偷換語義）
輸出只允許：PASS / RETURN(缺口清單) / BLOCK(原因碼)
以下是待檢核內容：<貼上你要檢核的段落或提案>
```

---

## 6. 你每個工作包結束前必做的「落盤三步驟」
### Step 1｜把本次結果貼回「目標治理文件」
- 只允許 Only-Add（新增段落）  
- 只能貼到你指定的位置（章節末/段落末/整合段落 區）  
- 不得偷偷改原文句子

### Step 2｜更新 Worklog（只更新「最新狀態」＋追加一條歷史）
- 填：last_work_package / last_doc_key / last_insert_point / next_work_package

### Step 3｜更新 Ledger（追加一行）
- 把 ecr_id、目標 doc_key、插入位置、引用摘要、下一步寫清楚
- 你開新對話時，只要複製最新一行就能續編

---

## 7. 新手常見錯誤與立即救援（照做就能回來）

### 7.1 我忘了上次做到哪
- 先開 Worklog，看「最新狀態」區塊  
- 再開 Ledger，看最新一行（ecr_id / doc_key / insert_point）  
- 新對話貼 Context Pack，把最新一行帶進來即可

### 7.2 我不知道哪些文件是 ACTIVE
- 不要猜。  
- 用 REPORT_ONLY 任務，要求我「只引用 DOCUMENT_INDEX」做 Phase 0 盤點。

### 7.3 我貼上去後發現有錯字或寫錯位置
- 不要去修改舊內容（避免覆寫/改寫爭議）。  
- 新增一個「更正工作包」Only-Add：補一段「更正聲明」或「勘誤」段落（視你文件風格），並在 Ledger 新增一行標註 CORR。

### 7.4 對話太長，看不懂了
- 立刻切新對話，帶上 Context Pack。  
- 新對話只做一件事：把缺口補齊或做 Gate 檢核。

---

## 8. 你應該採用的日常節奏（最穩、最省時間）

### 8.1 每天只做一個工作包（推薦）
- 今天只做：某 doc_key 的一段 Only-Add  
- 做完落盤：貼回目標文件 + 更新 Worklog + 更新 Ledger  
- 明天做下一段或下一份文件

### 8.2 你不用一次理解 Phase 0~5
如果你目前主要在整理/增補文件：
- 先把工作包固定成「REPORT_ONLY」與「ONLY_ADD_EDIT」兩種即可  
- 真的要進工程實作（Cursor）再引入工程 Phase 與 Lx 模組化

---

## 補強規範
---

## 補強規範
---

## 補強規範
---

（END）

---

## 附錄 D｜GPT 模板：ECR_LEDGER（最新版）全文內嵌

# TAITS_GPT_ECR_LEDGER（GPT 編輯工作包帳本｜Append-only）__ADDENDUM_20251228R_FINAL
---

## 1. 欄位說明（最小欄位）

- ecr_id：工作包編號（你自訂，但要唯一；建議 `ECR-YYYYMMDD-####`）
- created_at：建立時間（Asia/Taipei）
- work_type：REPORT_ONLY / ONLY_ADD_EDIT / GATE_CHECK
- target_doc_key：本次目標 doc_key
- target_file：你實際要貼入/更新的檔名（或「產出檔」）
- insert_point：插入位置（章節/段落路徑；Report-only 可填 N/A）
- change_summary：一句話摘要（Only-Add）
- ref_min_citation：引用摘要（至少包含：ref_file / ref_doc_key / ref_version_date / ref_section / audit_anchor）
- gate_result：PASS / RETURN / BLOCK（若未做 Gate 檢核則填 N/A）
- output_artifact：輸出產物路徑或檔名（例如：新增段落標題 / addendum 檔）
- next_step：下一個工作包要做什麼（務必寫一句話）

---

## 2. Ledger Entries（只追加）

| ecr_id | created_at | work_type | target_doc_key | target_file | insert_point | change_summary | ref_min_citation | gate_result | output_artifact | next_step |
|---|---|---|---|---|---|---|---|---|---|---|
| ECR-20251228-0001 | 2025-12-28 00:00 | ONLY_ADD_EDIT | (EXAMPLE) DOCUMENT_INDEX | (EXAMPLE) <file>.md | (EXAMPLE) §X 末 | (EXAMPLE) 新增：引用格式補強段 | ref_file=...; ref_doc_key=...; ref_version_date=...; ref_section=...; audit_anchor=... | N/A | (EXAMPLE) 段落標題/產出檔 | (EXAMPLE) 下一包：Only-Add 增補 MASTER_ARCH |
| ECR-20251228-0002 | 2025-12-28 00:00 | REPORT_ONLY | (EXAMPLE) MASTER_CANON | (EXAMPLE) <file>.md | N/A | (EXAMPLE) 盤點：L1–L11 邊界缺口 | ref_file=...; ref_doc_key=...; ref_version_date=...; ref_section=...; audit_anchor=... | N/A | (EXAMPLE) 報告摘要 | (EXAMPLE) 下一包：Only-Add 補一段於 §Y 末 |
---

## 附錄 E｜GPT 模板：WORKLOG（最新版）全文內嵌

# TAITS_GPT_WORKLOG（唯一進度事實來源）__ADDENDUM_20251228R_FINAL
---

## 最新狀態（只更新本區；其餘只追加）
- last_updated: <YYYY-MM-DD HH:MM Asia/Taipei>
- governance_state: FREEZE_V1
- active_index_ref: DOCUMENT_INDEX:<version_date>
- last_work_package (ecr_id): <ECR-YYYYMMDD-####>
- last_doc_key: <doc_key>
- last_insert_point: <章節/段落路徑>
- last_output: <檔名/段落標題/產出檔>
- next_work_package: <你下一步要做的事（只寫一句話）>

---

## 歷史條目（只追加，不覆寫）
- <YYYY-MM-DD> | <ECR-...> | doc_key=<...> | insert=<...> | output=<...> | next=<...>

---

## 附錄 F｜GPT 模板：CONTEXT_PACK（最新版）全文內嵌

# TAITS_GPT_CONTEXT_PACK（新對話續編包｜複製貼到新對話第一則）__ADDENDUM_20251228R_FINAL
---

## 最新續編包（把本段整段複製貼到新對話第一則）

```text
TAITS 架構已完整載入，我已準備好在此基礎上繼續開發。
嚴格對齊模式：Freeze v1.0 / Only-Add / Index Gate First。

【本次任務類型】（三選一，只能選一個）
A) REPORT_ONLY（只報告不修改）
B) ONLY_ADD_EDIT（只新增，不刪減、不覆寫、不偷換語義）
C) GATE_CHECK（只輸出 PASS / RETURN(缺口清單) / BLOCK(原因碼)）

【Minimum Load Set（專案內具備）】
- AI_GOV
- DOCUMENT_INDEX
- MASTER_ARCH
- MASTER_CANON
- GOVERNANCE_STATE（Freeze v1.0）

〔TAITS 最小引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <版本日期/檔名日期>
ref_section = <章節/段落路徑>
ref_notes = 新對話啟動/本次裁決依據
audit_anchor = VERSION_AUDIT:<若未知先填 VA-PLACEHOLDER-0001>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 最小引用標頭〕

【續編狀態（從 Worklog / Ledger 帶入）】
- 上一次工作包（ecr_id）：<ECR-...>
- 上一次目標：doc_key=<...> / 插入位置=<...>
- 本次目標：doc_key=<...> / 插入位置=<...> / Only-Add
- 本次輸出要求：<可直接貼上的 md 段落 + 插入位置 + Ledger 一行>
```

---

## 歷史續編包（只追加，不覆寫）
- <YYYY-MM-DD>：<把當天的續編包貼在這裡作快照>

---

## 附錄 G｜專案檔案更新包（Migration Pack）全文內嵌

# TAITS｜專案檔案更新包（Only-Add Migration Pack：合併入口×不刪檔）__ADDENDUM_20251228_FINAL
---

## 0. 你要達成的結果（你說的「更新專案檔案」= 這三件事）

1) 你日常只需要看 **一份入口文件**：  
   - `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`

2) 既有 SOP/錨定檔不刪不改語義，但**加上「已併入合併版」的導流段**（避免你或未來的你走錯文件）。

3) 專案入口（README / Unified Process Anchor）用 Only-Add 加上「從此以合併版為入口」的指引段。

---

## 1. 你要放進專案的「唯一入口文件」

### 1.1 請確保專案已包含下列檔案（若已有可跳過）
- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`
---

## 2. 更新入口文件：README（Only-Add 貼上段）

### 2.1 目標檔案
- `TAITS_專案總覽與使用說明（README）__251231__ADDENDUM_20251227_FINAL.md`

### 2.2 插入位置（Only-Add）
建議插在 README 的「新手開始/操作方式/如何開新對話」段落**末尾**（或文件最末尾新增「附錄：工程操作入口」章）。

### 2.3 可直接貼上的新增段落（複製貼上即可）
```markdown
---

## 【Only-Add｜新增】工程操作入口（合併版總手冊）
### 日常唯一入口（建議）
從即日起，日常操作（GPT 新對話續編 + Cursor 工程落地 + 雙錨使用）請以以下文件為主：

- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`

### 重要限制（避免誤用）
- 本合併版總手冊屬 SUPPORT（工程/操作支援），不具治理裁決效力。  
- 任何 ACTIVE / doc_key / 版本有效性 / 覆蓋序之裁決，一律回到 `DOCUMENT_INDEX → MASTER_ARCH → AI_GOV`。
```

---

## 3. 更新主流程錨點：Unified Process Anchor（Only-Add 貼上段）

### 3.1 目標檔案（擇一）
- 若你專案使用「主檔」：`TAITS｜程式開發流程定錨文件（Unified Process Anchor）.md`
- 若你專案以「更新版」為準：`TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md`
### 3.2 插入位置（Only-Add）
建議插在「如何開新對話 / 如何對齊 / 本文件用途」段落**末尾**，或文件最末尾新增「附錄：日常操作入口」章。

### 3.3 可直接貼上的新增段落
```markdown
---

## 【Only-Add｜新增】日常操作入口（合併版總手冊）
### 合併版總手冊（建議作為日常唯一入口）
- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`

### 本文件與合併版的分工（不可互相取代）
- 本文件（PROCESS_ANCHOR / Unified Process Anchor）：負責「工程節點與對話一致性（主流程骨架）」  
- 合併版總手冊：負責「GPT 新對話續編 + Cursor 任務切片 + 證據鏈與 Gate 落盤」之可操作細節
```

---

## 4. 更新既有 SOP 檔：加上「已併入合併版」導流段（Only-Add）
---

### 4.1 目標檔案 A（Cursor）
- `TAITS｜Cursor工程落地SOP（雙錨整合：PROCESS_ANCHOR×工程轉譯錨定）__ADDENDUM_20251228_FINAL.md`

**新增導流段（貼在文件最前或最末）**
```markdown
---

## 【Only-Add｜新增】導流聲明（合併版入口）

本文件內容已納入下列「合併版總手冊」作為日常唯一入口；本文件仍保留作歷史快照與追溯參考（Freeze v1.0：Only-Add，不刪檔不覆寫）。

- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`

> 注意：本文件屬 SUPPORT（工程支援），不具治理裁決效力；裁決一律回 `DOCUMENT_INDEX → MASTER_ARCH → AI_GOV`。
```

---

### 4.2 目標檔案 B（GPT）
- `TAITS｜GPT新對話續編編輯SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228_FINAL.md`
- 或你最新修訂版：`TAITS｜GPT新對話續編編輯SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228R_FINAL.md`

**新增導流段**
```markdown
---

## 【Only-Add｜新增】導流聲明（合併版入口）

本文件內容已納入下列「合併版總手冊」作為日常唯一入口；本文件仍保留作歷史快照與追溯參考（Freeze v1.0：Only-Add，不刪檔不覆寫）。

- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`
```

---

### 4.3 目標檔案 C（工程落地拆解錨定）
- `TAITS｜工程落地拆解流程錨定（L1–L11×工程支撐）__ADDENDUM_20251228_FINAL.md`

**新增導流段**
```markdown
---

## 【Only-Add｜新增】導流聲明（合併版入口）

本文件內容已納入下列「合併版總手冊」作為日常唯一入口；本文件仍保留作歷史快照與追溯參考（Freeze v1.0：Only-Add，不刪檔不覆寫）。

- `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md`
```

---

## 5. 最終你會得到什麼（你要的「檔案變少」實務效果）

- 你日常只需要看：**合併版總手冊**
- README / Unified Process Anchor 會指向合併版（新手入口一致）
- 舊文件不刪除、不覆寫，只加「導流段」讓你不會走錯
- 完全符合 Freeze v1.0（Only-Add）與「不取代既有語義」要求

---

## 6. 小白執行清單（照打勾就完成更新）

- [ ] 把合併版總手冊放進專案檔案池  
- [ ] 在 README 末尾貼上第 2 節新增段落  
- [ ] 在 Unified Process Anchor 末尾貼上第 3 節新增段落  
- [ ] 在三份舊 SOP/錨定檔貼上第 4 節導流段（可選但強烈建議）  
- [ ] 從此你只用合併版工作；舊檔只做追溯參考

---

（END）

---

（END OF ALL-IN-ONE APPENDIX）

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

- 本文件主文未明示 `doc_key`；依 Index Gate（DOCUMENT_INDEX）補登／裁決口徑，本文件之引用端 `doc_key` **必須**使用：`PROCESS_ANCHOR`。

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
---

# 補強規範
---

## P1. 定義（Audit Anchor Placeholder）
本文件內出現之字串：

- `VA-PLACEHOLDER-0001`

其性質為 **Audit Anchor Placeholder（稽核錨點占位值）**，僅允許用於「對話草案 / 範本示例 / 尚未寫入 ACTIVE 的暫存文本」之表示用途。

## P2. ACTIVE 入庫門檻（必須替換）
凡任何內容被納入 **ACTIVE 文件集合**、或被作為 Gate 稽核依據、或被 VERSION_AUDIT 引用時：

- `VA-PLACEHOLDER-0001` **不得存在**；必須替換為 VERSION_AUDIT 中可查得之有效條目 ID。  
- 有效 ID 格式以 VERSION_AUDIT「METADATA_FIX Ledger」現行規則為準（例如：`VA-METADATA_FIX-YYYYMMDD-NNNN`）。

## P3. 最小替換規則（不新增制度，只對齊既有 VERSION_AUDIT）
- 若本次變更已對應既有 Ledger 條目：以該條目 ID 作為 `audit_anchor`。  
- 若本次變更為新增（Only-Add）且尚無對應條目：必須於同一批次變更中，先在 VERSION_AUDIT｜整合段落 A｜METADATA_FIX Ledger 追加條目，再以新增條目 ID 作為 `audit_anchor`。

## P4. 裁決封口（避免誤用）
- `VA-PLACEHOLDER-0001` 不具任何治理裁決效力；不得被用於追溯、稽核、回放、或證據鏈斷言。  
- 任何 Agent 或工具不得基於 `VA-PLACEHOLDER-0001` 自行推導「缺少稽核資料可自行補完」之授權。

## P5. 最終宣告
- 本 整合段落 為 Only-Add；不改寫本文件任何既有條款。  
- 本 整合段落 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。
```