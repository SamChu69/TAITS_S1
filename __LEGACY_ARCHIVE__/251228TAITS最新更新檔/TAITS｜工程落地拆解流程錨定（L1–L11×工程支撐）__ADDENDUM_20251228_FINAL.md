# TAITS｜工程落地拆解流程錨定（L1–L11×工程支撐）__ADDENDUM_20251228_FINAL

> 文件定位：Engineering Translation Anchor（工程轉譯錨定檔）  
> 文件屬性：SUPPORT / Non-Governance（工程支援文件；**不具治理裁決效力**）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
> 版本日期：2025-12-28  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
> 編輯原則：Only-Add（只可新增；不得刪減／覆寫／偷換 Canonical 語義）  

---

## 0. Scope Lock（必讀｜避免誤用）

### 0.1 本文件**可以**做什麼
本文件僅用於：
- 將 TAITS Canonical（L1–L11）轉譯為 **Cursor 可編輯、可測試、可回放、可稽核** 的工程拆解與交付單元（工程層）
- 提供「新對話續編」之工程操作錨點（以工程紀錄為唯一事實來源，避免依賴對話記憶）
- 提供工程檔案結構、命名慣例、最小交付清單（Minimum Deliverables）與 Gate 對齊檢核清單

### 0.2 本文件**不得**做什麼（硬限制）
本文件**不得**被用來：
- 裁決 ACTIVE 文件集合、文件數量、doc_key 合法性、治理等級、版本有效性
- 改寫／重排 Canonical Flow（L1–L11）或任何治理文件之裁決順位
- 弱化或繞過 Risk/Compliance 否決權、Governance Gate、UI 義務、Audit 義務
- 以「工程便利」為理由偷換制度語義

> 涉及裁決（尤其：ACTIVE / doc_key / 位階 / 衝突 / 生效狀態）一律回到：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（A+）之裁決序。

---

## 1. 權威依據與引用規則（Index Gate First｜Freeze v1.0）

### 1.1 唯一裁決入口（Authoritative Index）
- **DOCUMENT_INDEX** 是治理有效文件的唯一裁決表：不在表內＝不具治理效力  
- 本文件僅引用 DOCUMENT_INDEX 中列為 ACTIVE 的文件作為工程轉譯依據（其餘視為無治理效力）

### 1.2 最小引用格式（AI_GOV 強制）
任何工程主張若依據某治理文件，必須附上最小引用欄位；缺一視為未引用、不得作裁決性輸出依據。

```text
〔TAITS 引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:<你的 CR / 變更錨點>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 引用標頭〕
```

### 1.3 Gate 衝突裁決順位（工程端必須可檢核）
若輸入或引用與下列順位衝突，工程 Gate 必須 BLOCK 並記錄 reason_code（含對應 doc_key）。

1) MASTER_ARCH  
2) AI_GOV  
3) DOCUMENT_INDEX  
4) MASTER_CANON  
5) RISK_COMPLIANCE  
6) ARCH_FLOW / FULL_ARCH  
7) UI_SPEC / VERSION_AUDIT / DATA_SOURCES / LOCAL_ENV / 其他

---

## 2. 名詞與識別碼（工程落地必備）

### 2.1 核心座標
- **Canonical Layer**：L1–L11（不可跳層／不可跨層合併）
- **工程交付單元（Engineering Unit）**：對應單一 Lx 的最小可驗證單元（可測、可回放、有證據）
- **ECR**（Engineering Change Record）：工程變更紀錄（工作單元紀錄；可對應 CR）
- **CR**（Change Request）：版本治理變更請求（VERSION_AUDIT 要求欄位）

### 2.2 Ops / Audit 識別碼（DEPLOY_OPS 對齊）
- **run_id**：一次執行單元（研究/回測/模擬/紙上/實盤 或 部署/回滾/演練）之主關聯鍵（必填、不可中途改寫）
- **trace_id**：細粒度鏈路追蹤鍵（多個 trace_id 對應同一 run_id；trace_id 必須可回溯 run_id）
- **artifact_id**：產物鍵（每個產物/快照/證據檔案的唯一識別）

---

## 3. Repo 檔案結構（Cursor 可編輯拆解｜工程層 Only-Add）

> 原則：治理文件原文只讀；工程輸出可回放；每層各自封裝；證據鏈可定位。

建議最小結構（可依語言/框架調整，但**不可破壞層邊界與證據鏈**）：

```
/docs/
  /governance/                  # ACTIVE 治理文件原文（只讀快照）
  /governance/_index/           # DOCUMENT_INDEX / README / BEGINNER_GUIDE（入口）
/engineering/
  /worklog/                     # ENGINEERING_STATUS.md（進度唯一事實來源）
  /ecr/                         # 每次工程變更一份 ECR（含引用標頭與 Gate 結果）
  /cr/                          # 需要治理級變更時：CR（依 VERSION_AUDIT 欄位）
  /gates/                       # Gate 執行紀錄（PASS/BLOCK/RETURN + reason_codes）
  /trace/                       # Trace / Evidence Chain 產物索引（run_id/trace_id/artifact_id）
/src/
  /l01/ ... /l11/               # 一層一目錄（不得跨層合併）
/tests/
  /l01/ ... /l11/
/ops/
  /runbooks/                    # 部署/回滾/停機/演練等 Runbook（對齊 DEPLOY_OPS）
```

---

## 4. 「17 部分」落地拆解總覽（最小可落地切割）

### 4.1 Canonical Runtime（11 部分｜一層一模組）
- L1 資料取得（Data Acquisition）
- L2 資料清洗（Cleaning / Normalization）
- L3 特徵／因子生成（Features / Factors）
- L4 訊號產生（Signal Generation）
- L5 組合／曝險建構（Portfolio / Exposure Construction）
- L6 Regime / Context（狀態辨識）
- L7 Risk / Compliance Gate（最高否決層；PASS / VETO）
- L8 執行前整備（Pre-Trade Prep；策略提案不得直連下單）
- L9 Governance Gate（流程完整性／引用合法性／回放一致性；PASS / BLOCK / RETURN）
- L10 決策裁決（Decision Template & Rationale；人類主權入口）
- L11 全紀錄／可回放（Audit / Evidence / Replay）

### 4.2 工程支撐面（6 部分｜橫向能力，貫穿 L1–L11）
12) Index Loader（治理束載入器：以 DOCUMENT_INDEX 為單一入口）  
13) Doc-key / Version Contract（引用與版本契約：最小引用格式＋Active Version Map）  
14) Gate Framework（PASS/BLOCK/RETURN/VETO 機制骨架＋reason_codes）  
15) Trace / Evidence Chain（證據鏈骨架：run_id/trace_id/artifact_id + 快照索引）  
16) Human-in-the-Loop UI Contract（UI 必填欄位與決策簽章）  
17) Ops / Deploy Runbook Contract（部署/回滾/停機/演練可稽核）

---

## 5. 每層（L1–L11）工程交付：Minimum Deliverables（Only-Add）

> 本節只定義「工程交付格式與檢核點」，不重述/改寫各層制度語義。各層語義以 MASTER_CANON / ARCH_FLOW 等上位文件裁決。

### 5.0 每層通用交付（所有 Lx 一律必備）
每個 Lx 工程模組**至少**產出以下 8 類交付物（可由同一產物承載，但不得缺項）：

1) `contracts/`：輸入/輸出資料契約（IO Contract）
2) `runner/`：該層可重跑入口（可在本機執行）
3) `artifacts/`：輸出產物（含摘要與必要快照）
4) `evidence/`：證據快照索引（指向 artifact_id）
5) `gate/`：該層 Gate 結果（PASS/BLOCK/RETURN 或 PASS/VETO）與 reason_codes
6) `version_ref/`：Active Version Map 引用（doc/policy/model/rulebook snapshots）
7) `trace_ref/`：run_id / trace_id / artifact_id 對應（可回溯）
8) `tests/`：最小可重跑測試（含固定種子/固定輸入快照）

### 5.1 L1（資料取得）工程交付要點
- 交付聚焦：資料來源連線與拉取的可重跑性、來源標識、時間戳與快照索引
- 必填：資料來源的 `source_id` / `snapshot_time` / `fetch_trace_id`（工程欄位；不得取代 doc_key）

### 5.2 L2（資料清洗）工程交付要點
- 交付聚焦：清洗規則可重跑、缺漏/異常處理留痕、輸出可驗證（hash）
- 必填：清洗前後摘要（行數/缺失率/異常統計）＋輸出 hash

### 5.3 L3（特徵/因子）工程交付要點
- 交付聚焦：特徵定義不可偷換、計算窗口與參數可追溯、特徵版本化
- 必填：feature_set_id / feature_version / 參數快照

### 5.4 L4（訊號）工程交付要點
- 交付聚焦：訊號生成規則可重跑、信號化與特徵的邊界明確、輸出不可直連下單
- 必填：signal_id / signal_confidence / 觸發條件快照

### 5.5 L5（組合/曝險）工程交付要點
- 交付聚焦：曝險計算、倉位建議與限制條件具可回放證據；輸出提供給 L7/L11
- 必填：exposure_snapshot / position_constraints / worst_case_assumptions（工程欄位）

### 5.6 L6（Regime/Context）工程交付要點
- 交付聚焦：regime_state 可重跑、狀態切換留痕、與策略適配只做映射不做裁決
- 必填：regime_state / regime_confidence / regime_inputs_snapshot

### 5.7 L7（Risk/Compliance Gate）工程交付要點（RISK_COMPLIANCE 對齊）
- 輸出固定為：`risk_gate_decision = PASS / VETO`
- 若 VETO：`veto_reason_codes[]` 必填，不可空
- 必填：Rulebook Snapshot（規則快照引用）＋ Evidence Bundle（證據束索引）

> 注意：Risk/Compliance 否決成立必須立即生效；不得以績效或緊急性推翻。

### 5.8 L8（執行前整備）工程交付要點
- 交付聚焦：策略提案、可用性與風險映射、執行約束；不得產生可直接送出委託之物件
- 必填：strategy_proposal_ref / pre_trade_constraints / execution_intent_candidate（僅候選）

### 5.9 L9（Governance Gate）工程交付要點（GOVERNANCE_GATE_SPEC 對齊）
- Gate 固定輸出：PASS / BLOCK / RETURN
- RETURN 必須包含：`missing_items[]`（缺口清單，讓工程可補齊）
- BLOCK 必須包含：reason_codes（含衝突 doc_key / ref_section）

### 5.10 L10（決策裁決）工程交付要點（UI_SPEC 對齊）
- 必須可呈現：L7 風控決策與原因碼、L9 Gate 結果、版本映射、證據可點開
- UI 必填輸出：
  - `human_decision`：APPROVE / REJECT / ABORT（禁止空白）
  - `human_decision_reason`
  - `ui_trace_ref`
  - `decision_signature`（user_id + timestamp + hash）

### 5.11 L11（全紀錄/可回放）工程交付要點（VERSION_AUDIT / DEPLOY_OPS 對齊）
- 交付聚焦：把 L1–L10 的輸入/輸出/版本/證據/決策完整打包成可回放束（Replay Bundle）
- Replay Bundle 至少包含：
  - active_version_map
  - run_id / trace_id 對應表
  - artifact index（含 hash）
  - gate decisions（L7/L9）
  - UI decision trace（L10）
  - replay instructions（如何重跑、用哪個入口）

---

## 6. 工程 Gate（落地實作規格｜只定義檢核，不重寫制度）

### 6.1 Index Gate（引用合法性 Gate）
- 檢核：ref_doc_key 是否存在於 DOCUMENT_INDEX 且狀態為 ACTIVE
- 不合格：RETURN（缺欄位可補）或 BLOCK（引用非法/衝突不可補）

### 6.2 Layer Gate（不跳層/不跨層合併 Gate）
- 檢核：本次變更是否只觸及單一 Lx（src/lXX 與 tests/lXX）
- 不合格：BLOCK（跨層會造成 Canonical 邊界破壞）

### 6.3 Risk Gate（L7 PASS/VETO）
- 檢核：若 VETO，必須中止後續執行鏈；不得「仍然繼續下游」  
- 不合格：BLOCK（重大違規）

### 6.4 Governance Gate（L9 PASS/BLOCK/RETURN）
- RETURN：列出 missing_items（工程補齊清單）
- BLOCK：列出 reason_codes（含衝突 doc_key / ref_section）

---

## 7. 變更治理（VERSION_AUDIT 對齊｜Freeze v1.0）

### 7.1 CR（Change Request）最小欄位（必填）
每個變更必須建立 CR，至少包含：
- change_id
- scope（doc/policy/rule/model/config）
- reason（禁止用「感覺更好」）
- risk_impact（影響哪些風控/合規/執行/UI）
- rollback_plan
- approver
- effective_time

### 7.2 回滾（Rollback）語義
- 回滾不是覆寫，而是切回舊版本為 Active（新增一筆切換事件）
- 回滾必須記錄：rollback_event_id / from_version / to_version / reason

---

## 8. 新對話續編：不依賴記憶的「工程續航三件套」

### 8.1 Minimum Load Set（新對話最小載入）
每次新對話開始，必須先確認（以 DOCUMENT_INDEX ACTIVE 為準）：
- AI_GOV
- DOCUMENT_INDEX
- MASTER_ARCH
- MASTER_CANON
- GOVERNANCE_STATE（狀態宣告與限制）

### 8.2 進度唯一事實來源（Worklog）
- `engineering/worklog/ENGINEERING_STATUS.md` 為唯一進度事實來源  
- 每次完成一個 Engineering Unit（單一 Lx）必更新：完成度、輸出 artifact_id、Gate 結果、對應 ECR/CR

### 8.3 新對話開場模板（可直接貼）
```text
已進入嚴格對齊模式（Freeze v1.0 / Only-Add / 不跳層）。

〔TAITS 引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <本次用途>
audit_anchor = VERSION_AUDIT:<change_id 或變更錨點>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 引用標頭〕

本次工作定位：
- Canonical Layer = <Lx>
- Engineering Unit = <一句話交付物>
- 續編依據（Worklog）= engineering/worklog/ENGINEERING_STATUS.md（最新條目：<ID/日期>）
```

---

## 9. Cursor 任務切片（Task Slicing）標準（最大穩定、最低漂移）

### 9.1 一個 Cursor 任務只做一件事
- 只做單一 Lx 的最小交付（Minimum Deliverables 完成一輪）
- 同步補齊該層 Gate 輸出與證據鏈索引（便於 L11 回放）

### 9.2 Cursor 任務開工 Prompt（可直接貼）
```text
〔TAITS Cursor 工程任務｜Freeze v1.0｜Only-Add〕
硬性約束：
1) 僅能依 docs/governance 內 ACTIVE 文件作依據；引用必帶 ref_file/ref_doc_key/ref_version_date/ref_section/audit_anchor。
2) Only-Add：不可刪減、不可覆寫、不可偷換語義。
3) 嚴格層級邊界：本次只允許修改 /src/lXX/** 與 /tests/lXX/**（XX = 指定層）。
4) 先建立 engineering/ecr/ECR-<id>.md，首段貼上引用標頭，並填入本次依據。
5) 完成後輸出 Gate 結果（Index/Layer/Risk/Gov）與 artifact_id 索引。

本次目標：
- Layer = LXX
- Deliverable = <一句話交付物>
〔/TAITS Cursor 工程任務〕
```

### 9.3 完工前自檢（Pre-merge Checklist）
- Index Gate：引用標頭欄位是否齊全？doc_key 是否為 ACTIVE？
- Only-Add：是否存在刪除/覆寫/語義替換？
- Layer Gate：是否只改動單一層目錄？
- Audit：是否生成 run_id/trace_id/artifact_id 對應與可回放證據？
- UI（若涉及 L10）：是否輸出 human_decision / decision_signature / ui_trace_ref？

Fail 任一條：停止，提出最小修補方案（只增補、不重構）。

---

## 10. 演進規則（Only-Add｜Freeze v1.0）

允許：
- 新增工程轉譯層章節、補充 Checklist、增加 reason_codes 表、補充 schema 範本
- 新增更多「工程交付模板」（ECR/CR/worklog）以提升可回放性

禁止：
- 刪除既有段落
- 重寫裁決順位或改寫 Canonical 定義
- 把本文件升格為治理裁決文件（除非經 DOCUMENT_INDEX 納管且仍保持 SUPPORT）

---

## Appendix A｜建議的工程產物命名（可回放友善）

- ECR：`engineering/ecr/ECR-YYYYMMDD-####.md`
- CR：`engineering/cr/CR-YYYYMMDD-####.md`
- Gate log：`engineering/gates/{run_id}/{layer}/gate_result.json`
- Artifacts：`engineering/trace/{run_id}/{layer}/{artifact_id}/*`
- Replay Bundle：`engineering/trace/{run_id}/replay_bundle.zip`（或資料夾）

> 以上命名為工程建議；不得與治理 doc_key 概念混淆。
