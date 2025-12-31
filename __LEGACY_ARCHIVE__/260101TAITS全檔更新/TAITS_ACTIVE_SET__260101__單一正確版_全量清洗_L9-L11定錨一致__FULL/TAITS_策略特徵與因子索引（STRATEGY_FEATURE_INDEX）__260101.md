<!--
TAITS｜ACTIVE UPDATED（單檔內嵌更新版）
產出日期：2025-12-29（Asia/Taipei）
更新規格：單檔內嵌；可更新處直接更新並避免重複；不可更新處以 Appendix 內嵌 Only-Add 全文。
來源檔：TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md
-->

# TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219
doc_key：STRATEGY_FEATURE_INDEX
治理等級：B+（Feature Governance & Semantic Boundary Charter｜全知識自洽最大完備版）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（特徵層治理封頂＋可展開知識索引，Only-Add 演進）
版本日期：2026-01-01
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX
平行參照：STRATEGY_UNIVERSE / ARCH_FLOW / RISK_COMPLIANCE / VERSION_AUDIT / UI_SPEC / DATA_SOURCES / TWSE_RULES
變更原則：Only-Add（只可新增，不可刪減、不可覆寫、不可改寫既有語義、不可弱化邊界）

## L9–L11 最終語義定錨（單一正確版｜必須一致）

> 本節為 TAITS 在 L9／L10／L11 的**唯一正確語義**。  
> 任何文件中若出現與本節不一致之描述，視為舊錯口徑（不得保留於單一正確版）。

### L9｜投資報告（Investment Report｜可追蹤、可更新、可稽核）
L9 的產出定位為「**給人看的完整投資報告**」，不是一次性的口頭解說；必須可在後續事件/行情變動下持續更新並可追溯。
L9 最低交付物應包含（不限於）：
- **標的化**：標的識別、觀測起點、追蹤狀態（open/hold/watch/exit-candidate 等）、版本號與時間戳。
- **數據**：對應 L1–L8 的關鍵數據表（消息/基本/技術/籌碼/風險/制度），含來源、取樣時間、缺漏註記。
- **圖形**：至少包含價格走勢與關鍵技術指標狀態視覺化（例如均線、RSI、MACD；以「狀態」呈現，非主觀敘事）。
- **進出場建議（非下單）**：建議區間/觸發條件/失效條件（停損/停利/風險撤退），並明確標示「此為建議，不構成下單」。
- **情境更新（Regime/Event）**：當市場制度/事件/風險狀態改變，需能產生增量更新（delta）並保留回放鏈。
- **可稽核鏈**：引用到 L11 的 record_id / ledger_id（或等價識別），以確保報告可被回放與驗證。

### L10｜人類裁決與交易授權（Human Decision & Authorization｜唯一決策點）
L10 的定位為「**人類最高決策者的最終裁決介面與授權層**」。  
- **最終決策者永遠是人類**：你決定採取何種模式與是否授權交易。
- L10 可裁決/授權的動作包含（不限於）：**不動作／回測／模擬／半自動／全自動**。
- AI/Agent 在 L10 僅能提供「選項、理由、風險揭露與建議」，**不得自行構成下單行為**；下單/執行屬於 L10 授權後由執行控制規範承接。

### L11｜工程稽核與全層回放（Engineering Audit & Replay｜全層留痕）
L11 的定位為「**工程檢視與稽核回放層**」，不是下單層，也不是只記錄 L10。
- **全層留痕**：L11 必須覆蓋 L1–L11 每一層的關鍵輸入/輸出/裁決/否決/變更理由與時間戳。
- **雙料輸出**：同一筆紀錄需同時具備  
  1) 人話可讀（你能看懂，用於檢視系統是否合理）  
  2) 工程可用（可重現、可驗證、可追溯，用於開發/稽核/回放）
- **目的**：用來檢查每一層的功能是否合理、是否需要調整、以及自動/半自動/全自動在不同時點的決策依據是否一致可回放。

核心宣告：Feature ≠ Signal ≠ Strategy ≠ Order（特徵非訊號、非策略、非下單）

---
---

# TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219
doc_key：STRATEGY_FEATURE_INDEX
治理等級：B+（Feature Governance & Semantic Boundary Charter｜全知識自洽最大完備版）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（特徵層治理封頂＋可展開知識索引，Only-Add 演進）
版本日期：2026-01-01
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX
平行參照：STRATEGY_UNIVERSE / ARCH_FLOW / RISK_COMPLIANCE / VERSION_AUDIT / UI_SPEC / DATA_SOURCES / TWSE_RULES
變更原則：Only-Add（只可新增，不可刪減、不可覆寫、不可改寫既有語義、不可弱化邊界）
核心宣告：Feature ≠ Signal ≠ Strategy ≠ Order（特徵非訊號、非策略、非下單）

---

# Part 2｜附錄A：Feature ID 命名規範與範例全集（最大完備）

> 本 Part 2 為 Part 1 的 **Only-Add 擴充**，不改寫、不覆蓋任何既有語義。
> 目的：讓 TAITS 在「新增特徵」時能保持跨版本一致、跨 Agent 一致、跨模式一致（Research/Backtest/Sim/Paper/Live）。

---

## A0. 附錄定位（為什麼一定要有命名規範）

若沒有嚴格命名規範，會出現下列治理災難（必須避免）：
- 同一個 Feature 被不同人/不同 Agent 用不同名字重複發明（版本混亂）
- 不同 Feature 被叫同一個名字（語義污染）
- Feature 被「偷偷信號化」：在命名中暗示買賣與方向（治理違規但難被抓）
- 回放時無法知道當時到底計算的是哪一個版本、哪一個公式（Replay 失效）
- UI/審計無法可靠聚合（Evidence 缺口）

因此本附錄的定位是：
> **命名本身就是治理的一部分**（Naming is Governance）。

---

## A1. Feature ID 的正式格式（不可縮減）

### A1.1 標準 Feature ID
推薦格式（必須遵守欄位意義；分隔符可以 Only-Add 增強但不可改寫語義）：

`FTR.<DOMAIN>.<FAMILY>.<NAME>.<VER>`

- `FTR`：固定前綴（Feature）
- `DOMAIN`：資料面向域（見 A2）
- `FAMILY`：家族分類（見 A3）
- `NAME`：特徵名稱（描述性、無方向性）
- `VER`：語義版本（例如 `v1`, `v2`；不可省略）

範例：
- `FTR.TECH.TREND.GMMA_BAND_STRUCTURE.v1`
- `FTR.STRUCT.WYCKOFF.PHASE_LABEL.v1`
- `FTR.STRUCT.CHANLUN.DIVERGENCE_SCORE.v1`

### A1.2 可選擴充段（Only-Add）
若需更精確管理，可加上「可選擴充段」，但不得破壞標準欄位語義：

`FTR.<DOMAIN>.<FAMILY>.<NAME>.<VER>__<IMPL>__<TF>__<SRC>`

- `IMPL`：實作標記（僅標記演算法實作版本，不得影響語義）
- `TF`：週期標記（例如 `1D`, `5m`）
- `SRC`：來源標記（例如 `TWSE`, `TAIFEX`, `BROKER`, `ALT`）

範例（更嚴格版本管理）：
- `FTR.TECH.VOL.ATR_LEVEL.v1__implA__1D__TWSE`
- `FTR.FUND.VAL.PE_PERCENTILE.v2__implB__1D__MOPS`
- `FTR.FLOW.LIQ.SPREAD_LEVEL.v1__implA__Tick__BROKER`

---

## A2. DOMAIN（資料面向域）標準字典（最大完備）

> DOMAIN 是 Feature 的「法定領域」；用錯 DOMAIN 視為語義污染。

- `TECH`：技術面（價格/量能衍生）
- `STRUCT`：結構（區間/段落/中樞/階段等）
- `FUND`：基本面（財報/估值/品質/成長）
- `FLOW`：籌碼/交易行為（參與度、法人、流向）
- `LIQ`：流動性（深度/點差/成交可行性）
- `VOL`：波動（波動水平、波動型態）
- `EVENT`：事件/公告/時間窗（非方向）
- `SENT`：情緒/文本（僅描述，需證據追溯）
- `MACRO`：宏觀（利率、匯率、景氣、政策）
- `RISK`：風險描述（曝險度量、壓力狀態描述；不得變成 gate）
- `EXEC`：執行觀測（延遲、拒單率、對帳一致性描述；不得作策略）
- `GOV`：治理觀測（完整度、缺口、版本一致性描述）
- `QA`：資料品質（缺值率、延遲、異常標記）
- `META`：元特徵（feature_of_feature；嚴禁方向化）

📌 注意：
- `LIQ` 與 `VOL` 可視為 `TECH` 的子域，但在治理上必須可獨立引用，所以保留獨立 DOMAIN。
- `RISK`/`EXEC`/`GOV`/`QA` 只能描述狀態，絕不可取代 Gate 或下單判斷。

---

## A3. FAMILY（家族分類）標準字典（最大完備）

> FAMILY 用來統一語義聚合（UI/審計/研究）；同一 Feature 家族下不得混入方向性。

### A3.1 TECH/STRUCT 常用 FAMILY
- `TREND`：趨勢結構（描述延續性/有序性）
- `MOM`：動能（描述加速度/衰減）
- `VOL`：波動（描述水平/型態）
- `RANGE`：區間/盤整（描述區間邊界與有效性）
- `BREAK`：結構破壞/轉換（描述轉換狀態，不是突破信號）
- `PATTERN`：型態（描述辨識結果與完備度）
- `LEVEL`：位置/價位相對關係（描述相對位置）
- `DIVERGE`：背離/背馳（描述程度，不是反轉）
- `PHASE`：階段（描述階段標籤）
- `CENTER`：中樞/樞紐（描述狀態與關係）

### A3.2 FUND 常用 FAMILY
- `VAL`：估值
- `QUAL`：品質
- `GROW`：成長
- `LEV`：槓桿/償債
- `CASH`：現金流
- `MARGIN`：毛利/營益等
- `STAB`：穩定性（波動、連續性）

### A3.3 FLOW/LIQ 常用 FAMILY
- `PARTIC`：參與度（換手、量能結構）
- `INST`：法人/大戶（描述流向）
- `DEPTH`：深度
- `SPREAD`：點差
- `IMPACT`：衝擊成本（估計）
- `BAL`：供需平衡（描述）
- `RATE`：速率（成交/委託/取消等，描述）

### A3.4 EVENT/SENT/MACRO 常用 FAMILY
- `CAL`：日曆/窗口（財報/除權息/公告）
- `FLAG`：事件旗標（存在與否）
- `DENS`：密度（事件密度/新聞密度）
- `POL`：政策/制度時點（描述）
- `MOOD`：情緒狀態（描述）
- `TOPIC`：主題（描述）
- `SURP`：驚喜/偏離（描述）

### A3.5 QA/GOV/EXEC 常用 FAMILY
- `MISS`：缺失（缺值/缺檔）
- `DELAY`：延遲
- `ANOM`：異常
- `CONSIS`：一致性（版本/對帳）
- `HEALTH`：健康度（通道/服務）
- `COVER`：覆蓋度（審計覆蓋/證據覆蓋）
- `REPLAY`：可回放度（描述）

---

## A4. NAME（特徵名稱）治理規則（硬門檻）

### A4.1 必須是描述性（Descriptive）
名稱只能描述「狀態/關係/程度/標籤」，不得描述行為或方向。

✅ 合法例：
- `BAND_STRUCTURE`、`PHASE_LABEL`、`DIVERGENCE_SCORE`、`SPREAD_LEVEL`、`DEPTH_STRESS`

❌ 非法例（方向化/行為化）：
- `BUY_SIGNAL`、`SELL_SIGNAL`、`LONG_ENTRY`、`SHORT_EXIT`、`STRONG_BUY`、`MUST_RISE`

違規碼（本文件內部，用於審計標記）：
- `GOV-FTR-NAME-DIRECTIONAL`：命名含方向
- `GOV-FTR-NAME-ACTION`：命名含行為
- `GOV-FTR-NAME-PERF`：命名含績效承諾（win/profit等）

### A4.2 不得把策略/方法論當成方向
可以寫方法論標籤（tags），但名稱仍需保持描述性。

✅ 合法：`WYCKOFF_PHASE_LABEL` / `CHANLUN_CENTER_STATE`
❌ 非法：`WYCKOFF_BUY_ZONE` / `CHANLUN_REVERSAL_SIGNAL`

---

## A5. VER（語義版本）規則（必須可回放）

### A5.1 什麼情況要升 VER（語義版本）
只要改到以下任一項，就必須升 `v#`：
- output_semantics（輸出語義）
- output_type（輸出型態）
- 欄位定義（例如 score 的範圍從 0~1 改成 -1~1）
- 品質檢查與缺值處理語義（會影響輸出）

### A5.2 什麼情況不能升 VER（只能改 impl）
- 演算法實作優化但不改語義（例如加速、不同程式實作）
→ 用 `__implX` 記錄，不可用 `v#` 假裝語義有變。

---

## A6. FeatureMeta 必備欄位（用於新對話可展開）

> 本節把 Part 1 的 schema 具體化成「建檔模板」。
> 任何新增 Feature，必須能寫出下面這段（可直接貼到 repo / 文檔）。

### A6.1 FeatureMeta Template（可貼用）
```yaml
feature_id: "FTR.<DOMAIN>.<FAMILY>.<NAME>.v1"
feature_name_zh: "<中文名稱>"
feature_name_en: "<English Name, optional>"
domain: "<DOMAIN>"
family: "<FAMILY>"
methodology_tags: ["<GMMA|Wyckoff|ChanLun_Bodick|...>"]
timeframe: "<Tick|1m|5m|1D|1W|...>"
inputs:
 - "<canonical_field_or_datasource_field_1>"
 - "<...>"
lookahead_policy: "NO_LOOKAHEAD"
data_latency: "<REALTIME|DELAYED|ANNOUNCEMENT_LAG|SPARSE>"
output_type: "<Scalar|Vector|Label|State|Distribution>"
output_semantics: "<描述性語義，不含方向>"
quality_checks:
 - "<missing_value_handling>"
 - "<halt/suspension handling>"
 - "<outlier handling>"
audit_requirements:
 must_have:
 - correlation_id
 - snapshot_ref
 - provenance_map_ref
 - input_hash
 - output_hash
allowed_uses:
 - "EVIDENCE_INPUT"
 - "REGIME_INPUT"
 - "AUDIT_EXPLAIN"
forbidden_uses:
 - "DIRECT_SIGNAL"
 - "DIRECT_STRATEGY"
 - "DIRECT_ORDER"
notes_zh: "<備註：常見陷阱、資料延遲、適用條件>"
A7. 範例全集（最大完備｜可供 STRATEGY_UNIVERSE 直接引用）
下列範例以「可擴充」方式提供；不是限制清單。
你可在未來 Only-Add 新增更多 Feature，不得覆寫本段既有語義。

A7.1 GMMA 範例（TECH.TREND）
FTR.TECH.TREND.GMMA_BAND_STRUCTURE.v1

zh：GMMA 群組結構有序度

output_semantics：群組排列與分層的有序程度（0~1）

FTR.TECH.TREND.GMMA_BAND_SPREAD_STATE.v1

zh：GMMA 群組擴張/收斂狀態

output_semantics：{CONTRACTING, NEUTRAL, EXPANDING}

FTR.TECH.TREND.GMMA_SLOPE_CONSISTENCY.v1

zh：GMMA 群組斜率一致性

output_semantics：短長群斜率一致程度（0~1）

FTR.TECH.STRUCT.GMMA_PHASE_LABEL.v1

zh：GMMA 階段標籤（描述性）

output_semantics：{ORDERLY_TREND, COMPRESSION_RANGE, DISTORTION_TRANSITION, UNKNOWN}

A7.2 顧比倒數線 範例（TECH.MOM）
FTR.TECH.MOM.GUPPY_COUNTDOWN_STATE.v1

zh：顧比倒數狀態

output_semantics：{RUNNING, COMPLETED, RESET, INVALID}

FTR.TECH.MOM.GUPPY_COUNTDOWN_PROGRESS.v1

zh：顧比倒數進度

output_semantics：0~1（進度；不代表方向）

FTR.TECH.MOM.GUPPY_COUNTDOWN_INTENSITY.v1

zh：顧比倒數強度

output_semantics：0~1（強度；不代表建議）

A7.3 威科夫 範例（STRUCT.PHASE / STRUCT.EVENT）
FTR.STRUCT.PHASE.WYCKOFF_PHASE_LABEL.v1

zh：威科夫階段標籤

output_semantics：{A,B,C,D,E,UNKNOWN}

FTR.STRUCT.EVENT.WYCKOFF_EVENT_FLAGS.v1

zh：威科夫事件旗標集合

output_semantics：事件集合（PS/SC/AR/ST/SOS/LPS…）的存在標記（非方向）

FTR.STRUCT.RANGE.WYCKOFF_RANGE_VALIDITY.v1

zh：威科夫區間有效性

output_semantics：區間邊界穩定度/有效性（0~1）

FTR.STRUCT.BAL.WYCKOFF_SUPPLY_DEMAND_BALANCE.v1

zh：供需平衡度量

output_semantics：供需偏移程度（描述性，需明示範圍）

FTR.STRUCT.DIVERGE.WYCKOFF_EFFORT_RESULT_DIVERGENCE.v1

zh：努力/結果背離程度

output_semantics：背離程度（0~1）

A7.4 纏論｜鮑迪克版本 範例（STRUCT.CENTER / STRUCT.DIVERGE）
FTR.STRUCT.CENTER.CHANLUN_ZS_CENTER_STATE.v1

zh：纏論中樞狀態

output_semantics：{FORMING, EXPANDING, BROKEN, REBUILT}

FTR.STRUCT.CENTER.CHANLUN_PIVOT_RELATION.v1

zh：中樞相對關係

output_semantics：{UPSHIFT, DOWNSHIFT, OVERLAP, DISPERSE}

FTR.STRUCT.PATTERN.CHANLUN_BI_SEGMENT_STATE.v1

zh：筆段落狀態

output_semantics：{FORMING, EXTENDING, COMPLETED}

FTR.STRUCT.DIVERGE.CHANLUN_DIVERGENCE_SCORE.v1

zh：背馳程度

output_semantics：0~1（描述程度）

FTR.STRUCT.META.CHANLUN_STRUCTURE_COMPLETENESS.v1

zh：結構完備度

output_semantics：0~1（描述完整度，不是可交易性）

A7.5 波動/流動性 範例（VOL / LIQ）
FTR.VOL.VOL.ATR_LEVEL.v1

zh：ATR 波動水平

output_semantics：波動水平（數值＋標準化版本）

FTR.VOL.VOL.VOLATILITY_COMPRESSION_STATE.v1

zh：波動收斂狀態

output_semantics：{COMPRESSING, NEUTRAL, EXPANDING}

FTR.LIQ.SPREAD.SPREAD_LEVEL.v1

zh：點差水平

output_semantics：點差（ticks / bps）

FTR.LIQ.DEPTH.DEPTH_STRESS.v1

zh：深度壓力

output_semantics：深度不足程度（0~1 或分級）

FTR.LIQ.IMPACT.PRICE_IMPACT_ESTIMATE.v1

zh：衝擊成本估計

output_semantics：估計衝擊成本（bps，描述）

A7.6 基本面 範例（FUND.*）
FTR.FUND.VAL.PE_PERCENTILE.v1

zh：本益比分位數

output_semantics：0~1（分位；需明示資料窗口）

FTR.FUND.VAL.PB_PERCENTILE.v1

zh：股價淨值比分位數

output_semantics：0~1

FTR.FUND.QUAL.ROE_LEVEL.v1

zh：ROE 水平

output_semantics：ROE（數值＋期間）

FTR.FUND.GROW.REVENUE_YOY_RATE.v1

zh：營收年增率

output_semantics：YoY（描述；需公告可得時間）

FTR.FUND.CASH.CFO_QUALITY_SCORE.v1

zh：現金流品質分數

output_semantics：品質分數（描述性）

📌 FUND 類一律必填：

data_latency=ANNOUNCEMENT_LAG

lookahead_policy=NO_LOOKAHEAD
並要求 available_at（何時可得）寫入 provenance/audit（不得用事後值）。

A7.7 事件/情緒/宏觀 範例（EVENT/SENT/MACRO）
FTR.EVENT.FLAG.EARNINGS_WINDOW_FLAG.v1

zh：財報窗口旗標

output_semantics：{IN_WINDOW, OUT_WINDOW}

FTR.EVENT.DENS.NEWS_DENSITY_LEVEL.v1

zh：新聞密度水平

output_semantics：密度（描述性）

FTR.SENT.MOOD.SENTIMENT_POLARITY_SCORE.v1

zh：情緒極性分數

output_semantics：-1~1（描述性；不得命名為多空）

FTR.MACRO.POL.RATE_DECISION_FLAG.v1

zh：利率決策時點旗標

output_semantics：{UPCOMING, RECENT, NONE}

A7.8 QA/GOV/EXEC 範例（治理觀測）
FTR.QA.MISS.MISSING_RATE.v1

zh：缺值率

output_semantics：0~1

FTR.QA.DELAY.DATA_LATENCY_MS.v1

zh：資料延遲毫秒

output_semantics：延遲（ms）

FTR.GOV.COVER.AUDIT_COVERAGE_SCORE.v1

zh：審計覆蓋分數

output_semantics：0~1（描述性）

FTR.EXEC.HEALTH.CHANNEL_HEALTH_STATE.v1

zh：通道健康狀態

output_semantics：{OK, DEGRADED, DOWN}

FTR.EXEC.CONSIS.RECONCILIATION_STATE.v1

zh：對帳一致性狀態

output_semantics：{CONSISTENT, INCONSISTENT, UNKNOWN}

A8. 命名與審計的連動規則（必須落地）
A8.1 審計必須記錄 Feature ID（全字串）
任何 Feature 的輸出若被納入 Evidence，審計物必須包含：

feature_id（含 ver）

若有擴充段：完整保留 __impl__tf__src

A8.2 UI 顯示規則（最小要求）
UI 不必顯示完整 feature_id（可顯示中文名），但必須能「展開」看到：

feature_id

feature_version

inputs（最小集合）

output_semantics

A8.3 命名違規的 Gate（建議落在 GOV/QA）
若命名違規（含方向詞、行為詞、績效詞）：

必須阻止其被納入 Evidence（RETURN 或 VETO，依政策）

必須留下審計原因碼：

GOV-FTR-NAME-DIRECTIONAL

GOV-FTR-NAME-ACTION

GOV-FTR-NAME-PERF

A9. Only-Add 演進規則（附錄 A 專屬）
允許新增：

新 DOMAIN（但必須補齊語義與邊界）

新 FAMILY

新命名範例

新 FeatureMeta 欄位（不得刪舊欄位）

禁止：

改寫既有 DOMAIN/FAMILY 的語義

把方向/行為/績效詞合法化

用「簡化」名義刪除版本段（VER）

（STRATEGY_FEATURE_INDEX｜Part 2：附錄A v2026-01-01 完）

# TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219
doc_key：STRATEGY_FEATURE_INDEX
治理等級：B+（Feature Governance & Semantic Boundary Charter｜全知識自洽最大完備版）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（特徵層治理封頂＋可展開知識索引，Only-Add 演進）
版本日期：2026-01-01
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX
平行參照：STRATEGY_UNIVERSE / ARCH_FLOW / RISK_COMPLIANCE / VERSION_AUDIT / UI_SPEC / DATA_SOURCES / TWSE_RULES
變更原則：Only-Add（只可新增，不可刪減、不可覆寫、不可改寫既有語義、不可弱化邊界）
核心宣告：Feature ≠ Signal ≠ Strategy ≠ Order（特徵非訊號、非策略、非下單）

---

# Part 3｜附錄B：特徵治理檢核（Feature Governance Checklist）＋違規判定（最大完備）

> 本 Part 3 為 Part 1/Part 2 的 **Only-Add 擴充**。
> 目的：把「特徵」從研究到實盤的全生命週期，落成 **可機器審計、可人類審查、可回放** 的治理規格。
> 本節不新增交易建議、不新增策略、不涉下單；僅規範「特徵」如何被允許/禁止使用。

---

## B0. 本附錄的法律地位（治理定位）

- 本附錄是 STRATEGY_FEATURE_INDEX 的治理子章，屬於 **語義邊界與可審計性** 的最高規格之一。
- 一切「特徵可不可以進入 Evidence」的裁決，必須至少經過本附錄的 Hard Gates。
- 若與上位約束衝突：以 MASTER_ARCH / DOCUMENT_INDEX / AI_GOV 母法裁決。

---

## B1. Feature 分級制度（Feature Tiering｜必須標記）

> Feature 不同成熟度，能用在哪裡不同。
> 分級不是好壞評分，而是 **允許用途（Allowed Uses）** 的治理欄位。

### B1.1 Feature Tier 定義（最小集合）
- **T0｜Draft（草稿）**
 - 允許：Research 局部實驗（不得入 Evidence）
 - 禁止：Backtest/Sim/Paper/Live 的 Canonical Evidence
- **T1｜Research-Validated（研究驗證）**
 - 允許：Research / Backtest（可入 Evidence 但需標記實驗）
 - 禁止：Paper/Live（除非升級到 T2）
- **T2｜Replay-Safe（可回放安全）**
 - 允許：Research / Backtest / Simulation / Paper
 - 條件：provenance + version_ref + deterministic replay 成立
- **T3｜Live-Allowed（可進實盤）**
 - 允許：全模式（含 Live）
 - 條件：資料延遲/缺值/異常處理被制度化；風控可理解其語義
- **T4｜Critical（關鍵特徵）**
 - 允許：全模式
 - 額外要求：變更需更嚴格審批（VERSION_AUDIT 加強）

### B1.2 FeatureMeta 必填欄位（新增：tier）
任何 FeatureMeta 必須包含：
- `tier: T0|T1|T2|T3|T4`

---

## B2. Feature Hard Gates（逐條寫滿｜不可省略）

> 下列任一 Gate 失敗：
> - 至少 RETURN（禁止納入 Evidence）
> - 在 Live 風險鏈路中可升級為 VETO（依政策）

### B2.1 Gate-1：語義邊界（Semantic Boundary）
檢核點（全部通過）：
- Feature 的 `output_semantics` 只描述狀態/關係/程度/標籤
- Feature 名稱不含方向/行為/績效承諾（見 Part 2 A4）
- Feature 不在輸出中直接提供 `buy/sell/long/short/entry/exit` 類字段

Fail → 原因碼（本文件內部用於審計標記）：
- `GOV-FTR-SEM-DIRECTIONAL`
- `GOV-FTR-SEM-ACTION`
- `GOV-FTR-SEM-PERF`

### B2.2 Gate-2：可追溯性（Provenance）
檢核點（全部通過）：
- inputs 均可追溯到 DATA_SOURCES 的來源項目
- 必有 `provenance_map_ref`
- 必有 `input_hash` / `output_hash`

Fail → 原因碼：
- `GOV-FTR-PROV-MISSING`
- `GOV-FTR-PROV-BROKEN`
- `GOV-FTR-HASH-MISSING`
- `GOV-FTR-HASH-FAIL`

### B2.3 Gate-3：無前視（No Lookahead）
檢核點（全部通過）：
- `lookahead_policy=NO_LOOKAHEAD`
- FUND/EVENT 類必記錄 `available_at`（資料可得時間）
- 回測/回放時使用「當時可得版本」

Fail → 原因碼：
- `GOV-FTR-LOOKAHEAD`
- `GOV-FTR-AVAILABLE_AT-MISSING`

### B2.4 Gate-4：回放一致性（Replay Determinism）
檢核點（全部通過）：
- 相同 replay bundle + 相同版本 → 相同輸出
- 若使用隨機或外部服務：必有 deterministic 設定或快照固化

Fail → 原因碼：
- `GOV-FTR-REPLAY-NONDET`
- `GOV-FTR-REPLAY-NOSNAPSHOT`

### B2.5 Gate-5：缺值/異常處理制度化（Robustness）
檢核點（全部通過）：
- `quality_checks` 明確定義缺值處理語義
- 停牌/分盤/撮合異常時的處理定義存在
- Outlier（極端值）處理語義存在（若該 domain 需要）

Fail → 原因碼：
- `GOV-FTR-QA-MISSING`
- `GOV-FTR-HALT-HANDLING-MISSING`
- `GOV-FTR-OUTLIER-HANDLING-MISSING`

### B2.6 Gate-6：用途白名單（Allowed Uses）
檢核點（全部通過）：
- `allowed_uses` 僅包含：
 - `EVIDENCE_INPUT`
 - `REGIME_INPUT`
 - `AUDIT_EXPLAIN`
 - `UI_EXPLAIN`
 - `RISK_CONTEXT_ONLY`（若要給風控只能是上下文，不是決策）
- `forbidden_uses` 必包含：
 - `DIRECT_SIGNAL`
 - `DIRECT_STRATEGY`
 - `DIRECT_ORDER`

Fail → 原因碼：
- `GOV-FTR-USE-ILLEGAL`
- `GOV-FTR-USE-WHITELIST-MISSING`

---

## B3. Feature → Evidence 的納入規則（Evidence Ingestion Rules）

> Feature 進 Evidence 不是「加就好」，必須可被審計與可被解釋。

### B3.1 Evidence 允許載入的 Feature 類型
允許（示例）：
- 描述性：結構狀態、區間有效性、波動水平、流動性壓力、估值分位數、事件旗標
- 不允許任何含「交易行為指令」的輸出

### B3.2 Evidence 必須記錄的 Feature 欄位（最小集合）
- `feature_id`
- `feature_version`
- `inputs_ref`（可指向 snapshot/provenance）
- `output_value_ref`（或 hash）
- `computed_at`
- `available_at`（若資料為公告型/延遲型）
- `quality_flags`（缺值/異常標記）

### B3.3 Evidence 的「禁止偷換」
- 禁止在 Evidence 層把多個 Feature 合成「方向」字段
- 若要合成，只能形成「更高階描述性 Feature」，且必須：
 - 新 feature_id
 - 新 ver
 - 完整 FeatureMeta
 - 通過本附錄 Hard Gates

違規碼：
- `GOV-EVD-SIGNALIZATION`
- `GOV-EVD-UNREGISTERED-FEATURE`

---

## B4. Feature → Regime 的使用邊界（Regime Input Boundary）

> Regime 是狀態判定，不是交易方向。
> Feature 在 Regime 只能貢獻「狀態證據」，不得導出買賣建議。

### B4.1 Regime 可使用的 Feature 類型（示例）
- 波動壓縮/擴張狀態（VOL）
- 流動性壓力狀態（LIQ）
- 結構階段（STRUCT.PHASE）
- 趨勢有序度（TECH.TREND 的描述性指標）

### B4.2 禁止的 Regime 使用方式
- 以單一 feature 直接決定 regime（除非制度明確定義且有多證據一致性）
- 用「策略績效最好」來調 regime 門檻（績效辯護違規）

違規碼：
- `GOV-REG-SINGLE-FTR-DECISION`
- `GOV-REG-PERF-DRIVEN`

---

## B5. Feature → Risk 的使用邊界（Risk Context Only）

> 風控文件定義 Gate；Feature 只能提供上下文，不能取代 Gate。

### B5.1 Risk 可引用 Feature 的合法方式
- 作為風控計算的「上下文輸入」：
 - 波動水平、點差水平、深度壓力、事件窗口、資料品質狀態
- 但風控 PASS/VETO 必須由 RISK_COMPLIANCE 的條文裁決

### B5.2 禁止事項
- 以 Feature 直接宣告 PASS（Soft Pass）
- 以 Feature 直接宣告 VETO（除非該 feature 本身是風控條文映射的一部分，且已被制度化）
- 用 AI 模型輸出當成風控裁決（除非 RISK_COMPLIANCE 明確允許且可回放）

違規碼：
- `GOV-RISK-SOFTPASS-BY-FTR`
- `GOV-RISK-VETO-BY-FTR-UNAUTHORIZED`
- `GOV-RISK-AI-OVERRIDE`

---

## B6. Feature 生命週期（Lifecycle）與版本控管（VERSION_AUDIT 對位）

### B6.1 Feature 狀態（Status）
- `DRAFT`
- `ACTIVE`
- `DEPRECATED`（保留可回放，但不得用於新決策）
- `RETIRED`（仍可回放，但需更嚴格權限）

### B6.2 變更類型（Change Types）
- `SEMANTIC_CHANGE` → 必升 `VER`
- `IMPLEMENTATION_CHANGE` → 只能改 `__impl`
- `DATA_SOURCE_CHANGE` → 可能升 `VER`（若影響語義）

### B6.3 必備審計輸出（與 VERSION_AUDIT 對位）
每次變更必須產生：
- `change_id`
- `feature_id_before` / `feature_id_after`
- `reason`
- `approver`
- `effective_time`
- `replay_compatibility_note`

---

## B7. 跨文件一致性要求（DOCUMENT_INDEX / STRATEGY_UNIVERSE）

### B7.1 STRATEGY_UNIVERSE 引用 Feature 的規則
- 策略條目中可以引用 Feature ID 作為：
 - Evidence 構成要件
 - 適用條件描述
 - 風控上下文提示
- 但不得引用「未登記 Feature」（未在本文件的索引/模板管理）

違規碼：
- `GOV-STR-REF-UNKNOWN-FTR`
- `GOV-STR-REF-NONINDEX-DOC`（若引用非 Index 文件）

### B7.2 新對話可展開的必要性（你關心的點）
要讓「新對話」能展開，最低要做到：
- Feature ID 命名規範固定
- FeatureMeta template 固定
- 舉例（A7）足夠全面，能指向 GMMA / 顧比倒數 / 威科夫 / 纏論（鮑迪克）等方法論

本 Part 3 的作用就是把上述「展開」變成可審計規則，而不是靠猜。

---

## B8. Mermaid｜Feature 治理 Gate 流程圖（完整）

```mermaid
```
flowchart TB
 F0[New/Updated Feature Proposal] --> G1{Gate-1 Semantic Boundary}
 G1 -->|FAIL| R1[RETURN: Fix Naming/Semantics<br/>Audit: GOV-FTR-SEM-*]
 G1 -->|PASS| G2{Gate-2 Provenance + Hash}
 G2 -->|FAIL| R2[RETURN: Fix Provenance/Hash<br/>Audit: GOV-FTR-PROV/HASH-*]
 G2 -->|PASS| G3{Gate-3 No Lookahead + Available_at}
 G3 -->|FAIL| R3[RETURN: Fix Lookahead/Available_at<br/>Audit: GOV-FTR-LOOKAHEAD]
 G3 -->|PASS| G4{Gate-4 Replay Determinism}
 G4 -->|FAIL| R4[RETURN: Snapshot/Determinism Required<br/>Audit: GOV-FTR-REPLAY-*]
 G4 -->|PASS| G5{Gate-5 Robust QA Handling}
 G5 -->|FAIL| R5[RETURN: Define QA/Halt/Outlier Handling<br/>Audit: GOV-FTR-QA-*]
 G5 -->|PASS| G6{Gate-6 Allowed/Forbidden Uses}
 G6 -->|FAIL| R6[RETURN: Fix Uses Whitelist/Blacklist<br/>Audit: GOV-FTR-USE-*]
 G6 -->|PASS| A1[APPROVE: Feature Eligible for Evidence/Regime Use<br/>Tier Controls Apply]
B9. Only-Add 演進規則（Part 3 專屬）
允許新增：

新的 Gate 檢核點（更嚴格）

新的違規原因碼（reason_code）

新的 Feature Tier（但不得放寬既有 Tier 的限制）

新的範例與模板欄位（不得移除既有欄位）

禁止：

刪除任何 Hard Gate

把方向化命名合法化

允許 Feature 直接成為策略或下單指令

以「研究方便」為理由跳過 provenance / replay / no-lookahead

（STRATEGY_FEATURE_INDEX｜Part 3：附錄B v2026-01-01 完）

# TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219
doc_key：STRATEGY_FEATURE_INDEX
治理等級：B+（Feature Governance & Semantic Boundary Charter｜全知識自洽最大完備版）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（特徵層治理封頂＋可展開知識索引，Only-Add 演進）
版本日期：2026-01-01
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX
平行參照：STRATEGY_UNIVERSE / ARCH_FLOW / RISK_COMPLIANCE / VERSION_AUDIT / UI_SPEC / DATA_SOURCES / TWSE_RULES
變更原則：Only-Add（只可新增，不可刪減、不可覆寫、不可改寫既有語義、不可弱化邊界）
核心宣告：Feature ≠ Signal ≠ Strategy ≠ Order（特徵非訊號、非策略、非下單）

---

# Part 4｜附錄C：特徵資料結構模板（Schema）＋落地範例（Examples）＋UI/審計對位（最大完備）

> 本 Part 4 為 Part 1/Part 2/Part 3 的 **Only-Add 擴充**。
> 目的：提供「可直接貼用」的特徵資料結構模板（FeatureMeta / FeatureValue / ProvenanceMap / QualityFlags），
> 並補齊 GMMA、顧比倒數線、威科夫、纏論（鮑迪克）等方法論在 TAITS 中的 **特徵化落地範例**（注意：只做描述性特徵，不輸出交易方向）。

---

## C0. 附錄C的使用邊界（不可越權）

- 本附錄提供「結構化模板」與「描述性特徵範例」：
 - ✅ 可用於 L4 Feature Engine / L5 Evidence Builder / UI Explain / Audit Replay
 - ✅ 可用於 STRATEGY_UNIVERSE 的策略條目備註引用（以 feature_id 引用）
 - ❌ 不得直接變成策略規則（策略在 STRATEGY_UNIVERSE 定義）
 - ❌ 不得直接變成下單信號（下單在 EXECUTION_CONTROL，且需 Human + Risk Token）

---

## C1. FeatureMeta 模板（Canonical Template｜最小必備欄位）

> FeatureMeta 是「特徵定義本體」，屬於治理物件：必須版控、可審計、可回放。
> 任何特徵進入 Evidence/Regime/Risk Context/UI Explain，都必須先有 FeatureMeta。

```yaml
feature_meta:
 feature_id: "TECH.TREND.GMMA_SPREAD_RATIO"
 feature_name_zh: "GMMA長短群均線擴散比（描述性）"
 feature_name_en: "GMMA Spread Ratio (Descriptive)"
 domain: "TECH" # TECH/FUND/NEWS/MACRO/MKT/STRUCT/LIQ/ORDERFLOW/RISK/SYS/EVENT
 family: "TREND" # 族群分類：TREND/MOMENTUM/VOL/LIQ/STRUCT/VALUATION/QUALITY/...
 subfamily: "GMMA" # 子族群：GMMA/WYCKOFF/CHANLUN_BODICK/...
 description: >
 描述長短期均線群之間的擴散程度，用於刻畫趨勢有序度與動能狀態，
 僅輸出連續數值，不輸出買賣方向。
 output_semantics: "ratio_non_directional" # 必須是描述性語義
 unit: "ratio"
 value_type: "float" # float/int/bool/category/struct
 value_range: "[0, +inf)"
 default_timeframe: "D" # 1m/5m/15m/60m/D/W/M
 computation:
 formula_summary: "spread = mean(abs(short_group - long_group)/price"
 lookahead_policy: "NO_LOOKAHEAD"
 required_inputs:
 - "PRICE.CLOSE"
 - "TECH.MA(3,5,8,10,12,15,30,35,40,45,50,60)"
 dependencies:
 - "DATA_SOURCES:TWSE_OHLCV"
 - "FEATURES:TECH.MA_GROUPS"
 tier: "T3" # T0/T1/T2/T3/T4
 status: "ACTIVE" # DRAFT/ACTIVE/DEPRECATED/RETIRED
 allowed_uses:
 - "EVIDENCE_INPUT"
 - "REGIME_INPUT"
 - "AUDIT_EXPLAIN"
 - "UI_EXPLAIN"
 forbidden_uses:
 - "DIRECT_SIGNAL"
 - "DIRECT_STRATEGY"
 - "DIRECT_ORDER"
 quality_checks:
 missing_policy: "FLAG" # FLAG/IMPUTE/STOP (STOP 必須升級治理)
 outlier_policy: "WINSORIZE" # NONE/WINSORIZE/FLAG/STOP
 halt_handling: "FREEZE_LAST" # FREEZE_LAST/FLAG/STOP/NA
 provenance_requirements:
 require_provenance_map: true
 require_input_hash: true
 require_output_hash: true
 require_available_at: false # FUND/EVENT/NEWS 類通常 true
 audit_requirements:
 audit_layer: "L4"
 must_emit_artifacts:
 - "FeatureValueRecord"
 - "ProvenanceMapRef"
 - "QualityFlags"
 versioning:
 feature_version: "1.0.0"
 impl_version: "impl_2026-01-01_001"
 change_policy: "SEMANTIC_CHANGE=>bump_feature_version"
 ui_explain:
 explain_level: "L2" # L1/L2/L3（UI_SPEC 對位）
 display_hint: "可視化為趨勢有序度/擴散程度，禁止顯示買賣箭頭"
C2. FeatureValueRecord 模板（值紀錄｜必備可回放）
FeatureValueRecord 是「某一次計算出的特徵值」：必須可回放、可稽核。

json
複製程式碼
{
 "record_type": "FeatureValueRecord",
 "correlation_id": "CID-20251219-000001",
 "session_id": "SID-20251219-000009",
 "timestamp_utc": "2026-01-01T00:01:23Z",
 "market_time": "2026-01-01T13:31:00+08:00",
 "layer_id": "L4",
 "module_id": "FEATURE_ENGINE",
 "feature_id": "TECH.TREND.GMMA_SPREAD_RATIO",
 "feature_version": "1.0.0",
 "impl_version": "impl_2026-01-01_001",
 "instrument": "TWSE:2330",
 "timeframe": "D",
 "value_type": "float",
 "value": 0.0375,
 "value_ref": null,
 "quality_flags": {
 "missing": false,
 "halted": false,
 "outlier": false,
 "source_degraded": false
 },
 "available_at": null,
 "input_hash": "sha256:....",
 "output_hash": "sha256:....",
 "provenance_map_ref": "PROV-20251219-000001",
 "version_ref": {
 "doc_key": ["STRATEGY_FEATURE_INDEX@251219", "DATA_SOURCES@251219"],
 "policy": ["RISK_POLICY@..."],
 "rulebook": ["TWSE_RULES@251219"]
 },
 "status": "SUCCESS",
 "reason_codes": []
}
C3. ProvenanceMap 模板（來源可追溯圖｜必備）
ProvenanceMap 將「特徵值」追溯到「資料來源」與「原始輸入範圍」。
沒有 provenance_map_ref → Part 3 Gate-2 失敗。

json
複製程式碼
{
 "record_type": "ProvenanceMap",
 "provenance_id": "PROV-20251219-000001",
 "correlation_id": "CID-20251219-000001",
 "created_at_utc": "2026-01-01T00:01:23Z",
 "instrument": "TWSE:2330",
 "timeframe": "D",
 "inputs": [
 {
 "field": "PRICE.CLOSE",
 "source": "DATA_SOURCES:TWSE_OHLCV",
 "source_priority": "OFFICIAL_PRIMARY",
 "time_range": ["2025-10-01", "2026-01-01"],
 "raw_ref": "RAWSET-...-CLOSE",
 "transform_chain": ["canonicalize", "adjust_corporate_actions"]
 },
 {
 "field": "TECH.MA_GROUPS",
 "source": "FEATURES:TECH.MA_GROUPS",
 "source_priority": "INTERNAL_DERIVED",
 "time_range": ["2025-10-01", "2026-01-01"],
 "raw_ref": "FTRSET-...-MA",
 "transform_chain": ["ma_calc", "group_aggregate"]
 }
 ],
 "integrity": {
 "input_hashes": ["sha256:...","sha256:..."],
 "provenance_hash": "sha256:..."
 }
}
C4. QualityFlags / Degrade Policy（品質旗標與降級語義）
注意：降級只影響「可用性」與「標記」，不得偷偷修正成方向或掩蓋缺失。

C4.1 QualityFlags（最小集合）
missing：缺值（含任一關鍵輸入缺失）

halted：停牌/不可交易狀態

outlier：極端值

source_degraded：來源降級（官方→備援）

stale：資料過舊（延遲超過門檻）

late_available：公告型資料尚未可得（FUND/EVENT）

C4.2 降級語義（示例）
FLAG：保留值或設為 null，但必標記並在 Evidence 顯示不完整

STOP：停止輸出，Evidence 不得使用（可 RETURN）

IMPUTE：僅限研究/回測且明示（Live 不建議，除非制度化）

C5. 方法論落地範例（Descriptive Feature Examples｜最大完備）
本節是你最在意的「備註可展開」落地：
把 GMMA / 顧比倒數線 / 威科夫 / 纏論（鮑迪克）各自拆成「描述性特徵」可引用。
這些特徵不產生買賣方向，只提供可解釋的狀態刻畫，供 Evidence/Regime/策略條目備註引用。

C5.1 GMMA（顧比均線群）特徵族（TECH.TREND.GMMA_*）
GMMA 本質：短期群與長期群的相對位置、擴散、收斂、斜率狀態（全部描述性）。

GMMA-A：群擴散程度（已於 C1 範例）
TECH.TREND.GMMA_SPREAD_RATIO

語義：短群 vs 長群的擴散程度（越大代表趨勢有序度可能更強，但不等於做多/做空）

GMMA-B：群相對位階（短群在上/下）
TECH.TREND.GMMA_STACKING_STATE

value_type：category（SHORT_ABOVE_LONG / MIXED / SHORT_BELOW_LONG）

禁止：把 SHORT_ABOVE_LONG 直接當買進

GMMA-C：群收斂狀態（壓縮/擴張）
TECH.TREND.GMMA_COMPRESSION_STATE

value_type：category（COMPRESSING / EXPANDING / NEUTRAL）

可用於 Regime：趨勢狀態/盤整狀態的證據之一

GMMA-D：長群斜率穩定性（趨勢穩定）
TECH.TREND.GMMA_LONG_SLOPE_STABILITY

value_type：float（例如斜率變異係數）

用途：描述「趨勢是否穩定」，非方向

C5.2 顧比倒數線（Guppy Countdown）特徵族（TECH.MOMENTUM.COUNTDOWN_*）
倒數線常用於「節奏」與「耗竭」的描述：用倒數進度而非訊號。

CD-A：倒數進度（0~N）
TECH.MOMENTUM.COUNTDOWN_PROGRESS

value_type：int

語義：當前處於倒數序列的進度（例如 0..13）

禁止：進度達到 N 直接視為反轉訊號（那是策略層）

CD-B：倒數條件完整度
TECH.MOMENTUM.COUNTDOWN_CONDITION_COVERAGE

value_type：float（0..1）

語義：倒數必要條件滿足比例（描述性）

CD-C：倒數中斷原因（若中斷）
TECH.MOMENTUM.COUNTDOWN_INTERRUPT_REASON

value_type：category

語義：倒數為何中斷（缺資料/狀態不符/停牌等）

C5.3 威科夫（Wyckoff）特徵族（STRUCT.WYCKOFF_*）
威科夫屬「結構/階段」：以階段、事件、供需特徵刻畫，不輸出方向。

WY-A：階段標籤（Phase）
STRUCT.WYCKOFF_PHASE_LABEL

category：ACCUMULATION / MARKUP / DISTRIBUTION / MARKDOWN / UNKNOWN

注意：此為「結構推定狀態」，必須多證據一致性（Volume/Range/Trend/Support/Resistance 等）

WY-B：供需不平衡強度（Supply-Demand Imbalance）
STRUCT.WYCKOFF_SDI_SCORE

float：供需不平衡程度（描述性 score）

WY-C：事件旗標（事件不等於交易）
STRUCT.WYCKOFF_EVENT_FLAG

category（可多值）：SC/AR/ST/SPRING/UTAD/NONE

禁止：把 SPRING 直接當買進信號（策略層才能決定）

WY-D：成交量-價差關係（VSA 風格的描述）
STRUCT.WYCKOFF_VOLUME_SPREAD_RELATION

category：WIDE_SPREAD_HIGH_VOL / NARROW_SPREAD_HIGH_VOL / ...

用途：Evidence 或 UI Explain

C5.4 纏論（鮑迪克纏論）特徵族（STRUCT.CHANLUN_BODICK_*）
纏論（作為結構與判斷體系）在 TAITS 中落地方式：
以「結構段落、筆/線段/中樞、背離狀態、級別一致性」等描述性特徵輸出。

CLB-A：結構級別（Level）
STRUCT.CHANLUN_BODICK_LEVEL

category：MINOR/MAJOR/MULTI_LEVEL（或你在母法中定義的級別體系）

用途：標記當前結構解析所屬級別

CLB-B：中樞存在性與範圍
STRUCT.CHANLUN_BODICK_ZS_EXISTS

bool：是否存在有效中樞（描述性）

STRUCT.CHANLUN_BODICK_ZS_RANGE

struct：{low, high, width_ratio}（描述性）

CLB-C：筆/線段方向（僅結構方向，不是交易方向）
STRUCT.CHANLUN_BODICK_SEGMENT_DIRECTION

category：UP_SEGMENT / DOWN_SEGMENT / UNKNOWN

禁止：把 UP_SEGMENT 直接視為買入（策略層再用）

CLB-D：背離狀態（Divergence State）
STRUCT.CHANLUN_BODICK_DIVERGENCE_STATE

category：NONE/WEAK/STRONG/UNDETERMINED

必須記錄：使用的動能/量能/價格結構依據（provenance）

CLB-E：多級別一致性（Alignment）
STRUCT.CHANLUN_BODICK_MULTI_LEVEL_ALIGNMENT

float：0..1（各級別結構一致程度）

用途：Regime / Evidence（描述性）

C6. UI_EXPLAIN 對位（與 UI_SPEC 的接口欄位）
本節定義 Feature 在 UI 上的最小呈現義務（不取代 UI_SPEC，只提供接口一致性）。

C6.1 UI 必須能顯示（可展開）
feature_name_zh

feature_value（含 unit）

quality_flags

provenance_map_ref（可點開顯示來源）

computed_at / market_time

feature_version / impl_version

C6.2 UI 禁止顯示方式
禁止直接以箭頭/顏色暗示買賣（除非 UI 明確標示「這是描述性狀態」且不作交易引導）

禁止把 Feature 當作 PASS/VETO（Risk 仍由 RISK_COMPLIANCE 裁決）

C7. 審計輸出（Audit Artifacts）最小清單（對位 ARCH_FLOW / VERSION_AUDIT）
Feature 層（L4）至少必須輸出：

FeatureValueRecord（每個 feature 每次計算）

ProvenanceMap（可聚合但不可缺）

QualityFlags

VersionRef（doc_key/policy/rulebook/impl）

Hash（input/output/provenance）

若缺任一項：

在 Live/Paper 可升級為風控否決（SYS-AUDIT / SYS-PROV）

C8. Mermaid｜Feature → Evidence → Regime 的合法流（完整）
mermaid
複製程式碼
flowchart TB
 L3[Snapshot Ready] --> L4[Feature Engine<br/>Compute FeatureValueRecords]
 L4 --> P[ProvenanceMap + Hash + QualityFlags]
 P --> G{Feature Governance Gates<br/>Part3 Gate-1..6}
 G -->|FAIL| R[RETURN: Fix Feature Meta/Provenance/Replay]
 G -->|PASS| L5[Evidence Builder<br/>Assemble Evidence Bundle]
 L5 --> L6[Regime Engine<br/>State Classification]
 L6 --> L7[Risk & Compliance Gate<br/>PASS/VETO]
C9. Only-Add 演進規則（Part 4 專屬）
允許新增：

新的 FeatureMeta 欄位（不得刪舊欄位）

新的方法論特徵族（如新增新的 ChanLun 子系）

新的 UI 提示欄位（不得弱化風險揭露）

新的品質旗標與來源映射

禁止：

任何把描述性特徵偷換成方向/信號/策略/下單意圖的改動

刪除 Provenance / Hash / Replay 必備欄位

以「簡化」之名移除方法論特徵拆解（若要簡化只能在 UI 層折疊呈現）

（STRATEGY_FEATURE_INDEX｜Part 4：附錄C v2026-01-01 完）

<!-- =========================================================
TAITS｜STRATEGY_FEATURE_INDEX｜Only-Add Canonical Alignment Addendum
GOVERNANCE_STATE = Freeze v1.0
變更原則：Only-Add（只可新增，不可刪減、不可覆寫、不可偷換既有語義）
適用文件：STRATEGY_FEATURE_INDEX（本檔）＋ STRATEGY_UNIVERSE（Part 8 新增策略模板）
對齊母法：MASTER_CANON（Canonical Flow L1–L11）
裁決序位：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON
========================================================= -->

# Block A｜文件開頭追加：MASTER_CANON 對位指引（Only-Add · Freeze v1.0）

（Only-Add · Canonical Alignment Guideline · Freeze v1.0）

## A.0 本段定位與效力聲明（不可省略）

1. 本段為 **STRATEGY_FEATURE_INDEX 對位 MASTER_CANON 的補充指引**，用於確保「特徵（Feature）層」在 Canonical Flow 中之合法邊界、責任歸屬與稽核可追溯性；**不構成新 Layer**，亦 **不改寫 MASTER_CANON 的 L1–L11**。
2. 本段 **不新增策略、不改寫策略條目、不授權任何下單語義**；STRATEGY_FEATURE_INDEX 僅規範 Feature 的語義、可用性、品質與稽核輸出。
3. 若本檔任一段落與 MASTER_CANON 存在歧義，**一律以 MASTER_CANON 為最終裁決**；本段僅提供「正確解讀與工程落地一致性」之對位方式。

## A.1 STRATEGY_FEATURE_INDEX 與 MASTER_CANON 的「差異」與「分工」界線（對位總結）

### A.1.1 MASTER_CANON 是「法源與流程」；STRATEGY_FEATURE_INDEX 是「特徵語義與輸出契約」

- MASTER_CANON：定義 L1–L11 的唯一 Canonical Flow（流程裁決母法）。
- STRATEGY_FEATURE_INDEX：定義 L4（Feature）層之**語義邊界、計算輸出、品質旗標、來源映射（Provenance）、版本/雜湊（Hash）、可回放（Replay Determinism）**等工程與治理必備義務；並提供 Feature → Evidence → Regime 的合法流之規格化展開。
- **不可跨界**：Feature 不得「方向化」（不可變成 Signal），不得「策略化」（不可變成 Strategy），更不得「下單化」（不可變成 Order）。此界線屬硬性治理邊界（Hard Boundary）。:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

### A.1.2 STRATEGY_FEATURE_INDEX 的上/下游責任邊界（Canonical 對位）

- 上游（L3 Snapshot Ready）：本檔不定義 Snapshot 規則本體，但要求 Feature 計算必須能被 Snapshot 回放支持（Reproducible / Deterministic）。
- 本層（L4 Feature Engine）：本檔定義 FeatureValueRecord、Provenance、QualityFlags、VersionRef、Hash 等最小稽核工件；缺任一項可在 Live/Paper 升級為風控否決（SYS-AUDIT / SYS-PROV）。:contentReference[oaicite:2]{index=2}
- 下游（L5 Evidence / L6 Regime / L7 Risk & Compliance）：本檔允許 Feature 作為 Evidence/Regime 的輸入，但 **不得讓 Feature 直接成為 PASS/VETO 或裁決依據**；裁決權仍屬 L7（RISK_COMPLIANCE）與 L10（Decision）。:contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

## A.2 與 STRATEGY_UNIVERSE（Part 8 新增策略模板）之同步對位：唯一正確引用方式

### A.2.1 STRATEGY_UNIVERSE 的 Required Evidence 必須以 Feature ID 引用（不得用自由文字替代）

- STRATEGY_UNIVERSE（Part 8）在新增策略條目（8.X）中要求列出 Required Evidence，且需包含資料源引用與特徵依賴引用；本檔定義「特徵依賴引用」的唯一合法格式為：**Feature ID（feature_id）清單＋版本/來源/品質條件**。:contentReference[oaicite:5]{index=5}
- 禁止：用「某某指標很好」「看起來偏多」等自由敘述代替 Feature ID；禁止把 Feature 的 UI 呈現（例如箭頭/顏色）當作 Evidence 本體。:contentReference[oaicite:6]{index=6}

### A.2.2 STRATEGY_UNIVERSE 的 Output Contract（Allowed/Forbidden/Void Handling）不得被 Feature/Index 內容越權

- STRATEGY_UNIVERSE（Part 8）定義永久禁止輸出（Forbidden Outputs），包含任何可直接下單欄位組合、任何「立即執行」語義、任何券商指令/API payload/委託參數包，並規定違規需標記 INVALID_STRATEGY_OUTPUT、Gate 必須 BLOCK、並寫入審計鏈。:contentReference[oaicite:7]{index=7}
- 本檔（Feature Index）之任何新增內容 **不得** 放寬或改寫上述策略輸出禁令；Feature 僅能提供描述性輸出與稽核對位欄位。

---

# Block B｜文件最末端追加：Appendix Y（Only-Add · Freeze v1.0）

# Appendix Y｜STRATEGY_FEATURE_INDEX × MASTER_CANON × STRATEGY_UNIVERSE（Part 8）同步對位附錄
（Only-Add · Canonical + Template Sync Addendum · Freeze v1.0）

doc_key：STRATEGY_FEATURE_INDEX
附錄性質：Addendum / Alignment Appendix（僅補充，不改寫、不覆蓋）
生效狀態：GOVERNANCE_STATE = Freeze v1.0
對齊母法：MASTER_CANON（Canonical Flow L1–L11）
同步對位：STRATEGY_UNIVERSE（Part 8｜新增策略條目治理模板）
裁決序位：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON
變更原則：Only-Add（只可新增，不可刪減、不可偷換既有語義）

---

## Y.0 附錄目的（不可省略）

本附錄提供兩件事：

1) **Canonical 對位**：把 Feature 層（L4）的輸出、品質、來源、版本、稽核工件，與 MASTER_CANON 的上下游責任邊界做「可驗證」對位。
2) **模板同步**：把 STRATEGY_UNIVERSE（Part 8）新增策略時必填的 Required Evidence / Output Contract / Governance & Audit 欄位，與本檔 Feature 規格做「硬一致」接口（interface）對位，避免新策略條目因引用不一致而失效。

---

## Y.1 Canonical Layer 對位表（L3–L7 最小閉環）

> 本表為「工程落地檢核」用途；不改寫 MASTER_CANON 定義。

| Canonical Layer | 角色定位 | STRATEGY_FEATURE_INDEX 在此層的硬義務 | 缺失後果（治理語義） |
|---|---|---|---|
| L3 Snapshot Ready | 可回放快照就緒 | Feature 計算須可回放；不得存在 lookahead；需能追溯 available_at（對延遲資料尤需） | Gate RETURN 或升級風控（視缺陷類型） |
| L4 Feature | 特徵計算與語義契約 | 必輸出：FeatureValueRecord / ProvenanceMapRef / QualityFlags / VersionRef / Hash | Live/Paper 可升級否決（SYS-AUDIT / SYS-PROV）:contentReference[oaicite:8]{index=8} |
| L5 Evidence | 證據組裝 | Feature 僅作為 Evidence Input；不得直接輸出買賣方向或「裁決」 | 語義違規（GOV-FTR-SEM-*） |
| L6 Regime | 狀態分類 | Feature 允許作 Regime Input，但不得越權宣告可交易/不可交易 | 越權視同治理違規 |
| L7 Risk & Compliance | 最高否決權 | Feature 不得成為 PASS/VETO；不得縮減風控揭露與稽核工件 | 觸發 VETO/BLOCK |

---

## Y.2 Feature 引用的「唯一合法格式」：FeatureRefBlock（供 STRATEGY_UNIVERSE Part 8 使用）

> 本段定義：當 STRATEGY_UNIVERSE（8.X）要求「Required Evidence（含特徵依賴引用）」時，必須使用以下格式。
> 禁止用自由文字替代 Feature ID；禁止用 UI 呈現（顏色/箭頭）替代 Feature 值與品質狀態。

### Y.2.1 FeatureRefBlock（必填）

```yaml
FeatureRefBlock:
 feature_id: "TECH.GMMA_SPREAD_RATIO" # 必須對應本檔 feature_id（唯一鍵）
 feature_version_min: "1.0.0" # 最低可接受版本（語義不破壞）
 allowed_uses_required:
 - "EVIDENCE_INPUT"
 forbidden_uses_assert:
 - "DIRECT_SIGNAL"
 - "DIRECT_STRATEGY"
 - "DIRECT_ORDER"
 quality_requirements:
 missing_policy: "FLAG|STOP" # 僅允許引用本檔定義的政策集合
 outlier_policy: "FLAG|STOP|WINSORIZE"
 halt_handling: "FREEZE_LAST|FLAG|STOP"
 provenance_requirements:
 require_provenance_map: true
 require_input_hash: true
 require_output_hash: true
 audit_requirements:
 must_emit_artifacts:
 - "FeatureValueRecord"
 - "ProvenanceMapRef"
 - "QualityFlags"
 - "VersionRef"
 - "Hash"
 ui_explain_binding:
 explain_level: "L1|L2|L3" # 對位 UI_SPEC 顯示階層（僅接口，不越權 UI 規範）
 display_prohibition:
 - "禁止買賣箭頭/顏色暗示（除非明確標示描述性且不作交易引導）"
上述欄位語義依循本檔既有 Feature 範例（含 allowed_uses / forbidden_uses、provenance、hash、versioning、ui_explain 等結構），不得刪減。
TAITS_策略特徵與因子索引（STRATEGY_FEATUR…


Y.3 STRATEGY_UNIVERSE（Part 8）欄位 ↔ Feature Index 對位表（同步硬規則）
目的：確保新策略（8.X）在「Required Evidence / Governance & Audit / Output Contract」三塊，與 Feature 層輸出契約一致，且不越權。

STRATEGY_UNIVERSE（8.X）欄位	必須如何引用/對位 STRATEGY_FEATURE_INDEX	硬性禁止
Required Evidence（含特徵依賴）	必須列出 FeatureRefBlock 清單（每個 evidence 要能追溯 feature_id + provenance + quality）	以自由文字/感覺敘述取代 feature_id
Governance & Audit（最小工件）	必須承諾：FeatureValueRecord / ProvenanceMapRef / QualityFlags / VersionRef / Hash（缺一不可）
TAITS_策略特徵與因子索引（STRATEGY_FEATUR…

刪除或弱化稽核工件；以「簡化」名義移除 provenance/hash/replay
Output Contract（Allowed/Forbidden/Violation）	必須沿用 STRATEGY_UNIVERSE Part 8 的 Forbidden Outputs 與 Violation Handling（不可改）
TAITS_策略宇宙全集（STRATEGY_UNIVERSE）…

任何下單參數、券商指令、API payload、立即執行語義

Y.4 新增/更新 Feature 的 Gate 統一要求（不得放寬）
本段為「本檔內部一致性」要求，並對位治理 Gate 流程：Semantic Boundary → Provenance/Hash → No Lookahead/Available_at → Replay Determinism → QA Handling → Allowed/Forbidden Uses。
TAITS_策略特徵與因子索引（STRATEGY_FEATUR…


Y.4.1 Gate 最小檢核清單（提交即用）
語義邊界：命名與輸出必為描述性；不得方向化（不可把描述性特徵偷換為信號）。
TAITS_策略特徵與因子索引（STRATEGY_FEATUR…


來源與雜湊：必有 provenance_map 與 input/output hash；不可缺省。

反前視（No Lookahead）：必聲明 lookahead_policy；延遲資料需 available_at。

可回放性：同一 snapshot 必須產生一致輸出（deterministic）。

品質處理：缺值/離群/停牌處理需明確且可稽核。

用途白名單/黑名單：allowed_uses / forbidden_uses 必須存在；禁止 DIRECT_SIGNAL / DIRECT_STRATEGY / DIRECT_ORDER。
TAITS_策略特徵與因子索引（STRATEGY_FEATUR…


Y.5 Only-Add 演進規則（本附錄專屬）
允許新增（Only-Add）：

新的 FeatureMeta 欄位（不得刪舊欄位）

新的方法論特徵族（例如新增新的結構體系子族）

新的 UI 提示欄位（不得弱化風險揭露）

新的品質旗標與來源映射（provenance mapping）

新的 Gate 檢核點與 reason_code（僅可更嚴，不可放寬）
TAITS_策略特徵與因子索引（STRATEGY_FEATUR…


禁止（硬禁）：

任何把描述性特徵偷換為方向/信號/策略/下單意圖的改動
TAITS_策略特徵與因子索引（STRATEGY_FEATUR…


刪除 Provenance / Hash / Replay 相關必備欄位
TAITS_策略特徵與因子索引（STRATEGY_FEATUR…


以「簡化」名義移除方法論特徵拆解（如需簡化只能在 UI 層折疊呈現，不得刪除規格本體）
TAITS_策略特徵與因子索引（STRATEGY_FEATUR…


（Appendix Y｜STRATEGY_FEATURE_INDEX × MASTER_CANON × STRATEGY_UNIVERSE 同步對位補充附錄 · Freeze v1.0 · Only-Add 完）
---

## Appendix 2025-12-28｜Only-Add：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）
> 適用文件：TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md（doc_key：STRATEGY_FEATURE_INDEX）
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 Addendum/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`STRATEGY_FEATURE_INDEX`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=STRATEGY_FEATURE_INDEX` + `canonical_filename=TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md`。
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---