# TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260104

doc_key：MASTER_ARCH  
治理等級：A（母體／憲法級｜核心鐵律）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live / Live-Shadow）  
版本狀態：ACTIVE（單一正確正文版｜最大完備＋累積式更新）  
版本日期：2026-01-04（Asia/Taipei）  
對齊母法：DOCUMENT_INDEX（A+）／AI_GOV（A+）  
平行參照：MASTER_CANON／RISK_COMPLIANCE／GOVERNANCE_GATE_SPEC／EXECUTION_CONTROL／VERSION_AUDIT／UI_SPEC  
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

## 0. 文件定位（Constitution）

本文件為 TAITS 母體憲法級文件，用於定義「永遠不可違反」的核心鐵律與越權禁止邊界。  
若任何下位文件、工程實作、Agent 行為、UI 呈現與本文件衝突，一律以本文件裁決。

---

doc_key：MASTER_ARCH  
治理等級：A（Constitutional｜母體總憲法）  
版本狀態：ACTIVE · LOCKABLE  
適用範圍：TAITS 全系統（TWSE / TAIFEX；Research / Backtest / Simulation / Paper / Live）  
版本日期：2026-01-04（Asia/Taipei）  
變更原則：**最大完備（Max-Completeness）＋累積式更新（Cumulative Update）**  
- 允許：融合更新／覆寫／重排版／修正錯誤敘述，以收斂為「單一正確正文（Single Correct 正文）」  
- 禁止：只保留重點／摘要化縮水／使有效資訊消失／造成新舊混讀  
- 舊內容保留：凡屬有效資訊且未被新正文明確更新者，一律保留並持續累積（可重排、可整併重複表述）  
- 可省略：僅限已被新正文**明確取代/更新**之舊資訊；且必須以 VERSION_AUDIT／L11 稽核鏈承接（CHANGELOG＋HASH_MANIFEST＋Scope＋Audit Hand-off）

---

## 全局定錨｜單一口徑（S1）

### 1. 人類最高決策者主權（SOVEREIGNTY）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接，不得卡死更新。

### 2. L9–L11 最終語義（跨文件一致）

- **L9（投資報告層｜Investment Report）**：輸出「可追蹤、可更新、可標的化」之投資報告；必含數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源），並支援事件驅動滾動更新。  
- **L10（人類裁決與交易授權層｜Human Decision & Trade Authorization）**：由人類最高決策者裁決不動作／回測／模擬／紙上／實盤等，並決定授權邊界（automation_mode、authorization_envelope、有效期限、撤銷條件等）。任何交易型態皆以 L10 明確裁決為準。  
- **L11（全層工程稽核回放層｜Engineering Audit & Replay）**：對 L1–L11 全層輸入/處理/輸出/裁決/執行鏈路留痕，供人類與工程端可讀、可查、可回放；**L11 非下單層**，禁止作為下單或執行入口。

#### 2.A 詳細必備內容（工程一致口徑｜最大完備承接）

> 本小節承接歷史版本中已存在之 L9–L11 細項要求，作為本文件之「最大完備」可操作細節；不改變本節既有語義，只補足工程可執行的輸出規格。

##### L9｜投資報告層（Investment Report Layer）
- **目的**：產出「人類可讀」且「可追蹤」的完整投資報告，用於人類在 L10 做最終裁決前的資訊理解與方案評估。
- **必備內容（不可省略）**  
  1. **數據**：關鍵指標數值、區間變化、統計摘要（來源與時間戳須可追溯）  
  2. **圖形**：至少包含趨勢/區間/事件標註等可視化（可為文字描述的圖形規格，工程端可再渲染）  
  3. **進出價格建議（僅建議，非下單）**：  
     - 進場/加碼/減碼/出場/停損/停利的「價格區間」與「觸發條件」  
     - 必須附上假設、風險點、失效條件  
  4. **標的化追蹤（Tracking）**：  
     - `tracking_id`（唯一鍵）＋ `report_version`＋ `as_of`（資料截點）  
     - 明確記錄「本次報告」對同一標的的延續關係（非一次性解說）
- **輸出定位**：L9 是「投資報告」，不是 Gate、不是下單、不是稽核。

##### L10｜人類裁決與交易授權層（Human Decision & Trade Authorization）
- **目的**：由人類最高決策者對 L9 報告與全系統輸入做最終裁決，並決定執行模式與授權邊界。
- **L10 必須輸出**  
  - `decision`：NO_ACTION / BACKTEST / SIMULATION / PAPER / LIVE  
  - `automation_mode`：MANUAL / SEMI_AUTO / FULL_AUTO（授權模式，不改變「人類為最終裁決者」）  
  - `authorization_envelope`：允許的標的範圍、下單上限、風控條件、撤銷條件、有效期限  
  - `rationale`：裁決理由（需可稽核、可追溯）
- **邊界**：L10 是裁決與授權；實際執行仍受 **Risk/Compliance 最高否決權**與執行控制規範（EXECUTION_CONTROL）約束。

##### L11｜工程稽核回放層（Engineering Audit & Replay）
- **目的**：對 **L1–L11 全層**進行工程稽核、回放與可追溯驗證，用於人類檢視系統是否合理、是否需要調整。
- **L11 必須是「雙料輸出」**  
  1. **人類可讀（Human-Readable）**：能看懂每層做了什麼、為什麼、依據是什麼、哪裡不確定  
  2. **工程可用（Machine-Readable）**：可被程式回放與對帳（hash、版本、參數、輸入輸出索引、trace）
- **覆蓋範圍**：不是只稽核 L10；而是每一層都要留痕，才能評估層級功能是否合理、是否要調整。
- **邊界**：L11 僅做稽核/回放/對帳，**禁止作為下單或執行入口**。

### 3. HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：治理狀態/最大完備＋累積式更新/Gate 不得阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。

---

## 全局語義定錨（L9–L11｜跨文件一致）

> 本節為便於檢索之重導向（redirect）。L9–L11 的唯一有效定義以本文件「§1.2」為準；不得另行拷貝改寫造成新舊混讀。

---

## 治理補強（已整合為正文）

上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+｜Authoritative Index）＋MASTER_CANON（A）  
目的：在 治理狀態 v1.0 期間，封住 MASTER_ARCH 內部若出現之「文件數量／文件清單／ACTIVE 文件集合」快照式描述被誤用為治理裁決依據的風險；固定 ACTIVE/doc_key/治理等級/版本有效性一律由 DOCUMENT_INDEX 表格裁決；並將 S/B+/C+ 等標籤之法律定位明確回歸（Label ≠ 新治理層級），確保母憲法文件在新對話入口不會引入口徑漂移。

---

## A0. 適用範圍（Hard Boundary）

1) 本文件內若出現「文件數量/清單/ACTIVE 集合」之法律定位（Snapshot ≠ 裁決）  
2) Index Gate 唯一裁決來源（DOCUMENT_INDEX Authoritative Index）  
3) 治理標籤（S/B+/C+）之法律定位（Label/Sub-Label；bucket 仍回歸 A+/A/B/C）  
4) 裁決順序字串之助記化定位（Mnemonic ≠ Override Rule）

- 不改寫本文件既有母憲法鐵律、不可違反原則、Regime/Risk/Compliance 優先權  
- 不修改 Canonical Flow（L1–L11）  
- 不重排覆蓋規則（A+ > A > B > C）與衝突裁決程序（仍以 DOCUMENT_INDEX §6 為準）  
- 不新增任何未被上位文件授權的新制度語義

---

## A1. Snapshot 不裁決（No Hardcoded ACTIVE Set）

### A1.1 統一裁決：清單/數量一律視為 Snapshot
凡本文件（MASTER_ARCH）內部出現之：
- 「目前共有 X 份文件」  
- 「ACTIVE 文件數 = X」  
- 任何列舉文件清單、推薦載入清單、快捷載入集合  

- Snapshot（歷史快照/導覽用途）  
- **不具治理裁決效力**（不得用以判定 ACTIVE、doc_key、治理等級、覆蓋關係）

### A1.2 唯一裁決來源：Index Gate First
凡涉及：
- ACTIVE 文件集合  
- doc_key 合法性  
- 治理等級 bucket（A+/A/B/C；B+/C+ 的 bucket 化）  
- 版本有效性（version_date / 治理狀態 狀態）  

一律以 **DOCUMENT_INDEX 的 Authoritative Index 表格**裁決為準。

---

## A2. 治理標籤（S/B+/C+）法律定位回歸（Label/Sub-Label）

### A2.1 S（Supreme Canon）為 Label，不構成治理等級
凡本文件或其引用語境提及「MASTER_CANON（S）」：
- **S 一律視為敘事/版本標籤（Label）**  
- MASTER_CANON 之治理等級 bucket/ACTIVE 狀態/doc_key 仍以 DOCUMENT_INDEX 表格裁決為準（通常為 A）

### A2.2 B+ / C+ 為 Sub-Label，其 bucket 分別回歸 B / C
凡本文件或其引用語境提及「B+」「C+」：
- 一律視為子級顯示標籤（Sub-Label）  
- 覆蓋規則不變：A+ > A > B > C  

兼容處理（不改原文）：既有標籤文字保留；其法律效力由本節限定。

---

## A3. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）

本文件內若出現任何「裁決順序字串」或箭頭序列（例如：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`）：
- 一律視為閱讀/操作助記（Mnemonic）  
- 不得被用作覆蓋規則或裁決權重新分配  
- 若與 DOCUMENT_INDEX §3（覆蓋規則）或 §6（衝突裁決程序）產生張力：一律回到 DOCUMENT_INDEX（不可跳步）

---

## A4. 最終宣告（治理狀態 v1.0）

- MASTER_ARCH 內任何文件清單/數量一律視為 Snapshot；治理裁決一律回到 DOCUMENT_INDEX。  
- 治理標籤（S/B+/C+）不得被解讀為新治理層級；其 bucket 必須回歸 A+/A/B/C。  
- 缺少必要引用資訊時：依 DOCUMENT_INDEX §6 保守處置，並以 VERSION_AUDIT 留痕（audit_anchor 可用 `VA-METADATA_FIX-20251227-0015`）。

## 0. 文件地位聲明（不可省略）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）之最高母體憲法**，  
其法律位階高於所有模組、策略、流程、Agent、UI、執行層與 AI 行為。

**任何文件、程式、AI 回覆、Agent 推論，只要與本文件衝突：**
**一律以本文件為準，且視衝突方為「治理違規」。**

---

## 1. 不可動搖的核心排序（Supreme Priority Order）

TAITS 全系統之最終排序如下（不可更動）：

Human Sovereignty
→ Risk & Compliance (Supreme Veto)
→ Regime
→ Evidence
→ Strategy
→ Execution
→ Performance / Optimization

yaml
複製程式碼

### 1.1 強制解釋
- **人類主權**：AI 永不具最終決策權  
- **風險與合規**：可否決任何高績效策略  
- **Regime**：高於任何單一訊號或模型  
- **策略**：永遠只是「建議與假設」  
- **績效**：不能為任何違規辯護  

---

## 2. 人類主權（Human Sovereignty）鐵律

### 2.1 定義
TAITS 為 **Human-in-the-Loop 強制系統**。

### 2.2 禁止事項
- AI 不得：
  - 自動下單
  - 自動解除風控
  - 自動修改治理規則
- 不存在「完全無人值守交易」

### 2.3 違規判定
若任何模組、Agent、Prompt、文件出現：
- 「AI 自主決策」
- 「自動交易」
- 「系統自行判斷即可」

👉 **直接判定為 A 級治理違規**

---

## 3. Risk / Compliance 最高否決權（Supreme Veto）

### 3.1 否決權定義
Risk / Compliance 擁有跨層、跨模組、跨策略的**最高即時否決權**。

### 3.2 否決不需理由充分性
- 不需解釋績效
- 不需證明錯誤
- 只需符合風險或合規疑慮

### 3.3 禁止事項
- 不得以「長期績效」對抗否決
- 不得以「回測成功」解除否決

---

## 4. Regime 高於一切單一訊號

### 4.1 定義
Regime = 市場狀態母判斷（非策略、非指標）

### 4.2 強制規則
- Regime 不符 → 策略 **不得啟用**
- Regime 衝突 → 系統必須：
  - 降級策略
  - 或完全 BLOCK

### 4.3 禁止事項
- 不得「忽略 Regime」
- 不得「用策略反推 Regime」

---

## 5. Evidence 第一原則（Evidence-First）

### 5.1 定義
所有判斷必須來自 **可回放、可審計、可追溯** 的 Evidence。

### 5.2 Evidence 最低標準
- 來源明確
- 時點可重建
- 不可僅存在於記憶體

### 5.3 禁止事項
- 傳聞
- 主觀感覺
- 無法重現的經驗敘事

---

## 6. Strategy ≠ Execution（策略與下單嚴格分離）

### 6.1 Strategy 定位
Strategy 只允許輸出：
- proposal
- context
- risk_adjust
- avoid / observe

### 6.2 禁止事項
- 直接輸出：
  - 價格
  - 數量
  - 買賣方向
- 不得直連任何下單模組

---

## 7. Structure ≠ Strategy（結構不可升格）

### 7.1 結構系統定位
- 纏論 / 結構 / 型態  
  → **僅為結構描述語法**

### 7.2 結構允許輸出
- structure_state
- completeness_score
- conflict_flag
- warning

### 7.3 明確禁止
- 結構 = 買點
- 背離 = 反轉
- 中樞 = 突破

---

## 8. Annotation 永遠為 Non-Binding

### 8.1 定義
Annotation 僅供人類理解與語意對齊。

### 8.2 禁止事項
- Annotation 升格為條件
- Annotation 被程式解析
- Annotation 被用於回測或實盤

---

## 9. 最大完備＋累積式更新 演進鐵律（不可逆）

### 9.1 定義
TAITS 只允許「擴充」，不允許「刪減或弱化」。

### 9.2 不可逆條款
- 治理條款不可刪
- 否決權不可弱化
- 人類主權不可調降

---

## 10. AI 行為邊界（AI Behavior Boundary）

### 10.1 AI 允許行為
- 整理
- 分析
- 建議
- 風險提示

### 10.2 AI 禁止行為
- 自行定義新策略類型
- 自行修改治理文件
- 自行假設可執行性

---

## 11. 違規等級與處置（Enforcement）

### 11.1 違規等級
- **A 級**：觸碰人類主權、風控否決、治理鐵律
- **B 級**：越權推論、策略下單化
- **C 級**：文件簡化、語意誤導

### 11.2 處置原則
- A 級：立即停止、回滾、封鎖
- B 級：降級、重審
- C 級：文件修正

---

## 12. 與其他文件之關係（Hierarchy）

- MASTER_CANON
- ARCH_FLOW
- RISK_COMPLIANCE
- EXECUTION_CONTROL
- STRATEGY_UNIVERSE
- STRATEGY_FEATURE_INDEX
- UI_SPEC
- DOCUMENT_INDEX

---

## 13. 最終鎖定聲明（Final Lock）

**本文件一經標示為 ACTIVE + LOCKABLE，  
即視為 TAITS 永久治理母憲法。**

任何未來 AI、Agent、新對話：
- 不得重新解釋
- 不得簡化
- 不得繞過

---

（TAITS_MASTER_ARCHITECTURE｜母體總憲法與核心鐵律｜最大完備版 完）
---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`MASTER_ARCH`
- 版本狀態：ACTIVE（治理狀態 v1.0；最大完備＋累積式更新）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=MASTER_ARCH` + `canonical_filename=TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md`。  
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

## G5. 最終宣告（治理狀態 v1.0）

---

## 治理補強（已整合為正文）

對齊上位裁決：DOCUMENT_INDEX（A+）之「HUMAN SOVEREIGNTY｜最高裁決置頂條款」  

### A1. 定義（在本母法中的落地口徑）
- **人類最高決策者**：TAITS 專案之產品負責人／架構裁決者（Human Authority / Architecture Arbiter）。  
- **明確命令**：可被稽核回放之明示指令（須具備：發令者身份、時間戳、命令內容、引用 doc_key/章節定位、目的與風險告知）。  

### A2. 原則（不可阻擋，但必須留痕）
1) 當存在「人類最高決策者的明確命令」時：  
   - 系統之任何文件條款、Gate/Reason Code、Agent/AI 內規，**不得以程序性理由阻止命令生效**。  
   - 但必須以制度化方式完成：告警呈現、風險揭露、稽核留痕、可回放紀錄。  
2) 當不存在「明確命令」時：  
   - 系統依本母法既有之治理序位運作；風險與合規否決機制維持既有語義（可 STOP/RETURN/BLOCK）。  

### A3. 與「Risk & Compliance（Supreme Veto）」之關係（消歧義）
- 本母法既有之 **Risk & Compliance 最高否決權**，在「無人類明確命令」情境下保持完全效力。  
- 在「有人類最高決策者明確命令」情境下：  
  - Risk/Compliance 必須輸出完整否決理由與風險告知（可升級至最高等級告警），  
  - 但其結果 **不得轉為阻止人類明確命令之執行**；改以「強制揭露＋雙重確認＋全紀錄」承接。  

### A4. 最小留痕欄位（可直接貼用）
凡屬人類最高決策者之明確命令，至少需記錄：

- authority_role = Human Sovereignty（人類最高決策者）  
- authority_actor = <姓名/識別>  
- authority_time = <Asia/Taipei 時戳>  
- authority_command = <命令全文>  
- ref_doc_key = <DOC_KEY>  
- ref_section = <§ / Heading Path>  
- ref_purpose = <用途：rule_change / gate_override / deploy_decision / etc.>  
- risk_disclosure = <Risk/Compliance 提示摘要與引用>  
- acknowledgement = <確認紀錄（例如雙重確認）>


## 附錄 Z｜工程參考：本地運算環境基線（非治理裁決）

> 目的：保留已存在之工程端基線資訊，避免對話或文件遺失導致工具/AI 重新腦補硬體條件。
> 法律定位：本附錄不構成治理裁決規則；本地環境之正式制度以 `LOCAL_ENV`（doc_key=LOCAL_ENV）為準。

- 裝置：ASUS FX504GE（筆電）
- 作業系統：Windows 11
- CPU：Intel Core i7-8750H（6C/12T）
- 記憶體（RAM）：32GB（已升級）
- GPU：NVIDIA GeForce GTX 1050 Ti
- GPU VRAM：4GB
- 儲存：256GB SSD + 750GB HDD（依實際可用空間調整）
- 建議本地推理定位（在此硬體條件下）：
  - 優先：L11 稽核摘要、L1/L2 抽取與欄位化、L5 證據包整理（使用 3B–7B 量化模型）
  - 不建議本地硬扛：高品質長篇 L9 報告主力、重推理整合（可採雲端主力＋本地稽核/抽取池）

# 稽核區塊（Audit Section｜非正文）

> 本區塊為「本次融合更新」之留痕（Changelog／Hash Manifest／Scope／Audit Hand-off）。  
> 為避免新舊混讀：本區塊不參與正文裁決；正文以本檔案開頭至本區塊前之內容為準。

## A. Scope（適用範圍）
- scope_doc_key: MASTER_ARCH
- scope_files_output: TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260104.md
- scope_files_source: TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260102.md
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
4) 置頂補強全局定錨（人類主權＋L9/L10/L11 口徑），用於跨文件一致化（不改寫既有核心鐵律，只固定入口口徑）。

## C. Hash Manifest（指紋清單）
- hash_alg: sha256
- scope: BODY_ONLY（不含本稽核區塊）
- hash_value_sha256: 1a12c66d362d285e289238839d4cabce3aee5031622d952445b0a9210c153e4b

## D. Audit Hand-off（裁決承接）
- change_id: MA-FUSION-260104-0008
- authority_basis: HFI（人類最高決策者明確命令｜scope=MASTER_ARCH｜融合更新形成單一正文）
- governance_order_applied: DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- downstream_notes:
  - 後續更新 AI_GOV 與其他制度文件時，若涉及主權、越權、裁決權、L9/L10/L11 定錨，需以本文件為憲法級邊界同步對齊。
- rationale: 以單一正文消除補片式混讀來源，同時維持母體憲法級條款之最大完備與一致裁決能力，確保全系統越權防線可被穩定承接。
