# TAITS_文件索引與治理對照表（DOCUMENT_INDEX）

## 文件頭（Document Header）
- doc_key：DOCUMENT_INDEX
- 治理位階：最高母法（治理有效文件索引裁決）
- 基線日期：2026-01-11（Asia/Taipei）
- 版本日期：2026-01-16（Asia/Taipei）
- 裁決序位（自高至低）：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
- 文件定位：TAITS 治理有效文件清單（Authoritative Index）與衝突裁決程序之唯一權威索引

---

## 目錄（Table of Contents）
- 0. 文件定位
  - 0.1 全局定錨：單一口徑
  - 0.2 人類主權與人類明確命令（HFI）
- 1. 治理鐵律（Hard Laws）
  - 1.1 最高母法不可被覆寫
  - 1.2 Index 裁決（未列入即無效）
  - 1.3 上位位階覆蓋下位位階（無需協調）
  - 1.4 不得造成新舊混讀
  - 1.5 無稽核即未發生（Audit Supremacy）
- 2. doc_key 制度（唯一性、可追溯、不可偽造）
  - 2.1 doc_key 的法定位
  - 2.2 doc_key 唯一性（Hard Gate）
  - 2.3 doc_key 與檔名的關係
- 3. 治理位階（Governance Tier）與裁決力
  - 3.1 位階分桶（唯一有效）
  - 3.2 覆蓋規則（Override Rules）
- 4. 版本狀態（Version Status）與有效性
  - 4.1 狀態定義（最小集合）
  - 4.2 ACTIVE 唯一性（同 doc_key）
- 5. TAITS 治理有效文件清單（Authoritative Index｜唯一有效）
  - 5.1 最高母法（索引裁決與 AI 行為治理）
  - 5.2 母體／憲法級（主權鐵律、Canonical、治理狀態、最高否決權與執行控制）
  - 5.3 治理／制度級（系統規格、資料、策略、介面、部署、環境、版本稽核）
  - 5.4 操作／教學／工程定錨級（僅操作說明，不具治理裁決）
- 6. 衝突裁決程序（Conflict Resolution Procedure）
- 7. 引用合法性（Citation Legality）與最小格式（Hard Gate）
- 8. 模組可引用範圍矩陣（Authority Usage Matrix｜防越權）
- 9. 治理狀態（GOVERNANCE_STATE）之索引規則
- 10. 附屬文件（不具治理裁決）
- 稽核區塊（非正文）

---

## 0. 文件定位

本文件為 TAITS 的「最高裁決索引（Authoritative Index）」：

- 用於裁決治理有效文件集合（ACTIVE）、doc_key 合法性、治理位階分桶與版本狀態之唯一解讀口徑。
- 用於裁決衝突處理、覆蓋規則與跨文件引用的最小合法欄位（Hard Gate）。
- 任何快照清單（文件數量、載入集合、導覽清單）皆僅供導覽，不具裁決效力；治理裁決以本文件第 5 章為準。

### 0.1 全局定錨：單一口徑

- **Canonical Flow（L1–L11）之唯一正文來源**：doc_key=MASTER_CANON。其他文件不得重複定義或特別化任何子集合（包含不得特別化 L9–L11）。

- **L1–L11 層級之欄位契約／來源 Provenance／品質治理之落地規格承載**：由 doc_key=DATA_SOURCES（必要時搭配 TWSE_RULES 之制度引用）提供「欄位級契約與品質治理」之唯一制度化描述；其角色為工程落地規格與可稽核證據鏈前置條件之明文化，**不得視為 Canonical Flow 再定義**，亦不得與 MASTER_CANON 發生衝突；若出現衝突，一律以 MASTER_CANON 為準。
- **策略不等於下單**、**Agent 不等於策略**、**AI 不等於唯一真理**：任何企圖以流程或工具繞過上位邊界者，一律視為越權。
- **L11 非下單層**：L11 的職責是全鏈路留痕與可回放，不得被偷換為下單決策層。

### 0.2 人類主權與人類明確命令（HFI）

- TAITS 之最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件位階不得凌駕人類主權。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露、確認、全紀錄」承接；不得以程序性理由卡死承接。
  - 【Only-Add｜消歧義】本段所稱 Risk/Compliance「可否決」之對象限定為「執行放行／執行動作」（Execution Allow / Execution Action），不適用於「承接與留痕」（Accept/Intake）。因此：即使存在有效 HFI，系統不得以程序性理由卡死承接，仍必須完成強制揭露、確認與全紀錄；但 Risk/Compliance 仍可對任何可能造成成交之行為給出 VETO，並使 EXECUTION_CONTROL 之 Preflight/送單流程進入 BLOCK + AUDIT。

HFI（Human Formal Instruction｜人類明確命令）建議格式：
`HFI: <scope> | <action> | <intent> | <acknowledgement>`

若存在有效 HFI：系統必須在 scope 範圍內完成承接，並同步產生稽核承接（VERSION_AUDIT 落帳、Changelog、Hash Manifest、Audit Hand-off）。

---

## 1. 治理鐵律（Hard Laws）

### 1.1 最高母法不可被覆寫
最高母法位階之文件（含本文件）為最高裁決來源；任何下位位階文件不得改寫其裁決。

### 1.2 Index 裁決（未列入即無效）
任何「規則、流程、制度、策略、操作指南、工程文件」若不在本文件第 5 章（Authoritative Index）內：
- 不得主張治理效力
- 不得作為 Gate PASS 或 VETO、交易授權裁決、合規裁決、版本有效性判定之依據

### 1.3 上位位階覆蓋下位位階（無需協調）
治理位階分桶僅有四級（由高至低）：
1) 最高母法（索引裁決與 AI 行為治理）  
2) 母體／憲法級  
3) 治理／制度級  
4) 操作／教學／工程定錨級  

任何其他標註、別名、顯示用字樣均不構成新的治理位階。

### 1.4 不得造成新舊混讀
任何更新不得在正文內保留「被取代的舊版條文」或「歷史摘錄」造成混讀；必要留痕一律交由 VERSION_AUDIT 與 L11 承接。

### 1.5 無稽核即未發生（Audit Supremacy）
任何影響治理有效性的更新（新增、改狀態、改覆蓋、改裁決程序）必須可追溯：  
至少包含 Changelog、Hash Manifest、Scope、Audit Hand-off（並可交由 VERSION_AUDIT 落帳）。

---

## 2. doc_key 制度（唯一性、可追溯、不可偽造）

### 2.1 doc_key 的法定位
- doc_key 是治理身份（法定位）；所有裁決、引用、稽核、版本承接皆以 doc_key 為索引鍵。
- doc_key 不等同於檔名；檔名僅用於交付與導覽外觀。
- 任一治理有效文件必須可由 doc_key 唯一定位到「正文」與「稽核四件套」。

### 2.2 doc_key 唯一性（Hard Gate）
- 任一治理有效文件必須擁有且僅擁有一個 doc_key。
- 任一 doc_key 在同一時點僅能指向一個 ACTIVE 版本（見第 4 章）。

### 2.3 doc_key 與檔名的關係
- 檔名是交付與導覽外觀；doc_key 是治理身份。
- 檔名變更不得造成 doc_key 變更；若需變更 doc_key，視同新文件族群，必須更新第 5 章與 VERSION_AUDIT。

---

## 3. 治理位階（Governance Tier）與裁決力

### 3.1 位階分桶（唯一有效）
- **最高母法（索引裁決與 AI 行為治理）**：AI_GOV、DOCUMENT_INDEX
- **母體／憲法級**：MASTER_ARCH、MASTER_CANON、GOVERNANCE_STATE、RISK_COMPLIANCE、EXECUTION_CONTROL
- **治理／制度級**：FULL_ARCH、ARCH_FLOW、DATA_SOURCES、TWSE_RULES、STRATEGY_UNIVERSE、STRATEGY_FEATURE_INDEX、UI_SPEC、DEPLOY_OPS、LOCAL_ENV、VERSION_AUDIT、GOVERNANCE_GATE_SPEC
- **操作／教學／工程定錨級**：BEGINNER_GUIDE、README、UNIFIED_PROCESS_ANCHOR（不得主張治理裁決）

### 3.2 覆蓋規則（Override Rules）
- 上位位階可直接覆蓋下位位階之規定，無需協調。
- 同位階衝突：依第 6 章衝突裁決程序處置（保守處置優先）。

---

## 4. 版本狀態（Version Status）與有效性

### 4.1 狀態定義（最小集合）
- **ACTIVE**：治理有效，可被引用裁決
- **DEPRECATED**：仍可讀取或回放，但不得作為新裁決依據（除非另有明文）
- **RETIRED**：封存，只供歷史回放；不得作為任何裁決依據

### 4.2 ACTIVE 唯一性（同 doc_key）
- 同一 doc_key 同時只能存在一個 ACTIVE。
- 任何「替換 ACTIVE 指向」必須在 VERSION_AUDIT 留痕，並更新本文件第 5 章之索引表。

---

## 5. TAITS 治理有效文件清單（Authoritative Index｜唯一有效）

原則：**不在本清單內即不具治理效力。**  
本清單之「文件名稱（檔名）」為交付檔名口徑；治理身份以 **doc_key** 為準。  

- **具治理裁決效力之治理有效文件（Governance-Effective）**：合計 **21 份（ACTIVE_GOV=21）**，僅限 **5.1–5.3**。
- **操作／教學／工程定錨文件（Operational / Anchor）**：合計 **3 份（ACTIVE_OPS=3）**，列於 **5.4**；其狀態可為 ACTIVE，但**不得主張治理裁決效力**。

> 注意：任何快照清單（文件數量、載入集合、導覽清單）皆僅供導覽，不具裁決效力；治理裁決以本章為準。

### 5.1 最高母法（索引裁決與 AI 行為治理）
| 文件名稱（檔名） | doc_key | 治理位階 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260116__L1-L11_FULL_CHAIN_QA_ALIGN__OVERWRITE_v8.md | DOCUMENT_INDEX | 最高母法 | ACTIVE | 2026-01-16 | 治理有效文件清單（Authoritative Index）與衝突裁決程序之唯一權威索引 |
| TAITS_AI_行為與決策治理最終規則全集（AI_GOV）__260113__FINAL_QA__NORMALIZE.md | AI_GOV | 最高母法 | ACTIVE | 2026-01-11 | AI 行為邊界、越權禁止、裁決序位與可稽核輸出規範 |

### 5.2 母體／憲法級（主權鐵律、Canonical、治理狀態、最高否決權與執行控制）
| 文件名稱（檔名） | doc_key | 治理位階 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260114__L1-L11_QA__OVERWRITE.md | MASTER_ARCH | 母體／憲法級 | ACTIVE | 2026-01-11 | 母體總憲法、核心鐵律、權責邊界與上位裁決原則 |
| TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__260116__L6_LAYER_QA_FIX__OVERWRITE.md | MASTER_CANON | 母體／憲法級 | ACTIVE | 2026-01-16 | Canonical Flow（L1–L11）之唯一正文來源與全資訊體系定錨 |
| TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260113__FINAL_QA__NORMALIZE.md | GOVERNANCE_STATE | 母體／憲法級 | ACTIVE | 2026-01-11 | 治理狀態：封版、凍結、解凍之宣告、切換條件與承接要求 |
| TAITS_風險控管與合規最高否決權（RISK_COMPLIANCE）__260113__FINAL_QA__NORMALIZE.md | RISK_COMPLIANCE | 母體／憲法級 | ACTIVE | 2026-01-11 | 風險與合規最高否決權、停機、降級、隔離與合規裁決 |
| TAITS_交易執行與控制規範（EXECUTION_CONTROL）__260113__FINAL_QA__NORMALIZE.md | EXECUTION_CONTROL | 母體／憲法級 | ACTIVE | 2026-01-11 | 交易執行、下單前檢核、路由、成交回報、異常處理與緊急停機、復歸 |

### 5.3 治理／制度級（系統規格、資料、策略、介面、部署、環境、版本稽核）
| 文件名稱（檔名） | doc_key | 治理位階 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__260113__FINAL_QA__NORMALIZE.md | GOVERNANCE_GATE_SPEC | 治理／制度級 | ACTIVE | 2026-01-11 | 治理閘門 Gate 定義、裁決模型、通過、阻擋、退回條件與留痕要求 |
| TAITS_全系統架構總覽（FULL_ARCH）__260116__L8_LAYER_QA_FIX__OVERWRITE_v6.md | FULL_ARCH | 治理／制度級 | ACTIVE | 2026-01-16 | 全系統模組總覽與交互關係（不重複定義 L1–L11 語義） |
| TAITS_系統架構與流程細化說明（ARCH_FLOW）__260116__L4_BLOCKER_UNBLOCK__OVERWRITE_v4.md | ARCH_FLOW | 治理／制度級 | ACTIVE | 2026-01-16 | 架構與流程細化（工程與資料事件流落地細節） |
| TAITS_資料來源全集（DATA_SOURCES）__260116__L2_RECHECK_QA_ALIGN__OVERWRITE_v4.md | DATA_SOURCES | 治理／制度級 | ACTIVE | 2026-01-16 | 資料來源全集、合法性、取得方式、欄位契約與品質治理 |
| TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260113__FINAL_QA__NORMALIZE.md | TWSE_RULES | 治理／制度級 | ACTIVE | 2026-01-11 | 台灣市場制度引用層（TWSE、TPEX、TAIFEX）之規則彙編與引用原則 |
| TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__260114__L1-L11_QA__OVERWRITE.md | STRATEGY_UNIVERSE | 治理／制度級 | ACTIVE | 2026-01-11 | 策略宇宙：策略分類、輸入輸出契約、啟用與禁用條件（策略不等於下單） |
| TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__260114__L1-L11_QA__OVERWRITE.md | STRATEGY_FEATURE_INDEX | 治理／制度級 | ACTIVE | 2026-01-11 | 策略特徵與因子索引：定義、欄位、計算依賴與可追溯引用 |
| TAITS_使用者介面與人機決策規範（UI_SPEC）__260116__L6_RECHECK_UI_MAP__OVERWRITE_v2.md | UI_SPEC | 治理／制度級 | ACTIVE | 2026-01-16 | UI 與人機裁決：L9 呈現、L10 人類裁決流程、L11 回放呈現與權限邊界 |
| TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__260113__FINAL_QA__NORMALIZE.md | DEPLOY_OPS | 治理／制度級 | ACTIVE | 2026-01-11 | 部署、營運、日常運作制度；Evidence Chain 與可回放、可稽核要求 |
| TAITS_本地執行與運算環境規範（LOCAL_ENV）__260113__FINAL_QA__NORMALIZE.md | LOCAL_ENV | 治理／制度級 | ACTIVE | 2026-01-11 | 本地執行與運算環境規範：依賴、資安、隔離、資源限制與重現要求 |
| TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260116__L1-L11_FULL_CHAIN_QA_ALIGN__OVERWRITE_v8.md | VERSION_AUDIT | 治理／制度級 | ACTIVE | 2026-01-16 | 版本控管、封版、變更留痕、稽核資料結構、Hash Manifest 與交付格式 |

### 5.4 操作／教學／工程定錨級（僅操作說明，不具治理裁決）
| 文件名稱（檔名） | doc_key | 治理位階 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__260113__FINAL_QA__NORMALIZE.md | BEGINNER_GUIDE | 操作／教學／工程定錨級 | ACTIVE | 2026-01-11 | 新手教學與操作引導（僅操作說明，不具治理裁決） |
| TAITS_專案總覽與快速開始（README）__260113__FINAL_QA__NORMALIZE.md | README | 操作／教學／工程定錨級 | ACTIVE | 2026-01-11 | 專案總覽與快速開始（僅導覽與操作，不具治理裁決） |
| TAITS｜程式開發流程定錨文件（Unified Process Anchor）__260113__FINAL_QA__NORMALIZE.md | UNIFIED_PROCESS_ANCHOR | 操作／教學／工程定錨級 | ACTIVE | 2026-01-11 | 工程流程定錨（Phase 0–5 與交付規格；僅工程作業，不具治理裁決） |


## 6. 衝突裁決程序（Conflict Resolution Procedure）

當兩份（或多份）文件對同一事項產生衝突、張力、或可疑的語義偷換時，必須依序處置：

1) **確認 doc_key 合法性**：引用文件必須存在於第 5 章。  
2) **確認治理位階分桶**：依第 3 章判定文件位階。  
3) **套用覆蓋規則**：依第 3 章之覆蓋規則直接覆蓋；無需協調。  
4) **同位階衝突**：採保守處置（Fail Closed），並：
   - 退回（RETURN）要求補足引用格式（見第 7 章）或證據鏈  
   - 或要求由人類最高決策者以 L10 裁決承接  
5) **全程留痕**：衝突裁決過程必須能在 L11 回放；必要時由 VERSION_AUDIT 落帳。

---

## 7. 引用合法性（Citation Legality）與最小格式（Hard Gate）

任何跨文件引用若要作為「裁決依據」，至少必須包含以下欄位（最小集合）：

- doc_key（必填）
- 文件名稱（檔名，用於導覽）
- 版本日期（必填）
- 章節定位（必填）：章、節、條或標題
- 引用目的（必填）：用於何種裁決（Gate、Risk、Execution、UI、Ops、Audit）
- 引用範圍（必填）：適用的模組、角色、流程層或 Phase
- 引用限制（必填）：是否僅供操作說明、是否禁止作為裁決法源

缺少上述任一必填欄位者，視同非法引用：不得作為 PASS 或 VETO、交易授權、合規裁決、版本有效性判定之依據。

---

## 8. 模組可引用範圍矩陣（Authority Usage Matrix｜防越權）

> 本節為「引用邊界的摘要性矩陣」，目的在於降低越權與新舊混讀風險；不創造新的覆蓋規則，覆蓋裁決仍以第 3 章至第 7 章為準。

| 模組／角色 | 可引用（作為裁決依據） | 不可引用（不得作為裁決依據） | 備註 |
|---|---|---|---|
| Index／Governance Gate | 最高母法位階、母體／憲法級、治理／制度級；操作／教學／工程定錨級僅可作操作說明 | 任何未列入第 5 章之文件 | Gate 以第 7 章引用格式進行機器化檢核 |
| Risk／Compliance（L7） | 最高母法位階、母體／憲法級、治理／制度級（含 TWSE_RULES、DATA_SOURCES、VERSION_AUDIT） | 以操作／教學／工程定錨級作為否決法源 | 最高否決權以 RISK_COMPLIANCE 為準 |
| Execution Control（執行控制） | 最高母法位階、母體／憲法級（EXECUTION_CONTROL、RISK_COMPLIANCE、MASTER_ARCH、MASTER_CANON、VERSION_AUDIT） | 任何策略文件作為送單依據 | 送單行為須符合 EXECUTION_CONTROL；L11 非下單層 |
| Strategy／Research（L8／L9） | DATA_SOURCES、STRATEGY_UNIVERSE、STRATEGY_FEATURE_INDEX、TWSE_RULES（必要時） | 以 EXECUTION_CONTROL 作為「我可以下單」之授權依據 | 策略不等於下單；提案需可被 L7 與 L10 否決 |
| UI／Human Decision（L10） | UI_SPEC、RISK_COMPLIANCE、EXECUTION_CONTROL、MASTER_CANON | 以操作／教學／工程定錨級作為裁決法源 | L10 才是交易型態裁決層 |
| Deploy／Ops | DEPLOY_OPS、VERSION_AUDIT、GOVERNANCE_GATE_SPEC、LOCAL_ENV | 以 README 或教學文件作為制度改寫依據 | 變更需可回滾、可停機、可稽核 |
| Onboarding／Beginner | BEGINNER_GUIDE、README、UNIFIED_PROCESS_ANCHOR | 任何治理裁決 | 僅能教怎麼做，不得定義「做了就算通過」 |

---

## 9. 治理狀態（GOVERNANCE_STATE）之索引規則

- 本索引（第 5 章）僅列出治理有效文件之「當前有效版本」；治理狀態之宣告與切換規則以 GOVERNANCE_STATE 為準。
- 若 GOVERNANCE_STATE 宣告封版或凍結：
  - 第 5 章之 ACTIVE 指向不得變更，除非 GOVERNANCE_STATE 明文允許並完成可稽核承接（VERSION_AUDIT 落帳）。
  - 任何試圖以「操作文件」「工程定錨」繞過封版者，視為越權。
- 若 GOVERNANCE_STATE 宣告解凍：
  - 仍須依版本控管制度（VERSION_AUDIT）進行留痕、可回滾與可稽核交付。

---

## 10. 附屬文件（不具治理裁決）

本節所列文件不在第 5 章（Authoritative Index）內，不得主張治理效力；不得作為 Gate PASS 或 VETO、合規裁決、交易授權、版本有效性判定之依據。  
其用途僅限於「專案啟動、對話模式、使用說明、工程協作脈絡」。

| 文件名稱（檔名） | doc_key | 定位／狀態 | 版本日期 | 說明 |
|---|---|---|---|---|
| TAITS_PROJECT_PROMPT__260113__FINAL_QA__NORMALIZE.md | TAITS_PROJECT_PROMPT | 非治理文件（不在第 5 章） | 2026-01-11 | 新對話啟動與專案使用脈絡（不得作為任何治理裁決或 Gate 依據） |

---
## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 2026-01-16：L1-L11_FULL_CHAIN_QA_ALIGN：修正第 5 章（Authoritative Index）之交付檔名口徑，使『doc_key → ACTIVE 檔名』與目前專案最新覆蓋版一致（含 doc_key=DOCUMENT_INDEX 自指向、MASTER_ARCH/ARCH_FLOW/DATA_SOURCES/STRATEGY_* 等檔名口徑對齊）；不改寫裁決序位與 doc_key=MASTER_CANON 主幹語義。
- 2026-01-16：L8_RECHECK（FULL_ARCH v5→v6：修正 Markdown 條列格式；ACTIVE 指向更新；不改寫裁決序位與 Canonical 主幹語義。）
- 2026-01-16：L8_ACTIVATION：更新第 5.3 章 ACTIVE 指向：FULL_ARCH → __260116__L8_LAYER_QA_FIX__OVERWRITE_v4（補強 L8 Proposal 介面契約與 Canonical 最小工件鍵 refs 對齊；避免工程漂移與混讀；不改寫 doc_key=MASTER_CANON 主幹語義）。
- 2026-01-16：L6_ACTIVATION：啟用 L6（Regime）欄位級契約補強版 MASTER_CANON（__260116__L6_LAYER_QA_FIX）；同步更新 VERSION_AUDIT 檔名口徑，確保 ACTIVE 指向唯一且避免新舊混讀。
- 2026-01-16：INDEX_ALIGNMENT（L1/L2）：更新第 5 章 ACTIVE 指向以消除新舊混讀：ARCH_FLOW → __260116__L2_LAYER_QA_FIX__OVERWRITE_v3；DATA_SOURCES → __260116__L1_LAYER_QA_FIX__OVERWRITE_v3；並維持裁決序位與 Canonical 唯一正文來源不變。
- 2026-01-14：L5_ACTIVATION：更新 ACTIVE 指向，啟用 MASTER_CANON=__260114__L5_LAYER_QA_FIX__OVERWRITE（Evidence 欄位級契約補強）；維持其餘 doc_key 不變，以消除新舊混讀。
- 2026-01-14：L4_ACTIVATION：更新 ACTIVE 指向：MASTER_CANON → __260114__L4_LAYER_QA_FIX__OVERWRITE，以使 L4（Analysis）欄位級契約與 Hard No 規範具裁決力；其餘 ACTIVE 不變。
- 2026-01-14：L3_ACTIVATION：更新 ACTIVE 指向：MASTER_CANON → __260114__L3_LAYER_QA_FIX__OVERWRITE（L3 Snapshot/State 契約補強），其餘 ACTIVE 不變。
- 2026-01-14：L2_ACTIVATION：更新第 5 章 ACTIVE 交付檔名口徑，將 MASTER_CANON/FULL_ARCH/ARCH_FLOW/DATA_SOURCES 指向 __260114__ 覆蓋版（L1/L2 Layer QA Fix），以消除新舊混讀；並維持裁決序位與 Canonical 唯一正文來源不變。
- 2026-01-13：CONSISTENCY_QA_FIX：於第 0.2 節（HFI）新增「承接≠執行；VETO 對象為執行放行/執行動作」之消歧義條文，對齊 RISK_COMPLIANCE 與 AI_GOV；Only-Add，不改寫既有語義。
- 2026-01-13：LAYER_QA_FIX（L1）：補強「Canonical Flow 唯一正文來源」與「欄位契約/Provenance/品質治理之落地規格承載（DATA_SOURCES）」之索引式說明，以降低新舊口徑混讀風險；不改寫 Canonical Flow（MASTER_CANON）之制度語義。
- FINAL_QA_FIX：統一文件索引之交付檔名口徑為 __260113__FINAL_QA__NORMALIZE（替換原 __260111__ 參照），以確保 ACTIVE 集合可追溯性與版本集合一致。
- FINAL_QA_NORMALIZE：移除正文中可能殘留之標籤式／補丁式非正文行（若存在），確保正文乾淨且避免混讀。
- FINAL_QA_NORMALIZE：移除 Legacy Snapshot（若存在），以符合『不得保留 Legacy Snapshot』之正文規則。
- FINAL_QA_NORMALIZE：依 HASH_RULE 重新計算並更新 BODY_SHA256，確保稽核指紋可重現。
- 2026-01-11：Final QA 正文化：正文去重收斂、治理位階文字化（移除字母標籤）、移除箭頭順位／排序符號、更新第 5 章交付檔名口徑與基線日期，並重算 Hash Manifest。

### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：48b6451b97df9d33ea005efdcd743d73786063103e1d7f00d4ae3a26a8ac75d2
### 3) 適用範圍（Scope）
- scope_doc_key：DOCUMENT_INDEX
- scope_change_type：L1-L11_FULL_CHAIN_QA_ALIGN＋FINAL_QA_NORMALIZE＋LAYER_QA_FIX＋CONSISTENCY_QA_FIX（索引一致性收斂；HFI 消歧義 Only-Add；不改寫制度語義）
- scope_invariants：
  - 裁決序位固定（自高至低）：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
  - Canonical Flow（L1–L11）之唯一正文來源固定：MASTER_CANON
  - 第 4 章版本狀態最小集合維持：ACTIVE、DEPRECATED、RETIRED

### 4) Audit Hand-off（裁決承接）
- governance_order_applied：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
- note：本檔為 doc_key=DOCUMENT_INDEX 之唯一可引用正文；任何 ACTIVE 指向或交付檔名口徑變更，必須同步更新第 5 章，並以 VERSION_AUDIT 留痕。
