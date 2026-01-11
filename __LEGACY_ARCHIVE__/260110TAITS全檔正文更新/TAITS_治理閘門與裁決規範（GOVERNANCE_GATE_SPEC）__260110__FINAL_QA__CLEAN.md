# TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）

- doc_key：GOVERNANCE_GATE_SPEC
- 治理等級：B（治理／制度級）
- 版本日期：2026-01-10（Asia/Taipei）
- 基線日期：2026-01-10（Asia/Taipei）
- 裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- 適用範圍：TAITS 全系統之治理閘門（Gate）定義、裁決模型、通過/阻擋/退回條件、衝突裁決、升級路徑、裁決留痕、UI 呈現義務與可回放證據要求

---
## 0. 文件定位（Governance Gate Charter｜治理閘門憲章）

本文件定義 TAITS 在 Canonical Flow 中的「治理閘門（Governance Gate）」與「衝突裁決（Arbitration）」制度規格，以確保：

- 任何流程推進皆有明確、可稽核的治理邊界（不可繞過）
- 任何衝突處理皆可追溯、可回放（以稽核回放機制承接；不得被誤讀為批准或下單）
- 風控與合規（Risk / Compliance）之最高否決權可被正確承接與呈現（不得被治理程序稀釋）
- 投資報告輸出與人類裁決之間，具備一致的引用、版本與留痕規格（避免新舊混讀與語義漂移）

本文件用於定義：

- 什麼情況下流程可以前進（PASS）
- 什麼情況下流程必須被阻斷（BLOCK）
- 什麼情況下流程必須退回補齊（RETURN）
- Gate 的裁決權位階、優先序、衝突解決與保守處置
- Gate 必須輸出的稽核／回放（Audit / Replay）證據
- Gate 在 UI 的呈現義務（不可模糊、不可遮蔽）
- Gate 與風控／合規之邊界與協作方式

本文件明確不負責（避免越權）：

- 不定義 Canonical Flow 之層級順序與各層定義（由 MASTER_CANON 與 ARCH_FLOW 裁決）
- 不定義風控與合規條文或否決原因碼全集（由 RISK_COMPLIANCE 與 TWSE_RULES 裁決）
- 不定義下單通道、券商／撮合細則（由 EXECUTION_CONTROL 裁決）
- 不定義策略內容、參數與績效敘事（由 STRATEGY_UNIVERSE 裁決）
- 不產生交易方向、不承諾績效、不形成下單權

---
## 1. Gate 裁決模型與硬性邊界（Hard Gates｜不可動搖）

### 1.1 Gate 的制度定位
Gate 為「治理層裁決」，目的在於確保：

- 流程不可跳步（L1–L11 不可跳層；層級定義以 MASTER_CANON 為唯一正文來源）
- 引用合法（引用之 doc_key 必須存在於 DOCUMENT_INDEX 且為唯一 ACTIVE）
- 證據可追溯（Evidence 可回放、可稽核）
- 版本一致（version_ref 不可缺漏、不可互斥混用）
- 人類主權不可被取代（Human-in-the-Loop；人類裁決不得被程序取代）

### 1.2 Gate 輸出僅允許三態（Binary Gate + Return）
Gate 輸出僅允許：

- `PASS`：允許進入下一步
- `BLOCK`：阻斷流程（治理否決；不可繼續）
- `RETURN`：退回補齊（不是放行；補齊後必須重新進 Gate）

未執行 Gate 的流程結果屬治理違規（GOV-*），必須採 BLOCK 或 RETURN（依缺口是否可補）。

### 1.3 「無稽核＝未發生」（Audit-First）
- Gate 產出必須可被稽核、可被回放、可被追溯。
- 事後補稽核、回填裁決、或以推測補值補齊缺失證據，一律視為治理違規。

### 1.4 風控／合規最高否決權不受 Gate 影響
- Gate 不是風控；Gate 不得弱化風控與合規裁決。
- 風控／合規之否決權高於一切（含 Gate、策略與任何執行意圖）。
- Gate 的作用是保證：證據、版本、引用與流程完整性具備，且可回放。

### 1.5 Gate 不取代人類裁決
- Gate 不做「買／賣」裁決。
- Gate 不做「是否值得交易」裁決。
- Gate 做的是「是否允許進入下一步」的制度裁決。
- 交易授權入口只能由人類裁決產生；Gate 不得暗示或替代授權。

---
## 2. Gate 在 Canonical Flow 的定位（Primary Gate + Sub-Gates）

### 2.1 Gate 的兩層形態
1) **主 Gate（Primary Governance Gate）**  
- 被檢核對象：投資報告輸出產物（報告層產物）  
- Gate 本體定位：non-layer（治理檢核機制；不構成 Canonical Layer）  
- 目的：在進入人類裁決與交易授權之前，完成「全鏈路一致性裁決」與「證據／版本／引用合法性裁決」。

2) **子 Gate（Sub-Gates / Checkpoints）**  
- 分布於 L1–L11 各層（以檢核點形式存在）  
- 目的：各層完成最低治理義務（Evidence Completeness、Version Ref、Audit、可回放索引等）。

注意：子 Gate 不得改寫主 Gate 的裁決語義；只能輸出可稽核的檢核結果。

### 2.2 主 Gate 輸入（Inputs｜不可缺）
- `correlation_id` / `session_id`
- `documents_active_map_ref`：當下生效文件快照（以 DOCUMENT_INDEX 裁決）
- `layer_artifacts_map_ref`：上游各層審計物索引（包含必要的 Evidence／Regime／Risk／Strategy 提案產物索引）
- `evidence_bundle_ref`
- `regime_state_ref`
- `risk_decision_ref`：風控／合規裁決引用（含結果與原因碼引用）
- `strategy_proposal_ref`：策略提案引用（僅建議，不含下單權）
- `ui_trace_ref_pre_human`：供 UI_SPEC 對位之呈現證據
- `version_ref`：doc/policy/model/rule snapshot（不可缺）

### 2.3 主 Gate 輸出（Outputs｜最小集合）
- `governance_gate_decision`：PASS / BLOCK / RETURN
- `gate_reason_codes[]`：若非 PASS 必填
- `return_required_items[]`：若 RETURN 必填（具體補齊清單）
- `governance_artifact_ref`：主 Gate 稽核物引用
- `replay_bundle_ref`：回放包引用（或其組裝索引）

---
## 3. Gate 責任邊界（Boundary Map｜避免重疊與越權）

### 3.1 Gate 負責
- 流程完整性裁決（No Skip）
- 文件引用合法性裁決（doc_key / ACTIVE / 唯一性）
- 證據完整性裁決（Evidence 可回放、可追溯）
- 版本一致性裁決（version_ref / policy_version / rule snapshot）
- 審計完整性裁決（Artifacts / Hash / Correlation）
- 人類裁決前的資訊呈現義務裁決（UI Must-Show）

### 3.2 Gate 不負責
- 不裁決合規條文（由 RISK_COMPLIANCE / TWSE_RULES）
- 不裁決策略勝率與績效（禁止績效辯護）
- 不裁決交易方向（人類才可裁決是否執行）
- 不改寫 Canonical Flow（由 MASTER_CANON / ARCH_FLOW）
- 不改寫上位母法（AI_GOV / MASTER_ARCH / DOCUMENT_INDEX）

---
## 4. 衝突裁決與保守處置（Priority & Conflict Resolution）

### 4.1 裁決依據與順位（以 DOCUMENT_INDEX 為主）
- 治理等級覆蓋與衝突裁決程序，以 DOCUMENT_INDEX（Authoritative Index）為準。

### 4.2 衝突類型
- **硬衝突（Hard Conflict）**：定義互斥、語義矛盾、優先序不可調和 即 BLOCK
- **缺口衝突（Gap Conflict）**：非矛盾但缺少必備證據/引用 即 RETURN（可補齊）

### 4.3 Gate 進行衝突裁決之最小程序（不可跳步）
1) **Index Gate（合法性）**：確認引用的 doc_key 存在於 DOCUMENT_INDEX 且為該 doc_key 唯一 ACTIVE  
2) **治理等級覆蓋**：套用 DOCUMENT_INDEX 定義之覆蓋規則（A+ 高於 A，高於 B，高於 C）  
3) **同級衝突**：依 DOCUMENT_INDEX 的衝突裁決程序採保守裁決；仍無法裁決則 STOP（不可通融）  
4) **稽核留痕**：若屬 Metadata Discrepancy 或需固定解釋口徑，必須在 VERSION_AUDIT 留存（METADATA_FIX 或等價類型）

---
## 5. 引用合法性與可回放最小格式（Citation / Trace / Evidence）

本節定義 Gate 與其輸出之「引用合法性」與「可回放證據」最小格式。引用以 doc_key 為治理身份基礎；檔名僅為物理載體，不構成治理身份。

#### EC1. 最小引用標頭（Minimum Legal Citation Header）
```text
trace_id = <全域唯一>
session_id = <本次對話/流程>
event_id = <本次事件/操作>
actor = <human/agent/module>
timestamp = <ISO-8601>
doc_key = GOVERNANCE_GATE_SPEC
doc_title = TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）
ref_version_date = 2026-01-08
ref_section = <章節/段落路徑>
audit_anchor = VERSION_AUDIT:<對應條目（若有）>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
```

#### EC2. Evidence Chain 最小結構（Minimum Evidence Chain）
當本文件涉及「可回放產物」或「稽核必需證據」時，Evidence Chain 至少包含：

- `env_fingerprint`（環境指紋）
- `dependency_manifest`（依賴清單）
- `run_evidence`（執行證據：命令／時間／產物／日誌）
- `failure_recovery`（失敗與回復：PASS/FAIL 與處置）

欄位定義與格式以 DEPLOY_OPS 為準；本節僅宣告「必帶」與「缺失之保守處置」。

#### EC3. 缺欄位之保守處置
- 若缺少 EC1/EC2 最小欄位：不得視為可回放／可稽核輸出。
- 涉及風險／合規裁決時：依 RISK_COMPLIANCE 與本文件之保守處置機制，採 RETURN 或 BLOCK 以補齊引用資訊（不得以推測補值）。

---
## 6. Gate 規則全集（Rulebook｜最大完備）

> Gate 規則以「必備檢核」方式定義。任何命中即依規則輸出 PASS/BLOCK/RETURN。  
> 允許擴充規則，但禁止弱化本節既有規則之語義與強度。

### 6.1 必備檢核 A：流程完整性（FLOW Integrity）
- A1：L1–L8 層級審計物齊全（layer_artifacts_map_ref 完整）
- A2：存在合法 L5 Evidence 與 L6 Regime 引用（evidence_bundle_ref / regime_state_ref）
- A3：若曾 RETURN，必須看見補齊項目已完成之證據（return_required_items 對位）
- A4：不同模式不得降低 Gate 覆蓋（No Downgrade）

裁決：
- 缺任何 A* 即 RETURN（若可補）或 BLOCK（若不可補/矛盾）

### 6.2 必備檢核 B：文件引用合法性（DOCUMENT_INDEX Compliance）
- B1：所有引用 doc_key 必須存在於 DOCUMENT_INDEX
- B2：引用文件狀態必須 ACTIVE
- B3：doc_key 唯一性與版本引用一致性（不可含糊、不可多版混用）
- B4：上位/平行參照不得互相矛盾（硬衝突必 BLOCK）

裁決：
- 命中 B1/B2/B3（引用非法）即 BLOCK
- 命中 B4：硬衝突 即 BLOCK；缺口 即 RETURN

### 6.3 必備檢核 C：審計可回放（AUDIT/REPLAY）
- C1：correlation_id / session_id 完整
- C2：hash 鏈（input/output）可驗證（不可事後補寫）
- C3：回放包（Replay Bundle）可組裝，且指向不可變儲存
- C4：審計物可讀/可取回（可回放）

裁決：
- C1 缺 即 RETURN（若可補）
- C2/C3/C4 缺 即 BLOCK（不可在裁決後補）

### 6.4 必備檢核 D：版本一致性（VERSION Alignment）
- D1：所有輸出都帶 version_ref（doc/policy/model/rule snapshot）
- D2：policy_version 可在 VERSION_AUDIT 回溯
- D3：制度/規則快照可在 TWSE_RULES 或 rule snapshot 引用中找到
- D4：同一 correlation_id 不可混用互斥版本

裁決：
- D1 缺 即 RETURN（若可補）
- D2/D3/D4 缺 即 BLOCK（不可用不可信版本裁決）

### 6.5 必備檢核 E：UI 呈現義務（UI Must-Show）
- E1：Risk Gate 結果（PASS/VETO）與 reason codes 必須可視化（不可遮蔽）
- E2：version_ref / correlation_id 必須可視化
- E3：RETURN 時補齊清單必須可視化且阻斷前進
- E4：不得以績效圖表弱化風險揭露（風險揭露優先）

裁決：
- 命中任一 E* 即 BLOCK（屬治理違規）

### 6.6 必備檢核 F：安全與旁路防護（Bypass Prevention）
- F1：不得存在繞過 Risk 或 Gate 的旁路通道（暗通道）
- F2：敏感資訊不得被寫入不允許位置（依 LOCAL_ENV）
- F3：不得以「效能／便利」理由移除審計/回放/對帳鏈路

裁決：
- 命中任一 F* 即 BLOCK

---
## 7. Gate 裁決原因碼（Gate Reason Codes｜最大完備）

格式：`GOV-[Domain]-[Number]`  
Domain：FLOW（流程）/ DOC（文件）/ AUD（審計）/ VER（版本）/ PROV（追溯）/ UI（介面）/ SAFE（安全）/ SCOPE（範圍）

### 7.1 FLOW（流程完整性）
- GOV-FLOW-01：跳層或未執行必要層（違反 L1–L11）
- GOV-FLOW-02：非法回寫（Layer 回寫策略/結論）
- GOV-FLOW-03：RETURN 後未補齊即重入後層
- GOV-FLOW-04：模式降級（降低 Gate 密度或省略必備審計）

### 7.2 DOC（文件引用合法性）
- GOV-DOC-01：引用不存在於 DOCUMENT_INDEX 的 doc_key
- GOV-DOC-02：引用文件狀態非 ACTIVE（DEPRECATED/ARCHIVED 等）
- GOV-DOC-03：doc_key 不唯一或版本引用不唯一
- GOV-DOC-04：文件關係宣告（上位/平行）互相矛盾
- GOV-DOC-05：以別名或非治理身份識別子取代 doc_key

### 7.3 AUD（審計完整性）
- GOV-AUD-01：缺 correlation_id / session_id / layer_id
- GOV-AUD-02：缺 layer_artifacts（任一層缺審計物）
- GOV-AUD-03：hash 不一致（input_hash/output_hash 驗證失敗）
- GOV-AUD-04：審計物不可讀/不可取回（不可回放）
- GOV-AUD-05：疑似事後回填審計（Audit Backfill）

### 7.4 VER（版本一致性）
- GOV-VER-01：version_ref 缺漏（doc/policy/model/rule snapshot）
- GOV-VER-02：policy_version 不可追溯（VERSION_AUDIT 不存在）
- GOV-VER-03：制度/規則快照缺失（TWSE/TAIFEX 等）
- GOV-VER-04：同一 correlation_id 版本參照互相矛盾

### 7.5 PROV（來源追溯）
- GOV-PROV-01：Evidence provenance 斷裂（來源不可追溯）
- GOV-PROV-02：使用非官方來源作裁決依據（可補充不可裁決）
- GOV-PROV-03：資料時間戳不一致或交易日判定可疑（需 RETURN 或 BLOCK）

### 7.6 UI（介面呈現義務）
- GOV-UI-01：UI 未顯示 Risk Gate 結果或 reason codes（遮蔽風險）
- GOV-UI-02：UI 未顯示必要版本引用（version_ref 不可見）
- GOV-UI-03：UI 未顯示 RETURN 補齊清單而允許繼續
- GOV-UI-04：UI 以模糊措辭取代裁決（PASS/BLOCK/RETURN）

### 7.7 SAFE / SCOPE（安全與範圍）
- GOV-SAFE-01：敏感資訊疑似外洩或被寫入不允許位置（LOCAL_ENV 違反）
- GOV-SAFE-02：疑似繞過 Gate / Risk 的旁路通道（暗通道）
- GOV-SCOPE-01：Scope 宣告與實際輸出不一致（超範圍寫入/超範圍執行）

---
## 8. Gate 與風控／合規裁決之關係（Two-Gate Model）

### 8.1 本質差異
- **風控／合規裁決**：裁決「是否允許進入交易授權與執行鏈路」，具最高否決權。
- **治理閘門（Gate）**：裁決「流程與證據是否具備合法性、可追溯性、可回放性」，並確保 UI 與稽核留痕可用。

### 8.2 協作規則（不可顛倒）
- 若風控／合規裁決為否決：
  - 治理閘門不得以任何理由放行；
  - 治理閘門僅能完成完整記錄、回放包封存、原因碼與版本引用之治理義務（不構成放行）。
- 若風控／合規裁決為通過：
  - 治理閘門仍可因治理缺陷採 BLOCK 或 RETURN（例如缺版本、缺審計、引用非法、UI 遮蔽）。

---
## 9. Gate 審計輸出（Audit Artifacts｜不可縮減）

### 9.1 Governance Gate Artifact（最小欄位）
- `correlation_id`
- `session_id`
- `target_artifact_kind`：被檢核對象類型（投資報告輸出產物；不代表 Gate=Layer）
- `decision`（PASS/BLOCK/RETURN）
- `gate_reason_codes[]`
- `documents_active_map_ref`
- `layer_artifacts_map_ref`
- `evidence_bundle_ref`
- `regime_state_ref`
- `risk_decision_ref`
- `strategy_proposal_ref`
- `ui_trace_ref_pre_human`
- `version_ref`
- `input_hash`
- `output_hash`
- `created_at_utc`

### 9.2 RETURN 的補齊清單（必填）
- `return_required_items[]` 必須具體到「缺哪個引用／缺哪個 artifact／缺哪個版本」。
- 禁止模糊詞（例如：補資料、再看看、可能不足）。

---
## 10. UI 呈現義務（Gate 專屬 Must-Show）

UI 詳規由 UI_SPEC 管；本節定義 Gate 必須交付 UI 的硬欄位。

UI 必須顯示：
- 主 Gate 決策：PASS / BLOCK / RETURN（不可模糊）
- gate_reason_codes（可展開）
- 若 RETURN：補齊清單（可勾選/追蹤進度）
- correlation_id（可稽核）
- documents_active_map（可點開檢視版本）
- risk_decision 決策與 reason codes（不可遮蔽）
- version_ref（doc/policy/model/rule snapshot）

禁止：
- 以「建議」「注意」「可能」取代裁決
- 允許使用者在 RETURN/BLOCK 狀態進入人類裁決與交易授權
- 在 UI 隱藏 Gate 的原因碼或版本引用

---
## 11. Mermaid｜治理 Gate 全流程圖（含 RETURN/BLOCK）

```mermaid
flowchart TB
  A[Strategy Proposal<br/>(Non-binding)] --> B[Investment Report Output<br/>(Report Artifact)]
  B --> G[Governance Gate<br/>(non-layer governance check)]

  G -->|PASS| C[Human Decision & Trade Authorization<br/>(Only authorization entry)]
  G -->|RETURN| R[Return to Required Step(s)<br/>+ Required Items List]
  G -->|BLOCK| X[STOP<br/>Preserve Evidence + Audit Artifact]

  R --> D[Evidence/Regime/Artifacts Completion]
  D --> B

  C -->|NO_ACTION| Y[STOP + Audit]
  C -->|AUTHORIZED| E[Execution Control<br/>(Module, not a layer)]
  E --> F[Audit & Replay<br/>(Replay only, not approval)]
```

---
## 12. 禁止事項（Forbidden｜一票否決）

- 任何形式跳過治理閘門檢核，直接進入人類裁決與交易授權或後續執行鏈路
- 任何形式以其他層輸出冒充投資報告輸出產物（報告層產物）以規避治理檢核
- 任何形式 Gate 決策模糊化，或 UI 遮蔽原因碼
- 任何形式引用未在 DOCUMENT_INDEX 列為 ACTIVE 的文件作裁決
- 任何形式缺稽核、缺 hash、缺版本引用仍放行
- 任何形式以績效辯護要求 Gate 放行
- 任何形式事後補稽核或回填裁決
- 任何形式旁路通道繞過風控／合規或 Gate（暗通道）
- 任何形式 AI/Agent 自行批准或暗示批准

---
## 13. 變更原則（本文件專屬）

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
## 14. 終極裁決語句（固定口徑）

沒有可追溯的證據與版本，就沒有合法的決策。  
沒有合法的決策，就不允許進入人類裁決與執行層。

---

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 正常化：移除正文中的補丁式語句、對話痕跡、歷史承接段落與重複說明。
- 收斂：移除「子級標籤／Label 法律定位」「順位助記」等非制度必要內容，避免下游文件誤學與混讀。
- 去特別化：移除對特定單層之重複定義與特別章節；層級定義一律承接 MASTER_CANON（Canonical Flow）之唯一正文來源。
- 精簡不越權：刪除與本文件職責無關之本地硬體建議段落（改由 LOCAL_ENV / DEPLOY_OPS 承接）。
- 版本更新：本文件版本日期更新為 2026-01-10（Asia/Taipei）。

### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：f2773fd76aeb4354195c7a4c72f22adbc73f05034fc7aacd1052f363ad53d024

### 3) 適用範圍（Scope）
本次覆蓋版修正範圍僅限於 doc_key=GOVERNANCE_GATE_SPEC 之正文正常化與去重收斂：
- 不新增、刪改其他 doc_key 之治理條文。
- 不變更 DOCUMENT_INDEX、MASTER_ARCH、AI_GOV 之裁決序位與其法律效力。
- 本文件之條款僅規範 Gate 制度本身，不改寫 Canonical Flow（層級定義由 MASTER_CANON 為唯一正文來源）。

### 4) 裁決承接（Audit Hand-off）
- 若後續文件引用本文件之 Gate 制度，必須以 doc_key=GOVERNANCE_GATE_SPEC 引用，並附帶 version_date 與 ref_section（依 EC1 格式）。
- 若跨文件出現衝突，應回到 DOCUMENT_INDEX 所定之衝突裁決程序處置；本文件不得自設覆蓋規則。
