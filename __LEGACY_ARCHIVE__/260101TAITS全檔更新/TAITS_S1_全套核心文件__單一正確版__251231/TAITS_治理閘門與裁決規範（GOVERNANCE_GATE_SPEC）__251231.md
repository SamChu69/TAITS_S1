# TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231
doc_key：GOVERNANCE_GATE_SPEC  
治理等級：B（Governance Gate Spec）  ）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（治理裁決核心文件，Only-Add 演進）  
P25-12-31
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251231（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX（Index 裁決）  
平行參照：ARCH_FLOW / FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES / LOCAL_ENV / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化裁決權/偷換語義）  
核心裁決：Binary Gate（PASS / RETURN / STOP）＋ Traceability First（可追溯優先）

---

---

# 補強規範
---

## 0. 治理等級與 ACTIVE 身份之唯一裁決（Index Gate｜不可否認）

### 0.1 Index 表格裁決優先
在 TAITS 中，文件之下列「身份性中繼資料」以 **DOCUMENT_INDEX（A+｜ACTIVE）表格裁決**為準：

- `doc_key`
- `治理等級`
- `版本狀態（ACTIVE/ARCHIVED/…）`

本文件檔頭所載之 `治理等級` 若與 DOCUMENT_INDEX 表格存在差異，屬 **Metadata Discrepancy**：
- 引用端一律以 DOCUMENT_INDEX 表格裁決為準（避免工具誤讀檔頭標示）
- 文件端僅能以 整合段落 / 整合段落 方式補強一致性（Freeze v1.0｜Only-Add）
- 差異處置必須可稽核（VERSION_AUDIT｜METADATA_FIX）

---

## 1. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）

### 1.1 本文件 §4.1「衝突裁決順位」一律視為助記字串
本文件 §4.1 所列「衝突裁決順位（高 → 低）」：
- 僅作 **閱讀／操作助記（Mnemonic）**
- 不得被解讀為「治理等級覆蓋規則」或「裁決權重新分配」
- 若其文字排序與 DOCUMENT_INDEX 正文之「治理等級覆蓋（A+ > A > B > C）」或「衝突裁決程序」產生張力：  
  **一律以 DOCUMENT_INDEX 正文（§3／§6）為準**，本文件排序不具裁決力

### 1.2 AI_GOV（A+）之最高約束不因任何字串而降低
凡涉及「AI 行為／AI 參與裁決邊界／AI 可不可補完／AI 可不可越權」之議題：
- 一律受 AI_GOV（A+）最高约束  
- 任何文件內部的順位字串不得被用來否認或降格 AI_GOV 的覆蓋地位

---

## 2. 本文件之衝突裁決「唯一可採用」程序（對齊 DOCUMENT_INDEX）

### 2.1 Gate 執行之最小程序（不可跳步）
當本 Gate 需要對衝突進行裁決時，必須依以下順序執行（不可跳步）：

1) **Index Gate（合法性）**：確認引用的 doc_key 存在於 DOCUMENT_INDEX 且為該 doc_key 唯一 ACTIVE  
2) **治理等級覆蓋**：套用 DOCUMENT_INDEX 定義的 A+ > A > B > C 覆蓋規則  
3) **同級衝突**：依 DOCUMENT_INDEX 的衝突裁決程序保守裁決；仍無法裁決則 STOP（不可通融）  
4) **稽核留痕**：若屬 Metadata Discrepancy 或需固定解釋口徑，必須在 VERSION_AUDIT 留存（METADATA_FIX 或等價類型）

### 2.2 本文件既有 §4.1 的使用方式（不改原文，只新增口徑）
本文件 §4.1 可作為「領域文件檢視順序」提示，但其任何排序**不得**：
- 覆蓋 DOCUMENT_INDEX 的裁決程序
- 覆蓋 A+ > A > B > C 覆蓋規則
- 覆蓋 AI_GOV 的最高約束地位

---

## 3. 格式性修補宣告（Mermaid Fence Patch｜Only-Add）

本文件 §10 Mermaid 圖示區塊若缺少結尾 fence（```），將造成後續章節（§11 以後）被誤判為 code block，進而破壞文件可讀性與引用定位。

本 整合段落 以 **Only-Add** 方式補上缺失之結尾 fence：
- 不改寫 Mermaid 內容
- 不刪改後續章節文字
- 僅補上必要的結尾 fence，以恢復正確的 Markdown 區塊邊界
## 0. 文件定位（Governance Gate Charter｜治理閘門憲章）

本文件是 TAITS 的「治理 Gate（閘門）裁決規範」母文件，負責定義：

- **什麼情況下流程可以前進（PASS）**
- **什麼情況下流程必須被阻斷（STOP）**
- **什麼情況下流程必須退回補齊（RETURN）**
- **Gate 的裁決權位階、優先序、衝突解決**
- **Gate 必須輸出的審計/回放（Audit / Replay）證據**
- **Gate 在 UI 的呈現義務（不可模糊、不可遮蔽）**
- **Gate 與 Risk / Compliance（風控與合規）之邊界與協作**

📌 本文件不負責（避免越權）：
- 不定義 Canonical Flow 的層級順序（由 MASTER_CANON / ARCH_FLOW 裁決）
- 不定義風控與合規條文、否決原因碼全集（由 RISK_COMPLIANCE / TWSE_RULES 裁決）
- 不定義下單通道、券商細則（由 EXECUTION_CONTROL 裁決）
- 不定義策略內容、參數、績效敘事（由 STRATEGY_UNIVERSE 裁決）
- 不產生交易方向、不承諾績效、不形成下單權

---

## 1. 核心鐵律（Hard Gates｜不可動搖）

### 1.1 Gate 位階（治理裁決的法定位階）
- Gate 的裁決屬於 **治理層裁決**，其目的在於保護：
  - 流程不可跳步（L1–L11 不可跳層）
  - 引用合法（doc_key 必須在 DOCUMENT_INDEX）
  - 證據可追溯（Evidence 可回放、可稽核）
  - 版本一致（version_ref 不可缺漏）
  - 人類主權不可被取代（Human-in-the-Loop）

### 1.2 Binary Gate（裁決輸出只能是三態）
Gate 輸出僅允許：
- `PASS`：允許進入下一層
- `STOP`：阻斷流程（視為治理否決；不可繼續）
- `RETURN`：退回補齊（不是放行；補齊後再走一次 Gate）

禁止：
- 模糊放行（Soft Pass）
- 條件通融（Conditional Pass）
- 以備註取代裁決狀態

### 1.3 「無審計＝未發生」延伸到 Gate
- Gate 若缺少審計物（Artifacts），該 Gate 視為未執行
- 未執行 Gate 的流程結果：**治理違規（GOV-*）→ 必須 STOP**

### 1.4 Risk / Compliance 最高否決權不受 Gate 影響
- Gate 不是風控；Gate 不得弱化風控
- **RISK_COMPLIANCE 的 VETO 高於一切**（含 Gate、策略、人類執行意圖）
- Gate 的功能：保證「該有的證據、版本、引用、流程完整性」都存在

### 1.5 人類裁決不可被 Gate 取代
- Gate 不做「買/賣」裁決
- Gate 不做「是否值得交易」裁決
- Gate 做的是：「是否**允許進入下一步**的制度裁決」
- L10（Human Decision）仍是唯一的人類裁決節點（依 ARCH_FLOW）

---

## 2. Gate 在 Canonical Flow 的定位（L9 主 Gate + 全鏈路子 Gate）

### 2.1 Gate 的兩層形態
TAITS 的治理 Gate 分為兩種：

1) **主 Gate（Primary Governance Gate）**  
- Canonical Layer：**L9b（主 Gate）**
- 目的：在進入 L10（Human Decision）前，完成「全鏈路一致性裁決」

2) **子 Gate（Sub-Gates / Checkpoints）**  
- 分布於 L1–L11 各層（以“檢核點”形式存在）
- 目的：每層完成最低治理義務（例如 Evidence Completeness、Version Ref、Audit）

📌 注意：子 Gate 不得改寫 L9 的裁決語義；只提供可稽核的檢核結果。

### 2.2 主 Gate（L9）輸入（Inputs）
主 Gate 必須取得以下輸入引用（不可缺）：

- `correlation_id` / `session_id`
- `documents_active_map`（當下生效文件版本）
- `layer_artifacts_map`（L1–L8 各層審計物引用）
- `evidence_bundle_ref`（L5）
- `regime_state_ref`（L6）
- `risk_gate_ref`（L7：PASS/VETO 與 reason codes 引用）
- `strategy_proposal_ref`（L8：僅建議；不可含下單權）
- `ui_trace_ref_pre_human`（供 UI_SPEC 對位）
- `version_ref`（doc/policy/model/rule snapshot）

### 2.3 主 Gate（L9）輸出（Outputs）
- `governance_gate_decision`：PASS / RETURN / STOP
- `gate_reason_codes[]`：若非 PASS 必填
- `return_required_items[]`：若 RETURN 必填（具體補齊清單）
- `governance_artifact_ref`：主 Gate 審計物引用
- `replay_bundle_ref`：回放包引用（或其組裝索引）

---

## 2.4 L9a（投資報告）承接要求（面向人類交付）

本文件之 Gate（L9b）雖然屬於制度裁決層，但在實務上必須承接「人類可閱讀投資報告（L9a）」之交付要求，避免系統只產生內部判斷而人類無法檢視。

L9a 最小交付規格（Gate 需可檢核其是否存在且欄位齊全）：

- 標的識別（代碼/名稱）與 `trace_id`
- 來源與證據引用（回指 L4–L8 之 Evidence Bundle）
- 多面向證據整合（消息/基本/技術/籌碼）之**數據與圖形**
- 條件式交易方案（非指令）：進場/出場條件、風險假設、再評估條件
- 持續追蹤欄位：`tracking_state`、`next_review_trigger`、`position_intent`

Gate 裁決原則：
- L9a 缺失或欄位不全：必須 RETURN（列出具體補齊項），不得 PASS。
- L9a 內容存在「指令式下單」或「自動批准」語句：必須 STOP（越權），並回報 reason code。
- L9a 與治理/合規/風控條款衝突：以 RISK_COMPLIANCE / AI_GOV / MASTER_ARCH / DOCUMENT_INDEX 之裁決序位處理。

---

## 3. Gate 責任邊界（Boundary Map｜避免重疊與越權）

### 3.1 Gate 負責
- 流程完整性裁決（No Skip）
- 文件引用合法性裁決（doc_key 必須在 Index）
- 證據完整性裁決（Evidence 可回放、可追溯）
- 版本一致性裁決（version_ref / policy_version / rule snapshot）
- 審計完整性裁決（Artifacts / Hash / Correlation）
- 人類裁決前的資訊呈現義務裁決（UI Must-Show）

### 3.2 Gate 不負責
- 不裁決合規條文（由 RISK_COMPLIANCE / TWSE_RULES）
- 不裁決策略勝率與績效（禁止績效辯護）
- 不裁決交易方向（Human 才可裁決是否執行意圖）
- 不改寫 Canonical Flow（MASTER_CANON / ARCH_FLOW）

---

## 4. Gate 優先序與衝突裁決（Priority & Conflict Resolution）

### 4.1 衝突裁決順位（高 → 低）
1) MASTER_ARCH（母體鐵律）
2) TAITS_AI_行為與決策治理最終規則全集__251231（母法）
3) DOCUMENT_INDEX（文件裁決與生效狀態）
4) MASTER_CANON（Canonical 流程母法）
5) RISK_COMPLIANCE（風險與合規最高否決）
6) ARCH_FLOW / FULL_ARCH（流程細化 / 架構映射）
7) EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES / 其他

📌 若任一輸入引用與上述順位衝突：
- Gate 必須 **STOP**，reason_code 記錄衝突來源與對應 doc_key

### 4.2 兩類衝突
- **硬衝突（Hard Conflict）**：定義互斥、語義矛盾、優先序不可調和 → STOP
- **缺口衝突（Gap Conflict）**：非矛盾但缺少必備證據/引用 → RETURN（可補齊）

---

## 5. Gate 裁決原因碼（Gate Reason Codes｜最大完備）
### 5.1 FLOW（流程完整性）
- GOV-FLOW-01：發現跳層或未執行必要層（違反 L1–L11）
- GOV-FLOW-02：發現非法回寫（Layer 回寫策略/結論）
- GOV-FLOW-03：發現 RETURN 後未補齊即重入後層
- GOV-FLOW-04：發現模式降級（Research/Backtest/Sim/Paper/Live 降低 Gate 密度）

### 5.2 DOC（文件引用合法性）
- GOV-DOC-01：引用不存在於 DOCUMENT_INDEX 的 doc_key
- GOV-DOC-02：引用文件狀態非 ACTIVE（例如 DEPRECATED/ARCHIVED）
- GOV-DOC-03：doc_key 重複或版本引用不唯一
- GOV-DOC-04：文件關係（上位/平行）宣告不一致

### 5.3 AUD（審計完整性）
- GOV-AUD-01：缺 correlation_id / session_id / layer_id
- GOV-AUD-02：缺 layer_artifacts（任一層缺審計物）
- GOV-AUD-03：hash 不一致（input_hash/output_hash 驗證失敗）
- GOV-AUD-04：審計物不可讀/不可取回（不可回放）

### 5.4 VER（版本一致性）
- GOV-VER-01：version_ref 缺漏（doc/policy/model/rule snapshot）
- GOV-VER-02：policy_version 不可追溯（VERSION_AUDIT 不存在）
- GOV-VER-03：rule snapshot 不存在（TWSE/TAIFEX 制度快照缺失）
- GOV-VER-04：同一 correlation_id 中版本參照互相矛盾

### 5.5 PROV（來源追溯）
- GOV-PROV-01：Evidence provenance 斷裂（來源不可追溯）
- GOV-PROV-02：使用非官方來源作裁決依據（可做補充但不可裁決）
- GOV-PROV-03：資料時間戳不一致或交易日判定可疑（需 RETURN/或 STOP）

### 5.6 UI（介面呈現義務）
- GOV-UI-01：UI 未顯示 Risk Gate 結果或 reason codes（遮蔽風險）
- GOV-UI-02：UI 未顯示必要版本引用（version_ref 不可見）
- GOV-UI-03：UI 未顯示「RETURN 補齊清單」而允許繼續
- GOV-UI-04：UI 以模糊措辭取代裁決（PASS / RETURN / STOP）

### 5.7 SCOPE / SAFE（凍結範圍與安全）
- GOV-SCOPE-01：Freeze 後越界變更（Only-Add 違規跡象）
- GOV-SAFE-01：敏感資訊疑似外洩或被寫入不允許位置（LOCAL_ENV 違反）
- GOV-SAFE-02：疑似繞過 Gate / Risk 的旁路通道（暗通道）

---

## 6. Gate 規則全集（Rulebook｜最大完備）
### 6.1 必備檢核 A：流程完整性（FLOW Integrity）
- 檢核 A1：L1–L8 層級審計物齊全
- 檢核 A2：存在合法的 L5 Evidence 與 L6 Regime 引用
- 檢核 A3：若曾 RETURN，必須看見補齊項目已完成之證據
- 檢核 A4：不同模式不得降低 Gate 覆蓋（No Downgrade）

裁決：
- 缺任何 A* → RETURN（若可補）或 STOP（若不可補/矛盾）

### 6.2 必備檢核 B：文件引用合法性（DOCUMENT_INDEX Compliance）
- 檢核 B1：所有引用 doc_key 必須存在於 DOCUMENT_INDEX
- 檢核 B2：引用文件狀態必須 ACTIVE
- 檢核 B3：doc_key 唯一性與版本引用一致性（不可含糊）
- 檢核 B4：上位/平行參照不得互相矛盾

裁決：
- 命中 GOV-DOC-* → STOP（因為引用非法不可補）

### 6.3 必備檢核 C：審計可回放（AUDIT/REPLAY）
- 檢核 C1：correlation_id / session_id 完整
- 檢核 C2：hash 鏈（input/output）可驗證
- 檢核 C3：回放包（Replay Bundle）可組裝，且指向不可變儲存
- 檢核 C4：審計物不可事後補寫（無證據=未發生）

裁決：
- 缺 C1/C2/C3 任一 → STOP（不可在裁決後補）

### 6.4 必備檢核 D：版本一致性（VERSION Alignment）
- 檢核 D1：所有輸出都帶 version_ref
- 檢核 D2：policy_version 可在 VERSION_AUDIT 回溯
- 檢核 D3：制度/規則快照可在 TWSE_RULES 或 rule snapshot 引用中找到
- 檢核 D4：同一 correlation_id 不可混用互斥版本

裁決：
- D1 缺 → RETURN（若可補上引用）
- D2/D3/D4 → STOP（不可用不可信版本裁決）

### 6.5 必備檢核 E：UI 呈現義務（UI Must-Show）
- 檢核 E1：Risk Gate 決策（PASS/VETO）與 reason codes 必須可視化
- 檢核 E2：version_ref / correlation_id 必須可視化
- 檢核 E3：RETURN 時補齊清單必須可視化且阻斷前進
- 檢核 E4：不得以績效圖表弱化風險揭露（風險揭露優先）

裁決：
- 命中 GOV-UI-* → STOP（屬治理違規）

---

## 7. Gate 與 Risk Gate（L7）關係（Two-Gate Model）

### 7.1 兩個 Gate 的本質差異
- **Risk Gate（L7）**：裁決「可不可以交易」（PASS/VETO），最高否決權  
- **Governance Gate（L9）**：裁決「流程與證據是否具備合法性、可追溯性、可回放性」

### 7.2 協作規則（不可顛倒）
- L7 若 VETO：
  - L9 不得以任何理由放行
  - L9 僅能完成「完整記錄與回放包封存」的治理義務
- L7 若 PASS：
  - L9 仍可因治理缺陷 STOP/RETURN（例如缺版本、缺審計、引用非法）

---

## 8. Gate 審計輸出（Audit Artifacts｜不可縮減）

### 8.1 Governance Gate Artifact（最小欄位）
- `correlation_id`
- `session_id`
- `layer_id = L9`
- `decision`（PASS / RETURN / STOP）
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

### 8.2 RETURN 的補齊清單（必填）
- `return_required_items[]` 必須具體到「缺哪個引用/缺哪個 artifact/缺哪個版本」
- 禁止使用模糊詞（例如：補資料、再看看、可能不足）

---

## 9. UI 呈現義務（Gate 專屬 Must-Show）
UI 必須顯示：
- 主 Gate 決策：PASS / RETURN / STOP（不可模糊）
- gate_reason_codes（可展開）
- 若 RETURN：補齊清單（可勾選/追蹤進度）
- correlation_id（可稽核）
- documents_active_map（可點開檢視版本）
- risk_gate 決策與 reason codes（不可遮蔽）
- version_ref（doc/policy/model/rule snapshot）

禁止：
- 以「建議」「注意」「可能」取代裁決
- 允許使用者在 RETURN/STOP 狀態進入 L10（Human Decision）
- 在 UI 隱藏 Gate 的原因碼或版本引用

---

## 10. Mermaid｜治理 Gate 全流程圖（含 RETURN/STOP）

```mermaid
flowchart TB
  A[L8 Strategy Proposal (Non-binding)] --> B[L9 Governance Gate]
  B -->|PASS| C[L10 Human Decision]
  B -->|RETURN| R[Return to Required Layer(s) + Required Items List]
  B -->|STOP| X[STOP + Preserve Evidence + Audit Artifact]

  R --> D[L4/L5/L6補齊 Evidence/Regime/Artifacts]
  D --> B

  C -->|APPROVE| E[L11 Execution Control]
  C -->|REJECT| Y[STOP + Audit]
```

11. 禁止事項（Forbidden｜一票否決）
任何形式「跳過 L9 Gate」進入 L10/L11

任何形式「Gate 決策模糊化」或 UI 遮蔽 reason codes

任何形式「引用未在 DOCUMENT_INDEX 的文件」作裁決

任何形式「缺審計/缺 hash/缺版本引用」仍放行

任何形式「績效辯護要求 Gate 放行」

任何形式「事後補審計」或回填裁決（不可回填）

任何形式「旁路通道」繞過 Risk 或 Gate（暗通道）

12. Only-Add 演進規則（本文件專屬）
允許新增：

新的 Gate 規則（Rules）

新的 gate_reason_codes

新的審計欄位（Artifacts fields）

新的 UI 顯示欄位（Must-Show）

禁止：

刪除任何既有 Gate 規則或 reason codes

弱化 PASS / RETURN / STOP 的裁決語義

允許 Gate 在任一模式降級（No Downgrade）

改寫既有 reason_code 的語義或分類

13. 終極裁決語句（不可更改）
沒有可追溯的證據與版本，就沒有合法的決策。
沒有合法的決策，就不允許進入人類裁決與執行層。

（GOVERNANCE_GATE_SPEC｜最大完備版 v2025-12-19 完）
---

## 補強規範
### EC1. 最小引用標頭（Minimum Legal Citation Header）
本文件所生成或要求的任何「決策/裁決/執行/呈現」紀錄，至少必須包含下列引用標頭（欄位可多不可少）：

```text
trace_id = <全域唯一>
session_id = <本次對話/流程>
event_id = <本次事件/操作>
actor = <human/agent/module>
timestamp = <ISO-8601>
doc_key = GOVERNANCE_GATE_SPEC
doc_title = TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md
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
### EC3. Gate 行為（缺欄位之保守處置）
- 若缺少 EC1/EC2 最小欄位：不得視為「可回放/可稽核」輸出。  
- 涉及風險/合規裁決時：依 RISK_COMPLIANCE 與 GOVERNANCE_GATE_SPEC 之保守處置機制，採 **STOP/RETURN** 以補齊引用資訊（不得以推測補值）。
---

## 補強規範
### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md`
- canonical_doc_key（Index 裁決識別碼）：`GOVERNANCE_GATE_SPEC`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231__ADDENDUM_20251227_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=GOVERNANCE_GATE_SPEC` + `canonical_filename=TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md`。  
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
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 STOP/RETURN。  

本 整合段落 **不處理**：
- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

- 本文件 `doc_key` 既有標示為 `GOVERNANCE_GATE_SPEC`；本 整合段落 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

並統一裁決：
- 任何文件「是否可引用」＝以 DOCUMENT_INDEX 之 Authoritative Index（ACTIVE 表格）為準  
- 任何文件「治理等級 bucket」＝以 DOCUMENT_INDEX 之 A+ / A / B / C 分桶為準  
- 文件內自述之等級/狀態若與 Index 有張力：依 DOCUMENT_INDEX §6 採「保守處置」（STOP/RETURN/STOP；以既有 Gate/風控規範語義為準）

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
  - 一律視為「引用非法」→ 依 GOVERNANCE_GATE_SPEC 進行 STOP/RETURN（依其既有語義；不得補救）。

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
- 依 DOCUMENT_INDEX §6 採保守處置：不得形成裁決性輸出（PASS/APPROVE/EXECUTE 等）；必要時 RETURN/STOP。

---

## G5. 最終宣告（Freeze v1.0）

- 本 整合段落 為 Only-Add；不改寫本文件任何既有條款。  
- 本 整合段落 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。  
- 本 整合段落 目的僅在於消解引用歧義、避免 Gate 因 metadata/格式缺口而誤判，並確保全鏈路可稽核、可回放。