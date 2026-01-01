# HUMAN SOVEREIGNTY｜最高裁決置頂條款（Top-of-File）


## 全局定錨｜單一口徑（S1）

### 1. 人類最高決策者主權（SOVEREIGNTY）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接，不得卡死更新。

### 2. L9–L11 最終語義（跨文件一致）
- L9（投資報告層）：可追蹤、可更新、可標的化投資報告；必含數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源），並支援事件驅動滾動更新。
- L10（人類裁決層）：由人類最高決策者裁決不動作/回測/模擬/半自動/全自動等；任何交易型態皆以 L10 明確裁決為準。
- L11（工程稽核回放層）：對 L1–L11 全層輸入/處理/輸出/裁決/執行鏈路留痕，供人類與工程端可讀、可查、可回放；L11 非下單決策層。

### 3. HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：Freeze/Only-Add/Gate 不得阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。

生效日：2025-12-29（Asia/Taipei）  
裁決：**人類最高決策者擁有最終裁決權**；任何治理文件、流程條款、Gate/Token/Reason Code、任何 Agent/AI 內規，**不得否決或阻止**人類最高決策者的明確命令。  
文件與流程之角色：提供「可回放／可稽核／可追溯」之制度化表述；不得作為限制器。  
無明確人類命令時：系統依既有治理裁決序位與當前狀態（Freeze v1.0）運作。  

---

# TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260101.md
doc_key：DOCUMENT_INDEX  
治理等級：A+（Document Governance Resolution Canon｜文件位階裁決最高層）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（Index 為裁決依據；Only-Add 演進）  
版本日期：2026-01-01  
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

**文件沒被 Index 收錄＝系統不承認。**

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

等級不是「重要性」主觀評分；等級是「發生衝突時誰能裁決誰」。

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

本表為「治理有效」文件全集。  
**不在表內＝不具治理效力。**  
本表只增不減（Only-Add）；新增/改狀態必須可稽核（VERSION_AUDIT）。

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

註：未來若新增 UNFREEZE 文件，必須同樣納入本表，並遵守 ACTIVE 唯一性（同類 doc_key 規則）。

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

註：LOCAL_ENV 若被定義為 B 或 C，須以 A/A+ 上位文件裁決；本 Index 現階段僅「收錄與引用裁決」，不擅自改寫其治理定位。

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

本節提供「最低約束」，實際更細規則以 A+ / MASTER_ARCH / 各規格文件裁決。

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

## 治理補強（已整合為正文）

對位母法：MASTER_CANON（Canonical Flow L1–L11）  

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

核心一句話：  
**DOCUMENT_INDEX 決定「誰有資格說話、哪份文件有權力被引用」。**

---

### A.2.2 MASTER_CANON —「層級語義」與「Canonical Flow」的最高母法

MASTER_CANON 的職責是裁決「系統如何運作」：

1) Canonical Flow（L1–L11）的存在性、邊界與不可越權原則  
2) 各層的輸入/輸出契約、稽核要求、回放一致性（Replay）  
3) 角色分工（人類/AI/系統）在流程中如何定位  
4) 跨層互鎖（Regime/Risk/Compliance/Execution/UI）的流程語義

核心一句話：  
**MASTER_CANON 決定「該怎麼走流程、什麼叫合規的層級行為」。**

---

### A.2.3 一句話界線（Hard Boundary）

- **DOCUMENT_INDEX 管「文件是否合法、是否可引用、誰覆蓋誰」。**  
- **MASTER_CANON 管「流程怎麼走、層級語義如何解讀、越權如何判定」。**

兩者互補，不互相替代。

---

## A.3 與 MASTER_CANON 的「對位使用規則」（避免誤用）

本節不改寫既有「衝突裁決程序」，只把操作順序固化成可讀規則。

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

重點：  
DOCUMENT_INDEX 不替代 MASTER_CANON 的流程語義；MASTER_CANON 不替代 DOCUMENT_INDEX 的可引用性裁決。

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

目的：  
確保「等級」永遠可稽核、可回放、不可被改名或誤標而繞過治理。

---

## A.5 FILE UPDATE MODE 下新增文件進入 Index 的「固定模板」（Only-Add）

本節提供「新增條目」的固定寫法，用於未來擴充文件宇宙；  
不改寫既有規則，只降低錯誤率。

### A.5.1 新增治理文件條目（Index Entry Template）

- 文件名稱：`<filename>`  
- doc_key：`<DOC_KEY>`  
- 治理等級：`A+ / A / B / C`  
- 版本狀態：`ACTIVE / ARCHIVED / DEPRECATED / DRAFT`  
- 版本日期：`YYYY-MM-DD`  
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

---

## 治理補強（已整合為正文）

裁決位階：不高於 DOCUMENT_INDEX 正文；僅作補齊、對齊、指引用途  

## 0.1 本附錄存在理由（不可省略）

DOCUMENT_INDEX 作為 **A+ 文件位階裁決母表**，  

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

若附錄與正文產生任何張力或歧義：  
**一律以正文為準，附錄自動失效，不需宣告。**

---

## 治理補強（已整合為正文）

目的：讓「哪些附錄存在、附錄屬於誰、可否引用」可被一次性裁決

## I.1 附錄存在即須被索引（Hard Rule）

- **任何附錄若未被本表收錄**
  - 視為：不存在
  - 不得被引用
  - 不得作為治理、裁決、稽核依據

## I.2 DOCUMENT_INDEX 專屬附錄清單

|---|---|---|---|---|

註：  
- 本表只增不減（Only-Add）  

---

## 治理補強（已整合為正文）

對位母法：MASTER_CANON（Canonical Flow L1–L11）

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

## 治理補強（已整合為正文）

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

## 治理補強（已整合為正文）

## C.1 Freeze 期間允許（Index 層）

- 新增附錄（Only-Add）  
- 新增文件條目（不改裁決序位）  
- 補齊索引、對位、引用指引  

## C.2 Freeze 期間禁止（Index 層）

- 改寫裁決順位  
- 改寫治理等級  
- 改寫 Canonical Flow 的解讀權  

判斷原則（不可模糊）：  
**若行為可能影響「誰能裁決誰」→ 一律視為結構性變更 → Freeze 下禁止。**

---

（Only-Add｜DOCUMENT_INDEX 附錄補齊 · 第 1 批 完）

---

## 治理補強（已整合為正文）

對位文件：TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md（doc_key：VERSION_AUDIT）  
裁決位階：不高於 DOCUMENT_INDEX 正文；僅補齊「Index 變更必可稽核」之落地對位口徑

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

本節不改寫正文第 9 章（Index Change Ledger），僅把可稽核類型「枚舉化」以防漏報。

以下行為一律視為「Index 變更」，必須在 VERSION_AUDIT 留存：

### D.2.1 ADD_ENTRY（新增治理文件條目）
- 新增任何「治理有效文件清單」之新列（任意等級 A+/A/B/C）

### D.2.2 STATUS_CHANGE（版本狀態變更）
- 任一 doc_key 的 `版本狀態` 變更（例如：ACTIVE → ARCHIVED / DEPRECATED / DRAFT）

### D.2.3 METADATA_FIX（中繼資料修補）
- 修補 doc header / Index 表格之 metadata 不一致（僅能以新增說明方式修補，不得覆寫原值）
- 例：治理等級標示不一致、檔名日期與版本日期對齊說明等

### D.2.4 APPENDIX_ADD（新增附錄）

### D.2.5 REFERENCE_EXPAND（平行參照擴充）
- 僅新增「平行參照」或「引用指引」之條目（不得引入新裁決權）

---

## D.3 VERSION_AUDIT 最小必填欄位（Hard Minimum）

對於上述任一變更類型，VERSION_AUDIT 至少必須包含：

- `change_id`（全域唯一）
- `change_time`（生效時間戳）
- `doc_key=DOCUMENT_INDEX`
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

## 治理補強（已整合為正文）

對位文件：TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md（doc_key：GOVERNANCE_GATE_SPEC）  
目的：把「文件合法性裁決（Index）」與「治理閘門裁決（L9 Gate）」的關係鎖定為單一路徑

---

## E.1 核心一句話（不可省略）

- DOCUMENT_INDEX：裁決「文件是否可被引用」  
- GOVERNANCE_GATE_SPEC：裁決「一次輸出/一次提案是否符合治理門檻」

兩者關係必須是：  
**先 Index Gate，再 Governance Gate；不得反向、不得跳步。**

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

## 治理補強（已整合為正文）

目的：避免新增文件條目時產生「隱性權力」或「狀態歧義」

---

## F.1 Index Entry（治理有效文件條目）標準模板

本模板僅用於「新增條目」；不得用於覆寫既有條目。

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

注意：本節僅「固定詞彙」，不新增任何上位文件未授權之裁決權。

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

## 治理補強（已整合為正文）

目的：防止附錄編號混亂、重複、或被用來「變相改寫正文」

---

## G.1 附錄類型詞彙（Vocabulary）

- **Guideline**：指引（操作性說明；不得作裁決依據）  
- **Annotation**：註解（非約束性；不得參與裁決鏈）

---

## G.2 掛載位置硬規則（Hard Placement Rule）

- 不得插入正文中段（避免造成「重排/改寫」之誤讀）  
- 不得以附錄形式對正文做「替代性描述」  
  - 若附錄與正文產生張力：附錄自動失效

---

## 治理補強（已整合為正文）

  → 否則該附錄治理上視為不存在

---

（Only-Add｜DOCUMENT_INDEX 附錄補齊 · 第 2 批 完）

---

## 治理補強（已整合為正文）

依據正文：§1（Hard Laws）／§3（治理等級與裁決力）／§6（文件衝突裁決程序）／§7（引用合法性）／§9（Index Change Ledger）  
目的：統一跨文件常見之「裁決順序字串」解讀口徑，避免字串被誤當成覆蓋規則；並將「Metadata Discrepancy（中繼資料差異）」之處置方式固定為可回放、可稽核之單一路徑。

---

## 0. 適用範圍與不適用範圍（Hard Boundary）

### 0.1 適用

1) **「裁決順序字串」的誤讀**  
   例如：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`、`DOCUMENT_INDEX → MASTER_ARCH → AI_GOV`、或其他以箭頭呈現之排序描述。

2) **Metadata Discrepancy（中繼資料差異）的處置**  
   例如：Index 表格與文件檔頭（doc header）之 `doc_key / 治理等級 / 版本狀態 / 檔名標示 / 概念別名` 不一致。

### 0.2 不適用（禁止越權）

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

若任何裁決順序字串與正文 §6（衝突裁決程序）或正文 §3（A+ > A > B > C）產生張力：  
**一律以正文 §6／§3 為準，該字串僅作助記，且在該張力範圍內不具裁決力。**

### 1.2 統一解讀：所有衝突裁決必須回到 §6（不可跳步）
跨文件一切衝突裁決，必須依正文 §6 的固定步驟（不可跳步）：

1) **Index Gate**：先確認是否收錄於 Index、且為該 doc_key 唯一 ACTIVE（未收錄＝無效／非 ACTIVE＝不得引用）。  
2) **治理等級覆蓋**：套用 §3 的 A+ > A > B > C。  
3) **同級衝突**：依正文 §6 的規則，往更上位約束文件裁決；仍無法裁決則保守禁止（STOP）。  
4) **稽核留痕**：必須在 VERSION_AUDIT 留存裁決紀錄（正文 §1.5／§6／§9）。

---

## 2. FILE UPDATE MODE 下「唯一可採用」的統一裁決口徑（可貼用字串）

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

注意：上述「Domain Canon」僅是「在通過 Index Gate 並套用覆蓋規則後」的領域選用提示；  
**其存在不改寫覆蓋規則本身。**

### 2.2 舊字串的統一解釋（兼容既有文件，不改原文）

- **字串 A：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`**  
  解釋：表示「先驗證文件合法性（Index Gate），再受憲法邊界約束（MASTER_ARCH），再以流程語義解讀（MASTER_CANON）」；  
  **不表示** AI_GOV 失去 A+ 覆蓋地位；若議題涉及 AI 行為／AI 參與裁決邊界，仍以 AI_GOV（A+）為最高約束。

- **字串 B：`DOCUMENT_INDEX → MASTER_ARCH → AI_GOV`**  
  解釋：表示「先驗證文件合法性（Index Gate），再受憲法邊界約束（MASTER_ARCH），並特別提醒 AI 行為仍受 AI_GOV 約束」；  
  **不表示** DOCUMENT_INDEX 或 MASTER_ARCH 可覆蓋 AI_GOV；一切覆蓋仍回到 §3／§6。

任何其他以箭頭描述之排序，一律依本節規則視為助記；遇張力回到正文 §6／§3。

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
4) **Index 端必要補強**：若差異會影響跨文件引用（例如 doc_key 誤用風險高），則可在本文件新增「歧義消解附錄」或「已知差異登錄」（只增不減）。

### 3.3 本次已登錄之 METADATA_FIX（可回放）
- 條目：`VA-METADATA_FIX-20251227-0001`  
- 主旨：修補 DATA_SOURCES 文件內「DATA_UNIVERSE（概念名詞）」被誤當 doc_key 之風險，並鎖定引用合法性（doc_key=DATA_SOURCES）。  

---

## 治理補強（已整合為正文）

- 任何裁決仍必須回到：正文 §6（衝突裁決程序）＋正文 §3（A+ > A > B > C）＋正文 §7（引用合法性）＋正文 §1.5（無審計＝未發生）。  

---

## 治理補強（已整合為正文）

上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+｜Authoritative Index）＋MASTER_ARCH（A）＋MASTER_CANON（A）  

---

## C1. 使用規則（Hard Rules）

1) 本映射表為 **操作收斂參考（Operational Mapping）**：  
   - 不取代 DOCUMENT_INDEX 既有 Authoritative Index 表格  
   - 不改變治理等級、覆蓋規則、ACTIVE 判定或衝突裁決程序

2) 任何涉及 ACTIVE/doc_key/治理等級/版本有效性之裁決：  
   - 一律以 DOCUMENT_INDEX 的 Authoritative Index 表格為準（本表僅提供「最新檔名」參考）

3) 若 repo 落盤檔名與本表不同：  
   - 以 repo 落盤為準  

---

## C2. 2025-12-27 批次輸出映射表（doc_key → Latest Artifact）

| doc_key | latest_artifact_filename | change_summary | audit_anchor_fix_id |
|---|---|---|---|

---

---

## 治理補強（已整合為正文）

上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+｜Authoritative Index）＋MASTER_ARCH（A）＋MASTER_CANON（A）  
目的：提供「doc_key → latest_artifact」的機器可讀映射，支援工程端自動載入/檢核；本附錄不取代、亦不改寫 DOCUMENT_INDEX 既有 Authoritative Index 表格（其仍為唯一裁決來源）。

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
latest_mapping:
  - doc_key: AI_GOV
    change_summary: "Only-Add｜Snapshot 不裁決／Index Gate／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0014
  - doc_key: DOCUMENT_INDEX
    change_summary: "Only-Add｜批次輸出映射表（本次收斂）"
    fix_id: VA-METADATA_FIX-20251227-0018
  - doc_key: MASTER_ARCH
    change_summary: "Only-Add｜Snapshot 不裁決／S・B+・C+ 標籤回歸"
    fix_id: VA-METADATA_FIX-20251227-0015
  - doc_key: MASTER_CANON
    change_summary: "Only-Add｜治理口徑補強（S=Label 等）"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: FULL_ARCH
    change_summary: "Only-Add｜DATA_UNIVERSE alias 封口／引用回歸"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: ARCH_FLOW
    change_summary: "Only-Add｜口徑對齊與引用模板"
    fix_id: VA-METADATA_FIX-20251227-0003
  - doc_key: GOVERNANCE_GATE_SPEC
    change_summary: "Only-Add｜裁決字串助記化／歧義消解"
    fix_id: VA-METADATA_FIX-20251227-0002
  - doc_key: RISK_COMPLIANCE
    change_summary: "Only-Add｜S=Label 對齊／引用口徑修補"
    fix_id: VA-METADATA_FIX-20251227-0008
  - doc_key: EXECUTION_CONTROL
    change_summary: "Only-Add｜S=Label 對齊／引用口徑修補"
    fix_id: VA-METADATA_FIX-20251227-0002
  - doc_key: LOCAL_ENV
    change_summary: "Only-Add｜Evidence Chain／引用模板"
    fix_id: VA-METADATA_FIX-20251227-0004
  - doc_key: DEPLOY_OPS
    change_summary: "Only-Add｜Deploy/Ops 證據鏈最小欄位／對齊 LOCAL_ENV"
    fix_id: VA-METADATA_FIX-20251227-0012
  - doc_key: UI_SPEC
    change_summary: "Only-Add｜UI Trace 最小引用欄位／Index Gate"
    fix_id: VA-METADATA_FIX-20251227-0011
  - doc_key: VERSION_AUDIT
    change_summary: "Only-Add｜METADATA_FIX Ledger 收斂補登（2025-12-28）"
    fix_id: VA-METADATA_FIX-20251227-0010
  - doc_key: DATA_SOURCES
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: TWSE_RULES
    change_summary: "Only-Add｜引用口徑一致化"
    fix_id: VA-METADATA_FIX-20251227-0005
  - doc_key: STRATEGY_UNIVERSE
    change_summary: "Only-Add｜DATA_UNIVERSE alias 封口／引用回歸 DATA_SOURCES"
    fix_id: VA-METADATA_FIX-20251227-0006
  - doc_key: STRATEGY_FEATURE_INDEX
    change_summary: "Only-Add｜B+ Sub-Label（bucket=B）對齊／引用模板"
    fix_id: VA-METADATA_FIX-20251227-0009
  - doc_key: PROJECT_PROMPT
    change_summary: "Only-Add｜Index Gate First／ACTIVE 不固化／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0007
  - doc_key: README
    change_summary: "Only-Add｜文件清單/數量快照化／Index Gate"
    fix_id: VA-METADATA_FIX-20251227-0010
  - doc_key: BEGINNER_GUIDE
    change_summary: "Only-Add｜新手入口快照化／Index Gate／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0013
  - doc_key: GOVERNANCE_STATE
    change_summary: "Only-Add｜狀態檔快照化／Index Gate／引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0016
  - doc_key: PROCESS_ANCHOR
    change_summary: "Only-Add｜定錨入口快照化／Index Gate／工程引用最小格式"
    fix_id: VA-METADATA_FIX-20251227-0017
```

---

## D3. JSON（machine-readable）

```json
{
  "schema_version": 1,
  "generated_date": "2025-12-28",
  "latest_mapping": [
    {
      "doc_key": "AI_GOV",
      "change_summary": "Only-Add｜Snapshot 不裁決／Index Gate／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0014"
    },
    {
      "doc_key": "DOCUMENT_INDEX",
      "change_summary": "Only-Add｜批次輸出映射表（本次收斂）",
      "fix_id": "VA-METADATA_FIX-20251227-0018"
    },
    {
      "doc_key": "MASTER_ARCH",
      "change_summary": "Only-Add｜Snapshot 不裁決／S・B+・C+ 標籤回歸",
      "fix_id": "VA-METADATA_FIX-20251227-0015"
    },
    {
      "doc_key": "MASTER_CANON",
      "change_summary": "Only-Add｜治理口徑補強（S=Label 等）",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "FULL_ARCH",
      "change_summary": "Only-Add｜DATA_UNIVERSE alias 封口／引用回歸",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "ARCH_FLOW",
      "change_summary": "Only-Add｜口徑對齊與引用模板",
      "fix_id": "VA-METADATA_FIX-20251227-0003"
    },
    {
      "doc_key": "GOVERNANCE_GATE_SPEC",
      "change_summary": "Only-Add｜裁決字串助記化／歧義消解",
      "fix_id": "VA-METADATA_FIX-20251227-0002"
    },
    {
      "doc_key": "RISK_COMPLIANCE",
      "change_summary": "Only-Add｜S=Label 對齊／引用口徑修補",
      "fix_id": "VA-METADATA_FIX-20251227-0008"
    },
    {
      "doc_key": "EXECUTION_CONTROL",
      "change_summary": "Only-Add｜S=Label 對齊／引用口徑修補",
      "fix_id": "VA-METADATA_FIX-20251227-0002"
    },
    {
      "doc_key": "LOCAL_ENV",
      "change_summary": "Only-Add｜Evidence Chain／引用模板",
      "fix_id": "VA-METADATA_FIX-20251227-0004"
    },
    {
      "doc_key": "DEPLOY_OPS",
      "change_summary": "Only-Add｜Deploy/Ops 證據鏈最小欄位／對齊 LOCAL_ENV",
      "fix_id": "VA-METADATA_FIX-20251227-0012"
    },
    {
      "doc_key": "UI_SPEC",
      "change_summary": "Only-Add｜UI Trace 最小引用欄位／Index Gate",
      "fix_id": "VA-METADATA_FIX-20251227-0011"
    },
    {
      "doc_key": "VERSION_AUDIT",
      "change_summary": "Only-Add｜METADATA_FIX Ledger 收斂補登（2025-12-28）",
      "fix_id": "VA-METADATA_FIX-20251227-0010"
    },
    {
      "doc_key": "DATA_SOURCES",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "TWSE_RULES",
      "change_summary": "Only-Add｜引用口徑一致化",
      "fix_id": "VA-METADATA_FIX-20251227-0005"
    },
    {
      "doc_key": "STRATEGY_UNIVERSE",
      "change_summary": "Only-Add｜DATA_UNIVERSE alias 封口／引用回歸 DATA_SOURCES",
      "fix_id": "VA-METADATA_FIX-20251227-0006"
    },
    {
      "doc_key": "STRATEGY_FEATURE_INDEX",
      "change_summary": "Only-Add｜B+ Sub-Label（bucket=B）對齊／引用模板",
      "fix_id": "VA-METADATA_FIX-20251227-0009"
    },
    {
      "doc_key": "PROJECT_PROMPT",
      "change_summary": "Only-Add｜Index Gate First／ACTIVE 不固化／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0007"
    },
    {
      "doc_key": "README",
      "change_summary": "Only-Add｜文件清單/數量快照化／Index Gate",
      "fix_id": "VA-METADATA_FIX-20251227-0010"
    },
    {
      "doc_key": "BEGINNER_GUIDE",
      "change_summary": "Only-Add｜新手入口快照化／Index Gate／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0013"
    },
    {
      "doc_key": "GOVERNANCE_STATE",
      "change_summary": "Only-Add｜狀態檔快照化／Index Gate／引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0016"
    },
    {
      "doc_key": "PROCESS_ANCHOR",
      "change_summary": "Only-Add｜定錨入口快照化／Index Gate／工程引用最小格式",
      "fix_id": "VA-METADATA_FIX-20251227-0017"
    }
  ]
}
```

---

---

## 治理補強（已整合為正文）

---

## F1. 覆寫規則（Hard Rules）

2) 工具鏈套用順序（固定）：  
   - ① Authoritative Index 表格（裁決）  

---

## F2. Override Table（Human-readable）

| doc_key | latest_artifact_filename | change_summary | audit_anchor_fix_id |
|---|---|---|---|

---

## F3. YAML Override Patch（machine-readable）

```yaml
schema_version: 1
override:
  - doc_key: DOCUMENT_INDEX
    fix_id: VA-METADATA_FIX-20251227-0022
  - doc_key: DEPLOY_OPS
    change_summary: "Only-Add｜Trace ID / Evidence Chain 欄位貫穿規範已納入（2025-12-28）"
    fix_id: VA-METADATA_FIX-20251227-0020
  - doc_key: VERSION_AUDIT
    change_summary: "Only-Add｜Ledger 補登（0021/0022/0023）延伸批次（2025-12-28）"
    fix_id: VA-METADATA_FIX-20251227-0023
```

---

## F4. JSON Override Patch（machine-readable）

```json
{
  "schema_version": 1,
  "override": [
    {
      "doc_key": "DOCUMENT_INDEX",
      "fix_id": "VA-METADATA_FIX-20251227-0022"
    },
    {
      "doc_key": "DEPLOY_OPS",
      "change_summary": "Only-Add｜Trace ID / Evidence Chain 欄位貫穿規範已納入（2025-12-28）",
      "fix_id": "VA-METADATA_FIX-20251227-0020"
    },
    {
      "doc_key": "VERSION_AUDIT",
      "change_summary": "Only-Add｜Ledger 補登（0021/0022/0023）延伸批次（2025-12-28）",
      "fix_id": "VA-METADATA_FIX-20251227-0023"
    }
  ]
}
```

---

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  

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

### H2.1 YAML（delta）

```yaml
  generated_date: "2025-12-28"
  rules:
    - when_doc_key_equals: "GOVERNANCE_STATE"
      resolve_to_doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      note: "正名封口：GOVERNANCE_STATE 僅為 alias；唯一合法 doc_key 為 GOVERNANCE_STATE_FREEZE_V1"
  additions:
    - doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      change_summary: "Only-Add｜P0 全閉合：引用模板作廢＋新模板固定＋alias 封口（不改原文）"
      fix_id: "VA-METADATA_FIX-20251228-0031"
```

### H2.2 JSON（delta）

```json
{
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
        "change_summary": "Only-Add｜P0 全閉合：引用模板作廢＋新模板固定＋alias 封口（不改原文）",
        "fix_id": "VA-METADATA_FIX-20251228-0031"
      }
    ]
  }
}
```

---

## H3. 引用端硬規則（P0 Re-Assert）

- 當「文件自述」與「Index 裁決」不一致：
  - 一律以 Index 裁決為準  
  - 自述視為 Metadata Discrepancy（不得被工具鏈提升為 doc_key）

---

## H4. 版本戳記
- generated_at: 2025-12-28 02:30:24 +0800（Asia/Taipei）

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  

---

## J1. Mapping Precedence（Hard｜工具鏈採用順序）

若同一文件內存在多份 machine-readable mapping（YAML/JSON）：
1) 先選擇 `schema_version` 最大者  
2) 若 `schema_version` 相同，選擇 `generated_date` 較新者  
4) 若無法裁決，視為不合規載入（不得進入 Gate/Audit/Replay）

---

## J2. Normalization Patch（schema_version: 2｜YAML）

```yaml
schema_version: 2
generated_date: 2025-12-28
batch_id: BATCH-20251228-P1-NORMALIZATION
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
      fix_id: "VA-METADATA_FIX-20251228-0034"
    - doc_key: "AI_GOV"
      fix_id: "VA-METADATA_FIX-20251228-0029"
    - doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      fix_id: "VA-METADATA_FIX-20251228-0030"
    - doc_key: "VERSION_AUDIT"
      fix_id: "VA-METADATA_FIX-20251228-0034"
    - doc_key: "DATA_SOURCES"
      fix_id: "VA-METADATA_FIX-20251228-0033"
```

---

## J3. Normalization Patch（schema_version: 2｜JSON）

```json
{
  "schema_version": 2,
  "generated_date": "2025-12-28",
  "batch_id": "BATCH-20251228-P1-NORMALIZATION",
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
        "fix_id": "VA-METADATA_FIX-20251228-0034"
      },
      {
        "doc_key": "AI_GOV",
        "fix_id": "VA-METADATA_FIX-20251228-0029"
      },
      {
        "doc_key": "GOVERNANCE_STATE_FREEZE_V1",
        "fix_id": "VA-METADATA_FIX-20251228-0030"
      },
      {
        "doc_key": "VERSION_AUDIT",
        "fix_id": "VA-METADATA_FIX-20251228-0034"
      },
      {
        "doc_key": "DATA_SOURCES",
        "fix_id": "VA-METADATA_FIX-20251228-0033"
      }
    ]
  }
}
```

---

## J4. 版本戳記
- generated_at: 2025-12-28 02:48:55 +0800（Asia/Taipei）

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
目的：補齊 `schema_version = 2` 之 `latest_mapping_v2` 覆蓋範圍，避免工具鏈因採用較新 schema 而「看不到」部分 doc_key；本補丁為 append-only（後序優先），不移除任何既有 mapping。

---

## K1. 適用範圍（Hard）
  - 覆蓋 **DOCUMENT_INDEX Authoritative Index 表格列為 ACTIVE** 之全部 doc_key  
  - 並額外補登：`PROJECT_PROMPT`、`PROCESS_ANCHOR`（入口與工程定錨）
- 若工具鏈採用 `schema_version = 2`，且遇到同級多份 v2 mapping：

---

## K2. Completeness Patch（schema_version: 2｜YAML）

```yaml
schema_version: 2
generated_date: 2025-12-28
batch_id: BATCH-20251228-P2-COMPLETENESS
  scope: "latest_mapping_v2_full"
  note: "補齊 v2 mapping 覆蓋全部 ACTIVE doc_key（以 Authoritative Index 為準），並補登入口/工程定錨文件；append-only，後序優先。"
  latest_mapping_v2_full:
    - doc_key: "AI_GOV"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "ARCH_FLOW"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "BEGINNER_GUIDE"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "DATA_SOURCES"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "DEPLOY_OPS"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "DOCUMENT_INDEX"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "EXECUTION_CONTROL"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "FULL_ARCH"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "GOVERNANCE_GATE_SPEC"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "LOCAL_ENV"
      latest_artifact: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "MASTER_ARCH"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "MASTER_CANON"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "README"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "RISK_COMPLIANCE"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "STRATEGY_FEATURE_INDEX"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "STRATEGY_UNIVERSE"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "TWSE_RULES"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "UI_SPEC"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "VERSION_AUDIT"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "PROJECT_PROMPT"
      fix_id: "VA-METADATA_FIX-20251228-0036"
    - doc_key: "PROCESS_ANCHOR"
      fix_id: "VA-METADATA_FIX-20251228-0036"
```

---

## K3. Completeness Patch（schema_version: 2｜JSON）

```json
{
  "schema_version": 2,
  "generated_date": "2025-12-28",
  "batch_id": "BATCH-20251228-P2-COMPLETENESS",
    "scope": "latest_mapping_v2_full",
    "note": "補齊 v2 mapping 覆蓋全部 ACTIVE doc_key（以 Authoritative Index 為準），並補登入口/工程定錨文件；append-only，後序優先。",
    "latest_mapping_v2_full": [
      {
        "doc_key": "AI_GOV",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "ARCH_FLOW",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "BEGINNER_GUIDE",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "DATA_SOURCES",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "DEPLOY_OPS",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "DOCUMENT_INDEX",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "EXECUTION_CONTROL",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "FULL_ARCH",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "GOVERNANCE_GATE_SPEC",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "GOVERNANCE_STATE_FREEZE_V1",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "LOCAL_ENV",
        "latest_artifact": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "MASTER_ARCH",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "MASTER_CANON",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "README",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "RISK_COMPLIANCE",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "STRATEGY_FEATURE_INDEX",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "STRATEGY_UNIVERSE",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "TWSE_RULES",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "UI_SPEC",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "VERSION_AUDIT",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "PROJECT_PROMPT",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      },
      {
        "doc_key": "PROCESS_ANCHOR",
        "fix_id": "VA-METADATA_FIX-20251228-0036"
      }
    ]
  }
}
```

---

## K4. 版本戳記
- generated_at: 2025-12-28 02:56:19 +0800（Asia/Taipei）

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
目的：  
1) 修補「PROJECT_PROMPT 自述 ACTIVE」但未列入 Authoritative Index ACTIVE 表格的治理不一致；以 Only-Add 追加 ACTIVE 補登（不改原表）。  
2) 提供單一可載入的 **Canonical Bundle（schema_version=3）**，整合 legacy 解析規則＋完整 latest mapping，避免多補丁選擇/合併歧義。

---

## L1. Authoritative Index｜ACTIVE 補登（Only-Add Amendment）

- 本補登為 append-only：不改寫既有表格；工具鏈與人工查核時，**Authoritative Index = 原表 + 本 Amendment（日期較新者優先）**。

### L1.1 Amendment Row（最小欄位）

| 文件名稱 | doc_key | 治理等級 | 狀態 | 備註 |
|---|---|---|---|---|
| TAITS_PROJECT_PROMPT.md | PROJECT_PROMPT | B（Project Prompt & Operating Contract） | ACTIVE | 入口治理契約；裁決仍回歸 DOCUMENT_INDEX / MASTER_ARCH / MASTER_CANON；僅供新對話啟動與對齊 |

---

## L2. Canonical Bundle（schema_version = 3）— Single Loadable Source

原則：工具鏈若支援 schema_version 選擇，一律優先採用 **schema_version 最大者**。  

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
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "ARCH_FLOW"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "BEGINNER_GUIDE"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "DATA_SOURCES"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "DEPLOY_OPS"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "DOCUMENT_INDEX"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "EXECUTION_CONTROL"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "FULL_ARCH"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "GOVERNANCE_GATE_SPEC"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "GOVERNANCE_STATE_FREEZE_V1"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "LOCAL_ENV"
      latest_artifact: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "MASTER_ARCH"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "MASTER_CANON"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "PROJECT_PROMPT"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "README"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "RISK_COMPLIANCE"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "STRATEGY_FEATURE_INDEX"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "STRATEGY_UNIVERSE"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "TWSE_RULES"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "UI_SPEC"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "VERSION_AUDIT"
      status: "ACTIVE"
      fix_id: "VA-METADATA_FIX-20251228-0039"
    - doc_key: "PROCESS_ANCHOR"
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
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "ARCH_FLOW",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "BEGINNER_GUIDE",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "DATA_SOURCES",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "DEPLOY_OPS",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "DOCUMENT_INDEX",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "EXECUTION_CONTROL",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "FULL_ARCH",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "GOVERNANCE_GATE_SPEC",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "GOVERNANCE_STATE_FREEZE_V1",
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
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "MASTER_CANON",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "PROJECT_PROMPT",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "README",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "RISK_COMPLIANCE",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "STRATEGY_FEATURE_INDEX",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "STRATEGY_UNIVERSE",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "TWSE_RULES",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "UI_SPEC",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "VERSION_AUDIT",
        "status": "ACTIVE",
        "fix_id": "VA-METADATA_FIX-20251228-0039"
      },
      {
        "doc_key": "PROCESS_ANCHOR",
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

---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
目的：消除「人類複製貼上」誤用 doc_key 的主要來源（表格顯示省略 `…`）；提供一份可直接複製、零省略、零歧義的 doc_key 清單。  

---

## M1. HARD RULE（表格省略不得作為引用鍵）

- 任何表格/展示型欄位若以 `…`、截斷、換行折疊、UI 省略呈現 doc_key：
  - 一律不得作為 `ref_doc_key` / `doc_key` / `gate_doc_key` / `audit_doc_key` 等引用鍵值
- 引用鍵值必須取自：
  1) 本文件之 **Canonical Bundle（schema_version=3）**；或  

---

## M2. Copy-Safe DocKey List（完整鍵清單｜可直接複製）

下列清單為「完整 doc_key 原字串」；不得增減字元、不得自行改寫大小寫、不得加空白。

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

---

## 治理補強（已整合為正文）

上位裁決：AI_GOV（A+）＋MASTER_ARCH（A）＋MASTER_CANON（A）  
目的：在不改寫既有 Index 表格與裁決規則之下，補齊「實體檔名差異」與「doc_key 別名」造成的引用歧義；確保 Gate / 稽核 / 回放能以唯一映射定位檔案。

---

## DI-A1. ACTIVE 實體檔名映射表（Logical→Physical）

- `canonical_filename`：DOCUMENT_INDEX 內的裁決檔名（治理身份）  
- `physical_filename`：本專案目錄中的實際檔名（載體）  
- 本表僅負責「定位檔案」；不新增任何治理位階、不改寫既有裁決規則。

| doc_key | canonical_filename | physical_filename |
|---|---|---|
| LOCAL_ENV | TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md | TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md |

---

## DI-A2. doc_key Alias（歷史別名）對照與唯一裁決宣告

- 原則：**跨文件引用一律使用 `canonical_doc_key`**。  
- `legacy_alias` 僅允許出現在舊版 header、歷史截圖、或已發佈文件之保留文字中；不得作為新的引用身份。  
- 若 alias 與 DOCUMENT_INDEX 裁決產生歧義：一律以 DOCUMENT_INDEX（Authoritative Index）為準。

| canonical_doc_key | legacy_alias | 適用範圍/備註 |
|---|---|---|
| AI_GOV | AI_GOVERNANCE_FULLSPEC | AI_GOV 文件 header 歷史保留字串；跨文件引用一律使用 AI_GOV |
| DATA_SOURCES | DATA_UNIVERSE | DATA_SOURCES 文件 header 歷史保留字串；跨文件引用一律使用 DATA_SOURCES |

---

## DI-A3. 稽核雜湊（可回放定位用；sha256 前 12 碼）

- 本表為稽核/回放用「可選欄位」；不取代 VERSION_AUDIT 的正式稽核程序。  
- 若檔案內容有變更（Only-Add），其 sha256 將隨之變動；應於 VERSION_AUDIT 進行對應登記。

| doc_key | physical_filename | sha256_12 |
|---|---|---|
| LOCAL_ENV | TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md | 9ef406565dbf |

---

## DI-A4. 最終宣告（Freeze v1.0）

- 若本映射表與實體目錄不一致：以 **本映射表** 為優先修補對象（Only-Add 增補/更正映射列），並同步於 VERSION_AUDIT 登錄。
---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md`
- canonical_doc_key（Index 裁決識別碼）：`DOCUMENT_INDEX`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=DOCUMENT_INDEX` + `canonical_filename=TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

## 治理補強（已整合為正文）

上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
目的：以 MASTER_CANON 為主導，對齊「引用合法性、doc_key 身份、子級標籤（Label）解讀、資料治理別名（alias）封口、最小可稽核引用格式」之全域一致口徑；不改寫任何既有正文條款。

---

## G0. 適用範圍（Hard Boundary）

1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。  
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。  
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。  
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。  

- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

並統一裁決：
- 任何文件「是否可引用」＝以 DOCUMENT_INDEX 之 Authoritative Index（ACTIVE 表格）為準  
- 任何文件「治理等級 bucket」＝以 DOCUMENT_INDEX 之 A+ / A / B / C 分桶為準  
- 文件內自述之等級/狀態若與 Index 有張力：依 DOCUMENT_INDEX §6 採「保守處置」（STOP/RETURN/BLOCK；以既有 Gate/風控規範語義為準）

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
  - 一律視為「引用非法」→ 依 GOVERNANCE_GATE_SPEC 進行 BLOCK/RETURN（依其既有語義；不得補救）。

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
- 依 DOCUMENT_INDEX §6 採保守處置：不得形成裁決性輸出（PASS/APPROVE/EXECUTE 等）；必要時 RETURN/BLOCK。

---

## G5. 最終宣告（Freeze v1.0）

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為約束另以 AI_GOV 為最高）  

---

## N0. 使用規則（Hard Rules）

   - 仍以 Authoritative Index 表格為準；工具鏈必須 **RETURN/BLOCK** 並回報差異（保守處置）。  
3) 任何引用若以檔名作為鍵值（含 `ref_filename`、`artifact_filename`、`latest_artifact` 等）：  
   - 不得回填/覆寫本段；必須以 Only-Add 追加「新 Bundle」做下一輪映射。

---

## N1. Bundle 251231｜Authoritative Physical Artifact Map（22 files）

| doc_key | status | canonical_filename（Index/引用） | physical_filename（本專案） | sha256_12 | source_alias（來源/舊檔名） |
|---|---|---|---|---|---|
| `GOVERNANCE_STATE_FREEZE_V1` | ACTIVE | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `443dbd4a27a4` | `—` |
| `DOCUMENT_INDEX` | ACTIVE | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `d407ea013bc5` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md` |
| `LOCAL_ENV` | ACTIVE | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md` | `a7f23ecb108f` | `TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md` |

---

## N2. Canonical Bundle（schema_version = 3）— Physical Map Extension（YAML）

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
      - doc_key: "AI_GOV"
        status: "ACTIVE"
        canonical_filename: "TAITS_AI_行為與決策治理最終規則全集__251217.md"
        physical_filename: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
        sha256_12: "53354789820b"
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
      - doc_key: "TWSE_RULES"
        status: "ACTIVE"
        canonical_filename: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md"
        physical_filename: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md"
        sha256_12: "3dfe33220600"
      - doc_key: "EXECUTION_CONTROL"
        status: "ACTIVE"
        canonical_filename: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md"
        physical_filename: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md"
        sha256_12: "b6a3ede344e7"
      - doc_key: "UI_SPEC"
        status: "ACTIVE"
        canonical_filename: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md"
        physical_filename: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md"
        sha256_12: "e60eb4446ae6"
      - doc_key: "FULL_ARCH"
        status: "ACTIVE"
        canonical_filename: "TAITS_全系統架構總覽（FULL_ARCH）__251219.md"
        physical_filename: "TAITS_全系統架構總覽（FULL_ARCH）__251231.md"
        sha256_12: "494d5b689e51"
      - doc_key: "MASTER_CANON"
        status: "ACTIVE"
        canonical_filename: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md"
        physical_filename: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md"
        sha256_12: "ecd9ce9c918b"
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
      - doc_key: "GOVERNANCE_GATE_SPEC"
        status: "ACTIVE"
        canonical_filename: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md"
        physical_filename: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md"
        sha256_12: "d3b7ab7fbaab"
      - doc_key: "VERSION_AUDIT"
        status: "ACTIVE"
        canonical_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md"
        physical_filename: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
        sha256_12: "1f3dfb7b29e0"
      - doc_key: "STRATEGY_UNIVERSE"
        status: "ACTIVE"
        canonical_filename: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md"
        physical_filename: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md"
        sha256_12: "4b7f6c871f4f"
      - doc_key: "STRATEGY_FEATURE_INDEX"
        status: "ACTIVE"
        canonical_filename: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md"
        physical_filename: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md"
        sha256_12: "01d564ba369e"
      - doc_key: "ARCH_FLOW"
        status: "ACTIVE"
        canonical_filename: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md"
        physical_filename: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md"
        sha256_12: "d702e88c6000"
      - doc_key: "DATA_SOURCES"
        status: "ACTIVE"
        canonical_filename: "TAITS_資料來源全集（DATA_SOURCES）__251219.md"
        physical_filename: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
        sha256_12: "0a197c01b6c8"
      - doc_key: "DEPLOY_OPS"
        status: "ACTIVE"
        canonical_filename: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md"
        physical_filename: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
        sha256_12: "4cee1444c6c3"
      - doc_key: "RISK_COMPLIANCE"
        status: "ACTIVE"
        canonical_filename: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md"
        physical_filename: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md"
        sha256_12: "344cd3cb642d"
      - doc_key: "PROCESS_ANCHOR"
        status: "SUPPORT"
        physical_filename: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
        sha256_12: "ee5ae3eb19bb"
```

---

## N3. Canonical Bundle（schema_version = 3）— Physical Map Extension（JSON）

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
        },
        {
          "doc_key": "AI_GOV",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_AI_行為與決策治理最終規則全集__251217.md",
          "physical_filename": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
          "sha256_12": "53354789820b",
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
        },
        {
          "doc_key": "TWSE_RULES",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md",
          "physical_filename": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md",
          "sha256_12": "3dfe33220600",
        },
        {
          "doc_key": "EXECUTION_CONTROL",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219.md",
          "physical_filename": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md",
          "sha256_12": "b6a3ede344e7",
        },
        {
          "doc_key": "UI_SPEC",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251219.md",
          "physical_filename": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md",
          "sha256_12": "e60eb4446ae6",
        },
        {
          "doc_key": "FULL_ARCH",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_全系統架構總覽（FULL_ARCH）__251219.md",
          "physical_filename": "TAITS_全系統架構總覽（FULL_ARCH）__251231.md",
          "sha256_12": "494d5b689e51",
        },
        {
          "doc_key": "MASTER_CANON",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md",
          "physical_filename": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md",
          "sha256_12": "ecd9ce9c918b",
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
        },
        {
          "doc_key": "GOVERNANCE_GATE_SPEC",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251219.md",
          "physical_filename": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md",
          "sha256_12": "d3b7ab7fbaab",
        },
        {
          "doc_key": "VERSION_AUDIT",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251219.md",
          "physical_filename": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
          "sha256_12": "1f3dfb7b29e0",
        },
        {
          "doc_key": "STRATEGY_UNIVERSE",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219.md",
          "physical_filename": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md",
          "sha256_12": "4b7f6c871f4f",
        },
        {
          "doc_key": "STRATEGY_FEATURE_INDEX",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md",
          "physical_filename": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md",
          "sha256_12": "01d564ba369e",
        },
        {
          "doc_key": "ARCH_FLOW",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md",
          "physical_filename": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md",
          "sha256_12": "d702e88c6000",
        },
        {
          "doc_key": "DATA_SOURCES",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_資料來源全集（DATA_SOURCES）__251219.md",
          "physical_filename": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
          "sha256_12": "0a197c01b6c8",
        },
        {
          "doc_key": "DEPLOY_OPS",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md",
          "physical_filename": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
          "sha256_12": "4cee1444c6c3",
        },
        {
          "doc_key": "RISK_COMPLIANCE",
          "status": "ACTIVE",
          "canonical_filename": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md",
          "physical_filename": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md",
          "sha256_12": "344cd3cb642d",
        },
        {
          "doc_key": "PROCESS_ANCHOR",
          "status": "SUPPORT",
          "physical_filename": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
          "sha256_12": "ee5ae3eb19bb",
        }
      ]
    }
  }
}
```

---

## N4. 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- bundle: BATCH-20251231-P0-PHYSICAL-ARTIFACT-MAP
- ledger_ref: VA-METADATA_FIX-20251231-0001

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為約束另以 AI_GOV 為最高）  
目的：修補「文件內出現之 legacy 引用檔名」無法解析到本 repo 落盤實體檔（__251231）之問題。  

---

## P1. 使用規則（Hard Rules）

1) 若引用檔名可直接命中 repo 實體檔名（physical_filename），則以實體檔名優先。  
3) 本 alias mapping 僅供載入/稽核/回放使用；不得據此推導新增治理條款或改寫既有語義。  
4) 若遇到未列入 mapping 之引用：一律視為不可解析引用（RETURN/BLOCK），並由 Gate 回報差異；不得自動猜測。

---

## P1.1｜Reference Alias Map（90 legacy refs）

| legacy_ref_filename | resolve_to_physical_filename | resolution_rule |
|---|---|---|
| `README.md` | `README__251231.md` | `generic_map` |
| `README｜TAITS 專案總覽與使用說明（README）__251220.md` | `README__251231.md` | `readme_route` |
| `TAITS_<中文主標題>（<DOC_KEY>）__YYMMDD.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `placeholder_template_route` |
| `TAITS_GOVERNANCE_STATE__UNFREEZE_vX.Y__<date>.md` | `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md` | `routing_token` |
| `TAITS_XXX__YYMMDD.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `placeholder_template_route` |
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
| `TAITS｜程式開發流程定錨文件（Unified Process Anchor）.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `generic_map` |
| `canonical_filename=README.md` | `README__251231.md` | `generic_map` |
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
| `docs/governance/TAITS_XXX__YYMMDD.md` | `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md` | `placeholder_template_route` |
| `engineering/cr/CR-YYYYMMDD-####.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `engineering_path_route` |
| `engineering/ecr/ECR-<id>.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `engineering_path_route` |
| `engineering/ecr/ECR-YYYYMMDD-####.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `engineering_path_route` |
| `engineering/worklog/ENGINEERING_STATUS.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_route_to_process_anchor` |
| `ref_doc_name = TAITS_資料來源全集（DATA_SOURCES）__251219.md` | `TAITS_資料來源全集（DATA_SOURCES）__251231.md` | `routing_token` |

---

## P1.2｜Resolver Bundle（schema_version = 3）— YAML

```yaml
schema_version: 3
batch_id: BATCH-20251231-P1-REFERENCE-ALIAS-EXPANSION
reference_alias_map:
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
      resolve_to: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
      rule: "ai_route"
      resolve_to: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
      rule: "ai_route"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "routing_token"
    - legacy_ref_filename: "TAITS_GOVERNANCE_STATE__UNFREEZE_vX.Y__<date>.md"
      resolve_to: "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_route_to_process_anchor"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_route_to_process_anchor"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_route_to_process_anchor"
    - legacy_ref_filename: "TAITS_XXX__YYMMDD.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "placeholder_template_route"
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
      resolve_to: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
      rule: "routing_token"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
    - legacy_ref_filename: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "generic_map"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
    - legacy_ref_filename: "canonical_filename=README.md"
      resolve_to: "README__251231.md"
      rule: "generic_map"
    - legacy_ref_filename: "canonical_filename=TAITS_AI_行為與決策治理最終規則全集__251217.md"
      resolve_to: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
      rule: "version_swap"
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

---

## P1.3｜Resolver Bundle（schema_version = 3）— JSON

```json
{
  "schema_version": 3,
  "batch_id": "BATCH-20251231-P1-REFERENCE-ALIAS-EXPANSION",
  "reference_alias_map": {
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
        "resolve_to": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
        "rule": "ai_route"
      },
      {
        "resolve_to": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
        "rule": "ai_route"
      },
      {
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "routing_token"
      },
      {
        "legacy_ref_filename": "TAITS_GOVERNANCE_STATE__UNFREEZE_vX.Y__<date>.md",
        "resolve_to": "TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_route_to_process_anchor"
      },
      {
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_route_to_process_anchor"
      },
      {
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_route_to_process_anchor"
      },
      {
        "legacy_ref_filename": "TAITS_XXX__YYMMDD.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "placeholder_template_route"
      },
      {
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
        "resolve_to": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
        "rule": "routing_token"
      },
      {
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
      },
      {
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
      },
      {
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
      },
      {
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
      },
      {
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
      },
      {
        "legacy_ref_filename": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "generic_map"
      },
      {
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
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

---

## 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- batch_id: BATCH-20251231-P1-REFERENCE-ALIAS-EXPANSION
- ledger_ref: VA-METADATA_FIX-20251231-0002

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為約束另以 AI_GOV 為最高）  

---

## P1B.1｜Reference Alias Extension（21 legacy refs）

| legacy_ref_filename | resolve_to_physical_filename | resolution_rule |
|---|---|---|
| `engineering/cr/CR-<id>.md` | `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md` | `engineering_path_route` |

---

## P1B.2｜Resolver Bundle Extension（schema_version = 3）— YAML

```yaml
schema_version: 3
batch_id: BATCH-20251231-P1B-REFERENCE-ALIAS-EXTENSION
reference_alias_map_extension:
  items:
      resolve_to: "TAITS_AI_行為與決策治理最終規則全集__251231.md"
      resolve_to: "TAITS_PROJECT_PROMPT__251231.md"
      resolve_to: "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md"
      resolve_to: "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md"
      resolve_to: "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md"
      resolve_to: "TAITS_全系統架構總覽（FULL_ARCH）__251231.md"
      resolve_to: "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md"
    - legacy_ref_filename: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md"
      resolve_to: "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md"
      resolve_to: "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md"
      resolve_to: "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md"
      resolve_to: "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      resolve_to: "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md"
      resolve_to: "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md"
      resolve_to: "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md"
      resolve_to: "TAITS_資料來源全集（DATA_SOURCES）__251231.md"
      resolve_to: "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md"
      resolve_to: "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      resolve_to: "TAITS_PROJECT_PROMPT__251231.md"
    - legacy_ref_filename: "engineering/cr/CR-<id>.md"
      resolve_to: "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md"
      rule: "engineering_path_route"
```

---

## P1B.3｜Resolver Bundle Extension（schema_version = 3）— JSON

```json
{
  "schema_version": 3,
  "batch_id": "BATCH-20251231-P1B-REFERENCE-ALIAS-EXTENSION",
  "reference_alias_map_extension": {
    "items": [
      {
        "resolve_to": "TAITS_AI_行為與決策治理最終規則全集__251231.md",
      },
      {
        "resolve_to": "TAITS_PROJECT_PROMPT__251231.md",
      },
      {
        "resolve_to": "TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md",
      },
      {
        "resolve_to": "TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md",
      },
      {
        "resolve_to": "TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md",
      },
      {
        "resolve_to": "TAITS_全系統架構總覽（FULL_ARCH）__251231.md",
      },
      {
        "resolve_to": "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251231.md",
      },
      {
        "legacy_ref_filename": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ACTIVE_20251229.md",
        "resolve_to": "TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md",
      },
      {
        "resolve_to": "TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md",
      },
      {
        "resolve_to": "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md",
      },
      {
        "resolve_to": "TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md",
      },
      {
        "resolve_to": "TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md",
      },
      {
        "resolve_to": "TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md",
      },
      {
        "resolve_to": "TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md",
      },
      {
        "resolve_to": "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md",
      },
      {
        "resolve_to": "TAITS_資料來源全集（DATA_SOURCES）__251231.md",
      },
      {
        "resolve_to": "TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md",
      },
      {
        "resolve_to": "TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md",
      },
      {
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
      },
      {
        "resolve_to": "TAITS_PROJECT_PROMPT__251231.md",
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

---

## 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- batch_id: BATCH-20251231-P1B-REFERENCE-ALIAS-EXTENSION
- ledger_ref: VA-METADATA_FIX-20251231-0003

## 治理補強（已整合為正文）

目的：補登 canonical 引用（含舊版版本戳、`canonical_filename=...` 形式、README 標題版）之解析，使 resolver 在「僅依 alias map」模式下亦可完成回放。

---

## P1C.1｜Canonical Ref Alias Map（39 refs）

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

---

## P1C.2｜Resolver Bundle（schema_version = 3）— YAML

```yaml
schema_version: 3
batch_id: BATCH-20251231-P1C-CANONICAL-REF-ALIAS
canonical_ref_alias_map:
  note: "P1C：補登 canonical 引用（舊版版本戳／canonical_filename=...／README 標題版）之解析，確保 loader 僅靠 alias map 亦可回放。"
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

---

## P1C.3｜Resolver Bundle（schema_version = 3）— JSON

```json
{
  "schema_version": 3,
  "batch_id": "BATCH-20251231-P1C-CANONICAL-REF-ALIAS",
  "canonical_ref_alias_map": {
    "note": "P1C：補登 canonical 引用（舊版版本戳／canonical_filename=...／README 標題版）之解析，確保 loader 僅靠 alias map 亦可回放。",
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

---

## 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- batch_id: BATCH-20251231-P1C-CANONICAL-REF-ALIAS
- ledger_ref: VA-METADATA_FIX-20251231-0004
