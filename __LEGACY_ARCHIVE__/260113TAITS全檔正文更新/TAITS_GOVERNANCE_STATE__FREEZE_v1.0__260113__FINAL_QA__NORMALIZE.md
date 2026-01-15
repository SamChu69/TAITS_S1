# TAITS_治理狀態宣告（GOVERNANCE_STATE）

- doc_key：GOVERNANCE_STATE
- 治理位階：治理狀態文件（FREEZE v1.0）
- 適用範圍：TAITS 全專案（治理狀態宣告、變更邊界、整編作業界線、封存與上線門檻）
- 版本狀態：ACTIVE（單一正確正文版）
- 版本日期：2026-01-11（Asia/Taipei）
- 基線日期：2026-01-11（Asia/Taipei）
- 裁決序位（自高至低）：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
- Canonical Flow（L1–L11）唯一正文來源：MASTER_CANON
- 平行參照：VERSION_AUDIT、GOVERNANCE_GATE_SPEC、RISK_COMPLIANCE、EXECUTION_CONTROL、DEPLOY_OPS

---

## 0. 文件定位（State Declaration）

本文件為 TAITS 治理狀態之唯一有效宣告，目的在於：

1. 明確宣告本專案目前處於 FREEZE v1.0 狀態。
2. 規範在 FREEZE v1.0 下允許與禁止的變更類型，以及最小稽核與留痕要求。
3. 提供跨文件一致的變更邊界，避免以「整理」「優化」「補強」之名改寫既有制度語義。

本文件不作為 Canonical Flow（L1–L11）之替代或補充正文；任何流程定義僅得引用 MASTER_CANON，其他文件亦不得在本文件要求下另行特別化 L9–L11 或任何子集合。

---

## 1. 治理狀態（FREEZE v1.0）之定義

FREEZE v1.0 表示：專案已進入制度穩定期，除符合本文件所列「允許變更類型」者外，禁止任何可能造成治理語義漂移、裁決序位漂移、或 Canonical Flow 口徑漂移之變更。

本狀態之核心精神：

- 優先維持既有制度條文之語義一致性與可追溯性。
- 允許必要的「正文化」與「一致性收斂」，但不得藉此引入新制度、改寫權限邊界、或重新分配最高否決權。
- Risk/Compliance 之最高否決權不得被削弱，亦不得以任何形式繞過治理 Gate 與人類裁決責任。

---

## 2. 變更分類與判定規則

### 2.1 何謂「結構性變更」（在 FREEZE v1.0 下禁止）

凡滿足任一條件，即屬結構性變更，於 FREEZE v1.0 下禁止：

1. 新增、刪除、合併、拆分任何治理文件之「治理位階」或其裁決效力描述。
2. 改寫裁決序位（DOCUMENT_INDEX、MASTER_ARCH、AI_GOV）之優先關係或適用條件。
3. 重新定義 Canonical Flow（L1–L11）之層級集合、輸入輸出、或將任何層級子集合特別化為「例外制度」。
4. 改變 Risk/Compliance、Execution、Governance Gate 之最高否決權、阻斷門檻、或其可追溯性要求。
5. 將任何非治理文件升格為治理裁決依據，或使 README、教學、定錨文件取得制度裁決效力。

### 2.2 何謂「非結構性變更」（在 FREEZE v1.0 下可允許）

在不觸及 2.1 的前提下，下列屬非結構性變更，得依 3. 章規範執行：

1. 正文正文化（FINAL QA）：去重收斂、結構重排、格式正常化、移除對話痕跡與補丁語句，但不得刪減制度條文。
2. 版本口徑一致性修復：檔名、版本日期、基線日期、ACTIVE 指向對齊，避免新舊混讀。
3. 稽核四件套修復：Changelog、Hash Manifest、Scope、Audit Hand-off 之欄位修正與一致化。
4. 明顯錯字、標點、排版修正（不改寫語義）。

---

## 3. FREEZE v1.0 下的變更流程（最小合規）

在 FREEZE v1.0 下，任何允許變更皆須滿足下列最小流程：

1. 變更以單一 doc_key 為單位提交，並可被「可直接覆蓋」之完整文件內容驗收。
2. 任何變更必須在檔尾保留稽核四件套，且 Hash Manifest 需可重算驗證。
3. 若變更涉及 ACTIVE 指向、檔名口徑、或跨檔引用口徑，須優先完成 DOCUMENT_INDEX 之收斂，避免混讀。
4. 如變更可能觸及風險、合規或執行控制門檻，應同時對照 RISK_COMPLIANCE 與 EXECUTION_CONTROL 之既有規範，不得造成否決權削弱。

---

## 4. 解封版（UNFREEZE）之最低門檻（宣告性要求）

本文件不直接啟動解封版；解封版必須由具最高裁決責任之人類角色依既有治理流程宣告，且至少滿足：

1. 已完成全專案的 Final QA 正文化收斂，並通過治理 Gate 稽核。
2. 版本控管與留痕機制（VERSION_AUDIT）可對所有變更提供可追溯鏈。
3. 風險與合規否決權在解封版後仍可行使且可稽核。

---

## 5. 裁決與衝突處理

若發生「本文件允許」與「其他治理文件禁止」之衝突，應依裁決序位（自高至低）解決；本文件僅為狀態宣告，不得用以反向改寫上位文件之語義。

---
## 稽核區塊（Audit Section｜非正文）

### 1) Changelog（變更清單）
- 2026-01-11（Asia/Taipei）：FINAL QA 正文化收斂（移除對話痕跡與占位符、對齊基線日期、補齊稽核四件套、重算正文指紋），不改寫制度語義。

### 2) Hash Manifest（指紋清單）
- hash_method：SHA-256
- body_sha256：eb9b7a9589fe4a649c6c174c6fe0f1e4dc641e9c7ac723767e579a45f217567b
- canonicalization：UTF-8、LF、正文包含結尾換行；Hash 計算範圍為「稽核區塊」之前全部內容。

### 3) Scope（範圍與不變量）
- scope_doc_key：GOVERNANCE_STATE
- scope_change_type：FINAL_QA（正文乾淨、去重收斂、結構與格式正常化、基線日期對齊）
- scope_files_output：TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260111__FINAL_QA__NORMALIZE.md
- scope_invariants：
  - 裁決序位維持：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
  - Canonical Flow（L1–L11）唯一正文來源維持：MASTER_CANON
  - Risk/Compliance 最高否決權不被削弱
  - FREEZE v1.0 之禁止邊界不被擴權或弱化（僅明文化與可維護化）

### 4) Audit Hand-off（裁決承接）
- governance_order_applied：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
- canonical_flow_anchor：MASTER_CANON（L1–L11）
- note：本檔僅宣告治理狀態與變更邊界；本稽核區塊屬非正文。
