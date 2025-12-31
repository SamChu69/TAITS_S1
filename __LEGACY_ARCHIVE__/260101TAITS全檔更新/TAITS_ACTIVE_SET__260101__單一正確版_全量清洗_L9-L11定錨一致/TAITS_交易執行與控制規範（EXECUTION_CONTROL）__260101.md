# TAITS_交易執行與控制規範（EXECUTION_CONTROL）__260101
doc_key：EXECUTION_CONTROL  
治理等級：A（Execution & Control Specification｜嚴格執行層最高規範）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（執行控制規範，Only-Add 演進）  
版本日期：2026-01-01  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：FULL_ARCH / ARCH_FLOW / RISK_COMPLIANCE / UI_SPEC / VERSION_AUDIT / DEPLOY_OPS / LOCAL_ENV / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化安全機制/偷換定義）  
核心鐵律：Human-in-the-Loop + Risk PASS Token Required + Kill Switch Always Available  

## L9–L11 最終語義定錨（單一正確版｜不得歧義）

> 版本日期：2026-01-01（Asia/Taipei）  
> 本段為 TAITS 對 L9 / L10 / L11 的「唯一有效語義」。任何文件若出現牴觸描述，以本段為準並視牴觸描述為無效。

### L9｜投資報告層（Human-Readable Investment Report）
**定位**：將 L1–L8 的資訊與策略證據，彙整為「可被人類決策」的完整投資報告（不是下單層）。  
**必備輸出（最小要求）**：
- 標的化追蹤：標的 ID / 名稱 / 市場（TWSE/TAIFEX）/ 追蹤起訖時間 / 狀態（觀察、候選、持有、出場）
- 數據與圖形：關鍵時間序列、技術指標圖、事件時間線、風險指標、情境/Regime 標示
- 交易建議（僅建議，不執行）：進出場區間/條件、停損/停利、部位建議、情境觸發的調整規則
- 版本可回放：資料快照指紋（hash）、引用來源、計算參數、結論摘要與反證點

**重要邊界**：L9 **不得**直接觸發任何交易執行；不得將建議視為命令。

### L10｜人類裁決與交易授權層（Human Decision & Trade Authorization）
**定位**：唯一允許產生「交易授權」的層級；所有回測/模擬/紙上/實盤、半自動/全自動/不動作之裁決，均在 L10 形成。  
**決策模式（由人類最高決策者裁決）**：
- 不動作（NO_ACTION）
- 研究/觀察（RESEARCH_ONLY）
- 回測（BACKTEST）
- 模擬（SIMULATION）
- 紙上（PAPER）
- 半自動（SEMI_AUTO：人類確認後才送出）
- 全自動（FULL_AUTO：在授權條件內自動執行）

**重要邊界**：下單/送出/撤單/改單等任何交易行為，只能在 **L10 授權成立後** 才能進入執行流程。

### L11｜工程稽核與回放層（Engineering Audit, Replay & Diagnostics）
**定位**：全系統稽核與工程檢視層，用於驗證每一層輸入/輸出是否符合規範、可回放、可追溯；**不是下單層**。  
**稽核範圍**：L1–L11 **每一層**都必須可被 L11 稽核（不僅是 L10）。  
**雙料內容（同時必備）**：
- 人話版：讓人類最高決策者能讀懂（原因、證據、風險、差異、結論）
- 工程版：讓工程/系統能回放與診斷（事件序列、參數、資料快照、指紋、例外、重現步驟）

**重要邊界**：L11 **不得**生成或替代 L10 的交易授權；僅能輸出告警、回放、診斷與改進建議（供後續治理/工程處置）。

---

---
