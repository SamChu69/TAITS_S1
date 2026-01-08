# TAITS_文件索引與治理對照表（DOCUMENT_INDEX）

## 文件頭（Document Header）
- doc_key：DOCUMENT_INDEX  
- 治理等級：A+（最高母法與索引裁決）  
- 基線日期：2026-01-08（Asia/Taipei）  
- 版本日期：2026-01-08（Asia/Taipei）  
- 治理裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
- 文件定位：TAITS 治理有效文件清單（Authoritative Index）與衝突裁決程序之唯一權威索引  

---

## 目錄（Table of Contents）

- 全局定錨｜單一口徑（S1）
- 0. 文件定位（Index Charter）
- 1. 治理鐵律（Hard Laws）
- 2. doc_key 制度（唯一性、可追溯、不可偽造）
- 3. 治理等級（Governance Level）與裁決力
- 4. 版本狀態（Version Status）與有效性
- 5. TAITS 治理有效文件清單（Authoritative Index｜唯一有效）
- 6. 衝突裁決程序（Conflict Resolution Procedure）
- 7. 引用合法性（Citation Legality）與最小格式（Hard Gate）
- 8. 模組可引用範圍矩陣（Authority Usage Matrix｜防越權）
- 9. 治理狀態（GOVERNANCE_STATE）之索引規則
- 10. 非治理有效文件（Non-Authoritative｜允許存在但不得裁決）
- 11. 最終宣告（Final Declaration）
- E3. 機器可讀工件（Machine-Readable Artifacts）
- A. Scope（適用範圍）
- B. Changelog（變更清單）
- C. Hash Manifest（指紋清單）
- D. Audit Hand-off（裁決承接）
- D.2 工程附錄（Engineering Annex｜非正文）


## 全局定錨｜單一口徑（S1）

- 本文件為 **TAITS 文件治理之最高裁決索引**；任何衝突一律以本檔之「Authoritative Index」與「衝突裁決程序」為最終依據。  
- **去混讀（De-Interleaving）**：正文不得殘留補丁式語句（例如：臨時附註、凍結補丁敘述、對話式指令殘留）以致混入裁決語義；留痕一律置於檔尾稽核區（§A–§D）或由 VERSION_AUDIT 承接。  
- **Canonical Flow 主幹來源（唯一正文）**：L1–L11 定義以 doc_key=MASTER_CANON 為唯一正文來源；本檔僅宣告承接規則，禁止其他文件重複定義造成語義漂移；如需補強語義，應在 MASTER_CANON 進行並由 VERSION_AUDIT 落帳承接。  
- **L9/L10/L11 標籤口徑（承接 MASTER_CANON）**：L9＝投資報告層；L10＝人類裁決與交易授權層；L11＝全層工程稽核回放層（非下單層）。  

### S1-1｜人類最高決策者主權（SOVEREIGNTY）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令（HFI）之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接；不得以程序卡死更新或裁決承接。

### S1-2｜HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：治理狀態/更新規則/Gate 不得阻擋 scope 範圍內之更新／覆寫／重排版；並必須同步產生稽核承接（VERSION_AUDIT 落帳、Changelog、Hash Manifest、Audit Hand-off）。


## 0. 文件定位（Index Charter）

本文件為 TAITS 的「最高裁決索引（Authoritative Index）」：
- 用於裁決 **ACTIVE 治理有效文件集合**、doc_key 合法性、治理等級（A+/A/B/C）與版本狀態之唯一解讀口徑。
- 用於裁決衝突處理、覆蓋規則與跨文件引用的最小合法欄位。
- 任何快照清單（文件數量、載入集合、導覽清單）皆僅為導覽用途，不具裁決效力。


## 1. 治理鐵律（Hard Laws）

### 1.1 A+ 母法不可被覆寫
A+ 文件（含本文件）為最高裁決來源；任何 A/B/C 文件不得改寫其裁決。

### 1.2 Index 裁決（未列入＝無效）
任何「規則、流程、制度、策略、操作指南、工程文件」若不在本文件 §5 的 Authoritative Index 內：
- 不得主張治理效力
- 不得作為 Gate PASS/VETO、下單、合規裁決、版本有效性判定之依據

### 1.3 上位覆蓋下位（無需協調）
覆蓋分桶僅有四級：**A+ > A > B > C**。  
任何其他標註/別名/顯示用字樣均不構成新的治理等級。

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
註：本清單合計 **21 份治理有效文件**（以本文件為準）；任何未列入者不得主張治理效力。


### 5.1 A+（Supreme Charter）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_AI_行為與決策治理最終規則全集__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | AI_GOV | A+ | ACTIVE（單一正確正文版｜最大完備＋累積式更新） | 2026-01-06 | TAITS 全系統（AI 行為邊界／越權禁止／裁決序位／輸出規範／稽核留痕要求） |
| TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260108__NORMALIZE__CLEAN_v3.md | DOCUMENT_INDEX | A+ | ACTIVE | 2026-01-08 | TAITS 全系統（TWSE / TAIFEX；Research / Backtest / Simulation / Paper / Live） |


### 5.2 A（Constitutional / State）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | MASTER_ARCH | A | ACTIVE · LOCKABLE（單一正確正文版｜最大完備＋累積式更新） | 2026-01-06 | TAITS 全系統（最高架構公理／不可違反鐵律／裁決序位／系統邊界與權責） |
| TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__260108__NORMALIZE__CLEAN_v2.md | MASTER_CANON | A | ACTIVE（單一正確正文版｜最大完備＋累積式更新） | 2026-01-08 | TAITS 全系統（Canonical Flow L1–L11 全層語義定錨／資料與事件流全景／Agent 與治理邊界／L9-L11 關鍵口徑） |
| TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | GOVERNANCE_STATE | A | ACTIVE（治理狀態 v1.0 生效） | 2026-01-06 | TAITS 全系統（宣告 治理狀態 v1.0 之預設保守門檻；並定義 HFI Override 與狀態切換要求） |


### 5.3 B（Governance / Spec）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_全系統架構總覽（FULL_ARCH）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106__CLEAN_260107.md | FULL_ARCH | B | ACTIVE（單一正確正文版｜最大完備＋累積式更新） | 2026-01-06 | TAITS 全系統（Research / Backtest / Simulation / Paper / Live / Live-Shadow） |
| TAITS_系統架構與流程細化說明（ARCH_FLOW）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | ARCH_FLOW | B | ACTIVE（單一正確正文版｜最大完備＋累積式更新） | 2026-01-06 | TAITS 全系統（Research / Backtest / Simulation / Paper / Live） |
| TAITS_風險控管與合規最高否決權（RISK_COMPLIANCE）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | RISK_COMPLIANCE | B | ACTIVE（單一正確正文版｜最終覆蓋版｜去混讀＋留痕分離） | 2026-01-06 | TAITS 全系統（任何層級輸出、任何策略、任何執行）之最高否決/停機/降級/隔離與合規裁決 |
| TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | GOVERNANCE_GATE_SPEC | B | ACTIVE（單一正確正文版｜最大完備＋累積式更新｜可直接覆蓋） | 2026-01-06 | TAITS 全系統（治理閘門 Gate 定義／裁決模型／通過/阻擋/退回條件／衝突裁決／升級路徑／裁決留痕／UI 呈現義務／引用合法性） |
| TAITS_交易執行與控制規範（EXECUTION_CONTROL）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | EXECUTION_CONTROL | B | ACTIVE（單一正確正文版｜覆蓋版｜去混讀＋留痕分離） | 2026-01-06 | TAITS 執行鏈（下單前檢核／委託與路由／成交回報／風險控制／異常處理／緊急停機與復歸；交易授權唯一入口為 L10） |
| TAITS_使用者介面與人機決策規範（UI_SPEC）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | UI_SPEC | B | ACTIVE（單一正確正文版｜覆蓋版｜去混讀＋留痕分離） | 2026-01-06 | TAITS 前端/報告呈現（L9）、人類裁決流程（L10）、稽核回放呈現（L11），以及人機權限邊界 |
| TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106__CLEAN_260107.md | DEPLOY_OPS | B | ACTIVE（單一正確正文版｜最大完備＋累積式更新） | 2026-01-06 | TAITS 全系統（Research / Backtest / Simulation / Paper / Live） |
| TAITS_本地執行與運算環境規範（LOCAL_ENV）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | LOCAL_ENV | B | ACTIVE（單一正確正文版｜覆蓋版｜去混讀＋留痕分離） | 2026-01-06 | TAITS 本地開發/測試/回放（依 LOCAL_ENV 規範之 OS、依賴、資安、金鑰、隔離、資源限制） |
| TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | VERSION_AUDIT | B | ACTIVE（單一正確正文版｜最終覆蓋版｜去混讀＋留痕分離＋章節去重） | 2026-01-06 | TAITS 全系統（版本命名/封版/變更留痕/稽核資料結構/重現與回放/Hash Manifest/交付格式） |
| TAITS_資料來源全集（DATA_SOURCES）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106__CLEAN_260107.md | DATA_SOURCES | B | ACTIVE（單一正確正文版｜最大完備＋累積式更新） | 2026-01-06 | TAITS 全系統（Research / Backtest / Simulation / Paper / Live） |
| TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106__CLEAN_260107.md | TWSE_RULES | B | ACTIVE（最大完備／累積式更新：允許融合更新、覆寫修正、重排版；禁止摘要縮水；未被新內容明確取代者必保留；被取代者可移除但須留痕承接） | 2026-01-06 | TAITS 台灣市場（TWSE / TPEX / TAIFEX 之「制度引用」層；裁決以官方為準） |
| TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106__CLEAN_260107.md | STRATEGY_UNIVERSE | B | ACTIVE（單一正確正文版｜最大完備＋累積式更新） | 2026-01-06 | TAITS 策略層（策略分類/定義/輸入輸出契約/可用條件/禁用條件；策略本身不等於下單） |
| TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106__CLEAN_260107.md | STRATEGY_FEATURE_INDEX | B | ACTIVE（單一正確正文版｜最大完備＋累積式更新） | 2026-01-06 | TAITS 策略層（特徵/因子/指標索引與標準化命名；策略可引用但不得繞過風控/合規/人類裁決） |


### 5.4 C（Operations / Guide）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106__CLEAN_260107.md | BEGINNER_GUIDE | C | ACTIVE（單一正確正文版｜最大完備＋累積式更新） | 2026-01-06 | TAITS 使用者操作、對話開啟、檔案更新流程、工程 Phase 使用方式與常見錯誤避免 |
| README__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md | README | C | ACTIVE | 2026-01-06 |  |
| TAITS_PROJECT_PROMPT__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106__CLEAN_260107.md | PROJECT_PROMPT | C | ACTIVE（單一正確正文版｜最大完備＋累積式更新（允許融合更新／覆寫修正／重排版以形成單一正確正文；禁止摘要化縮水；未被新版本明確取代之有效內容一律保留並持續累積；已被新版本明確取代者可自正文移除但必須由稽核留痕承接）） | 2026-01-06 | TAITS 全系統（TWSE / TAIFEX｜Research / Backtest / Simulation / Paper / Live）之「新對話啟動、嚴格對齊、引用格式、可稽核交付」 |

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
- TAITS｜程式開發流程定錨文件（Unified Process Anchor）__260106__單一正確正文版__最終覆蓋版__覆蓋輸出__FINALQA_260106.md（doc_key：PROCESS_ANCHOR；不入 §5）

---

## 11. 最終宣告（Final Declaration）

- **Index 不是參考，而是裁決**：文件合法性、位階、覆蓋、引用格式、衝突處置，皆以本文件為唯一入口。
- **策略 ≠ 下單**、**Agent ≠ 策略**、**AI ≠ 唯一真理**：任何企圖以流程或工具繞過 L7/L10/L11 邊界者，一律視為越權。
- **L11 非下單層**：L11 的職責是全鏈路留痕與可回放，不得被偷換為「下單決策層」。

---

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）

- 2026-01-08：Normalize v4：移除 Legacy Audit Snapshot（歷史摘錄）以符合「僅保留整理後的新正文」要求；Hash Manifest 同步重算更新。

- 2026-01-08：Normalize v3：移除 §3.3「顯示標籤」段與 §0 重複元資訊段；§1.3 收斂為「僅 A+/A/B/C 四級分桶」單一規則文字；同步更新 §5 自身索引檔名與 Hash Manifest。

- 2026-01-08：Normalize 收斂：收斂文件頭為單一《文件頭（Document Header）》；§S1 去重：移除獨立之「S1-2｜L9–L11 最終語義承接」段落，改併入 §S1 之「Canonical Flow 主幹來源（唯一正文）」承接條款；並將 §S1-3 重新編號為 §S1-2（HFI）。同步更新基線日期為 2026-01-08。
- 修正：將文件頂層標題收斂為單一 H1；原既有稽核區塊內容改以 Legacy Snapshot 承接於檔尾，避免正文／稽核邊界混讀。
- 保留：本文件正文規範與索引條目全量承接，不做摘要縮水；僅進行引用檔名一致化與結構去混讀收斂。


### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：ca7ffed4617f6d0daf76396848c8ed3eeea89563f068ca850cec46e9a0f98355
### 3) 適用範圍（Scope）
本次覆蓋版修正範圍僅限於 doc_key=DOCUMENT_INDEX：
- §5 Authoritative Index（ACTIVE=21）之檔名引用一致化（以本專案現行覆蓋輸出檔名為準）
- 正文／稽核邊界去混讀（單一 H1；檔尾稽核區塊固定化；既有稽核內容以 Legacy Snapshot 承接）
- 不修改其他 doc_key 文件正文內容（僅更新本檔引用之檔名字串）


### 4) 裁決承接（Audit Hand-off）
- 本檔為 DOCUMENT_INDEX 現行唯一可引用正文。
- 後續若任何 doc_key 之覆蓋輸出檔名變更，必須同步回寫本檔 §5（Authoritative Index）以維持裁決入口的唯一性。
- 若與其他治理文件存在衝突，裁決序位固定為：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。


