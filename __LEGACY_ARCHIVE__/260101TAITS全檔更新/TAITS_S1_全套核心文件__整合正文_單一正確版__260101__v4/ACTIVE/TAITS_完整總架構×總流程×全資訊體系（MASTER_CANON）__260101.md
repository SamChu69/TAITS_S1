# TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__260101
doc_key：MASTER_CANON  
治理等級：A（Supreme Canon｜最高裁決母體）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（最高母法，Only-Add 演進）  
版本日期：2026-01-01  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / DOCUMENT_INDEX  
平行參照：FULL_ARCH / ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES / STRATEGY_UNIVERSE / STRATEGY_FEATURE_INDEX / LOCAL_ENV / DEPLOY_OPS / TWSE_RULES / README  
變更原則：Only-Add（僅可新增，不可刪減／覆寫／改寫語義）  

## SOVEREIGNTY｜人類最高決策者唯一主權（不可牴觸）

- TAITS 之**唯一最高主權**屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何文件治理等級（A+／A／B／C）、任何治理閘門（Gate）、任何 Agent、任何程序性規則不得高於人類主權；不得以程序性理由阻止人類明確命令之生效。
- 風險與合規（Risk/Compliance）之「最高否決權」屬**系統內最高否決**：在**無人類明確命令**時可否決；在**有人類明確命令**時必須輸出完整風險揭露與替代方案，但不得將其結果升格為阻止命令之否決，改以「強制揭露＋確認＋全紀錄」承接。

## L9–L11｜最終語義定錨（跨文件一致）

- **L9（投資報告層）**：輸出可追蹤、可更新的「標的化投資報告」。必含：數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態／更新時間／依據來源）。報告需可因市場事件／風險變化滾動更新。
- **L10（人類裁決層）**：人類最高決策者基於 L9 與治理/風控資訊進行裁決：不動作／回測／模擬／半自動／全自動等。任何交易型態皆以 L10 的明確裁決為準。
- **L11（工程稽核回放層）**：對 **L1–L11 全層**輸入/處理/輸出/裁決/執行鏈路留痕，供你與工程端可讀、可查、可回放；L11 不是下單決策層。

## HFI｜人類明確命令（可執行觸發工件）

為避免「主權存在但無法執行」之治理失效，本系統承認以下最小格式之人類明確命令（HFI：Human Final Instruction）：

- `HFI: <scope> | <action> | <intent> | <acknowledgement>`

範例：
- `HFI: ALL | overwrite+reformat | 全量重整更新重新排版為單一正確版 | 我確認此命令為最終裁決並要求完整留痕`

當有效 HFI 存在時：Freeze/Only-Add/Gate 不得阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。


---

---

## 0. 文件定位（Canonical Master｜最大完備整合版）

本檔為 **MASTER_CANON 的「最終整合單檔版」**（Final Integrated Edition）。  
本版本的整合原則為：

- **原有正文內容「原封不動保留」**（不刪、不縮、不改義）  
- 僅以 **Only-Add** 方式補齊：文件宇宙分類、引用合法性、衝突裁決、以及「新對話/新 AI 啟動行為規範」  
- 所有新增章節均以本檔的 **治理等級 S** 進行裁決性落地，供 `DOCUMENT_INDEX` 建立引用與衝突裁決秩序

---

## 【Canonical 使用與解讀指引（Normative Reading Guide）】

本文件（MASTER_CANON）為 TAITS 之最高架構母法（Canonical Constitution），
其目的在於：

1. 定義 TAITS 各層級（L1–L11）之存在性、責任邊界與不可越權原則  
2. 鎖定人類、AI 與系統之分工關係與治理裁決順序  
3. 防止任何角色（人或系統）對層級職責產生混用、誤用或越權解讀  

### 重要解讀原則（強制）

- 本文件中所描述之分析項目、敘事責任與品質要求，  
  屬於「合格標準與語義邊界定義（Normative Boundary）」，  
  **不代表每次實際運行時，必須完整逐項輸出。**

- 實際分析輸出之深度、形式與篇幅，  
  得依市場情境、風險等級與人類決策需求彈性調整，  
  **惟不得違反本 Canon 所定義之層級語義與不可越權原則。**

- 任何文件、模組、AI 行為或工程實作，  
  若與本文件之語義邊界發生衝突，  
  **一律以 MASTER_CANON 為最終裁決依據。**

本指引為解讀與使用說明，  
不構成新增流程、層級或權限之修改。

---
