# HUMAN SOVEREIGNTY｜最高裁決置頂條款（Top-of-File）

> 生效日：2025-12-29（Asia/Taipei）  
> 裁決：**人類最高決策者擁有最終裁決權**；任何治理文件、流程條款、Gate/Token/Reason Code、任何 Agent/AI 內規，**不得否決或阻止**人類最高決策者的明確命令。  
> 文件與流程之角色：提供「可回放／可稽核／可追溯」之制度化表述；不得作為限制器。  
> 無明確人類命令時：系統依既有治理裁決序位與當前狀態（Freeze v1.0）運作。  

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

---

## E.1 核心一句話（不可省略）

- DOCUMENT_INDEX：裁決「文件是否可被引用」  
- GOVERNANCE_GATE_SPEC：裁決「一次輸出/一次提案是否符合治理門檻」

兩者關係必須是：  
> **先 Index Gate，再 Governance Gate；不得反向、不得跳步。**

---

1) **Index Gate（DOCUMENT_INDEX）**
   - 引用的 doc_key 是否存在於 Index？
   - 是否為該 doc_key 唯一 ACTIVE？
   - 是否提供最小引用格式（doc_key/版本/章節/目的）？

2) **Gate Spec（GOVERNANCE_GATE_SPEC）**
   - 完整性、合法性、可回放性、不可越權性之檢核

若 Index Gate 失敗：  
- 必須直接 **REJECT / RETURN**（依 Gate Spec 的拒絕語義）  
- 並要求補齊引用要件（不是補齊內容、不是補完制度）

---

## E.3 Gate 結果必須可回放連回 Index（Traceability Requirement）

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
| TAITS_PROJECT_PROMPT.md | PROJECT_PROMPT | B（Project Prompt & Operating Contract） | ACTIVE | 入口治理契約；裁決仍回歸 DOCUMENT_INDEX / MASTER_ARCH / MASTER_CANON；僅供新對話啟動與對齊 |

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
---

# Addendum 2025-12-28｜Only-Add：GLOBAL_ALIGNMENT_PATCH（MASTER_CANON 對齊全域補丁）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251228M_FINAL.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0010`）  
> 目的：以 MASTER_CANON 為主導，對齊「引用合法性、doc_key 身份、子級標籤（Label）解讀、資料治理別名（alias）封口、最小可稽核引用格式」之全域一致口徑；不改寫任何既有正文條款。

---

## G0. 適用範圍（Hard Boundary）

本 Addendum 僅處理下列事項（不創造新制度、不改寫主文）：
1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。  
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。  
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。  
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。  

本 Addendum **不處理**：
- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

- 本文件 `doc_key` 既有標示為 `DOCUMENT_INDEX`；本 Addendum 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

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

- 本 Addendum 為 Only-Add；不改寫本文件任何既有條款。  
- 本 Addendum 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。  
- 本 Addendum 目的僅在於消解引用歧義、避免 Gate 因 metadata/格式缺口而誤判，並確保全鏈路可稽核、可回放。

（Addendum 2025-12-28｜Only-Add｜Freeze v1.0 完）

# Addendum 2025-12-31｜Only-Add：Bundle 251231｜Physical Artifact Map × Hash Ledger（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為約束另以 AI_GOV 為最高）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（新增條目：`VA-METADATA_FIX-20251231-0001`）  
> 目的：修補「文件內引用檔名（canonical/addendum）≠ repo 落盤實體檔名（__251231）」之失配，避免 Gate/Loader/稽核工具鏈因檔名找不到而失效；本 Addendum **不改寫**既有 Authoritative Index 表格、ACTIVE 裁決、治理等級、覆蓋/否決規則，只提供可回放的實體映射與 hash ledger。

---

## N0. 使用規則（Hard Rules）

1) 本 Addendum 為 **工具鏈/工程載入** 用之「實體檔案映射（Physical Map）」與「hash ledger」。  
2) 若本 Addendum 與本文件既有 Authoritative Index 表格之 ACTIVE / 治理等級 / 覆蓋規則不一致：  
   - 仍以 Authoritative Index 表格為準；工具鏈必須 **RETURN/BLOCK** 並回報差異（保守處置）。  
3) 任何引用若以檔名作為鍵值（含 `ref_filename`、`artifact_filename`、`latest_artifact` 等）：  
   - 一律先依本 Addendum 之 mapping 解析至 `physical_filename`；若解析失敗 → 視為 **不可用引用**（不得產生裁決/執行性輸出）。  
4) 本 Addendum 僅新增；若未來 repo 落盤檔名再變更：  
   - 不得回填/覆寫本段；必須以 Only-Add 追加「新 Bundle」做下一輪映射。

---

## N1. Bundle 251231｜Authoritative Physical Artifact Map（22 files）

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

---

## N4. 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- bundle: BATCH-20251231-P0-PHYSICAL-ARTIFACT-MAP
- ledger_ref: VA-METADATA_FIX-20251231-0001

（Addendum 2025-12-31｜Only-Add｜Freeze v1.0 完）

# Addendum 2025-12-31｜Only-Add：P1｜Reference Alias Expansion（Resolver Map）— legacy refs → physical（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為約束另以 AI_GOV 為最高）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（新增條目：`VA-METADATA_FIX-20251231-0002`）  
> 目的：修補「文件內出現之 legacy 引用檔名」無法解析到本 repo 落盤實體檔（__251231）之問題。  
> 本 Addendum 不改寫任何既有段落、不更動 ACTIVE/裁決序位；僅新增 resolver 所需之 alias mapping。

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
| `TAITS｜GPT新對話續編編輯SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228R_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_addendum_route` |
| `TAITS｜GPT新對話續編編輯SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228_FINAL.md` | `TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md` | `support_addendum_route` |
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

---

## P1.2｜Resolver Bundle（schema_version = 3）— YAML

```yaml
schema_version: 3
batch_id: BATCH-20251231-P1-REFERENCE-ALIAS-EXPANSION
reference_alias_map:
  note: "P1：補登 legacy 引用檔名（含舊版版本戳、README.md、工程路徑、舊 addendum 檔名、樣板檔名）之解析；不改寫既有文件內容，僅提供 resolver 之 alias mapping。"
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
    - legacy_ref_filename: "TAITS｜GPT新對話續編編輯SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228R_FINAL.md"
      resolve_to: "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md"
      rule: "support_addendum_route"
    - legacy_ref_filename: "TAITS｜GPT新對話續編編輯SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228_FINAL.md"
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

---

## P1.3｜Resolver Bundle（schema_version = 3）— JSON

```json
{
  "schema_version": 3,
  "batch_id": "BATCH-20251231-P1-REFERENCE-ALIAS-EXPANSION",
  "reference_alias_map": {
    "note": "P1：補登 legacy 引用檔名（含舊版版本戳、README.md、工程路徑、舊 addendum 檔名、樣板檔名）之解析；不改寫既有文件內容，僅提供 resolver 之 alias mapping。",
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
        "legacy_ref_filename": "TAITS｜GPT新對話續編編輯SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228R_FINAL.md",
        "resolve_to": "TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md",
        "rule": "support_addendum_route"
      },
      {
        "legacy_ref_filename": "TAITS｜GPT新對話續編編輯SOP（Freeze v1.0｜Index Gate First）__ADDENDUM_20251228_FINAL.md",
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

---

## 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- batch_id: BATCH-20251231-P1-REFERENCE-ALIAS-EXPANSION
- ledger_ref: VA-METADATA_FIX-20251231-0002

（Addendum 2025-12-31｜Only-Add｜P1 完）

# Addendum 2025-12-31｜Only-Add：P1B｜Reference Alias Extension（v4 補登）— 21 legacy refs → physical（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為約束另以 AI_GOV 為最高）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（新增條目：`VA-METADATA_FIX-20251231-0003`）  
> 目的：補登 Postcheck v4 新增發現之 21 筆 legacy 引用（多為 addendum / inlineappendix / 工程路徑）之解析規則，避免載入/稽核回放因檔名缺失而中斷。

---

## P1B.1｜Reference Alias Extension（21 legacy refs）

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

---

## P1B.2｜Resolver Bundle Extension（schema_version = 3）— YAML

```yaml
schema_version: 3
batch_id: BATCH-20251231-P1B-REFERENCE-ALIAS-EXTENSION
reference_alias_map_extension:
  note: "P1B：補登 Postcheck v4 新增之 21 筆 legacy 引用（多為 addendum/inlineappendix/工程路徑）。"
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

---

## P1B.3｜Resolver Bundle Extension（schema_version = 3）— JSON

```json
{
  "schema_version": 3,
  "batch_id": "BATCH-20251231-P1B-REFERENCE-ALIAS-EXTENSION",
  "reference_alias_map_extension": {
    "note": "P1B：補登 Postcheck v4 新增之 21 筆 legacy 引用（多為 addendum/inlineappendix/工程路徑）。",
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

---

## 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- batch_id: BATCH-20251231-P1B-REFERENCE-ALIAS-EXTENSION
- ledger_ref: VA-METADATA_FIX-20251231-0003

（Addendum 2025-12-31｜Only-Add｜P1B 完）

# Addendum 2025-12-31｜Only-Add：P1C｜Canonical Ref Alias Map（v5 補登）— 39 refs → physical（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220.md（doc_key：DOCUMENT_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（新增條目：`VA-METADATA_FIX-20251231-0004`）  
> 目的：補登 canonical 引用（含舊版版本戳、`canonical_filename=...` 形式、README 標題版）之解析，使 resolver 在「僅依 alias map」模式下亦可完成回放。

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

---

## P1C.2｜Resolver Bundle（schema_version = 3）— YAML

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

---

## P1C.3｜Resolver Bundle（schema_version = 3）— JSON

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

---

## 版本戳記
- generated_at: 2025-12-31 00:00:00 +0800（Asia/Taipei）
- batch_id: BATCH-20251231-P1C-CANONICAL-REF-ALIAS
- ledger_ref: VA-METADATA_FIX-20251231-0004

（Addendum 2025-12-31｜Only-Add｜P1C 完）
