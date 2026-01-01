# TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260102.md
doc_key：GOVERNANCE_STATE_FREEZE_V1  
治理等級：A（Governance State｜治理狀態裁決文件）  
版本狀態：ACTIVE（Freeze v1.0 生效）  
版本日期：2026-01-02（Asia/Taipei）  
最後修訂：2026-01-02（對齊「最大完備＋累積式更新」口徑；移除 Append-only（僅允許新增） 作為治理口徑；重排章節為單一可讀正文）  
物理檔名：TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260102.md（本文件之治理身份以本標頭為準；檔名差異僅屬物理映射）  
上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ AI_GOV（A+）  
適用範圍：TAITS 全系統（宣告 Freeze v1.0 之預設保守門檻；並定義 HFI Override 與狀態切換要求）  
變更原則（本文件）：  
- 允許：融合更新／覆寫修正／重排版，以收斂為「單一正確正文」，但必須同步完成稽核留痕（見〈附錄｜稽核留痕〉）。  
- 禁止：以附錄補丁、補綴式 Addendum/Appendix、Freeze 註記等方式造成新舊混讀。  
- 狀態切換：必須以「新 GOVERNANCE_STATE_* 文件」完成（見 §4），不得以覆寫本檔方式偷換治理狀態版本。

---

## 0. 文件定位（State Declaration）

本文件為 TAITS 的「治理狀態宣告文件」，用於宣告當前治理狀態為 **Freeze v1.0**，並對 TAITS 全系統施加預設保守門檻，以避免：

- 語義漂移（Semantic Drift）
- 規格分叉（Spec Fork）
- 新舊混讀（Mixed Reading）
- 不可回放（Non-replayable）

注意：Freeze v1.0 的角色是「狀態門檻」，不是「最高權限」。  
TAITS 的**唯一最高主權**始終屬於人類最高決策者；本文件不得被曲解為限制人類最高決策者之明確命令（見 §1.1 與 §3）。

---

## 1. 全局定錨｜單一口徑（S1）

### 1.1 人類最高決策者主權（SOVEREIGNTY）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接，不得卡死更新。

### 1.2 L9–L11 最終語義（跨文件一致）
- L9（投資報告層）：可追蹤、可更新、可標的化投資報告；必含數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源），並支援事件驅動滾動更新。
- L10（人類裁決層）：由人類最高決策者裁決不動作/回測/模擬/半自動/全自動等；任何交易型態皆以 L10 明確裁決為準。
- L11（工程稽核回放層）：對 L1–L11 全層輸入/處理/輸出/裁決/執行鏈路留痕，供人類與工程端可讀、可查、可回放；L11 非下單決策層。

### 1.3 HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：Freeze/Gate 不得阻擋 scope 範圍內之融合更新／覆寫修正／重排版；並必須同步完成稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。

---

## 2. Freeze v1.0 預設規則（Default Constraints）

### 2.1 適用文件層級
- 對所有 **B／C 治理文件**：在無有效 HFI 時，適用本節「預設保守門檻」。
- 對 A/A+ 文件：其變更由 DOCUMENT_INDEX 與 VERSION_AUDIT 之規則約束；Freeze 不得被曲解為「禁止母法更新」，但在無 HFI 時仍應採保守策略並遵守 Index Gate 與稽核要求。

### 2.2 預設允許（無 HFI 時｜最大完備＋累積式更新之非破壞性變更）
在 Freeze v1.0 下，對 B/C 文件之「預設允許」僅限下列 **非破壞性** 變更型態：

1) **新增**章節／條款／附表／附錄（不造成既有內容失效或被隱形替換）  
2) **補強**更清楚的定義、邊界說明、例外處理、操作步驟（不得改寫既有規則語義）  
3) **補齊**稽核欄位與留痕格式（不得刪減既有留痕要求）  
4) **重排版**僅限版面與索引（章節順序、標題層級、列表格式），不得改動規則語義；若有任何語義影響，視同覆寫修正，必須走 HFI（見 §3）。

> 重要：Freeze v1.0 期間禁止以「摘要化／精華版」取代原文。  
> 未被新內容**明確取代**者，必須保留並持續累積；僅當新內容已對舊內容形成明確取代關係時，方可在正文中省略舊段落，但必須以稽核留痕承接（見〈附錄｜稽核留痕〉與 VERSION_AUDIT）。

### 2.3 預設禁止（除非 HFI Override）
在 Freeze v1.0 下，對 B/C 文件預設禁止：

- 靜默刪除既有內容（含移除段落、刪減條款、刪掉關鍵限定語）  
- 靜默覆寫既有段落（含改寫既有語義、替換既有規則、刪改條款適用範圍）  
- 以「重排版」之名實質改動規則語義  
- 未完成稽核留痕即進行大幅度版本替換（例如：單一正確正文收斂、全量融合重寫）

---

## 3. HUMAN SOVEREIGNTY｜人類主權（唯一最高）

### 3.1 唯一最高主權（唯一性宣告）
TAITS 之最終裁決權 **唯一**屬於人類最高決策者（產品負責人／架構裁決者）。  
除人類最高決策者外，**不存在**任何同級或更高之「權限／裁決權」。任何文件等級（A+／A／B／C）、任何 Gate、任何 Agent/AI 內規、任何流程條款（含 Freeze）均不得在主權位階上與其並列、不得高於其。

---

## 4. 狀態切換（State Transition）與保守處置（Conservative Handling）

### 4.1 狀態切換必備條件（Switch Requirements）
若要切換治理狀態（例如：UNFREEZE／新的 FREEZE 版本），必須同時滿足：

1) **新增**一份新的 `TAITS_GOVERNANCE_STATE__<STATE>_vX.Y__<date>.md`  
2) 在 `DOCUMENT_INDEX` 中納入該文件，並完成 **ACTIVE 唯一性切換**  
3) 在 `VERSION_AUDIT` 留下變更帳本（change_id、理由、範圍、影響清單、指紋清單引用）

### 4.2 保守處置（Conservative Handling）
如狀態切換文件缺失、或 ACTIVE 切換不完整：

- 一律視為 Freeze v1.0 仍生效（保守處置）

---

## 5. 最終宣告（Final）

- Freeze v1.0 生效：B/C 文件在無有效 HFI 時，預設採保守門檻（禁止靜默刪減與靜默覆寫；禁止摘要縮水）。  
- HFI Override 生效：當 Valid HFI 存在時，Freeze 不得阻擋 scope 內之融合更新／覆寫修正／重排版／全量替換；必須同步完成稽核承接。  
- 任何牴觸：以 DOCUMENT_INDEX 之衝突裁決程序處置；但任何文件與流程不得高於人類最高決策者之唯一主權。  
- 本文件之角色為「狀態宣告」，不創造新治理權力；其約束不得被曲解為限制人類最高決策者主權。


---

## 附錄｜稽核留痕（不屬正文｜禁止作為新裁決依據）

> 本附錄用於滿足「強制留痕」要求：CHANGELOG＋SCOPE＋HASH_MANIFEST＋AUDIT_HANDOFF。  
> 任何引用與裁決，仍以正文為準；本附錄不得被用來創造新規則或改寫正文語義。

## A. Changelog（變更清單）
- change_id：GS-FREEZE-FUSION-260102-0001
- change_type：融合更新／覆寫修正／重排版（收斂為單一正確正文）
- key_updates：
  1) 將「舊口徑（僅允許新增）」由治理口徑移除，改以「最大完備＋累積式更新」與「禁止摘要縮水」作為正文可讀規則。  
  2) 明確區分：無 HFI 的預設保守門檻 vs. 有 HFI 的融合覆寫權限（HFI Override）。  
  3) 章節依序重排（0→5），並將 S1 定錨（主權、L9–L11、HFI）置於前部，避免跨文件混讀。

## B. Scope（適用範圍）
- doc_key：GOVERNANCE_STATE_FREEZE_V1
- state：FREEZE v1.0
- applies_to：TAITS 全系統（預設門檻套用於 B/C 文件；A/A+ 以其上位規範與稽核規範為準）
- compatibility_note：
  - 歷史文件若仍出現 舊口徑（僅允許新增）等字樣，應依本檔 §2 與 §5 解讀：不得摘要縮水；未被新內容明確取代者須保留；需融合覆寫必須有效 HFI 並完成稽核承接。

## C. Hash Manifest（指紋清單）
- hash_alg：sha256
- body_scope：BODY_ONLY（不含本附錄）
- body_sha256：abed9c16185515ebc972281df92cb508bad14fcb5757d32e5cfdd57aeb3a5dc0

### C1. Source File Hashes（來源檔指紋）
| source_file | sha256 |
|---|---|
| TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260101__單一檔.md | 1a57241f063ca17709fbaaedd794e5b889f971bc4f6a25f8bc053312598eb59c |

## D. Audit Hand-off（裁決承接）
- authority_basis：HFI（人類最高決策者明確命令｜scope=GOVERNANCE_STATE_FREEZE_V1｜action=融合更新/覆寫/重排版｜intent=單一正確正文＋最大完備＋避免混讀）
- downstream_requirements（必做）
  1) 更新 `DOCUMENT_INDEX`（doc_key=DOCUMENT_INDEX）中 GOVERNANCE_STATE_FREEZE_V1 對應檔名與版本日期，並確保 ACTIVE 唯一性仍成立。  
  2) 更新 `VERSION_AUDIT`（doc_key=VERSION_AUDIT）：新增 GS-FREEZE-FUSION-260102-0001 變更帳（含 scope、原因、影響面、回滾策略、body_sha256）。  
  3) L11 回放鏈：保存「來源檔」與「本檔 body_sha256」對應關係，確保可回放比對（diff 可生成但不得混入正文）。

