# TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）

- doc_key：BEGINNER_GUIDE
- 基線日期：2026-01-06（Asia/Taipei）
- 版本定位：單一正確正文版／最終覆蓋版（RE-EDIT · NO-NOTE）
- 治理裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV

---

doc_key：BEGINNER_GUIDE  
治理等級：C（操作／啟動級｜新手教學與操作引導總則）  
適用範圍：TAITS 使用者操作、對話開啟、檔案更新流程、工程 Phase 使用方式與常見錯誤避免  
版本狀態：ACTIVE（單一正確正文版｜最大完備＋累積式更新）  
版本日期：2026-01-06（Asia/Taipei）  
裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（最終裁決序位）  
本檔性質：操作／啟動級指引（不得重新分配裁決權；不得覆寫上位治理文件）  
平行參照：TAITS_PROJECT_PROMPT／Unified Process Anchor／UI_SPEC／VERSION_AUDIT／GOVERNANCE_GATE_SPEC  
變更原則：最大完備＋累積式更新（允許融合更新／覆寫修正／重排版以形成單一正確正文；禁止摘要化縮水；未被新版本明確取代之有效內容一律保留並持續累積；已被新版本明確取代者可自正文移除但必須由稽核留痕承接）

---

## 全局定錨｜單一口徑（S1）

- 本文件為單一正確正文版；任何歷史狀態標記不構成正文裁決依據（以 DOCUMENT_INDEX／MASTER_ARCH／AI_GOV 為準）。  
- 本文件為操作引導；不構成策略/交易建議。  
- L9＝投資報告層；L10＝人類裁決與交易決策層；L11＝全層稽核回放層（非下單層）。  

---

## 啟動確認語（必貼）

- 開啟任何新對話前，請先貼上並要求 AI 僅回覆以下一句作為啟動確認：  
  「TAITS 架構已完整載入，我已準備好在此基礎上繼續開發。」

---

## 0. 文件定位（Beginner Guide）

本文件提供 TAITS 的「操作入口」與「對話/文件更新的標準流程」：
- 新對話啟動：如何載入治理文件、如何選擇模式（File Update Mode / Engineering Mode 等）。
- 文件更新：如何指定 doc_key、如何交付可覆蓋單一正文、如何輸出留痕（稽核區塊）。
- L1–L11 驗收：如何逐層驗收、如何判斷跳層與越權、如何要求 L9 報告含價格與追蹤欄位。
- 本文件為單一正確正文版；任何歷史狀態標記不構成正文裁決依據（以 DOCUMENT_INDEX／MASTER_ARCH／AI_GOV 為準）。

---

---


## 目錄（依序排列）

- 全局定錨｜單一口徑（S1）
  - 1. 人類最高決策者主權（SOVEREIGNTY）
  - 2. L9–L11 最終語義（跨文件一致）
  - 3. HFI｜人類明確命令（可執行觸發）
- 治理一致化條款（正文）
- B0. 本文件定位（Scope Lock）
- B1. Snapshot 不裁決（No Hardcoded ACTIVE Set）
  - B1.1 統一裁決：清單/數量一律視為 Snapshot
  - B1.2 唯一裁決來源：Index Gate First
- B2. 新對話啟動最小規格（Minimum Load Set｜以 GOVERNANCE_STATE 現況為準（本文件為單一正確正文版；任何歷史狀態標記不構成正文裁決依據（以 DOCUMENT_INDEX／MASTER_ARCH／AI_GOV 為準）。
- B3. 引用合法性最小格式（Minimum Legal Citation Format）
  - B3.1 強制欄位（缺一視為未引用）
  - B3.2 可直接貼用的引用標頭
- B4. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）
- B5. 最終宣告（以 GOVERNANCE_STATE 現況為準（本文件為單一正確正文版；任何歷史狀態標記不構成正文裁決依據（以 DOCUMENT_INDEX／MASTER_ARCH／AI_GOV 為準）。
- 治理一致化條款（正文）
  - A1. 本文件之唯一治理身份（Canonical Identity）
  - A2. 本專案目錄中的實體檔案（Physical Artifact）
  - A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 治理一致化條款（正文）
- G0. 適用範圍（Hard Boundary）
- G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）
- G2. 子級標籤（Label）之唯一合法解讀（S / B+ / C+）
- G3. DATA_UNIVERSE（alias）封口（資料治理引用回歸 DATA_SOURCES）
- G4. 最小可稽核引用格式（Minimum Legal Citation Format｜可直接貼用）
- G5. 最終宣告（以 GOVERNANCE_STATE 現況為準（本文件為單一正確正文版；任何歷史狀態標記不構成正文裁決依據（以 DOCUMENT_INDEX／MASTER_ARCH／AI_GOV 為準）。

---


## 全局定錨｜單一口徑（S1）

### 1. 人類最高決策者主權（SOVEREIGNTY）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接，不得卡死更新。

### 2. L9–L11 最終語義（跨文件一致）
- L9＝投資報告層（含數據/圖形/條件式進出場建議〔非指令〕/風險敘述/可追蹤更新欄位）
- L10＝人類裁決與交易決策層（唯一交易授權入口）
- L11＝全層工程稽核回放層（L1–L11 全留痕），且 L11 非下單層

### 3. HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：治理狀態/最大完備＋累積式更新（原 累積式更新 口徑已淘汰）/Gate 不得阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。

## 治理一致化條款（正文）

上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+｜Authoritative Index）＋MASTER_ARCH（A）＋MASTER_CANON（A）  

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

- Snapshot（歷史快照/導覽用途）  
- **不具治理裁決效力**（不得用來判定 ACTIVE、doc_key、等級、覆蓋關係）

### B1.2 唯一裁決來源：Index Gate First
凡涉及：
- ACTIVE 文件集合  
- doc_key 合法性  
- 治理等級 bucket（A+/A/B/C；B+/C+ 的 bucket 化）  
- 版本有效性（version_date / 治理狀態 狀態）

一律以 **DOCUMENT_INDEX 的 Authoritative Index 表格**裁決為準。

---

## B2. 新對話啟動最小規格（Minimum Load Set｜以 GOVERNANCE_STATE 現況為準（本文件為單一正確正文版；任何歷史狀態標記不構成正文裁決依據（以 DOCUMENT_INDEX／MASTER_ARCH／AI_GOV 為準）。

任何新對話在開始工作前，至少必須能指向（以版本日期與章節可稽核為準）：

1) AI_GOV（A+）  
2) DOCUMENT_INDEX（A+｜Authoritative Index）  
3) MASTER_ARCH（A）  
4) MASTER_CANON（A）  
5) GOVERNANCE_STATE（以 GOVERNANCE_STATE 現況為準（本文件為單一正確正文版；任何歷史狀態標記不構成正文裁決依據（以 DOCUMENT_INDEX／MASTER_ARCH／AI_GOV 為準）。

BEGINNER_GUIDE 僅提供「如何載入」之步驟，不裁決「載入清單」。載入清單以 DOCUMENT_INDEX 為準。

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
〔TAITS 新手引用標頭｜以 GOVERNANCE_STATE 現況為準（本文件為單一正確正文版；任何歷史狀態標記不構成正文裁決依據（以 DOCUMENT_INDEX／MASTER_ARCH／AI_GOV 為準）。
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

## B5. 最終宣告（以 GOVERNANCE_STATE 現況為準）

本文件為單一正確正文版；任何歷史狀態標記不構成正文裁決依據（以 DOCUMENT_INDEX／MASTER_ARCH／AI_GOV 為準）。


- 本文件內任何清單/數量一律視為 Snapshot；治理裁決一律回到 DOCUMENT_INDEX。  
- 缺少必要引用欄位時：依 DOCUMENT_INDEX §6 保守處置，並以 VERSION_AUDIT 留痕。

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 重新編輯：移除舊檔檔頭雜項標記與既有稽核片段，統一為單一正文入口與單一檔尾稽核區塊。
- 保留：正文規範內容全量承接，不做摘要縮水。

### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：2f18d9e3c220cfabdcd4635a12cd511b04e3ec08770bffc4ec5ed08b6874ec42

### 3) 適用範圍（Scope）
- 僅適用於本文件（本次 re-edit 排版與稽核邊界一致化）。

### 4) 裁決承接（Audit Hand-off）
- 若與其他治理文件存在衝突，裁決序位固定：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。
