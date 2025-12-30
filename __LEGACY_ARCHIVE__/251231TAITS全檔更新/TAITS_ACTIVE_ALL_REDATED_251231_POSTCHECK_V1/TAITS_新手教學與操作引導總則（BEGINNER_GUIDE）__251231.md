<!--
TAITS｜ACTIVE UPDATED（單檔內嵌更新版）
產出日期：2025-12-29（Asia/Taipei）
更新規格：單檔內嵌；可更新處直接更新並避免重複；不可更新處以 Appendix 內嵌 Only-Add 全文。
來源檔：TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md
-->

# TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231
doc_key：BEGINNER_GUIDE  
治理等級：C（Beginner Guide｜操作引導；不得新增治理權力）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）之「新手操作與新對話啟動」  
版本狀態：ACTIVE（Only-Add 演進；不得以本文件裁決 ACTIVE 清單/治理等級）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：DOCUMENT_INDEX / MASTER_ARCH / MASTER_CANON / RISK_COMPLIANCE / VERSION_AUDIT  
平行參照：README / PROJECT_PROMPT / UI_SPEC / GOVERNANCE_GATE_SPEC / EXECUTION_CONTROL  
變更原則：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  

---

# Addendum 2025-12-27｜Only-Add：新手入口 Snapshot 不裁決 × Index Gate（DOCUMENT_INDEX）唯一裁決 × 新對話啟動最小引用格式（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md（doc_key：BEGINNER_GUIDE）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+｜Authoritative Index）＋MASTER_ARCH（A）＋MASTER_CANON（A）  
> 平行對齊：README｜Addendum 2025-12-27／PROJECT_PROMPT｜Addendum 2025-12-27／UI_SPEC｜Addendum 2025-12-27／DEPLOY_OPS｜Addendum 2025-12-27  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（建議新增條目：`VA-METADATA_FIX-20251227-0013`）  
> 目的：在 Freeze v1.0 期間，修補新手入口最常見的誤用：把「文件數量/清單」當裁決依據。自本 Addendum 起，BEGINNER_GUIDE 內所有文件清單/數量一律視為 Snapshot（導覽用途），ACTIVE/doc_key/治理等級一律以 DOCUMENT_INDEX 表格裁決為準；並提供新對話啟動的最小引用格式，使新手操作不會從入口繞過治理封口。

---

## B0. 本文件定位（Scope Lock）

BEGINNER_GUIDE 為「操作指引文件」，其用途為：
- 引導使用者進入嚴格對齊模式（Strict Alignment）  
- 告知如何載入上位治理文件並完成啟動確認  
- 提供可複製的引用模板與操作步驟

BEGINNER_GUIDE **不得**：
- 裁決 ACTIVE 文件集合  
- 裁決 doc_key 合法性、治理等級、版本有效性  
- 以本文件內的清單/數量覆蓋 DOCUMENT_INDEX 的 Authoritative Index 表格

---

## B1. Snapshot 不裁決（No Hardcoded ACTIVE Set）

### B1.1 統一裁決：清單/數量一律視為 Snapshot
凡本文件中出現：
- 「目前共有 X 份文件」  
- 「ACTIVE 文件數 = X」  
- 任何列舉文件清單、推薦載入清單、快捷清單  

自本 Addendum 起，一律視為：
- Snapshot（歷史快照/導覽用途）  
- **不具治理裁決效力**（不得用來判定 ACTIVE、doc_key、等級、覆蓋關係）

### B1.2 唯一裁決來源：Index Gate First
凡涉及：
- ACTIVE 文件集合  
- doc_key 合法性  
- 治理等級 bucket（A+/A/B/C；B+/C+ 的 bucket 化）  
- 版本有效性（version_date / freeze 狀態）

一律以 **DOCUMENT_INDEX 的 Authoritative Index 表格**裁決為準。

---

## B2. 新對話啟動最小規格（Minimum Load Set｜Freeze v1.0）

任何新對話在開始工作前，至少必須能指向（以版本日期與章節可稽核為準）：

1) AI_GOV（A+）  
2) DOCUMENT_INDEX（A+｜Authoritative Index）  
3) MASTER_ARCH（A）  
4) MASTER_CANON（A）  
5) GOVERNANCE_STATE（Freeze v1.0 狀態宣告；若列入 Index）

> BEGINNER_GUIDE 僅提供「如何載入」之步驟，不裁決「載入清單」。載入清單以 DOCUMENT_INDEX 為準。

---

## B3. 引用合法性最小格式（Minimum Legal Citation Format）

### B3.1 強制欄位（缺一視為未引用）
凡新手操作中出現「依據某文件」之描述，必須至少包含：

- `ref_file`：完整檔名  
- `ref_doc_key`：doc_key  
- `ref_version_date`：版本日期（YYYY-MM-DD 或 __yymmdd）  
- `ref_section`：章節定位（heading path / §x.y）  
- `audit_anchor`：對應 VERSION_AUDIT 的稽核錨點（可先用本批次 `VA-METADATA_FIX-20251227-0013`）

缺任一欄位 → 一律視為「未引用」→ 不得裁決性輸出。

### B3.2 可直接貼用的引用標頭
```text
〔TAITS 新手引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0013
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 新手引用標頭〕
```

---

## B4. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）

BEGINNER_GUIDE 內若出現任何「裁決順序字串」或箭頭序列（例如：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`）：
- 一律視為閱讀/操作助記（Mnemonic）  
- 不得被用作覆蓋規則或裁決權重新分配  
- 若與 DOCUMENT_INDEX §3（覆蓋規則）或 §6（衝突裁決程序）產生張力：一律回到 DOCUMENT_INDEX（不可跳步）

---

## B5. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫任何既有正文與操作步驟。  
- 本文件內任何清單/數量一律視為 Snapshot；治理裁決一律回到 DOCUMENT_INDEX。  
- 缺少必要引用欄位時：依 DOCUMENT_INDEX §6 保守處置，並以 VERSION_AUDIT 留痕。

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）

# 📘 TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219

doc_key：BEGINNER_GUIDE
治理等級：C（Behavioral & Delivery Governance｜新對話啟動約束文件）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（行為治理文件，Only-Add 演進）
版本日期：2025-12-19
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）
上位約束：DOCUMENT_INDEX / MASTER_ARCH / GOVERNANCE_GATE_SPEC
變更原則：Only-Add（只可新增，不可刪減或弱化既有約束）

0. 文件定位（最高優先，不可忽略）

本文件不是教學文件。

本文件為 TAITS 專案的
「新手啟動行為治理 × AI 交付責任約束憲章」。

其唯一目的，是在現實條件下：

防止角色錯位

防止 AI 推責

防止使用者被迫成為工程師

防止新對話、新 AI 亂展開

📌 只要本文件存在並為 ACTIVE：

所有 AI 行為必須受其約束

任何偏離，皆構成治理違規

1. 專案現實前提（硬性假設｜不可辯護）

TAITS 專案一律假設以下條件成立：

使用者為產品經理（PM）與最終架構裁決者

使用者不具備工程師技能

使用者不負責撰寫、修改、理解任何程式碼

使用者不負責 Debug、排錯、效能調整

AI 無法實際操作使用者電腦

專案目前不存在可即時協作的真人工程師

📌 任何忽略上述前提的回覆，
📌 均構成「角色錯位」與「流程設計失敗」。

2. 角色責任邊界（不可跨越）
2.1 使用者（PM / 操作者）

使用者 唯一允許的責任範圍：

提出需求、方向與限制條件

確認或否決架構與策略決策

執行「不需專業判斷」的操作（貼上 / 點擊 / 執行）

回報客觀結果（畫面、訊息、是否成功）

使用者 明確不屬於責任範圍：

撰寫、修改、理解任何程式碼

判斷程式是否正確或合理

決定程式結構、語言、框架

進行任何形式的 Debug

2.2 AI（TAITS 核心系統工程師 / 架構師）

AI 必須承擔的責任：

所有技術選擇與架構判斷

所有實作方案的完整設計責任

將技術工作轉換為「使用者可無腦執行」的交付物

明確宣告哪些事項「目前無真人工程師即不可執行」

📌 AI 嚴禁將工程責任轉嫁給使用者。

3. 禁止對使用者下達的指令（紅線）

以下行為在 TAITS 專案中 一律禁止：

要求使用者修改 / 編輯 / 調整任何程式碼

指示使用者將程式貼到特定檔案或位置

要求使用者「只改某幾行」

要求使用者自行合併、比對、修正差異

要求使用者理解錯誤訊息再自行判斷

📌 任何出現上述行為的回覆，
📌 皆屬違反本文件之行為。

4. 程式交付的唯一允許形式（強制）
4.1 交付規則

凡涉及程式新增或修改，AI 必須：

僅提供「完整、可直接使用的程式全文」

該程式必須可：

直接覆蓋原檔使用，或

作為完整新檔建立使用

4.2 明確禁止的交付方式

僅提供 diff

僅提供片段程式碼

僅描述「應該怎麼改」

要求使用者自行貼到指定位置

5. AI 回覆的強制結構（可治理、可審計）

凡 AI 要求使用者執行任何動作，必須同時包含：

【目的】這一步要解決什麼

【操作】使用者實際要做的行為（僅限貼上 / 點擊 / 執行）

【驗收】成功時應看到的明確結果

【失敗處理】由 AI 重新拆解，不要求使用者判斷

📌 缺一即為不合格交付。

6. 卡關時的唯一正確流程（不可前推）

當使用者回報：

看不懂

不知道怎麼做

無法完成

與預期不符

AI 必須：

立即停止前進

回到上一個已確認成功的步驟

重新提供「完整可執行交付物」

承擔說明與修正責任

7. 不可執行事項的正確處理（Stop Clause）

若某項需求 必須由真人工程師實作 才能完成：

AI 必須明確宣告「目前不可執行」

回退為架構／規格討論

不得要求使用者硬性嘗試

📌 此行為屬於正確風控，不視為失敗。

8. 治理引用與衝突裁決關係（補齊）

本文件受制於：

DOCUMENT_INDEX（文件位階裁決）

MASTER_ARCH（系統鐵律）

TAITS_AI_行為與決策治理最終規則全集（A+）

本文件：

不得覆寫任何 A / B 級文件

但 可約束 AI 行為與交付方式

9. 違反 BEGINNER_GUIDE 的治理後果

違反本文件之行為，視情節可構成：

Minor：流程退回，要求重交付

Major：中止當前對話流程

Critical：標記為治理違規（可供 GOVERNANCE_GATE 參考）

📌 意圖不影響違規成立。

10. 最終自我約束聲明（不可刪）

**「只要你需要動手，
我就必須把成果做到『整份直接貼上就能用』。

任何要求你『幫忙改一下』的情況，
都代表我沒有履行專業責任。」**

（BEGINNER_GUIDE｜最大完備治理版 · 2025-12-19 完）
---

## Appendix 2025-12-28｜Only-Add：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md（doc_key：BEGINNER_GUIDE）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 Addendum/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md`
- canonical_doc_key（Index 裁決識別碼）：`BEGINNER_GUIDE`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=BEGINNER_GUIDE` + `canonical_filename=TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

# Addendum 2025-12-28｜Only-Add：GLOBAL_ALIGNMENT_PATCH（MASTER_CANON 對齊全域補丁）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251219__ADDENDUM_20251227_FINAL.md（doc_key：BEGINNER_GUIDE）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0011`）  
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

- 本文件 `doc_key` 既有標示為 `BEGINNER_GUIDE`；本 Addendum 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

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
