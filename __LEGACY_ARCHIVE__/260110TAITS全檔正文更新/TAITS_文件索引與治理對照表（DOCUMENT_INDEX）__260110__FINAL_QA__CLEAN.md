# TAITS_文件索引與治理對照表（DOCUMENT_INDEX）

## 文件頭（Document Header）
- doc_key：DOCUMENT_INDEX
- 治理等級：A+（最高母法與索引裁決）
- 基線日期：2026-01-10（Asia/Taipei）
- 版本日期：2026-01-10（Asia/Taipei）
- 裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- 文件定位：TAITS 治理有效文件清單（Authoritative Index）與衝突裁決程序之唯一權威索引

---

## 目錄（Table of Contents）
- 0. 文件定位
  - 0.1 全局定錨：單一口徑
  - 0.2 人類主權與人類明確命令（HFI）
- 1. 治理鐵律
- 2. doc_key 制度
- 3. 治理等級與覆蓋規則
- 4. 版本狀態與有效性
- 5. TAITS 治理有效文件清單（Authoritative Index｜唯一有效）
- 6. 衝突裁決程序
- 7. 引用合法性與最小格式（Hard Gate）
- 8. 模組可引用範圍矩陣（防越權）
- 9. 治理狀態（GOVERNANCE_STATE）之索引規則
- 10. 附屬文件（不具治理裁決）
- 稽核區塊（非正文）

---

## 0. 文件定位

本文件為 TAITS 的「最高裁決索引（Authoritative Index）」：

- 用於裁決 **治理有效文件集合（ACTIVE）**、doc_key 合法性、治理等級（A+ / A / B / C）與版本狀態之唯一解讀口徑。
- 用於裁決衝突處理、覆蓋規則與跨文件引用的最小合法欄位（Hard Gate）。
- 任何快照清單（文件數量、載入集合、導覽清單）皆僅供導覽，不具裁決效力；治理裁決以本文件 §5 為準。

### 0.1 全局定錨：單一口徑

- **Canonical Flow（L1–L11）之唯一正文來源**：doc_key=MASTER_CANON。其他文件不得重複定義或特別化任何子集合（包含不得特別化 L9–L11）。
- **策略 ≠ 下單**、**Agent ≠ 策略**、**AI ≠ 唯一真理**：任何企圖以流程或工具繞過上位邊界者，一律視為越權。
- **L11 非下單層**：L11 的職責是全鏈路留痕與可回放，不得被偷換為下單決策層。

### 0.2 人類主權與人類明確命令（HFI）

- TAITS 之最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權。
- 風險與合規（Risk/Compliance）在**無人類明確命令**時可否決；在**有人類明確命令**時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接；不得以程序性理由卡死承接。

HFI（Human Formal Instruction｜人類明確命令）建議格式：
`HFI: <scope> | <action> | <intent> | <acknowledgement>`

若存在有效 HFI：系統必須在 scope 範圍內完成承接，並同步產生稽核承接（VERSION_AUDIT 落帳、Changelog、Hash Manifest、Audit Hand-off）。

---

## 1. 治理鐵律（Hard Laws）

### 1.1 A+ 母法不可被覆寫
A+ 文件（含本文件）為最高裁決來源；任何 A / B / C 文件不得改寫其裁決。

### 1.2 Index 裁決（未列入＝無效）
任何「規則、流程、制度、策略、操作指南、工程文件」若不在本文件 §5 的 Authoritative Index 內：
- 不得主張治理效力
- 不得作為 Gate PASS / VETO、交易授權裁決、合規裁決、版本有效性判定之依據

### 1.3 上位覆蓋下位（無需協調）
覆蓋分桶僅有四級：**A+ > A > B > C**。  
任何其他標註、別名、顯示用字樣均不構成新的治理等級。

### 1.4 不得造成新舊混讀
任何更新不得在正文內保留「被取代的舊版條文」或「歷史摘錄」造成混讀；必要留痕一律交由 VERSION_AUDIT 與 L11 承接。

### 1.5 無稽核＝未發生（Audit Supremacy）
任何影響治理有效性的更新（新增/改狀態/改覆蓋/改裁決程序）必須可追溯：  
至少包含 Changelog + Hash Manifest + Scope + Audit Hand-off（並可交由 VERSION_AUDIT 落帳）。

---

## 2. doc_key 制度（唯一性、可追溯、不可偽造）

### 2.1 doc_key 的法定位
- `doc_key` 是文件治理身份（Identity），高於檔名與路徑。
- 一切引用、稽核、回放、Gate 檢核以 doc_key 為主鍵。

### 2.2 doc_key 唯一性（Hard Gate）
- 任一治理有效文件必須擁有且僅擁有一個 doc_key。
- 任一 doc_key 在同一時點僅能指向一個 ACTIVE 版本（見 §4.2）。

### 2.3 doc_key 與檔名的關係
- 檔名是交付與導覽外觀；doc_key 是治理身份。
- 檔名變更不得造成 doc_key 變更；若需變更 doc_key，視同新文件族群，必須更新 §5 與 VERSION_AUDIT。

---

## 3. 治理等級（Governance Level）與裁決力

### 3.1 等級分桶（唯一有效）
- **A+**：最高母法與索引裁決（AI_GOV、DOCUMENT_INDEX）
- **A**：憲法級／主權級／治理狀態／最高否決權與執行控制（MASTER_ARCH、MASTER_CANON、RISK_COMPLIANCE、EXECUTION_CONTROL、GOVERNANCE_STATE）
- **B**：制度/規格/架構/資料/策略宇宙（FULL_ARCH、ARCH_FLOW、DATA_SOURCES、TWSE_RULES、STRATEGY_UNIVERSE、STRATEGY_FEATURE_INDEX、UI_SPEC、DEPLOY_OPS、LOCAL_ENV、VERSION_AUDIT、GOVERNANCE_GATE_SPEC）
- **C**：操作/教學/工程定錨（BEGINNER_GUIDE、README、UNIFIED_PROCESS_ANCHOR；不得主張治理裁決）

### 3.2 覆蓋規則（Override Rules）
- A+ 覆蓋 A / B / C
- A 覆蓋 B / C
- B 覆蓋 C
- 同桶衝突：依 §6 衝突裁決程序處置（保守處置優先）

---

## 4. 版本狀態（Version Status）與有效性

### 4.1 狀態定義（最小集合）
- **ACTIVE**：治理有效，可被引用裁決
- **DEPRECATED**：仍可讀取/回放，但不得作為新裁決依據（除非另有明文）
- **RETIRED**：封存，只供歷史回放；不得作為任何裁決依據

### 4.2 ACTIVE 唯一性（同 doc_key）
- 同一 doc_key 同時只能存在一個 ACTIVE。
- 任何「替換 ACTIVE 指向」必須在 VERSION_AUDIT 留痕，並更新本文件 §5 的索引表。

---

## 5. TAITS 治理有效文件清單（Authoritative Index｜唯一有效）

原則：**不在本清單內＝不具治理效力。**  
本清單之「文件名稱（檔名）」為**交付檔名口徑**；治理身份以 doc_key 為準。  
本清單合計 **21 份治理有效文件（ACTIVE=21）**，以本文件為唯一裁決來源。

### 5.1 A+（Supreme Charter）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260110__FINAL_QA__CLEAN.md | DOCUMENT_INDEX | A+ | ACTIVE | 2026-01-10 | 治理有效文件清單（Authoritative Index）與衝突裁決程序之唯一權威索引 |
| TAITS_AI_行為與決策治理最終規則全集（AI_GOV）__260108__NORMALIZE__CLEAN_v4.md | AI_GOV | A+ | ACTIVE | 2026-01-08 | AI 行為邊界、越權禁止、裁決序位與可稽核輸出規範 |

### 5.2 A（Constitutional / State / Supreme Veto & Control）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260108__NORMALIZE__CLEAN_v5.md | MASTER_ARCH | A | ACTIVE | 2026-01-08 | 母體總憲法、核心鐵律、權責邊界與上位裁決原則 |
| TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__260108__NORMALIZE__CLEAN_v2.md | MASTER_CANON | A | ACTIVE | 2026-01-08 | Canonical Flow（L1–L11）之唯一正文來源與全資訊體系定錨 |
| TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260108__NORMALIZE__CLEAN.md | GOVERNANCE_STATE | A | ACTIVE | 2026-01-08 | 治理狀態：封版/凍結/解凍之宣告、切換條件與承接要求 |
| TAITS_風險控管與合規最高否決權（RISK_COMPLIANCE）__260108__NORMALIZE__CLEAN.md | RISK_COMPLIANCE | A | ACTIVE | 2026-01-08 | Risk/Compliance 最高否決權、停機、降級、隔離與合規裁決 |
| TAITS_交易執行與控制規範（EXECUTION_CONTROL）__260108__NORMALIZE__CLEAN.md | EXECUTION_CONTROL | A | ACTIVE | 2026-01-08 | 交易執行、下單前檢核、路由、成交回報、異常處理與緊急停機/復歸 |

### 5.3 B（System / Governance / Spec / Data / Strategy）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__260108__NORMALIZE__CLEAN.md | GOVERNANCE_GATE_SPEC | B | ACTIVE | 2026-01-08 | 治理閘門 Gate 定義、裁決模型、通過/阻擋/退回條件與留痕要求 |
| TAITS_全系統架構總覽（FULL_ARCH）__260108__NORMALIZE__CLEAN_v6.md | FULL_ARCH | B | ACTIVE | 2026-01-08 | 全系統模組總覽與交互關係（不重複定義 L1–L11 語義） |
| TAITS_系統架構與流程細化說明（ARCH_FLOW）__260108__NORMALIZE__CLEAN_v2.md | ARCH_FLOW | B | ACTIVE | 2026-01-08 | 架構與流程細化（工程與資料/事件流落地細節） |
| TAITS_資料來源全集（DATA_SOURCES）__260108__NORMALIZE__CLEAN.md | DATA_SOURCES | B | ACTIVE | 2026-01-08 | 資料來源全集、合法性、取得方式、欄位契約與品質治理 |
| TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260108__NORMALIZE__CLEAN.md | TWSE_RULES | B | ACTIVE | 2026-01-08 | 台灣市場制度引用層（TWSE/TPEX/TAIFEX）之規則彙編與引用原則 |
| TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__260108__NORMALIZE__CLEAN.md | STRATEGY_UNIVERSE | B | ACTIVE | 2026-01-08 | 策略宇宙：策略分類、輸入輸出契約、啟用/禁用條件（策略≠下單） |
| TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__260108__NORMALIZE__CLEAN.md | STRATEGY_FEATURE_INDEX | B | ACTIVE | 2026-01-08 | 策略特徵/因子索引：定義、欄位、計算依賴與可追溯引用 |
| TAITS_使用者介面與人機決策規範（UI_SPEC）__260108__NORMALIZE__CLEAN.md | UI_SPEC | B | ACTIVE | 2026-01-08 | UI 與人機裁決：L9 呈現、L10 人類裁決流程、L11 回放呈現與權限邊界 |
| TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__260110__FINAL_QA__MAX_COVER__CLEAN.md | DEPLOY_OPS | B | ACTIVE | 2026-01-10 | 部署/營運/日常運作制度；Evidence Chain 與可回放/可稽核要求 |
| TAITS_本地執行與運算環境規範（LOCAL_ENV）__260108__NORMALIZE__CLEAN.md | LOCAL_ENV | B | ACTIVE | 2026-01-08 | 本地執行與運算環境規範：依賴、資安、隔離、資源限制與重現要求 |
| TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260108__NORMALIZE__CLEAN.md | VERSION_AUDIT | B | ACTIVE | 2026-01-08 | 版本控管、封版、變更留痕、稽核資料結構、Hash Manifest 與交付格式 |

### 5.4 C（Operational / Onboarding / Engineering Anchor）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__260108__NORMALIZE__CLEAN_v2.md | BEGINNER_GUIDE | C | ACTIVE | 2026-01-08 | 新手教學與操作引導（僅操作說明，不具治理裁決） |
| TAITS_專案總覽與快速開始（README）__260108__NORMALIZE__CLEAN.md | README | C | ACTIVE | 2026-01-08 | 專案總覽與快速開始（僅導覽/操作；不具治理裁決） |
| TAITS｜程式開發流程定錨文件（Unified Process Anchor）__260108__NORMALIZE__CLEAN.md | UNIFIED_PROCESS_ANCHOR | C | ACTIVE | 2026-01-08 | 工程流程定錨（Phase 0–5 與交付規格；僅工程作業，不具治理裁決） |

---

## 6. 衝突裁決程序（Conflict Resolution Procedure）

當兩份（或多份）文件對同一事項產生衝突、張力、或可疑的語義偷換時，必須依序處置：

1) **確認 doc_key 合法性**：引用文件必須存在於 §5。  
2) **確認治理分桶**：依 §3 判定 A+ / A / B / C。  
3) **套用覆蓋規則**：依 §3.2 直接覆蓋；無需協調。  
4) **同桶衝突**：採保守處置（Fail Closed），並：
   - 退回（RETURN）要求補足引用格式（見 §7）或證據鏈  
   - 或要求由人類最高決策者以 L10 裁決承接  
5) **全程留痕**：衝突裁決過程必須能在 L11 回放；必要時由 VERSION_AUDIT 落帳。

---

## 7. 引用合法性（Citation Legality）與最小格式（Hard Gate）

任何模組／AI／人類若聲稱「依據文件」，必須同時提供：

- `doc_key`
- `版本日期`（YYYY-MM-DD 或檔名日期碼）
- `章節定位`（如：§3.2 / 章-節-項）
- `引用目的`（用於：否決／流程／UI 呈現／部署裁決／資料來源裁決等）

缺任一項：**引用無效**。  
引用無效時，只允許輸出「缺口清單」與「如何補足」，不得輸出裁決性結論（PASS / VETO / APPROVE / ACTIVE 等）。

---

## 8. 模組可引用範圍矩陣（Authority Usage Matrix｜防越權）

> 本節為「引用邊界的摘要性矩陣」，目的在於降低越權與新舊混讀風險；不創造新的覆蓋規則，覆蓋裁決仍以 §3–§7 為準。

| 模組/角色 | 可引用（作為裁決依據） | 不可引用（不得作為裁決依據） | 備註 |
|---|---|---|---|
| Index / Governance Gate | A+ / A / B / C（C 僅作操作說明） | 任何未列入 §5 的文件 | Gate 以 §7 引用格式進行機器化檢核 |
| Risk/Compliance（L7） | A+ / A / B（含 TWSE_RULES、DATA_SOURCES、VERSION_AUDIT） | 以 C 作為否決法源 | 最高否決權以 RISK_COMPLIANCE 為準 |
| Execution Control（執行控制） | A+ / A（EXECUTION_CONTROL、RISK_COMPLIANCE、MASTER_ARCH、MASTER_CANON）與必要之 B（GOVERNANCE_GATE_SPEC、DEPLOY_OPS、VERSION_AUDIT） | 任何策略文件作為送單依據 | 送單行為須符合 EXECUTION_CONTROL；L11 非下單層 |
| Strategy / Research（L8/L9） | DATA_SOURCES、STRATEGY_UNIVERSE、STRATEGY_FEATURE_INDEX、MASTER_CANON（作為語義定錨） | 以 EXECUTION_CONTROL 作為「我可以下單」之授權依據 | 策略 ≠ 下單；提案需可被 L7/L10 否決 |
| UI / Human Decision（L10） | UI_SPEC、RISK_COMPLIANCE、EXECUTION_CONTROL、MASTER_CANON | 以 C 作為裁決法源 | L10 才是交易型態裁決層 |
| Deploy/Ops | DEPLOY_OPS、VERSION_AUDIT、GOVERNANCE_GATE_SPEC、LOCAL_ENV | 以 README/教學文件作為制度改寫依據 | 變更需可回滾、可停機、可稽核 |
| Onboarding / Beginner | BEGINNER_GUIDE、README、UNIFIED_PROCESS_ANCHOR | 任何治理裁決 | 僅能教怎麼做，不得定義「做了就算通過」 |

---

## 9. 治理狀態（GOVERNANCE_STATE）之索引規則

- 治理狀態文件以 `doc_key = GOVERNANCE_STATE` 為唯一身份鍵，屬 A 分桶。  
- 任一時點治理狀態以「唯一 ACTIVE」為準（見 §4.2）。  
- 任何狀態切換必須：
  1) 產出新的治理狀態文件版本（不得摘要縮水；且必留痕承接）  
  2) 更新本文件 §5（維持 doc_key=GOVERNANCE_STATE 之唯一 ACTIVE 指向）  
  3) 以 VERSION_AUDIT 留痕（包含變更原因、影響範圍與回滾策略）

---

## 10. 附屬文件（不具治理裁決）

本節所列文件**不在 §5（Authoritative Index）內**，不得主張治理效力；不得作為 Gate PASS/VETO、合規裁決、交易授權、版本有效性判定之依據。  
其用途僅限於「專案啟動、對話模式、使用說明、工程協作脈絡」。

| 文件名稱（檔名） | doc_key | 定位/狀態 | 版本日期 | 說明 |
|---|---|---|---|---|
| TAITS_PROJECT_PROMPT__260108__NORMALIZE__CLEAN_v2.md | TAITS_PROJECT_PROMPT | 非治理文件（不在 §5） | 2026-01-08 | 新對話啟動／專案使用脈絡（不得作為任何治理裁決或 Gate 依據） |

---

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 2026-01-10：FINAL_QA_NORMALIZE：移除正文中的標籤化段落編號（例如 S1-*）、移除正文內占位符號與省略號、修復 §5 Authoritative Index 之檔名/欄位截斷與不一致；補齊 ACTIVE 清單為 21 份並以現行檔名口徑統一；新增 §10「附屬文件（不具治理裁決）」以容納 TAITS_PROJECT_PROMPT（不納入 §5）。同步更新基線/版本日期與 Hash Manifest。
- 2026-01-08：Normalize v4：正文去重收斂、刪除正文內之歷史摘錄；並固定檔尾稽核四件套格式。

### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：8fa63a69982613fea85a8d691d300fb1f6e3158cad0ca31e6cefa51c456372ac

### 3) 適用範圍（Scope）
- scope_doc_key：DOCUMENT_INDEX
- scope_change_type：FINAL_QA_NORMALIZE（正文乾淨／去重收斂／結構重排／引用檔名口徑修復）
- scope_invariants：
  - 裁決序位固定：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
  - Canonical Flow（L1–L11）之唯一正文來源固定：MASTER_CANON
  - §4 版本狀態最小集合維持：ACTIVE / DEPRECATED / RETIRED

### 4) Audit Hand-off（裁決承接）
- governance_order_applied：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- note：本檔為 doc_key=DOCUMENT_INDEX 之唯一可引用正文；任何 ACTIVE 指向或檔名口徑變更，必須同步更新 §5，並以 VERSION_AUDIT 留痕。
