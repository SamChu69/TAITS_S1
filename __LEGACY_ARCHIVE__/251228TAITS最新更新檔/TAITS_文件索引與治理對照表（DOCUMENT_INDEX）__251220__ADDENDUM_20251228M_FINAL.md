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

---

# Appendix 0｜DOCUMENT_INDEX 專屬附錄治理總則（Only-Add）

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 裁決位階：不高於 DOCUMENT_INDEX 正文；僅作補齊、對齊、指引用途  

## 0.1 本附錄存在理由（不可省略）

DOCUMENT_INDEX 作為 **A+ 文件位階裁決母表**，  
其正文負責「裁決本體」，而附錄（Appendix）負責：

- 補齊「裁決如何被穩定使用」的操作層說明  
- 補齊「避免誤讀、誤用、越權引用」的防呆結構  
- 補齊 Freeze 狀態下，Index 層可合法新增的治理指引  

📌 本附錄 **不新增任何新權力、不創造任何新制度**，  
📌 僅將 DOCUMENT_INDEX 既有裁決邏輯，轉化為「不可誤用的可操作結構」。

---

## 0.2 DOCUMENT_INDEX 附錄的法律地位（Hard Boundary）

- 本文件正文（第 0～11 章）仍為 **唯一裁決本體**
- 任何附錄內容：
  - 不得被引用為「新裁決依據」
  - 不得凌駕正文
  - 不得與正文產生競合解讀

> 若附錄與正文產生任何張力或歧義：  
> **一律以正文為準，附錄自動失效，不需宣告。**

---

# Appendix I｜附錄啟用索引表（Appendix Activation Index）

> 補充性質：Only-Add  
> 生效狀態：Freeze v1.0  
> 目的：讓「哪些附錄存在、附錄屬於誰、可否引用」可被一次性裁決

## I.1 附錄存在即須被索引（Hard Rule）

- **任何附錄若未被本表收錄**
  - 視為：不存在
  - 不得被引用
  - 不得作為治理、裁決、稽核依據

## I.2 DOCUMENT_INDEX 專屬附錄清單

| Appendix 編號 | 附錄名稱 | 所屬 doc_key | 生效狀態 | 說明 |
|---|---|---|---|---|
| Appendix 0 | DOCUMENT_INDEX 專屬附錄治理總則 | DOCUMENT_INDEX | ACTIVE | 定義附錄法律地位與使用邊界 |
| Appendix I | 附錄啟用索引表 | DOCUMENT_INDEX | ACTIVE | 裁決哪些附錄存在 |
| Appendix A | DOCUMENT_INDEX × MASTER_CANON 對位附錄 | DOCUMENT_INDEX | ACTIVE | 裁決「文件裁決」與「流程母法」邊界 |
| Appendix B | 文件引用合法性防呆附錄 | DOCUMENT_INDEX | ACTIVE | 防止模糊引用與越權 |
| Appendix C | Freeze v1.0 下 Index 可行為清單 | DOCUMENT_INDEX | ACTIVE | Freeze 期間 Index 層允許/禁止行為 |

> 註：  
> - 本表只增不減（Only-Add）  
> - 未來新增任何 Appendix，必須先補此表，否則該附錄治理上視為不存在

---

# Appendix A｜DOCUMENT_INDEX × MASTER_CANON 對位附錄（Freeze v1.0）

> 補充性質：Only-Add  
> 生效狀態：Freeze v1.0  
> 對位母法：MASTER_CANON（Canonical Flow L1–L11）

## A.1 為何必須存在此附錄（治理風險說明）

在實務中，最常見且最危險的誤用為：

- 將 MASTER_CANON 當成「文件合法性裁決表」
- 將 DOCUMENT_INDEX 誤解為「流程與層級母法」

此誤用一旦發生，將直接導致：
- AI / Agent 引用越權  
- 人類裁決錯置  
- 風控與流程裁決鏈斷裂  

因此本附錄 **僅用來固化邊界，不創造新邊界**。

## A.2 權責一句話裁決（不可簡化）

- **DOCUMENT_INDEX：裁決『誰有資格被引用、誰覆蓋誰』**  
- **MASTER_CANON：裁決『流程怎麼走、層級語義如何解讀』**

兩者互補，不互相替代。

## A.3 強制使用順序（Hard Sequence）

任何治理引用，必須嚴格依序：

1. **Index Gate**  
   - 文件是否在 DOCUMENT_INDEX 中？  
   - 是否為該 doc_key 唯一 ACTIVE？  
   - 否則：STOP（不得引用）

2. **Canonical Interpretation**  
   - 僅在通過 Index Gate 後  
   - 才可進入 MASTER_CANON 的 L1–L11 語義裁決

---

# Appendix B｜文件引用合法性防呆附錄（Citation Guard）

> 補充性質：Only-Add  
> 生效狀態：Freeze v1.0  

## B.1 最小合法引用格式（再次強化，不得省略）

任何聲稱「依據文件」的行為，**必須同時具備**：

- doc_key  
- 文件版本日期  
- 章節定位  
- 引用目的（裁決 / 否決 / 流程 / UI / 稽核）

缺一即視為：**未引用、未發生、不得成立**。

## B.2 明確禁止的引用行為（常見誤區）

- 「依母法」、「依架構」、「依規範」但無章節定位  
- 引用 README / BEGINNER_GUIDE 作為裁決依據  
- 引用未被 DOCUMENT_INDEX 收錄之文件  

---

# Appendix C｜Freeze v1.0 下 DOCUMENT_INDEX 可行為清單

> 補充性質：Only-Add  
> 生效狀態：Freeze v1.0  

## C.1 Freeze 期間允許（Index 層）

- 新增附錄（Only-Add）  
- 新增文件條目（不改裁決序位）  
- 補齊索引、對位、引用指引  

## C.2 Freeze 期間禁止（Index 層）

- 改寫裁決順位  
- 改寫治理等級  
- 改寫 Canonical Flow 的解讀權  

> 判斷原則（不可模糊）：  
> **若行為可能影響「誰能裁決誰」→ 一律視為結構性變更 → Freeze 下禁止。**

---

（Only-Add｜DOCUMENT_INDEX 附錄補齊 · 第 1 批 完）

---

# Appendix D｜DOCUMENT_INDEX × VERSION_AUDIT 對位附錄（Freeze v1.0｜Only-Add）

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 對位文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
> 裁決位階：不高於 DOCUMENT_INDEX 正文；僅補齊「Index 變更必可稽核」之落地對位口徑

---

## D.1 本附錄目的（不可省略）

DOCUMENT_INDEX 正文已明確宣告：  
- Index 變更必須可稽核（VERSION_AUDIT）  
- 無審計＝未發生（Audit Supremacy）

本附錄僅補齊：  
1) **哪些 Index 行為必須寫入 VERSION_AUDIT**  
2) **寫入時的最小欄位集合（不可縮減）**  
3) **Freeze v1.0 下的保守判準（避免變相改寫）**

---

## D.2 Index 變更類型（Change Types｜Only-Add）

> 本節不改寫正文第 9 章（Index Change Ledger），僅把可稽核類型「枚舉化」以防漏報。

以下行為一律視為「Index 變更」，必須在 VERSION_AUDIT 留存：

### D.2.1 ADD_ENTRY（新增治理文件條目）
- 新增任何「治理有效文件清單」之新列（任意等級 A+/A/B/C）

### D.2.2 STATUS_CHANGE（版本狀態變更）
- 任一 doc_key 的 `版本狀態` 變更（例如：ACTIVE → ARCHIVED / DEPRECATED / DRAFT）

### D.2.3 METADATA_FIX（中繼資料修補）
- 修補 doc header / Index 表格之 metadata 不一致（僅能以新增說明方式修補，不得覆寫原值）
- 例：治理等級標示不一致、檔名日期與版本日期對齊說明等

### D.2.4 APPENDIX_ADD（新增附錄）
- 新增任何 Appendix（含新增「Appendix 啟用索引表」之條目）

### D.2.5 REFERENCE_EXPAND（平行參照擴充）
- 僅新增「平行參照」或「引用指引」之條目（不得引入新裁決權）

---

## D.3 VERSION_AUDIT 最小必填欄位（Hard Minimum）

對於上述任一變更類型，VERSION_AUDIT 至少必須包含：

- `change_id`（全域唯一）
- `change_time`（生效時間戳）
- `doc_key=DOCUMENT_INDEX`
- `change_type`（ADD_ENTRY / STATUS_CHANGE / METADATA_FIX / APPENDIX_ADD / REFERENCE_EXPAND）
- `change_scope`（Research / Backtest / Simulation / Paper / Live 影響範圍）
- `added_items[]`（新增內容之清單；若為狀態變更則列出變更項）
- `reason`（原因；不得以「整理」「優化」作為唯一原因）
- `approver`（批准者；人類主權）
- `evidence_refs[]`（對應章節定位或支持證據引用；至少能回到文段定位）
- `backward_compatibility`（回放相容性聲明；若可能影響回放，需明示保守策略）

缺任一欄位：視為 **未發生**（Audit Supremacy）。

---

## D.4 Freeze v1.0 下 Index 變更的保守判準（Hard Conservative Rule）

Freeze v1.0 期間，即使屬 Only-Add，也必須遵守：

- 任何新增若會造成「裁決序位」或「權力邊界」產生新的可解釋空間  
  → 一律視為結構性變更意圖  
  → Freeze 下不得成立  
  → Index 僅可「收錄已由上位文件裁決完成之結果」，不得先行創造裁決

---

# Appendix E｜DOCUMENT_INDEX × GOVERNANCE_GATE_SPEC 對位附錄（Freeze v1.0｜Only-Add）

> 補充性質：Only-Add  
> 生效狀態：Freeze v1.0  
> 對位文件：TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md（doc_key：GOVERNANCE_GATE_SPEC）  
> 目的：把「文件合法性裁決（Index）」與「治理閘門裁決（L9 Gate）」的關係鎖定為單一路徑

---

## E.1 核心一句話（不可省略）

- DOCUMENT_INDEX：裁決「文件是否可被引用」  
- GOVERNANCE_GATE_SPEC：裁決「一次輸出/一次提案是否符合治理門檻」

兩者關係必須是：  
> **先 Index Gate，再 Governance Gate；不得反向、不得跳步。**

---

## E.2 L9 Gate 必須強制執行 Index Gate（Hard Binding）

任何進入 L9（Governance Gate）的輸出（不論來自哪個模組/Agent/人類彙整），必須先通過：

1) **Index Gate（DOCUMENT_INDEX）**
   - 引用的 doc_key 是否存在於 Index？
   - 是否為該 doc_key 唯一 ACTIVE？
   - 是否提供最小引用格式（doc_key/版本/章節/目的）？

2) **Gate Spec（GOVERNANCE_GATE_SPEC）**
   - 完整性、合法性、可回放性、不可越權性之檢核

若 Index Gate 失敗：  
- L9 Gate 不得進一步審查內容優劣  
- 必須直接 **REJECT / RETURN**（依 Gate Spec 的拒絕語義）  
- 並要求補齊引用要件（不是補齊內容、不是補完制度）

---

## E.3 Gate 結果必須可回放連回 Index（Traceability Requirement）

L9 Gate 任一結果（PASS / RETURN / REJECT）必須在審計輸出中包含：

- `index_validation`：  
  - `doc_keys_used[]`  
  - `active_check_passed`（true/false）  
  - `citation_minimum_passed`（true/false）  
  - `index_version_ref`（DOCUMENT_INDEX 版本日期/定位）

缺失則視為：  
- Gate 結果不可成立（無審計＝未發生）

---

# Appendix F｜新增文件進入 Index 的固定模板（完整版｜Freeze v1.0｜Only-Add）

> 補充性質：Only-Add  
> 生效狀態：Freeze v1.0  
> 目的：避免新增文件條目時產生「隱性權力」或「狀態歧義」

---

## F.1 Index Entry（治理有效文件條目）標準模板

> 本模板僅用於「新增條目」；不得用於覆寫既有條目。

新增任一治理文件至 Index 時，必須同步提供以下欄位（不可縮減）：

- **文件名稱（含版本標記）**：`<filename>`  
- **doc_key**：`<DOC_KEY>`  
- **治理等級**：`A+ / A / B / C`  
- **版本狀態**：`ACTIVE / ARCHIVED / DEPRECATED / DRAFT / RESTRICTED`  
- **版本日期**：`YYYY-MM-DD`（或與檔名日期一致之版本日）  
- **對齊母法**：`AI_GOV / MASTER_ARCH / MASTER_CANON`（至少一項）  
- **上位約束**：`<higher_constraints...>`（明列，不可省略）  
- **平行參照**：`<peer_refs...>`（可多選）  
- **適用範圍**：`Research / Backtest / Simulation / Paper / Live`（可多選）  
- **變更原則聲明**：`Only-Add / Freeze v1.0`（若適用）  
- **一句話定位說明**：不得新增未授權權力、不得改寫既有裁決鏈  
- **納管要求**：必須建立 VERSION_AUDIT 變更帳本（change_id / approver / reason / effective_time）  

---

## F.2 doc_key 命名與生命週期約束（Hard Gate）

### F.2.1 doc_key 命名硬規則
- 必須全域唯一  
- 不得以相似 key 造成混淆（視為治理風險）  
- 不得以改 key 形式迴避 ACTIVE 唯一性與 Only-Add

### F.2.2 狀態集合（Status Vocabulary）
為避免狀態語義漂移，Index 層允許的狀態詞彙固定為：

- `ACTIVE`：此刻具治理效力，唯一可引用  
- `ARCHIVED`：歷史存檔，可回放，不可作「現行裁決」依據  
- `DEPRECATED`：準退役，不可新啟用，可回放  
- `DRAFT`：草稿，不具治理效力（除非上位文件另有裁決）  
- `RESTRICTED`：受限狀態（通常由風控/合規/治理觸發），僅允許特定範圍引用或僅研究用途（具體限制仍須由上位文件裁決）

> 注意：本節僅「固定詞彙」，不新增任何上位文件未授權之裁決權。

---

## F.3 ACTIVE 切換的固定流程（Index 層）

對同一 doc_key 進行 ACTIVE 切換時（例如新版本上線）：

1) 新版本文件先新增條目（不得覆寫舊條目）  
2) 新版本設為 `ACTIVE`  
3) 舊版本改為 `ARCHIVED`（或上位裁決之等價狀態）  
4) VERSION_AUDIT 必須留存：
   - `change_type=STATUS_CHANGE`
   - 舊新版本定位
   - 生效時間
   - 回放相容性聲明

缺任一步驟：切換無效。

---

# Appendix G｜Appendix / Addendum 命名與掛載規則（Freeze v1.0｜Only-Add）

> 補充性質：Only-Add  
> 生效狀態：Freeze v1.0  
> 目的：防止附錄編號混亂、重複、或被用來「變相改寫正文」

---

## G.1 附錄類型詞彙（Vocabulary）

- **Appendix**：附錄（治理補齊、對位、模板、指引；不得改寫正文）  
- **Addendum**：補遺（通常指新增政策性說明或補充規範，但不得創造未授權的新權力）  
- **Guideline**：指引（操作性說明；不得作裁決依據）  
- **Annotation**：註解（非約束性；不得參與裁決鏈）

---

## G.2 掛載位置硬規則（Hard Placement Rule）

- 所有 Appendix / Addendum 必須置於文件**最末端**  
- 不得插入正文中段（避免造成「重排/改寫」之誤讀）  
- 不得以附錄形式對正文做「替代性描述」  
  - 若附錄與正文產生張力：附錄自動失效

---

## G.3 附錄啟用必須回寫 Appendix Activation Index（Hard Rule）

- 新增任何 Appendix / Addendum  
  → 必須同步更新 **Appendix I｜附錄啟用索引表**  
  → 否則該附錄治理上視為不存在

---

（Only-Add｜DOCUMENT_INDEX 附錄補齊 · 第 2 批 完）

---

# Addendum 2025-12-27｜Only-Add：裁決順序字串統一 × 歧義消解（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位約束：TAITS_AI_行為與決策治理最終規則全集（AI_GOV｜A+）  
> 依據正文：§1（Hard Laws）／§3（治理等級與裁決力）／§6（文件衝突裁決程序）／§7（引用合法性）／§9（Index Change Ledger）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251227-0001`）  
> 目的：統一跨文件常見之「裁決順序字串」解讀口徑，避免字串被誤當成覆蓋規則；並將「Metadata Discrepancy（中繼資料差異）」之處置方式固定為可回放、可稽核之單一路徑。

---

## 0. 適用範圍與不適用範圍（Hard Boundary）

### 0.1 適用
本 Addendum 僅針對以下兩類高頻誤用進行歧義消解（不新增任何新權力）：

1) **「裁決順序字串」的誤讀**  
   例如：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`、`DOCUMENT_INDEX → MASTER_ARCH → AI_GOV`、或其他以箭頭呈現之排序描述。

2) **Metadata Discrepancy（中繼資料差異）的處置**  
   例如：Index 表格與文件檔頭（doc header）之 `doc_key / 治理等級 / 版本狀態 / 檔名標示 / 概念別名` 不一致。

### 0.2 不適用（禁止越權）
本 Addendum **不得**被用於：

- 變相改寫正文 §6 的「衝突裁決程序」或 §3 的「治理等級覆蓋規則（A+ > A > B > C）」  
- 以「字串統一」為名重新排序 A+/A/B/C 的覆蓋關係  
- 將任何文件升格／降格治理等級  
- 取代或弱化 AI_GOV（A+）之最高約束地位（正文 §1.1）

---

## 1. 「裁決順序字串」之法律定位（Mnemonic ≠ Override Rule）

### 1.1 定義：裁決順序字串僅是「閱讀／操作助記」，不是覆蓋規則
凡文件內出現之「裁決順序字串」（箭頭排序／高→低順位），**一律視為：**
- **閱讀／操作助記（Mnemonic）**，用於提示「先看哪份文件、再看哪份文件」；
- **不得**被解讀為「治理等級覆蓋規則」或「裁決權重新分配」。

> 若任何裁決順序字串與正文 §6（衝突裁決程序）或正文 §3（A+ > A > B > C）產生張力：  
> **一律以正文 §6／§3 為準，該字串僅作助記，且在該張力範圍內不具裁決力。**

### 1.2 統一解讀：所有衝突裁決必須回到 §6（不可跳步）
跨文件一切衝突裁決，必須依正文 §6 的固定步驟（不可跳步）：

1) **Index Gate**：先確認是否收錄於 Index、且為該 doc_key 唯一 ACTIVE（未收錄＝無效／非 ACTIVE＝不得引用）。  
2) **治理等級覆蓋**：套用 §3 的 A+ > A > B > C。  
3) **同級衝突**：依正文 §6 的規則，往更上位約束文件裁決；仍無法裁決則保守禁止（STOP）。  
4) **稽核留痕**：必須在 VERSION_AUDIT 留存裁決紀錄（正文 §1.5／§6／§9）。

本 Addendum 僅將上述流程「固定化為跨文件一致口徑」，不改寫其內容。

---

## 2. FILE UPDATE MODE 下「唯一可採用」的統一裁決口徑（可貼用字串）

> 用途：供未來所有 Addendum / Appendix / Guideline 在描述「裁決順序」時，使用同一套不歧義表述，避免再出現互斥字串。

### 2.1 統一口徑（建議固定寫法）
在 Freeze v1.0（Only-Add）期間，任何文件若需要描述「裁決順序」，**應使用以下唯一口徑**：

- **Index Gate（合法性）**：`DOCUMENT_INDEX`（確認收錄／doc_key／ACTIVE 唯一性／最小引用格式）  
- **Override Rule（覆蓋規則）**：`A+ > A > B > C`（依正文 §3／§6）  
- **Domain Canon（領域母法／規格）**：依問題性質套用對應文件（不改寫覆蓋規則）  
  - AI 行為與決策邊界 → `AI_GOV（A+）`
  - 系統憲法鐵律／主權與邊界 → `MASTER_ARCH（A）`
  - Canonical Flow（L1–L11）語義／越權判定 → `MASTER_CANON（A）`
  - 風險與合規否決 → `RISK_COMPLIANCE（A）`
  - 執行控制／Kill Switch／委託與回報 → `EXECUTION_CONTROL（A）`
  - UI 主權與決策呈現 → `UI_SPEC（B）`
  - 部署／營運／停機與回滾 → `DEPLOY_OPS（B）`
  - 資料來源治理與 Provenance → `DATA_SOURCES（B）`
  - 交易規則參考（制度快照） → `TWSE_RULES（B）`
  - 版本與稽核可追溯 → `VERSION_AUDIT（B）`
- **Audit Supremacy（稽核）**：任何裁決／修補必須落到 `VERSION_AUDIT`（正文 §1.5／§6／§9）

> 注意：上述「Domain Canon」僅是「在通過 Index Gate 並套用覆蓋規則後」的領域選用提示；  
> **其存在不改寫覆蓋規則本身。**

### 2.2 舊字串的統一解釋（兼容既有文件，不改原文）
為避免改寫既有文件，本 Addendum 對常見舊字串做一致解釋如下（Only-Add）：

- **字串 A：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`**  
  解釋：表示「先驗證文件合法性（Index Gate），再受憲法邊界約束（MASTER_ARCH），再以流程語義解讀（MASTER_CANON）」；  
  **不表示** AI_GOV 失去 A+ 覆蓋地位；若議題涉及 AI 行為／AI 參與裁決邊界，仍以 AI_GOV（A+）為最高約束。

- **字串 B：`DOCUMENT_INDEX → MASTER_ARCH → AI_GOV`**  
  解釋：表示「先驗證文件合法性（Index Gate），再受憲法邊界約束（MASTER_ARCH），並特別提醒 AI 行為仍受 AI_GOV 約束」；  
  **不表示** DOCUMENT_INDEX 或 MASTER_ARCH 可覆蓋 AI_GOV；一切覆蓋仍回到 §3／§6。

> 任何其他以箭頭描述之排序，一律依本節規則視為助記；遇張力回到正文 §6／§3。

---

## 3. Metadata Discrepancy（中繼資料差異）之單一路徑處置（Only-Add）

### 3.1 定義：何謂 Metadata Discrepancy
凡出現以下任一項不一致，皆屬「Metadata Discrepancy」：

- Index 表格之 `doc_key / 治理等級 / 版本狀態 / 文件名稱版本標記` 與文件檔頭（doc header）標示不一致  
- 文件內將「概念名詞／別名」誤標為 doc_key，導致引用合法性混亂  
- 同一 doc_key 在 ACTIVE 範圍內出現多份「看似可引用」之版本（違反 ACTIVE 唯一性）

### 3.2 單一路徑（不可跳步）
遇到 Metadata Discrepancy 時，必須依以下順序處置（Only-Add）：

1) **保守引用**：在裁決前，引用端必須以 Index 表格裁決之 `doc_key / ACTIVE` 為唯一合法引用來源（避免誤用檔頭）。  
2) **VERSION_AUDIT 留痕**：新增一筆 `METADATA_FIX`（Append-only），包含：差異描述、影響範圍、引用修補口徑、evidence refs、批准者與生效時間。  
3) **文件端 Only-Add 修補**：在相關文件中以 Addendum / Appendix 方式新增「一致性修補說明」；不得刪改原檔頭或既有段落。  
4) **Index 端必要補強**：若差異會影響跨文件引用（例如 doc_key 誤用風險高），則可在本文件新增「歧義消解附錄」或「已知差異登錄」（只增不減）。

### 3.3 本次已登錄之 METADATA_FIX（可回放）
- 條目：`VA-METADATA_FIX-20251227-0001`  
- 主旨：修補 DATA_SOURCES 文件內「DATA_UNIVERSE（概念名詞）」被誤當 doc_key 之風險，並鎖定引用合法性（doc_key=DATA_SOURCES）。  
- 稽核位置：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（Append-only）。

---

## 4. 最終宣告（針對本 Addendum）

- 本 Addendum 僅統一「字串解讀口徑」與「中繼資料差異處置路徑」，不新增任何新制度、不改寫正文裁決程序。  
- 任何裁決仍必須回到：正文 §6（衝突裁決程序）＋正文 §3（A+ > A > B > C）＋正文 §7（引用合法性）＋正文 §1.5（無審計＝未發生）。  
- 本 Addendum 自發布日起生效於 Freeze v1.0 期間之 FILE UPDATE MODE，並採 Only-Add 永續保留（Append-only）。

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）

---

# Addendum 2025-12-27-C｜Only-Add：批次輸出映射表（doc_key → Latest Artifact）× Freeze v1.0（Index Gate 載入收斂）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 批次識別：date=2025-12-27｜batch_id=BATCH-20251227-ADDENDUM-PACK-01  
> 上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+｜Authoritative Index）＋MASTER_ARCH（A）＋MASTER_CANON（A）  
> 稽核對位：VERSION_AUDIT:VA-METADATA_FIX-20251227-0018（建議同時補登 VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger）  
> 目的：在 Freeze v1.0 期間，將 2025-12-27 批次所產出之「最新落盤版本（Latest Artifact）」以 mapping 表形式追加，作為 Index Gate 載入時的操作收斂參考；本 Addendum 不改寫任何原有 Authoritative Index 表格內容，僅提供「doc_key → Latest Artifact」的可機器檢索映射，避免新對話/工程端載入舊檔名。

---

## C1. 使用規則（Hard Rules）

1) 本映射表為 **操作收斂參考（Operational Mapping）**：  
   - 不取代 DOCUMENT_INDEX 既有 Authoritative Index 表格  
   - 不改變治理等級、覆蓋規則、ACTIVE 判定或衝突裁決程序

2) 任何涉及 ACTIVE/doc_key/治理等級/版本有效性之裁決：  
   - 一律以 DOCUMENT_INDEX 的 Authoritative Index 表格為準（本表僅提供「最新檔名」參考）

3) 若 repo 落盤檔名與本表不同：  
   - 以 repo 落盤為準  
   - 但不得刪除此 Addendum；應以 Only-Add 方式追加修正版映射（append-only）

---

## C2. 2025-12-27 批次輸出映射表（doc_key → Latest Artifact）

| doc_key | latest_artifact_filename | change_summary | audit_anchor_fix_id |
|---|---|---|---|
| `AI_GOV` | `TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251227_FINAL.md` | Only-Add｜Snapshot 不裁決／Index Gate／引用最小格式 | `VA-METADATA_FIX-20251227-0014` |
| `DOCUMENT_INDEX` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228_FINAL.md` | Only-Add｜批次映射表（本次收斂） | `VA-METADATA_FIX-20251227-0018` |
| `MASTER_ARCH` | `TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜Snapshot 不裁決／S・B+・C+ 標籤回歸 | `VA-METADATA_FIX-20251227-0015` |
| `MASTER_CANON` | `TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜治理口徑補強（S=Label 等） | `VA-METADATA_FIX-20251227-0005` |
| `FULL_ARCH` | `TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜DATA_UNIVERSE alias 封口／引用回歸 | `VA-METADATA_FIX-20251227-0005` |
| `ARCH_FLOW` | `TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜口徑對齊與引用模板 | `VA-METADATA_FIX-20251227-0003` |
| `GOVERNANCE_GATE_SPEC` | `TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜裁決字串助記化／歧義消解 | `VA-METADATA_FIX-20251227-0002` |
| `RISK_COMPLIANCE` | `TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜S=Label 對齊／引用口徑修補 | `VA-METADATA_FIX-20251227-0008` |
| `EXECUTION_CONTROL` | `TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜S=Label 對齊／引用口徑修補 | `VA-METADATA_FIX-20251227-0002` |
| `LOCAL_ENV` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜Evidence Chain／引用模板 | `VA-METADATA_FIX-20251227-0004` |
| `DEPLOY_OPS` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜Deploy/Ops 證據鏈最小欄位／對齊 LOCAL_ENV | `VA-METADATA_FIX-20251227-0012` |
| `UI_SPEC` | `TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜UI Trace 最小引用欄位／Index Gate | `VA-METADATA_FIX-20251227-0011` |
| `VERSION_AUDIT` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜METADATA_FIX Ledger 批次補登 | `VA-METADATA_FIX-20251227-0001` |
| `DATA_SOURCES` | `TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_1_FINAL.md` | Only-Add｜Addendum 0/0.1（DATA_UNIVERSE=alias／引用回歸） | `VA-METADATA_FIX-20251227-0005` |
| `TWSE_RULES` | `TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜引用口徑一致化 | `VA-METADATA_FIX-20251227-0005` |
| `STRATEGY_UNIVERSE` | `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜DATA_UNIVERSE alias 封口／引用回歸 DATA_SOURCES | `VA-METADATA_FIX-20251227-0006` |
| `STRATEGY_FEATURE_INDEX` | `TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜B+ Sub-Label（bucket=B）對齊／引用模板 | `VA-METADATA_FIX-20251227-0009` |
| `PROJECT_PROMPT` | `TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md` | Only-Add｜Index Gate First／ACTIVE 不固化／引用最小格式 | `VA-METADATA_FIX-20251227-0007` |
| `README` | `TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md` | Only-Add｜文件清單/數量快照化／Index Gate | `VA-METADATA_FIX-20251227-0010` |
| `BEGINNER_GUIDE` | `TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md` | Only-Add｜新手入口快照化／Index Gate／引用最小格式 | `VA-METADATA_FIX-20251227-0013` |
| `GOVERNANCE_STATE` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251227_FINAL.md` | Only-Add｜狀態檔快照化／Index Gate／引用最小格式 | `VA-METADATA_FIX-20251227-0016` |
| `PROCESS_ANCHOR` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md` | Only-Add｜定錨入口快照化／Index Gate／工程引用最小格式 | `VA-METADATA_FIX-20251227-0017` |

---

（Addendum 2025-12-27-C｜Only-Add｜Freeze v1.0 完）

---

# Addendum 2025-12-28-D｜Only-Add：Latest Mapping 機器可讀附錄（YAML/JSON）× Freeze v1.0（Index Gate 載入自動化）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 批次識別：date=2025-12-28｜batch_id=BATCH-20251227-ADDENDUM-PACK-01B  
> 上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+｜Authoritative Index）＋MASTER_ARCH（A）＋MASTER_CANON（A）  
> 稽核對位：VERSION_AUDIT:VA-METADATA_FIX-20251227-0019（建議同時補登 VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger）  
> 目的：提供「doc_key → latest_artifact」的機器可讀映射，支援工程端自動載入/檢核；本附錄不取代、亦不改寫 DOCUMENT_INDEX 既有 Authoritative Index 表格（其仍為唯一裁決來源）。

---

## D1. 使用規則（Hard Rules）

1) 本附錄僅提供 **載入與工具鏈** 使用之 machine-readable mapping：  
   - 不取代 DOCUMENT_INDEX 既有 Authoritative Index 表格  
   - 不改變 ACTIVE、治理等級、覆蓋規則、衝突裁決程序  
2) 若本附錄與 Authoritative Index 表格不一致：  
   - 以 Authoritative Index 表格為準  
   - 工具鏈應回報差異並停機/退回（保守處置）  
3) 若 repo 最終落盤檔名與本附錄不同：  
   - 以 repo 落盤為準  
   - 但本附錄不得刪除；需以 Only-Add 追加更正映射（append-only）

---

## D2. YAML（machine-readable）

```yaml
schema_version: 1
generated_date: 2025-12-28
batch_id: BATCH-20251227-ADDENDUM-PACK-01B
latest_mapping:
  - doc_key: AI_GOV
    latest_artifact: "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜Snapshot 不裁決／Index Gate／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0014
  - doc_key: DOCUMENT_INDEX
    latest_artifact: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228_FINAL.md"
    change_summary: "Only-Add｜批次輸出映射表（本次收斂）"
    fix_id: VA-METADATA_FIX-20251227-0018
  - doc_key: MASTER_ARCH
    latest_artifact: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜Snapshot 不裁決／S・B+・C+ 標籤回歸"
    fix_id: VA-METADATA_FIX-20251227-0015
  - doc_key: MASTER_CANON
    latest_artifact: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜治理口徑補強（S=Label 等）"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: FULL_ARCH
    latest_artifact: "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜DATA_UNIVERSE alias 封口／引用回歸"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: ARCH_FLOW
    latest_artifact: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜口徑對齊與引用模板"
    fix_id: VA-METADATA_FIX-20251227-0003
  - doc_key: GOVERNANCE_GATE_SPEC
    latest_artifact: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜裁決字串助記化／歧義消解"
    fix_id: VA-METADATA_FIX-20251227-0002
  - doc_key: RISK_COMPLIANCE
    latest_artifact: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜S=Label 對齊／引用口徑修補"
    fix_id: VA-METADATA_FIX-20251227-0008
  - doc_key: EXECUTION_CONTROL
    latest_artifact: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜S=Label 對齊／引用口徑修補"
    fix_id: VA-METADATA_FIX-20251227-0002
  - doc_key: LOCAL_ENV
    latest_artifact: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜Evidence Chain／引用模板"
    fix_id: VA-METADATA_FIX-20251227-0004
  - doc_key: DEPLOY_OPS
    latest_artifact: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜Deploy/Ops 證據鏈最小欄位／對齊 LOCAL_ENV"
    fix_id: VA-METADATA_FIX-20251227-0012
  - doc_key: UI_SPEC
    latest_artifact: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜UI Trace 最小引用欄位／Index Gate"
    fix_id: VA-METADATA_FIX-20251227-0011
  - doc_key: VERSION_AUDIT
    latest_artifact: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228_FINAL.md"
    change_summary: "Only-Add｜METADATA_FIX Ledger 收斂補登（2025-12-28）"
    fix_id: VA-METADATA_FIX-20251227-0010
  - doc_key: DATA_SOURCES
    latest_artifact: "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_1_FINAL.md"
    change_summary: "Only-Add｜Addendum 0/0.1（DATA_UNIVERSE=alias／引用回歸）"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: TWSE_RULES
    latest_artifact: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜引用口徑一致化"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: STRATEGY_UNIVERSE
    latest_artifact: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜DATA_UNIVERSE alias 封口／引用回歸 DATA_SOURCES"
    fix_id: VA-METADATA_FIX-20251227-0006
  - doc_key: STRATEGY_FEATURE_INDEX
    latest_artifact: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜B+ Sub-Label（bucket=B）對齊／引用模板"
    fix_id: VA-METADATA_FIX-20251227-0009
  - doc_key: PROJECT_PROMPT
    latest_artifact: "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜Index Gate First／ACTIVE 不固化／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0007
  - doc_key: README
    latest_artifact: "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜文件清單/數量快照化／Index Gate"
    fix_id: VA-METADATA_FIX-20251227-0010
  - doc_key: BEGINNER_GUIDE
    latest_artifact: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜新手入口快照化／Index Gate／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0013
  - doc_key: GOVERNANCE_STATE
    latest_artifact: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜狀態檔快照化／Index Gate／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0016
  - doc_key: PROCESS_ANCHOR
    latest_artifact: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md"
    change_summary: "Only-Add｜定錨入口快照化／Index Gate／工程引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0017
```

---

## D3. JSON（machine-readable）

```json
{
  "schema_version": 1,
  "generated_date": "2025-12-28",
  "batch_id": "BATCH-20251227-ADDENDUM-PACK-01B",
  "latest_mapping": [
    {
      "doc_key": "AI_GOV",
      "latest_artifact": "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜Snapshot 不裁決／Index Gate／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0014"
    },
    {
      "doc_key": "DOCUMENT_INDEX",
      "latest_artifact": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228_FINAL.md",
      "change_summary": "Only-Add｜批次輸出映射表（本次收斂）",
      "fix_id": "VA-METADATA_FIX-20251227-0018"
    },
    {
      "doc_key": "MASTER_ARCH",
      "latest_artifact": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜Snapshot 不裁決／S・B+・C+ 標籤回歸",
      "fix_id": "VA-METADATA_FIX-20251227-0015"
    },
    {
      "doc_key": "MASTER_CANON",
      "latest_artifact": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜治理口徑補強（S=Label 等）",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "FULL_ARCH",
      "latest_artifact": "TAITS_全系統架構總覽（FULL_ARCH）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜DATA_UNIVERSE alias 封口／引用回歸",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "ARCH_FLOW",
      "latest_artifact": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜口徑對齊與引用模板",
      "fix_id": "VA-METADATA_FIX-20251227-0003"
    },
    {
      "doc_key": "GOVERNANCE_GATE_SPEC",
      "latest_artifact": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜裁決字串助記化／歧義消解",
      "fix_id": "VA-METADATA_FIX-20251227-0002"
    },
    {
      "doc_key": "RISK_COMPLIANCE",
      "latest_artifact": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜S=Label 對齊／引用口徑修補",
      "fix_id": "VA-METADATA_FIX-20251227-0008"
    },
    {
      "doc_key": "EXECUTION_CONTROL",
      "latest_artifact": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜S=Label 對齊／引用口徑修補",
      "fix_id": "VA-METADATA_FIX-20251227-0002"
    },
    {
      "doc_key": "LOCAL_ENV",
      "latest_artifact": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜Evidence Chain／引用模板",
      "fix_id": "VA-METADATA_FIX-20251227-0004"
    },
    {
      "doc_key": "DEPLOY_OPS",
      "latest_artifact": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜Deploy/Ops 證據鏈最小欄位／對齊 LOCAL_ENV",
      "fix_id": "VA-METADATA_FIX-20251227-0012"
    },
    {
      "doc_key": "UI_SPEC",
      "latest_artifact": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜UI Trace 最小引用欄位／Index Gate",
      "fix_id": "VA-METADATA_FIX-20251227-0011"
    },
    {
      "doc_key": "VERSION_AUDIT",
      "latest_artifact": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228_FINAL.md",
      "change_summary": "Only-Add｜METADATA_FIX Ledger 收斂補登（2025-12-28）",
      "fix_id": "VA-METADATA_FIX-20251227-0010"
    },
    {
      "doc_key": "DATA_SOURCES",
      "latest_artifact": "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_1_FINAL.md",
      "change_summary": "Only-Add｜Addendum 0/0.1（DATA_UNIVERSE=alias／引用回歸）",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "TWSE_RULES",
      "latest_artifact": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜引用口徑一致化",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "STRATEGY_UNIVERSE",
      "latest_artifact": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜DATA_UNIVERSE alias 封口／引用回歸 DATA_SOURCES",
      "fix_id": "VA-METADATA_FIX-20251227-0006"
    },
    {
      "doc_key": "STRATEGY_FEATURE_INDEX",
      "latest_artifact": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜B+ Sub-Label（bucket=B）對齊／引用模板",
      "fix_id": "VA-METADATA_FIX-20251227-0009"
    },
    {
      "doc_key": "PROJECT_PROMPT",
      "latest_artifact": "TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜Index Gate First／ACTIVE 不固化／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0007"
    },
    {
      "doc_key": "README",
      "latest_artifact": "TAITS_專案總覽與使用說明（README）__251220__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜文件清單/數量快照化／Index Gate",
      "fix_id": "VA-METADATA_FIX-20251227-0010"
    },
    {
      "doc_key": "BEGINNER_GUIDE",
      "latest_artifact": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜新手入口快照化／Index Gate／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0013"
    },
    {
      "doc_key": "GOVERNANCE_STATE",
      "latest_artifact": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜狀態檔快照化／Index Gate／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0016"
    },
    {
      "doc_key": "PROCESS_ANCHOR",
      "latest_artifact": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__ADDENDUM_20251227_FINAL.md",
      "change_summary": "Only-Add｜定錨入口快照化／Index Gate／工程引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0017"
    }
  ]
}
```

---

（Addendum 2025-12-28-D｜Only-Add｜Freeze v1.0 完）

---

# Addendum 2025-12-28-F｜Only-Add：Latest Mapping Override Patch（收斂修正版）× Freeze v1.0（Index Gate 載入一致化最終）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 稽核對位：VERSION_AUDIT:VA-METADATA_FIX-20251227-0022（對應 VERSION_AUDIT｜Addendum 2025-12-28-C｜METADATA_FIX:0022）  
> 目的：針對 2025-12-28 期間多版本並存（mapping D + override patch E/others）所造成的 latest 指向歧義，以 append-only 方式追加「收斂修正版 override patch」，確保工具鏈與人工載入在 Freeze v1.0 期間使用同一組 latest 指向（尤其：DOCUMENT_INDEX、DEPLOY_OPS、VERSION_AUDIT）。

---

## F1. 覆寫規則（Hard Rules）

1) 本 patch 僅覆寫「latest_artifact」指向，不改變 Authoritative Index 表格之治理裁決。  
2) 工具鏈套用順序（固定）：  
   - ① Authoritative Index 表格（裁決）  
   - ② Mapping（Addendum C/D 等）（參考）  
   - ③ Override Patch（本 Addendum F）（最後套用，收斂 latest 指向）  
3) 若 repo 最終落盤檔名與本 patch 不一致：以 repo 落盤為準，並以 Only-Add 追加下一版 patch（append-only）。  

---

## F2. Override Table（Human-readable）

| doc_key | latest_artifact_filename | change_summary | audit_anchor_fix_id |
|---|---|---|---|
| `DOCUMENT_INDEX` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228F_FINAL.md` | Only-Add｜Latest Mapping（YAML/JSON）+ Override Patch（收斂修正版）已納入；本檔即為 latest | `VA-METADATA_FIX-20251227-0022` |
| `DEPLOY_OPS` | `TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md` | Only-Add｜Trace ID / Evidence Chain 欄位貫穿規範已納入（2025-12-28） | `VA-METADATA_FIX-20251227-0020` |
| `VERSION_AUDIT` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228C_FINAL.md` | Only-Add｜Ledger 補登（0021/0022/0023）延伸批次（2025-12-28） | `VA-METADATA_FIX-20251227-0023` |

---

## F3. YAML Override Patch（machine-readable）

```yaml
schema_version: 1
patch_type: latest_mapping_override
patch_date: 2025-12-28
patch_batch_id: BATCH-20251227-ADDENDUM-PACK-01C
override:
  - doc_key: DOCUMENT_INDEX
    latest_artifact: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228F_FINAL.md"
    change_summary: "Only-Add｜Latest Mapping（YAML/JSON）+ Override Patch（收斂修正版）已納入；本檔即為 latest"
    fix_id: VA-METADATA_FIX-20251227-0022
  - doc_key: DEPLOY_OPS
    latest_artifact: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md"
    change_summary: "Only-Add｜Trace ID / Evidence Chain 欄位貫穿規範已納入（2025-12-28）"
    fix_id: VA-METADATA_FIX-20251227-0020
  - doc_key: VERSION_AUDIT
    latest_artifact: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228C_FINAL.md"
    change_summary: "Only-Add｜Ledger 補登（0021/0022/0023）延伸批次（2025-12-28）"
    fix_id: VA-METADATA_FIX-20251227-0023
```

---

## F4. JSON Override Patch（machine-readable）

```json
{
  "schema_version": 1,
  "patch_type": "latest_mapping_override",
  "patch_date": "2025-12-28",
  "patch_batch_id": "BATCH-20251227-ADDENDUM-PACK-01C",
  "override": [
    {
      "doc_key": "DOCUMENT_INDEX",
      "latest_artifact": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228F_FINAL.md",
      "change_summary": "Only-Add｜Latest Mapping（YAML/JSON）+ Override Patch（收斂修正版）已納入；本檔即為 latest",
      "fix_id": "VA-METADATA_FIX-20251227-0022"
    },
    {
      "doc_key": "DEPLOY_OPS",
      "latest_artifact": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md",
      "change_summary": "Only-Add｜Trace ID / Evidence Chain 欄位貫穿規範已納入（2025-12-28）",
      "fix_id": "VA-METADATA_FIX-20251227-0020"
    },
    {
      "doc_key": "VERSION_AUDIT",
      "latest_artifact": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228C_FINAL.md",
      "change_summary": "Only-Add｜Ledger 補登（0021/0022/0023）延伸批次（2025-12-28）",
      "fix_id": "VA-METADATA_FIX-20251227-0023"
    }
  ]
}
```

---

（Addendum 2025-12-28-F｜Only-Add｜Freeze v1.0 完）
---

# Addendum 2025-12-28｜Only-Add：P0 全閉合（GOVERNANCE_STATE doc_key 正名 × Mapping Delta Patch｜Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
> 稽核對位：VERSION_AUDIT｜建議新增條目：`VA-METADATA_FIX-20251228-0031`  
> 目的：閉合「狀態檔 doc_key 正名」與「machine-readable mapping 仍保留 GOVERNANCE_STATE 作 doc_key」的歧義；以 Only-Add 方式追加後序優先的 Override Patch（Delta），使工具鏈與人工引用一致。

---

## H1. GOVERNANCE_STATE 正名裁決（Hard）

- 權威 doc_key：`GOVERNANCE_STATE_FREEZE_V1`
- `GOVERNANCE_STATE` 僅允許作為：
  - 文件自然語言名稱／助記（Mnemonic）
  - 查找關鍵字／UI 顯示別名（alias）
- `GOVERNANCE_STATE` **不得**作為：
  - `doc_key`
  - 任何引用鍵（`ref_doc_key` / `gate_doc_key` / `audit_doc_key` / `evidence_doc_key`）

---

## H2. Mapping Override Patch（後序優先｜Only-Add｜Delta）

> 規則：本區塊為後序優先的 Override Patch；若同一文件中存在多個 mapping 區塊，工具鏈必須以標記為 Override Patch 且日期較新者為準。

### H2.1 YAML（delta）

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
      change_summary: "Only-Add｜P0 全閉合：引用模板作廢＋新模板固定＋alias 封口（不改原文）"
      fix_id: "VA-METADATA_FIX-20251228-0031"
```

### H2.2 JSON（delta）

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
        "change_summary": "Only-Add｜P0 全閉合：引用模板作廢＋新模板固定＋alias 封口（不改原文）",
        "fix_id": "VA-METADATA_FIX-20251228-0031"
      }
    ]
  }
}
```

---

## H3. 引用端硬規則（P0 Re-Assert）

- doc_key 的唯一真相：`DOCUMENT_INDEX` Authoritative Index（含 Override Patch）。  
- 當「文件自述」與「Index 裁決」不一致：
  - 一律以 Index 裁決為準  
  - 自述視為 Metadata Discrepancy（不得被工具鏈提升為 doc_key）

---

## H4. 版本戳記
- generated_at: 2025-12-28 02:30:24 +0800（Asia/Taipei）

（Addendum 2025-12-28｜Only-Add｜DOCUMENT_INDEX｜P0 全閉合 完）
---

# Addendum 2025-12-28｜Only-Add：Mapping Normalization（Legacy doc_key 降格 × Tooling 映射收斂｜Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
> 稽核對位：VERSION_AUDIT｜新增條目：`VA-METADATA_FIX-20251228-0034`  
> 目的：在不刪除既有 machine-readable mapping（append-only）的前提下，追加一份「Normalization Patch」使工具鏈不再被 legacy doc_key 誤導；並收斂至 Index Gate（含 Override Patch）的一致解析口徑。

---

## J1. Mapping Precedence（Hard｜工具鏈採用順序）

若同一文件內存在多份 machine-readable mapping（YAML/JSON）：
1) 先選擇 `schema_version` 最大者  
2) 若 `schema_version` 相同，選擇 `generated_date` 較新者  
3) 若仍衝突，以「明確標記為 normalization_patch / override_patch」者優先  
4) 若無法裁決，視為不合規載入（不得進入 Gate/Audit/Replay）

---

## J2. Normalization Patch（schema_version: 2｜YAML）

```yaml
schema_version: 2
generated_date: 2025-12-28
batch_id: BATCH-20251228-P1-NORMALIZATION
normalization_patch:
  patch_id: "DOCUMENT_INDEX-NORMALIZATION-PATCH-2025-12-28-J"
  authoritative_source: "DOCUMENT_INDEX"
  rules:
    - legacy_doc_key: "GOVERNANCE_STATE"
      resolve_to_doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      note: "正名封口：GOVERNANCE_STATE 僅為 alias；唯一合法 doc_key 為 GOVERNANCE_STATE_FREEZE_V1"
    - legacy_doc_key: "DATA_UNIVERSE"
      resolve_to_doc_key: "DATA_SOURCES"
      note: "Alias 封口：DATA_UNIVERSE 僅為概念標籤；法律承載文件為 DATA_SOURCES"
  deprecated_doc_keys:
    - "GOVERNANCE_STATE"
    - "DATA_UNIVERSE"
  latest_mapping_v2:
    - doc_key: "DOCUMENT_INDEX"
      latest_artifact: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228J_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0034"
    - doc_key: "AI_GOV"
      latest_artifact: "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0029"
    - doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      latest_artifact: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228H_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0030"
    - doc_key: "VERSION_AUDIT"
      latest_artifact: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228J_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0034"
    - doc_key: "DATA_SOURCES"
      latest_artifact: "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md"
      fix_id: "VA-METADATA_FIX-20251228-0033"
```

---

## J3. Normalization Patch（schema_version: 2｜JSON）

```json
{
  "schema_version": 2,
  "generated_date": "2025-12-28",
  "batch_id": "BATCH-20251228-P1-NORMALIZATION",
  "normalization_patch": {
    "patch_id": "DOCUMENT_INDEX-NORMALIZATION-PATCH-2025-12-28-J",
    "authoritative_source": "DOCUMENT_INDEX",
    "rules": [
      {
        "legacy_doc_key": "GOVERNANCE_STATE",
        "resolve_to_doc_key": "GOVERNANCE_STATE_FREEZE_V1",
        "note": "正名封口：GOVERNANCE_STATE 僅為 alias；唯一合法 doc_key 為 GOVERNANCE_STATE_FREEZE_V1"
      },
      {
        "legacy_doc_key": "DATA_UNIVERSE",
        "resolve_to_doc_key": "DATA_SOURCES",
        "note": "Alias 封口：DATA_UNIVERSE 僅為概念標籤；法律承載文件為 DATA_SOURCES"
      }
    ],
    "deprecated_doc_keys": ["GOVERNANCE_STATE", "DATA_UNIVERSE"],
    "latest_mapping_v2": [
      {
        "doc_key": "DOCUMENT_INDEX",
        "latest_artifact": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228J_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0034"
      },
      {
        "doc_key": "AI_GOV",
        "latest_artifact": "TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0029"
      },
      {
        "doc_key": "GOVERNANCE_STATE_FREEZE_V1",
        "latest_artifact": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220__ADDENDUM_20251228H_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0030"
      },
      {
        "doc_key": "VERSION_AUDIT",
        "latest_artifact": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219__ADDENDUM_20251228J_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0034"
      },
      {
        "doc_key": "DATA_SOURCES",
        "latest_artifact": "TAITS_資料來源全集（DATA_SOURCES）__251219__ADDENDUM_0_2C_FINAL.md",
        "fix_id": "VA-METADATA_FIX-20251228-0033"
      }
    ]
  }
}
```

---

## J4. 版本戳記
- generated_at: 2025-12-28 02:48:55 +0800（Asia/Taipei）

（Addendum 2025-12-28｜Only-Add｜DOCUMENT_INDEX｜Mapping Normalization 完）
---

# Addendum 2025-12-28｜Only-Add：v2 Mapping Completeness（latest_mapping_v2 全量補齊｜Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
> 稽核對位：VERSION_AUDIT｜新增條目：`VA-METADATA_FIX-20251228-0036`  
> 目的：補齊 `schema_version = 2` 之 `latest_mapping_v2` 覆蓋範圍，避免工具鏈因採用較新 schema 而「看不到」部分 doc_key；本補丁為 append-only（後序優先），不移除任何既有 mapping。

---

## K1. 適用範圍（Hard）
- 本 Addendum 定義之 `latest_mapping_v2_full`：
  - 覆蓋 **DOCUMENT_INDEX Authoritative Index 表格列為 ACTIVE** 之全部 doc_key  
  - 並額外補登：`PROJECT_PROMPT`、`PROCESS_ANCHOR`（入口與工程定錨）
- 若工具鏈採用 `schema_version = 2`，且遇到同級多份 v2 mapping：
  - 以本 Addendum（日期較新、明確標記 completeness_patch）為準

---

## K2. Completeness Patch（schema_version: 2｜YAML）

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

---

## K3. Completeness Patch（schema_version: 2｜JSON）

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

---

## K4. 版本戳記
- generated_at: 2025-12-28 02:56:19 +0800（Asia/Taipei）

（Addendum 2025-12-28｜Only-Add｜DOCUMENT_INDEX｜v2 Mapping Completeness 完）
---

# Addendum 2025-12-28｜Only-Add：ACTIVE 對齊修補 × Canonical Bundle（schema_version=3）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
> 稽核對位：VERSION_AUDIT｜新增條目：`VA-METADATA_FIX-20251228-0039`、`VA-METADATA_FIX-20251228-0040`  
> 目的：  
> 1) 修補「PROJECT_PROMPT 自述 ACTIVE」但未列入 Authoritative Index ACTIVE 表格的治理不一致；以 Only-Add 追加 ACTIVE 補登（不改原表）。  
> 2) 提供單一可載入的 **Canonical Bundle（schema_version=3）**，整合 legacy 解析規則＋完整 latest mapping，避免多補丁選擇/合併歧義。

---

## L1. Authoritative Index｜ACTIVE 補登（Only-Add Amendment）

- 自本 Addendum 起，`PROJECT_PROMPT` 視為 **ACTIVE**（與文件自述之 ACTIVE 一致），並納入「可用於 Freeze v1.0 下的新對話啟動與治理對齊」之入口治理文件集合。
- 本補登為 append-only：不改寫既有表格；工具鏈與人工查核時，**Authoritative Index = 原表 + 本 Amendment（日期較新者優先）**。

### L1.1 Amendment Row（最小欄位）

| 文件名稱 | doc_key | 治理等級 | 狀態 | 備註 |
|---|---|---|---|---|
| TAITS_PROJECT_PROMPT__ADDENDUM_20251227_FINAL.md | PROJECT_PROMPT | B（Project Prompt & Operating Contract） | ACTIVE | 入口治理契約；裁決仍回歸 DOCUMENT_INDEX / MASTER_ARCH / MASTER_CANON；僅供新對話啟動與對齊 |

---

## L2. Canonical Bundle（schema_version = 3）— Single Loadable Source

> 原則：工具鏈若支援 schema_version 選擇，一律優先採用 **schema_version 最大者**。  
> 自本 Addendum 起，建議工具鏈以本束作為「單一載入入口」，以避免 v2 多補丁（override/normalization/completeness）之選擇與合併歧義。

### L2.1 YAML

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

### L2.2 JSON

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

---

## L3. 版本戳記
- generated_at: 2025-12-28 03:02:28 +0800（Asia/Taipei）

（Addendum 2025-12-28｜Only-Add｜DOCUMENT_INDEX｜ACTIVE 對齊修補 × Canonical Bundle 完）
---

# Addendum 2025-12-28｜Only-Add：Copy-Safe DocKey List（人因防呆：完整鍵清單 × 表格省略禁用｜Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
> 稽核對位：VERSION_AUDIT｜新增條目：`VA-METADATA_FIX-20251228-0042`  
> 目的：消除「人類複製貼上」誤用 doc_key 的主要來源（表格顯示省略 `…`）；提供一份可直接複製、零省略、零歧義的 doc_key 清單。  
> 補充說明：本 Addendum 不改寫任何既有表格／既有 mapping；僅提供人因防呆的 Copy-Safe 版本與硬規則。

---

## M1. HARD RULE（表格省略不得作為引用鍵）

- 任何表格/展示型欄位若以 `…`、截斷、換行折疊、UI 省略呈現 doc_key：
  - 一律不得作為 `ref_doc_key` / `doc_key` / `gate_doc_key` / `audit_doc_key` 等引用鍵值
- 引用鍵值必須取自：
  1) 本文件之 **Canonical Bundle（schema_version=3）**；或  
  2) 本 Addendum 之 **Copy-Safe DocKey List**（完整鍵清單）

---

## M2. Copy-Safe DocKey List（完整鍵清單｜可直接複製）

> 下列清單為「完整 doc_key 原字串」；不得增減字元、不得自行改寫大小寫、不得加空白。

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

---

## M3. 版本戳記
- generated_at: 2025-12-28 03:09:05 +0800（Asia/Taipei）

（Addendum 2025-12-28｜Only-Add｜DOCUMENT_INDEX｜Copy-Safe DocKey List 完）
