# TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）

- doc_key：BEGINNER_GUIDE
- 治理位階：操作／啟動級（Behavioral & Delivery Governance｜新對話啟動與交付行為約束）
- 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
- 基線日期：（Asia/Taipei）
- 版本日期：（Asia/Taipei）
- 裁決序位（自高至低）：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
- Canonical Flow（L1–L11）：以 doc_key=MASTER_CANON 為唯一正文來源（本文件不重複定義層級語義）

---

## 目錄（依序排列）

- 啟動確認語（必貼）
- 0. 文件定位
- 稽核區塊（非正文）

---

## 啟動確認語（必貼）

> 「TAITS 架構已完整載入，我已準備好在此基礎上繼續開發。」

---

## 0. 文件定位

本文件為 TAITS「新手教學與操作引導總則」，其唯一職責為：

- 規定新對話啟動時之必備前提、引用邊界與交付方式，使所有對話輸出可被治理文件接納與稽核。
- 明確聲明 Canonical Flow（L1–L11）之唯一正文來源為 doc_key=MASTER_CANON；本文件不得重複定義或特別化任何層級語義（包含不得特別化 L9–L11）。
- 明確聲明裁決序位（自高至低）為：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV；若發生衝突，必須依序位裁決。

本文件屬於操作與行為治理文件，禁止承擔制度裁決或策略內容之新增、改寫與推導。

---

# 稽核區塊（Audit Section｜非正文）

## 1) 變更清單（Changelog）

- ：Final QA 正文化覆蓋版（移除箭頭順位與治理字母標籤；修正省略式占位；重整稽核四件套與指紋）。

## 2) 指紋清單（Hash Manifest）

---

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- FINAL_QA_FIX：重新計算並更新 BODY_SHA256（以稽核區塊標頭之前全文為計算範圍），確保稽核指紋可重現。
- FINAL_QA_NORMALIZE：移除正文中之占位符號（如「...」）與中段散落之 Hash 行，確保正文乾淨並將稽核四件套固定於檔尾（非正文）。
- FINAL_QA_NORMALIZE：依 HASH_RULE 重新計算並更新 BODY_SHA256，確保稽核指紋可重現。

### 2) Hash Manifest（指紋清單）
- HASH_METHOD：SHA-256（UTF-8，LF）
- BODY_SHA256：c7aaaf979fc23f868911ab7c0a237a2da777a200b8c388d51b93b83540435399
### 3) Scope（適用範圍）
- scope_doc_key：BEGINNER_GUIDE
- scope_files_output：TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__260113__FINAL_QA__NORMALIZE.md
- scope_mode：FINAL QA MODE（正文去重收斂／結構重排／正文乾淨化／檔尾稽核四件套固定）
- version_date：（Asia/Taipei）

### 4) Audit Hand-off（裁決承接）
- adjudication_chain：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- canonical_flow_source：MASTER_CANON
- note：本檔為 BEGINNER_GUIDE 現行唯一可引用正文；若與其他治理文件存在衝突，裁決序位固定為 DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。
