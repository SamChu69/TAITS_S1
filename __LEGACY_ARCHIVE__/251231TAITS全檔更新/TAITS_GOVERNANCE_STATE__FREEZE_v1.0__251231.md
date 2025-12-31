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
