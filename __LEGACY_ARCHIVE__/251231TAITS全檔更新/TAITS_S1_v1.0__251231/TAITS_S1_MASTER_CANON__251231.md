# TAITS_S1｜Canonical Flow（L1–L11）最終口徑（S1 Edition）

doc_key：TAITS_S1_MASTER_CANON  
治理等級：S1（Engineering Edition）  
版本狀態：ACTIVE（S1 口徑；不取代 A+/A 治理母法）  
版本日期：2025-12-31  
上位裁決：TAITS_S1_MASTERBOOK（TAITS_S1_MASTERBOOK__20251231.md）

---

本文件為 TAITS_S1_MASTERBOOK 第 1 章的獨立版。請以 MASTERBOOK 為裁決，本文作為方便引用的分冊。

## 1. Canonical Flow（L1–L11）最終確定語義（本次統一核心）

> 本節為 TAITS 的「層級功能唯一口徑」。任何後續文件、Agent 行為、UI 顯示、稽核回放，必須對齊本節。

### L1｜資料接入（Data Intake）
**功能**：取得原始資料（行情/新聞/公告/籌碼/基本面/衍生品/事件），完成可追溯的來源標記（source_id / time / license / checksum）。  
**輸出**：Raw Capture + Source Provenance（來源證明）  
**禁止**：在 L1 做策略結論或下單建議。

### L2｜清洗標準化（Clean & Normalize）
**功能**：欄位對齊、缺失處理、時區/交易日對齊、異常標記；產生可稽核的清洗報告（what/why/how）。  
**輸出**：Normalized Dataset + Data Quality Report（DQ 報告）  
**禁止**：以清洗結果直接推導交易動作。

### L3｜特徵與指標生成（Features & Indicators）
**功能**：依策略宇宙與研究需要，生成技術指標/統計特徵/事件特徵；保留計算版本與參數。  
**輸出**：Feature Store Snapshot + Indicator Ledger  
**禁止**：把「指標」當成「決策」。

### L4｜面向分析（Multi-Lens Analysis）
**功能**：消息面/基本面/技術面/籌碼面/衍生品面/產業與宏觀面等多面向分析；輸出各面向的「證據」與「限制」。  
**輸出**：Lens Analysis Pack（含 evidence / counter-evidence / caveats）

### L5｜證據封裝（Evidence Packaging）
**功能**：把 L4 的分析轉為「可引用、可追溯、可組裝」的證據包；每項證據必須具備來源、時間、可信度、失效條件。  
**輸出**：Evidence Pack（可被 L9 引用）

### L6｜Regime / Context（市場狀態與情境）
**功能**：判定當前市場/標的之 Regime（波動、趨勢、流動性、事件風險狀態等）；產生 Regime 置信度與轉換條件。  
**輸出**：Regime State + Confidence + Transition Triggers  
**關鍵規則**：Regime 高於策略；若 Regime 不確定，必須降級輸出並提升風控門檻。

### L7｜Risk / Compliance Gate（最高否決權）
**功能**：依風險與合規制度，對「任何可能的交易意圖」做否決/降級/放行；此層輸出為裁決結果，不是建議。  
**輸出**：PASS / DOWNGRADE / BLOCK + 理由 + 要求補件  
**禁止**：LLM 替代 Gate 判定；LLM 僅能將 Gate 結果翻譯為人話。

### L8｜策略候選與路徑（Strategy Candidate & Path）
**功能**：在 Regime 與 Gate 許可範圍內，產生策略候選（不是下單）、列出適用條件、風險、失效、與可量化驗證方式。  
**輸出**：Strategy Candidate Set（含可測假設）

### L9｜投資報告（Investment Report Layer｜你要看的完整報告）
**功能**：將 L1–L8 的資料、證據、Regime、Gate、策略候選，整合成「你可閱讀、可裁決、可追蹤」的投資報告。  
**L9 必須具備**（缺一不可）：
1. **數據摘要**：核心數據表、關鍵指標值與變動
2. **圖形/視覺化**：至少包含價格走勢/指標/風險圖（由工程繪圖；L9 說明與解讀）
3. **進出價格建議（非下單）**：Entry/Exit 條件、價格區間、停損停利邏輯、撤退條件（明確標示「建議」）
4. **情境與事件追蹤**：對同一標的建立「追蹤鍵（tracking_id）」；後續事件/價格變動可生成增量報告（不是一次性）
5. **不確定性與反例**：列出主要假設、可能打臉的反例、與需補資料項

**輸出**：L9 Report（Human-Readable）+ Report Metadata（Machine-Readable）

### L10｜人類裁決與交易授權（Decision & Trading Authorization Layer）
**功能**：由你進行最終裁決。L10 不是策略層；L10 是「你」決定 TAITS 進入何種交易模式與授權範圍。  
**L10 的裁決結果**（最小集合）：
- NO_ACTION（不動作）
- RESEARCH_ONLY（僅研究）
- BACKTEST（回測）
- SIMULATION（模擬）
- PAPER（紙上）
- SEMI_AUTO（半自動）
- FULL_AUTO（全自動）

**關鍵規則**：
- **下單與執行以 L10 授權為前提**；沒有 L10 授權，不得產生真實委託。
- L10 裁決必須引用：L9 報告版本、L7 Gate 結果、與關鍵風險條件。

**輸出**：Decision Record（Human + Machine）

### L11｜工程稽核與回放（Engineering Audit & Replay Layer）
**功能**：不是交易層。L11 是為了讓你與工程端都能**回放** TAITS 的全流程，檢查每一層是否合理、是否需要調整。  
**L11 必須覆蓋**：**L1–L11 全層工件**，而不只是 L10。  
**L11 必須同時產出**：
- **人類可讀（你看得懂）**：事件時間線、關鍵決策理由、主要差異與失效點
- **工程可用（系統回放）**：工件索引、hash、版本、參數、模型路由、輸入輸出摘要

**輸出**：Audit Bundle（Human Report + Machine Ledger）  
**禁止**：在 L11 產生交易委託；不得以 L11 作為下單入口。

---
