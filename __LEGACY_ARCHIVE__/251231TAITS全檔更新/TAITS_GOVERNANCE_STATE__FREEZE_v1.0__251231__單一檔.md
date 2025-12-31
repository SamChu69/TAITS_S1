# TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220
doc_key：GOVERNANCE_STATE_FREEZE_V1  
治理等級：A（Governance State｜治理狀態裁決文件）  
適用範圍：TAITS 全系統（對所有 B/C 文件施加 Freeze v1.0 之變更門檻與 Only-Add 約束）  
版本狀態：ACTIVE（Freeze v1.0 生效）  
版本日期：2025-12-20  
最後修訂：2026-01-01（納入「人類主權＝唯一最高」之可執行例外條款）  
物理檔名：TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md（本文件之治理身份以本標頭為準；檔名差異僅屬物理映射）  
上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ AI_GOV（A+）  
平行參照：VERSION_AUDIT / GOVERNANCE_GATE_SPEC / DEPLOY_OPS  
變更原則：Only-Add（本文件為狀態宣告；任何狀態切換必須以「新 GOVERNANCE_STATE_* 文件」形式新增並納入 DOCUMENT_INDEX）  

---

## 0. 文件定位（State Declaration）

本文件為 TAITS 的「治理狀態宣告文件」，用於宣告當前治理狀態為 **Freeze v1.0**，並對 TAITS 全系統施加以下約束：

- **預設保守狀態**：以避免語義漂移、規格分叉、版本混讀與不可回放。  
- **B/C 文件預設僅允許 Only-Add**：不得覆寫、不得刪減、不得偷換既有語義。  
- **狀態切換必須可稽核**：必須以新 `GOVERNANCE_STATE_*` 文件新增並完成 `DOCUMENT_INDEX` 之 ACTIVE 切換；否則視為 Freeze 持續生效（保守處置）。  

> 注意：Freeze v1.0 的角色是「狀態門檻」，不是「最高權限」。  
> TAITS 的**唯一最高主權**始終屬於人類最高決策者；本文件不得被用來否決或阻止人類最高決策者之明確命令（見 §1）。  

---

## 1. HUMAN SOVEREIGNTY｜人類主權（唯一最高）

### 1.1 唯一最高主權（唯一性宣告）
TAITS 之最終裁決權 **唯一**屬於人類最高決策者（產品負責人／架構裁決者）。  
除人類最高決策者外，**不存在**任何同級或更高之「權限／裁決權」。任何文件等級（A+／A／B／C）、任何 Gate、任何 Agent/AI 內規、任何流程條款（含 Freeze/Only-Add）均不得在主權位階上與其並列、不得高於其。

---

## 2. Freeze v1.0 預設規則（Default Constraints）

### 2.1 適用文件層級
- 對所有 **B／C 治理文件**：預設僅允許 Only-Add。  
- 對 A/A+ 文件：其變更由 DOCUMENT_INDEX 與 VERSION_AUDIT 之規則約束；Freeze 不得被曲解為「禁止母法更新」，但在無 HFI 時仍應採保守策略並遵守 Index Gate。  

### 2.2 Only-Add（預設允許）
在 Freeze v1.0 下，對 B/C 文件之允許變更型態僅限：

- 新增章節／條款／附表／附錄  
- 新增更清楚的定義、邊界說明、例外處理（不得改寫既有語義）  
- 新增稽核欄位與留痕格式（不得刪減既有留痕要求）

### 2.3 預設禁止（除非 HFI Override）
在 Freeze v1.0 下，對 B/C 文件預設禁止：

- 刪除既有內容  
- 覆寫既有段落（包含改寫既有語義、替換既有規則、刪改條款的適用範圍）  
- 以「重排版」之名實質改動規則語義  
- 在未完成稽核留痕時進行大幅度版本替換

---

## 3. 狀態切換（State Transition）與保守處置（Conservative Handling）

### 3.1 狀態切換必備條件（Switch Requirements）
若要切換治理狀態（例如：UNFREEZE／新的 FREEZE 版本），必須同時滿足：

1) **新增**一份新的 `TAITS_GOVERNANCE_STATE__<STATE>_vX.Y__<date>.md`  
2) 在 `DOCUMENT_INDEX` 中納入該文件，並完成 **ACTIVE 唯一性切換**  
3) 在 `VERSION_AUDIT` 留下變更帳本（change_id、理由、範圍、影響清單、指紋清單引用）

### 3.2 保守處置（Conservative Handling）
如狀態切換文件缺失、或 ACTIVE 切換不完整：

- 一律視為 Freeze v1.0 仍生效（保守處置）


## 4. 最終宣告（Final）

- Freeze v1.0 生效：B/C 文件預設僅可 Only-Add。  
- HFI Override 生效：當 Valid HFI 存在時，Freeze 不得阻擋 scope 內之覆寫／重排版／全量替換；必須同步完成稽核承接。  
- 任何牴觸：以 DOCUMENT_INDEX 之衝突裁決程序處置；但任何文件與流程不得高於人類最高決策者之唯一主權。  
- 本文件之角色為「狀態宣告」，不創造新治理權力；其約束不得被曲解為限制人類最高決策者主權。

（TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251220｜ACTIVE）
