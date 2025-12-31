<!--
TAITS｜ACTIVE UPDATED（單檔內嵌更新版）
產出日期：2025-12-29（Asia/Taipei）
更新規格：單檔內嵌；可更新處直接更新並避免重複；不可更新處以 Appendix 內嵌 Only-Add 全文。
來源檔：TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md
-->

# TAITS_風險控管與合規最高否決權（RISK_COMPLIANCE）__251219
doc_key：RISK_COMPLIANCE
治理等級：A（Risk & Compliance Supreme Veto｜高於策略、高於績效、高於主觀）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（最高否決權文件，Only-Add 演進）
版本日期：2026-01-01
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX（Index 裁決）
平行參照：FULL_ARCH / ARCH_FLOW / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES / TWSE_RULES
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化否決權/偷換定義）

## L9–L11 最終語義定錨（單一正確版｜必須一致）

> 本節為 TAITS 在 L9／L10／L11 的**唯一正確語義**。  
> 任何文件中若出現與本節不一致之描述，視為舊錯口徑（不得保留於單一正確版）。

### L9｜投資報告（Investment Report｜可追蹤、可更新、可稽核）
L9 的產出定位為「**給人看的完整投資報告**」，不是一次性的口頭解說；必須可在後續事件/行情變動下持續更新並可追溯。
L9 最低交付物應包含（不限於）：
- **標的化**：標的識別、觀測起點、追蹤狀態（open/hold/watch/exit-candidate 等）、版本號與時間戳。
- **數據**：對應 L1–L8 的關鍵數據表（消息/基本/技術/籌碼/風險/制度），含來源、取樣時間、缺漏註記。
- **圖形**：至少包含價格走勢與關鍵技術指標狀態視覺化（例如均線、RSI、MACD；以「狀態」呈現，非主觀敘事）。
- **進出場建議（非下單）**：建議區間/觸發條件/失效條件（停損/停利/風險撤退），並明確標示「此為建議，不構成下單」。
- **情境更新（Regime/Event）**：當市場制度/事件/風險狀態改變，需能產生增量更新（delta）並保留回放鏈。
- **可稽核鏈**：引用到 L11 的 record_id / ledger_id（或等價識別），以確保報告可被回放與驗證。

### L10｜人類裁決與交易授權（Human Decision & Authorization｜唯一決策點）
L10 的定位為「**人類最高決策者的最終裁決介面與授權層**」。  
- **最終決策者永遠是人類**：你決定採取何種模式與是否授權交易。
- L10 可裁決/授權的動作包含（不限於）：**不動作／回測／模擬／半自動／全自動**。
- AI/Agent 在 L10 僅能提供「選項、理由、風險揭露與建議」，**不得自行構成下單行為**；下單/執行屬於 L10 授權後由執行控制規範承接。

### L11｜工程稽核與全層回放（Engineering Audit & Replay｜全層留痕）
L11 的定位為「**工程檢視與稽核回放層**」，不是下單層，也不是只記錄 L10。
- **全層留痕**：L11 必須覆蓋 L1–L11 每一層的關鍵輸入/輸出/裁決/否決/變更理由與時間戳。
- **雙料輸出**：同一筆紀錄需同時具備  
  1) 人話可讀（你能看懂，用於檢視系統是否合理）  
  2) 工程可用（可重現、可驗證、可追溯，用於開發/稽核/回放）
- **目的**：用來檢查每一層的功能是否合理、是否需要調整、以及自動/半自動/全自動在不同時點的決策依據是否一致可回放。

核心裁決：Binary Compliance（PASS / VETO）＋ Worst-case First（最壞情境優先）

---

---

# Appendix A｜RISK_COMPLIANCE × MASTER_CANON 對位補充（Only-Add）
（Only-Add · Alignment Addendum · Freeze v1.0）

## A.0 補充性質聲明（不可省略）
- 適用文件：RISK_COMPLIANCE（doc_key=RISK_COMPLIANCE）
- 補充類型：Addendum / Alignment Guideline（對位補充；不改寫 Canonical）
- 生效狀態：GOVERNANCE_STATE = Freeze v1.0
- 變更原則：Only-Add（只可新增，不可刪減/覆寫/偷換既有語義）
- 衝突裁決序：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON
- 範圍限定：僅針對本文件與 MASTER_CANON（含附錄 Z）在 **L7 Gate 職責語義、輸入輸出、否決權位階、全紀錄原則與人機分工邊界** 之一致性對位

## A.1 與 MASTER_CANON 的定位差異（法源分工）
> 本節僅用於「裁決對位」，不得被理解為新增 Canonical Flow 或改寫 L1–L11。

### A.1.1 MASTER_CANON（治理等級 S）在本議題的法源角色
MASTER_CANON 負責裁決（與本文件相關者）：
- Canonical Flow（L1–L11）之語義不可變核心（含 L7 的存在性與輸入/輸出語義）
- L7：Risk & Compliance 的 **PASS/VETO 二元裁決**、**禁止 Soft Pass**、**禁止以績效辯護否決**
- L9a/L10/L11 人機分工與全紀錄原則（附錄 Z）：確保「分析敘事」「人類決策」「系統執行」三者不可混用，且所有關鍵結論必須可回指 Evidence（可驗證/可否決/可稽核）

### A.1.2 RISK_COMPLIANCE（治理等級 A）在本議題的法規角色
本文件負責把母法級要求落地為：
- L7 Gate 的 **最高否決權（Supreme Veto）** 制度化定義（位階、不可覆寫、即刻生效）
- 風險分類體系（Risk Taxonomy）、否決條件全集（Veto Conditions）、否決原因碼（Reason Codes）
- Risk PASS Token（放行憑證）之結構、簽章/防偽、有效期、版本引用與審計物要求
- Gate 與 UI 的交付義務（PASS/VETO + reason codes + Evidence/Policy 版本可追溯）
- 審計與回放（Audit/Replay）之最小集合，並與 ARCH_FLOW / VERSION_AUDIT / EXECUTION_CONTROL 形成可對帳的工件鏈

## A.2 對位結論（一致性宣告）
- MASTER_CANON 定義「L7 是什麼、可輸出什麼、禁止什麼」；RISK_COMPLIANCE 定義「如何以制度條文把 L7 落地為可驗證、可否決、可回放」。
- 任何歧義：一律回到 MASTER_CANON 的語義裁決，再以 Only-Add 方式在本文件附錄增補可驗證條件；不得反向改寫母法。

## A.3 MASTER_CANON 的 L7 語義鎖定：對位映射（不改主文）
MASTER_CANON 對 L7 的語義要求（摘要）：
- 目的：對所有意圖做 PASS/VETO 裁決
- 輸入：Regime State + Evidence + Account/Portfolio + Rules
- 輸出：PASS / VETO + reason codes + token（PASS only）
- 禁止：Soft Pass；以績效辯護否決

本文件對位落點（主文既有內容）：
- §1.2 Binary Compliance（PASS/VETO）＝對位「禁止 Soft Pass」
- §3.3 Gate 輸出（PASS/VETO + reason codes + token）＝對位「輸出 token（PASS only）」
- §1.1、§7（否決條件）與 §14（禁止事項）＝對位「不得以績效/直覺/緊急性辯護否決」

---

# Appendix B｜對位 MASTER_CANON 附錄 Z：人機分工邊界對 L7 的限制（Only-Add）
（Only-Add · Boundary Lock for L7 · Freeze v1.0）

## B.0 補充性質聲明
- 適用文件：RISK_COMPLIANCE
- 補充類型：Guideline（邊界鎖定指引；不改寫 Canonical）
- 生效狀態：GOVERNANCE_STATE = Freeze v1.0
- 目的：將 MASTER_CANON 附錄 Z 所述「L9a 敘事 / L10 決策 / L11 執行」不可混用邊界，落到 L7 Gate 的行為限制，避免風控越權或被誤用為「決策替代」。

## B.1 L7 的合法輸出形態（嚴格限制）
L7 對外（供 L9/L10/L11）唯一合法輸出僅允許：
- `risk_gate_decision = PASS | VETO`
- `veto_reason_codes[]`（VETO 必填且不可空）
- `risk_pass_token`（僅 PASS 生成）
- `risk_evidence_snapshot_ref`（可回放）

禁止 L7 輸出：
- 任何交易方向建議、進出場條件建議、標的偏好（屬 L8/L9a 範圍）
- 任何「替代 L10 的批准/拒絕敘事」或情緒性語句（L7 只能裁決 PASS/VETO + 理由碼）
- 任何以 L9a 人話敘事替代 Evidence 的放行（Evidence First）

## B.2 L7 不得被 L9a 影響其裁決語義（Evidence > Narrative）
- 附錄 Z 要求：L9a 的關鍵敘述必須可回指 Evidence，且僅作 L10 參考。
- 因此，L7 的裁決必須以 **Evidence + Rules + Account/Portfolio + Regime** 為唯一有效依據；
- 若輸入中存在僅敘事、無可回指 Evidence 的主張，視為 Evidence 不完整：依主文 §1.4 直接觸發 SYS 類否決（SYS-AUD / SYS-PROV）。

## B.3 L7 與 L10 的不可替代關係（Veto ≠ Decision）
- L7 的 PASS 不是「建議下單」，只是「風險/合規層不否決」。
- L7 的 VETO 不是「投資建議」，而是「制度上禁止進入執行」。
- L10 人類裁決（APPROVE/REJECT/ABORT）不得被 L7 的 PASS 誤解為自動批准；UI 必須明確區隔「PASS」與「APPROVE」。

---

# Appendix C｜L7 全紀錄原則：Risk Gate 工件鏈與 Replay 最小集（Only-Add）
（Only-Add · Audit/Replay Hardening for L7 · Freeze v1.0）

## C.0 補充性質聲明
- 適用文件：RISK_COMPLIANCE
- 補充類型：Appendix（工件鏈補強附錄；不取代主文）
- 生效狀態：GOVERNANCE_STATE = Freeze v1.0
- 目的：對位 MASTER_CANON「可驗證、可否決、可稽核」之全紀錄原則，將 L7 必備工件鏈落地為可被 ARCH_FLOW / VERSION_AUDIT / EXECUTION_CONTROL 一致引用的最小集合。

## C.1 L7 Gate 審計事件最小欄位集（Risk Gate Decision Minimal Fields）
任何一次 L7 Gate 計算（無論 PASS 或 VETO）至少必須寫入：
- `correlation_id`
- `layer_id = L7`
- `timestamp_utc`
- `risk_gate_decision = PASS | VETO`
- `veto_reason_codes[]`（PASS 可空；VETO 不可空）
- `policy_version`
- `rulebook_snapshot_ref`
- `regime_state_ref`
- `evidence_bundle_ref`（或等價引用）
- `account_state_ref`（資金/倉位/未成交/曝險快照引用）
- `input_hash_ref`（Evidence/State 的 hash）
- `output_hash_ref`（決策輸出的 hash）
- `documents_active_map_ref`（ACTIVE 文件版本映射快照）
- `immutability_flag`（append-only/immutable）

缺任一欄位 → 視為 `SYS-AUDIT-01` 或等價否決，並不得產生有效 PASS Token。

## C.2 Risk PASS Token 的「不可否認性」最低要求（對位 EXECUTION_CONTROL）
為確保 EXECUTION_CONTROL 可驗證且不可偽造，本文件主文 §10.2 之 Token 最小欄位在 Freeze v1.0 下補強如下（Only-Add）：
- `token_id`
- `correlation_id`
- `policy_version`
- `issued_at` / `expires_at`
- `gate_decision = PASS`
- `input_hash_ref`（指向 Evidence/Regime/Account/Rules 的 hash 清單或 manifest）
- `documents_active_map_ref`
- `signature`（不可否認簽章/摘要；具可驗證性）
- `scope`（可選；若存在，至少包含 mode 與標的/帳戶範圍之限制，避免 token 跨模式濫用）

Token 若缺 `signature` 或 `documents_active_map_ref` → 視為不可驗證（SYS-VERIFY-01）→ VETO。

## C.3 ARCH_FLOW Replay Bundle 的 L7 子集（Risk Sub-Bundle）
L7 必須能提供 Replay 子集（可被整體 Replay Bundle 引用）：
- `risk_gate_decision_ref`
- `veto_reason_codes[]`
- `policy_version`
- `rulebook_snapshot_ref`
- `risk_pass_token_ref`（PASS only）
- `regime_state_ref`
- `evidence_bundle_ref`
- `account_state_ref`
- `documents_active_map_ref`
- `hash_manifest_ref`

要求：相同 Replay 子集必須可重算得到相同 PASS/VETO 結論；否則視為污染（Pollution）並必須阻斷後續同類執行，直到人工介入。

---

# Appendix D｜L7→L10→L11 交接契約（Handoff Contract）與 UI 呈現補強（Only-Add）
（Only-Add · Handoff Integrity · Freeze v1.0）

## D.0 補充性質聲明
- 適用文件：RISK_COMPLIANCE
- 補充類型：Checklist / Contract Appendix（交接契約附錄；不取代主文）
- 生效狀態：GOVERNANCE_STATE = Freeze v1.0
- 目的：把 L7 Gate 的輸出，規範為 UI（L10）與執行層（L11）可直接驗證的交接契約，防止「PASS 被誤當 APPROVE」「Token 被誤用」「理由碼被遮蔽」。

## D.1 L7→L10（UI）交付欄位（Must-Deliver to UI）
UI（L10）在展示給人類裁決前，必須收到且能呈現：
- `risk_gate_decision`（PASS/VETO，禁止模糊）
- `veto_reason_codes[]`（VETO 必須可展開、不可遮蔽）
- `risk_evidence_snapshot_ref`（可點開回放）
- `policy_version`（可追溯）
- `rulebook_snapshot_ref`（制度快照版本）
- `correlation_id`（稽核主鍵）
- `documents_active_map_ref`（本次運行 Active 版本映射）

UI 禁止：
- 以「建議」「注意」取代 VETO
- 以績效圖表弱化風險揭露（風險揭露優先於績效）
- 在 VETO 時仍允許進入 APPROVE（必須硬阻斷）

## D.2 L7→L11（Execution Control）交付欄位（Must-Deliver to Execution）
當且僅當 `risk_gate_decision=PASS`，L7 必須交付：
- `risk_pass_token_ref`（含 token 可驗證內容）
- `policy_version`
- `documents_active_map_ref`
- `input_hash_ref` / `hash_manifest_ref`

並且明確規範（對位 EXECUTION_CONTROL）：
- L11 送單前必驗：token 未過期、correlation_id 一致、policy_version 存在且可回放、signature 可驗證、scope 不越界
- 驗證失敗：視為 SYS-VERSION / SYS-VERIFY 類 VETO，並觸發執行層保護（BLOCK/SAFE MODE）

## D.3 交接一致性檢查（Consistency Checks｜全部不通過＝BLOCK）
1) PASS ≠ APPROVE
- UI 必須明確標示：Risk PASS 只是「未否決」，仍需 L10 人類 APPROVE 才能進入 L11。

2) Token 不可跨模式濫用
- Simulation/Paper/Live 的 token 不得互用；任何不一致屬 `TOKEN_SCOPE_MISMATCH` → BLOCK。

3) Reason Codes 不可空與不可遮蔽
- VETO 時 reason_codes 必須非空且 UI 可見；遮蔽視為 `SYS-AUDIT` 等價重大缺失 → VETO。

4) Evidence 必須可回放
- risk_evidence_snapshot_ref 不可用「文字敘事」替代；不可回放視為 Evidence 不完整 → VETO。

---

（RISK_COMPLIANCE｜Only-Add Addendum Pack：Appendix A–D · Freeze v1.0 生效）
---

## Appendix 2025-12-28｜Only-Add：Trace ID / Evidence Chain 最小欄位貫穿（RISK_COMPLIANCE）對齊 DEPLOY_OPS（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）
> 適用文件：TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md（doc_key：RISK_COMPLIANCE）
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0
> 上位裁決：RISK_COMPLIANCE（A）＋EXECUTION_CONTROL（A）＋DOCUMENT_INDEX（A+）＋AI_GOV（A+）
> 平行對齊：DEPLOY_OPS｜Addendum 2025-12-27（D2/D3：Evidence Chain 最小欄位與結構）
> 目的：將 Trace ID / Evidence Chain 的「最小可回放欄位」貫穿到本文件所管轄的產物/紀錄/裁決輸出；不改既有流程，只固定最低輸出格式。

### EC1. 最小引用標頭（Minimum Legal Citation Header）
本文件所生成或要求的任何「決策/裁決/執行/呈現」紀錄，至少必須包含下列引用標頭（欄位可多不可少）：

```text
trace_id = <全域唯一>
session_id = <本次對話/流程>
event_id = <本次事件/操作>
actor = <human/agent/module>
timestamp = <ISO-8601>
doc_key = RISK_COMPLIANCE
doc_title = TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:<對應條目（若有）>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
```

### EC2. Evidence Chain 最小結構（對齊 DEPLOY_OPS D3）
當本文件涉及「可回放產物」或「稽核必需證據」時，Evidence Chain 至少包含：

- `env_fingerprint`（環境指紋）
- `dependency_manifest`（依賴清單）
- `run_evidence`（執行證據：命令/時間/產物/日誌）
- `failure_recovery`（失敗與回復：PASS/FAIL 與處置）

> 欄位定義與格式以 DEPLOY_OPS｜D3 為準；本附錄不重複改寫其語義，僅宣告「必帶」。

### EC3. Gate 行為（缺欄位之保守處置）
- 若缺少 EC1/EC2 最小欄位：不得視為「可回放/可稽核」輸出。
- 涉及風險/合規裁決時：依 RISK_COMPLIANCE 與 GOVERNANCE_GATE_SPEC 之保守處置機制，採 **STOP/RETURN** 以補齊引用資訊（不得以推測補值）。
---

## Appendix 2025-12-28｜Only-Add：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）
> 適用文件：TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md（doc_key：RISK_COMPLIANCE）
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 Addendum/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`RISK_COMPLIANCE`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=RISK_COMPLIANCE` + `canonical_filename=TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md`。
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---