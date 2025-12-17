# 📘 TAITS_Architecture_Layer_Map.md
## TAITS 全系統層級地圖（Architecture Layer Map）

---

## 0. 文件定位（必讀）

本文件提供 TAITS 的「層級地圖（Layer Map）」與「責任邊界（Responsibility Boundaries）」。

目的：
- 讓任何人/AI 一眼知道：哪些可改、哪些不可改、哪些只能加不能動
- 防止未來擴充（期貨/選擇權/更多 Agent/更多策略）導致層級混亂或越權

本文件屬於：
- Architecture / Governance 的索引層文件（Index-Level Spec）
- 不定義新邏輯，只定義層級與接口責任

---

## 1. TAITS 層級總覽（由上到下，權限遞減）

> 原則：越上層越接近「生存」，越下層越接近「績效」  
> 任何下層不得覆寫上層結論

### L0｜Constitution Layer（憲章層）
- 定義不可違反原則：Regime 高於一切、Risk 可否決一切、策略≠下單、AI≠唯一真理
- 變更頻率：幾乎不可變更
- 例：TAITS_MASTER_ARCHITECTURE.md、TAITS_Risk_and_Compliance.md（概念性最高約束）

### L1｜Architecture Layer（架構層）
- 定義模組邊界、事件流/資料流、系統責任分工
- 變更頻率：極低（只能擴充，不宜重寫）
- 例：TAITS_Architecture_and_Flow.md、TAITS_Full_System_Architecture.md、TAITS_Document_Index.md

### L2｜Data & Validation Layer（資料與校驗層）
- 資料來源、欄位一致性、延遲/缺漏、fallback、稽核紀錄
- 變更頻率：中（常擴充資料源，但規格要一致）
- 例：TAITS_DataSources_Universe.md、資料 Validator 規格

### L3｜Evidence & Interpretation Layer（證據解讀層）
- 把資料轉成「可被決策引用的證據」：如威科夫結構、情緒、基本面評分、消息可信度等
- 變更頻率：中（可新增證據類型，但不得越權下單）
- 例：
  - TAITS_Wyckoff_Market_Structure_Framework.md
  - TAITS_Wyckoff_Explore_Exploit_Rule_Matrix.md

### L4｜Regime & Risk Gate Layer（市場狀態與風險門控層）
- 決定「此刻哪些行為被允許存在」
- 具有否決權：可直接 NO_TRADE
- 變更頻率：低～中（可新增 Gate，但邏輯必須更嚴謹，不能更寬鬆）
- 例：
  - TAITS_Time_Advantage_Framework.md（原則）
  - TAITS_Market_Manipulation_Risk_Framework.md
  - TAITS_Market_Manipulation_Risk_Checklist.md

### L5｜Strategy Governance Layer（策略治理層）
- 管理 285+ 策略：分群、啟用條件、禁用條件、Evidence Tier 對齊
- 變更頻率：中（常新增策略或調整群組，但要遵守 Gate）
- 例：
  - TAITS_Strategy_Universe_Mapping_to_Dual_Track.md
  - TAITS_Dual_Track_Strategy_Governance.md

### L6｜Decision Core Layer（決策核心層）
- 唯一輸出：TRADE / WAIT / NO_TRADE
- 決策必須依序引用：Regime/Risk Gate → Evidence → Strategy Governance
- 變更頻率：低（避免頻繁更動造成決策漂移）
- 例：
  - TAITS_Dual_Track_Decision_Architecture.md
  - TAITS_Single_Page_Playbook.md

### L7｜Execution & Portfolio Layer（執行與組合層）
- 下單、倉位、資金分配（目前以股票/零股為主；期貨下單未來擴充）
- 變更頻率：中（會隨券商 API、成本、產品而調整）
- 注意：不得繞過 Decision Core

### L8｜Operations Layer（作業操作層）
- 每日/每週檢查流程、例行稽核、報告格式
- 變更頻率：高（可因使用習慣調整，但不得違反 Gate）
- 例：
  - TAITS_Daily_Weekly_Risk_Check_Procedure.md

---

## 2. 層級責任與「不得越權」清單（硬規則）

- L2 資料層：不得直接產生交易建議
- L3 證據層：不得單獨觸發交易，只能提供 Evidence
- L4 Gate 層：可否決一切，但不得「強制交易」
- L5 策略治理層：只能在 Gate 允許時啟用策略
- L6 決策核心：唯一輸出決策，任何模組不得自行下單
- L8 操作層：可以讓流程更順，但不得把門控繞掉

---

## 3. 決策資料流（One-pass Flow）

1) Data Ingest（資料進來）
2) Validation（校驗/補缺/稽核）
3) Evidence Build（建立證據）
4) Regime/Risk Gate（允許/否決）
5) Strategy Governance（策略群組啟用）
6) Decision Core（TRADE/WAIT/NO_TRADE）
7) Execution（下單/控倉/紀錄）
8) Ops Review（每日/每週檢查）

---

## 4. 文件層級標籤規範（建議採用）

為避免未來文件越寫越亂，建議所有核心文件在開頭標註：

- [ARCH] Architecture（不可動）
- [GOV] Governance（少動，需審核）
- [OPS] Operations（可調，需一致）
- [REF] Reference（資料庫/列表）
- [SPEC] Spec（規格）

---

## 5. 最終一句話（TAITS Layer Map 憲章）

> TAITS 以「Gate（Regime/Risk）」守住生存，
> 以「Governance（策略治理）」管理複雜度，
> 以「Decision Core」收斂為單一決策輸出，
> 以「Operations」確保每天都不走偏。
