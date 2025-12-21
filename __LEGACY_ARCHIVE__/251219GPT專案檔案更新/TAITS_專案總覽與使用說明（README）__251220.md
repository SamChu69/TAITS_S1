# TAITS_專案總覽與使用說明（README）__251220
doc_key：README  
治理等級：C（Project Overview & Usage Charter｜入口導覽文件，不具上位裁決權）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（Only-Add：只可新增，不可刪減/覆寫/偷換語義）  
版本日期：2025-12-20  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：DOCUMENT_INDEX / MASTER_ARCH / MASTER_CANON（衝突時以上位文件裁決）  
平行參照：FULL_ARCH / ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES / STRATEGY_UNIVERSE / STRATEGY_FEATURE_INDEX / DEPLOY_OPS / LOCAL_ENV / TWSE_RULES / BEGINNER_GUIDE / GOVERNANCE_GATE_SPEC  
變更原則：Only-Add（允許補強導覽、補充流程入口、補充引用索引；禁止刪減既有治理宣告與邊界）  

---

## 0. 文件定位（README 的「唯一職責」）

本 README 是 **TAITS 專案的入口憲章與導覽地圖**，只負責三件事：

1) **讓新對話 / 新 AI / 新 Agent 在不誤解的前提下快速進入治理正軌**  
2) **定義 TAITS 是什麼／不是什麼（避免越權與誤用）**  
3) **提供「正確閱讀順序」與「文件導航」以保證一致性與可追溯**

📌 本 README **不具裁決權**：  
- 不裁決文件衝突（由 `DOCUMENT_INDEX` 裁決）  
- 不定義鐵律（由 `MASTER_ARCH` 裁決）  
- 不定義 Canonical Flow（由 `MASTER_CANON / ARCH_FLOW` 裁決）  
- 不定義風控否決條文（由 `RISK_COMPLIANCE` 裁決）  
- 不定義下單細節（由 `EXECUTION_CONTROL` 裁決）

---

## 1. TAITS 是什麼？（不可被誤解的定義）

**TAITS（Taiwan Alpha Intelligence Trading System）** 是一套：

- 以 **台灣市場（TWSE / TAIFEX）** 為核心對象
- 以 **治理（Governance）與風險/合規（Risk/Compliance）** 為最高優先序
- 以 **Canonical Flow（L1–L11，不可跳步）** 為全系統骨架
- 允許 **多 Agent** 與 **多策略宇宙** 長期演進（Only-Add）
- 強制 **審計（Audit）/回放（Replay）/可追溯（Traceability）**
- 明確規定 **AI 只能輔助、不能取代人類裁決（Human-in-the-Loop）**

的 **完整系統母體**（非 Demo、非教學專案、非單一策略）。

---

## 2. TAITS 不是什麼？（禁止錯誤期待）

TAITS **不是**：

- ❌ 單一策略或選股法  
- ❌ 以績效展示為核心的投資工具  
- ❌ 「AI 自動下單」黑箱  
- ❌ 無人值守、自動批准、自動執行的交易機器  
- ❌ 需要使用者自行 Debug / 自行補完的工程專案  

📌 在 TAITS：  
- **策略 ≠ 下單**  
- **Agent ≠ 策略**  
- **AI ≠ 唯一真理**  
- **Regime（市場狀態）高於單一訊號**  
- **Risk / Compliance 可否決一切**

---

## 3. TAITS 的最高鐵律摘要（僅作入口提醒；裁決以 MASTER_ARCH / AI_GOV 為準）

以下屬於入口級「不可破壞理解」：

1) **Only-Add**：內容只可新增，不可刪減/覆寫/弱化  
2) **L1–L11 不可跳步**：任何捷徑都屬治理違規  
3) **Evidence First**：無證據不得進入判斷/執行  
4) **Binary Compliance（PASS / VETO）**：合規與否決不容模糊  
5) **Human-in-the-Loop**：人類裁決不可被取代（L10 必須存在）  
6) **No Audit = Not Happened**：無審計視為未發生  
7) **Risk PASS Token Required**：未通過風控放行憑證不得進入執行層  
8) **Kill Switch Always Available**：任何執行狀態必須可立即中止  

---

## 4. 正確閱讀順序（新對話 / 新 AI / 新 Agent 必須遵守）

### 4.1 最小必讀（不得跳過）
1) `TAITS_AI_行為與決策治理最終規則全集__251217`（A+）  
2) `DOCUMENT_INDEX`（A+ / A+裁決性）  
3) `MASTER_ARCH`（A）  
4) `MASTER_CANON`（A）  
5) `FULL_ARCH`（B）  
6) `ARCH_FLOW`（B+）  
7) `RISK_COMPLIANCE`（A）  
8) `EXECUTION_CONTROL`（A）  
9) `VERSION_AUDIT`（B）  

### 4.2 視需求擴展（在治理框架下）
- `DATA_SOURCES`（B）  
- `STRATEGY_UNIVERSE`（B）  
- `STRATEGY_FEATURE_INDEX`（B）  
- `UI_SPEC`（B）  
- `DEPLOY_OPS`（B）  
- `LOCAL_ENV`（C/B，依專案定義）  
- `TWSE_RULES`（B/C：參考彙編，但合規裁決需回到官方來源入口）  
- `BEGINNER_GUIDE`（C：新手操作引導，不能作治理裁決依據）  
- `GOVERNANCE_GATE_SPEC`（B：治理閘門與裁決規範）

📌 任何「先談策略再補治理」的工作方式，在 TAITS 一律視為高風險且不可接受。

---

## 5. 專案文件一覽（以 doc_key 為唯一識別）

> 若你看到文件名不同，但 doc_key 相同，以 `DOCUMENT_INDEX` 的 ACTIVE 裁決為準。

### 5.1 A+（最高母法）
- `AI_GOV`：TAITS_AI_行為與決策治理最終規則全集__251217（A+）

### 5.2 A（憲法級）
- `MASTER_ARCH`：母體總憲法與核心鐵律  
- `MASTER_CANON`：完整總架構×總流程×全資訊體系

### 5.3 B / B+（架構、流程、風控、執行、營運、資料）
- `DOCUMENT_INDEX`：文件索引與治理對照表（裁決性極高；以專案定義為準）  
- `FULL_ARCH`：全系統架構總覽（模組地圖與邊界）  
- `ARCH_FLOW`：系統架構與流程細化說明（Canonical Flow：L1–L11）  
- `RISK_COMPLIANCE`：風險與合規最高否決權（Supreme Veto）  
- `EXECUTION_CONTROL`：交易執行與控制規範（Execution & Control）  
- `VERSION_AUDIT`：版本控管、稽核與可追溯治理規範  
- `DATA_SOURCES`：資料來源全集（官方優先、多層 fallback、可追溯）  
- `STRATEGY_UNIVERSE`：策略宇宙全集（白名單、生命週期、不可直連下單）  
- `STRATEGY_FEATURE_INDEX`：策略特徵與因子索引（特徵≠方向）  
- `UI_SPEC`：使用者介面與人機決策規範（否決可視化、決策追溯）  
- `DEPLOY_OPS`：部署、營運與日常運作規範（回滾、停機、Runbook）  
- `TWSE_RULES`：TWSE 交易規則參考彙編（觸發映射；裁決回到官方入口）  
- `GOVERNANCE_GATE_SPEC`：治理閘門與裁決規範（Gate 定義與一致性）

### 5.4 C（操作/引導）
- `BEGINNER_GUIDE`：新手教學與操作引導總則  
- `README`：本文件

---

## 6. TAITS 的「運作模式」一致性宣告（不可降級）

TAITS 支援（概念上）：
- Research（研究）
- Backtest（回測）
- Simulation（模擬）
- Paper（紙上/模擬下單）
- Live（實盤）

但**所有模式必須共用同一套治理語義**：
- **L1–L11 不得因模式不同而跳層**
- **Risk / Compliance 不得因模式不同而降級**
- **Audit / Replay 不得因模式不同而缺失**

📌 「回測可跑但實盤不行」在 TAITS 視為制度設計失敗。

---

## 7. 角色分工（強制遵守）

### 7.1 人類（使用者）
- 身分：產品經理 / 架構決策者 / 最終裁決者（L10）  
- 不負責：寫程式、Debug、補完缺失  
- 擁有：最終裁決權（但**不擁有文件解釋權**；裁決依文件）

### 7.2 AI（系統工程師 + 架構設計師 + 量化研究員）
- 必須交付：可直接貼上的完整內容（不可片段、不可要求使用者補齊）  
- 禁止：  
  - 自行簡化（No-Slimming）  
  - 文件沒寫就自行合理化（No Fabrication of Authority）  
  - 用「推測」取代「文件依據」

---

## 8. 合規與官方入口（規則裁決必回到官方）

> TAITS 允許彙編與對照，但**制度裁決以官方來源為準**。

- TWSE 規章/法規查詢：https://twse-regulation.twse.com.tw/  
- TWSE 交易制度/交易機制：https://www.twse.com.tw/en/products/system/trading.html  
- TAIFEX 規章與規則：https://www.taifex.com.tw/enl/eng6/ruleRegulation  
- FSC 金管會法規資訊：https://www.fsc.gov.tw/en/home.jsp?id=3&parentpath=0  
- SFB 證期局入口：https://www.sfb.gov.tw/en/  
- TDCC 集保結算（結算交割相關）：https://www.tdcc.com.tw/portal/en/equity/settlement  

📌 若彙編內容與官方更新衝突：以官方為準，並依 `VERSION_AUDIT` 啟動變更流程。

---

## 9. 專案「嚴格對齊模式」工作規範（README 層級宣告）

在 TAITS 專案內協作（含新對話）必遵守：

1) **以 doc_key 為引用主鍵**（文件名可能變、doc_key 不可變）  
2) **任何新增內容必標記：來源文件、章節、版本**  
3) **Only-Add**：不允許刪減或覆寫既有制度語義  
4) **遇到缺口：先停、先請示、先補文件**（禁止自行補完）  
5) **凡涉及交易執行：必須可審計、可回放、可追責**  

---

## 10. 快速啟動（不是操作手冊；是「不踩雷」入口）

如果你要開始一個新議題（新增模組、策略、Agent、資料源、UI、部署）：

請先決定它屬於哪一層：

- **治理母法 / 鐵律** → `MASTER_ARCH`  
- **流程順序 / Canon** → `MASTER_CANON / ARCH_FLOW`  
- **風險與合規否決** → `RISK_COMPLIANCE`  
- **執行與控制** → `EXECUTION_CONTROL`  
- **版本追溯與審計** → `VERSION_AUDIT`  
- **資料來源與可追溯** → `DATA_SOURCES`  
- **策略白名單與生命週期** → `STRATEGY_UNIVERSE`  
- **特徵與因子管理** → `STRATEGY_FEATURE_INDEX`  
- **介面、人機裁決、否決可視化** → `UI_SPEC`  
- **營運、部署、回滾、停機** → `DEPLOY_OPS`  
- **交易所規則彙編/觸發映射** → `TWSE_RULES`  
- **新手操作引導** → `BEGINNER_GUIDE`  
- **治理閘門一致性** → `GOVERNANCE_GATE_SPEC`

📌 若你不知道該歸哪一份：請以 `DOCUMENT_INDEX` 的裁決規則處理。

---

## 11. 最終聲明（不可刪）

TAITS 的核心價值不在於「多聰明」，而在於：

- **不亂來**
- **不越權**
- **可回放**
- **可追責**
- **可長期演進**

> 只要存在不可接受風險，  
> 就算錯過機會，也必須選擇不交易。  
> （裁決依 `RISK_COMPLIANCE`）

---

（README｜最大完備治理版 · 2025-12-20 完）
