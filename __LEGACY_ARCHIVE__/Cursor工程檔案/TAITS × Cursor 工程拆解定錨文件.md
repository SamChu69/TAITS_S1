# 📘 TAITS × Cursor 工程拆解定錨文件  
Version: Freeze v1.0  
適用狀態：GOVERNANCE_STATE = Freeze v1.0  
變更原則：Only-Add（只可新增，不可刪減、覆寫、偷換語義）

---

## 0. 文件定位（工程母錨定）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）**  
在 **Cursor** 中進行工程拆解、編輯、審閱、落地時之：

**唯一工程流程與結構定錨文件**。

### 本文件用途
- 防止新對話 / token 增長造成語義漂移
- 鎖定工程節奏、檔名、責任單元
- 確保 Canonical 文件可 1：1 工程化落地

### 本文件不做的事
- 不承載 Canonical 內容本身
- 不取代 DOCUMENT_INDEX / MASTER_ARCH / MASTER_CANON
- 不新增任何制度或語義

---

## 1. 最高工程原則（不可違反）

- 目前狀態：**GOVERNANCE_STATE = Freeze v1.0**
- 唯一裁決依據：DOCUMENT_INDEX 中列為 ACTIVE 之文件
- Canonical Flow：MASTER_CANON（L1–L11），不得跳層
- 僅允許：**Only-Add**
- Risk / Compliance 具 **最高否決權**
- Human-in-the-Loop（L10）不可移除
- UI 為唯一人機裁決入口

---

## 2. Batch 拆解制度（工程節奏）

### 核心規則
- **拆解以 Batch 為節奏單位**
- **審閱以單一工程檔為責任單位**
- 任一 Batch 未全數 Pass  
  → **不得進入下一 Batch**

### Batch 總覽

| Batch | 類型 | 風險等級 |
|---|---|---|
| Batch 1 | 最高治理母法 | 🔴 極高 |
| Batch 2 | 憲法 / Canonical | 🔴 極高 |
| Batch 3 | 治理制度落地 | 🟧 中高 |
| Batch 4 | 架構 × 策略 × 資料 | 🔴 最高 |
| Batch 5 | 操作 / 環境 | 🟩 中 |

---

## 3. 原始 Canonical 母檔（18 份）

1. TAITS_AI_行為與決策治理最終規則全集__251217.md  
2. TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md  
3. TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md  
4. TAITS_全系統架構總覽（FULL_ARCH）__251219.md  
5. TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md  
6. TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md  
7. TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md  
8. TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md  
9. TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md  
10. TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md  
11. TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md  
12. TAITS_資料來源全集（DATA_SOURCES）__251219.md  
13. TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md  
14. TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md  
15. TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md  
16. TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md  
17. TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251219.md  
18. TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251219.md  

---

## 4. Batch × Canonical 母檔對照

### Batch 1｜Governance Core
來源母檔：1、6  
→ 工程檔：01–06

### Batch 2｜Canonical Definition
來源母檔：2、3、18  
→ 工程檔：07–13

### Batch 3｜Governance Execution
來源母檔：7、8、9、17  
→ 工程檔：14–22

### Batch 4｜Architecture / Strategy / Data
來源母檔：4、5、10、11、12  
→ 工程檔：23–34

### Batch 5｜Operations / Environment
來源母檔：13、14、15、16  
→ 工程檔：35–42

---

## 5. 拆解後「工程檔案名」定錨（42 檔，不可變）

### 命名規則
NN_<english_snake_case>__<中文語義>.md

yaml
複製程式碼

- NN：01–42，不得跳號
- 檔名一經確認，不得更名
- 一檔 = 一個治理責任單元 = 一個 Cursor 新對話

### Batch 1（01–06）
01_ai_decision_governance_core__AI決策治理核心規則.md  
02_ai_behavior_constraints__AI行為限制與禁止事項.md  
03_ai_decision_scope_boundaries__AI決策權限邊界.md  
04_risk_compliance_veto_authority__風險與合規最高否決權.md  
05_risk_compliance_trigger_conditions__風險與合規觸發條件.md  
06_risk_compliance_override_rules__風險合規覆寫與裁決規則.md  

### Batch 2（07–13）
07_master_architecture_constitution__母體總憲法與核心鐵律.md  
08_system_immutable_principles__系統不可變原則.md  
09_canonical_flow_overview__Canonical流程總覽.md  
10_canonical_layer_l1_l3__Canonical層級L1–L3定義.md  
11_canonical_layer_l4_l7__Canonical層級L4–L7定義.md  
12_canonical_layer_l8_l11__Canonical層級L8–L11定義.md  
13_document_governance_hierarchy__文件治理位階與裁決順序.md  

### Batch 3（14–22）
14_governance_gate_framework__治理閘門總體框架.md  
15_governance_gate_definitions__治理閘門定義與類型.md  
16_governance_decision_workflow__治理裁決流程.md  
17_governance_freeze_state__治理Freeze狀態定義.md  
18_version_control_policy__版本控管政策.md  
19_audit_traceability_rules__稽核與可追溯規則.md  
20_execution_control_boundaries__交易執行控制邊界.md  
21_execution_pre_trade_controls__交易前控制規範.md  
22_execution_post_trade_controls__交易後控制規範.md  

### Batch 4（23–34）
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

### Batch 5（35–42）
35_deployment_architecture__部署架構定義.md  
36_runtime_operations_procedures__營運與日常運作程序.md  
37_local_execution_environment__本地執行環境規範.md  
38_compute_resource_constraints__運算資源限制.md  
39_user_interface_decision_boundary__人機決策邊界.md  
40_ui_action_permission_rules__UI操作權限規則.md  
41_twse_market_rules_reference__TWSE交易規則參考.md  
42_market_compliance_constraints__市場合規限制彙整.md  

---

## 6. Cursor「9 階段編輯視角」× 工程檔放置清單

### S1_Governance_Foundation
01–06

### S2_Canonical_Constitution
07、08、13

### S3_Canonical_Flow_Layers
09–12

### S4_Governance_Execution
14–19

### S5_System_Architecture
23–26

### S6_Strategy_and_Factors
27–31

### S7_Data_and_Quality
32–34

### S8_Execution_and_UI
20–22、39–40

### S9_Deployment_and_Environment
35–38、41–42

---

## 7. 新對話拆解規則（強制）

- 一個工程檔 = 一個新對話
- 新對話首則必貼「工程拆解開場錨定模板」
- 每個工程檔 **必含 SOURCE_TAG**

```md
<!--
SOURCE_TAG
原始文件：<Canonical 原始文件名稱>
原文範圍：<概略章節或全文>
-->
8. 雙層防失真機制（已啟用）
開場錨定模板（硬性）

工程提醒對話框（軟性）

任一缺失 → 拆解無效，不得審閱。

9. 審閱與裁決規則
審閱逐檔進行

裁決僅三種：

Pass

Reject

Scope-limited Rework

Batch 完成條件：

該 Batch 所有工程檔 Pass

10. 文件治理地位
本文件為：工程流程與結構定錨

不修改、不取代：

DOCUMENT_INDEX

MASTER_ARCH

MASTER_CANON
