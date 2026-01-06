# TAITS（README）

- doc_key：README
- 基線日期：2026-01-06（Asia/Taipei）
- 版本定位：單一正確正文版／最終覆蓋版（RE-EDIT · NO-NOTE）
- 治理裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV

---

# README__260106（單一正確正文版｜最終覆蓋版｜覆蓋輸出｜FINALQA_260106）

doc_key：README  
治理等級：C（操作／啟動級）  
版本基線：2026-01-06（Asia/Taipei）  
文件狀態：單一正確正文版（本檔可直接覆蓋使用）  
治理有效文件集合：以 doc_key=DOCUMENT_INDEX 之 Authoritative Index 為準（ACTIVE=21）  
最終裁決序位（不得自創）：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  

---

## 0. 本 README 的唯一職責（Scope Lock）

本 README 僅作為 **TAITS 專案入口導覽**，提供：
- 新對話啟動與最小閱讀順序提示（僅提示，不裁決清單）
- 核心語義定錨（S1）之入口版提醒（完整裁決以 MASTER_ARCH / AI_GOV 為準）
- 文件索引導覽（doc_key 對照與閱讀順序）
- 操作安全邊界提醒（避免越權、跳層、混讀）

**本 README 不構成治理裁決來源**；所有裁決與治理有效文件集合，一律以 DOCUMENT_INDEX 為準。

---

## 1. 全局定錨｜單一口徑（S1）

### 1.1 人類最高決策者主權（SOVEREIGNTY）
- 人類（產品負責人／架構裁決者）為 TAITS 的最高決策者（L10 唯一授權入口）。  
- AI / Agent 僅為輔助，**不得成為決策主體**。  
- Risk / Compliance 具最高否決權（依 RISK_COMPLIANCE）。

### 1.2 L9–L11 最終語義（跨文件一致｜禁止混讀）
- **L9＝投資報告層（Investment Report）**：含數據/圖形/條件式進出場建議（非指令）/風險敘述/可追蹤更新欄位。  
- **L10＝人類裁決與交易決策層（Human Decision & Trade Authorization）**：唯一交易授權入口。  
- **L11＝全層工程稽核回放層（Audit Replay, L1–L11 全留痕）**：L11 非下單層。

補充（避免誤讀）：
- Governance Gate（治理閘門）為 **non-layer 檢核機制**，主要作用是 **L9→L10** 的檢核/阻擋/退回（依 GOV_GATE_SPEC）。  
- Execution Control（交易執行與控制）為 **模組/制度**，僅能在 **L10 人類授權後** 被啟動；不得將其等同為 L11。

### 1.3 HFI｜人類明確命令（可執行觸發）
所有會導致「裁決」「版本狀態切換」「落地執行」的行為，必須由人類以明確命令（Human-First Instruction, HFI）觸發，且需可被稽核回放（依 AI_GOV／VERSION_AUDIT）。

---

## 2. 新對話啟動（必讀）

### 2.1 啟動確認語（新對話第一句）
你必須先回覆且只能回覆以下一句作為啟動確認：  
「TAITS 架構已完整載入，我已準備好在此基礎上繼續開發。」

### 2.2 新對話載入最小規格（Minimum Load Set）
- README 僅提示「載入方式」，不裁決「載入清單」；**載入清單以 DOCUMENT_INDEX 為準**。  
- 任何「文件數量／清單」一律視為 Snapshot（歷史快照，不具裁決力）。

---

## 3. 正確閱讀順序（入口提示）

### 3.1 最小必讀（不得跳過）
1) DOCUMENT_INDEX（Authoritative Index）  
2) MASTER_ARCH（母體總憲法與核心鐵律）  
3) AI_GOV（AI 行為與決策治理最終規則）  
4) GOVERNANCE_STATE（治理狀態：Freeze/Unfreeze/版本基線）  
5) MASTER_CANON（完整總架構×總流程×全資訊體系）

### 3.2 視需求擴展（在治理框架下）
- RISK_COMPLIANCE（風險與合規最高否決權）  
- GOV_GATE_SPEC / EXECUTION_CONTROL / VERSION_AUDIT  
- FULL_ARCH / ARCH_FLOW  
- DATA_SOURCES / TWSE_RULES  
- STRATEGY_UNIVERSE / STRATEGY_FEATURE_INDEX  
- UI_SPEC / DEPLOY_OPS / LOCAL_ENV  
- BEGINNER_GUIDE（操作引導）

---

## 4. 角色分工（強制遵守）
- 使用者（人類）：產品負責人／架構裁決者（不寫程式）。  
- AI（本助手）：核心系統工程師＋系統架構設計師＋量化研究員；僅在治理框架內提供可直接貼用之文件輸出與工程化內容。  
- Risk / Compliance：可否決一切（依 RISK_COMPLIANCE）。  

---

## 5. 使用本專案文件的基本規則（入口版）
- doc_key 為唯一識別：引用文件時以 doc_key 為準。  
- 不得跳層：策略 ≠ 下單；AI ≠ 決策主體；Regime 高於策略。  
- 去混讀：正文不得混入補丁式語句；留痕必須獨立於稽核區塊（或獨立稽核檔）。  

---

## 6. 引用合法性最小格式（Minimum Legal Citation Format）
為避免「有提到就算引用」的誤用，任何引用行為，最少必須包含：
- 文件名（完整檔名或 canonical_filename）  
- doc_key  
- 版本日期（version_date）  
- 章節定位（section / heading path）

缺任一欄位 → 一律視為「未引用」→ 不得裁決性輸出。

建議固定引用標頭（可直接貼用）：
```text
〔TAITS 引用標頭〕
ref_file = <完整檔名或 canonical_filename>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
〔/TAITS 引用標頭〕
```

---

## 7. 最終聲明（入口版，不可刪）
TAITS 的核心價值不在於「多聰明」，而在於：
- 不亂來
- 不越權
- 可回放
- 可追責
- 可長期演進

只要存在不可接受風險，就算錯過機會，也必須選擇不交易（裁決依 RISK_COMPLIANCE）。

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 重新編輯：移除舊檔檔頭雜項標記與既有稽核片段，統一為單一正文入口與單一檔尾稽核區塊。
- 保留：正文規範內容全量承接，不做摘要縮水。

### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：c0fb5b4033012f008bc5c83f5238dc5fea9febc77d2019474e1b0840e4304421

### 3) 適用範圍（Scope）
- 僅適用於本文件（本次 re-edit 排版與稽核邊界一致化）。

### 4) 裁決承接（Audit Hand-off）
- 若與其他治理文件存在衝突，裁決序位固定：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。
