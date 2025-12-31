# TAITS｜程式開發流程定錨文件（Unified Process Anchor）

doc_key：PROCESS_ANCHOR
治理等級：C｜操作／啟動級（Operation / Onboarding）
版本狀態：ACTIVE（Freeze v1.0；Only-Add）
裁決序位：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（本檔不覆蓋上位治理裁決）

## SOVEREIGNTY｜人類最高決策者唯一主權（不可牴觸｜單一口徑）

1. TAITS 之**唯一最高主權**屬於人類最高決策者（產品負責人／架構裁決者）。
2. 任何文件治理等級（A+／A／B／C）、任何治理閘門（Gate）、任何 Agent、任何程序性規則不得高於人類主權；不得以程序性理由阻止人類明確命令之生效。
3. 風險與合規（Risk/Compliance）之「最高否決權」屬**系統內最高否決**：在**無人類明確命令**時可否決；在**有人類明確命令**時必須輸出完整風險揭露與替代方案，但不得將其結果升格為阻止命令之否決，改以「強制揭露＋確認＋全紀錄」承接。

## L9–L11｜最終語義定錨（跨文件一致｜單一口徑）

- **L9（投資報告層）**：輸出「可追蹤、可更新、可標的化」投資報告；必含數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源）。報告需可因市場事件/風險變化滾動更新。
- **L10（人類裁決層）**：人類最高決策者基於 L9 與治理/風控資訊裁決：不動作/回測/模擬/半自動/全自動等；任何交易型態皆以 L10 明確裁決為準。
- **L11（工程稽核回放層）**：對 **L1–L11 全層**輸入/處理/輸出/裁決/執行鏈路留痕，供你與工程端可讀、可查、可回放；L11 非下單決策層。

## HFI｜人類明確命令（可執行觸發｜單一口徑）

本系統承認以下最小格式之人類明確命令（HFI：Human Final Instruction），以確保主權可執行且不再被 Freeze/Only-Add/Gate 以程序性理由阻擋：

- `HFI: <scope> | <action> | <intent> | <acknowledgement>`

當有效 HFI 存在時：Freeze/Only-Add/Gate 不得阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。



文件類型：Engineering Process Anchor（Read-Only / Non-Governance）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
治理狀態：Freeze v1.0  
最後更新：2025-12-29  

---

## 1. 文件定位與權限聲明

> **裁決性聲明**

- 唯一具有治理裁決力之流程定義：
  - MASTER_CANON（L1–L11）
  - ARCH_FLOW
- 本文件：
  - 不具治理裁決力
  - 不新增、不修改任何制度
  - 不覆寫 Canonical Flow
- 本文件之唯一用途：
  - 作為 TAITS 工程開發之「流程定錨文件」
  - 固定工程流程座標，終止流程歧義
  - 明確標示目前實作進度

若本文件與 Canonical 文件存在任何衝突：

> **一律以 MASTER_CANON / ARCH_FLOW 為最終裁決依據**

---

## 2. 定錨文件存在目的

在 TAITS 專案中：

- AI 對話不具治理效力
- 不同對話可能出現不同流程敘述方式

若缺乏流程定錨，將導致：

- 新對話反覆討論流程
- 工程順序理解漂移
- 無法一致回答「目前做到哪一階段」

本文件存在目的為：

> **不論新對話或新 AI，  
所有工程討論皆必須回到同一流程座標系。**

---

## 3. 流程定錨核心原則

### 3.1 流程裁決唯一性

- Canonical Flow 僅有一條：L1–L11
- 工程敘述不得覆蓋 Canonical

### 3.2 Phase 的正確定位

- Phase 0–5 為工程敘述語言
- Phase 僅用於描述「工程進度」
- Phase 不具 PASS / VETO / 裁決權

### 3.3 程式碼可定位性要求

任何工程實作，必須能回答：

1. 屬於哪一個 Phase  
2. 對應哪一個 Canonical Layer（Lx）  
3. 能否指回對應治理文件  

---

## 4. Canonical Layer × Engineering Phase 對位表

| Canonical Layer | Layer 名稱 | 對應 Phase |
|-----------------|------------|------------|
| L1 | Data Source | Phase 1 |
| L2 | Normalization | Phase 1 |
| L3 | Snapshot & State | Phase 1 |
| L4 | Analysis | Phase 2 |
| L5 | Evidence | Phase 2 |
| L6 | Regime | Phase 3 |
| L7 | Risk & Compliance | Phase 3 |
| L8 | Strategy & Research | Phase 4 |
| L9 | Governance Gate | Phase 4 |
| L10 | Human Decision | Phase 5 |
| L11 | Execution & Control | Phase 5 |

---

## 5. Engineering Phase 定義（定錨版）

### 5.1 Phase 0｜治理與版本鎖定

性質：治理前置階段（不屬於任何 L 層）

必須完成項目：

- DOCUMENT_INDEX ACTIVE 文件確認
- GOVERNANCE_STATE = Freeze v1.0
- doc_key / version_ref / hash 固定
- 模組 L 層標註規則確立

禁止事項：

- 使用對話作為治理依據
- 未標註 L 層即開始實作

---

### 5.2 Phase 1｜資料與狀態骨架（L1–L3）

允許事項：

- 官方資料來源
- 正規化處理
- Snapshot / State 落盤與回放

禁止事項：

- 指標與訊號
- 策略與交易語義

---

### 5.3 Phase 2｜分析與證據（L4–L5）

允許事項：

- 描述性分析
- Evidence Bundle（可追溯、可回放）

禁止事項：

- buy / sell
- signal / trigger
- 績效、勝率、排序

---

### 5.4 Phase 3｜Regime 與 Risk（L6–L7）

必須成立條件：

- Regime 可標示不可交易狀態
- Risk 僅輸出 PASS / VETO
- VETO 附 reason codes
- Risk PASS Token 機制存在

禁止事項：

- Soft Pass
- 人類或 AI 覆寫 VETO

---

### 5.5 Phase 4｜策略提案與治理檢查（L8–L9）

允許事項：

- Strategy Proposal / Scenario
- Governance Gate RETURN / STOP

禁止事項：

- 策略即行為
- 策略直連 Execution
- AI 自動批准

---

### 5.6 Phase 5｜人類裁決與執行（L10–L11）

必須成立條件：

- UI 為唯一 APPROVE / REJECT 入口
- 無 Risk PASS Token → Execution BLOCK
- Execution 全程可審計、可中止

禁止事項：

- 無 UI 自動批准
- 無 Token 下單

---

## 6. 工程進度狀態標示（流程座標）

> **本區為流程定錨之唯一狀態來源**

```text
Current Phase        : Phase 0
Completed Phases     : Phase 0
Next Target Phase    : Phase 1（L1–L3 Data / State Skeleton）
Blocked Layers       : L4–L11（依法不可實作）
Last Review Date     : YYYY-MM-DD


---

# 【Only-Add｜新增】All-in-One 內嵌附錄（為減檔與新手便利而設）

> 新增日期：2025-12-28  
> 生效前提：GOVERNANCE_STATE = Freeze v1.0（Only-Add）  
> 目的：你提出「檔案太多要合併」，因此在不刪檔、不覆寫的前提下，將相關 SOP/模板**全文內嵌**於本文件附錄，供日常查閱。  
> 重要限制：以下內嵌內容皆屬 SUPPORT（工程/操作支援），**不具治理裁決效力**；任何裁決仍回 `DOCUMENT_INDEX → MASTER_ARCH → AI_GOV`。

---
