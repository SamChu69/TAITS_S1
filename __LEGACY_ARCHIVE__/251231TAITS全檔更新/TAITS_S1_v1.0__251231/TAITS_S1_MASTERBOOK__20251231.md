# TAITS_S1｜更新版工程母體（S1 Edition）— 統一口徑版（TAITS_S1__v1.0__251231）

doc_key：TAITS_S1_MASTERBOOK  
治理等級：S1（Engineering Consolidated Edition｜工程統一口徑母體）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（S1 工程口徑唯一裁決；不取代 A+/A 治理母法；以「工程落地一致性」為最高目標）  
版本日期：2025-12-31  
裁決序位（S1 內）：本文件 > S1_* 分冊  
上位約束（治理母法）：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（僅作對照；S1 以「一致口徑」消歧）  
核心原則：Regime 高於策略；Risk/Compliance 可否決一切；策略 ≠ 下單；AI ≠ 決策主體；L9=投資報告；L10=人類裁決；L11=工程稽核  

---

## 0. S1 Edition 的定位與使用規範（重要）

### 0.1 為何需要 S1 Edition
TAITS 的治理母法（A+/A/B 級）追求「不可漂移」與「Only-Add 演進」，但在工程落地階段，若多份文件存在歷史口徑差異（例如 L9/L10/L11 語義），AI/Agent 會因局部不一致而：
- 誤判層級功能（例如把 L11 當下單、把 L9 當一次性解說）
- 自行腦補缺口（尤其在資訊不足或規則衝突時）
- 為求一致而「縮減」或「重寫」既有條文，導致治理語義漂移

S1 Edition 的目的即是：**把「你已裁決的確定語義」整理成一套工程唯一口徑**，並以完整排版、明確模板、明確工件集的方式，讓後續所有工程實作、測試、稽核、回放，均不再依賴推測。

### 0.2 S1 與治理母法的關係
- S1 Edition **不取代**原治理母法（A+/A/B），也不刪減任何母法內容。
- 任何母法的歷史口徑，S1 以「**確定語義**」做 **消歧**：在 S1 範圍內以本文件為準。
- 若要把 S1 的確定語義「回寫」為治理母法的正式覆寫更新，需走治理程序（狀態切換、版本留痕、逐檔替換）。

---

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

## 2. L9 / L10 / L11 模板與最小工件集（不可省略）

### 2.1 L9 投資報告模板（摘要版）
- 報告識別：tracking_id / report_id / symbol / market / timestamp / author（含 AI）
- 主要結論（不含下單）
- 數據摘要（表）
- 圖形與解讀（圖由工程生成；本節解釋）
- 進出價格建議（Entry/Exit 條件、區間、撤退條件；明確標示「建議」）
- Regime 判定與轉換觸發
- Risk/Compliance Gate 結果（PASS/DOWNGRADE/BLOCK）
- 策略候選（可測假設）
- 不確定性、反例、需補資料
- 追蹤計畫（下一次更新條件、監控欄位）

### 2.2 L10 裁決模板（摘要版）
- decision_id / linked_report_id / linked_gate_id
- 裁決模式（NO_ACTION / BACKTEST / SIMULATION / PAPER / SEMI_AUTO / FULL_AUTO）
- 授權封套（size / max_loss / max_pos / time_in_force / revoke_conditions）
- 生效期間與撤銷條件
- 引用與理由（必須引用 L9 / L7）
- 人類簽核（你）

### 2.3 L11 稽核最小工件集（摘要版）
- run_id / tracking_id / decision_id
- 全層工件索引（L1–L11 artifact manifest）
- 每層摘要（輸入、輸出、版本、參數、時間）
- 模型路由紀錄（如有 LLM）：provider/model/temperature/max_tokens/失敗與 fallback
- 差異與異常（DQ、Regime flip、Gate block、策略失效）
- 回放指令（工程端如何重跑同一 run）

---

## 3. 本地部署與運算環境（Local）— 以你目前設備為基線

### 3.1 你的本地基線（已鎖定）
- 裝置：ASUS FX504GE
- 作業系統：Windows 11
- CPU：Intel Core i7-8750H（6C/12T）
- 記憶體（RAM）：32GB
- GPU：NVIDIA GeForce GTX 1050 Ti
- GPU VRAM：4GB
- 儲存：256GB SSD + 750GB HDD


### 3.2 對本地 AI 部署的務實定位（基於 4GB VRAM）
- 可本地化優先：L11（稽核摘要）、L1/L2（抽取/欄位化）、L5（證據條列）
- 不建議本地硬扛：L4/L6/L9 主力（推理與長文品質需求高）
- 推薦本地模型級別：3B（優先）→ 7B（量化；需控制上下文）
- 你的 TAITS 最佳策略：雲端（Plus/付費）主力 + 本地（小模型）稽核與敏感資料處理

---

## 4. AI 模型使用治理（以 GPT + DeepSeek 為主，未來可擴充）

> 本節是「使用建議」，不構成治理母法裁決；但 S1 工程落地以此做預設路由。

### 4.1 模型路由原則（建議）
- Default：Primary/Fallback（主用/備援）  
- Dual-Run（雙跑審核）僅限 L6、L9：第二模型只做一致性檢查，不改寫主輸出
- L11 必須記錄路由事件（超時、限流、schema fail、fallback）

### 4.2 分層建議（只列主用）
- L1/L2/L5/L11：低成本模型（摘要/抽取/結構化）
- L4/L6/L8/L9/L10：高品質推理模型（但限制輸出長度；避免成本失控）

---

## 5. 版本、稽核、與「不被吃掉」的硬性規範

### 5.1 任何關鍵基線必須落在文件中
- 本地環境基線（你電腦規格）
- L9/L10/L11 定義（本文件第 1 章）
- 模板與工件集（本文件第 2 章）
- 任何外部依賴（資料源、授權、模型版本）

### 5.2 反漂移（Anti-Drift）規則
- 任何 AI/Agent 回覆若與本文件第 1 章衝突，一律視為錯誤
- 任何更新必須「全文重排」而不是零散補丁（本次你要求的 B 路徑即採此）
- 所有更新在 S1 內以「整版重排」保證一致，避免只改一處導致混線

---

# 附錄 A｜S1 分冊索引（以本文件為裁決）
- TAITS_S1_DOCUMENT_INDEX.md
- TAITS_S1_MASTER_ARCH.md
- TAITS_S1_MASTER_CANON.md
- TAITS_S1_FULL_ARCH.md
- TAITS_S1_ARCH_FLOW.md
- TAITS_S1_RISK_COMPLIANCE.md
- TAITS_S1_GOVERNANCE_GATE_SPEC.md
- TAITS_S1_EXECUTION_CONTROL.md
- TAITS_S1_UI_SPEC.md
- TAITS_S1_DEPLOY_OPS.md
- TAITS_S1_LOCAL_ENV.md
- TAITS_S1_VERSION_AUDIT.md
- TAITS_S1_DATA_SOURCES.md
- TAITS_S1_TWSE_RULES.md
- TAITS_S1_STRATEGY_UNIVERSE.md
- TAITS_S1_STRATEGY_FEATURE_INDEX.md
- TAITS_S1_BEGINNER_GUIDE.md
- TAITS_S1_README.md

