# TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260104__單一正確正文版

doc_key：DOCUMENT_INDEX  
治理等級：A+（Authoritative Index｜最高裁決索引）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live / Live-Shadow）  
版本狀態：ACTIVE（單一正確正文版｜最大完備＋累積式更新）  
版本日期：2026-01-04（Asia/Taipei）  
裁決序位（不得自創）：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
變更原則：最大完備＋累積式更新（允許融合更新／覆寫修正／重排版以形成單一正確正文；禁止摘要化縮水；未被新版本明確取代之有效內容一律保留並持續累積；已被新版本明確取代者可自正文移除但必須由稽核留痕承接）

---

## 全局定錨｜單一口徑（S1）

### 1. 人類最高決策者主權（SOVEREIGNTY）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接，不得卡死更新。

### 2. L9–L11 最終語義（跨文件一致）
- L9（投資報告層）：可追蹤、可更新、可標的化投資報告；必含數據、價格、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源），並支援事件驅動滾動更新。
- L10（人類裁決層）：由人類最高決策者裁決不動作/回測/模擬/半自動/全自動等；任何交易型態皆以 L10 明確裁決為準（唯一交易授權入口）。
- L11（工程稽核回放層）：對 L1–L11 全層輸入/處理/輸出/裁決/執行鏈路留痕，供人類與工程端可讀、可查、可回放；L11 非下單層。

---

## 0. 文件定位（Index Charter）

本文件為 TAITS 的「最高裁決索引（Authoritative Index）」：
- 用於裁決 ACTIVE 文件集合、doc_key 合法性、治理等級 bucket（A+/A/B/C）與任何子標籤之唯一解讀口徑
- 用於裁決衝突處理、覆蓋規則與跨文件引用的最小合法欄位
- 任何快照清單（文件數量、載入集合、推薦清單）皆僅為導覽用途，不具裁決效力

---

doc_key：DOCUMENT_INDEX  
治理等級：A+（Authoritative Index & Override Gate｜唯一有效索引）  
適用範圍：TAITS 全系統（TWSE / TAIFEX；Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（本文件為裁決依據；可演進但必須可追溯）  
版本日期：2026-01-04

---

## 全局定錨｜單一口徑（S1）

### 1) 人類最高決策者主權（SOVEREIGNTY）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令（HFI）之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接；不得以程序卡死更新或裁決承接。

### 2) L9–L11 最終語義（跨文件一致）
- **L9（投資報告層）**：可追蹤、可更新、可標的化投資報告；必含數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源），並支援事件驅動滾動更新。
- **L10（人類裁決與交易決策層）**：由人類最高決策者裁決「不動作/回測/模擬/半自動/全自動」等；任何交易型態皆以 L10 明確裁決為準。
- **L11（全層工程稽核回放層）**：對 L1–L11 全層輸入/處理/輸出/裁決/執行鏈路留痕，供人類與工程端可讀、可查、可回放；**L11 非下單層**。

### 3) HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：治理狀態 狀態/更新規則/Gate **不得**阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 落帳、CHANGELOG、HASH_MANIFEST）。

---

## 0. 文件定位（Why DOCUMENT_INDEX Is Power）

本文件為 TAITS 之「治理有效文件索引」與「裁決覆蓋總閘（Index Gate）」：

- **索引裁決**：任何文件、章節、條文若未被本表納入「治理有效清單」，不得被當作治理依據。
- **覆蓋裁決**：當多份文件之表述彼此衝突或產生張力時，本文件定義「覆蓋規則」與「衝突裁決程序」，並提供可機器化檢核的引用格式。
- **一致化定錨**：本文件負責鎖定跨文件一致之語義口徑（尤其 L9–L11 定錨、doc_key 合法性、治理等級分桶）。

---

## 1. 治理鐵律（Hard Laws）

### 1.1 A+ 母法不可被覆寫
A+ 文件（含本文件）為最高裁決來源；任何 A/B/C 文件不得改寫其裁決。

### 1.2 Index 裁決（未列入＝無效）
任何「規則、流程、制度、策略、操作指南、工程文件」若不在本文件 §5 的 Authoritative Index 內：
- 不得主張治理效力
- 不得作為 Gate PASS/VETO、下單、合規裁決、版本有效性判定之依據

### 1.3 上位覆蓋下位（無需協調）
覆蓋分桶僅有四級：**A+ > A > B > C**。  
任何 B+/C+、S 等字樣僅屬**顯示標籤**，不構成新的治理等級。

### 1.4 最大完備（Max-Completeness）與累積式更新（Cumulative Update）
- 本專案治理文件之目標是**最大完備（最大可用、最大細節、可長期累積）**，允許為達成單一正確正文而進行**融合更新／覆寫／重排版／修正錯誤敘述**。
- **禁止「只保留重點／摘要化」**：任何會造成有效資訊被省略、縮水或失去可操作性與可追溯性的改寫，均視為不合格更新。
- **舊內容保留原則**：凡屬有效資訊且未被新版本內容明確更新者，必須**一律保留並持續累積**（可重排、可整併重複表述，但不得使資訊消失）。
- **可省略條件（僅限已被更新之舊資訊）**：若某段舊資訊已被新版本的「單一正確正文」所**明確取代/更新**，則舊資訊可自正文移除，但必須：
  - 在 VERSION_AUDIT 留存可追溯的變更承接（包含被取代段落之定位與原因）
  - 於本文件之稽核留痕（Audit Section）列入 CHANGELOG 與 HASH_MANIFEST
- **任何省略必須可被稽核回放**：正文只保留「當前單一正確版本」；歷史內容以稽核鏈（VERSION_AUDIT / L11）承接，不得造成新舊混讀。

### 1.5 無稽核＝未發生（Audit Supremacy）
任何影響治理有效性的更新（新增/改狀態/改覆蓋/改裁決程序）必須可追溯：  
至少包含 CHANGELOG + HASH_MANIFEST + Scope + Audit Hand-off（交由 VERSION_AUDIT 落帳）。

---

## 2. doc_key 制度（唯一性、可追溯、不可偽造）

### 2.1 doc_key 的法定位
- `doc_key` 是文件治理身份（Identity），高於檔名與路徑。
- 一切引用、稽核、回放、Gate 檢核以 doc_key 為主鍵。

### 2.2 doc_key 唯一性（Hard Gate）
- 任一治理有效文件必須擁有且僅擁有一個 doc_key。
- 同一 doc_key 在同一時間只能有一個 ACTIVE 版本（除非本文件另有明文允許之多版本並存機制；默認不允許）。

### 2.3 doc_key 與檔名（Filename）的關係
- 檔名是可讀性與版本標示；doc_key 才是治理身份。
- 引用端不得以「檔名近似」推定 doc_key；必須明示 doc_key。

---

## 3. 治理等級（Governance Level）與裁決力

### 3.1 等級分桶（唯一有效）
- **A+**：最高母法與索引裁決（AI_GOV、DOCUMENT_INDEX）
- **A**：憲法級／主權級／最高否決權與執行控制（MASTER_ARCH、MASTER_CANON、RISK_COMPLIANCE、EXECUTION_CONTROL、GOVERNANCE_STATE_*）
- **B**：制度/規格/架構/資料/策略宇宙（FULL_ARCH、ARCH_FLOW、DATA_SOURCES…）
- **C**：操作/教學/README（不得主張治理裁決）

### 3.2 覆蓋規則（Override Rules）
- A+ 覆蓋 A/B/C  
- A 覆蓋 B/C  
- B 覆蓋 C  
- 同桶衝突：依 §6 衝突裁決程序處置（保守處置優先）

### 3.3 顯示標籤（Label）之法律定位
- `S`、`B+`、`C+`、`LOCK_CANDIDATE` 等字樣：僅為顯示/完備度/嚴格度標籤，不得改寫 §3.2 覆蓋規則。
- 若其他文件以箭頭字串宣稱覆蓋順位（例如「X → Y → Z」）：一律視為助記，不得取代本節。

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
註：本表之「治理等級」以 §3 分桶為準；B+/C+ 等僅作顯示標籤。

### 5.1 A+（Supreme Canon）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_AI_行為與決策治理最終規則全集__260101.md | AI_GOV | A+ | ACTIVE | 2026-01-04 | 全系統 AI 行為與決策治理母法 |
| TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260104.md | DOCUMENT_INDEX | A+ | ACTIVE | 2026-01-04 | 文件位階裁決最高層（本文件） |

### 5.2 A（Constitutional / State）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260101.md | MASTER_ARCH | A | ACTIVE | 2026-01-04 | 人類主權、鐵律、三權分立、邊界與否決鏈 |
| TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__260101.md | MASTER_CANON | A | ACTIVE | 2026-01-04 | L1–L11 Canonical Flow 最高總綱與全資訊體系 |
| TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__260101.md | RISK_COMPLIANCE | A | ACTIVE | 2026-01-04 | 最高否決權（PASS/VETO）、理由碼、合規保守處置 |
| TAITS_交易執行與控制規範（EXECUTION_CONTROL）__260101.md | EXECUTION_CONTROL | A | ACTIVE | 2026-01-04 | 執行控制、Token、Kill Switch、Human-in-the-Loop |
| TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260101__單一檔.md | GOVERNANCE_STATE_FREEZE_V1 | A | ACTIVE | 2026-01-04 | 治理狀態宣告：治理狀態 狀態（以 GOVERNANCE_STATE 為準） 生效（對變更施加門檻） |

### 5.3 B（Governance / Spec）
| 文件名稱（檔名） | doc_key | 治理等級 | 顯示標籤 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|---|
| TAITS_全系統架構總覽（FULL_ARCH）__260101.md | FULL_ARCH | B |  | ACTIVE | 2026-01-04 | 橫向模組 × 縱向層級架構地圖 |
| TAITS_系統架構與流程細化說明（ARCH_FLOW）__260101.md | ARCH_FLOW | B | B+（顯示） | ACTIVE | 2026-01-04 | 流程層細化（承接 MASTER_CANON），不得改寫 Canonical |
| TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__260101.md | GOVERNANCE_GATE_SPEC | B |  | ACTIVE | 2026-01-04 | Gate 規則：完整性、引用合法性、拒絕與退回語義 |
| TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260101.md | VERSION_AUDIT | B |  | ACTIVE | 2026-01-04 | 變更帳本、回放、稽核證據、可追溯治理 |
| TAITS_資料來源全集（DATA_SOURCES）__260101.md | DATA_SOURCES | B |  | ACTIVE | 2026-01-04 | 官方優先、來源追溯、Fallback、Provenance |
| TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260101.md | TWSE_RULES | B |  | ACTIVE | 2026-01-04 | 交易規則參考、觸發映射、制度快照 |
| TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__260101.md | STRATEGY_UNIVERSE | B |  | ACTIVE | 2026-01-04 | 策略白名單、生命週期、輸出契約；策略≠下單 |
| TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__260101.md | STRATEGY_FEATURE_INDEX | B |  | ACTIVE | 2026-01-04 | 特徵/因子定義與審計；禁止信號化偷換 |
| TAITS_使用者介面與人機決策規範（UI_SPEC）__260101.md | UI_SPEC | B |  | ACTIVE | 2026-01-04 | UI 決策可視化、否決呈現、Decision Trace |
| TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__260101.md | DEPLOY_OPS | B |  | ACTIVE | 2026-01-04 | 部署、回滾、停機、Runbook、Live 運作制度 |

### 5.4 C（Operational / Guide｜不具治理裁決力）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__260101.md | BEGINNER_GUIDE | C | ACTIVE | 2026-01-04 | 新手操作引導；不得新增治理權力 |
| README__260101.md | README | C | ACTIVE | 2026-01-04 | 專案總覽與使用方式；不得越權 |
| TAITS_PROJECT_PROMPT__260101.md | PROJECT_PROMPT | C | ACTIVE | 2026-01-04 | 專案對話啟動與行為規範（操作級） |
| TAITS_本地執行與運算環境規範（LOCAL_ENV）__260101.md | LOCAL_ENV | C | ACTIVE | 2026-01-04 | 金鑰隔離、環境檢核、敏感資料禁止入 repo |

> 註：上述清單合計 **21 份治理有效文件**（依 TAITS 專案已生效之核心治理文件集合）。任何未列入者不得主張治理效力。

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
引用無效時，只允許輸出「缺口清單」與「如何補足」，不得輸出裁決性結論（PASS/VETO/APPROVE/ACTIVE 等）。

---

## 8. 模組可引用範圍矩陣（Authority Usage Matrix｜防越權）

> 本節為「引用邊界的摘要性矩陣」，目的在於降低越權與新舊混讀風險；不創造新的覆蓋規則，覆蓋裁決仍以 §3–§7 為準。

| 模組/角色 | 可引用（作為裁決依據） | 不可引用（不得作為裁決依據） | 備註 |
|---|---|---|---|
| Index / Governance Gate | A+ / A / B / C（但 C 僅作操作說明） | 任何未列入 §5 的文件 | Gate 以 §7 引用格式機器化檢核 |
| Risk/Compliance（L7） | A+ / A / B（含 TWSE_RULES、DATA_SOURCES） | 任何 C 作為否決依據 | 最高否決權以 RISK_COMPLIANCE 為準 |
| Execution Control（執行控制） | A+ / A（EXECUTION_CONTROL、RISK_COMPLIANCE）＋必要之 B（如 DEPLOY_OPS） | 任何策略文件作為送單依據 | 送單行為須符合 EXECUTION_CONTROL；L11 非下單層 |
| Strategy / Research（L8/L9） | DATA_SOURCES / STRATEGY_UNIVERSE / STRATEGY_FEATURE_INDEX / ARCH_FLOW（僅流程語義） | 以 EXECUTION_CONTROL 作為「我可以下單」依據 | 策略 ≠ 下單；提案需可被 L7/L10 否決 |
| UI / Human Decision（L10） | UI_SPEC / RISK_COMPLIANCE / EXECUTION_CONTROL / MASTER_CANON | 任何 C 作為裁決法源 | L10 才是交易型態裁決層 |
| Deploy/Ops | DEPLOY_OPS / VERSION_AUDIT / GOVERNANCE_GATE_SPEC | 以 README/教學文件作為制度改寫依據 | 變更需可回滾、可停機、可稽核 |
| Onboarding / Beginner | BEGINNER_GUIDE / README | 任何治理裁決 | 僅能教怎麼做，不得定義「做了就算通過」 |

---

## 9. 治理狀態（GOVERNANCE_STATE）之索引規則

- 治理狀態文件以 `doc_key = GOVERNANCE_STATE_*` 命名族群管理，屬 A 分桶。  
- 任一時點治理狀態以「唯一 ACTIVE」為準。  
- 任何狀態切換（例如 治理狀態 狀態 → 治理狀態）必須：
  1) 新增一份新的 GOVERNANCE_STATE_* 文件（可覆寫修正（但禁止摘要縮水；且必留痕承接）舊狀態文件）  
  2) 納入本文件 §5  
  3) 以 VERSION_AUDIT 留痕（包含變更原因、影響範圍與回滾策略）

---

## 10. 非治理有效文件（Non-Authoritative｜允許存在但不得裁決）

下列文件可作為工程協作、開發節奏與工作定錨之參考，但 **不具治理裁決力**，不得用於：
- 宣稱文件位階、覆蓋順序、ACTIVE 指向
- Gate PASS/VETO
- Risk/Compliance 否決法源
- Execution Control 下單授權

### 10.1 常見工程支援文件（示例）
- TAITS｜程式開發流程定錨文件（Unified Process Anchor）__260101.md（建議 doc_key：PROCESS_ANCHOR；**不入 §5**）

---

## 11. 最終宣告（Final Declaration）

- **Index 不是參考，而是裁決**：文件合法性、位階、覆蓋、引用格式、衝突處置，皆以本文件為唯一入口。
- **策略 ≠ 下單**、**Agent ≠ 策略**、**AI ≠ 唯一真理**：任何企圖以流程或工具繞過 L7/L10/L11 邊界者，一律視為越權。
- **L11 非下單層**：L11 的職責是全鏈路留痕與可回放，不得被偷換為「下單決策層」。

---

# 工程附錄（Engineering Annex｜不屬正文）

> 本附錄承接 2025-12-31（S1）版本之「路由映射／補丁／解析規則」工件，用於工程工具鏈之回放與相容性。
> 本附錄 **不具治理裁決力**：不得用於宣告位階、覆蓋、ACTIVE 指向；裁決一律以正文與 `DOCUMENT_INDEX` §3–§7 為準。
> 本附錄之目的為「最大完備＋可追溯」：保留歷史有效資訊，但避免與正文混讀。


## E1. Legacy Artifact Resolution（歷史工件解析）

- 用途：將舊檔名、舊版本、舊 alias、patch 交換紀錄，解析到「當前 ACTIVE」的單一入口（供工具鏈回放）。
- 原則：**doc_key 優先**；若無 doc_key 則依 `DOCUMENT_INDEX` §10 的規則執行，並將解析過程留痕於 L11/VERSION_AUDIT。


## E2. 映射與解析表（Tables）


### E2.1
| 補充資料集 編號 | 附錄名稱 | 所屬 doc_key | 生效狀態 | 說明 |
|---|---|---|---|---|
| 補充資料集 0 | DOCUMENT_INDEX 專屬附錄治理總則 | DOCUMENT_INDEX | ACTIVE | 定義附錄法律地位與使用邊界 |
| 補充資料集 I | 附錄啟用索引表 | DOCUMENT_INDEX | ACTIVE | 裁決哪些附錄存在 |
| 補充資料集 A | DOCUMENT_INDEX × MASTER_CANON 對位附錄 | DOCUMENT_INDEX | ACTIVE | 裁決「文件裁決」與「流程母法」邊界 |
| 補充資料集 B | 文件引用合法性防呆附錄 | DOCUMENT_INDEX | ACTIVE | 防止模糊引用與越權 |
| 補充資料集 C | 治理狀態 狀態（以 GOVERNANCE_STATE 為準） 下 Index 可行為清單 | DOCUMENT_INDEX | ACTIVE | 治理狀態 狀態 期間 Index 層允許/禁止行為 |


### E2.2
| doc_key | latest_artifact_filename | change_summary | audit_anchor_fix_id |
|---|---|---|---|
| `AI_GOV` | `TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜Snapshot 不裁決／Index Gate／引用最小格式 | `VA-METADATA_FIX-20251227-0014` |
| `DOCUMENT_INDEX` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228_FINAL.md` | 最大完備＋累積式更新｜批次映射表（本次收斂） | `VA-METADATA_FIX-20251227-0018` |
| `MASTER_ARCH` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜Snapshot 不裁決／S・B+・C+ 標籤回歸 | `VA-METADATA_FIX-20251227-0015` |
| `MASTER_CANON` | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜治理口徑補強（S=Label 等） | `VA-METADATA_FIX-20251227-0005` |
| `FULL_ARCH` | `TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜DATA_UNIVERSE alias 封口／引用回歸 | `VA-METADATA_FIX-20251227-0005` |
| `ARCH_FLOW` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜口徑對齊與引用模板 | `VA-METADATA_FIX-20251227-0003` |
| `GOVERNANCE_GATE_SPEC` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜裁決字串助記化／歧義消解 | `VA-METADATA_FIX-20251227-0002` |
| `RISK_COMPLIANCE` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜S=Label 對齊／引用口徑修補 | `VA-METADATA_FIX-20251227-0008` |
| `EXECUTION_CONTROL` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜S=Label 對齊／引用口徑修補 | `VA-METADATA_FIX-20251227-0002` |
| `LOCAL_ENV` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜Evidence Chain／引用模板 | `VA-METADATA_FIX-20251227-0004` |
| `DEPLOY_OPS` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜Deploy/Ops 證據鏈最小欄位／對齊 LOCAL_ENV | `VA-METADATA_FIX-20251227-0012` |
| `UI_SPEC` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜UI Trace 最小引用欄位／Index Gate | `VA-METADATA_FIX-20251227-0011` |
| `VERSION_AUDIT` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜METADATA_FIX Ledger 批次補登 | `VA-METADATA_FIX-20251227-0001` |
| `DATA_SOURCES` | `TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_1_FINAL.md` | 最大完備＋累積式更新｜補充條目 0/0.1（DATA_UNIVERSE=alias／引用回歸） | `VA-METADATA_FIX-20251227-0005` |
| `TWSE_RULES` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜引用口徑一致化 | `VA-METADATA_FIX-20251227-0005` |
| `STRATEGY_UNIVERSE` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜DATA_UNIVERSE alias 封口／引用回歸 DATA_SOURCES | `VA-METADATA_FIX-20251227-0006` |
| `STRATEGY_FEATURE_INDEX` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜B+ Sub-Label（bucket=B）對齊／引用模板 | `VA-METADATA_FIX-20251227-0009` |
| `PROJECT_PROMPT` | `TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜Index Gate First／ACTIVE 不固化／引用最小格式 | `VA-METADATA_FIX-20251227-0007` |
| `README` | `TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜文件清單/數量快照化／Index Gate | `VA-METADATA_FIX-20251227-0010` |
| `BEGINNER_GUIDE` | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜新手入口快照化／Index Gate／引用最小格式 | `VA-METADATA_FIX-20251227-0013` |
| `GOVERNANCE_STATE` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜狀態檔快照化／Index Gate／引用最小格式 | `VA-METADATA_FIX-20251227-0016` |
| `PROCESS_ANCHOR` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md` | 最大完備＋累積式更新｜定錨入口快照化／Index Gate／工程引用最小格式 | `VA-METADATA_FIX-20251227-0017` |


### E2.3
| doc_key | latest_artifact_filename | change_summary | audit_anchor_fix_id |
|---|---|---|---|
| `DOCUMENT_INDEX` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228F_FINAL.md` | 最大完備＋累積式更新｜Latest Mapping（YAML/JSON）+ Override Patch（收斂修正版）已納入；本檔即為 latest | `VA-METADATA_FIX-20251227-0022` |
| `DEPLOY_OPS` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md` | 最大完備＋累積式更新｜Trace ID / Evidence Chain 欄位貫穿規範已納入（2025-12-28） | `VA-METADATA_FIX-20251227-0020` |
| `VERSION_AUDIT` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228C_FINAL.md` | 最大完備＋累積式更新｜Ledger 補登（0021/0022/0023）延伸批次（2025-12-28） | `VA-METADATA_FIX-20251227-0023` |


### E2.4
| 文件名稱 | doc_key | 治理等級 | 狀態 | 備註 |
|---|---|---|---|---|
| TAITS_PROJECT_PROMPT.md | PROJECT_PROMPT | B（Project Prompt & Operating Contract） | ACTIVE | 入口治理契約；裁決仍回歸 DOCUMENT_INDEX / MASTER_ARCH / MASTER_CANON；僅供新對話啟動與對齊 |


### E2.5
| doc_key | status | canonical_filename（Index/引用） | physical_filename（本專案） | sha256_12 | source_alias（來源/舊檔名） |
|---|---|---|---|---|---|
| `README` | ACTIVE | `TAITS_專案總覽與使用說明（README）__251220.md` | `README__251231.md` | `11d42db1475e` | `TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md` |
| `AI_GOV` | ACTIVE | `TAITS_AI_行為與決策治理最終規則全集__251217.md` | `TAITS_AI_行為與決策治理最終規則全集__251231.md` | `53354789820b` | `TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md` |
| `GOVERNANCE_STATE_FREEZE_V1` | ACTIVE | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `443dbd4a27a4` | `—` |
| `PROJECT_PROMPT` | ACTIVE | `TAITS_PROJECT_PROMPT.md` | `TAITS_PROJECT_PROMPT__251231.md` | `c58e3fde8f97` | `TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md` |
| `TWSE_RULES` | ACTIVE | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md` | `3dfe33220600` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md` |
| `EXECUTION_CONTROL` | ACTIVE | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md` | `b6a3ede344e7` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md` |
| `UI_SPEC` | ACTIVE | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md` | `e60eb4446ae6` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md` |
| `FULL_ARCH` | ACTIVE | `TAITS_全系統架構總覽（FULL_ARCH）__251219.md` | `TAITS_全系統架構總覽（FULL_ARCH）__251231.md` | `494d5b689e51` | `TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md` |
| `MASTER_CANON` | ACTIVE | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md` | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md` | `ecd9ce9c918b` | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md` |
| `DOCUMENT_INDEX` | ACTIVE | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `d407ea013bc5` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md` |
| `BEGINNER_GUIDE` | ACTIVE | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md` | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md` | `2ea9efdfcc4c` | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md` |
| `LOCAL_ENV` | ACTIVE | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md` | `a7f23ecb108f` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` |
| `MASTER_ARCH` | ACTIVE | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md` | `0c0495f757da` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md` |
| `GOVERNANCE_GATE_SPEC` | ACTIVE | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md` | `d3b7ab7fbaab` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md` |
| `VERSION_AUDIT` | ACTIVE | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `1f3dfb7b29e0` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL__TOPBANNER_ONLYFREEZE__20251229.md` |
| `STRATEGY_UNIVERSE` | ACTIVE | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md` | `4b7f6c871f4f` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md` |
| `STRATEGY_FEATURE_INDEX` | ACTIVE | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md` | `01d564ba369e` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md` |
| `ARCH_FLOW` | ACTIVE | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md` | `d702e88c6000` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md` |
| `DATA_SOURCES` | ACTIVE | `TAITS_資料來源全集（DATA_SOURCES）__251219.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `0a197c01b6c8` | `TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md` |
| `DEPLOY_OPS` | ACTIVE | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md` | `4cee1444c6c3` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md` |
| `RISK_COMPLIANCE` | ACTIVE | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md` | `344cd3cb642d` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md` |
| `PROCESS_ANCHOR` | SUPPORT | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251228_ALLINONE_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `ee5ae3eb19bb` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251228_ALLINONE_FINAL.md` |


### E2.6
| legacy_ref_filename | resolve_to_physical_filename | resolution_rule |
|---|---|---|
| `README.md` | `README__251231.md` | `generic_map` |
| `README｜TAITS 專案總覽與使用說明（README）__251220.md` | `README__251231.md` | `readme_route` |
| `TAITS_<中文主標題>（<DOC_KEY>）__YYMMDD.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `placeholder_template_route` |
| `TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251227_FINAL.md` | `TAITS_AI_行為與決策治理最終規則全集__251231.md` | `ai_route` |
| `TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228E_FINAL.md` | `TAITS_AI_行為與決策治理最終規則全集__251231.md` | `ai_route` |
| `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251227_FINAL.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `routing_token` |
| `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228E_FINAL.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `routing_token` |
| `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228H_FINAL.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `routing_token` |
| `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228K_FINAL.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `routing_token` |
| `TAITS_GOVERNANCE_STATE__UNFREEZE_vX.Y__<date>.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `routing_token` |
| `TAITS_GPT_CONTEXT_PACK__ADDENDUM_20251228R_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_route_to_process_anchor` |
| `TAITS_GPT_ECR_LEDGER__ADDENDUM_20251228R_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_route_to_process_anchor` |
| `TAITS_GPT_WORKLOG__ADDENDUM_20251228R_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_route_to_process_anchor` |
| `TAITS_XXX__YYMMDD.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `placeholder_template_route` |
| `TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md` | `routing_token` |
| `TAITS_完_TWSE交易規則參考彙編（TWSE_RULES）__251219.md` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md` | `routing_token` |
| `TAITS_完_交易執行與控制規範（EXECUTION_CONTROL）__251219.md` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md` | `routing_token` |
| `TAITS_完_使用者介面與人機決策規範（UI_SPEC）__251219.md` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md` | `routing_token` |
| `TAITS_完_全系統架構總覽（FULL_ARCH）__251219.md` | `TAITS_全系統架構總覽（FULL_ARCH）__251231.md` | `routing_token` |
| `TAITS_完_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md` | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md` | `routing_token` |
| `TAITS_完_文件索引與治理對照表（DOCUMENT_INDEX）__251219.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_完_本地執行與運算環境規範（LOCAL_ENV）__251219.md` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md` | `routing_token` |
| `TAITS_完_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md` | `routing_token` |
| `TAITS_完_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md` | `routing_token` |
| `TAITS_完_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `routing_token` |
| `TAITS_完_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md` | `routing_token` |
| `TAITS_完_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md` | `routing_token` |
| `TAITS_完_系統架構與流程細化說明（ARCH_FLOW）__251219.md` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md` | `routing_token` |
| `TAITS_完_資料來源全集（DATA_SOURCES）__251219.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `routing_token` |
| `TAITS_完_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md` | `routing_token` |
| `TAITS_完_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md` | `routing_token` |
| `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251227B_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228D_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228E_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228F_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228G_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228H_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228J_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228K_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228L_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228M_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228_FINAL.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `routing_token` |
| `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md` | `routing_token` |
| `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md` | `routing_token` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `routing_token` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228C_FINAL.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `routing_token` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228H_FINAL.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `routing_token` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228J_FINAL.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `routing_token` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228K_FINAL.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `routing_token` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228L_FINAL.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `routing_token` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `routing_token` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228_FINAL.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `routing_token` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__METADATA_FIX_APPENDIX_A_FINAL.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `routing_token` |
| `TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_1_FINAL.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `routing_token` |
| `TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2B_FINAL.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `routing_token` |
| `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md` | `routing_token` |
| `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL (1).md` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md` | `routing_token` |
| `TAITS｜Cursor工程落地SOP（雙錨整合：PROCESS_ANCHOR×工程轉譯錨定）__ADDENDUM_20251228_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_addendum_route` |
| `TAITS｜GPT新對話續編編輯SOP（治理狀態 狀態（以 GOVERNANCE_STATE 為準）｜Index Gate First）__ADDENDUM_20251228R_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_addendum_route` |
| `TAITS｜GPT新對話續編編輯SOP（治理狀態 狀態（以 GOVERNANCE_STATE 為準）｜Index Gate First）__ADDENDUM_20251228_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_addendum_route` |
| `TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_addendum_route` |
| `TAITS｜工程落地拆解流程錨定（L1–L11×工程支撐）__ADDENDUM_20251228_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_addendum_route` |
| `TAITS｜程式開發流程定錨文件（Unified Process Anchor）.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `generic_map` |
| `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_addendum_route` |
| `canonical_filename=README.md` | `README__251231.md` | `generic_map` |
| `canonical_filename=TAITS_AI_行為與決策治理最終規則全集__251217.md` | `TAITS_AI_行為與決策治理最終規則全集__251231.md` | `version_swap` |
| `canonical_filename=TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `last_resort_support_route` |
| `canonical_filename=TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_全系統架構總覽（FULL_ARCH）__251219.md` | `TAITS_全系統架構總覽（FULL_ARCH）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md` | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_資料來源全集（DATA_SOURCES）__251219.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md` | `version_swap` |
| `docs/governance/TAITS_XXX__YYMMDD.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `placeholder_template_route` |
| `engineering/cr/CR-YYYYMMDD-####.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `engineering_path_route` |
| `engineering/ecr/ECR-<id>.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `engineering_path_route` |
| `engineering/ecr/ECR-YYYYMMDD-####.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `engineering_path_route` |
| `engineering/worklog/ENGINEERING_STATUS.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_route_to_process_anchor` |
| `ref_doc_name = TAITS_資料來源全集（DATA_SOURCES）__251219.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `routing_token` |


### E2.7
| legacy_ref_filename | resolve_to_physical_filename | resolution_rule |
|---|---|---|
| `TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md` | `TAITS_AI_行為與決策治理最終規則全集__251231.md` | `ai_addendum_route` |
| `TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md` | `TAITS_PROJECT_PROMPT__251231.md` | `project_prompt_addendum_route` |
| `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md` | `twse_rules_addendum_route` |
| `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md` | `exec_control_addendum_route` |
| `TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md` | `ui_spec_addendum_route` |
| `TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_全系統架構總覽（FULL_ARCH）__251231.md` | `full_arch_addendum_route` |
| `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md` | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md` | `master_canon_addendum_route` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `document_index_addendum_route` |
| `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md` | `beginner_guide_addendum_route` |
| `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md` | `master_arch_addendum_route` |
| `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md` | `gate_spec_addendum_route` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL__TOPBANNER_ONLYFREEZE__20251229.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `version_audit_addendum_route` |
| `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md` | `strategy_universe_addendum_route` |
| `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md` | `strategy_feature_index_addendum_route` |
| `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md` | `arch_flow_addendum_route` |
| `TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `data_sources_addendum_route` |
| `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md` | `deploy_ops_addendum_route` |
| `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md` | `risk_compliance_addendum_route` |
| `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251228_ALLINONE_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `process_anchor_addendum_route` |
| `canonical_filename=TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md` | `TAITS_PROJECT_PROMPT__251231.md` | `project_prompt_addendum_route` |
| `engineering/cr/CR-<id>.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `engineering_path_route` |


### E2.8
| legacy_ref_filename | resolve_to_physical_filename | resolution_rule |
|---|---|---|
| `TAITS_AI_行為與決策治理最終規則全集__251217.md` | `TAITS_AI_行為與決策治理最終規則全集__251231.md` | `version_swap` |
| `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `version_swap` |
| `TAITS_PROJECT_PROMPT.md` | `TAITS_PROJECT_PROMPT__251231.md` | `generic_map` |
| `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md` | `version_swap` |
| `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md` | `version_swap` |
| `TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md` | `version_swap` |
| `TAITS_全系統架構總覽（FULL_ARCH）__251219.md` | `TAITS_全系統架構總覽（FULL_ARCH）__251231.md` | `version_swap` |
| `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md` | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md` | `version_swap` |
| `TAITS_專案總覽與使用說明（README）__251220.md` | `README__251231.md` | `readme_route` |
| `TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md` | `README__251231.md` | `readme_route` |
| `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `version_swap` |
| `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md` | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md` | `version_swap` |
| `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md` | `version_swap` |
| `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md` | `version_swap` |
| `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md` | `version_swap` |
| `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `version_swap` |
| `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md` | `version_swap` |
| `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md` | `version_swap` |
| `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md` | `version_swap` |
| `TAITS_資料來源全集（DATA_SOURCES）__251219.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `version_swap` |
| `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md` | `version_swap` |
| `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_AI_行為與決策治理最終規則全集__251217.md` | `TAITS_AI_行為與決策治理最終規則全集__251231.md` | `version_swap` |
| `canonical_filename=TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_全系統架構總覽（FULL_ARCH）__251219.md` | `TAITS_全系統架構總覽（FULL_ARCH）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md` | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_資料來源全集（DATA_SOURCES）__251219.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md` | `version_swap` |
| `canonical_filename=TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md` | `version_swap` |


## E3. 機器可讀工件（Machine-Readable Artifacts）

> 下列區塊為工具鏈可用之歷史工件（JSON/YAML），保留原始結構以利回放。
> 若其中任何欄位與正文規則或現行 ACTIVE 清單衝突：一律以正文為準，並在 VERSION_AUDIT 留痕差異。


### E3.1
```yaml
schema_version: 1
generated_date: 2025-12-28
batch_id: BATCH-20251227-融合承接-PACK-01B
latest_mapping:
  - doc_key: AI_GOV
    latest_artifact: "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜Snapshot 不裁決／Index Gate／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0014
  - doc_key: DOCUMENT_INDEX
    latest_artifact: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228_FINAL.md"
    change_summary: "最大完備＋累積式更新｜批次輸出映射表（本次收斂）"
    fix_id: VA-METADATA_FIX-20251227-0018
  - doc_key: MASTER_ARCH
    latest_artifact: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜Snapshot 不裁決／S・B+・C+ 標籤回歸"
    fix_id: VA-METADATA_FIX-20251227-0015
  - doc_key: MASTER_CANON
    latest_artifact: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜治理口徑補強（S=Label 等）"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: FULL_ARCH
    latest_artifact: "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜DATA_UNIVERSE alias 封口／引用回歸"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: ARCH_FLOW
    latest_artifact: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜口徑對齊與引用模板"
    fix_id: VA-METADATA_FIX-20251227-0003
  - doc_key: GOVERNANCE_GATE_SPEC
    latest_artifact: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜裁決字串助記化／歧義消解"
    fix_id: VA-METADATA_FIX-20251227-0002
  - doc_key: RISK_COMPLIANCE
    latest_artifact: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜S=Label 對齊／引用口徑修補"
    fix_id: VA-METADATA_FIX-20251227-0008
  - doc_key: EXECUTION_CONTROL
    latest_artifact: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜S=Label 對齊／引用口徑修補"
    fix_id: VA-METADATA_FIX-20251227-0002
  - doc_key: LOCAL_ENV
    latest_artifact: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜Evidence Chain／引用模板"
    fix_id: VA-METADATA_FIX-20251227-0004
  - doc_key: DEPLOY_OPS
    latest_artifact: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜Deploy/Ops 證據鏈最小欄位／對齊 LOCAL_ENV"
    fix_id: VA-METADATA_FIX-20251227-0012
  - doc_key: UI_SPEC
    latest_artifact: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜UI Trace 最小引用欄位／Index Gate"
    fix_id: VA-METADATA_FIX-20251227-0011
  - doc_key: VERSION_AUDIT
    latest_artifact: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228_FINAL.md"
    change_summary: "最大完備＋累積式更新｜METADATA_FIX Ledger 收斂補登（2025-12-28）"
    fix_id: VA-METADATA_FIX-20251227-0010
  - doc_key: DATA_SOURCES
    latest_artifact: "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_1_FINAL.md"
    change_summary: "最大完備＋累積式更新｜補充條目 0/0.1（DATA_UNIVERSE=alias／引用回歸）"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: TWSE_RULES
    latest_artifact: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜引用口徑一致化"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: STRATEGY_UNIVERSE
    latest_artifact: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜DATA_UNIVERSE alias 封口／引用回歸 DATA_SOURCES"
    fix_id: VA-METADATA_FIX-20251227-0006
  - doc_key: STRATEGY_FEATURE_INDEX
    latest_artifact: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜B+ Sub-Label（bucket=B）對齊／引用模板"
    fix_id: VA-METADATA_FIX-20251227-0009
  - doc_key: PROJECT_PROMPT
    latest_artifact: "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜Index Gate First／ACTIVE 不固化／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0007
  - doc_key: README
    latest_artifact: "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜文件清單/數量快照化／Index Gate"
    fix_id: VA-METADATA_FIX-20251227-0010
  - doc_key: BEGINNER_GUIDE
    latest_artifact: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜新手入口快照化／Index Gate／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0013
  - doc_key: GOVERNANCE_STATE
    latest_artifact: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜狀態檔快照化／Index Gate／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0016
  - doc_key: PROCESS_ANCHOR
    latest_artifact: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md"
    change_summary: "最大完備＋累積式更新｜定錨入口快照化／Index Gate／工程引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0017
```


### E3.2
```json
{
  "schema_version": 1,
  "generated_date": "2025-12-28",
  "batch_id": "BATCH-20251227-融合承接-PACK-01B",
  "latest_mapping": [
    {
      "doc_key": "AI_GOV",
      "latest_artifact": "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜Snapshot 不裁決／Index Gate／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0014"
    },
    {
      "doc_key": "DOCUMENT_INDEX",
      "latest_artifact": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜批次輸出映射表（本次收斂）",
      "fix_id": "VA-METADATA_FIX-20251227-0018"
    },
    {
      "doc_key": "MASTER_ARCH",
      "latest_artifact": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜Snapshot 不裁決／S・B+・C+ 標籤回歸",
      "fix_id": "VA-METADATA_FIX-20251227-0015"
    },
    {
      "doc_key": "MASTER_CANON",
      "latest_artifact": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜治理口徑補強（S=Label 等）",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "FULL_ARCH",
      "latest_artifact": "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜DATA_UNIVERSE alias 封口／引用回歸",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "ARCH_FLOW",
      "latest_artifact": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜口徑對齊與引用模板",
      "fix_id": "VA-METADATA_FIX-20251227-0003"
    },
    {
      "doc_key": "GOVERNANCE_GATE_SPEC",
      "latest_artifact": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜裁決字串助記化／歧義消解",
      "fix_id": "VA-METADATA_FIX-20251227-0002"
    },
    {
      "doc_key": "RISK_COMPLIANCE",
      "latest_artifact": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜S=Label 對齊／引用口徑修補",
      "fix_id": "VA-METADATA_FIX-20251227-0008"
    },
    {
      "doc_key": "EXECUTION_CONTROL",
      "latest_artifact": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜S=Label 對齊／引用口徑修補",
      "fix_id": "VA-METADATA_FIX-20251227-0002"
    },
    {
      "doc_key": "LOCAL_ENV",
      "latest_artifact": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜Evidence Chain／引用模板",
      "fix_id": "VA-METADATA_FIX-20251227-0004"
    },
    {
      "doc_key": "DEPLOY_OPS",
      "latest_artifact": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜Deploy/Ops 證據鏈最小欄位／對齊 LOCAL_ENV",
      "fix_id": "VA-METADATA_FIX-20251227-0012"
    },
    {
      "doc_key": "UI_SPEC",
      "latest_artifact": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜UI Trace 最小引用欄位／Index Gate",
      "fix_id": "VA-METADATA_FIX-20251227-0011"
    },
    {
      "doc_key": "VERSION_AUDIT",
      "latest_artifact": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜METADATA_FIX Ledger 收斂補登（2025-12-28）",
      "fix_id": "VA-METADATA_FIX-20251227-0010"
    },
    {
      "doc_key": "DATA_SOURCES",
      "latest_artifact": "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_1_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜補充條目 0/0.1（DATA_UNIVERSE=alias／引用回歸）",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "TWSE_RULES",
      "latest_artifact": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜引用口徑一致化",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "STRATEGY_UNIVERSE",
      "latest_artifact": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜DATA_UNIVERSE alias 封口／引用回歸 DATA_SOURCES",
      "fix_id": "VA-METADATA_FIX-20251227-0006"
    },
    {
      "doc_key": "STRATEGY_FEATURE_INDEX",
      "latest_artifact": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜B+ Sub-Label（bucket=B）對齊／引用模板",
      "fix_id": "VA-METADATA_FIX-20251227-0009"
    },
    {
      "doc_key": "PROJECT_PROMPT",
      "latest_artifact": "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜Index Gate First／ACTIVE 不固化／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0007"
    },
    {
      "doc_key": "README",
      "latest_artifact": "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜文件清單/數量快照化／Index Gate",
      "fix_id": "VA-METADATA_FIX-20251227-0010"
    },
    {
      "doc_key": "BEGINNER_GUIDE",
      "latest_artifact": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜新手入口快照化／Index Gate／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0013"
    },
    {
      "doc_key": "GOVERNANCE_STATE",
      "latest_artifact": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜狀態檔快照化／Index Gate／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0016"
    },
    {
      "doc_key": "PROCESS_ANCHOR",
      "latest_artifact": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜定錨入口快照化／Index Gate／工程引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0017"
    }
  ]
}
```


### E3.3
```yaml
schema_version: 1
patch_type: latest_mapping_override
patch_date: 2025-12-28
patch_batch_id: BATCH-20251227-融合承接-PACK-01C
override:
  - doc_key: DOCUMENT_INDEX
    latest_artifact: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228F_FINAL.md"
    change_summary: "最大完備＋累積式更新｜Latest Mapping（YAML/JSON）+ Override Patch（收斂修正版）已納入；本檔即為 latest"
    fix_id: VA-METADATA_FIX-20251227-0022
  - doc_key: DEPLOY_OPS
    latest_artifact: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md"
    change_summary: "最大完備＋累積式更新｜Trace ID / Evidence Chain 欄位貫穿規範已納入（2025-12-28）"
    fix_id: VA-METADATA_FIX-20251227-0020
  - doc_key: VERSION_AUDIT
    latest_artifact: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228C_FINAL.md"
    change_summary: "最大完備＋累積式更新｜Ledger 補登（0021/0022/0023）延伸批次（2025-12-28）"
    fix_id: VA-METADATA_FIX-20251227-0023
```


### E3.4
```json
{
  "schema_version": 1,
  "patch_type": "latest_mapping_override",
  "patch_date": "2025-12-28",
  "patch_batch_id": "BATCH-20251227-融合承接-PACK-01C",
  "override": [
    {
      "doc_key": "DOCUMENT_INDEX",
      "latest_artifact": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228F_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜Latest Mapping（YAML/JSON）+ Override Patch（收斂修正版）已納入；本檔即為 latest",
      "fix_id": "VA-METADATA_FIX-20251227-0022"
    },
    {
      "doc_key": "DEPLOY_OPS",
      "latest_artifact": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜Trace ID / Evidence Chain 欄位貫穿規範已納入（2025-12-28）",
      "fix_id": "VA-METADATA_FIX-20251227-0020"
    },
    {
      "doc_key": "VERSION_AUDIT",
      "latest_artifact": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228C_FINAL.md",
      "change_summary": "最大完備＋累積式更新｜Ledger 補登（0021/0022/0023）延伸批次（2025-12-28）",
      "fix_id": "VA-METADATA_FIX-20251227-0023"
    }
  ]
}
```


### E3.5
```yaml
override_patch:
  patch_id: "DOCUMENT_INDEX-OVERRIDE-PATCH-2025-12-28-H"
  generated_date: "2025-12-28"
  rules:
    - when_doc_key_equals: "GOVERNANCE_STATE"
      resolve_to_doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      note: "正名封口：GOVERNANCE_STATE 僅為 alias；唯一合法 doc_key 為 GOVERNANCE_STATE_FREEZE_V1"
  additions:
    - doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      latest_artifact: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228H_FINAL.md"
      change_summary: "最大完備＋累積式更新｜P0 全閉合：引用模板作廢＋新模板固定＋alias 封口（不改原文）"
      fix_id: "VA-METADATA_FIX-20251228-0031"
```


### E3.6
```json
{
  "override_patch": {
    "patch_id": "DOCUMENT_INDEX-OVERRIDE-PATCH-2025-12-28-H",
    "generated_date": "2025-12-28",
    "rules": [
      {
        "when_doc_key_equals": "GOVERNANCE_STATE",
        "resolve_to_doc_key": "GOVERNANCE_STATE_FREEZE_V1",
        "note": "正名封口：GOVERNANCE_STATE 僅為 alias；唯一合法 doc_key 為 GOVERNANCE_STATE_FREEZE_V1"
      }
    ],
    "additions": [
      {
        "doc_key": "GOVERNANCE_STATE_FREEZE_V1",
        "latest_artifact": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228H_FINAL.md",
        "change_summary": "最大完備＋累積式更新｜P0 全閉合：引用模板作廢＋新模板固定＋alias 封口（不改原文）",
        "fix_id": "VA-METADATA_FIX-20251228-0031"
      }
    ]
  }
}
```


### E3.7
```yaml
schema_version: 2
generated_date: 2025-12-28
batch_id: BATCH-20251228-P2-COMPLETENESS
completeness_patch:
  patch_id: "DOCUMENT_INDEX-COMPLETENESS-PATCH-2025-12-28-K"
  scope: "latest_mapping_v2_full"
  note: "補齊 v2 mapping 覆蓋全部 ACTIVE doc_key（以 Authoritative Index 為準），並補登入口/工程定錨文件；append-only，後序優先。"
  latest_mapping_v2_full:
    - doc_key: "AI_GOV"
      latest_artifact: "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "ARCH_FLOW"
      latest_artifact: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "BEGINNER_GUIDE"
      latest_artifact: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "DATA_SOURCES"
      latest_artifact: "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "DEPLOY_OPS"
      latest_artifact: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL (1).md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "DOCUMENT_INDEX"
      latest_artifact: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228K_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "EXECUTION_CONTROL"
      latest_artifact: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "FULL_ARCH"
      latest_artifact: "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "GOVERNANCE_GATE_SPEC"
      latest_artifact: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      latest_artifact: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228K_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "LOCAL_ENV"
      latest_artifact: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "MASTER_ARCH"
      latest_artifact: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "MASTER_CANON"
      latest_artifact: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "README"
      latest_artifact: "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "RISK_COMPLIANCE"
      latest_artifact: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "STRATEGY_FEATURE_INDEX"
      latest_artifact: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "STRATEGY_UNIVERSE"
      latest_artifact: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "TWSE_RULES"
      latest_artifact: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "UI_SPEC"
      latest_artifact: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "VERSION_AUDIT"
      latest_artifact: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228K_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "PROJECT_PROMPT"
      latest_artifact: "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "PROCESS_ANCHOR"
      latest_artifact: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
```


### E3.8
```json
{
  "schema_version": 2,
  "generated_date": "2025-12-28",
  "batch_id": "BATCH-20251228-P2-COMPLETENESS",
  "completeness_patch": {
    "patch_id": "DOCUMENT_INDEX-COMPLETENESS-PATCH-2025-12-28-K",
    "scope": "latest_mapping_v2_full",
    "note": "補齊 v2 mapping 覆蓋全部 ACTIVE doc_key（以 Authoritative Index 為準），並補登入口/工程定錨文件；append-only，後序優先。",
    "latest_mapping_v2_full": [
      {
        "doc_key": "AI_GOV",
        "latest_artifact": "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "ARCH_FLOW",
        "latest_artifact": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "BEGINNER_GUIDE",
        "latest_artifact": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "DATA_SOURCES",
        "latest_artifact": "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "DEPLOY_OPS",
        "latest_artifact": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL (1).md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "DOCUMENT_INDEX",
        "latest_artifact": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228K_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "EXECUTION_CONTROL",
        "latest_artifact": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "FULL_ARCH",
        "latest_artifact": "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "GOVERNANCE_GATE_SPEC",
        "latest_artifact": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "GOVERNANCE_STATE_FREEZE_V1",
        "latest_artifact": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228K_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "LOCAL_ENV",
        "latest_artifact": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "MASTER_ARCH",
        "latest_artifact": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "MASTER_CANON",
        "latest_artifact": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "README",
        "latest_artifact": "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "RISK_COMPLIANCE",
        "latest_artifact": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "STRATEGY_FEATURE_INDEX",
        "latest_artifact": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "STRATEGY_UNIVERSE",
        "latest_artifact": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "TWSE_RULES",
        "latest_artifact": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "UI_SPEC",
        "latest_artifact": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "VERSION_AUDIT",
        "latest_artifact": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228K_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "PROJECT_PROMPT",
        "latest_artifact": "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "PROCESS_ANCHOR",
        "latest_artifact": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      }
    ]
  }
}
```


### E3.9
```yaml
schema_version: 3
generated_date: 2025-12-28
batch_id: BATCH-20251228-P3-CANONICAL-BUNDLE
canonical_bundle:
  bundle_id: "DOCUMENT_INDEX-CANONICAL-BUNDLE-2025-12-28-L"
  authoritative_source: "DOCUMENT_INDEX"
  note: "單一可載入束（schema_version=3）：整合 legacy 解析規則＋完整 latest mapping（含 ACTIVE 與必要 SUPPORT）。工具鏈應優先採用本束，避免多補丁選擇/合併歧義。"
  legacy_resolution_rules:
    - legacy_key: "GOVERNANCE_STATE"
      resolve_to: "GOVERNANCE_STATE_FREEZE_V1"
    - legacy_key: "DATA_UNIVERSE"
      resolve_to: "DATA_SOURCES"
    - legacy_key: "AI_GOVERNANCE_FULLSPEC"
      resolve_to: "AI_GOV"
  bundle_items:
    - doc_key: "AI_GOV"
      latest_artifact: "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "ARCH_FLOW"
      latest_artifact: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "BEGINNER_GUIDE"
      latest_artifact: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "DATA_SOURCES"
      latest_artifact: "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "DEPLOY_OPS"
      latest_artifact: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL (1).md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "DOCUMENT_INDEX"
      latest_artifact: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228L_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "EXECUTION_CONTROL"
      latest_artifact: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "FULL_ARCH"
      latest_artifact: "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "GOVERNANCE_GATE_SPEC"
      latest_artifact: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      latest_artifact: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228K_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "LOCAL_ENV"
      latest_artifact: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "MASTER_ARCH"
      latest_artifact: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "MASTER_CANON"
      latest_artifact: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "PROJECT_PROMPT"
      latest_artifact: "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "README"
      latest_artifact: "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "RISK_COMPLIANCE"
      latest_artifact: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "STRATEGY_FEATURE_INDEX"
      latest_artifact: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "STRATEGY_UNIVERSE"
      latest_artifact: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "TWSE_RULES"
      latest_artifact: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "UI_SPEC"
      latest_artifact: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "VERSION_AUDIT"
      latest_artifact: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228L_FINAL.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "PROCESS_ANCHOR"
      latest_artifact: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md"
      status: "SUPPORT"
      fix_id: "VA-METADATA_FIX-20251228-0039"
```


### E3.10
```json
{
  "schema_version": 3,
  "generated_date": "2025-12-28",
  "batch_id": "BATCH-20251228-P3-CANONICAL-BUNDLE",
  "canonical_bundle": {
    "bundle_id": "DOCUMENT_INDEX-CANONICAL-BUNDLE-2025-12-28-L",
    "authoritative_source": "DOCUMENT_INDEX",
    "note": "單一可載入束（schema_version=3）：整合 legacy 解析規則＋完整 latest mapping（含 ACTIVE 與必要 SUPPORT）。工具鏈應優先採用本束，避免多補丁選擇/合併歧義。",
    "legacy_resolution_rules": [
      {
        "legacy_key": "GOVERNANCE_STATE",
        "resolve_to": "GOVERNANCE_STATE_FREEZE_V1"
      },
      {
        "legacy_key": "DATA_UNIVERSE",
        "resolve_to": "DATA_SOURCES"
      },
      {
        "legacy_key": "AI_GOVERNANCE_FULLSPEC",
        "resolve_to": "AI_GOV"
      }
    ],
    "bundle_items": [
      {
        "doc_key": "AI_GOV",
        "latest_artifact": "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "ARCH_FLOW",
        "latest_artifact": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "BEGINNER_GUIDE",
        "latest_artifact": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "DATA_SOURCES",
        "latest_artifact": "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "DEPLOY_OPS",
        "latest_artifact": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL (1).md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "DOCUMENT_INDEX",
        "latest_artifact": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228L_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "EXECUTION_CONTROL",
        "latest_artifact": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "FULL_ARCH",
        "latest_artifact": "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "GOVERNANCE_GATE_SPEC",
        "latest_artifact": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "GOVERNANCE_STATE_FREEZE_V1",
        "latest_artifact": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228K_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "LOCAL_ENV",
        "latest_artifact": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "MASTER_ARCH",
        "latest_artifact": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "MASTER_CANON",
        "latest_artifact": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "PROJECT_PROMPT",
        "latest_artifact": "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "README",
        "latest_artifact": "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "RISK_COMPLIANCE",
        "latest_artifact": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "STRATEGY_FEATURE_INDEX",
        "latest_artifact": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "STRATEGY_UNIVERSE",
        "latest_artifact": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "TWSE_RULES",
        "latest_artifact": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "UI_SPEC",
        "latest_artifact": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "VERSION_AUDIT",
        "latest_artifact": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228L_FINAL.md",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "PROCESS_ANCHOR",
        "latest_artifact": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md",
        "status": "SUPPORT",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      }
    ]
  }
}
```


### E3.11
```text
GOVERNANCE_STATE_FREEZE_V1
DOCUMENT_INDEX
AI_GOV
VERSION_AUDIT
DATA_SOURCES
ARCH_FLOW
BEGINNER_GUIDE
DEPLOY_OPS
EXECUTION_CONTROL
FULL_ARCH
GOVERNANCE_GATE_SPEC
LOCAL_ENV
MASTER_ARCH
MASTER_CANON
README
RISK_COMPLIANCE
STRATEGY_FEATURE_INDEX
STRATEGY_UNIVERSE
TWSE_RULES
UI_SPEC
PROJECT_PROMPT
PROCESS_ANCHOR
```


### E3.12
```text
ref_doc_key = <DOC_KEY>
ref_file = <完整檔名>
ref_version = <版本日期或檔名日期碼>
ref_section = <章節定位（§ / Heading Path）>
ref_purpose = <用途：例如 gate_check / risk_veto / ui_decision / execution_policy / audit_replay>
ref_notes = <可選：alias/Label 解讀備註>
```


### E3.13
```yaml
schema_version: 3
generated_date: 2025-12-31
batch_id: BATCH-20251231-P0-PHYSICAL-ARTIFACT-MAP
canonical_bundle:
  bundle_id: "DOCUMENT_INDEX-CANONICAL-BUNDLE-2025-12-31-P0"
  authoritative_source: "DOCUMENT_INDEX"
  note: "P0 修補束（schema_version=3）：將 repo 落盤之 __251231 實體檔案集，對齊為可載入之 latest_artifact；並提供 sha256_12 供稽核回放。"
  legacy_resolution_rules:
    - legacy_key: "GOVERNANCE_STATE"
      resolve_to: "GOVERNANCE_STATE_FREEZE_V1"
    - legacy_key: "DATA_UNIVERSE"
      resolve_to: "DATA_SOURCES"
    - legacy_key: "AI_GOVERNANCE_FULLSPEC"
      resolve_to: "AI_GOV"
  physical_artifact_map:
    hash_alg: "sha256"
    hash_truncate: 12
    items:
      - doc_key: "README"
        status: "ACTIVE"
        canonical_filename: "TAITS_專案總覽與使用說明（README）__251220.md"
        physical_filename: "README__251231.md"
        sha256_12: "11d42db1475e"
        source_alias: "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md"
      - doc_key: "AI_GOV"
        status: "ACTIVE"
        canonical_filename: "TAITS_AI_行為與決策治理最終規則全集__251217.md"
        physical_filename: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
        sha256_12: "53354789820b"
        source_alias: "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md"
      - doc_key: "GOVERNANCE_STATE_FREEZE_V1"
        status: "ACTIVE"
        canonical_filename: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md"
        physical_filename: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
        sha256_12: "443dbd4a27a4"
      - doc_key: "PROJECT_PROMPT"
        status: "ACTIVE"
        canonical_filename: "TAITS_PROJECT_PROMPT.md"
        physical_filename: "TAITS_PROJECT_PROMPT__251231.md"
        sha256_12: "c58e3fde8f97"
        source_alias: "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md"
      - doc_key: "TWSE_RULES"
        status: "ACTIVE"
        canonical_filename: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md"
        physical_filename: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md"
        sha256_12: "3dfe33220600"
        source_alias: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md"
      - doc_key: "EXECUTION_CONTROL"
        status: "ACTIVE"
        canonical_filename: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md"
        physical_filename: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md"
        sha256_12: "b6a3ede344e7"
        source_alias: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md"
      - doc_key: "UI_SPEC"
        status: "ACTIVE"
        canonical_filename: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md"
        physical_filename: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md"
        sha256_12: "e60eb4446ae6"
        source_alias: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md"
      - doc_key: "FULL_ARCH"
        status: "ACTIVE"
        canonical_filename: "TAITS_全系統架構總覽（FULL_ARCH）__251219.md"
        physical_filename: "TAITS_全系統架構總覽（FULL_ARCH）__251231.md"
        sha256_12: "494d5b689e51"
        source_alias: "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
      - doc_key: "MASTER_CANON"
        status: "ACTIVE"
        canonical_filename: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md"
        physical_filename: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md"
        sha256_12: "ecd9ce9c918b"
        source_alias: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md"
      - doc_key: "DOCUMENT_INDEX"
        status: "ACTIVE"
        canonical_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md"
        physical_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
        sha256_12: "d407ea013bc5"
        source_alias: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md"
      - doc_key: "BEGINNER_GUIDE"
        status: "ACTIVE"
        canonical_filename: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md"
        physical_filename: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md"
        sha256_12: "2ea9efdfcc4c"
        source_alias: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md"
      - doc_key: "LOCAL_ENV"
        status: "ACTIVE"
        canonical_filename: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
        physical_filename: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md"
        sha256_12: "a7f23ecb108f"
        source_alias: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
      - doc_key: "MASTER_ARCH"
        status: "ACTIVE"
        canonical_filename: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md"
        physical_filename: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md"
        sha256_12: "0c0495f757da"
        source_alias: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md"
      - doc_key: "GOVERNANCE_GATE_SPEC"
        status: "ACTIVE"
        canonical_filename: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md"
        physical_filename: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md"
        sha256_12: "d3b7ab7fbaab"
        source_alias: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
      - doc_key: "VERSION_AUDIT"
        status: "ACTIVE"
        canonical_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md"
        physical_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
        sha256_12: "1f3dfb7b29e0"
        source_alias: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL__TOPBANNER_ONLYFREEZE__20251229.md"
      - doc_key: "STRATEGY_UNIVERSE"
        status: "ACTIVE"
        canonical_filename: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md"
        physical_filename: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md"
        sha256_12: "4b7f6c871f4f"
        source_alias: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md"
      - doc_key: "STRATEGY_FEATURE_INDEX"
        status: "ACTIVE"
        canonical_filename: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md"
        physical_filename: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md"
        sha256_12: "01d564ba369e"
        source_alias: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md"
      - doc_key: "ARCH_FLOW"
        status: "ACTIVE"
        canonical_filename: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md"
        physical_filename: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md"
        sha256_12: "d702e88c6000"
        source_alias: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md"
      - doc_key: "DATA_SOURCES"
        status: "ACTIVE"
        canonical_filename: "TAITS_資料來源全集（DATA_SOURCES）__251219.md"
        physical_filename: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
        sha256_12: "0a197c01b6c8"
        source_alias: "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md"
      - doc_key: "DEPLOY_OPS"
        status: "ACTIVE"
        canonical_filename: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md"
        physical_filename: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
        sha256_12: "4cee1444c6c3"
        source_alias: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md"
      - doc_key: "RISK_COMPLIANCE"
        status: "ACTIVE"
        canonical_filename: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md"
        physical_filename: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md"
        sha256_12: "344cd3cb642d"
        source_alias: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md"
      - doc_key: "PROCESS_ANCHOR"
        status: "SUPPORT"
        canonical_filename: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251228_ALLINONE_FINAL.md"
        physical_filename: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
        sha256_12: "ee5ae3eb19bb"
        source_alias: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251228_ALLINONE_FINAL.md"
```


### E3.14
```json
{
  "schema_version": 3,
  "generated_date": "2025-12-31",
  "batch_id": "BATCH-20251231-P0-PHYSICAL-ARTIFACT-MAP",
  "canonical_bundle": {
    "bundle_id": "DOCUMENT_INDEX-CANONICAL-BUNDLE-2025-12-31-P0",
    "authoritative_source": "DOCUMENT_INDEX",
    "note": "P0 修補束（schema_version=3）：將 repo 落盤之 __251231 實體檔案集，對齊為可載入之 latest_artifact；並提供 sha256_12 供稽核回放。",
    "legacy_resolution_rules": [
      {
        "legacy_key": "GOVERNANCE_STATE",
        "resolve_to": "GOVERNANCE_STATE_FREEZE_V1"
      },
      {
        "legacy_key": "DATA_UNIVERSE",
        "resolve_to": "DATA_SOURCES"
      },
      {
        "legacy_key": "AI_GOVERNANCE_FULLSPEC",
        "resolve_to": "AI_GOV"
      }
    ],
    "physical_artifact_map": {
      "hash_alg": "sha256",
      "hash_truncate": 12,
      "items": [
        {
          "doc_key": "README",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_專案總覽與使用說明（README）__251220.md",
          "physical_filename": "README__251231.md",
          "sha256_12": "11d42db1475e",
          "source_alias": "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "AI_GOV",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_AI_行為與決策治理最終規則全集__251217.md",
          "physical_filename": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
          "sha256_12": "53354789820b",
          "source_alias": "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md"
        },
        {
          "doc_key": "GOVERNANCE_STATE_FREEZE_V1",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md",
          "physical_filename": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
          "sha256_12": "443dbd4a27a4",
          "source_alias": ""
        },
        {
          "doc_key": "PROJECT_PROMPT",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_PROJECT_PROMPT.md",
          "physical_filename": "TAITS_PROJECT_PROMPT__251231.md",
          "sha256_12": "c58e3fde8f97",
          "source_alias": "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "TWSE_RULES",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md",
          "physical_filename": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md",
          "sha256_12": "3dfe33220600",
          "source_alias": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "EXECUTION_CONTROL",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md",
          "physical_filename": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md",
          "sha256_12": "b6a3ede344e7",
          "source_alias": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "UI_SPEC",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md",
          "physical_filename": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md",
          "sha256_12": "e60eb4446ae6",
          "source_alias": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md"
        },
        {
          "doc_key": "FULL_ARCH",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_全系統架構總覽（FULL_ARCH）__251219.md",
          "physical_filename": "TAITS_全系統架構總覽（FULL_ARCH）__251231.md",
          "sha256_12": "494d5b689e51",
          "source_alias": "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "MASTER_CANON",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md",
          "physical_filename": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md",
          "sha256_12": "ecd9ce9c918b",
          "source_alias": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md"
        },
        {
          "doc_key": "DOCUMENT_INDEX",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md",
          "physical_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
          "sha256_12": "d407ea013bc5",
          "source_alias": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md"
        },
        {
          "doc_key": "BEGINNER_GUIDE",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md",
          "physical_filename": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md",
          "sha256_12": "2ea9efdfcc4c",
          "source_alias": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "LOCAL_ENV",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md",
          "physical_filename": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md",
          "sha256_12": "a7f23ecb108f",
          "source_alias": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
        },
        {
          "doc_key": "MASTER_ARCH",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md",
          "physical_filename": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md",
          "sha256_12": "0c0495f757da",
          "source_alias": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md"
        },
        {
          "doc_key": "GOVERNANCE_GATE_SPEC",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md",
          "physical_filename": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md",
          "sha256_12": "d3b7ab7fbaab",
          "source_alias": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "VERSION_AUDIT",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md",
          "physical_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
          "sha256_12": "1f3dfb7b29e0",
          "source_alias": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL__TOPBANNER_ONLYFREEZE__20251229.md"
        },
        {
          "doc_key": "STRATEGY_UNIVERSE",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md",
          "physical_filename": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md",
          "sha256_12": "4b7f6c871f4f",
          "source_alias": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "STRATEGY_FEATURE_INDEX",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md",
          "physical_filename": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md",
          "sha256_12": "01d564ba369e",
          "source_alias": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "ARCH_FLOW",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md",
          "physical_filename": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md",
          "sha256_12": "d702e88c6000",
          "source_alias": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "DATA_SOURCES",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_資料來源全集（DATA_SOURCES）__251219.md",
          "physical_filename": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
          "sha256_12": "0a197c01b6c8",
          "source_alias": "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md"
        },
        {
          "doc_key": "DEPLOY_OPS",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md",
          "physical_filename": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
          "sha256_12": "4cee1444c6c3",
          "source_alias": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md"
        },
        {
          "doc_key": "RISK_COMPLIANCE",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md",
          "physical_filename": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md",
          "sha256_12": "344cd3cb642d",
          "source_alias": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md"
        },
        {
          "doc_key": "PROCESS_ANCHOR",
          "status": "SUPPORT",
          "canonical_filename": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251228_ALLINONE_FINAL.md",
          "physical_filename": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
          "sha256_12": "ee5ae3eb19bb",
          "source_alias": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251228_ALLINONE_FINAL.md"
        }
      ]
    }
  }
}
```


### E3.15
```yaml
schema_version: 3
batch_id: BATCH-20251231-P1-REFERENCE-ALIAS-EXPANSION
reference_alias_map:
  note: "P1：補登 legacy 引用檔名（含舊版版本戳、README.md、工程路徑、舊 融合承接 檔名、樣板檔名）之解析；不改寫既有文件內容，僅提供 resolver 之 alias mapping。"
  items:
    - legacy_ref_filename: "README.md"
      resolve_to: "README__251231.md"
      rule: "generic_map"
    - legacy_ref_filename: "README｜TAITS 專案總覽與使用說明（README）__251220.md"
      resolve_to: "README__251231.md"
      rule: "readme_route"
    - legacy_ref_filename: "TAITS_<中文主標題>（<DOC_KEY>）__YYMMDD.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "placeholder_template_route"
    - legacy_ref_filename: "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
      rule: "ai_route"
    - legacy_ref_filename: "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228E_FINAL.md"
      resolve_to: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
      rule: "ai_route"
    - legacy_ref_filename: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228E_FINAL.md"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228H_FINAL.md"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228K_FINAL.md"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_GOVERNANCE_STATE__UNFREEZE_vX.Y__<date>.md"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_GPT_CONTEXT_PACK__ADDENDUM_20251228R_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_route_to_process_anchor"
    - legacy_ref_filename: "TAITS_GPT_ECR_LEDGER__ADDENDUM_20251228R_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_route_to_process_anchor"
    - legacy_ref_filename: "TAITS_GPT_WORKLOG__ADDENDUM_20251228R_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_route_to_process_anchor"
    - legacy_ref_filename: "TAITS_XXX__YYMMDD.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "placeholder_template_route"
    - legacy_ref_filename: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_TWSE交易規則參考彙編（TWSE_RULES）__251219.md"
      resolve_to: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_交易執行與控制規範（EXECUTION_CONTROL）__251219.md"
      resolve_to: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_使用者介面與人機決策規範（UI_SPEC）__251219.md"
      resolve_to: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_全系統架構總覽（FULL_ARCH）__251219.md"
      resolve_to: "TAITS_全系統架構總覽（FULL_ARCH）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md"
      resolve_to: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_文件索引與治理對照表（DOCUMENT_INDEX）__251219.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
      resolve_to: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md"
      resolve_to: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md"
      resolve_to: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md"
      resolve_to: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md"
      resolve_to: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_系統架構與流程細化說明（ARCH_FLOW）__251219.md"
      resolve_to: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_資料來源全集（DATA_SOURCES）__251219.md"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md"
      resolve_to: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md"
      resolve_to: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251227B_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228D_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228E_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228F_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228G_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228H_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228J_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228K_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228L_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228M_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228_FINAL.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228C_FINAL.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228H_FINAL.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228J_FINAL.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228K_FINAL.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228L_FINAL.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228_FINAL.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__METADATA_FIX_APPENDIX_A_FINAL.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_1_FINAL.md"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2B_FINAL.md"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL (1).md"
      resolve_to: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS｜Cursor工程落地SOP（雙錨整合：PROCESS_ANCHOR×工程轉譯錨定）__ADDENDUM_20251228_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_addendum_route"
    - legacy_ref_filename: "TAITS｜GPT新對話續編編輯SOP（治理狀態 狀態（以 GOVERNANCE_STATE 為準）｜Index Gate First）__ADDENDUM_20251228R_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_addendum_route"
    - legacy_ref_filename: "TAITS｜GPT新對話續編編輯SOP（治理狀態 狀態（以 GOVERNANCE_STATE 為準）｜Index Gate First）__ADDENDUM_20251228_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_addendum_route"
    - legacy_ref_filename: "TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_addendum_route"
    - legacy_ref_filename: "TAITS｜工程落地拆解流程錨定（L1–L11×工程支撐）__ADDENDUM_20251228_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_addendum_route"
    - legacy_ref_filename: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "generic_map"
    - legacy_ref_filename: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_addendum_route"
    - legacy_ref_filename: "canonical_filename=README.md"
      resolve_to: "README__251231.md"
      rule: "generic_map"
    - legacy_ref_filename: "canonical_filename=TAITS_AI_行為與決策治理最終規則全集__251217.md"
      resolve_to: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "last_resort_support_route"
    - legacy_ref_filename: "canonical_filename=TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md"
      resolve_to: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md"
      resolve_to: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md"
      resolve_to: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_全系統架構總覽（FULL_ARCH）__251219.md"
      resolve_to: "TAITS_全系統架構總覽（FULL_ARCH）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md"
      resolve_to: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
      resolve_to: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md"
      resolve_to: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md"
      resolve_to: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md"
      resolve_to: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md"
      resolve_to: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md"
      resolve_to: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_資料來源全集（DATA_SOURCES）__251219.md"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md"
      resolve_to: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md"
      resolve_to: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "docs/governance/TAITS_XXX__YYMMDD.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "placeholder_template_route"
    - legacy_ref_filename: "engineering/cr/CR-YYYYMMDD-####.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "engineering_path_route"
    - legacy_ref_filename: "engineering/ecr/ECR-<id>.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "engineering_path_route"
    - legacy_ref_filename: "engineering/ecr/ECR-YYYYMMDD-####.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "engineering_path_route"
    - legacy_ref_filename: "engineering/worklog/ENGINEERING_STATUS.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_route_to_process_anchor"
    - legacy_ref_filename: "ref_doc_name = TAITS_資料來源全集（DATA_SOURCES）__251219.md"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      rule: "routing_token"
```


### E3.16
```json
{
  "schema_version": 3,
  "batch_id": "BATCH-20251231-P1-REFERENCE-ALIAS-EXPANSION",
  "reference_alias_map": {
    "note": "P1：補登 legacy 引用檔名（含舊版版本戳、README.md、工程路徑、舊 融合承接 檔名、樣板檔名）之解析；不改寫既有文件內容，僅提供 resolver 之 alias mapping。",
    "items": [
      {
        "legacy_ref_filename": "README.md",
        "resolve_to": "README__251231.md",
        "rule": "generic_map"
      },
      {
        "legacy_ref_filename": "README｜TAITS 專案總覽與使用說明（README）__251220.md",
        "resolve_to": "README__251231.md",
        "rule": "readme_route"
      },
      {
        "legacy_ref_filename": "TAITS_<中文主標題>（<DOC_KEY>）__YYMMDD.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "placeholder_template_route"
      },
      {
        "legacy_ref_filename": "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
        "rule": "ai_route"
      },
      {
        "legacy_ref_filename": "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228E_FINAL.md",
        "resolve_to": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
        "rule": "ai_route"
      },
      {
        "legacy_ref_filename": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228E_FINAL.md",
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228H_FINAL.md",
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228K_FINAL.md",
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_GOVERNANCE_STATE__UNFREEZE_vX.Y__<date>.md",
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_GPT_CONTEXT_PACK__ADDENDUM_20251228R_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_route_to_process_anchor"
      },
      {
        "legacy_ref_filename": "TAITS_GPT_ECR_LEDGER__ADDENDUM_20251228R_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_route_to_process_anchor"
      },
      {
        "legacy_ref_filename": "TAITS_GPT_WORKLOG__ADDENDUM_20251228R_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_route_to_process_anchor"
      },
      {
        "legacy_ref_filename": "TAITS_XXX__YYMMDD.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "placeholder_template_route"
      },
      {
        "legacy_ref_filename": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_TWSE交易規則參考彙編（TWSE_RULES）__251219.md",
        "resolve_to": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_交易執行與控制規範（EXECUTION_CONTROL）__251219.md",
        "resolve_to": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_使用者介面與人機決策規範（UI_SPEC）__251219.md",
        "resolve_to": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_全系統架構總覽（FULL_ARCH）__251219.md",
        "resolve_to": "TAITS_全系統架構總覽（FULL_ARCH）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md",
        "resolve_to": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_文件索引與治理對照表（DOCUMENT_INDEX）__251219.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_本地執行與運算環境規範（LOCAL_ENV）__251219.md",
        "resolve_to": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md",
        "resolve_to": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md",
        "resolve_to": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md",
        "resolve_to": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md",
        "resolve_to": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_系統架構與流程細化說明（ARCH_FLOW）__251219.md",
        "resolve_to": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_資料來源全集（DATA_SOURCES）__251219.md",
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md",
        "resolve_to": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md",
        "resolve_to": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251227B_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228D_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228E_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228F_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228G_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228H_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228J_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228K_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228L_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228M_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228_FINAL.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228C_FINAL.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228H_FINAL.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228J_FINAL.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228K_FINAL.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228L_FINAL.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228_FINAL.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__METADATA_FIX_APPENDIX_A_FINAL.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_1_FINAL.md",
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2B_FINAL.md",
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL (1).md",
        "resolve_to": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS｜Cursor工程落地SOP（雙錨整合：PROCESS_ANCHOR×工程轉譯錨定）__ADDENDUM_20251228_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS｜GPT新對話續編編輯SOP（治理狀態 狀態（以 GOVERNANCE_STATE 為準）｜Index Gate First）__ADDENDUM_20251228R_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS｜GPT新對話續編編輯SOP（治理狀態 狀態（以 GOVERNANCE_STATE 為準）｜Index Gate First）__ADDENDUM_20251228_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS｜工程操作總手冊（合併版：GPT續編×Cursor落地×雙錨）__ADDENDUM_20251228_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS｜工程落地拆解流程錨定（L1–L11×工程支撐）__ADDENDUM_20251228_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "generic_map"
      },
      {
        "legacy_ref_filename": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_addendum_route"
      },
      {
        "legacy_ref_filename": "canonical_filename=README.md",
        "resolve_to": "README__251231.md",
        "rule": "generic_map"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_AI_行為與決策治理最終規則全集__251217.md",
        "resolve_to": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "last_resort_support_route"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md",
        "resolve_to": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md",
        "resolve_to": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md",
        "resolve_to": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_全系統架構總覽（FULL_ARCH）__251219.md",
        "resolve_to": "TAITS_全系統架構總覽（FULL_ARCH）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md",
        "resolve_to": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md",
        "resolve_to": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md",
        "resolve_to": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md",
        "resolve_to": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md",
        "resolve_to": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md",
        "resolve_to": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md",
        "resolve_to": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_資料來源全集（DATA_SOURCES）__251219.md",
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md",
        "resolve_to": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md",
        "resolve_to": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "docs/governance/TAITS_XXX__YYMMDD.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "placeholder_template_route"
      },
      {
        "legacy_ref_filename": "engineering/cr/CR-YYYYMMDD-####.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "engineering_path_route"
      },
      {
        "legacy_ref_filename": "engineering/ecr/ECR-<id>.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "engineering_path_route"
      },
      {
        "legacy_ref_filename": "engineering/ecr/ECR-YYYYMMDD-####.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "engineering_path_route"
      },
      {
        "legacy_ref_filename": "engineering/worklog/ENGINEERING_STATUS.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_route_to_process_anchor"
      },
      {
        "legacy_ref_filename": "ref_doc_name = TAITS_資料來源全集（DATA_SOURCES）__251219.md",
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
        "rule": "routing_token"
      }
    ]
  }
}
```


### E3.17
```yaml
schema_version: 3
batch_id: BATCH-20251231-P1B-REFERENCE-ALIAS-EXTENSION
reference_alias_map_extension:
  note: "P1B：補登 Postcheck v4 新增之 21 筆 legacy 引用（多為 融合承接/inlineappendix/工程路徑）。"
  items:
    - legacy_ref_filename: "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md"
      resolve_to: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
      rule: "ai_addendum_route"
    - legacy_ref_filename: "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_PROJECT_PROMPT__251231.md"
      rule: "project_prompt_addendum_route"
    - legacy_ref_filename: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md"
      rule: "twse_rules_addendum_route"
    - legacy_ref_filename: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md"
      rule: "exec_control_addendum_route"
    - legacy_ref_filename: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md"
      resolve_to: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md"
      rule: "ui_spec_addendum_route"
    - legacy_ref_filename: "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_全系統架構總覽（FULL_ARCH）__251231.md"
      rule: "full_arch_addendum_route"
    - legacy_ref_filename: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md"
      resolve_to: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md"
      rule: "master_canon_addendum_route"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "document_index_addendum_route"
    - legacy_ref_filename: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md"
      rule: "beginner_guide_addendum_route"
    - legacy_ref_filename: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md"
      resolve_to: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md"
      rule: "master_arch_addendum_route"
    - legacy_ref_filename: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md"
      rule: "gate_spec_addendum_route"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL__TOPBANNER_ONLYFREEZE__20251229.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "version_audit_addendum_route"
    - legacy_ref_filename: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md"
      rule: "strategy_universe_addendum_route"
    - legacy_ref_filename: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md"
      rule: "strategy_feature_index_addendum_route"
    - legacy_ref_filename: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md"
      rule: "arch_flow_addendum_route"
    - legacy_ref_filename: "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      rule: "data_sources_addendum_route"
    - legacy_ref_filename: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md"
      resolve_to: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
      rule: "deploy_ops_addendum_route"
    - legacy_ref_filename: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md"
      rule: "risk_compliance_addendum_route"
    - legacy_ref_filename: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251228_ALLINONE_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "process_anchor_addendum_route"
    - legacy_ref_filename: "canonical_filename=TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md"
      resolve_to: "TAITS_PROJECT_PROMPT__251231.md"
      rule: "project_prompt_addendum_route"
    - legacy_ref_filename: "engineering/cr/CR-<id>.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "engineering_path_route"
```


### E3.18
```json
{
  "schema_version": 3,
  "batch_id": "BATCH-20251231-P1B-REFERENCE-ALIAS-EXTENSION",
  "reference_alias_map_extension": {
    "note": "P1B：補登 Postcheck v4 新增之 21 筆 legacy 引用（多為 融合承接/inlineappendix/工程路徑）。",
    "items": [
      {
        "legacy_ref_filename": "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md",
        "resolve_to": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
        "rule": "ai_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_PROJECT_PROMPT__251231.md",
        "rule": "project_prompt_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md",
        "rule": "twse_rules_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md",
        "rule": "exec_control_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md",
        "resolve_to": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md",
        "rule": "ui_spec_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_全系統架構總覽（FULL_ARCH）__251231.md",
        "rule": "full_arch_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md",
        "resolve_to": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md",
        "rule": "master_canon_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "document_index_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md",
        "rule": "beginner_guide_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ACTIVE_CLEAN_INLINEAPPENDIX_20251229.md",
        "resolve_to": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md",
        "rule": "master_arch_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md",
        "rule": "gate_spec_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228M_FINAL__TOPBANNER_ONLYFREEZE__20251229.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "version_audit_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md",
        "rule": "strategy_universe_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md",
        "rule": "strategy_feature_index_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md",
        "rule": "arch_flow_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md",
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
        "rule": "data_sources_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md",
        "resolve_to": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
        "rule": "deploy_ops_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md",
        "rule": "risk_compliance_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251228_ALLINONE_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "process_anchor_addendum_route"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "TAITS_PROJECT_PROMPT__251231.md",
        "rule": "project_prompt_addendum_route"
      },
      {
        "legacy_ref_filename": "engineering/cr/CR-<id>.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "engineering_path_route"
      }
    ]
  }
}
```


### E3.19
```yaml
schema_version: 3
batch_id: BATCH-20251231-P1C-CANONICAL-REF-ALIAS
canonical_ref_alias_map:
  items:
    - legacy_ref_filename: "TAITS_AI_行為與決策治理最終規則全集__251217.md"
      resolve_to: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_PROJECT_PROMPT.md"
      resolve_to: "TAITS_PROJECT_PROMPT__251231.md"
      rule: "generic_map"
    - legacy_ref_filename: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md"
      resolve_to: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md"
      resolve_to: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md"
      resolve_to: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_全系統架構總覽（FULL_ARCH）__251219.md"
      resolve_to: "TAITS_全系統架構總覽（FULL_ARCH）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md"
      resolve_to: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_專案總覽與使用說明（README）__251220.md"
      resolve_to: "README__251231.md"
      rule: "readme_route"
    - legacy_ref_filename: "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md"
      resolve_to: "README__251231.md"
      rule: "readme_route"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md"
      resolve_to: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
      resolve_to: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md"
      resolve_to: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md"
      resolve_to: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md"
      resolve_to: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md"
      resolve_to: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md"
      resolve_to: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_資料來源全集（DATA_SOURCES）__251219.md"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md"
      resolve_to: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md"
      resolve_to: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_AI_行為與決策治理最終規則全集__251217.md"
      resolve_to: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md"
      resolve_to: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md"
      resolve_to: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md"
      resolve_to: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_全系統架構總覽（FULL_ARCH）__251219.md"
      resolve_to: "TAITS_全系統架構總覽（FULL_ARCH）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md"
      resolve_to: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
      resolve_to: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md"
      resolve_to: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md"
      resolve_to: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md"
      resolve_to: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md"
      resolve_to: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md"
      resolve_to: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_資料來源全集（DATA_SOURCES）__251219.md"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md"
      resolve_to: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
      rule: "version_swap"
    - legacy_ref_filename: "canonical_filename=TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md"
      resolve_to: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md"
      rule: "version_swap"
```


### E3.20
```json
{
  "schema_version": 3,
  "batch_id": "BATCH-20251231-P1C-CANONICAL-REF-ALIAS",
  "canonical_ref_alias_map": {
    "items": [
      {
        "legacy_ref_filename": "TAITS_AI_行為與決策治理最終規則全集__251217.md",
        "resolve_to": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md",
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_PROJECT_PROMPT.md",
        "resolve_to": "TAITS_PROJECT_PROMPT__251231.md",
        "rule": "generic_map"
      },
      {
        "legacy_ref_filename": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md",
        "resolve_to": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md",
        "resolve_to": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md",
        "resolve_to": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_全系統架構總覽（FULL_ARCH）__251219.md",
        "resolve_to": "TAITS_全系統架構總覽（FULL_ARCH）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md",
        "resolve_to": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_專案總覽與使用說明（README）__251220.md",
        "resolve_to": "README__251231.md",
        "rule": "readme_route"
      },
      {
        "legacy_ref_filename": "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md",
        "resolve_to": "README__251231.md",
        "rule": "readme_route"
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md",
        "resolve_to": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md",
        "resolve_to": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md",
        "resolve_to": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md",
        "resolve_to": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md",
        "resolve_to": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md",
        "resolve_to": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md",
        "resolve_to": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_資料來源全集（DATA_SOURCES）__251219.md",
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md",
        "resolve_to": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md",
        "resolve_to": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_AI_行為與決策治理最終規則全集__251217.md",
        "resolve_to": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md",
        "resolve_to": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md",
        "resolve_to": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md",
        "resolve_to": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_全系統架構總覽（FULL_ARCH）__251219.md",
        "resolve_to": "TAITS_全系統架構總覽（FULL_ARCH）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md",
        "resolve_to": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md",
        "resolve_to": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md",
        "resolve_to": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md",
        "resolve_to": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md",
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md",
        "resolve_to": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md",
        "resolve_to": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md",
        "resolve_to": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_資料來源全集（DATA_SOURCES）__251219.md",
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md",
        "resolve_to": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
        "rule": "version_swap"
      },
      {
        "legacy_ref_filename": "canonical_filename=TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md",
        "resolve_to": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md",
        "rule": "version_swap"
      }
    ]
  }
}
```

# 稽核區塊（Audit Section｜非正文）

> 本區塊為「本次融合更新」之留痕（Changelog／Hash Manifest／Scope／Audit Hand-off）。  
> 為避免新舊混讀：本區塊不參與正文裁決；正文以本檔案開頭至本區塊前之內容為準。

## A. Scope（適用範圍）
- scope_doc_key: DOCUMENT_INDEX
- scope_files_output: TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260104__單一正確正文版.md
- scope_files_source: TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260102__單一正確正文版.md
- scope_mode: FILE UPDATE MODE（融合更新／整合重排版／語義定錨一致化／Final QA）
- version_date: 2026-01-04（Asia/Taipei）
- anchors_enforced:
  - 衝突裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
  - L9/L10/L11 最終語義定錨（跨文件一致）
  - 留痕與正文分離（本次 Changelog/Hash/Scope/Audit Hand-off 不混入正文）

## B. Changelog（變更清單）
1) 版本日期與檔名統一更新為 2026-01-04（Asia/Taipei）／__260104，輸出為可直接覆蓋之單一正確正文版。  
2) 維持最大完備：未刪減任何未被本次更新明確取代之有效內容；僅進行必要的標記字串去混讀（例如融合承接/附錄/治理狀態等補片式字樣之中性化），避免新舊混讀。  
3) 若原文件尾端存在既有稽核留痕段落，已以本檔末端之單一稽核區塊取代，避免多份留痕並存。  
4) 置頂補強全局定錨（人類主權＋L9/L10/L11 口徑），用於跨文件一致化（不改寫既有裁決規則，只固定口徑）。

## C. Hash Manifest（指紋清單）
- hash_alg: sha256
- scope: BODY_ONLY（不含本稽核區塊）
- hash_value_sha256: f46caa8ff197c1aaed004da2a6afe0e0b5bbe91df1a475b6724e68ea7ca116c3

## D. Audit Hand-off（裁決承接）
- change_id: DI-FUSION-260104-0007
- authority_basis: HFI（人類最高決策者明確命令｜scope=DOCUMENT_INDEX｜融合更新形成單一正文）
- governance_order_applied: DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- downstream_notes:
  - 後續更新任何文件時，若涉及 doc_key、治理等級、ACTIVE 集合、引用最小欄位或衝突裁決程序，必須以本文件為準同步對齊。
- rationale: 以單一正文消除補片式混讀來源，同時維持 Authoritative Index 的最大完備與一致裁決能力，確保跨文件語義定錨與治理裁決可被穩定承接。
