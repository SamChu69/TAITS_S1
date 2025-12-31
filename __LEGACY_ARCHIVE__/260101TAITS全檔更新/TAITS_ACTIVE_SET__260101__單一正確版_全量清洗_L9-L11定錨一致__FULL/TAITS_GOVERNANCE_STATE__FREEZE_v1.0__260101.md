# TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220
doc_key：GOVERNANCE_STATE_FREEZE_V1
治理等級：A（Governance State｜治理狀態裁決文件）
適用範圍：TAITS 全系統（對所有 B/C 文件施加 Freeze v1.0 之變更門檻與 Only-Add 約束）
版本狀態：ACTIVE（Freeze v1.0 生效）
版本日期：2026-01-01
上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ AI_GOV（A+）
平行參照：VERSION_AUDIT / GOVERNANCE_GATE_SPEC / DEPLOY_OPS
變更原則：Only-Add（本文件為狀態宣告；任何狀態切換必須以「新 GOVERNANCE_STATE_* 文件」形式新增並納入 DOCUMENT_INDEX）

## L9–L11 最終語義定錨（單一正確版｜必須一致）

> 本節為 TAITS 在 L9／L10／L11 的**唯一正確語義**。  
> 任何文件中若出現與本節不一致之描述，視為舊錯口徑（不得保留於單一正確版）。

### L9｜投資報告（Investment Report｜可追蹤、可更新、可稽核）
L9 的產出定位為「**給人看的完整投資報告**」，不是一次性的口頭解說；必須可在後續事件/行情變動下持續更新並可追溯。
L9 最低交付物應包含（不限於）：
- **標的化**：標的識別、觀測起點、追蹤狀態（open/hold/watch/exit-candidate 等）、版本號與時間戳。
- **數據**：對應 L1–L8 的關鍵數據表（消息/基本/技術/籌碼/風險/制度），含來源、取樣時間、缺漏註記。
- **圖形**：至少包含價格走勢與關鍵技術指標狀態視覺化（例如均線、RSI、MACD；以「狀態」呈現，非主觀敘事）。
- **進出場建議（非下單）**：建議區間/觸發條件/失效條件（停損/停利/風險撤退），並明確標示「此為建議，不構成下單」。
- **情境更新（Regime/Event）**：當市場制度/事件/風險狀態改變，需能產生增量更新（delta）並保留回放鏈。
- **可稽核鏈**：引用到 L11 的 record_id / ledger_id（或等價識別），以確保報告可被回放與驗證。

### L10｜人類裁決與交易授權（Human Decision & Authorization｜唯一決策點）
L10 的定位為「**人類最高決策者的最終裁決介面與授權層**」。  
- **最終決策者永遠是人類**：你決定採取何種模式與是否授權交易。
- L10 可裁決/授權的動作包含（不限於）：**不動作／回測／模擬／半自動／全自動**。
- AI/Agent 在 L10 僅能提供「選項、理由、風險揭露與建議」，**不得自行構成下單行為**；下單/執行屬於 L10 授權後由執行控制規範承接。

### L11｜工程稽核與全層回放（Engineering Audit & Replay｜全層留痕）
L11 的定位為「**工程檢視與稽核回放層**」，不是下單層，也不是只記錄 L10。
- **全層留痕**：L11 必須覆蓋 L1–L11 每一層的關鍵輸入/輸出/裁決/否決/變更理由與時間戳。
- **雙料輸出**：同一筆紀錄需同時具備  
  1) 人話可讀（你能看懂，用於檢視系統是否合理）  
  2) 工程可用（可重現、可驗證、可追溯，用於開發/稽核/回放）
- **目的**：用來檢查每一層的功能是否合理、是否需要調整、以及自動/半自動/全自動在不同時點的決策依據是否一致可回放。


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