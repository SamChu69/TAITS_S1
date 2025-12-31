# TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220
doc_key：GOVERNANCE_STATE_FREEZE_V1  
治理等級：A（Governance State｜治理狀態裁決文件）  
適用範圍：TAITS 全系統（對所有 B/C 文件施加 Freeze v1.0 之變更門檻與 Only-Add 約束）  
版本狀態：ARCHIVED（已由 Freeze v1.1 取代；僅供追溯）  
版本日期：2025-12-20  
上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ AI_GOV（A+）  
平行參照：VERSION_AUDIT / GOVERNANCE_GATE_SPEC / DEPLOY_OPS  
變更原則：Only-Add（本文件為狀態宣告；任何狀態切換必須以「新 GOVERNANCE_STATE_* 文件」形式新增並納入 DOCUMENT_INDEX）  

> 【狀態提醒｜2025-12-31（Asia/Taipei）】本文件已退役；現行請以 `TAITS_GOVERNANCE_STATE__FREEZE_v1.1__251231.md`（ACTIVE）為準。

---

## 【L9–L11 最終定位｜B 路徑（全面重編）｜Binding】（生效日：2025-12-31（Asia/Taipei））

> 本段為 **TAITS 全文件宇宙之 L9–L11 統一定義（唯一有效口徑）**。  
> 任何文件中若存在與本段不一致之舊文描述，**一律視為歷史敘述（DEPRECATED／不參與裁決）**；不得被 AI/Agent 作為現行功能解讀依據。  
> 本段之目的：消除 AI 腦補、語義漂移、摘要化縮減、與層級混線（特別是 L9/L10/L11）。

### L9｜投資報告層（Investment Report Layer｜你可見、可追蹤、可版本化）
- **定位**：將 L1–L8 的多面向資訊（消息/基本/技術/籌碼/策略候選/風險合規結論）整合為「**可閱讀、可追蹤、可更新**」的標的投資報告。
- **必備輸出（最少集合）**：
  1) **結論摘要**（不含下單指令）  
  2) **關鍵數據與圖形**：以「數據表/指標快照 + 圖形引用（或渲染結果）」呈現（例如均線/RSI/MACD、區間統計、事件時間線）。  
  3) **進出場價格建議（非下單）**：以「區間/條件式」給出（例如進場區間、停損/停利區間、失效條件、更新觸發）。  
  4) **情境與風險**：哪些事件/價量/籌碼變化會導致需改判、提早出場、或轉為觀望。  
  5) **標的化追蹤（Dossier）**：必須具備 `instrument_id / report_id / version / timestamp / trigger_set`，以支援後續事件更新與連續報告（不是一次性解說）。
- **禁止**：
  - 直接下單、直接發送委託、或輸出「必須買/必須賣」之指令語句（那屬 L10 人類裁決與授權）。
  - 將 L9 降格為「只講人話、不含數據/圖形/追蹤」之單次解說。

### L10｜人類裁決層（Human Decision Authority｜交易授權在此）
- **定位**：由人類最高決策者做最終裁決，決定系統下一步模式：  
  `NO_ACTION / WATCH / BACKTEST / SIMULATION / PAPER / SEMI_AUTO / FULL_AUTO`（以及其授權邊界）
- **交易的開始點**：任何「下單/執行」皆必須建立在 **L10 的明確授權封套（Trade Authorization Envelope）** 之上；未授權則不得執行。
- **必備輸出（最少集合）**：
  - 選擇的模式 + 理由（引用 L9 報告章節定位）
  - 授權邊界：資金/風險上限、允許的策略/委託類型、有效期限、撤銷條件
  - 風險/合規之 PASS/VETO 結果與理由碼（若適用）
- **禁止**：
  - 以 L10 取代風險與合規否決權（否決權仍可阻止自動化執行，但不得阻止人類發出命令本身；執行面仍需留痕與明確承擔）。

### L11｜工程稽核層（Engineering Audit & System Review｜全層回放、雙料輸出）
- **定位**：L11 是「工程稽核／回放／可追溯」用途，**不是下單層、不是分析層、不是投資報告層**。
- **稽核範圍**：不只稽核 L10；而是 **L1–L11 每一層** 都必須留痕，才能檢視層級設計是否合理、是否需調整。
- **雙料輸出（同時必須存在）**：
  1) **人類可讀（Management View）**：用你看得懂的方式描述「本次流程發生了什麼、為何如此、關鍵證據與關鍵風險」。  
  2) **工程可用（Engineering View）**：可被系統回放的工件索引（artifact index）、版本與 hash、模型路由（model_id/版本/溫度/上下文）、輸入輸出摘要、事件時間線、錯誤與重試紀錄。
- **禁止**：
  - 把 L11 當成執行/下單入口。
  - 只留工程 log 而不產出你看得懂的稽核摘要（或反之）。

### 舊口徑處置（強制消歧）
- 若文件中仍出現「L9 = Governance Gate / L11 = Execution」等舊描述：一律標示為 **DEPRECATED**，不得作為現行解讀。

## 0. 文件定位（State Declaration）

本文件為 TAITS 的「治理狀態宣告文件」，用於宣告：

- 當前治理狀態 = **Freeze v1.0**
- Freeze v1.0 對「文件變更」之最小限制與門檻
- Freeze v1.0 與 Only-Add 的適用邊界（避免誤解為可任意改寫）

本文件不定義（避免越權）：
- 不定義任何交易策略、不定義下單、不定義風控/合規細節（其裁決仍以各母文件為準）
- 不重排治理等級覆蓋規則（A+ > A > B > C 由 DOCUMENT_INDEX 裁決）

---

## 1. Freeze v1.0 宣告（Binding）

### 1.1 Freeze v1.0 生效
自本文件版本日期起，TAITS 進入：

- `GOVERNANCE_STATE = Freeze v1.0`

### 1.2 適用範圍
Freeze v1.0 對下列文件之「變更方式」生效：

- 所有 **B / C** 治理有效文件（以 DOCUMENT_INDEX｜Authoritative Index 表格為準）
- 對 **A / A+** 文件：不得以 Freeze v1.0 作為弱化或改寫之理由（A/A+ 之變更仍須走其既有最嚴門檻）

---

## 2. Freeze v1.0 期間的變更規則（Hard Rules）

### 2.1 Only-Add 強制
Freeze v1.0 期間：

- **只可新增（Only-Add）**
- 禁止：刪減／覆寫／偷換語義／摘要化導致語義縮減
- 若需修補歧義、補充引用口徑、補充稽核欄位：以「新增章節 / 附錄 / Addendum（Only-Add）」方式處理

### 2.2 結構性變更禁止（Structural Change Ban）
Freeze v1.0 期間，禁止下列變更（即使以新增方式也不允許）：

- 新增或調整治理位階（A+/A/B/C）之覆蓋規則
- 變更 Canonical Flow（L1–L11）之順序或語義（MASTER_CANON 為準）
- 變更 Risk/Compliance 最高否決權（RISK_COMPLIANCE 為準）
- 變更 Execution 安全機制（EXECUTION_CONTROL/DEPLOY_OPS 為準）

### 2.3 版本與稽核必備（Audit Anchor Required）
任何在 Freeze v1.0 期間的新增內容，必須：

- 可定位到 ref_doc_key / ref_file / ref_version / ref_section
- 於 VERSION_AUDIT 留存變更帳本（至少：change_id、範圍、理由、批准者、影響面）

---

## 3. 狀態切換規則（Freeze → Unfreeze）

### 3.1 狀態切換不得覆寫本文件
未來若需解除 Freeze v1.0：

- 必須新增新文件：`TAITS_GOVERNANCE_STATE__UNFREEZE_vX.Y__<date>.md`
- 並在 DOCUMENT_INDEX 內完成 ACTIVE 切換（同 doc_key 僅能一份 ACTIVE）
- 本文件不得被覆寫；僅能由新狀態文件「覆蓋其效力」

### 3.2 保守處置
如狀態切換文件缺失、或 ACTIVE 切換不完整：

- 一律視為 Freeze v1.0 仍生效（保守處置）

---

## 4. 最終宣告（Final）

- Freeze v1.0 生效：B/C 文件僅可 Only-Add。
- 任何牴觸：以 DOCUMENT_INDEX §6（衝突裁決程序）處置。
- 本文件之角色為「狀態宣告」，不創造新治理權力。

（TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220｜ACTIVE）
