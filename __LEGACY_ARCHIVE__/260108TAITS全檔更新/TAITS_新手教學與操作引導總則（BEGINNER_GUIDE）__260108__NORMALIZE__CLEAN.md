# TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）

- doc_key：BEGINNER_GUIDE  
- 治理等級：C  
- 基線日期：2026-01-08（Asia/Taipei）  
- 版本日期：2026-01-08（Asia/Taipei）  
- 裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  
- Canonical Flow（L1–L11）：以 doc_key=MASTER_CANON 為唯一正文來源（本文件不重複定義層級語義）

---

## 目錄（依序排列）

- 啟動確認語（必貼）
- 0. 文件定位（Beginner Guide）
- 1. 本文件定位（Scope Lock）
- 2. Snapshot 不裁決（No Hardcoded ACTIVE Set）
- 3. 新對話啟動最小規格（Minimum Load Set）
- 4. 引用合法性最小格式（Minimum Legal Citation Format）
- 稽核區塊（Audit Section｜非正文）

---

## 啟動確認語（必貼）

- 開啟任何新對話前，請先貼上並要求 AI 僅回覆以下一句作為啟動確認：  
  「TAITS 架構已完整載入，我已準備好在此基礎上繼續開發。」

---

---

## 0. 文件定位（Beginner Guide）

本文件提供 TAITS 的「操作入口」與「對話／文件更新」之標準流程，用於協助使用者以一致方式：
- 開啟新對話並完成啟動確認
- 指定文件（doc_key）進行正文正常化（Normalize）與覆蓋交付
- 依治理序位進行問題裁決與可追溯留痕（稽核四件套）

本文件為操作指引，**不裁決** ACTIVE 文件集合、doc_key 合法性、治理等級與版本有效性；上述裁決一律以 doc_key=DOCUMENT_INDEX 之 Authoritative Index 為準。

---

## 1. 本文件定位（Scope Lock）

BEGINNER_GUIDE 為「操作指引文件」，其用途為：
- 引導使用者進入嚴格對齊模式（Strict Alignment）  
- 告知如何載入上位治理文件並完成啟動確認  
- 提供可複製的引用模板與操作步驟

BEGINNER_GUIDE **不得**：
- 裁決 ACTIVE 文件集合  
- 裁決 doc_key 合法性、治理等級、版本有效性  
- 以本文件內的清單/數量覆蓋 DOCUMENT_INDEX 的 Authoritative Index 表格

---

## 2. Snapshot 不裁決（No Hardcoded ACTIVE Set）

### 2.1 統一裁決：清單/數量一律視為 Snapshot
凡本文件中出現：
- 「目前共有 X 份文件」  
- 「ACTIVE 文件數 = X」  
- 任何列舉文件清單、推薦載入清單、快捷清單  

- Snapshot（歷史快照/導覽用途）  
- **不具治理裁決效力**（不得用來判定 ACTIVE、doc_key、等級、覆蓋關係）

### 2.2 唯一裁決來源：Index Gate First
凡涉及：
- ACTIVE 文件集合  
- doc_key 合法性  
- 治理等級（A+/A/B/C）  
- 版本有效性（version_date / 治理狀態 狀態）

一律以 **DOCUMENT_INDEX 的 Authoritative Index 表格**裁決為準。

---

## 3. 新對話啟動最小規格（Minimum Load Set）

任何新對話在開始工作前，至少必須能指向（以版本日期與章節可稽核為準）：

1) AI_GOV（A+）  
2) DOCUMENT_INDEX（A+｜Authoritative Index）  
3) MASTER_ARCH（A）  
4) MASTER_CANON（A）  
5) GOVERNANCE_STATE（治理狀態文件；以現行生效版本為準）  


BEGINNER_GUIDE 僅提供「如何載入」之步驟，不裁決「載入清單」。載入清單以 DOCUMENT_INDEX 為準。

---

## 4. 引用合法性最小格式（Minimum Legal Citation Format）

### 4.1 強制欄位（缺一視為未引用）
凡新手操作中出現「依據某文件」之描述，必須至少包含：

- `ref_file`：完整檔名  
- `ref_doc_key`：doc_key  
- `ref_version_date`：版本日期（YYYY-MM-DD 或 __yymmdd）  
- `ref_section`：章節定位（heading path / §x.y）  
- `audit_anchor`：對應 VERSION_AUDIT 的稽核錨點（由本次作業或治理裁決指定）

缺任一欄位 → 一律視為「未引用」→ 不得裁決性輸出。

### 4.2 可直接貼用的引用標頭
```text
〔TAITS 新手引用標頭〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = <VERSION_AUDIT 稽核錨點>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS 新手引用標頭〕
```

---

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 正常化：移除正文中之作業/補丁語彙、重複章節與混讀段落（包含：全局定錨 S1、治理一致化條款、子級標籤/助記順位、Legacy Snapshot）。
- 收斂：本文件僅保留「新手操作指引」必要內容；不在本文件內重複定義 L1–L11（層級語義一律以 MASTER_CANON 為準）。
- 修復：引用模板移除硬編碼稽核錨點，改為欄位化輸入。

### 2) 指紋清單（Hash Manifest）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：e81ba7c09b813e9f528953eb541ed9c215dd6b1ee85d52f9c3f30d8f11375f67

### 3) 適用範圍（Scope）
本次覆蓋版修正範圍僅限於 doc_key=BEGINNER_GUIDE：
- 正文章節去重、去混讀、結構重排與模板修正  
- 不新增其他文件之治理語義；不改寫上位文件裁決內容

### 4) 裁決承接（Audit Hand-off）
- 本檔為 BEGINNER_GUIDE 現行唯一可引用正文。  
- 若與其他治理文件存在衝突，裁決序位固定為：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。
