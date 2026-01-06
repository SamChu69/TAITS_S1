# TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）

- doc_key：GOVERNANCE_GATE_SPEC  
- 基線日期：2026-01-06（Asia/Taipei）  
- 覆蓋輸出：單一正確正文版／最終覆蓋版（FINALQA）  
- 去混讀狀態：已收斂（正文不含 Addendum／Appendix／Freeze 補丁語句；留痕僅於檔尾稽核區塊）  
- 強制定錨：Regime／Risk／Compliance 高於策略；L9=投資報告；L10=人類裁決；L11=全層稽核回放（非下單層）  
- 治理裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  

---
doc_key：GOVERNANCE_GATE_SPEC  
治理等級：B（治理／制度級｜治理閘門與裁決規範）  
適用範圍：TAITS 全系統（治理閘門 Gate 定義／裁決模型／通過/阻擋/退回條件／衝突裁決／升級路徑／裁決留痕／UI 呈現義務／引用合法性）  
版本狀態：ACTIVE（單一正確正文版｜最大完備＋累積式更新｜可直接覆蓋）  
版本日期：2026-01-06（Asia/Taipei）  
最終裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
本檔定位：B 級制度規範（受最終裁決序位約束；不得與上位裁決衝突）  
平行參照：RISK_COMPLIANCE／VERSION_AUDIT／EXECUTION_CONTROL／UI_SPEC／MASTER_CANON／FULL_ARCH／ARCH_FLOW／DATA_SOURCES／TWSE_RULES／DEPLOY_OPS／LOCAL_ENV  
核心裁決模型：Binary Gate（PASS / BLOCK / RETURN）＋ Traceability First（可追溯優先）  
變更原則：最大完備＋累積式更新（允許融合更新／覆寫修正／重排版以形成單一正確正文；禁止摘要化縮水；未被新版本明確取代之有效內容一律保留並持續累積；已被新版本明確取代者可自正文移除但必須由稽核留痕承接）

---

## 0. 文件定位（Governance Gate Charter｜治理閘門憲章）

本文件定義 TAITS 在 Canonical Flow 中的「治理閘門（Governance Gate）」與「衝突裁決（Arbitration）」制度規格，以確保：

- 任何流程推進皆有明確、可稽核的治理邊界（不可繞過）
- 任何衝突處理皆可追溯、可回放（由 L11 承接回放；L11 非批准/下單層）
- Risk / Compliance（風控與合規）最高否決權可被正確承接與呈現（不得被 Gate 程序稀釋）
- L9 投資報告與 L10 人類裁決具備一致的引用、版本與留痕規格（避免新舊混讀與語義漂移）

本文件用於定義：

- 什麼情況下流程可以前進（PASS）
- 什麼情況下流程必須被阻斷（BLOCK）
- 什麼情況下流程必須退回補齊（RETURN）
- Gate 的裁決權位階、優先序、衝突解決與保守處置
- Gate 必須輸出的審計／回放（Audit / Replay）證據
- Gate 在 UI 的呈現義務（不可模糊、不可遮蔽）
- Gate 與 Risk / Compliance（風控與合規）之邊界與協作方式

本文件明確不負責（避免越權）：

- 不定義 Canonical Flow（L1–L11）層級順序（由 MASTER_CANON / ARCH_FLOW 裁決）
- 不定義風控與合規條文、否決原因碼全集（由 RISK_COMPLIANCE / TWSE_RULES 裁決）
- 不定義下單通道、券商/撮合細則（由 EXECUTION_CONTROL 裁決）
- 不定義策略內容、參數、績效敘事（由 STRATEGY_UNIVERSE 裁決）
- 不產生交易方向、不承諾績效、不形成下單權

---

## 1. 全局語義定錨（S1｜跨文件一致｜單一口徑）

> 本章為本檔之語義定錨；若跨文件出現不同口徑，一律依最終裁決序位（DOCUMENT_INDEX → MASTER_ARCH → AI_GOV）裁決，並由 DOCUMENT_INDEX 的衝突裁決程序承接。

- 本文件為單一正確正文版；任何歷史狀態標記不構成正文裁決依據（以 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV 為準；本檔受其約束）。  
- **Risk / Compliance 具最高否決權**：即使治理閘門通過，仍可於後續層級被否決。  
- L9＝投資報告層（含數據/價格/圖形/條件式進出場價格建議〔非指令〕/風險敘述/可追蹤更新欄位）  
- L10＝人類裁決與交易決策層（唯一交易授權入口）  
- L11＝全層工程稽核回放層（L1–L11 全留痕），且 L11 非下單層  

### 1.1 人類最高決策者主權（SOVEREIGNTY）
- TAITS 之最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令之生效。
- Gate 的使命是保護「流程完整性、引用合法性、可追溯性、可回放性」，而非取代人類裁決。

### 1.2 L9–L11 終局語義（跨文件一致）
- **L9（投資報告層）**：可追蹤、可更新、可標的化投資報告；必含數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源），並支援事件驅動滾動更新。
- **L10（人類裁決層）**：由人類最高決策者裁決不動作/回測/模擬/紙上/實盤，以及手動/半自動/全自動授權模式；任何交易型態皆以 L10 明確裁決為準。
- **L11（工程稽核回放層）**：對 L1–L11 全層輸入/處理/輸出/裁決/執行鏈路留痕，供人類與工程端可讀、可查、可回放；L11 非下單決策層，亦不得被誤讀為批准入口。

### 1.3 禁止 AI 自行批准與禁止把 L11 當批准/下單層（Hard）
- AI/Agent/LLM 不具批准權；不得輸出任何等同 PASS/APPROVE/放行執行之裁決語義。
- 不得以「已記錄/已回放/已完成 L11」暗示已批准；批准僅能在 L10 由人類裁決。

### 1.4 HFI｜人類明確命令（可執行觸發）
- 有效 HFI 存在時：Gate 與治理流程不得阻擋其 scope 範圍內之融合更新／覆寫修正／重排版，但必須同步產出稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。
- Gate 對 HFI 的最低義務：清晰呈現 scope、風險揭露、可回放紀錄與版本引用；不得以程序性理由「卡死」更新。

---

## 2. Gate 裁決模型與硬性邊界（Hard Gates｜不可動搖）

### 2.1 Gate 的法律定位
- Gate 為「治理層裁決」，目的在於確保：
  - 流程不可跳步（L1–L11 不可跳層）
  - 引用合法（doc_key 必須在 DOCUMENT_INDEX 且為唯一 ACTIVE）
  - 證據可追溯（Evidence 可回放、可稽核）
  - 版本一致（version_ref 不可缺漏、不可互斥混用）
  - 人類主權不可被取代（Human-in-the-Loop）

### 2.2 Gate 輸出僅允許三態（Binary Gate + Return）
Gate 輸出僅允許：
- `PASS`：允許進入下一層
- `BLOCK`：阻斷流程（治理否決；不可繼續）
- `RETURN`：退回補齊（不是放行；補齊後必須重新進 Gate）

禁止：
- 模糊放行（Soft Pass）
- 條件通融（Conditional Pass）
- 以備註取代裁決狀態
- 以「推測補值」修補缺失引用或缺失證據

### 2.3 「無審計＝未發生」（Audit-First）
- Gate 若缺少必要審計物（Artifacts），該 Gate 視為未執行。
- 未執行 Gate 的流程結果：治理違規（GOV-*）→ 必須 BLOCK（或 RETURN 退回補齊；依缺口是否可補）。

### 2.4 Risk / Compliance 最高否決權不受 Gate 影響
- Gate 不是風控；Gate 不得弱化風控。
- RISK_COMPLIANCE 之 VETO 高於一切（含 Gate、策略、人類執行意圖）。
- Gate 的作用是保證：該有的證據、版本、引用、流程完整性都存在，並且可回放。

### 2.5 Gate 不取代人類裁決
- Gate 不做「買/賣」裁決。
- Gate 不做「是否值得交易」裁決。
- Gate 做的是：「是否允許進入下一步」的制度裁決。
- L10（Human Decision）仍是唯一的人類裁決與授權節點。

---

## 3. Gate 在 Canonical Flow 的定位（Primary Gate + Sub-Gates）

### 3.1 Gate 的兩層形態
1) **主 Gate（Primary Governance Gate）**  
- 對應 Canonical Layer（被檢核對象）：**L9（投資報告層）**
- Gate 本體定位：**non-layer（治理檢核機制）**
- 目的：在進入 L10（Human Decision）之前，完成「全鏈路一致性裁決」與「證據/版本/引用合法性裁決」。

2) **子 Gate（Sub-Gates / Checkpoints）**  
- 分布於 L1–L11 各層（以檢核點形式存在）
- 目的：每層完成最低治理義務（Evidence Completeness、Version Ref、Audit、可回放索引等）

注意：子 Gate 不得改寫 主 Gate（對 L9 投資報告） 的裁決語義；只提供可稽核的檢核結果。

### 3.2 主 Gate（Primary Governance Gate｜對 L9 投資報告）輸入（Inputs｜不可缺）
- `correlation_id` / `session_id`
- `documents_active_map_ref`：當下生效文件快照（以 DOCUMENT_INDEX 裁決）
- `layer_artifacts_map_ref`：L1–L8 各層審計物索引
- `evidence_bundle_ref`（L5）
- `regime_state_ref`（L6）
- `risk_gate_ref`（L7：PASS/VETO + reason codes 引用）
- `strategy_proposal_ref`（L8：僅建議，不含下單權）
- `ui_trace_ref_pre_human`（供 UI_SPEC 對位）
- `version_ref`：doc/policy/model/rule snapshot（不可缺）

### 3.3 主 Gate（Primary Governance Gate｜對 L9 投資報告）輸出（Outputs｜最小集合）
- `governance_gate_decision`：PASS / BLOCK / RETURN
- `gate_reason_codes[]`：若非 PASS 必填
- `return_required_items[]`：若 RETURN 必填（具體補齊清單）
- `governance_artifact_ref`：主 Gate 審計物引用
- `replay_bundle_ref`：回放包引用（或其組裝索引）

---

## 4. Gate 責任邊界（Boundary Map｜避免重疊與越權）

### 4.1 Gate 負責
- 流程完整性裁決（No Skip）
- 文件引用合法性裁決（doc_key / ACTIVE / 唯一性）
- 證據完整性裁決（Evidence 可回放、可追溯）
- 版本一致性裁決（version_ref / policy_version / rule snapshot）
- 審計完整性裁決（Artifacts / Hash / Correlation）
- 人類裁決前的資訊呈現義務裁決（UI Must-Show）

### 4.2 Gate 不負責
- 不裁決合規條文（由 RISK_COMPLIANCE / TWSE_RULES）
- 不裁決策略勝率與績效（禁止績效辯護）
- 不裁決交易方向（Human 才可裁決是否執行）
- 不改寫 Canonical Flow（由 MASTER_CANON / ARCH_FLOW）
- 不改寫上位母法（AI_GOV / MASTER_ARCH / DOCUMENT_INDEX）

---

## 5. 衝突裁決與保守處置（Priority & Conflict Resolution）

### 5.1 裁決依據與順位（以 DOCUMENT_INDEX 為主）
- 治理等級覆蓋與衝突裁決程序，以 DOCUMENT_INDEX（Authoritative Index）為準。
- 本文件內任何「順位字串」皆屬閱讀助記（Mnemonic），不得被誤讀為覆蓋規則或裁決權重新分配。
- 凡涉及「AI 行為／AI 參與裁決邊界／AI 可不可補完／AI 可不可越權」：一律受 AI_GOV（A+）最高約束，不得以任何順位字串降格 AI_GOV 的覆蓋地位。

### 5.2 衝突類型
- **硬衝突（Hard Conflict）**：定義互斥、語義矛盾、優先序不可調和 → BLOCK
- **缺口衝突（Gap Conflict）**：非矛盾但缺少必備證據/引用 → RETURN（可補齊）

### 5.3 Gate 進行衝突裁決之最小程序（不可跳步）
1) **Index Gate（合法性）**：確認引用的 doc_key 存在於 DOCUMENT_INDEX 且為該 doc_key 唯一 ACTIVE  
2) **治理等級覆蓋**：套用 DOCUMENT_INDEX 定義之覆蓋規則（A+ > A > B > C）  
3) **同級衝突**：依 DOCUMENT_INDEX 的衝突裁決程序採保守裁決；仍無法裁決則 STOP（不可通融）  
4) **稽核留痕**：若屬 Metadata Discrepancy 或需固定解釋口徑，必須在 VERSION_AUDIT 留存（METADATA_FIX 或等價類型）

---

## 6. 引用合法性與可回放最小格式（Citation / Trace / Evidence）

### 6.1 文件身份與引用合法性（Canonical Identity）
- 本文件唯一治理身份：`doc_key = GOVERNANCE_GATE_SPEC`
- 本文件實體檔名（本次正文版）：`TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__260106.md`
- 工程層引用必須以 `doc_key` 為主；檔名只作物理載體，不得用相近檔名替代治理身份。

### 6.2 子級標籤（Label）之唯一合法解讀（S / B+ / C+）
- `S`、`B+`、`C+` 等字樣一律視為顯示標籤（Label）或完備度標示，不構成新的治理等級 bucket。
- 治理覆蓋規則固定以 DOCUMENT_INDEX 為準，不得由 Label 改寫。

### 6.3 DATA_UNIVERSE（alias）封口（資料治理引用回歸 DATA_SOURCES）
- 凡出現 `DATA_UNIVERSE` 一律視為概念別名（alias），不得作為 doc_key。
- 任何需要引用資料來源治理時，唯一合法 doc_key：`DATA_SOURCES`。
- 若 Gate / Evidence / Audit / UI Trace 引用欄位出現 `doc_key=DATA_UNIVERSE`：一律視為引用非法 → BLOCK 或 RETURN（依可補性），不得以推測補救。

### 6.4 最小可稽核引用格式（Minimum Legal Citation Format）
凡聲稱「依據治理文件」之輸出（含：Evidence、Risk/Compliance、Governance Gate、UI Decision、Execution Control、Audit）一律必須同時提供：

```text
ref_doc_key = <DOC_KEY>
ref_file = <完整檔名>
ref_version = <版本日期或檔名日期碼>
ref_section = <章節定位（§ / Heading Path）>
ref_purpose = <用途：例如 gate_check / risk_veto / ui_decision / execution_policy / audit_replay>
ref_notes = <可選：alias/Label 解讀備註>
```

缺任一欄位：依 DOCUMENT_INDEX 採保守處置（RETURN 或 BLOCK），不得形成裁決性輸出（PASS/APPROVE/EXECUTE 等）。

### 6.5 Trace ID / Evidence Chain 最小欄位（對齊 DEPLOY_OPS）
#### EC1. 最小引用標頭（Minimum Legal Citation Header）
```text
trace_id = <全域唯一>
session_id = <本次對話/流程>
event_id = <本次事件/操作>
actor = <human/agent/module>
timestamp = <ISO-8601>
doc_key = GOVERNANCE_GATE_SPEC
doc_title = TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__260106.md
ref_version_date = 2026-01-06
ref_section = <章節/段落路徑>
audit_anchor = VERSION_AUDIT:<對應條目（若有）>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
```

#### EC2. Evidence Chain 最小結構（Minimum Evidence Chain）
當本文件涉及「可回放產物」或「稽核必需證據」時，Evidence Chain 至少包含：
- `env_fingerprint`（環境指紋）
- `dependency_manifest`（依賴清單）
- `run_evidence`（執行證據：命令/時間/產物/日誌）
- `failure_recovery`（失敗與回復：PASS/FAIL 與處置）

欄位定義與格式以 DEPLOY_OPS 為準；本節僅宣告「必帶」與「缺失之保守處置」。

#### EC3. 缺欄位之保守處置
- 若缺少 EC1/EC2 最小欄位：不得視為可回放/可稽核輸出。
- 涉及風險/合規裁決時：依 RISK_COMPLIANCE 與本文件之保守處置機制，採 RETURN/BLOCK 以補齊引用資訊（不得以推測補值）。

---

## 7. Gate 規則全集（Rulebook｜最大完備）

> Gate 規則以「必備檢核」方式定義。任何命中 → 依規則輸出 PASS/BLOCK/RETURN。  
> 允許擴充規則，但禁止弱化本節既有規則之語義與強度。

### 7.1 必備檢核 A：流程完整性（FLOW Integrity）
- A1：L1–L8 層級審計物齊全（layer_artifacts_map_ref 完整）
- A2：存在合法 L5 Evidence 與 L6 Regime 引用（evidence_bundle_ref / regime_state_ref）
- A3：若曾 RETURN，必須看見補齊項目已完成之證據（return_required_items 對位）
- A4：不同模式不得降低 Gate 覆蓋（No Downgrade）

裁決：
- 缺任何 A* → RETURN（若可補）或 BLOCK（若不可補/矛盾）

### 7.2 必備檢核 B：文件引用合法性（DOCUMENT_INDEX Compliance）
- B1：所有引用 doc_key 必須存在於 DOCUMENT_INDEX
- B2：引用文件狀態必須 ACTIVE
- B3：doc_key 唯一性與版本引用一致性（不可含糊、不可多版混用）
- B4：上位/平行參照不得互相矛盾（硬衝突必 BLOCK）

裁決：
- 命中 B1/B2/B3（引用非法）→ BLOCK
- 命中 B4：硬衝突 → BLOCK；缺口 → RETURN

### 7.3 必備檢核 C：審計可回放（AUDIT/REPLAY）
- C1：correlation_id / session_id 完整
- C2：hash 鏈（input/output）可驗證（不可事後補寫）
- C3：回放包（Replay Bundle）可組裝，且指向不可變儲存
- C4：審計物可讀/可取回（可回放）

裁決：
- C1 缺 → RETURN（若可補）
- C2/C3/C4 缺 → BLOCK（不可在裁決後補）

### 7.4 必備檢核 D：版本一致性（VERSION Alignment）
- D1：所有輸出都帶 version_ref（doc/policy/model/rule snapshot）
- D2：policy_version 可在 VERSION_AUDIT 回溯
- D3：制度/規則快照可在 TWSE_RULES 或 rule snapshot 引用中找到
- D4：同一 correlation_id 不可混用互斥版本

裁決：
- D1 缺 → RETURN（若可補）
- D2/D3/D4 缺 → BLOCK（不可用不可信版本裁決）

### 7.5 必備檢核 E：UI 呈現義務（UI Must-Show）
- E1：Risk Gate 結果（PASS/VETO）與 reason codes 必須可視化（不可遮蔽）
- E2：version_ref / correlation_id 必須可視化
- E3：RETURN 時補齊清單必須可視化且阻斷前進
- E4：不得以績效圖表弱化風險揭露（風險揭露優先）

裁決：
- 命中任一 E* → BLOCK（屬治理違規）

### 7.6 必備檢核 F：安全與旁路防護（Bypass Prevention）
- F1：不得存在繞過 Risk 或 Gate 的旁路通道（暗通道）
- F2：敏感資訊不得被寫入不允許位置（依 LOCAL_ENV）
- F3：不得以「效能／便利」理由移除審計/回放/對帳鏈路

裁決：
- 命中任一 F* → BLOCK

---

## 8. Gate 裁決原因碼（Gate Reason Codes｜最大完備）

格式：`GOV-[Domain]-[Number]`  
Domain：FLOW（流程）/ DOC（文件）/ AUD（審計）/ VER（版本）/ PROV（追溯）/ UI（介面）/ SAFE（安全）/ SCOPE（範圍）

### 8.1 FLOW（流程完整性）
- GOV-FLOW-01：跳層或未執行必要層（違反 L1–L11）
- GOV-FLOW-02：非法回寫（Layer 回寫策略/結論）
- GOV-FLOW-03：RETURN 後未補齊即重入後層
- GOV-FLOW-04：模式降級（降低 Gate 密度或省略必備審計）

### 8.2 DOC（文件引用合法性）
- GOV-DOC-01：引用不存在於 DOCUMENT_INDEX 的 doc_key
- GOV-DOC-02：引用文件狀態非 ACTIVE（DEPRECATED/ARCHIVED 等）
- GOV-DOC-03：doc_key 不唯一或版本引用不唯一
- GOV-DOC-04：文件關係宣告（上位/平行）互相矛盾
- GOV-DOC-05：以 Label / 別名取代 doc_key（例如 DATA_UNIVERSE）

### 8.3 AUD（審計完整性）
- GOV-AUD-01：缺 correlation_id / session_id / layer_id
- GOV-AUD-02：缺 layer_artifacts（任一層缺審計物）
- GOV-AUD-03：hash 不一致（input_hash/output_hash 驗證失敗）
- GOV-AUD-04：審計物不可讀/不可取回（不可回放）
- GOV-AUD-05：疑似事後回填審計（Audit Backfill）

### 8.4 VER（版本一致性）
- GOV-VER-01：version_ref 缺漏（doc/policy/model/rule snapshot）
- GOV-VER-02：policy_version 不可追溯（VERSION_AUDIT 不存在）
- GOV-VER-03：制度/規則快照缺失（TWSE/TAIFEX 等）
- GOV-VER-04：同一 correlation_id 版本參照互相矛盾

### 8.5 PROV（來源追溯）
- GOV-PROV-01：Evidence provenance 斷裂（來源不可追溯）
- GOV-PROV-02：使用非官方來源作裁決依據（可補充不可裁決）
- GOV-PROV-03：資料時間戳不一致或交易日判定可疑（需 RETURN 或 BLOCK）

### 8.6 UI（介面呈現義務）
- GOV-UI-01：UI 未顯示 Risk Gate 結果或 reason codes（遮蔽風險）
- GOV-UI-02：UI 未顯示必要版本引用（version_ref 不可見）
- GOV-UI-03：UI 未顯示 RETURN 補齊清單而允許繼續
- GOV-UI-04：UI 以模糊措辭取代裁決（PASS/BLOCK/RETURN）

### 8.7 SAFE / SCOPE（安全與範圍）
- GOV-SAFE-01：敏感資訊疑似外洩或被寫入不允許位置（LOCAL_ENV 違反）
- GOV-SAFE-02：疑似繞過 Gate / Risk 的旁路通道（暗通道）
- GOV-SCOPE-01：Scope 宣告與實際輸出不一致（超範圍寫入/超範圍執行）

---

## 9. Gate 與 Risk Gate（L7）關係（Two-Gate Model）

### 9.1 本質差異
- **Risk Gate（L7）**：裁決「可不可以交易」（PASS/VETO），具最高否決權。
- **Governance Gate（對 L9 投資報告）**：裁決「流程與證據是否具備合法性、可追溯性、可回放性」。

### 9.2 協作規則（不可顛倒）
- L7 若 VETO：
  - 治理閘門不得以任何理由放行；
  - 治理閘門僅能完成完整記錄、回放包封存、reason codes 與版本引用的治理義務（不構成放行）。
- L7 若 PASS：
  - 治理閘門仍可因治理缺陷 BLOCK/RETURN（例如缺版本、缺審計、引用非法、UI 遮蔽）。

---

## 10. Gate 審計輸出（Audit Artifacts｜不可縮減）

### 10.1 Governance Gate Artifact（最小欄位）
- `correlation_id`
- `session_id`
- `layer_id = L9`（注意：此 layer_id 表示被檢核對象之報告層級；不代表 Gate=Layer）
- `decision`（PASS/BLOCK/RETURN）
- `gate_reason_codes[]`
- `documents_active_map_ref`
- `layer_artifacts_map_ref`
- `evidence_bundle_ref`
- `regime_state_ref`
- `risk_gate_ref`
- `strategy_proposal_ref`
- `ui_trace_ref_pre_human`
- `version_ref`
- `input_hash`
- `output_hash`
- `created_at_utc`

### 10.2 RETURN 的補齊清單（必填）
- `return_required_items[]` 必須具體到「缺哪個引用／缺哪個 artifact／缺哪個版本」。
- 禁止模糊詞（例如：補資料、再看看、可能不足）。

---

## 11. UI 呈現義務（Gate 專屬 Must-Show）

UI 詳規由 UI_SPEC 管；本節定義 Gate 必須交付 UI 的硬欄位。

UI 必須顯示：
- 主 Gate 決策：PASS / BLOCK / RETURN（不可模糊）
- gate_reason_codes（可展開）
- 若 RETURN：補齊清單（可勾選/追蹤進度）
- correlation_id（可稽核）
- documents_active_map（可點開檢視版本）
- risk_gate 決策與 reason codes（不可遮蔽）
- version_ref（doc/policy/model/rule snapshot）

禁止：
- 以「建議」「注意」「可能」取代裁決
- 允許使用者在 RETURN/BLOCK 狀態進入 L10（Human Decision）
- 在 UI 隱藏 Gate 的原因碼或版本引用

---

## 12. Mermaid｜治理 Gate 全流程圖（含 RETURN/BLOCK）

```mermaid
flowchart TB
  A[L8 Strategy Proposal<br/>(Non-binding)] --> B[L9 Investment Report<br/>(Report Layer)]
  B --> G[Governance Gate<br/>(non-layer check on L9 report)]

  G -->|PASS| C[L10 Human Decision<br/>(Only trade authorization entry)]
  G -->|RETURN| R[Return to Required Layer(s)<br/>+ Required Items List]
  G -->|BLOCK| X[STOP<br/>Preserve Evidence + Audit Artifact]

  R --> D[L4/L5/L6補齊<br/>Evidence/Regime/Artifacts]
  D --> B

  C -->|NO_ACTION| Y[STOP + Audit]
  C -->|BACKTEST/SIMULATION/PAPER/LIVE| E[Execution Control<br/>(Module, not a layer)]
  E --> F[L11 Audit & Replay<br/>(Replay only, not approval)]
```

---

## 13. 禁止事項（Forbidden｜一票否決）

- 任何形式跳過 **治理閘門檢核（對 L9 投資報告）** 直接進入 L10/L11
- 任何形式跳過 **L9 投資報告層**（直接進入 L10）或以其他層輸出冒充 L9 報告
- 任何形式 Gate 決策模糊化，或 UI 遮蔽 reason codes
- 任何形式引用未在 DOCUMENT_INDEX 的文件作裁決
- 任何形式缺審計/缺 hash/缺版本引用仍放行
- 任何形式以績效辯護要求 Gate 放行
- 任何形式事後補審計或回填裁決
- 任何形式旁路通道繞過 Risk 或 Gate（暗通道）
- 任何形式 AI/Agent 自行批准或暗示批准

---

## 14. 演進規則（本文件專屬｜最大完備＋累積式更新）

允許新增（可擴充）：
- 新的 Gate 規則（Rules）
- 新的 gate_reason_codes
- 新的審計欄位（Artifact fields）
- 新的 UI Must-Show 欄位
- 新的回放包視角（Replay Views）

禁止（不得降級）：
- 刪除或弱化 PASS/BLOCK/RETURN 的裁決語義
- 刪除或弱化引用合法性檢核（DOCUMENT_INDEX Compliance）
- 以效能理由省略審計、回放、版本引用、hash 鏈
- 允許在任一模式降級 Gate 覆蓋密度（No Downgrade）
- 以推測補值補齊缺失證據或缺失引用

---

## 15. 工程端本地運算環境基線（參照｜不構成治理強制）

> 本節為工程端環境資訊之「固定基線參照」，用於避免工程溝通中對硬體條件重新腦補。  
> 若與 LOCAL_ENV 有衝突，以 LOCAL_ENV 裁決為準。

- 裝置：ASUS FX504GE（筆電）
- 作業系統：Windows 11
- CPU：Intel Core i7-8750H（6C/12T）
- 記憶體（RAM）：32GB（已升級）
- GPU：NVIDIA GeForce GTX 1050 Ti
- GPU VRAM：4GB
- 儲存：256GB SSD + 750GB HDD（依實際可用空間調整）
- 建議本地推理定位（在此硬體條件下）：
  - 優先：L11 稽核摘要、L1/L2 抽取與欄位化、L5 證據包整理（使用 3B–7B 量化模型）
  - 不建議本地硬扛：高品質長篇 L9 報告主力、重推理整合（可採雲端主力＋本地稽核/抽取池）

---

## 16. 終極裁決語句（固定口徑）

沒有可追溯的證據與版本，就沒有合法的決策。  
沒有合法的決策，就不允許進入人類裁決與執行層。

---

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 修正：將文件內「治理裁決序位」表述統一收斂為唯一箭頭鏈口徑：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。
- 修正：本檔若引用其他治理文件檔名，統一指向現行覆蓋輸出檔名（優先 __CLEAN_260107）。
- 修正：若原檔存在稽核區塊或補丁式標記，已以 Legacy Snapshot 承接於檔尾稽核區塊，避免正文／稽核邊界混讀。
- 保留：GOVERNANCE_GATE_SPEC 全文條款全量承接，不做摘要縮水；僅做去混讀與引用一致化。


### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：16e80e1889673e0f2d9c7fb9dcad0cb0d7a8aa38f8bf92b0799e3d56ba43b0cb
- LEGACY_AUDIT_SHA256：9b8cc44b03faeb29bb03db5946db913066953fa411019a935eabee5c7d6de487

### 3) 適用範圍（Scope）
本次覆蓋版修正範圍僅限於 doc_key=GOVERNANCE_GATE_SPEC：
- 治理裁決序位表示法一致化（箭頭鏈口徑）
- 正文／稽核邊界去混讀（檔尾稽核區塊固定化；既有稽核內容以 Legacy Snapshot 承接）
- 引用檔名一致化（僅更新本檔提及之檔名字串；不修改其他 doc_key 正文內容）


### 4) 裁決承接（Audit Hand-off）
- 本檔為 GOVERNANCE_GATE_SPEC 現行唯一可引用正文。
- 治理閘門裁決規範之任何條款變更，必須同步更新 MASTER_CANON（Canonical Flow）與 RISK_COMPLIANCE（否決權承接）之對應承接語句，以維持單一口徑。
- 若與其他治理文件存在衝突，裁決序位固定為：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。


### Legacy Audit Snapshot（被本次覆蓋版承接／非正文）

> # 稽核區塊（Audit Section｜非正文）
> 
> > 本區塊為「本次更新」之留痕（Changelog／Hash Manifest／Scope／Audit Hand-off）。  
> > 為避免新舊混讀：本區塊不參與正文裁決；正文以本檔案開頭至本區塊前之內容為準。
> 
> ## A. Scope（適用範圍）
> - doc_key: GOVERNANCE_GATE_SPEC
> - version_date: 2026-01-06（Asia/Taipei）
> - applies_to: TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
> - governance_order_applied: DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
> - semantic_anchor_enforced:
>   - L9＝投資報告層（投資報告，含數據/圖形/條件式進出場建議〔非指令〕/風險敘述/追蹤欄位）
>   - L10＝人類裁決與交易決策層（唯一交易授權入口）
>   - L11＝全層工程稽核回放層（L1–L11 全留痕；非下單層）
> - gate_positioning_note:
>   - Governance Gate 為 non-layer 治理檢核機制（主要作用於 L9 報告進入 L10 之前；不得被誤讀為 L9=Gate）
> 
> 版本日期：2026-01-06（Asia/Taipei）
> 
> ## B. Changelog（變更清單）
> 1) **語義定錨收斂**：修正「主 Gate＝L9」之層級綁定語句，明確化 Governance Gate 為 non-layer 檢核機制（主要作用於 L9 投資報告進入 L10 之前），以符合本對話強制定錨（L9=投資報告、L10=人類裁決、L11=稽核回放）。  
> 2) **去混讀重排版**：合併重複的文件定位/metadata 段落，章節依序排列，避免同檔自撞與跨段落混讀。  
> 3) **流程圖一致化**：更新 Mermaid 圖中 L9/L10/L11 與 Gate/Execution Control 之標示，避免把 Gate 或 Execution 誤綁為 Canonical Layer。  
> 4) **指紋同步**：更新 Hash Manifest（BODY_ONLY）以對齊本次覆蓋輸出正文。
> 
> 5) **Final QA 基線一致化（260106）**：版本日期統一為 2026-01-06（Asia/Taipei），並新增稽核區塊父層標題以強化「非正文」邊界，降低混讀風險。  
> 
> ## C. Hash Manifest（指紋清單）
> - hash_alg: sha256
> - scope: BODY_ONLY（不含本稽核區塊）
> - hash_value_sha256: 073748ad336e62bb6ca0e2810b19814dfd88f2e9f2c69f20b668f7675a401d15
> ## D. Audit Hand-off（裁決承接）
> - change_id: GG-FINALQA-260106-0001
> - change_id_prev:
>   - GG-FIX-260104-0001
> - authority_basis: HFI（人類最高決策者明確命令｜scope=GOVERNANCE_GATE_SPEC｜Final QA 去混讀/語義定錨一致化）
> - governance_order_applied: DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
> - audit_handoff:
>   - downstream_docs_to_recheck:
>     - FULL_ARCH（Mermaid / Module×Layer Mapping）
>     - ARCH_FLOW（Canonical Flow 標示）
>     - MASTER_CANON（全局語義定錨）
>     - UI_SPEC（Gate Must-Show 對位）
>     - VERSION_AUDIT（Hash/Changelog 機制一致化）
