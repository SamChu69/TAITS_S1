# TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220
doc_key：DOCUMENT_INDEX  
治理等級：A+（Document Governance Resolution Canon｜文件位階裁決最高層）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（Index 為裁決依據；Only-Add 演進）  
版本日期：2025-12-20  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
平行參照：VERSION_AUDIT / MASTER_ARCH / MASTER_CANON / ARCH_FLOW / FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / DEPLOY_OPS / LOCAL_ENV / DATA_SOURCES / TWSE_RULES / STRATEGY_UNIVERSE / STRATEGY_FEATURE_INDEX / BEGINNER_GUIDE / README / GOVERNANCE_STATE_*  
變更原則：Only-Add（只可新增，不可刪減／覆寫／偷換語義；Index 變更必須可稽核）  
核心裁決：Index 裁決（未列入 Index＝不具治理效力；衝突裁決以本文件為準）  

---

## 0. 文件定位（Why DOCUMENT_INDEX Is Power）

在 TAITS 中，**文件不是說明書，而是制度本體**。  
因此必須存在一份「裁決文件」來終止任何解釋權爭奪：

- 誰有權定義什麼（權力邊界）
- 文件衝突時誰覆蓋誰（覆蓋裁決）
- 誰可以引用哪一層文件（引用合法性）
- 哪些文件在此刻有效（ACTIVE 唯一性）
- 未收錄文件一律不得作為治理依據（Index 裁決）

📌 **本文件只做裁決，不做內容創作。**  
📌 本文件不提供策略、不提供流程、不提供實作；它只決定「誰有資格提供那些東西」。

---

## 1. TAITS 文件治理的不可動搖鐵律（Hard Laws）

### 1.1 A+ 母法不可被覆寫
- `TAITS_AI_行為與決策治理最終規則全集__251217.md`（A+）  
為最高母法；任何與之衝突之內容，**自動失效，無需宣告**。

### 1.2 Index 裁決（未列入＝無效）
- **任何文件、任何片段、任何外部連結**，若未被本文件收錄為「治理有效」，不得作為：
  - 系統行為依據
  - AI 推論依據
  - 人類裁決依據
  - 風控／合規／執行裁決依據

> **文件沒被 Index 收錄＝系統不承認。**

### 1.3 上位覆蓋下位（無需協調）
- 發生衝突時：
  - **不協調、不折衷、不調和**
  - 直接適用上位文件
- 下位文件不得引入新權力，不得創造上位文件未授權之例外。

### 1.4 Only-Add（只增不減）
- 所有治理有效文件在 ACTIVE 狀態下：
  - 只能新增（Only-Add）
  - 禁止刪除、覆寫、偷換語義、摘要化導致語義縮減
- Index 亦同（Index 的裁決能力不得被弱化）。

### 1.5 無審計＝未發生（Audit Supremacy）
- 任何聲稱「依據文件」的行為，若不能指向：
  - 文件版本（version_date / hash）
  - 章節定位
  - 變更帳本（VERSION_AUDIT）
則治理上視為：**未引用、未發生、不得成立**。

---

## 2. doc_key 制度（唯一性、可追溯、不可偽造）

### 2.1 doc_key 的法定位
`doc_key` 是 TAITS 的「文件身份證」，其職責：
- 唯一識別一份治理文件的「制度身分」
- 使版本控管、引用審計、回放重建可落地

### 2.2 doc_key 唯一性（Hard Gate）
- 一份治理文件 **必須且只能**有一個 doc_key
- 一個 doc_key **在 ACTIVE 範圍內不可重複**
- 禁止用「改檔名/改 key」規避治理約束（視為重大違規）

### 2.3 doc_key 與檔名的關係
- 檔名可含日期、版本、描述
- doc_key 不能隨意變更（除非以「新文件」形式新增，並在 Index 中明確裁決舊新關係）

---

## 3. 治理等級（Governance Level）與裁決力

### 3.1 等級定義（唯一有效）
- **A+｜Supreme Canon**：最高母法（不可覆寫、不可簡化、不可 AI 補完）
- **A｜Constitutional**：憲法級（定義本質、主權、三權分立、鐵律、最高否決）
- **B｜Governance / Spec**：制度與規格級（流程、架構、風控、執行、介面、資料、策略制度）
- **C｜Operational / Guide**：操作與教學級（不得新增治理權力）

> 等級不是「重要性」主觀評分；等級是「發生衝突時誰能裁決誰」。

### 3.2 覆蓋規則（Override Rules）
- A+ 覆蓋 A / B / C
- A 覆蓋 B / C
- B 不得覆蓋 A+ / A
- C 不得覆蓋任何上位文件

### 3.3 否決權的裁決位置（Veto Placement）
否決權不是「意見」，是制度機制。  
任何否決一旦成立，必須：
- 立即生效
- 不可用績效、緊急性、人類直覺要求通融
- 留存原因碼與證據快照（可回放、可稽核）

---

## 4. ACTIVE 唯一性（同 doc_key 僅能有一份 ACTIVE）

### 4.1 ACTIVE 的定義
- `版本狀態：ACTIVE` 代表：
  - 在「此刻」具有治理效力
  - 可被系統／AI／人類引用作為裁決依據

### 4.2 唯一性規則（Hard Gate）
- 對同一 doc_key：
  - **只允許 1 份 ACTIVE**
- 若要更換 ACTIVE：
  - 必須新增新版本文件
  - 舊版本狀態須調整為 ARCHIVED（或等價狀態）
  - 並在 VERSION_AUDIT 留下變更帳本（含原因、批准者、時間、影響範圍）

---

## 5. TAITS 治理有效文件清單（Authoritative Index｜唯一有效）

> 本表為「治理有效」文件全集。  
> **不在表內＝不具治理效力。**  
> 本表只增不減（Only-Add）；新增/改狀態必須可稽核（VERSION_AUDIT）。

### 5.1 A+（Supreme Canon）
| 文件名稱 | doc_key | 治理等級 | 版本狀態 | 說明 |
|---|---|---:|---|---|
| TAITS_AI_行為與決策治理最終規則全集__251217.md | AI_GOV | A+ | ACTIVE | 全系統 AI 行為與決策治理母法 |

### 5.2 A（Constitutional）
| 文件名稱 | doc_key | 治理等級 | 版本狀態 | 說明 |
|---|---|---:|---|---|
| TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md | MASTER_ARCH | A | ACTIVE | 人類主權、三權分立、Only-Add、邊界鐵律 |
| TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md | MASTER_CANON | A | ACTIVE | L1–L11 Canonical Flow 最高總綱與全資訊體系 |

### 5.3 A（Governance State Documents｜治理狀態裁決）
| 文件名稱 | doc_key | 治理等級 | 版本狀態 | 說明 |
|---|---|---:|---|---|
| TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md | GOVERNANCE_STATE_FREEZE_V1 | A | ACTIVE | 宣告 Freeze v1.0 生效：對所有 B/C 文件施加 Only-Add 與變更門檻 |

> 註：未來若新增 UNFREEZE 文件，必須同樣納入本表，並遵守 ACTIVE 唯一性（同類 doc_key 規則）。

### 5.4 B（Governance / Spec）
| 文件名稱 | doc_key | 治理等級 | 版本狀態 | 說明 |
|---|---|---:|---|---|
| TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md | DOCUMENT_INDEX | A+ | ACTIVE | 文件位階裁決最高層（本文件） |
| TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md | ARCH_FLOW | B+ | ACTIVE | L1–L11 流程細化、審計/回放一致性 |
| TAITS_全系統架構總覽（FULL_ARCH）__251219.md | FULL_ARCH | B | ACTIVE | 橫向模組 × 縱向層級架構地圖 |
| TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md | RISK_COMPLIANCE | A | ACTIVE | 最高否決權、理由碼、PASS/VETO Gate |
| TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md | EXECUTION_CONTROL | A | ACTIVE | Human-in-the-Loop + Token + Kill Switch + 審計 |
| TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md | UI_SPEC | B | ACTIVE | UI 決策可視化、否決呈現、Decision Trace |
| TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md | DEPLOY_OPS | B | ACTIVE | 部署、回滾、停機、Runbook、Live 運作制度 |
| TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md | LOCAL_ENV | C+ | ACTIVE | 金鑰隔離、環境檢核、敏感資料禁止入 repo |
| TAITS_資料來源全集（DATA_SOURCES）__251219.md | DATA_SOURCES | B | ACTIVE | 官方優先、來源追溯、Fallback、Provenance |
| TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md | TWSE_RULES | B | ACTIVE | 交易規則參考、觸發映射、制度快照 |
| TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md | STRATEGY_UNIVERSE | B | ACTIVE | 策略白名單、生命周期、策略元資料 |
| TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md | STRATEGY_FEATURE_INDEX | B | ACTIVE | 特徵與因子定義、審計、禁止信號化偷換 |
| TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md | VERSION_AUDIT | B | ACTIVE | 變更帳本、回放、稽核證據、Only-Add 執行方式 |
| TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md | GOVERNANCE_GATE_SPEC | B | ACTIVE | L9 治理閘門：完整性、引用合法性、拒絕與退回語義 |

> 註：LOCAL_ENV 若被定義為 B 或 C，須以 A/A+ 上位文件裁決；本 Index 現階段僅「收錄與引用裁決」，不擅自改寫其治理定位。

### 5.5 C（Operational / Guide）
| 文件名稱 | doc_key | 治理等級 | 版本狀態 | 說明 |
|---|---|---:|---|---|
| TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219.md | BEGINNER_GUIDE | C | ACTIVE | 新手操作引導；不得新增治理權力 |
| README.md | README | C | ACTIVE | 專案總覽、使用方式、責任聲明；不得越權 |

---

## 6. 文件衝突裁決程序（Conflict Resolution Protocol）

當任意內容衝突時，裁決流程如下（不可跳步）：

1. **確認是否在 Index（本文件）內**
   - 不在 Index：直接判定無效（STOP）
2. **確認 doc_key 與版本狀態**
   - 非 ACTIVE：不得引用（STOP）
3. **套用治理等級覆蓋規則（A+ > A > B > C）**
4. **若同級衝突**
   - 以「更上位約束文件」裁決（如 MASTER_ARCH / MASTER_CANON）
   - 若仍無法裁決：視為治理缺口 → **保守禁止**（STOP / FREEZE 依 DEPLOY_OPS）
5. **留下稽核輸出**
   - 必須在 VERSION_AUDIT 留存裁決紀錄（含衝突片段定位與最終裁決依據）

---

## 7. 引用合法性（Citation Legality）與最小格式

### 7.1 最小合法引用格式（Hard Gate）
任何模組／AI／人類若聲稱「依據文件」，必須同時提供：

- `doc_key`
- `版本日期`（YYYY-MM-DD 或文件命名日期）
- `章節定位`（如 §3.2 / 章-節-項）
- `引用目的`（用於：否決／流程／UI 呈現／部署裁決／資料來源裁決等）

缺任一項：**引用無效**。

### 7.2 禁止事項（Citation Forbidden）
- 模糊引用（例如：依規範、依母法、依架構）但未提供章節定位
- 引用非 Index 文件作為裁決依據
- 以外部網站／文章作為制度裁決（可作補充資訊，但不得裁決）

---

## 8. 主體可引用權限（Who Can Cite What｜權力邊界）

> 本節提供「最低約束」，實際更細規則以 A+ / MASTER_ARCH / 各規格文件裁決。

### 8.1 AI / Agent（任何 AI）
- 可引用：A+ / A / B
- 不可引用：C 作為「裁決依據」（可引用作操作說明，但不得用來覆寫制度）
- 禁止：
  - 補完文件缺失條款
  - 自行推論文件意圖
  - 以「合理」改寫既有語義

### 8.2 Strategy（策略/研究模組）
- 可引用：DATA_SOURCES / STRATEGY_UNIVERSE / STRATEGY_FEATURE_INDEX / ARCH_FLOW（僅流程語義）
- 不可引用：EXECUTION_CONTROL 作為下單依據；不得主張執行權力
- 永遠禁止：策略直連下單

### 8.3 Risk/Compliance（風控合規）
- 可引用：A+ / A / B（含 TWSE_RULES、DATA_SOURCES、DEPLOY_OPS）
- 具備：最高否決裁決（以 RISK_COMPLIANCE 為準）
- 禁止：以績效、勝率、回測曲線弱化否決

### 8.4 Execution（執行模組）
- 可引用：EXECUTION_CONTROL / RISK_COMPLIANCE / DEPLOY_OPS / TWSE_RULES
- 不可引用：策略文件作為執行方向來源（Execution 不得自生成方向）

### 8.5 Human（人類）
- 可引用：UI_SPEC / MASTER_CANON / RISK_COMPLIANCE / DEPLOY_OPS / VERSION_AUDIT
- 注意：人類有裁決權（L10），但不得「改寫文件含義」。

---

## 9. 版本控管與變更帳本（Index Change Ledger）

### 9.1 Index 變更的必備審計輸出
任何對 DOCUMENT_INDEX 的增補，必須在 VERSION_AUDIT 形成紀錄，至少包含：

- `change_id`
- `doc_key=DOCUMENT_INDEX`
- `change_type`（ADD / STATUS_CHANGE / METADATA_FIX）
- `added_items[]`（新增之文件或條目）
- `reason`
- `approver`
- `effective_time`
- `backward_compatibility`（對回放相容性的聲明）

### 9.2 禁止的 Index 變更
- 刪除既有條目
- 降低治理等級（A+→A→B→C）
- 將 ACTIVE 改為多份同 doc_key
- 以改名/改 key 規避 Only-Add 與 Freeze

---

## 10. 合規檢核清單（DOCUMENT_INDEX 專屬）

- [ ] 所有治理文件皆有 doc_key
- [ ] 同 doc_key 僅一份 ACTIVE
- [ ] 所有引用皆可定位到版本與章節
- [ ] 未收錄文件不得被引用作裁決
- [ ] Index 變更皆有 VERSION_AUDIT 紀錄
- [ ] Freeze 狀態文件被收錄且可裁決 B/C 變更規則

---

## 11. 最終宣告（Final Declaration）

在 TAITS 中：

- **Index 不是參考表，而是裁決權本身。**
- **未列入 Index 的文件，不具治理效力。**
- **任何衝突裁決以本文件為準，且必須可稽核、可回放。**

（DOCUMENT_INDEX｜A+｜ACTIVE｜2025-12-20）

📑 DOCUMENT_INDEX｜索引指引補充（治理指引附錄）

本附錄僅用於閱讀、引用與裁決指引，
不構成任何新規則、不改寫任何既有文件語義。
若與任何文件產生解讀衝突，仍以 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV 為最終裁決順序。

一、裁決用途矩陣（Authority Usage Matrix）

目的：避免在多份 A/A+ 級文件同時存在時，
產生「誰負責裁決什麼」的誤判。

文件	裁決用途定位	可裁決事項	不得裁決事項
AI_GOV（A+）	AI 行為與決策最終治理	AI 行為邊界、AI 可否參與決策	系統架構、交易策略
DOCUMENT_INDEX（A）	裁決索引與優先序	文件權威順序、衝突指引	任何業務邏輯
MASTER_ARCH（A）	系統母體憲法	核心鐵律、不可違反原則	流程細節、實作
MASTER_CANON（A）	Canonical Flow	L1–L11 流程結構	策略內容、UI 行為
RISK_COMPLIANCE（A）	最高否決權	風險/合規否決	流程重排、UI 設計
GOV_GATE_SPEC（A）	治理閘門	Gate 判斷條件	策略細節
UI_SPEC（A）	人機決策主權	人類介入權限	風控裁決
VERSION_AUDIT（A）	版本/稽核	追溯與審計	系統設計
FULL_ARCH / ARCH_FLOW（B）	描述與展開	說明性參考	任何裁決
README / BEGINNER_GUIDE（C）	導覽與操作	使用說明	任何裁決

📌 裁決原則提醒：

否決權（Risk/Compliance）永遠高於執行與策略

描述文件（B/C 級）不得被視為裁決依據

二、Freeze 狀態可行為清單（Index-Level）

目的：避免在 Freeze 生效期間，
操作/工程文件被誤解為可進行結構性調整。

✅ Freeze 期間「允許」行為

文件閱讀、引用、稽核

策略/資料/因子之描述性補充（不改語義）

稽核、版本標記、狀態查詢

教學與導覽文件之指引性補充

❌ Freeze 期間「禁止」行為

任何結構性變更

Canonical Flow（L1–L11）調整

治理閘門、否決邏輯之改寫

Agent / Strategy / Execution 的結構重排

架構、流程、權限邊界之修改

📌 判斷原則：

若行為可能影響「誰能否決誰、流程如何走、權限如何分配」
→ 視為結構性變更，Freeze 下禁止。

三、索引使用說明（強制）

本附錄僅作為 DOCUMENT_INDEX 的閱讀與引用指引

不得被任何文件引用為「新規則來源」

不得在未解除 Freeze 前，據此進行任何結構調整

✅ 狀態確認

本補充 不新增任何治理規則

本補充 不改寫任何既有文件

本補充 僅提升裁決鏈可讀性與一致性

---

# Appendix A｜Only-Add：DOCUMENT_INDEX × MASTER_CANON 對位附錄（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 對位母法：MASTER_CANON（Canonical Flow L1–L11）  
> 裁決序位：以本文件既有「衝突裁決程序」與「治理等級覆蓋規則」為準；本附錄僅補齊對位解讀與引用一致性規則（不新增新權力、不改寫既有裁決機制）。

---

## A.1 本附錄目的（不可省略）

本附錄用於解決一個常見但高風險的治理誤讀：

- MASTER_CANON 被誤當成「文件清單與有效性裁決」  
- DOCUMENT_INDEX 被誤當成「流程母法與層級語義定義」

上述誤讀會導致「引用越權」與「裁決鏈斷裂」。  
因此本附錄以 Only-Add 方式，將 DOCUMENT_INDEX 與 MASTER_CANON 的職責做出可稽核、可操作的對位界線。

---

## A.2 DOCUMENT_INDEX 與 MASTER_CANON 的「不同」：權力來源與責任分工（對位總結）

### A.2.1 DOCUMENT_INDEX（本文件）—「可引用性」與「文件裁決」的最高層

DOCUMENT_INDEX 的職責是裁決「文件世界的合法性」：

1) 什麼文件在此刻具治理效力（ACTIVE 唯一性）  
2) 哪些文件可被引用作裁決依據（Index 裁決：未收錄＝無效）  
3) 文件衝突時如何套用治理等級覆蓋規則（A+ > A > B > C）  
4) 引用最小格式（doc_key / 版本日期 / 章節定位 / 引用目的）  
5) 變更必須可稽核（VERSION_AUDIT）

> 核心一句話：  
> **DOCUMENT_INDEX 決定「誰有資格說話、哪份文件有權力被引用」。**

---

### A.2.2 MASTER_CANON —「層級語義」與「Canonical Flow」的最高母法

MASTER_CANON 的職責是裁決「系統如何運作」：

1) Canonical Flow（L1–L11）的存在性、邊界與不可越權原則  
2) 各層的輸入/輸出契約、稽核要求、回放一致性（Replay）  
3) 角色分工（人類/AI/系統）在流程中如何定位  
4) 跨層互鎖（Regime/Risk/Compliance/Execution/UI）的流程語義

> 核心一句話：  
> **MASTER_CANON 決定「該怎麼走流程、什麼叫合規的層級行為」。**

---

### A.2.3 一句話界線（Hard Boundary）

- **DOCUMENT_INDEX 管「文件是否合法、是否可引用、誰覆蓋誰」。**  
- **MASTER_CANON 管「流程怎麼走、層級語義如何解讀、越權如何判定」。**

兩者互補，不互相替代。

---

## A.3 與 MASTER_CANON 的「對位使用規則」（避免誤用）

> 本節不改寫既有「衝突裁決程序」，只把操作順序固化成可讀規則。

### A.3.1 先做「可引用性 Gate」，再做「語義裁決」

所有引用與裁決，必須依序滿足：

1) **Index Gate（可引用性）**  
   - 文件是否在本文件的「治理有效文件清單」中？  
   - 是否為該 doc_key 之唯一 ACTIVE？  
   - 若否：直接 STOP（不得引用、不得裁決）

2) **Canonical Interpretation（語義解讀）**  
   - 若屬流程/層級/越權問題：以 MASTER_CANON 的 L1–L11 語義解讀  
   - 若屬風控/合規否決：以 RISK_COMPLIANCE 的否決條款裁決  
   - 若屬執行與控制：以 EXECUTION_CONTROL 的執行約束裁決  
   - 若屬人機介面：以 UI_SPEC 的呈現與決策主權約束裁決

> 重點：  
> DOCUMENT_INDEX 不替代 MASTER_CANON 的流程語義；MASTER_CANON 不替代 DOCUMENT_INDEX 的可引用性裁決。

---

## A.4 「治理等級」與「文件表格」之詮釋一致性（Only-Add Clarification）

### A.4.1 Index 表格的法律效力

本文件第 5 章（治理有效文件清單）之表格，對以下事項具裁決效力：

- 收錄與否（是否具治理效力）  
- doc_key（唯一識別）  
- 版本狀態（ACTIVE / ARCHIVED 等）  
- 說明（用途摘要，不構成覆寫他文件正文）

### A.4.2 治理等級欄位之一致性要求（避免「等級漂移」）

若發生下列情況：

- Index 表格中的「治理等級」與該文件檔頭（doc header）標示不一致  
- 或同一文件在不同地方被標為不同等級

則視為 **Metadata Discrepancy（中繼資料差異）**，必須：

1) 以本文件既有「衝突裁決程序」處理引用與裁決（保守適用更上位約束）  
2) 由 VERSION_AUDIT 建立一筆「METADATA_FIX」變更帳本（Only-Add）  
3) 後續僅以「新增修正說明段落」方式修補一致性（不得刪改既有段落）

> 目的：  
> 確保「等級」永遠可稽核、可回放、不可被改名或誤標而繞過治理。

---

## A.5 FILE UPDATE MODE 下新增文件進入 Index 的「固定模板」（Only-Add）

> 本節提供「新增條目」的固定寫法，用於未來擴充文件宇宙；  
> 不改寫既有規則，只降低錯誤率。

### A.5.1 新增治理文件條目（Index Entry Template）

- 文件名稱：`<filename>`  
- doc_key：`<DOC_KEY>`  
- 治理等級：`A+ / A / B / C`  
- 版本狀態：`ACTIVE / ARCHIVED / DEPRECATED / DRAFT`  
- 版本日期：`YYYY-MM-DD`  
- 對齊母法：`<上位約束>`  
- 平行參照：`<refs...>`  
- 說明：`<一句話定位；不得新增權力>`  
- 新增原因：`<why>`  
- 影響範圍：`<Research/Backtest/Simulation/Paper/Live>`  
- 稽核要求：`必須在 VERSION_AUDIT 留存 change_id、approver、effective_time、reason`

### A.5.2 Freeze v1.0 下的硬限制提醒（Index 專用）

- Freeze v1.0 期間：允許新增條目（Only-Add），但不得以新增條目形式「變相改寫」既有裁決權力與覆蓋秩序。  
- 任何新增條目若涉及「裁決序位、否決權、Canonical Flow」之變更意圖：  
  - 一律視為結構性變更  
  - Freeze 下不得成立  
  - 必須回到 GOVERNANCE_STATE／母法裁決後才可處理（本文件僅收錄裁決結果，不創造裁決本體）。

---

（Appendix A｜DOCUMENT_INDEX × MASTER_CANON 對位附錄 · Freeze v1.0 · Only-Add 完）
