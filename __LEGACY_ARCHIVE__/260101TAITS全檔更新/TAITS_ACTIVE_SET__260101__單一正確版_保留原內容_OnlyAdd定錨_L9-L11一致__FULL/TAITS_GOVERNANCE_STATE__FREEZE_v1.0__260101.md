# TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220
doc_key：GOVERNANCE_STATE_FREEZE_V1  
治理等級：A（Governance State｜治理狀態裁決文件）  
適用範圍：TAITS 全系統（對所有 B/C 文件施加 Freeze v1.0 之變更門檻與 Only-Add 約束）  
版本狀態：ACTIVE（Freeze v1.0 生效）  
版本日期：2025-12-20  
上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ AI_GOV（A+）  
平行參照：VERSION_AUDIT / GOVERNANCE_GATE_SPEC / DEPLOY_OPS  
變更原則：Only-Add（本文件為狀態宣告；任何狀態切換必須以「新 GOVERNANCE_STATE_* 文件」形式新增並納入 DOCUMENT_INDEX）  

---

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
