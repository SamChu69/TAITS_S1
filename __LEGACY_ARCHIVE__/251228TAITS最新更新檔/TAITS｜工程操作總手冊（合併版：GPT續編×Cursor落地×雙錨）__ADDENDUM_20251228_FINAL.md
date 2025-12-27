# TAITS｜工程操作總手冊（合併版：GPT 續編 × Cursor 落地 × 雙錨）__ADDENDUM_20251228_FINAL

> 文件定位：Master Operating Runbook（合併版總手冊；供 GPT 專案與 Cursor 工程共同使用）  
> 文件屬性：SUPPORT / Non-Governance（工程/操作支援文件；**不具治理裁決效力**）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
> 版本日期：2025-12-28  
> 合併目的：在不違反 Freeze v1.0 / Only-Add 的前提下，把「日常操作流程」集中到**一份文件**，避免檔案過多造成新手困擾與新對話斷線。  

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

> 涉及裁決：一律回到 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（A+）之裁決序。

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

> 這樣你得到「實務上只用一份」的效果，同時不違反 Only-Add。

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

> 你不用寫程式，只要維護 3 個 Markdown 檔案就能續編：

1) **TAITS_GPT_WORKLOG**：進度唯一事實來源（做到哪/下一步）  
2) **TAITS_GPT_ECR_LEDGER**：工作包帳本（一行索引每次工作）  
3) **TAITS_GPT_CONTEXT_PACK**：新對話必貼續編包（把上下文一鍵搬回來）

> 任何新對話，先讀 Worklog/Ledger，再貼 Context Pack。

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

> 你只要改三個欄位：任務類型／本次目標 doc_key／本次輸出要求。

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

> 你只要每次做完這三步，新對話一定接得上。

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

> 每次 Cursor 任務只做**單一層**，完成該層「最小交付一輪」：

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
> 你說檔案太多，這是最小集合（其餘可放 GitHub/Repo，不必全塞 GPT 專案）：

- AI_GOV（A+）
- DOCUMENT_INDEX（Authoritative Index）
- MASTER_ARCH
- MASTER_CANON
- GOVERNANCE_STATE（Freeze v1.0）
- 本合併手冊（本檔）

> 其他 SUPPORT/教學/附錄，可視需求放在 repo 但不必全部塞進 GPT 專案檔案池。

---

# APPENDIX｜三個 GPT 續編必備模板（可直接複製建立）

## Appendix 1｜TAITS_GPT_WORKLOG（模板）
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

## Appendix 2｜TAITS_GPT_ECR_LEDGER（模板）
```markdown
# TAITS_GPT_ECR_LEDGER（GPT 編輯工作包帳本｜Append-only）

| ecr_id | created_at | work_type | target_doc_key | target_file | insert_point | change_summary | ref_min_citation | gate_result | output_artifact | next_step |
|---|---|---|---|---|---|---|---|---|---|---|
| ECR-YYYYMMDD-0001 | YYYY-MM-DD HH:MM | ONLY_ADD_EDIT | <doc_key> | <file>.md | <位置> | 新增：... | ref_file=...; ref_doc_key=...; ref_version_date=...; ref_section=...; audit_anchor=... | N/A | <段落/檔> | 下一包：... |
```

## Appendix 3｜TAITS_GPT_CONTEXT_PACK（模板）
```markdown
# TAITS_GPT_CONTEXT_PACK（新對話續編包｜複製貼到新對話第一則）

（把本文件 A3 的續編包整段貼在這裡，並在每次工作包後 Only-Add 一段歷史快照）
```

---

（END）
