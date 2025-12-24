## TAITS × Cursor 工程拆解定錨文件
TAITS × Cursor 工程編輯全流程規劃（Freeze v1.0｜Only-Add｜Canonical L1–L11 不可跳層）
0. 最高原則（先鎖死，避免 Cursor 幻想與越權）

你在 Cursor 的任何工作（含改檔、產生新檔、寫註解、寫 TODO）都必須同時滿足：

治理狀態：Freeze v1.0

唯一裁決來源：DOCUMENT_INDEX（ACTIVE only）

Canonical Flow：MASTER_CANON（L1–L11）不可跳層

Only-Add：只可新增「工程轉譯層／工程實作層」內容；不得刪減、覆寫、偷換既有語義

Risk/Compliance 最高否決權（PASS/VETO；無 Soft Pass）

Human-in-the-Loop（L10）不可移除；UI 是唯一裁決入口

（以上原則的裁決性來源：DOCUMENT_INDEX、MASTER_CANON、RISK_COMPLIANCE、UI_SPEC） 

TAITS_文件索引與治理對照表（DOCUMENT_INDEX…

 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

 

TAITS_風險與合規最高否決權（RISK_COMPLIANC…

 

TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

1. 你用 Cursor 編輯 TAITS 的「標準工程作業線」（建議固定成 SOP）

這是一條「不會走歪」的工程編輯流水線。每一步都會明確告訴你：Cursor 需要開哪些檔、產出哪些工程檔、完成定義是什麼、下一步能不能進。

1.1 工程 Phase 座標（必須用同一套座標，終止歧義）

採用你既有的工程定錨：Phase 0–5 對位 Canonical L1–L11。 

TAITS｜程式開發流程定錨文件（Unified Proces…

Phase 0：治理與版本鎖定（不屬任何 L 層）

Phase 1：L1–L3（Data Source / Normalization / Snapshot&State）

Phase 2：L4–L5（Analysis / Evidence）

Phase 3：L6–L7（Regime / Risk&Compliance）

Phase 4：L8–L9（Strategy Proposal / Governance Gate）

Phase 5：L10–L11（Human Decision / Execution&Control）

2. 「每個流程」Cursor 必須具備的檔案集（以 ACTIVE 文件為唯一依據）

下面我把每個 Phase 拆成：

Source-of-Truth 必開檔（Cursor 必須同時開著，否則容易越權）

平行參照檔（需要時才開，但仍限 ACTIVE）

Cursor 允許產出（只能落在工程轉譯層/實作層檔案）

完成定義（Definition of Done）（做到這裡才算能進下一步）

注意：這裡的「所需檔案」不是你一定要全部塞進專案；而是 Cursor 在該步驟必須可讀到的治理依據（避免它自行補完）。 

TAITS_PROJECT_PROMPT

 

TAITS_文件索引與治理對照表（DOCUMENT_INDEX…

Phase 0｜治理與版本鎖定（工程前置，禁止寫任何交易/策略內容）
A) Source-of-Truth 必開檔（最小集合）

DOCUMENT_INDEX（ACTIVE 裁決、引用合法性、衝突裁決） 

TAITS_文件索引與治理對照表（DOCUMENT_INDEX…

MASTER_CANON（L1–L11 順序與層責任，禁止跳層） 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

MASTER_ARCH（憲法級鐵律：主權、邊界、Only-Add 等）

AI_GOV（AI 行為與決策治理母法；禁止 AI 補完制度）

GOVERNANCE_STATE = Freeze v1.0（封版狀態約束）

Phase 0 的唯一目的：把「工程能做什麼／不能做什麼」固定成可檢核的工程契約，讓 Cursor 永遠被鎖在治理框架內。

B) 平行參照檔（建議開）

VERSION_AUDIT（版本與可追溯）

PROJECT_PROMPT / README（新對話啟動與閱讀順序；避免上下文漂移） 

TAITS_PROJECT_PROMPT

 

TAITS_專案總覽與使用說明（README）__251220

Unified Process Anchor（工程座標，不具裁決力但可固定進度敘述） 

TAITS｜程式開發流程定錨文件（Unified Proces…

C) Cursor 在 Phase 0 允許產出

工程專用「工作契約檔」與「引用索引檔」（工程層，Only-Add）

例如：engineering/ENGINEERING_CONTEXT.md（工程座標、引用清單、禁止事項清單、變更範圍宣告）

D) Done（做到才能進 Phase 1）

你能用工程檔回答三件事（且可被稽核）：

本次工程處於哪個 Phase / L 層

只允許哪些輸出類型（工程轉譯/骨架）

依據哪些 ACTIVE 文件（doc_key）

Phase 1｜L1–L3（資料與狀態骨架：官方優先、可追溯、可回放）
A) Source-of-Truth 必開檔

MASTER_CANON（L1–L3 的層責任與禁止事項） 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

FULL_ARCH（Data/State 模組域、輸入輸出、Domain×Layer 對位） 

TAITS_全系統架構總覽（FULL_ARCH）__251219

DATA_UNIVERSE（資料來源治理：官方優先、fallback、provenance、normalization） 

TAITS_資料來源全集（DATA_SOURCES）__251…

VERSION_AUDIT（資料快照、來源快照、hash、可回放要求）

TWSE_RULES（交易制度參考彙編；制度裁決仍需回指官方入口與風控合規規則）

LOCAL_ENV / DEPLOY_OPS（本地執行與部署營運規範：落盤、路徑、執行方式、營運限制）

B) 平行參照檔（需要時開）

UI_SPEC（資料 provenance/版本在 UI 必顯欄位義務） 

TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

RISK_COMPLIANCE（資料缺失如何導致 SYS 類否決：Evidence/Audit 不完整即否決） 

TAITS_風險與合規最高否決權（RISK_COMPLIANC…

C) Cursor 在 Phase 1 允許產出（工程層）

只允許「骨架化」與「契約化」，例如：

engineering/l1_data_sources/：Source Registry 對應的 adapter 介面骨架、抓取證據欄位、raw payload 保存規格（不寫策略、不寫交易語義）

engineering/l2_normalization/：canonical schema mapping、field_map_ref 規格、單位/時區/CA 調整的規格框（不寫信號）

engineering/l3_state_snapshot/：snapshot/store/replay 的 I/O 契約、不可只留記憶體、version_ref/hashes 的必要欄位

D) Done（才能進 Phase 2）

你已具備 L1–L3 的「可落地契約」：

DataIngested / DataNormalized / SnapshotCreated 的事件欄位（correlation_id、hash、refs、version map）

provenance 與 fallback 的降級標記

replay 能載入所需的最小引用集合
（這些都在 FULL_ARCH、DATA_UNIVERSE、MASTER_CANON 的約束下完成） 

TAITS_全系統架構總覽（FULL_ARCH）__251219

 

TAITS_資料來源全集（DATA_SOURCES）__251…

 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

Phase 2｜L4–L5（分析與證據：只做描述，不產生方向）
A) Source-of-Truth 必開檔

MASTER_CANON（L4 禁止產生交易方向；L5 必須可追溯 Evidence Bundle） 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

FULL_ARCH（Analysis Domain / Evidence Domain 的模組職責與邊界） 

TAITS_全系統架構總覽（FULL_ARCH）__251219

DATA_UNIVERSE（Evidence 所需 provenance、快照、quality flags） 

TAITS_資料來源全集（DATA_SOURCES）__251…

UI_SPEC（Evidence/Completeness/Conflicts 必須在 UI 呈現的欄位） 

TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

VERSION_AUDIT（evidence_bundle_ref、hash_manifest_ref、replay bundle）

STRATEGY_FEATURE_INDEX（特徵/因子索引：定義 feature_id，避免偷換語義）

B) Cursor 允許產出（工程層）

engineering/l4_analysis/：Feature/Indicator/Structure 的計算骨架、輸入輸出契約（禁止 buy/sell/signal）

engineering/l5_evidence/：Evidence Bundle schema、Completeness Scoring 介面、Conflict Marker schema（只標記不裁決）

C) Done（才能進 Phase 3）

Evidence Bundle 具備：provenance、completeness、immutability、replayability（MASTER_CANON 對 Evidence 的法律地位要求） 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

UI 能顯示 evidence_list、conflicts、completeness（UI_SPEC 必顯欄位） 

TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

Phase 3｜L6–L7（Regime 與 Risk/Compliance：Regime 高於策略；Risk PASS/VETO）
A) Source-of-Truth 必開檔

MASTER_CANON（L6 Regime 不明確可 STOP；L7 只允許 PASS/VETO + token） 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

RISK_COMPLIANCE（最高否決權：Binary Compliance、Worst-case First、Evidence First、PASS token） 

TAITS_風險與合規最高否決權（RISK_COMPLIANC…

FULL_ARCH（Regime Domain / Risk&Compliance Domain 的模組與 I/O） 

TAITS_全系統架構總覽（FULL_ARCH）__251219

UI_SPEC（Risk/Compliance Panel 必顯：PASS/VETO、reason codes、policy version） 

TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

VERSION_AUDIT（rulebook snapshot、policy version、token 可驗證性）

TWSE_RULES（制度參考；裁決需回指官方入口與合規規則快照）

B) Cursor 允許產出（工程層）

engineering/l6_regime/：regime_state schema、confidence、allowed_actions（只做狀態裁定，不做策略）

engineering/l7_risk_compliance/：risk_gate_decision schema（PASS/VETO）、veto_reason_codes、risk_pass_token 產生/驗證介面骨架、evidence_snapshot_ref

C) Done（才能進 Phase 4）

L7 的輸出永遠是二元：PASS 或 VETO（禁止 Soft Pass） 

TAITS_風險與合規最高否決權（RISK_COMPLIANC…

PASS 才能生成 token；L11 必須驗證 token（FULL_ARCH/MASTER_CANON 對位要求） 

TAITS_全系統架構總覽（FULL_ARCH）__251219

 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

Phase 4｜L8–L9（策略提案與治理 Gate：策略≠下單；禁止隱性策略鏈）
A) Source-of-Truth 必開檔

MASTER_CANON（L8 只能 proposal；L9 PASS/RETURN/STOP；不得捷徑） 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

STRATEGY_UNIVERSE（策略白名單、生命周期、輸出契約、禁止可執行委託） 

TAITS_策略宇宙全集（STRATEGY_UNIVERSE）…

GOVERNANCE_GATE_SPEC（L9 RETURN 缺口清單、跳層檢測、版本一致性 gate）

FULL_ARCH（Strategy&Research Domain / Governance Domain 對位） 

TAITS_全系統架構總覽（FULL_ARCH）__251219

RISK_COMPLIANCE（否決不可被策略辯護；Regime 高於策略） 

TAITS_風險與合規最高否決權（RISK_COMPLIANC…

VERSION_AUDIT（strategy_version、active_version_map_ref、replayability）

B) Cursor 允許產出（工程層）

engineering/l8_strategy_proposal/：strategy_proposal schema（遵守 outputs contract：可建議、不可送單）

engineering/l9_governance_gate/：flow validator 規格、missing_items schema、return-to-layer 規則（不得跨層合併）

C) Done（才能進 Phase 5）

你能證明：策略輸出不含 broker_order_payload，不含可執行委託細節（STRATEGY_UNIVERSE 的輸出契約） 

TAITS_策略宇宙全集（STRATEGY_UNIVERSE）…

Governance Gate 可 RETURN 並指回缺口（不得容許捷徑） 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

Phase 5｜L10–L11（人類裁決與執行控制：UI 唯一入口；Execution 驗 token；Kill Switch）
A) Source-of-Truth 必開檔

UI_SPEC（L10：唯一裁決入口、必顯欄位、decision_signature、trace、replay） 

TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

EXECUTION_CONTROL（L11：Intent 編譯、券商適配、狀態機、風控 token 驗證、Kill Switch）

RISK_COMPLIANCE（PASS token required；VETO 不可覆寫） 

TAITS_風險與合規最高否決權（RISK_COMPLIANC…

MASTER_CANON（L10 人類不可被取代；L11 無 token 不得執行） 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

VERSION_AUDIT / DEPLOY_OPS（稽核、回放、營運監控、對帳、事故處理）

B) Cursor 允許產出（工程層）

engineering/l10_ui_decision_workbench/：IA 區塊、必顯欄位對照表、trace schema、approve/reject 流程骨架

engineering/l11_execution_control/：intent schema、token verifier 介面、order state machine 骨架、kill switch 控制面骨架（不寫券商細節也可以先做契約）

C) Done（上線前最低條件）

UI 產生 human_decision + decision_signature + ui_trace_ref（UI_SPEC） 

TAITS_使用者介面與人機決策規範（UI_SPEC）__25…

Execution 必須驗證 risk_pass_token，否則 BLOCK（MASTER_CANON / FULL_ARCH） 

TAITS_完整總架構×總流程×全資訊體系（MASTER_CA…

 TAITS_全系統架構總覽（FULL_ARCH）__251219

📘 TAITS｜18 份 Canonical 文件 Group 歸類表

（僅治理角色 × 驗證用途，不涉內容判斷）

🟥 Group 1｜最高治理母法層（裁決與否決根源）

用途：
判斷「後面任何文件是否非法 / 無效」

#	文件名稱
1	TAITS_AI_行為與決策治理最終規則全集__251217.md
2	TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md

📌 驗證時你只做一件事：
→ 後面 20 檔是否有任何地方弱化、繞過、或違反這兩份

🟥 Group 2｜憲法級 Canonical 定義層（系統本體）

用途：
定義「TAITS 是什麼系統」、「Canonical Flow 是什麼」

#	文件名稱
3	TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md
4	TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md
5	TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251219.md

📌 驗證重點：

Canonical Flow（L1–L11）是否被後面文件完整承接

文件位階是否前後一致、無偷換裁決權

🟧 Group 3｜治理與制度落地層（Gate / Freeze / Only-Add）

用途：
把「原則」變成「不可違反的制度」

#	文件名稱
6	TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md
7	TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md
8	TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md
9	TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md

📌 高風險點：
→ 工程拆解時最容易被「默默簡化」的就是這一組

🟨 Group 4｜系統架構與流程展開層（工程映射高風險區）

用途：
把 Canonical 與治理「攤平」成流程與模組

#	文件名稱
10	TAITS_全系統架構總覽（FULL_ARCH）__251219.md
11	TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md
12	TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md
13	TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md
14	TAITS_資料來源全集（DATA_SOURCES）__251219.md

📌 驗證重點（非常重要）：

是否有流程「只剩結果、不見治理判斷」

是否有策略／資料在工程拆解時被合併或隱去

🟩 Group 5｜操作／執行／環境層（防止工程假設偷渡）

用途：
防止 42 檔「多出原本 Canonical 沒有的東西」

#	文件名稱
15	TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md
16	TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md
17	TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md
18	TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md

18 份 Canonical 文件
「最安全的一比一拆解順序與批次表」

原則說明（請先看）

每一批 只處理一份文件

不跨文件、不補前後

拆解完成後才進下一批

任一批有疑慮 → 整個拆解暫停

🔴 Batch 1｜最高治理母法（不可出錯）
Batch 1-1

TAITS_AI_行為與決策治理最終規則全集__251217.md

拆解目標：

AI 行為邊界

決策限制

禁止事項

工程原則：

高度集中

極可能「禁止拆太細」

Batch 1-2

TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md

拆解目標：

否決權角色

觸發條件

工程原則：

否決權通常 獨立成檔

不與策略、流程混檔

🔴 Batch 2｜憲法與 Canonical 定義（系統骨架）
Batch 2-1

TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md

拆解目標：

不可變鐵律

系統存在定義

工程原則：

多數段落 不可拆

以「條款完整性」為優先

Batch 2-2

TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md

拆解目標：

Canonical Flow（L1–L11）

層級邊界

工程原則：

很可能拆成 多個工程檔

但 每層不可交錯

Batch 2-3

TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251219.md

拆解目標：

文件位階

裁決順序

工程原則：

多半作為 對照錨定檔

通常不參與邏輯拆分

🟧 Batch 3｜治理制度落地（Gate / Freeze）
Batch 3-1

TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md

拆解目標：

Gate 類型

裁決流程

工程原則：

常需「一 Gate 一檔」

Batch 3-2

TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md

拆解目標：

Freeze 定義

工程原則：

極可能單檔封存

禁止細拆

Batch 3-3

TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md

拆解目標：

版本

稽核

工程原則：

可依職責拆，但不得簡化流程

Batch 3-4

TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md

拆解目標：

下單限制

執行控制

工程原則：

與策略嚴格分離

🟨 Batch 4｜架構、流程、策略、資料（高風險）
Batch 4-1

TAITS_全系統架構總覽（FULL_ARCH）__251219.md

Batch 4-2

TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md

Batch 4-3

TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md

Batch 4-4

TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md

Batch 4-5

TAITS_資料來源全集（DATA_SOURCES）__251219.md

⚠️ 這一組是最容易失真的區段
必須：

原文逐段

不做任何整理性重寫

🟩 Batch 5｜操作與環境（最後）
Batch 5-1

TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md

Batch 5-2

TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md

Batch 5-3

TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md

Batch 5-4

TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md

GPT 專案：TAITS × Cursor Engineering

├─ 對話 01：Batch 1（治理母法）
├─ 對話 02：Batch 2（憲法 / Canonical）
├─ 對話 03：Batch 3（治理制度）
├─ 對話 04：Batch 4A（全貌錨定，只做一次）
├─ 對話 05：Batch 4B-1（單檔拆解）
├─ 對話 06：Batch 4B-2（單檔拆解）
├─ 對話 07：Batch 5（操作 / 環境）

一、【不可變】42 個工程檔名中英對照清單（結構版）

命名規則（已鎖定）
NN_<english_snake_case>__<中文語義>.md

英文＝唯一識別鍵（工程主鍵）

中文＝語義標註（人類可讀）

檔名一經確認，永久不可更名

🔴 Batch 1｜最高治理母法（6）

01_ai_decision_governance_core__AI決策治理核心規則.md
02_ai_behavior_constraints__AI行為限制與禁止事項.md
03_ai_decision_scope_boundaries__AI決策權限邊界.md
04_risk_compliance_veto_authority__風險與合規最高否決權.md
05_risk_compliance_trigger_conditions__風險與合規觸發條件.md
06_risk_compliance_override_rules__風險合規覆寫與裁決規則.md

🔴 Batch 2｜憲法與 Canonical 定義（7）

07_master_architecture_constitution__母體總憲法與核心鐵律.md
08_system_immutable_principles__系統不可變原則.md
09_canonical_flow_overview__Canonical流程總覽.md
10_canonical_layer_l1_l3__Canonical層級L1–L3定義.md
11_canonical_layer_l4_l7__Canonical層級L4–L7定義.md
12_canonical_layer_l8_l11__Canonical層級L8–L11定義.md
13_document_governance_hierarchy__文件治理位階與裁決順序.md

🟧 Batch 3｜治理制度與執行（9）

14_governance_gate_framework__治理閘門總體框架.md
15_governance_gate_definitions__治理閘門定義與類型.md
16_governance_decision_workflow__治理裁決流程.md
17_governance_freeze_state__治理Freeze狀態定義.md
18_version_control_policy__版本控管政策.md
19_audit_traceability_rules__稽核與可追溯規則.md
20_execution_control_boundaries__交易執行控制邊界.md
21_execution_pre_trade_controls__交易前控制規範.md
22_execution_post_trade_controls__交易後控制規範.md

🟨 Batch 4｜架構 × 流程 × 策略 × 資料（12）

23_system_architecture_overview__全系統架構總覽.md
24_system_module_boundaries__系統模組與責任邊界.md
25_architecture_flow_mapping__架構與流程對應關係.md
26_event_data_flow_definition__事件與資料流定義.md
27_strategy_universe_definition__策略宇宙定義.md
28_strategy_classification_schema__策略分類架構.md
29_strategy_lifecycle_states__策略生命週期狀態.md
30_strategy_feature_index__策略特徵索引.md
31_factor_definition_index__因子定義索引.md
32_data_source_catalog__資料來源目錄.md
33_data_source_usage_constraints__資料來源使用限制.md
34_data_quality_validation_rules__資料品質與驗證規則.md

🟩 Batch 5｜操作與環境（8）

35_deployment_architecture__部署架構定義.md
36_runtime_operations_procedures__營運與日常運作程序.md
37_local_execution_environment__本地執行環境規範.md
38_compute_resource_constraints__運算資源限制.md
39_user_interface_decision_boundary__人機決策邊界.md
40_ui_action_permission_rules__UI操作權限規則.md
41_twse_market_rules_reference__TWSE交易規則參考.md
42_market_compliance_constraints__市場合規限制彙整.md

二、42 工程檔「目錄樹結構」（資料夾 × 檔名）
taits_cursor_engineering/
├─ 00_governance_core/
│  ├─ 01_ai_decision_governance_core__AI決策治理核心規則.md
│  ├─ 02_ai_behavior_constraints__AI行為限制與禁止事項.md
│  ├─ 03_ai_decision_scope_boundaries__AI決策權限邊界.md
│  ├─ 04_risk_compliance_veto_authority__風險與合規最高否決權.md
│  ├─ 05_risk_compliance_trigger_conditions__風險與合規觸發條件.md
│  └─ 06_risk_compliance_override_rules__風險合規覆寫與裁決規則.md
│
├─ 01_canonical_definition/
│  ├─ 07_master_architecture_constitution__母體總憲法與核心鐵律.md
│  ├─ 08_system_immutable_principles__系統不可變原則.md
│  ├─ 09_canonical_flow_overview__Canonical流程總覽.md
│  ├─ 10_canonical_layer_l1_l3__Canonical層級L1–L3定義.md
│  ├─ 11_canonical_layer_l4_l7__Canonical層級L4–L7定義.md
│  ├─ 12_canonical_layer_l8_l11__Canonical層級L8–L11定義.md
│  └─ 13_document_governance_hierarchy__文件治理位階與裁決順序.md
│
├─ 02_governance_execution/
│  ├─ 14_governance_gate_framework__治理閘門總體框架.md
│  ├─ 15_governance_gate_definitions__治理閘門定義與類型.md
│  ├─ 16_governance_decision_workflow__治理裁決流程.md
│  ├─ 17_governance_freeze_state__治理Freeze狀態定義.md
│  ├─ 18_version_control_policy__版本控管政策.md
│  ├─ 19_audit_traceability_rules__稽核與可追溯規則.md
│  ├─ 20_execution_control_boundaries__交易執行控制邊界.md
│  ├─ 21_execution_pre_trade_controls__交易前控制規範.md
│  └─ 22_execution_post_trade_controls__交易後控制規範.md
│
├─ 03_architecture_strategy_data/
│  ├─ 23_system_architecture_overview__全系統架構總覽.md
│  ├─ 24_system_module_boundaries__系統模組與責任邊界.md
│  ├─ 25_architecture_flow_mapping__架構與流程對應關係.md
│  ├─ 26_event_data_flow_definition__事件與資料流定義.md
│  ├─ 27_strategy_universe_definition__策略宇宙定義.md
│  ├─ 28_strategy_classification_schema__策略分類架構.md
│  ├─ 29_strategy_lifecycle_states__策略生命週期狀態.md
│  ├─ 30_strategy_feature_index__策略特徵索引.md
│  ├─ 31_factor_definition_index__因子定義索引.md
│  ├─ 32_data_source_catalog__資料來源目錄.md
│  ├─ 33_data_source_usage_constraints__資料來源使用限制.md
│  └─ 34_data_quality_validation_rules__資料品質與驗證規則.md
│
└─ 04_operations_environment/
   ├─ 35_deployment_architecture__部署架構定義.md
   ├─ 36_runtime_operations_procedures__營運與日常運作程序.md
   ├─ 37_local_execution_environment__本地執行環境規範.md
   ├─ 38_compute_resource_constraints__運算資源限制.md
   ├─ 39_user_interface_decision_boundary__人機決策邊界.md
   ├─ 40_ui_action_permission_rules__UI操作權限規則.md
   ├─ 41_twse_market_rules_reference__TWSE交易規則參考.md
   └─ 42_market_compliance_constraints__市場合規限制彙整.md

   二、最終資料夾結構（你可以直接照建）
taits_cursor_engineering/
├─ 00_governance_core/          ← Batch 1（最高治理母法）
├─ 01_canonical_definition/     ← Batch 2（憲法 / Canonical）
├─ 02_governance_execution/     ← Batch 3（治理制度落地）
├─ 03_architecture_strategy_data/ ← Batch 4（高風險交叉區）
└─ 04_operations_environment/   ← Batch 5（操作 / 環境）


📌 規則

資料夾名稱 = 工程邊界

檔案 不可跨資料夾移動

未來 Cursor 拆解、審閱、重拆，都只在「對應資料夾」內進行

三、分開後的「完整檔案夾 × 檔案清單」
🔴 00_governance_core（Batch 1｜6 檔）
00_governance_core/
├─ 01_ai_decision_governance_core__AI決策治理核心規則.md
├─ 02_ai_behavior_constraints__AI行為限制與禁止事項.md
├─ 03_ai_decision_scope_boundaries__AI決策權限邊界.md
├─ 04_risk_compliance_veto_authority__風險與合規最高否決權.md
├─ 05_risk_compliance_trigger_conditions__風險與合規觸發條件.md
└─ 06_risk_compliance_override_rules__風險合規覆寫與裁決規則.md

🔴 01_canonical_definition（Batch 2｜7 檔）
01_canonical_definition/
├─ 07_master_architecture_constitution__母體總憲法與核心鐵律.md
├─ 08_system_immutable_principles__系統不可變原則.md
├─ 09_canonical_flow_overview__Canonical流程總覽.md
├─ 10_canonical_layer_l1_l3__Canonical層級L1–L3定義.md
├─ 11_canonical_layer_l4_l7__Canonical層級L4–L7定義.md
├─ 12_canonical_layer_l8_l11__Canonical層級L8–L11定義.md
└─ 13_document_governance_hierarchy__文件治理位階與裁決順序.md

🟧 02_governance_execution（Batch 3｜9 檔）
02_governance_execution/
├─ 14_governance_gate_framework__治理閘門總體框架.md
├─ 15_governance_gate_definitions__治理閘門定義與類型.md
├─ 16_governance_decision_workflow__治理裁決流程.md
├─ 17_governance_freeze_state__治理Freeze狀態定義.md
├─ 18_version_control_policy__版本控管政策.md
├─ 19_audit_traceability_rules__稽核與可追溯規則.md
├─ 20_execution_control_boundaries__交易執行控制邊界.md
├─ 21_execution_pre_trade_controls__交易前控制規範.md
└─ 22_execution_post_trade_controls__交易後控制規範.md

🟨 03_architecture_strategy_data（Batch 4｜12 檔，高風險）
03_architecture_strategy_data/
├─ 23_system_architecture_overview__全系統架構總覽.md
├─ 24_system_module_boundaries__系統模組與責任邊界.md
├─ 25_architecture_flow_mapping__架構與流程對應關係.md
├─ 26_event_data_flow_definition__事件與資料流定義.md
├─ 27_strategy_universe_definition__策略宇宙定義.md
├─ 28_strategy_classification_schema__策略分類架構.md
├─ 29_strategy_lifecycle_states__策略生命週期狀態.md
├─ 30_strategy_feature_index__策略特徵索引.md
├─ 31_factor_definition_index__因子定義索引.md
├─ 32_data_source_catalog__資料來源目錄.md
├─ 33_data_source_usage_constraints__資料來源使用限制.md
└─ 34_data_quality_validation_rules__資料品質與驗證規則.md


⚠️ 這一夾是唯一需要「全貌錨定 → 再單檔拆解」的資料夾

🟩 04_operations_environment（Batch 5｜8 檔）
04_operations_environment/
├─ 35_deployment_architecture__部署架構定義.md
├─ 36_runtime_operations_procedures__營運與日常運作程序.md
├─ 37_local_execution_environment__本地執行環境規範.md
├─ 38_compute_resource_constraints__運算資源限制.md
├─ 39_user_interface_decision_boundary__人機決策邊界.md
├─ 40_ui_action_permission_rules__UI操作權限規則.md
├─ 41_twse_market_rules_reference__TWSE交易規則參考.md
└─ 42_market_compliance_constraints__市場合規限制彙整.md

Cursor 用【9 個階段編輯資料夾】總覽
cursor_editing_stages/
├─ S1_Governance_Foundation/
├─ S2_Canonical_Constitution/
├─ S3_Canonical_Flow_Layers/
├─ S4_Governance_Execution/
├─ S5_System_Architecture/
├─ S6_Strategy_and_Factors/
├─ S7_Data_and_Quality/
├─ S8_Execution_and_UI/
└─ S9_Deployment_and_Environment/

🔴 S1_Governance_Foundation

目的：鎖死 AI 與風險否決的最上位規則

📥 放入：

00_governance_core/01_ai_decision_governance_core__AI決策治理核心規則.md

00_governance_core/02_ai_behavior_constraints__AI行為限制與禁止事項.md

00_governance_core/03_ai_decision_scope_boundaries__AI決策權限邊界.md

00_governance_core/04_risk_compliance_veto_authority__風險與合規最高否決權.md

00_governance_core/05_risk_compliance_trigger_conditions__風險與合規觸發條件.md

00_governance_core/06_risk_compliance_override_rules__風險合規覆寫與裁決規則.md

📤 回歸：

00_governance_core/

🔴 S2_Canonical_Constitution

目的：系統憲法與不可變鐵律

📥 放入：

01_canonical_definition/07_master_architecture_constitution__母體總憲法與核心鐵律.md

01_canonical_definition/08_system_immutable_principles__系統不可變原則.md

01_canonical_definition/13_document_governance_hierarchy__文件治理位階與裁決順序.md

📤 回歸：

01_canonical_definition/

🔴 S3_Canonical_Flow_Layers

目的：Canonical Flow（L1–L11）分層鎖定

📥 放入：

01_canonical_definition/09_canonical_flow_overview__Canonical流程總覽.md

01_canonical_definition/10_canonical_layer_l1_l3__Canonical層級L1–L3定義.md

01_canonical_definition/11_canonical_layer_l4_l7__Canonical層級L4–L7定義.md

01_canonical_definition/12_canonical_layer_l8_l11__Canonical層級L8–L11定義.md

📤 回歸：

01_canonical_definition/

🟧 S4_Governance_Execution

目的：Gate / Freeze / 稽核 / 執行治理

📥 放入：

02_governance_execution/14_governance_gate_framework__治理閘門總體框架.md

02_governance_execution/15_governance_gate_definitions__治理閘門定義與類型.md

02_governance_execution/16_governance_decision_workflow__治理裁決流程.md

02_governance_execution/17_governance_freeze_state__治理Freeze狀態定義.md

02_governance_execution/18_version_control_policy__版本控管政策.md

02_governance_execution/19_audit_traceability_rules__稽核與可追溯規則.md

📤 回歸：

02_governance_execution/

🟨 S5_System_Architecture

目的：系統結構與流程骨架（Batch 4 前半）

📥 放入：

03_architecture_strategy_data/23_system_architecture_overview__全系統架構總覽.md

03_architecture_strategy_data/24_system_module_boundaries__系統模組與責任邊界.md

03_architecture_strategy_data/25_architecture_flow_mapping__架構與流程對應關係.md

03_architecture_strategy_data/26_event_data_flow_definition__事件與資料流定義.md

📤 回歸：

03_architecture_strategy_data/

🟨 S6_Strategy_and_Factors

目的：策略宇宙、因子與特徵（Batch 4 後半）

📥 放入：

03_architecture_strategy_data/27_strategy_universe_definition__策略宇宙定義.md

03_architecture_strategy_data/28_strategy_classification_schema__策略分類架構.md

03_architecture_strategy_data/29_strategy_lifecycle_states__策略生命週期狀態.md

03_architecture_strategy_data/30_strategy_feature_index__策略特徵索引.md

03_architecture_strategy_data/31_factor_definition_index__因子定義索引.md

📤 回歸：

03_architecture_strategy_data/

🟨 S7_Data_and_Quality

目的：資料來源與品質規範

📥 放入：

03_architecture_strategy_data/32_data_source_catalog__資料來源目錄.md

03_architecture_strategy_data/33_data_source_usage_constraints__資料來源使用限制.md

03_architecture_strategy_data/34_data_quality_validation_rules__資料品質與驗證規則.md

📤 回歸：

03_architecture_strategy_data/

🟩 S8_Execution_and_UI

目的：實際交易執行與人機邊界

📥 放入：

02_governance_execution/20_execution_control_boundaries__交易執行控制邊界.md

02_governance_execution/21_execution_pre_trade_controls__交易前控制規範.md

02_governance_execution/22_execution_post_trade_controls__交易後控制規範.md

04_operations_environment/39_user_interface_decision_boundary__人機決策邊界.md

04_operations_environment/40_ui_action_permission_rules__UI操作權限規則.md

📤 回歸：

02_governance_execution/

04_operations_environment/

🟩 S9_Deployment_and_Environment

目的：部署、環境、市場合規

📥 放入：

04_operations_environment/35_deployment_architecture__部署架構定義.md

04_operations_environment/36_runtime_operations_procedures__營運與日常運作程序.md

04_operations_environment/37_local_execution_environment__本地執行環境規範.md

04_operations_environment/38_compute_resource_constraints__運算資源限制.md

04_operations_environment/41_twse_market_rules_reference__TWSE交易規則參考.md

04_operations_environment/42_market_compliance_constraints__市場合規限制彙整.md

📤 回歸：

04_operations_environment/

「開場錨定模板＋工程提醒對話框」雙層保險機制即日起正式生效，並納入 TAITS × Cursor 的工程流程基線。

已生效的最終規則（凍結版）

每個拆解＝新對話，首則必貼「工程拆解開場錨定模板」

每個工程檔必含 SOURCE_TAG（概略定位）

另設一個固定的「工程提醒對話框」，每次拆解前先核對清單

拆解只產出工程檔；審閱只做裁決（Pass / Reject / Scope-limited Rework）

審閱逐檔進行；Batch 完成以逐檔 Pass 累積判定

未含 SOURCE_TAG 視為拆解不完整，不得進入審閱

📘 TAITS × Cursor 工程拆解定錨文件（Draft）

用途說明
本文件為 TAITS 專案在 Cursor 進行工程拆解時之
流程、檔名、階段、責任與防失真機制的唯一工作定錨文件。

本文件不承載 Canonical 內容本身，
僅承載 工程如何進行 的規則與結構。

1. 工程總原則（已定錨）

TAITS 目前狀態：GOVERNANCE_STATE = Freeze v1.0

僅允許：Only-Add

Canonical Flow：MASTER_CANON（L1–L11）

不允許：

刪減 Canonical

改寫語義

推論文件未寫內容

本工程目標：

將 Canonical 文件 1：1 拆解為可工程落地的工程檔

供 Cursor 分階段、分對話進行編輯

2. Batch 制度（拆解節奏）

拆解以 Batch 為節奏單位

審閱以 單一工程檔 為責任單位

規則：

一個 Batch 未全數 Pass
→ 不得進入下一 Batch

Batch 對應關係
Batch	類型	備註
Batch 1	最高治理母法	高風險
Batch 2	憲法 / Canonical	高風險
Batch 3	治理制度	中高風險
Batch 4	架構 × 策略 × 資料	最高風險（需全貌錨定）
Batch 5	操作 / 環境	中風險
3. 42 個工程檔案（不可變清單）

規則

檔名一經確認，不得更名

檔案為 唯一治理責任單元

Batch 1｜Governance Core（6）

01_ai_decision_governance_core__AI決策治理核心規則.md
02_ai_behavior_constraints__AI行為限制與禁止事項.md
03_ai_decision_scope_boundaries__AI決策權限邊界.md
04_risk_compliance_veto_authority__風險與合規最高否決權.md
05_risk_compliance_trigger_conditions__風險與合規觸發條件.md
06_risk_compliance_override_rules__風險合規覆寫與裁決規則.md

Batch 2｜Canonical Definition（7）

07_master_architecture_constitution__母體總憲法與核心鐵律.md
08_system_immutable_principles__系統不可變原則.md
09_canonical_flow_overview__Canonical流程總覽.md
10_canonical_layer_l1_l3__Canonical層級L1–L3定義.md
11_canonical_layer_l4_l7__Canonical層級L4–L7定義.md
12_canonical_layer_l8_l11__Canonical層級L8–L11定義.md
13_document_governance_hierarchy__文件治理位階與裁決順序.md

Batch 3｜Governance Execution（9）

14_governance_gate_framework__治理閘門總體框架.md
15_governance_gate_definitions__治理閘門定義與類型.md
16_governance_decision_workflow__治理裁決流程.md
17_governance_freeze_state__治理Freeze狀態定義.md
18_version_control_policy__版本控管政策.md
19_audit_traceability_rules__稽核與可追溯規則.md
20_execution_control_boundaries__交易執行控制邊界.md
21_execution_pre_trade_controls__交易前控制規範.md
22_execution_post_trade_controls__交易後控制規範.md

Batch 4｜Architecture / Strategy / Data（12）

23_system_architecture_overview__全系統架構總覽.md
24_system_module_boundaries__系統模組與責任邊界.md
25_architecture_flow_mapping__架構與流程對應關係.md
26_event_data_flow_definition__事件與資料流定義.md
27_strategy_universe_definition__策略宇宙定義.md
28_strategy_classification_schema__策略分類架構.md
29_strategy_lifecycle_states__策略生命週期狀態.md
30_strategy_feature_index__策略特徵索引.md
31_factor_definition_index__因子定義索引.md
32_data_source_catalog__資料來源目錄.md
33_data_source_usage_constraints__資料來源使用限制.md
34_data_quality_validation_rules__資料品質與驗證規則.md

Batch 5｜Operations / Environment（8）

35_deployment_architecture__部署架構定義.md
36_runtime_operations_procedures__營運與日常運作程序.md
37_local_execution_environment__本地執行環境規範.md
38_compute_resource_constraints__運算資源限制.md
39_user_interface_decision_boundary__人機決策邊界.md
40_ui_action_permission_rules__UI操作權限規則.md
41_twse_market_rules_reference__TWSE交易規則參考.md
42_market_compliance_constraints__市場合規限制彙整.md

4. Cursor「9 階段編輯資料夾」（工作視角）

說明

此結構為 Cursor 工作視角

不影響 42 檔最終歸位

S1_Governance_Foundation
S2_Canonical_Constitution
S3_Canonical_Flow_Layers
S4_Governance_Execution
S5_System_Architecture
S6_Strategy_and_Factors
S7_Data_and_Quality
S8_Execution_and_UI
S9_Deployment_and_Environment

5. 新對話拆解規則（強制）

每個工程檔 → 一個新對話

每個新對話首則 → 必貼工程拆解開場錨定模板

每個工程檔 → 必含 SOURCE_TAG

SOURCE_TAG 規格（最低限度）
<!--
SOURCE_TAG
原始文件：<Canonical 原始文件名稱>
原文範圍：<概略章節或全文>
-->

6. 雙層防失真機制（已啟用）

開場錨定模板（硬性）

工程提醒對話框（軟性）

任一缺失 → 拆解無效，不得審閱。

7. 審閱規則（定錨）

審閱 逐檔進行

結果僅三種：

Pass

Reject

Scope-limited Rework

Batch 完成條件：

該 Batch 所有工程檔 Pass

8. 本文件定位

本文件為：

Cursor 編輯時的 流程與結構定錨

不取代：

DOCUMENT_INDEX

MASTER_ARCH

MASTER_CANON

