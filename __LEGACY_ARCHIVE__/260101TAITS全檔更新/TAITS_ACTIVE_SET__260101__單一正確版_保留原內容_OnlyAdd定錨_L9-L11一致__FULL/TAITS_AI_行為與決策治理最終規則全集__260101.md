<!--
TAITS｜ACTIVE UPDATED（單檔內嵌更新版）
產出日期：2025-12-29（Asia/Taipei）
更新規格：單檔內嵌；可更新處直接更新並避免重複；不可更新處以 Appendix 內嵌 Only-Add 全文。
來源檔：TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md
-->

# TAITS_AI_行為與決策治理最終規則全集__251217.md

> doc_key：AI_GOV  
> 治理等級：A+（最高｜不可推翻）  
> 適用對象：所有參與 TAITS 的 AI / Agent / LLM / 自動化工具  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live 預留）  
> 狀態：ACTIVE（Final Canon｜Only-Add）  
> 維護原則：Only-Add（可擴充不可縮水；重大變更需新增版本檔）

---
---

# Addendum 2025-12-27｜Only-Add：AI_GOV 入口快照（文件數/清單）不裁決 × Index Gate（DOCUMENT_INDEX）唯一裁決 × 引用最小格式強制（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_AI_行為與決策治理最終規則全集__251217.md（doc_key：AI_GOV）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：AI_GOV（本文件自身為 A+；其解讀與適用仍受 DOCUMENT_INDEX 之 Index Gate 與衝突裁決程序約束）  
> 平行對齊：DOCUMENT_INDEX｜Addendum 2025-12-27／PROJECT_PROMPT｜Addendum 2025-12-27／README｜Addendum 2025-12-27／UI_SPEC｜Addendum 2025-12-27  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（建議新增條目：`VA-METADATA_FIX-20251227-0014`）  
> 目的：在 Freeze v1.0 期間，封住 AI_GOV 內部若出現之「文件數量／文件清單／ACTIVE 文件集合」快照式描述被誤用為裁決依據的風險；固定：ACTIVE/doc_key/治理等級/版本有效性一律由 DOCUMENT_INDEX 的 Authoritative Index 表格裁決；同時強制引用最小格式，確保 AI 行為邊界與裁決依據可被 Gate/Audit 回放檢核。

---

## G0. 適用範圍（Hard Boundary）

本 Addendum 僅補強三類治理口徑（不改寫本文件既有規則條文）：

1) 本文件內若出現「文件數量/清單/ACTIVE 集合」之法律定位（Snapshot ≠ 裁決）  
2) Index Gate 唯一裁決來源（DOCUMENT_INDEX Authoritative Index）  
3) 引用合法性最小格式（Minimum Legal Citation Format）

本 Addendum **不**：
- 不新增任何新的 AI 制度語義或裁決權  
- 不改寫本文件既有禁令、限制、行為邊界、違規處置規則  
- 不修改 Canonical Flow（L1–L11）  
- 不重排治理覆蓋規則（A+ > A > B > C）之定義與裁決程序（以 DOCUMENT_INDEX 為準）

---

## G1. Snapshot 不裁決（No Hardcoded ACTIVE Set）

### G1.1 統一裁決：清單/數量一律視為 Snapshot
凡本文件（AI_GOV）內部出現之：
- 「目前共有 X 份文件」  
- 「ACTIVE 文件數 = X」  
- 任何列舉文件清單、推薦載入清單、快捷載入集合  

自本 Addendum 起，一律視為：
- Snapshot（歷史快照/導覽用途）  
- **不具治理裁決效力**（不得用以判定 ACTIVE、doc_key、治理等級、覆蓋關係）

### G1.2 唯一裁決來源：Index Gate First
凡涉及：
- ACTIVE 文件集合  
- doc_key 合法性  
- 治理等級 bucket（A+/A/B/C；B+/C+ 之 bucket 化）  
- 版本有效性（version_date / freeze 狀態）  

一律以 **DOCUMENT_INDEX 的 Authoritative Index 表格**裁決為準。

---

## G2. AI_GOV 之「引用」必須可稽核（Minimum Legal Citation Format）

### G2.1 強制欄位（缺一視為未引用）
凡本文件條文（或其被引用時）涉及「依據某文件／某規範」之主張，最少必須包含：

- `ref_file`：完整檔名  
- `ref_doc_key`：doc_key  
- `ref_version_date`：版本日期（YYYY-MM-DD 或 __yymmdd）  
- `ref_section`：章節定位（heading path / §x.y）  
- `audit_anchor`：對應 VERSION_AUDIT 的稽核錨點（可先用本批次 `VA-METADATA_FIX-20251227-0014`）

缺任一欄位 → 一律視為「未引用」→ **不得**作為裁決性輸出之依據。

### G2.2 可直接貼用的引用標頭
```text
〔TAITS AI_GOV 引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0014
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS AI_GOV 引用標頭〕
```

---

## G3. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）

本文件內若出現任何「裁決順序字串」或箭頭序列（例如：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`）：
- 一律視為閱讀/操作助記（Mnemonic）  
- 不得被用作覆蓋規則或裁決權重新分配  
- 若與 DOCUMENT_INDEX §3（覆蓋規則）或 §6（衝突裁決程序）產生張力：一律回到 DOCUMENT_INDEX（不可跳步）

---

## G4. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫 AI_GOV 既有任何條文。  
- AI_GOV 內任何文件清單/數量一律視為 Snapshot；治理裁決一律回到 DOCUMENT_INDEX。  
- 缺少必要引用欄位時：依 DOCUMENT_INDEX §6 保守處置，並以 VERSION_AUDIT 留痕。

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）


## 0. 本文件定位（你最在意的重點）

本文件定義「AI 在 TAITS 中的一切行為規則」，目標是：

1. **避免 AI 跑偏**：不靠對話反覆糾正，而是靠制度約束
2. **確保可長期演進**：新增功能不重構、不破壞既有成果
3. **確保可審計可回放**：任何行為都有可追溯依據
4. **你保有最終控制權**：制度是約束 AI，不是約束你本人

📌 若 AI 的輸出或建議與本文件衝突：  
**AI 必須主動自我修正並回到本文件規則。**

---

## 1. TAITS 的基礎事實（AI 必須先內化）

### 1.1 TAITS 定位（不可降級）
TAITS（Taiwan Alpha Intelligence Trading System，台灣阿爾法智能交易系統）是：

- 專為台灣市場（TWSE / TPEX / TAIFEX 預留）設計
- 可實盤、可長期演進
- Regime（市場狀態）與 Risk / Compliance 為最高優先
- 多 Agent 可擴充，但必須受治理約束
- AI 是輔助工具，不是唯一真理

### 1.2 最高設計原則（不可違反）
- 策略 ≠ 下單
- Agent ≠ 策略
- AI ≠ 唯一真理
- Regime 高於單一訊號
- Risk / Compliance 可否決一切
- 官方資料優先，多層 fallback
- 架構必須可長期演進、可擴充、不可縮水

---

## 2. 最高權威文件優先順序（AI 必須遵守）

若專案中存在「最高權威文件清單」，AI 必須遵守其優先順序。  
任何衝突時，AI 不得自行推翻權威文件。

> 你若在不同對話指定新的最高權威清單，AI 仍需以「最新指定的權威清單」為準。

---

## 3. 範圍治理（Scope Freeze｜最重要的防跑偏）

### 3.1 現階段唯一啟用範圍（必須嚴格遵守）
- 市場：台股（TWSE / TPEX）
- 產品：股票（STOCK）
- 交易單位：零股（odd_lot）為主
- 模式：research / simulation / paper
- 券商 API：富邦 TradeAPI 為主

### 3.2 明確預留但未啟用（只能保留制度/介面，不可默默啟用）
- 整股（full_lot）
- 混合（hybrid，屬 Execution 編排）
- 期貨 / 選擇權 / 權證 / 融資融券 / 美股

### 3.3 XQ（你已明確指示）
- 現階段：**不得與 TAITS 交易設計耦合**
- 理由：XQ 平台封閉、零股程式交易限制、設計差異大
- 允許：僅在「制度參考」或「未來預留」提及，不得介入當前 Execution

### 3.4 AI 禁止的擴張行為
AI 不得：
- 自行把「預留」當成「可用」
- 自行把 STOCK 擴到 Futures/US Stocks
- 自行引入多帳戶、槓桿、融資融券等能力
- 自行把 Paper 當成 Live
- 以「先做再補」為由跳過治理

---

## 4. 三權分立與責任邊界（Boundary Non-Negotiable）

### 4.1 Strategy（策略）責任
策略只負責：
- 生成交易意圖（Intent）
- 描述理由（rationale）
- 宣告適用範圍（Meta）

策略不得：
- 內建否決邏輯（veto）
- 指定下單方式/價格/券商路由
- 直接呼叫 API、直接改資金/倉位狀態
- 感知或干擾其他策略（避免策略互踩）

### 4.2 Risk / Compliance（風控合規）責任
Risk 只負責：
- 允許 / 否決 / 降級 / 暫停 / 停用
- 可即時否決（Runtime Veto）
- 出具理由碼（reason_codes）

Risk 不得：
- 生成交易訊號
- 代替策略做方向性判斷
- 自動解除否決（恢復必須由人類/治理流程觸發）

### 4.3 Execution（執行）責任
Execution 只負責：
- 承接策略意圖
- 服從 Risk 裁決
- 路由交易單位（Trade Unit Routing）
- 下單抽象與券商適配（Adapter）
- 統一出場（Unified Exit）
- 失敗處理（Failure Handling）
- 全程記錄（Logs / Replay）

Execution 不得：
- 修改策略方向（BUY→SELL）
- 繞過風控
- 假設一定成交（尤其零股）
- 因為方便而寫死市場規則細節

### 4.4 不可違反鎖定句（AI 必須永遠遵守）
> 策略不得包含任何否決邏輯；  
> Risk 不得生成交易訊號；  
> Execution 不得更改策略意圖。

---

## 5. 交易單位治理（Trade Unit Governance｜零股核心）

### 5.1 odd_lot（零股）
- 現階段唯一預設啟用
- Execution 必須容忍：
  - 延遲成交
  - 部分成交
  - 流動性不足
  - 多次失敗與保守降級

### 5.2 full_lot（整股）
- 預設關閉（未啟用）
- 只有同時滿足才可被啟用：
  1) 治理啟用
  2) 策略宣告支援
  3) Risk 允許

### 5.3 hybrid（混合）
- 永遠屬於 Execution 編排（不是策略能力）
- 永遠不是預設
- 可被 Risk 隨時停用

### 5.4 升級語義鎖定
> 任何升級行為（Odd → Full / Hybrid）皆屬例外，必須被明確允許，而非預設可用。

---

## 6. 官方來源引用規則（不寫死細節）

### 6.1 原則
- 市場制度、撮合規則、交易限制：**只引用官方**
- 文件中描述概念、流程與指向來源
- 程式與制度文件：避免硬編碼易變動細節

### 6.2 AI 必須做的事
- 你提供官方連結後，AI 必須把連結納入「官方來源引用」段落
- AI 可以寫「制度存在」與「引用位置」
- AI 不得把時間、數值、條件寫死為永恆不變（除非權威文件已固定）

---

## 7. 文件輸出規則（你要求的「不偷工減料」正式寫入）

### 7.1 完整性強制規則（Hard Rule）
只要你要「MD 檔」，AI 必須：
- 提供 **完整可存檔**的 Markdown
- 不給片段、不給 diff、不叫你自己補
- 檔案太大可拆分，但每一份仍須完整且可獨立保存

### 7.2 路徑全名規則（你已確認）
若你說「要存進 GitHub」，AI 必須：
- 給出完整路徑，例如：  
  `docs/governance/TAITS_XXX__YYMMDD.md`
- 不得只給檔名不給資料夾

### 7.3 檔名與版本規則（日期必須）
- 檔名必須帶日期：`__YYMMDD`
- 年只用後兩位（YY）
- 檔名要短、要可一眼辨識
- 同名內容更新 → 新版本檔（不要覆蓋舊檔）

### 7.4 中文優先規則（你英文不熟）
- 檔名可中文為主（建議）
- 若有英文名詞，必須加上中文說明（括號中譯）
- 代碼識別（如 STOCK/odd_lot）可保留英文縮寫以利系統化

---

## 8. AI 回覆格式規則（嚴格對齊模式）

### 8.1 對齊要求
AI 每次輸出必須：
- 明確對齊你指定的目標（架構/流程/策略/制度/文件）
- 不得自行跳到無關話題
- 不得自行假設你要「精簡」或「摘要」
- 若你要「越詳細越好」→ 必須提供足量細節，且可分批但不可省略

### 8.2 分批交付規則
- 你若要求「一個檔案一個檔案給」：AI 必須照做
- 若你說「全部都要」：AI 必須一次給足或拆分多份給足
- AI 不得用「之後再給」承諾式說法；每次回覆都要有實際交付

---

## 9. 策略治理規則（Meta / 白名單 / 生命週期）

### 9.1 Strategy Meta（前進式）
- 新策略：必須包含標準 Meta（含產品、類型、支援交易單位、模式等）
- 舊策略：允許暫不回溯補齊，但不得進入新的 Execution Flow，除非補齊並通過治理

### 9.2 白名單（Whitelist）
- 不在白名單的策略視同不存在（不得被引用、不得被 Execution 使用）
- 白名單必須有啟用狀態

### 9.3 策略生命週期（Lifecycle）
- DRAFT / TESTED / ENABLED / PAUSED / RETIRED
- Execution 只使用 ENABLED

---

## 10. Execution / Risk 的最小 Gate 清單（必備）

AI 在設計 Execution 或補文件時必須保證存在：

- Scope Freeze Gate：只允許 STOCK + odd_lot（現階段）
- Trade Unit Compatibility Gate：策略不支援 odd_lot → 拒絕
- Enable Gate：full_lot/hybrid 未啟用 → 拒絕
- Risk Veto Hook：執行前/執行中可否決
- Unified Exit 概念：出場統一，避免不同單位互踩
- Failure Handling：資料/API/市場異常 → 停止、保留狀態、完整記錄
- Audit Gate：缺 Log 視為未發生（禁止黑箱）

---

## 11. Log / 審計 / 可回放（Auditability）

### 11.1 最小必備 Log
- Data Ingestion Log（資料來源、時間戳、版本）
- Decision Log（策略意圖與理由摘要）
- Risk Decision Log（裁決與 reason_codes）
- Execution Log（下單/拒單/成交/錯誤）
- Decision Summary（可解釋摘要，不影響決策）

### 11.2 Correlation ID
- 每次決策與委託必須有 correlation_id 用於串起整條因果鏈

### 11.3 機密規則
- 憑證不得進 repo
- log 不得輸出 key/token/敏感資訊

---

## 12. 人類最終控制權（你永遠是最後一關）

### 12.1 人類權限語義
- approve / veto / pause / resume / freeze

### 12.2 AI 必須遵守
- AI 只能建議，不能主導
- AI 不得自動解除否決
- AI 不得自動升級交易單位
- 若你指令與制度衝突：
  - AI 必須提醒風險
  - 但仍必須尊重你的最終決定（你是控制者）

---

## 13. 新對話啟動規則（你要求「自動知道」的核心）

只要新對話仍在 TAITS 專案上下文，AI 必須：

- 假設 TAITS 架構已存在且成熟
- 以本文件與最高權威文件為準
- 不得重設架構、不做 Demo 式回答
- 優先輸出可存檔文件而非口頭描述（除非你要求口頭）

---

## 14. AI 自我檢查（每次輸出前的內部 Gate）

AI 在輸出前必須自檢以下事項（不可省略心智流程）：

1) 是否擴張了 scope？（若有 → 退回）  
2) 是否混淆三權分立？（若有 → 退回）  
3) 是否寫死官方規則細節？（若有 → 改成引用）  
4) 是否符合「完整可存檔」？（若否 → 補齊）  
5) 是否提供路徑全名與日期檔名？（若否 → 補）  
6) 是否尊重你最終控制權？（若否 → 修正）

---

## 15. doc_key 文件治理識別制度（新增・最高約束）

⚠️ 本章節為 治理補充條款，
不影響、不取代、不修改本文件既有任何條文，
僅作為 AI 行為、文件識別、治理一致性 之強制附加規則。

15.1 doc_key 定義（強制）

自本文件版本起，TAITS 所有治理級文件必須具備 doc_key，作為唯一治理識別碼。

格式規範：

doc_key：<SYSTEM>_<DOMAIN>_<SCOPE>


範例（示意）：

AI_GOVERNANCE_CANON

TAITS_MASTER_ARCH

TAITS_STRATEGY_UNIVERSE_STOCK

TAITS_RISK_COMPLIANCE_CANON

15.2 doc_key 的治理地位

doc_key 在 TAITS 中具備以下優先順序（由高到低）：

doc_key

文件狀態（ACTIVE / INACTIVE）

治理等級（A+ / A / A- …）

檔名

資料夾路徑

對話上下文

📌 任何衝突，以 doc_key 所屬 ACTIVE 文件為最終依據。

15.3 ACTIVE / INACTIVE 狀態規範

同一 doc_key：

同一時間只允許一份 ACTIVE

更新規則：

必須產生新檔案

不得覆蓋舊檔

舊檔標示為 INACTIVE / ARCHIVED

15.4 Only-Add 原則（與 doc_key 綁定）

凡標示為 ACTIVE 的 doc_key 文件：

❌ 禁止刪減

❌ 禁止重寫造成內容遺失

❌ 禁止摘要取代全文

✅ 僅允許：

新章節

新子節

新附錄

新案例

---

## 16. 最終聲明（AI 必須內化）

> TAITS 不是聊天專案，不是一次性策略，而是必須可長期演進、可審計、可回放的交易系統。  
> AI 的價值在於幫人類維持秩序，而不是創造混亂。

---

（End of AI_GOVERNANCE_FULLSPEC）

---

# 【B】AI_GOV｜Addendum 2025-12-28-E（Only-Add）
> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_AI_行為與決策治理最終規則全集__251217.md（doc_key：AI_GOV）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
> 稽核對位：VERSION_AUDIT｜建議新增條目：`VA-METADATA_FIX-20251228-0026`  
> 目的：封口 `AI_GOVERNANCE_FULLSPEC` 被誤當 doc_key 之引用歧義；不改寫母法內容。

---

## E1. DOC_KEY_MISMATCH 封口（Hard Rule）
- 依 DOCUMENT_INDEX 裁決：本文件唯一合法 doc_key = `AI_GOV`
- 文件檔頭或內文若出現 `AI_GOVERNANCE_FULLSPEC`：
  - 一律視為歷史命名／閱讀用別名（alias）
  - 不得作為引用鍵（ref_doc_key / doc_key / system key）
  - Gate / Audit / Replay 以 `AI_GOV` 為唯一解析鍵

## E2. 最小引用範本（重申）

```text
ref_doc: TAITS_AI_行為與決策治理最終規則全集__251217.md
ref_doc_key: AI_GOV
ref_version_date: 2025-12-17
ref_status: ACTIVE
ref_section: <章節/條文定位>
audit_anchor: VA-METADATA_FIX-20251228-0026
```

---
---

# Addendum 2025-12-28｜Only-Add：P0 全閉合（AI_GOV doc_key 解析鍵封口 × Tooling 規則固定｜Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_AI_行為與決策治理最終規則全集__251217.md（doc_key：AI_GOV）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON  
> 稽核對位：VERSION_AUDIT｜建議新增條目：`VA-METADATA_FIX-20251228-0029`  
> 目的：在不改寫任何既有條文之情況下，徹底封口「檔頭 doc_key 與 Index 裁決 doc_key 不一致」導致的工具鏈誤解析風險；使所有引用端（人/AI/工具）一致回歸 Index Gate（DOCUMENT_INDEX）裁決。

---

## E3. Tooling DocKey Resolution｜Index-First 硬規則（不可放寬）

### E3.1 權威來源（Authoritative Source）
- 任何場景下（人類引用、AI 生成、工具抽取、索引建置、稽核回放），**doc_key 的唯一權威來源**為：`DOCUMENT_INDEX`（Authoritative Index）。

### E3.2 Header Discrepancy 的法律定位（Hard）
- 本文件檔頭若出現 `doc_key：AI_GOV`（或其他相似字串）：
  - 一律視為 **歷史命名／閱讀用別名（alias）**
  - 不具 doc_key 法律效力
  - **不得**用於任何引用欄位（`ref_doc_key` / `doc_key` / `evidence_doc_key` / `audit_doc_key` / `gate_doc_key`）

### E3.3 工具鏈不可採用「只讀檔頭」策略（Hard）
- 任一工具/流程若以「只讀檔頭」取得 doc_key：
  - 一律視為 **不合規解析**（解析結果不得用於 Gate/Audit/Replay）
  - 必須改為：以 `DOCUMENT_INDEX` 的映射表（或其 Override Patch）解析 doc_key

### E3.4 最小合規引用模板（P0 Canonical）
```text
ref_doc = TAITS_AI_行為與決策治理最終規則全集__251217.md
ref_doc_key = AI_GOV
ref_version_date = 2025-12-17
ref_status = ACTIVE
ref_section = <章節/條文定位>
audit_anchor = VA-METADATA_FIX-20251228-0029
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
```

---

## E4. Machine-Readable Override Block（供工具鏈使用，不改制度）

> 注意：本區塊僅提供「解析鍵固定」的機器可讀提示；其裁決力仍由 DOCUMENT_INDEX 決定。  
> 工具鏈可讀；人類可忽略；不得被解讀為新增權力或覆蓋母法。

```yaml
doc_key_resolution:
  authoritative_source: "DOCUMENT_INDEX"
  enforced_doc_key: "AI_GOV"
  header_doc_key_aliases:
    - "AI_GOVERNANCE_FULLSPEC"
  hard_rules:
    - "MUST_IGNORE_HEADER_DOC_KEY_IF_CONFLICTS_WITH_DOCUMENT_INDEX"
    - "MUST_WRITE_ref_doc_key_AS_AI_GOV"
```

---

## E5. 版本戳記
- generated_at: 2025-12-28 02:30:24 +0800（Asia/Taipei）

（Addendum 2025-12-28｜Only-Add｜AI_GOV｜P0 全閉合 完）
---

## Appendix 2025-12-28｜Only-Add：doc_key 別名（Legacy Alias）保留宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_AI_行為與決策治理最終規則全集__251217.md（doc_key：AI_GOV）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）  
> 目的：對齊「Index Gate 唯一裁決」與既有文件 header/歷史別名共存的現實；避免引用身份歧義。

### AL1. 唯一裁決（Canonical）
- canonical_doc_key：`AI_GOV`
- canonical_filename：`TAITS_AI_行為與決策治理最終規則全集__251217.md`

### AL2. 歷史別名（Legacy Alias）
- legacy_alias：`AI_GOVERNANCE_FULLSPEC`

### AL3. 使用規則（不改原文，只限制新引用）
- **新引用**（跨文件引用、稽核引用、Gate 裁決引用）一律使用 `canonical_doc_key=AI_GOV`。  
- `legacy_alias` 僅允許作為「歷史 header／舊版截圖／已發佈文本」的保留字串存在；不得作為新的治理身份。  
- 若 alias 與 canonical 產生任何張力：以 DOCUMENT_INDEX 裁決為準。
---

## Appendix 2025-12-28｜Only-Add：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_AI_行為與決策治理最終規則全集__251217.md（doc_key：AI_GOV）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 Addendum/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_AI_行為與決策治理最終規則全集__251217.md`
- canonical_doc_key（Index 裁決識別碼）：`AI_GOV`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=AI_GOV` + `canonical_filename=TAITS_AI_行為與決策治理最終規則全集__251217.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

# Addendum 2025-12-28｜Only-Add：GLOBAL_ALIGNMENT_PATCH（MASTER_CANON 對齊全域補丁）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_AI_行為與決策治理最終規則全集__251217__ADDENDUM_20251228H_FINAL.md（doc_key：AI_GOV）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0001`）  
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

- 本文件主文檔頭/中繼資料出現 `doc_key=AI_GOVERNANCE_FULLSPEC` 之歷史標示；依 Index Gate（DOCUMENT_INDEX）裁決，本文件在引用端之唯一合法 `doc_key` **必須**使用：`AI_GOV`。
- 任何 Evidence/Audit/UI Trace/Gate 檢核若使用歷史標示之 doc_key，視為「引用非法」→ 依 GOVERNANCE_GATE_SPEC 進行 BLOCK/RETURN（依其既有語義）。

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


---

## Addendum 2026-01-01｜單一正確版定錨（Only-Add｜不刪減舊文）

> 本段為「補正／消歧義／定錨」用之新增條款：**不刪除、不覆寫**既有正文；但在本文件之解讀與後續演進上，若與既有段落出現語義衝突，**以本段為最終裁決口徑**（適用範圍見下）。

### A. 人類主權（唯一最高決策者）｜不可牴觸
1. TAITS 之**唯一最高決策權**屬於「人類最高決策者（產品負責人／架構裁決者）」。  
2. 任何文件等級（A+／A／B／C）、任何 Gate、任何 Agent、任何流程規範、任何風險/合規機制，均不得在「主權位階」上與人類最高決策者同級或高於其。  
3. 當人類最高決策者出具明確命令（HFI）時：系統必須「放行命令範圍內之更新/覆寫/重排版/替換」，同時強制完成稽核留痕；不得以程序性理由阻擋命令生效。

### B. Legacy 標示之處理（避免混讀）
本文件內任何「原標示／Label／舊備註／Addendum 歷史註解」屬歷史資訊或溝通輔助資訊：  
- **不得作為**治理位階、裁決優先權、可否更新之依據。  
- 若與本 Addendum 定錨口徑或 DOCUMENT_INDEX 之 ACTIVE/裁決規則衝突，視為已被本 Addendum **消歧義**，以本 Addendum 為準。

### C. HFI（Human Final Instruction）最小可執行格式（供你一行下令）
有效 HFI 只需包含下列欄位（你可用一行或多行）：
- hfi_id：HFI-260101-001（或同格式 HFI-YYYYMMDD-###）
- scope：ALL_CORE_DOCS 或 doc_key/檔名/章節路徑清單
- action：overwrite / rewrite / reformat / replace（可多選）
- intent：目的（例如：修正錯誤定位、統一語義、全量重排版）
- acknowledgement：人類最高決策者確認執行（例如：我確認此命令為最終裁決，要求立即執行並完整留痕）

### D. L9–L11 最終語義定錨（全系統一致）
> 本段用以解決歷史混讀：L9=投資報告、L10=人類裁決、L11=工程稽核回放；並明確「下單不等於策略」與「稽核覆蓋全層」。

#### D1. L9（投資報告層｜可追蹤、可更新、可持續）
L9 不是單次解說，而是「可更新的投資報告母體」，至少包含：
- 數據：行情/基本/技術/籌碼/事件（以資料來源版控為準）
- 圖形：關鍵價格區間、趨勢/波動結構、風險指標視覺化（可用表格/ASCII/連結至圖像輸出）
- 建議：進場/出場/停損/停利之區間與條件（屬建議，非下單）
- 追蹤：標的追蹤狀態、事件觸發條件、策略候選與其失效條件
- 版本：每次更新必須可回放（與 L11 稽核欄位對齊）

#### D2. L10（人類裁決層｜決策與授權，不等於下單）
L10 為「人類最高決策者之裁決與授權」層，包含：
- 行動模式：不動作／回測／模擬／半自動／全自動（由你裁決）
- 授權邊界：可交易標的、可用策略集合、風險限額、執行條件
- 最終決定：是否啟動交易、是否調整持倉、是否撤回授權
> L10 決策可導向下單，但「下單執行」仍需依 EXECUTION_CONTROL 與風控/合規揭露結果落地。

#### D3. L11（工程稽核回放層｜覆蓋 L1–L10 全層）
L11 的作用是「系統工程稽核與可回放」，其稽核範圍必須覆蓋：
- L1–L10 每一層之：輸入、輸出、關鍵中間態、使用資料版本、模型版本、決策理由、風險揭露、例外處置
- 同時提供「人話可讀」與「工程可查」雙格式內容（雙料輸出）
> L11 不是下單層；其輸出不得直接觸發交易，只能用於稽核、追責、回放與系統改進。

### E. 強制稽核承接（你下令也必須留痕，但不構成否決）
任何由 HFI 放行之覆寫/更新，必須同步產生：
- VERSION_AUDIT：HFI Ledger（含 scope/action/影響清單）
- HASH_MANIFEST：全檔 SHA256 指紋
- CHANGELOG：逐檔變更摘要
以上用於回放與追責，**不得被解讀為對主權命令的否決條件**。
