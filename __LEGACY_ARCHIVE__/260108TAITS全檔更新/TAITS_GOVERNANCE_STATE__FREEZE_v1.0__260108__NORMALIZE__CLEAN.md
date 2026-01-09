# TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260108（正文乾淨｜最大完備覆蓋版）

doc_key：GOVERNANCE_STATE  
治理等級：A（治理狀態文件｜FREEZE v1.0）  
適用範圍：TAITS 全專案（治理狀態宣告、是否允許結構性變更、融合更新作業界線、封存/上線門檻）  
版本狀態：ACTIVE（單一正確正文版）  
版本日期：2026-01-08（Asia/Taipei）  
裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（最終裁決序位；本檔僅宣告治理狀態，不得與之衝突）  
平行參照：VERSION_AUDIT／GOVERNANCE_GATE_SPEC／MASTER_CANON  
變更原則：正文不得混入留痕；稽核四件套（Changelog／Hash Manifest／Scope／Audit Hand-off）一律置於檔尾「稽核區塊（非正文）」。

---

## 0. 文件定位（State Declaration）

本文件為 TAITS 的「治理狀態宣告文件」，用於宣告當前治理狀態為 **FREEZE v1.0**，並對 TAITS 全系統施加預設保守門檻，以避免：

- 非必要的結構性變更造成語義漂移與跨文件混讀  
- 未經稽核承接的「縮水／摘要化」取代原文  
- 在無人類明確命令（HFI）時，任意覆寫或刪減既有制度內容  

TAITS 的唯一最高主權始終屬於人類最高決策者；本文件不得被曲解為限制人類最高決策者之明確命令（見 §1.1 與 §1.3）。

---

## 1. 全局定錨｜單一口徑（S1）

### 1.1 SOVEREIGNTY｜人類最高決策者主權（不可牴觸）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接，不得卡死更新。

### 1.2 Canonical Flow 承接（不重複定義）
- L1–L11 之層級定義與 Canonical Flow：一律以 doc_key=MASTER_CANON 為唯一正文來源。
- 本檔僅宣告「治理狀態」與「變更邊界」：不得跳過治理/稽核邊界、不得以任何方式繞過人類裁決路徑與稽核承接要求。

### 1.3 HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：治理狀態/Gate 不得阻擋 scope 範圍內之融合更新／覆寫修正／重排版／全量替換；並必須同步完成稽核承接（VERSION_AUDIT 留痕、Hash Manifest、Changelog）。

---

## 2. FREEZE v1.0 預設規則（Default Constraints）

### 2.1 適用文件層級
- 對所有 **B／C 治理文件**：在無有效 HFI 時，適用本節「預設保守門檻」。
- 對 A/A+ 文件：其變更由 DOCUMENT_INDEX 與 VERSION_AUDIT 之規則約束；治理狀態不得被曲解為「禁止母法更新」，但在無 HFI 時仍應採保守策略並遵守 Index/Gate 與稽核要求。

### 2.2 預設允許（無 HFI 時｜非破壞性變更）
在 FREEZE v1.0 下，對 B/C 文件之「預設允許」僅限下列 **非破壞性** 變更型態：

1) **新增**章節／條款／附表／附錄（不造成既有內容失效或被隱形替換）  
2) **補強**更清楚的定義、邊界說明、例外處理、操作步驟（不得改寫既有規則語義）  
3) **補齊**稽核欄位與留痕格式（不得刪減既有留痕要求）  
4) **重排版**僅限版面與索引（章節順序、標題層級、列表格式），不得改動規則語義；若有任何語義影響，視同覆寫修正，必須走 HFI（見 §1.3）。

> 重要：FREEZE v1.0 期間禁止以「摘要化／精華版」取代原文。  
> 未被新內容**明確取代**者，必須保留並持續累積；僅當新內容已對舊內容形成明確取代關係時，方可在正文中以新版本取代舊段落，但必須以 VERSION_AUDIT 與指紋清單完成稽核承接。

### 2.3 預設禁止（除非 HFI Override）
在 FREEZE v1.0 下，對 B/C 文件預設禁止：

- 靜默刪除既有內容（含移除段落、刪減條款、刪掉關鍵限定語）  
- 靜默覆寫既有段落（含改寫既有語義、替換既有規則、刪改條款適用範圍）  
- 以「重排版」之名實質改動規則語義  
- 未完成稽核承接即進行大幅度版本替換（例如：全量融合重寫、單一正確正文收斂但未完成指紋/變更帳本）

---

## 3. 狀態切換（State Transition）與保守處置（Conservative Handling）

### 3.1 狀態切換必備條件（Switch Requirements）
若要切換治理狀態（例如：UNFREEZE／新的治理狀態版本），必須同時滿足：

1) **新增**一份新的 `TAITS_GOVERNANCE_STATE_<STATE>_vX.Y__<date>.md`  
2) 在 `DOCUMENT_INDEX` 中納入該文件，並完成 **ACTIVE 唯一性切換**  
3) 在 `VERSION_AUDIT` 留下變更帳本（change_id、理由、範圍、影響清單、指紋清單引用）

### 3.2 保守處置（Conservative Handling）
如狀態切換文件缺失、或 ACTIVE 切換不完整：

- 一律視為 FREEZE v1.0 仍生效（保守處置）

---

## 4. 最終宣告（Final）

- FREEZE v1.0 生效：B/C 文件在無有效 HFI 時，預設採保守門檻（禁止靜默刪減與靜默覆寫；禁止摘要縮水）。  
- HFI Override 生效：當 Valid HFI 存在時，治理狀態不得阻擋 scope 內之融合更新／覆寫修正／重排版／全量替換；必須同步完成稽核承接。  
- 任何牴觸：以 DOCUMENT_INDEX 之衝突裁決程序處置；但任何文件與流程不得高於人類最高決策者之唯一主權。  
- 本文件之角色為「狀態宣告」，不創造新治理權力；其約束不得被曲解為限制人類最高決策者主權。

# 稽核區塊（Audit Section｜非正文）

## A. Scope（適用範圍）
- 文件：doc_key=GOVERNANCE_STATE（FREEZE v1.0）
- 適用範圍：TAITS 全專案（治理狀態宣告、結構性變更邊界、融合更新作業界線、封存/上線門檻）
- 本次覆蓋版目標：正文乾淨、無重複、無混讀；不新增制度語義、不縮水摘要；僅去重收斂與結構/格式正常化。

## B. Changelog（變更清單）
- 2026-01-08：NORMALIZE｜移除正文中與 MASTER_CANON 重複之 L9–L11 定義；刪除重複主權段落；移除 Legacy/片段附錄；重整章節結構並維持 FREEZE v1.0 規則完整性；更新版本日期與指紋。

## C. Hash Manifest（指紋清單）
- BODY_SHA256：`e91791ec24e14a6cd4ddecd6f28d03a61da85fbab136a9d63caeb1600d5c7f98`
- 計算範圍：自檔首起至（不含）本段標題 `# 稽核區塊（Audit Section｜非正文）` 之前之全文，採 UTF-8 編碼，含最後一個換行字元。

## D. Audit Hand-off（裁決承接）
- 本文件僅宣告治理狀態與變更邊界；不得與最終裁決序位牴觸。
- 最終裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV。
- Canonical Flow（L1–L11）之正文定義來源：doc_key=MASTER_CANON。
