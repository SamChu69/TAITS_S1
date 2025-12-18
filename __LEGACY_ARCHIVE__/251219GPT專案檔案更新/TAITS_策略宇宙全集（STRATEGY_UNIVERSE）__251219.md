# TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219
doc_key：STRATEGY_UNIVERSE  
治理等級：D（Strategy Universe｜白名單 × 生命週期 × 審計可回放 × Regime-First）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（策略宇宙可 Only-Add 擴充；不得刪減既有治理欄位與否決鏈）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX / VERSION_AUDIT / RISK_COMPLIANCE  
平行參照：ARCH_FLOW / FULL_ARCH / DATA_UNIVERSE / TWSE_RULES / EXECUTION_CONTROL / UI_SPEC / DEPLOY_OPS / LOCAL_ENV  
變更原則：Only-Add（只可新增，不可覆寫/刪除/弱化；策略版本只可追加；任何啟用需可追溯）  
核心鐵律：**策略 ≠ 下單**；**Agent ≠ 策略**；**AI ≠ 唯一真理**；**Regime 高於單一訊號**；**Risk/Compliance 可否決一切**；**策略必須白名單與可稽核**；**不得存在隱性策略鏈**

---

## 0. 文件定位（Strategy Universe Charter）

本文件為 TAITS 的「策略宇宙全集（Strategy Universe）」治理母表與規範文件，其目的在於：

- 建立 TAITS 可被允許使用的策略集合（Whitelist Universe），並以治理方式管理：
  - 策略分類、適用市場/商品、使用資料、依賴特徵、風險類型、Regime 前置條件
  - 版本、審計、回放（Replay）、證據鏈要求
  - 生命週期（Draft → Review → Approved → Active → Restricted → Deprecated → Retired）
- 明確規範策略與下單/執行的邊界：
  - 策略只能輸出「情境與建議」（hypothesis / proposal / constraints）
  - 下單只能在 EXECUTION_CONTROL（L11）且必須取得 L7 的 PASS token
- 防止任何形式的「隱性策略」：
  - Agent 私下串聯、跨層回寫、把特徵當方向、把 AI 建議直接變成下單指令

📌 本文件不做的事（避免越權）：
- 不承諾策略績效、不提供投資建議、不得行銷化
- 不取代 RISK_COMPLIANCE 的否決與原因碼
- 不定義資料來源（由 DATA_UNIVERSE 管理）
- 專注：策略宇宙的「治理、分類、元資料、審計、生命週期與輸出契約」

---

## 1. 策略治理的硬性總原則（Hard Governance Gates）

### 1.1 策略永遠不直連下單（Hard Gate）
- Strategy Layer（L8）輸出只能是：
  - `strategy_proposal`（策略提案）
  - `trade_intent_candidate`（候選意圖，仍需風控/合規與人類主權裁決）
  - `constraints`（限制條件：何時能做、何時不能做、風險上限）
- 禁止輸出：
  - 任何可被直接送往券商 API 的「可執行委託」
  - 任何繞過 L7/L10/L11 的捷徑流程

### 1.2 Regime-First（Regime 高於訊號）
- 任一策略都必須聲明：
  - 可被啟用的 Regime 集合（allowed_regimes）
  - Regime 信心門檻（min_regime_confidence）
- Regime 不滿足 → 策略必須自動「禁用/降級」為不可提案或僅供參考

### 1.3 Risk/Compliance 最高否決權（Hard Veto）
- L7 的 VETO 一律終止策略意圖進入 L11
- 不允許策略以績效/勝率/AI 推薦推翻否決

### 1.4 Only-Add 與可回放（Replayable）
- 策略版本、參數、依賴特徵、資料快照引用：
  - 必須被納入 active_version_map_ref
  - 必須能回放到同一輸出（或可解釋差異）
- 禁止覆寫舊版本；只能新增新版本並切換 ACTIVE 指向（由治理決策）

### 1.5 禁止隱性策略（No Hidden Strategy）
- 任何策略行為都必須能在審計中被還原：
  - 使用了哪些特徵、哪些資料、哪些 Regime、哪些門檻、哪些否決原因碼
- Agent 之間不得形成「私下串聯策略鏈」（例如：A 產生方向、B 補上條件、C 直接送單）

---

## 2. 策略宇宙資料結構（Strategy Registry Schema｜可落地）

> TAITS 策略宇宙不是「文字清單」，而是可治理的 registry。  
> 每個策略是一筆可版本化記錄（Strategy Record），Only-Add。

### 2.1 Strategy Record（最小欄位，不可縮減）
- `strategy_id`（全域唯一；不可重用）
- `strategy_name_zh`（繁中正式名）
- `strategy_name_en`（可選，但建議保留；英文需中譯）
- `family`（策略家族：Trend/MR/Arb/Event/Vol/Carry/Relative/Stat/Structure…）
- `paradigm`（方法論：Rules/Stats/ML/Hybrid/ChanLun-Structure/…）
- `market_scope`：TWSE / TPEX / TAIFEX（可多選）
- `instrument_types[]`：EQUITY/ETF/FUTURES/OPTIONS/…
- `timeframes[]`：1m/5m/15m/1h/1d/…
- `regime_requirements`：
  - `allowed_regimes[]`
  - `min_regime_confidence`
  - `regime_features_required[]`
- `data_requirements[]`（引用 DATA_UNIVERSE 的 subcategory_id）
- `feature_requirements[]`（引用 STRATEGY_FEATURE_INDEX 的 feature_id）
- `evidence_requirements`（Evidence set 版本/門檻；對齊 DATA_UNIVERSE Part 3）
- `risk_profile`：
  - `risk_factors[]`（liquidity/gap/vol/limit-up/down/event…）
  - `max_exposure_rules_ref`（引用 RISK_COMPLIANCE 的門檻模板）
- `constraints`：
  - `hard_blocks[]`（必然禁止條件）
  - `soft_constraints[]`（降級條件）
- `outputs_contract`（策略輸出契約：可輸出哪些欄位，禁止輸出哪些欄位）
- `explainability`：
  - `required_explanations[]`（UI 必須呈現的解釋項）
- `lifecycle_state`：DRAFT/REVIEW/APPROVED/ACTIVE/RESTRICTED/DEPRECATED/RETIRED
- `owner`（責任模組/負責人或責任群組）
- `versioning`：
  - `strategy_version`
  - `parameters_schema_ref`
  - `implementation_ref`（程式/規則版本引用）
- `auditability`：
  - `required_logs[]`
  - `required_artifacts[]`
- `notes`（只能補充，不可弱化硬規則）

### 2.2 Strategy Instance（策略實例：一次運行的具體參數）
- `strategy_run_id`
- `strategy_id` + `strategy_version`
- `parameter_set_ref`
- `active_version_map_ref`
- `input_snapshot_refs[]`
- `feature_snapshot_refs[]`
- `regime_snapshot_ref`
- `evidence_bundle_ref`
- `output_proposal_ref`
- `hash_manifest_ref`

---

## 3. 策略生命週期（Lifecycle Governance｜硬規則）

### 3.1 狀態定義
- **DRAFT**：草稿，允許研究，但不得進入 Paper/Live
- **REVIEW**：審查中，必須具備完整證據鏈與回放能力
- **APPROVED**：治理層通過，可進 Simulation/Paper（仍需風控/合規）
- **ACTIVE**：允許在符合條件下輸出提案（仍需人類主權與 L7 PASS）
- **RESTRICTED**：受限（例如市場制度變動、資料品質問題、風險事件），僅研究用途
- **DEPRECATED**：準退役，保留回放；不可新啟用
- **RETIRED**：退役，只可讀不可用

### 3.2 狀態轉移硬門檻（不可縮減）
- DRAFT → REVIEW：
  - 必須有：data_requirements + feature_requirements + outputs_contract
- REVIEW → APPROVED：
  - 必須有：回測可回放、Evidence 完整度門檻（EC≥3）、風險情境測試（Worst-case First）
- APPROVED → ACTIVE：
  - 必須有：RISK_COMPLIANCE 對應的 exposure 模板、UI 解釋項完整
- ACTIVE → RESTRICTED/DEPRECATED：
  - 由風控/合規/治理觸發（制度變動、異常風險、資料不可用）

---

## 4. 策略分類體系（Taxonomy｜最大完備骨架）

> 目的：讓 285+ 策略可以被一致分類、治理、查詢、審計與擴充。

### 4.1 家族（Family）
- Trend Following（趨勢）
- Mean Reversion（均值回歸）
- Breakout / Momentum（突破/動能）
- Volatility / Options（波動/選擇權）
- Statistical Arbitrage（統計套利）
- Relative Value / Spread（相對價值/價差）
- Event-Driven（事件驅動）
- Microstructure（微結構/流動性）
- Structure-Driven（結構驅動：含 ChanLun 結構）
- Multi-Asset / Cross-Market（跨資產/跨市場：例如期貨影響現貨）

### 4.2 方法論（Paradigm）
- Rule-based（規則）
- Statistical（統計）
- ML / AI-assisted（機器學習/AI 輔助；不得越權）
- Hybrid（混合）
- ChanLun-Structure（纏論結構作為「結構與判斷體系」，非單一策略）

### 4.3 持有期（Holding Horizon）
- Intraday（日內）
- Swing（波段）
- Position（中長期）
- Hedging（對沖）

---

## 5. 策略輸出契約（Outputs Contract｜嚴格邊界）

> 最大完備重點：把「策略能說什麼」鎖死，避免策略變成下單。

### 5.1 允許輸出（Allowed Outputs）
- `proposal_type`：enter/exit/hold/avoid（建議類型）
- `direction_hint`：long/short/neutral（僅提示；不得直接生成委託）
- `setup_conditions[]`：成立條件（可被驗證）
- `invalidation_conditions[]`：失效條件（可被驗證）
- `time_validity`：有效窗口（例如下一根K/當日/到某事件）
- `risk_notes`：風險說明（必須可解釋）
- `required_regime`：所需 regime 與信心門檻
- `required_evidence`：所需 evidence set 與 EC 下限
- `recommended_constraints`：例如最大曝險、分批、停損/停利模板（模板引用，不是硬下單）
- `explanation_bundle_ref`：可視化解釋引用（UI 需要）

### 5.2 禁止輸出（Forbidden Outputs｜硬禁）
- `broker_order_payload`
- 可直接送單的價格/數量/帳戶路由細節（除非只是「區間建議」且不具可執行性）
- 任何繞過 L7 PASS token 的「自動送單指令」
- 任何把特徵直接等同方向的單句結論（例如：某因子>0 所以必買）

---

## 6. 策略與 Regime 的耦合規範（Regime Binding）

### 6.1 Regime 前置條件（必填）
每個策略必須聲明：
- `allowed_regimes[]`（例如：Trend/Range/HighVol/LowLiquidity/NewsShock…）
- `min_regime_confidence`
- `regime_conflict_behavior`：
  - `BLOCK`：不允許提案
  - `DOWNGRADE`：只給觀察，不給方向
  - `ALTERNATE`：切換到對應 regime 的子策略（仍需白名單）

### 6.2 Regime 與證據鏈（Evidence）
- Regime 判定必須使用 DATA_UNIVERSE 定義的 evidence sets
- 若 evidence completeness < 要求：
  - 策略不得提升信心
  - 不得從「不確定」硬判成「確定」

---

## 7. 策略與風險模板（Risk Templates｜引用而非重寫）

> 策略不得自創「放寬風控」的條款；只能引用 RISK_COMPLIANCE 的模板與 reason codes。

每個策略必須綁定：
- `risk_template_ref`（例如：Position Sizing、最大曝險、流動性門檻、跳空風險）
- `compliance_dependency`（是否涉及信用/放空/衍生品）
- `kill_switch_sensitivity`（遇到哪類市場狀態必須立即停止提案）

---

## 8. 策略審計輸出（Audit Outputs｜必須落地）

每次策略運行（strategy_run）必須產生（不可縮減）：
- `strategy_run_id`
- `strategy_id` + `strategy_version`
- `parameter_set_ref`
- `active_version_map_ref`
- `evidence_bundle_ref`（含 EC 等級）
- `regime_snapshot_ref`（含信心）
- `output_proposal_ref`（輸出提案）
- `risk_precheck_ref`（策略層風險預檢：不等於 L7 最終裁決）
- `explanation_bundle_ref`
- `hash_manifest_ref`

UI（L10）至少顯示：
- 策略名稱/版本、所需 regime、所用證據完整度（EC）、關鍵限制條件與失效條件
- 若被否決：顯示 reason codes（來自 L7，不是策略自說自話）

---

## 9. Mermaid｜策略提案到否決鏈（不得跳步）

flowchart TB
  L4[L4 Features] --> L5[L5 Evidence Bundle + EC]
  L5 --> L6[L6 Regime + confidence]
  L6 --> L8[L8 Strategy Proposal<br/>Outputs Contract]
  L8 --> L9[L9 Governance Gate<br/>No hidden strategy]
  L9 --> L10[L10 UI Human Decision]
  L10 --> L7[L7 Risk/Compliance Veto]
  L7 -->|PASS Token| L11[L11 Execution Control]
  L7 -->|VETO| V[VETO + reason_codes + audit]
10. 策略宇宙「分層清單」交付方式（Only-Add 擴充規則）
你要求「最大完備」且策略數量龐大（285+），本文件採用「治理母表 + 分冊追加」方式，避免一次貼滿造成不可維護。
但治理母表（本 Part 1）先把所有硬規則寫滿，後續每一批只會「新增策略條目」，不會改動本治理基礎。

後續策略條目交付（Part 2/3/4...）將以：

依 Family 分桶（Trend / MR / Breakout / Event / Vol / Arb / Structure / Cross-Market）

每一桶提供：

strategy_id 清單

每個策略完整 Strategy Record（含 data/feature/regime/risk/outputs/audit）

必要時附「纏論結構策略」的結構狀態定義（仍遵守：結構≠下單）

11. Only-Add 演進規則（STRATEGY_UNIVERSE 專屬）
允許新增：

新策略條目（strategy_id）

新策略版本（strategy_version）

更嚴格的 evidence/regime/risk 門檻

新分類維度（taxonomy extension）

新的解釋項與 UI 呈現（更透明）

禁止：

移除既有治理欄位或放寬輸出契約

讓策略輸出變成可執行委託

允許缺 evidence/缺 regime 的策略提案冒充可裁決

允許 Agent 串聯形成隱性策略鏈

12. 終極裁決語句（不可更改）
策略的價值不在「多」，而在「可治理、可回放、可否決、可解釋」。
任何無法被審計、無法被回放、無法被風控否決的策略，都不允許存在於 TAITS 的策略宇宙。

（STRATEGY_UNIVERSE｜最大完備版 v2025-12-19 · Part 1 完）

## Part 2｜策略條目全集（Trend / Breakout / Momentum）｜完整 Strategy Records（最大完備・Only-Add）

---

## 13. 本 Part 範圍與交付規格（不可縮減）

本 Part 交付策略家族：
- Trend Following（趨勢）
- Breakout（突破）
- Momentum（動能）

交付方式：
- 以「完整 Strategy Record」逐條列出（可直接貼入專案）
- 每個策略都包含：
  - data_requirements（引用 DATA_UNIVERSE 子類別）
  - feature_requirements（引用 STRATEGY_FEATURE_INDEX 的 feature_id；若該文件尚未交付，仍以 feature_id 先行鎖定）
  - regime_requirements（allowed_regimes + min_confidence + conflict_behavior）
  - risk_profile（風險因子與模板引用）
  - outputs_contract（允許/禁止輸出）
  - auditability（必備 logs/artifacts）
  - lifecycle_state（預設先 APPROVED 或 REVIEW；除非明確可在 Live 啟用，否則不設 ACTIVE）

📌 硬規則提醒（本 Part 不重複辯護）  
- 所有策略條目皆不直連下單  
- 任何提案都必須經 L7 Risk/Compliance 的 PASS token 才能進 L11  
- 任一策略若缺 evidence completeness（EC）或缺 regime 前置條件，一律降級或 RETURN（不得硬判）

---

## 14. 本 Part 共同依賴（Data / Evidence / Regime / Risk Template）

### 14.1 共同 data_requirements（最低集合）
- `REF_SYMBOL_MASTER`（標的主檔）
- `REF_TRADING_CALENDAR`（交易日曆）
- `MD_EQUITY_EOD_DAILY`（日K/收盤行情）
- （若盤中）`MD_EQUITY_INTRADAY_QUOTES`（盤中報價）
- （若過濾停牌/處置）`RS_HALT_LIST`, `RS_RESTRICTED_LIST`
- （若需復權/事件）`CA_MASTER`（公司行為）

### 14.2 Evidence completeness（最低門檻）
- Trend/Breakout/Momentum（Research/Backtest）：EC ≥ 3（可裁決但需標示缺口）
- Paper/Live（若啟用）：EC ≥ 4（完整），且資料 QG-A/B 以官方/授權為主  
- 任何使用 FALLBACK（QG-C）作為主要行情來源：`compliance_eligible=false` 且不得進合規裁決

### 14.3 Regime（範例命名，實際以 Regime Engine 為準）
- `RG_TREND_UP`：上行趨勢
- `RG_TREND_DOWN`：下行趨勢
- `RG_RANGE`：區間震盪
- `RG_HIGH_VOL`：高波動
- `RG_LOW_LIQ`：低流動性
- `RG_NEWS_SHOCK`：事件衝擊
- `RG_RISK_OFF`：風險趨避

### 14.4 風險模板引用（僅引用，不自創放寬條款）
- `RISK_TMPL_TREND_CORE`
- `RISK_TMPL_BREAKOUT_CORE`
- `RISK_TMPL_MOMENTUM_CORE`
- `RISK_TMPL_LIQUIDITY_GUARD`
- `RISK_TMPL_GAP_SHOCK_GUARD`
- `RISK_TMPL_LIMIT_UPDOWN_GUARD`

> 以上模板的細節裁決以 RISK_COMPLIANCE 為準；此處只做引用鎖定。

---

## 15. 策略條目清單（Whitelist Index｜Part 2）

> 你要最大完備：本 Part 先交付 36 條（Trend 14、Breakout 12、Momentum 10）。  
> 後續 Part 只會新增更多策略條目，不會改動本 Part 既有條目（Only-Add）。

- Trend：
  - TAITS_STG_TREND_001 ~ TAITS_STG_TREND_014
- Breakout：
  - TAITS_STG_BRK_001 ~ TAITS_STG_BRK_012
- Momentum：
  - TAITS_STG_MOM_001 ~ TAITS_STG_MOM_010

---

# 16. Strategy Records（完整條目｜可審計｜可回放）

> 格式：每條策略以「不可縮減欄位」完整列出。  
> 若你要我接著出 Part 3（Mean Reversion / Range），我會沿用同一格式 Only-Add。

---

## 16.1 Trend Following（趨勢）策略群

### TAITS_STG_TREND_001｜EMA 雙均線趨勢（EMA Fast/Slow Trend）
- strategy_id：TAITS_STG_TREND_001
- strategy_name_zh：EMA 雙均線趨勢（快慢線趨勢）
- family：Trend Following（趨勢）
- paradigm：Rule-based（規則）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d, 60m
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_TREND_DOWN
  - min_regime_confidence：0.70
  - regime_conflict_behavior：BLOCK
  - regime_features_required：FEAT_REGIME_TREND_STRENGTH, FEAT_REGIME_VOL_STATE
- data_requirements：
  - REF_SYMBOL_MASTER
  - REF_TRADING_CALENDAR
  - MD_EQUITY_EOD_DAILY
  - CA_MASTER（若啟用復權）
- feature_requirements：
  - FEAT_EMA_FAST
  - FEAT_EMA_SLOW
  - FEAT_EMA_CROSS_SIGNAL
  - FEAT_ATR_N
  - FEAT_VOLUME_TREND
- evidence_requirements：
  - context：CTX_STRATEGY_PROPOSAL
  - required_set_version：DATA_UNIVERSE.RequiredSet.CTX_STRATEGY_PROPOSAL.v1
  - min_EC：3（Research/Backtest）
- risk_profile：
  - risk_factors：gap, liquidity, limit_updown, trend_exhaustion
  - max_exposure_rules_ref：RISK_TMPL_TREND_CORE
  - additional_guards：RISK_TMPL_LIQUIDITY_GUARD, RISK_TMPL_GAP_SHOCK_GUARD
- constraints：
  - hard_blocks：
    - 若 RS_HALT_LIST 命中 → 禁止提案
    - 若 RS_RESTRICTED_LIST 命中且屬處置 → 降級或禁止（以政策裁決）
    - 若 QG 主要行情來源為 FALLBACK → 禁止進入任何合規/執行鏈
  - soft_constraints：
    - 高波動 RG_HIGH_VOL 時：降低信心或縮短有效窗口
- outputs_contract：
  - allowed_outputs：proposal_type, direction_hint, setup_conditions, invalidation_conditions, time_validity, required_regime, required_evidence, recommended_constraints, explanation_bundle_ref
  - forbidden_outputs：broker_order_payload, executable_price_qty, account_route_details
- explainability：
  - required_explanations：
    - 「均線狀態」：快線/慢線位置、交叉時間
    - 「趨勢強度」：趨勢強度特徵與 regime 信心
    - 「風險揭露」：跳空/流動性/漲跌停風險
- lifecycle_state：APPROVED
- owner：Strategy Library / Trend Group
- versioning：
  - strategy_version：1.0.0
  - parameters_schema_ref：STRAT_PARAMS_EMA_TREND_v1
  - implementation_ref：IMPL_RULESET_EMA_TREND_v1
- auditability：
  - required_logs：strategy_run_log, feature_snapshot_log, regime_snapshot_log, evidence_bundle_log, proposal_output_log
  - required_artifacts：parameter_set_ref, input_snapshot_refs, hash_manifest_ref, explanation_bundle_ref
- notes：不得以單一交叉訊號直接升格為「必買/必賣」；必須受 Regime 與風控否決。

---

### TAITS_STG_TREND_002｜SMA 三均線排列（Triple MA Alignment Trend）
- strategy_id：TAITS_STG_TREND_002
- strategy_name_zh：SMA 三均線排列趨勢（三線多空排列）
- family：Trend Following
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_TREND_DOWN
  - min_regime_confidence：0.75
  - regime_conflict_behavior：BLOCK
  - regime_features_required：FEAT_REGIME_TREND_STRENGTH
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY, CA_MASTER
- feature_requirements：FEAT_SMA_20, FEAT_SMA_60, FEAT_SMA_120, FEAT_MA_ALIGNMENT_STATE, FEAT_ATR_N
- evidence_requirements：context=CTX_STRATEGY_PROPOSAL, required_set_version=DATA_UNIVERSE.RequiredSet.CTX_STRATEGY_PROPOSAL.v1, min_EC=3
- risk_profile：
  - risk_factors：trend_exhaustion, gap, limit_updown, liquidity
  - max_exposure_rules_ref：RISK_TMPL_TREND_CORE
- constraints：
  - hard_blocks：停牌/處置/不可交易狀態一律禁止
  - soft_constraints：成交額/成交量低於門檻 → 降級（不給方向，只給觀察）
- outputs_contract：同 TAITS_STG_TREND_001
- explainability：三均線相對位置、排列維持天數、回撤幅度
- lifecycle_state：APPROVED
- owner：Strategy Library / Trend Group
- versioning：strategy_version=1.0.0, parameters_schema_ref=STRAT_PARAMS_TRIPLE_MA_v1, implementation_ref=IMPL_RULESET_TRIPLE_MA_v1
- auditability：同上（不可縮減）

---

### TAITS_STG_TREND_003｜ADX 趨勢強度濾網（ADX Trend Filter + Entry）
- strategy_id：TAITS_STG_TREND_003
- strategy_name_zh：ADX 趨勢強度濾網（含方向條件）
- family：Trend Following
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d, 60m
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_TREND_DOWN
  - min_regime_confidence：0.70
  - regime_conflict_behavior：BLOCK
  - regime_features_required：FEAT_REGIME_TREND_STRENGTH, FEAT_REGIME_CHOP_STATE
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_ADX_N, FEAT_DI_PLUS, FEAT_DI_MINUS, FEAT_ATR_N, FEAT_PRICE_BREAK_STRUCTURE
- evidence_requirements：min_EC=3
- risk_profile：
  - risk_factors：false_break, gap, liquidity
  - max_exposure_rules_ref：RISK_TMPL_TREND_CORE
- constraints：
  - hard_blocks：ADX 計算資料不足（缺 bars）→ RETURN
  - soft_constraints：RG_HIGH_VOL → 提案有效窗口縮短
- outputs_contract：同上
- explainability：ADX 值、DI 差、趨勢/盤整判斷依據
- lifecycle_state：REVIEW
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_ADX_TREND_v1 / IMPL_RULESET_ADX_TREND_v1
- auditability：同上

---

### TAITS_STG_TREND_004｜Donchian 趨勢通道（Donchian Channel Trend）
- strategy_id：TAITS_STG_TREND_004
- strategy_name_zh：Donchian 趨勢通道（突破延續）
- family：Trend Following
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_TREND_DOWN
  - min_regime_confidence：0.70
  - regime_conflict_behavior：BLOCK
  - regime_features_required：FEAT_REGIME_TREND_STRENGTH
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_DONCHIAN_HIGH_N, FEAT_DONCHIAN_LOW_N, FEAT_ATR_N, FEAT_VOLATILITY_STATE
- evidence_requirements：min_EC=3
- risk_profile：
  - risk_factors：breakout_failure, gap, limit_updown
  - max_exposure_rules_ref：RISK_TMPL_TREND_CORE
  - additional_guards：RISK_TMPL_LIMIT_UPDOWN_GUARD
- constraints：停牌/處置硬禁；RG_RANGE 時 BLOCK
- outputs_contract：同上
- explainability：通道上/下緣、突破距離、波動狀態
- lifecycle_state：APPROVED
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_DONCHIAN_TREND_v1 / IMPL_RULESET_DONCHIAN_TREND_v1
- auditability：同上

---

### TAITS_STG_TREND_005｜SuperTrend 趨勢（ATR-based SuperTrend）
- strategy_id：TAITS_STG_TREND_005
- strategy_name_zh：SuperTrend 趨勢（ATR 追蹤）
- family：Trend Following
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d, 60m
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_TREND_DOWN; min_regime_confidence=0.70; conflict=BLOCK; required=FEAT_REGIME_TREND_STRENGTH
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_SUPERTREND, FEAT_ATR_N, FEAT_VOLATILITY_STATE
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=gap, whipsaw, limit_updown; max_exposure_rules_ref=RISK_TMPL_TREND_CORE
- constraints：RG_RANGE → DOWNGRADE（只給觀察）；低流動性 → 降級或禁止
- outputs_contract：同上
- explainability：SuperTrend 線、翻轉點、ATR 倍數
- lifecycle_state：REVIEW
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_SUPERTREND_v1 / IMPL_RULESET_SUPERTREND_v1
- auditability：同上

---

### TAITS_STG_TREND_006｜趨勢回踩進場（Pullback-in-Trend）
- strategy_id：TAITS_STG_TREND_006
- strategy_name_zh：趨勢回踩（回撤到均線/支撐）
- family：Trend Following
- paradigm：Rule-based + Structure（含結構）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.75; conflict=BLOCK; required=FEAT_REGIME_TREND_STRENGTH
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY, CA_MASTER
- feature_requirements：FEAT_SMA_20, FEAT_SMA_60, FEAT_PULLBACK_DEPTH, FEAT_PULLBACK_RECOVERY, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=pullback_failure, gap, liquidity; max_exposure_rules_ref=RISK_TMPL_TREND_CORE
- constraints：若回撤深度超過政策門檻 → BLOCK（避免「跌勢中接刀」）
- outputs_contract：同上
- explainability：回撤深度/時間、回穩證據（量價/收斂）
- lifecycle_state：APPROVED
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_PULLBACK_TREND_v1 / IMPL_RULESET_PULLBACK_TREND_v1
- auditability：同上

---

### TAITS_STG_TREND_007｜多週期趨勢一致（MTF Trend Confirmation）
- strategy_id：TAITS_STG_TREND_007
- strategy_name_zh：多週期趨勢一致（週線/日線同向）
- family：Trend Following
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d, 1w
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_TREND_DOWN; min_regime_confidence=0.80; conflict=BLOCK; required=FEAT_REGIME_TREND_STRENGTH
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_MTF_TREND_ALIGN, FEAT_EMA_FAST, FEAT_EMA_SLOW, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=lag, gap; max_exposure_rules_ref=RISK_TMPL_TREND_CORE
- constraints：週期資料不足 → RETURN
- outputs_contract：同上
- explainability：多週期趨勢方向與一致性分數
- lifecycle_state：REVIEW
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_MTF_TREND_v1 / IMPL_RULESET_MTF_TREND_v1
- auditability：同上

---

### TAITS_STG_TREND_008｜趨勢延續（Higher High / Higher Low）
- strategy_id：TAITS_STG_TREND_008
- strategy_name_zh：高高低低趨勢延續（結構趨勢）
- family：Trend Following
- paradigm：Structure-Driven（結構驅動）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.75; conflict=BLOCK; required=FEAT_REGIME_TREND_STRENGTH
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_SWING_HHHL_STATE, FEAT_STRUCTURE_BREAK_VALIDATION, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=structure_false, gap, liquidity; max_exposure_rules_ref=RISK_TMPL_TREND_CORE
- constraints：RG_NEWS_SHOCK → DOWNGRADE（只給觀察）
- outputs_contract：同上
- explainability：波段高低點、結構成立條件
- lifecycle_state：REVIEW
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_STRUCTURE_TREND_v1 / IMPL_RULESET_STRUCTURE_TREND_v1
- auditability：同上

---

### TAITS_STG_TREND_009｜GMMA 趨勢群（短長期均線群擴散）
- strategy_id：TAITS_STG_TREND_009
- strategy_name_zh：GMMA 趨勢群（短/長均線群擴散）
- family：Trend Following
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_TREND_DOWN; min_regime_confidence=0.75; conflict=BLOCK; required=FEAT_REGIME_TREND_STRENGTH
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_GMMA_SHORT_BAND, FEAT_GMMA_LONG_BAND, FEAT_GMMA_SPREAD, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=whipsaw, gap; max_exposure_rules_ref=RISK_TMPL_TREND_CORE
- constraints：成交額不足 → DOWNGRADE
- outputs_contract：同上
- explainability：短長群距離、群擴散/收斂
- lifecycle_state：APPROVED
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_GMMA_TREND_v1 / IMPL_RULESET_GMMA_TREND_v1
- auditability：同上

---

### TAITS_STG_TREND_010｜趨勢加速（Slope/Acceleration）
- strategy_id：TAITS_STG_TREND_010
- strategy_name_zh：趨勢加速（均線斜率/加速度）
- family：Trend Following
- paradigm：Stat + Rule Hybrid
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.80; conflict=BLOCK; required=FEAT_REGIME_TREND_STRENGTH
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_MA_SLOPE, FEAT_MA_ACCEL, FEAT_ATR_N, FEAT_VOLATILITY_STATE
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=overheat, gap; max_exposure_rules_ref=RISK_TMPL_TREND_CORE
- constraints：RG_HIGH_VOL → DOWNGRADE
- outputs_contract：同上
- explainability：斜率/加速度、過熱警示
- lifecycle_state：REVIEW
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_TREND_ACCEL_v1 / IMPL_RULESET_TREND_ACCEL_v1
- auditability：同上

---

### TAITS_STG_TREND_011｜均線守住不破（MA Hold Trend）
- strategy_id：TAITS_STG_TREND_011
- strategy_name_zh：均線守住不破（支撐延續）
- family：Trend Following
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_MA_HOLD_SCORE, FEAT_PULLBACK_DEPTH, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=break_support, gap, liquidity; max_exposure_rules_ref=RISK_TMPL_TREND_CORE
- constraints：支撐多次測試失敗 → BLOCK
- outputs_contract：同上
- explainability：守住次數、守住幅度、回撤與修復
- lifecycle_state：APPROVED
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_MA_HOLD_v1 / IMPL_RULESET_MA_HOLD_v1
- auditability：同上

---

### TAITS_STG_TREND_012｜趨勢追蹤停利（Trailing Stop Template）
- strategy_id：TAITS_STG_TREND_012
- strategy_name_zh：趨勢追蹤停利（ATR/通道追蹤）
- family：Trend Following
- paradigm：Rule-based（Risk-Overlay 型）
- market_scope：TWSE, TPEX, TAIFEX（僅作模板）
- instrument_types：EQUITY, ETF, FUTURES
- timeframes：1d, 60m
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_TREND_DOWN; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY（或衍生品對應行情）, REF_TRADING_CALENDAR
- feature_requirements：FEAT_ATR_N, FEAT_TRAIL_STOP_LEVEL, FEAT_VOLATILITY_STATE
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=gap, slippage; max_exposure_rules_ref=RISK_TMPL_TREND_CORE
- constraints：此策略條目為「停利模板」，不得單獨生成方向提案
- outputs_contract：
  - allowed_outputs：recommended_constraints（停利/移動停利模板引用）, invalidation_conditions
  - forbidden_outputs：任何方向/進場訊號、任何可執行委託
- explainability：追蹤停利線與風險揭露
- lifecycle_state：APPROVED
- owner：Risk Overlay / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_TRAILSTOP_v1 / IMPL_RULESET_TRAILSTOP_v1
- auditability：required_logs=overlay_run_log, evidence_bundle_log; required_artifacts=parameter_set_ref, hash_manifest_ref

---

### TAITS_STG_TREND_013｜趨勢中的量能確認（Volume Confirmation Trend）
- strategy_id：TAITS_STG_TREND_013
- strategy_name_zh：趨勢量能確認（量能配合）
- family：Trend Following
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR, REF_SYMBOL_MASTER
- feature_requirements：FEAT_VOLUME_SURGE, FEAT_VOLUME_TREND, FEAT_PRICE_TREND_STATE, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=distribution, gap; max_exposure_rules_ref=RISK_TMPL_TREND_CORE
- constraints：若量增但價格不配合 → DOWNGRADE（只給觀察）
- outputs_contract：同上
- explainability：量能相對分位、量價背離提示
- lifecycle_state：REVIEW
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_VOLCONF_TREND_v1 / IMPL_RULESET_VOLCONF_TREND_v1
- auditability：同上

---

### TAITS_STG_TREND_014｜趨勢缺口延續（Gap-Continuation in Trend）
- strategy_id：TAITS_STG_TREND_014
- strategy_name_zh：趨勢缺口延續（跳空後延續）
- family：Trend Following
- paradigm：Rule-based + Risk-First
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d, 60m
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.80; conflict=BLOCK; required=FEAT_REGIME_VOL_STATE
- data_requirements：MD_EQUITY_EOD_DAILY, MD_EQUITY_INTRADAY_QUOTES, REF_TRADING_CALENDAR, REF_SYMBOL_MASTER
- feature_requirements：FEAT_GAP_SIZE, FEAT_GAP_FILL_RISK, FEAT_ATR_N, FEAT_LIMIT_UPDOWN_PROXIMITY
- evidence_requirements：min_EC=4（此條目涉及高風險情境，預設要求更高）
- risk_profile：risk_factors=gap, limit_updown, liquidity; max_exposure_rules_ref=RISK_TMPL_GAP_SHOCK_GUARD
- constraints：若接近漲跌停或流動性不足 → BLOCK
- outputs_contract：同上（不得輸出可執行委託）
- explainability：缺口大小（相對 ATR）、回補風險、漲跌停距離
- lifecycle_state：REVIEW
- owner：Strategy Library / Trend Group
- versioning：1.0.0 / STRAT_PARAMS_GAP_CONT_TREND_v1 / IMPL_RULESET_GAP_CONT_TREND_v1
- auditability：同上

---

## 16.2 Breakout（突破）策略群

### TAITS_STG_BRK_001｜N 日新高突破（Donchian / HH Breakout）
- strategy_id：TAITS_STG_BRK_001
- strategy_name_zh：N 日新高突破（價格突破）
- family：Breakout（突破）
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_HIGH_VOL
  - min_regime_confidence：0.70
  - regime_conflict_behavior：DOWNGRADE（RG_RANGE 時只給觀察）
  - regime_features_required：FEAT_REGIME_VOL_STATE
- data_requirements：REF_SYMBOL_MASTER, REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY, RS_HALT_LIST, RS_RESTRICTED_LIST
- feature_requirements：FEAT_NDAY_HIGH, FEAT_BREAKOUT_DISTANCE, FEAT_VOLUME_SURGE, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：
  - risk_factors：false_break, limit_updown, liquidity, gap
  - max_exposure_rules_ref：RISK_TMPL_BREAKOUT_CORE
  - additional_guards：RISK_TMPL_LIMIT_UPDOWN_GUARD, RISK_TMPL_LIQUIDITY_GUARD
- constraints：
  - hard_blocks：處置/停牌命中 → 禁止
  - soft_constraints：若量能未確認 → DOWNGRADE
- outputs_contract：同 Trend（禁止可執行委託）
- explainability：突破基準（N 日高）、突破幅度、量能確認、失效條件（跌回突破位）
- lifecycle_state：APPROVED
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_NHIGH_BREAK_v1 / IMPL_RULESET_NHIGH_BREAK_v1
- auditability：同 Trend

---

### TAITS_STG_BRK_002｜箱體突破（Range Box Breakout）
- strategy_id：TAITS_STG_BRK_002
- strategy_name_zh：箱體突破（區間上緣突破）
- family：Breakout
- paradigm：Rule-based + Structure
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_TREND_UP; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY, REF_SYMBOL_MASTER
- feature_requirements：FEAT_RANGE_TOP, FEAT_RANGE_WIDTH, FEAT_BREAKOUT_CONFIRM, FEAT_VOLUME_SURGE, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=false_break, whipsaw, liquidity; max_exposure_rules_ref=RISK_TMPL_BREAKOUT_CORE
- constraints：箱體寬度過小（噪音）→ DOWNGRADE；低流動性 → BLOCK
- outputs_contract：同上
- explainability：箱體定義、突破確認（收盤/量能）、失效條件
- lifecycle_state：REVIEW
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_BOX_BREAK_v1 / IMPL_RULESET_BOX_BREAK_v1
- auditability：同上

---

### TAITS_STG_BRK_003｜開盤突破延續（Opening Range Breakout）
- strategy_id：TAITS_STG_BRK_003
- strategy_name_zh：開盤區間突破（ORB）
- family：Breakout
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：5m, 15m, 60m
- regime_requirements：allowed_regimes=RG_HIGH_VOL,RG_TREND_UP; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_INTRADAY_QUOTES, REF_TRADING_CALENDAR, REF_SYMBOL_MASTER, RS_HALT_LIST
- feature_requirements：FEAT_ORB_RANGE, FEAT_ORB_BREAK, FEAT_VOLUME_SURGE_INTRADAY, FEAT_SPREAD_LIQUIDITY
- evidence_requirements：min_EC=4（盤中策略預設更高）
- risk_profile：risk_factors=slippage, liquidity, gap, limit_updown; max_exposure_rules_ref=RISK_TMPL_BREAKOUT_CORE
- constraints：若盤中流動性指標不足 → BLOCK；若接近漲跌停 → BLOCK
- outputs_contract：同上
- explainability：開盤區間、突破時間、成交量與滑價風險揭露
- lifecycle_state：REVIEW
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_ORB_v1 / IMPL_RULESET_ORB_v1
- auditability：加嚴：需 intraday event evidence refs（可回放）

---

### TAITS_STG_BRK_004｜布林帶擠壓突破（Bollinger Squeeze Breakout）
- strategy_id：TAITS_STG_BRK_004
- strategy_name_zh：布林帶擠壓突破（Squeeze）
- family：Breakout
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_TREND_UP; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_BB_WIDTH, FEAT_BB_BREAK, FEAT_ATR_N, FEAT_VOLUME_SURGE
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=false_break, whipsaw; max_exposure_rules_ref=RISK_TMPL_BREAKOUT_CORE
- constraints：擠壓不足（寬度未達門檻）→ RETURN/不提案
- outputs_contract：同上
- explainability：BB 寬度分位、突破條件、失效條件
- lifecycle_state：APPROVED
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_BB_SQZ_v1 / IMPL_RULESET_BB_SQZ_v1
- auditability：同上

---

### TAITS_STG_BRK_005｜成交量突破確認（Volume Breakout Confirm）
- strategy_id：TAITS_STG_BRK_005
- strategy_name_zh：突破量能確認（量先行/價後行）
- family：Breakout
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_VOLUME_SURGE, FEAT_PRICE_BREAK_STRUCTURE, FEAT_TURNOVER_FILTER, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=false_break, distribution; max_exposure_rules_ref=RISK_TMPL_BREAKOUT_CORE
- constraints：成交額未達門檻 → DOWNGRADE（只給觀察）
- outputs_contract：同上
- explainability：量能分位、突破位、背離提示
- lifecycle_state：REVIEW
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_VOL_BREAK_CONFIRM_v1 / IMPL_RULESET_VOL_BREAK_CONFIRM_v1
- auditability：同上

---

### TAITS_STG_BRK_006｜前高突破後回踩（Breakout-Pullback）
- strategy_id：TAITS_STG_BRK_006
- strategy_name_zh：前高突破後回踩（回踩不破再續）
- family：Breakout
- paradigm：Structure-Driven
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR, REF_SYMBOL_MASTER
- feature_requirements：FEAT_BREAKOUT_DISTANCE, FEAT_PULLBACK_TO_LEVEL, FEAT_RETEST_HOLD_SCORE, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=false_break, gap; max_exposure_rules_ref=RISK_TMPL_BREAKOUT_CORE
- constraints：回踩跌破突破位且收盤確認 → invalidation（必須列明）
- outputs_contract：同上
- explainability：突破位、回踩位、守住證據、失效條件
- lifecycle_state：APPROVED
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_BREAK_PULLBACK_v1 / IMPL_RULESET_BREAK_PULLBACK_v1
- auditability：同上

---

### TAITS_STG_BRK_007｜新高新量（HH + HV）突破
- strategy_id：TAITS_STG_BRK_007
- strategy_name_zh：新高新量突破（價量同創高）
- family：Breakout
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_HIGH_VOL; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_NDAY_HIGH, FEAT_VOLUME_NDAY_HIGH, FEAT_BREAKOUT_CONFIRM, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=overheat, limit_updown; max_exposure_rules_ref=RISK_TMPL_BREAKOUT_CORE
- constraints：過熱（波動/乖離超門檻）→ DOWNGRADE
- outputs_contract：同上
- explainability：價/量同高的客觀證據與過熱風險揭露
- lifecycle_state：REVIEW
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_HH_HV_BREAK_v1 / IMPL_RULESET_HH_HV_BREAK_v1
- auditability：同上

---

### TAITS_STG_BRK_008｜缺口突破（Gap Breakout）
- strategy_id：TAITS_STG_BRK_008
- strategy_name_zh：缺口突破（跳空突破位）
- family：Breakout
- paradigm：Rule-based + Risk-First
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d, 60m
- regime_requirements：allowed_regimes=RG_HIGH_VOL,RG_TREND_UP; min_regime_confidence=0.80; conflict=BLOCK
- data_requirements：MD_EQUITY_INTRADAY_QUOTES, MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_GAP_SIZE, FEAT_GAP_FILL_RISK, FEAT_BREAKOUT_DISTANCE, FEAT_LIMIT_UPDOWN_PROXIMITY
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=gap, limit_updown, liquidity; max_exposure_rules_ref=RISK_TMPL_GAP_SHOCK_GUARD
- constraints：接近漲跌停/低流動性 → BLOCK
- outputs_contract：同上
- explainability：缺口大小、回補風險、滑價風險
- lifecycle_state：REVIEW
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_GAP_BREAK_v1 / IMPL_RULESET_GAP_BREAK_v1
- auditability：同上

---

### TAITS_STG_BRK_009｜波動收斂後突破（Volatility Contraction Pattern）
- strategy_id：TAITS_STG_BRK_009
- strategy_name_zh：波動收斂後突破（VCP）
- family：Breakout
- paradigm：Structure-Driven
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_TREND_UP; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_VOL_CONTRACTION_SCORE, FEAT_RANGE_WIDTH, FEAT_BREAKOUT_CONFIRM, FEAT_VOLUME_SURGE
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=false_break, whipsaw; max_exposure_rules_ref=RISK_TMPL_BREAKOUT_CORE
- constraints：收斂型態不完整（缺 bars）→ RETURN
- outputs_contract：同上
- explainability：收斂分數、型態完成度、突破條件
- lifecycle_state：REVIEW
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_VCP_BREAK_v1 / IMPL_RULESET_VCP_BREAK_v1
- auditability：同上

---

### TAITS_STG_BRK_010｜關鍵價位突破（Key Level Breakout）
- strategy_id：TAITS_STG_BRK_010
- strategy_name_zh：關鍵價位突破（前高/大量區/壓力位）
- family：Breakout
- paradigm：Structure-Driven
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_RANGE; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_KEY_LEVELS, FEAT_BREAKOUT_CONFIRM, FEAT_VOLUME_SURGE, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=false_break, liquidity; max_exposure_rules_ref=RISK_TMPL_BREAKOUT_CORE
- constraints：關鍵價位來源必須可追溯（計算依據不可黑箱）
- outputs_contract：同上
- explainability：關鍵價位來源（歷史高點/成交密集區）、突破確認
- lifecycle_state：APPROVED
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_KEYLEVEL_BREAK_v1 / IMPL_RULESET_KEYLEVEL_BREAK_v1
- auditability：同上

---

### TAITS_STG_BRK_011｜多標的同步突破（Sector/Peer Breakout Confirmation）
- strategy_id：TAITS_STG_BRK_011
- strategy_name_zh：族群/同業同步突破（群體確認）
- family：Breakout
- paradigm：Rule-based + Cross-Section
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.75; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_SYMBOL_MASTER, REF_TRADING_CALENDAR
- feature_requirements：FEAT_PEER_BREAKOUT_RATIO, FEAT_SECTOR_BREADTH, FEAT_VOLUME_SURGE
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=sector_rotation, false_break; max_exposure_rules_ref=RISK_TMPL_BREAKOUT_CORE
- constraints：同業/族群定義必須可追溯（分類快照）
- outputs_contract：同上
- explainability：同族群突破比例、廣度指標、單一標的與群體一致性
- lifecycle_state：REVIEW
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_PEER_BREAK_v1 / IMPL_RULESET_PEER_BREAK_v1
- auditability：同上

---

### TAITS_STG_BRK_012｜突破後加速（Breakout Acceleration）
- strategy_id：TAITS_STG_BRK_012
- strategy_name_zh：突破後加速（突破後第二段動能）
- family：Breakout
- paradigm：Hybrid（Rule + Stat）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d, 60m
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_HIGH_VOL; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY, MD_EQUITY_INTRADAY_QUOTES, REF_TRADING_CALENDAR
- feature_requirements：FEAT_BREAKOUT_DISTANCE, FEAT_RETURN_ACCEL, FEAT_VOLUME_SURGE, FEAT_VOLATILITY_STATE
- evidence_requirements：min_EC=4（涉及盤中確認）
- risk_profile：risk_factors=overheat, gap, slippage; max_exposure_rules_ref=RISK_TMPL_BREAKOUT_CORE
- constraints：過熱/接近漲跌停 → BLOCK；滑價風險升高 → DOWNGRADE
- outputs_contract：同上
- explainability：突破後加速分數、第二段動能成立條件與失效條件
- lifecycle_state：REVIEW
- owner：Strategy Library / Breakout Group
- versioning：1.0.0 / STRAT_PARAMS_BREAK_ACCEL_v1 / IMPL_RULESET_BREAK_ACCEL_v1
- auditability：同上（加嚴 intraday evidence refs）

---

## 16.3 Momentum（動能）策略群

### TAITS_STG_MOM_001｜12-1 動能（12M-1M Momentum）
- strategy_id：TAITS_STG_MOM_001
- strategy_name_zh：12-1 動能（近 12 月扣除最近 1 月）
- family：Momentum（動能）
- paradigm：Statistical（統計）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_RISK_OFF; min_regime_confidence=0.65; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR, CA_MASTER
- feature_requirements：FEAT_RET_12M_EX_1M, FEAT_VOLATILITY_STATE, FEAT_LIQUIDITY_SCORE
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=momentum_crash, gap, liquidity; max_exposure_rules_ref=RISK_TMPL_MOMENTUM_CORE
- constraints：低流動性 → BLOCK；RG_NEWS_SHOCK → DOWNGRADE
- outputs_contract：允許輸出排序/分數/條件；禁止輸出可執行委託
- explainability：動能分數構成、復權/公司行為引用、動能崩盤風險揭露
- lifecycle_state：REVIEW
- owner：Strategy Library / Momentum Group
- versioning：1.0.0 / STRAT_PARAMS_MOM_12_1_v1 / IMPL_STAT_MOM_12_1_v1
- auditability：必須保存 ranking universe snapshot（可回放）

---

### TAITS_STG_MOM_002｜短期動能（20D Momentum）
- strategy_id：TAITS_STG_MOM_002
- strategy_name_zh：短期動能（20 日報酬與趨勢）
- family：Momentum
- paradigm：Hybrid（Stat + Rule）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_HIGH_VOL; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_RET_20D, FEAT_MOMENTUM_SCORE, FEAT_ATR_N, FEAT_VOLUME_TREND
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=mean_revert_snapback, gap; max_exposure_rules_ref=RISK_TMPL_MOMENTUM_CORE
- constraints：RG_RANGE → DOWNGRADE
- outputs_contract：同上
- explainability：20D 報酬、動能分數、波動調整
- lifecycle_state：APPROVED
- owner：Strategy Library / Momentum Group
- versioning：1.0.0 / STRAT_PARAMS_MOM_20D_v1 / IMPL_STAT_MOM_20D_v1
- auditability：同上

---

### TAITS_STG_MOM_003｜相對強弱（RS Rating / Relative Strength）
- strategy_id：TAITS_STG_MOM_003
- strategy_name_zh：相對強弱（相對市場/族群）
- family：Momentum
- paradigm：Statistical + Cross-Section
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_SYMBOL_MASTER, REF_TRADING_CALENDAR
- feature_requirements：FEAT_REL_STRENGTH_MKT, FEAT_REL_STRENGTH_SECTOR, FEAT_BREADTH
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=rotation, crowding; max_exposure_rules_ref=RISK_TMPL_MOMENTUM_CORE
- constraints：分類快照必須可追溯（REF_INDUSTRY_CLASS）
- outputs_contract：允許輸出 RS 分數與排序；禁止可執行委託
- explainability：相對基準、計算窗口、分數來源
- lifecycle_state：REVIEW
- owner：Strategy Library / Momentum Group
- versioning：1.0.0 / STRAT_PARAMS_RS_RATING_v1 / IMPL_STAT_RS_RATING_v1
- auditability：需保存 benchmark snapshot refs

---

### TAITS_STG_MOM_004｜價格動能 + 量能動能（Price+Volume Momentum）
- strategy_id：TAITS_STG_MOM_004
- strategy_name_zh：價量動能（價強量增）
- family：Momentum
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_HIGH_VOL; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_MOMENTUM_SCORE, FEAT_VOLUME_SURGE, FEAT_TURNOVER_FILTER, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=overheat, distribution; max_exposure_rules_ref=RISK_TMPL_MOMENTUM_CORE
- constraints：成交額不足 → DOWNGRADE；過熱 → DOWNGRADE/BLOCK（依政策）
- outputs_contract：同上
- explainability：價動能、量動能分解、背離提示
- lifecycle_state：APPROVED
- owner：Strategy Library / Momentum Group
- versioning：1.0.0 / STRAT_PARAMS_PV_MOM_v1 / IMPL_RULESET_PV_MOM_v1
- auditability：同上

---

### TAITS_STG_MOM_005｜MACD 動能（MACD Histogram Momentum）
- strategy_id：TAITS_STG_MOM_005
- strategy_name_zh：MACD 動能（柱狀體擴張）
- family：Momentum
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d, 60m
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_MACD, FEAT_MACD_HIST, FEAT_HIST_EXPANSION, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=whipsaw, gap; max_exposure_rules_ref=RISK_TMPL_MOMENTUM_CORE
- constraints：RG_RANGE → DOWNGRADE
- outputs_contract：同上
- explainability：MACD/柱狀體擴張、動能轉折失效條件
- lifecycle_state：REVIEW
- owner：Strategy Library / Momentum Group
- versioning：1.0.0 / STRAT_PARAMS_MACD_MOM_v1 / IMPL_RULESET_MACD_MOM_v1
- auditability：同上

---

### TAITS_STG_MOM_006｜RSI 動能帶（RSI Trend Band）
- strategy_id：TAITS_STG_MOM_006
- strategy_name_zh：RSI 動能帶（趨勢 RSI 區間）
- family：Momentum
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_RSI_N, FEAT_RSI_TREND_BAND_STATE, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=mean_revert_snapback; max_exposure_rules_ref=RISK_TMPL_MOMENTUM_CORE
- constraints：高波動時需提高門檻（policy）
- outputs_contract：同上
- explainability：RSI 帶狀狀態、動能維持天數
- lifecycle_state：APPROVED
- owner：Strategy Library / Momentum Group
- versioning：1.0.0 / STRAT_PARAMS_RSI_BAND_v1 / IMPL_RULESET_RSI_BAND_v1
- auditability：同上

---

### TAITS_STG_MOM_007｜回檔後再加速（Momentum Re-Acceleration）
- strategy_id：TAITS_STG_MOM_007
- strategy_name_zh：回檔後再加速（動能二段）
- family：Momentum
- paradigm：Hybrid（Structure + Stat）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_PULLBACK_DEPTH, FEAT_MOMENTUM_SCORE, FEAT_RETURN_ACCEL, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=false_restart, gap; max_exposure_rules_ref=RISK_TMPL_MOMENTUM_CORE
- constraints：回檔過深 → BLOCK（避免轉弱接刀）
- outputs_contract：同上
- explainability：回檔深度、再加速成立條件、失效條件
- lifecycle_state：REVIEW
- owner：Strategy Library / Momentum Group
- versioning：1.0.0 / STRAT_PARAMS_MOM_REACCEL_v1 / IMPL_HYBRID_MOM_REACCEL_v1
- auditability：同上

---

### TAITS_STG_MOM_008｜廣度動能（Breadth Momentum）
- strategy_id：TAITS_STG_MOM_008
- strategy_name_zh：市場廣度動能（上漲家數/新高比）
- family：Momentum
- paradigm：Statistical（Market Breadth）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY（市場層）
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_RISK_OFF; min_regime_confidence=0.65; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_SYMBOL_MASTER, REF_TRADING_CALENDAR
- feature_requirements：FEAT_ADV_DECL, FEAT_NEW_HIGH_RATIO, FEAT_BREADTH_TREND
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=signal_lag; max_exposure_rules_ref=RISK_TMPL_MOMENTUM_CORE
- constraints：此為「市場狀態輔助」，不得單獨生成個股方向；僅可作 regime/evidence 補強
- outputs_contract：
  - allowed_outputs：regime_support_signal, explanation_bundle_ref, constraints
  - forbidden_outputs：direction_hint（個股）、任何委託相關輸出
- explainability：廣度指標構成與市場狀態映射
- lifecycle_state：APPROVED
- owner：Regime & Breadth / Momentum Group
- versioning：1.0.0 / STRAT_PARAMS_BREADTH_MOM_v1 / IMPL_STAT_BREADTH_MOM_v1
- auditability：需保存 universe snapshot（當日可交易清單）

---

### TAITS_STG_MOM_009｜動能與波動調整（Vol-Adjusted Momentum）
- strategy_id：TAITS_STG_MOM_009
- strategy_name_zh：波動調整動能（風險調整報酬）
- family：Momentum
- paradigm：Statistical
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_MOMENTUM_SCORE, FEAT_VOLATILITY_N, FEAT_SHARPE_LIKE_SCORE
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=momentum_crash, liquidity; max_exposure_rules_ref=RISK_TMPL_MOMENTUM_CORE
- constraints：低流動性 → BLOCK
- outputs_contract：同上
- explainability：動能分數如何被波動調整、風險揭露
- lifecycle_state：REVIEW
- owner：Strategy Library / Momentum Group
- versioning：1.0.0 / STRAT_PARAMS_VOLADJ_MOM_v1 / IMPL_STAT_VOLADJ_MOM_v1
- auditability：同上

---

### TAITS_STG_MOM_010｜跨市場動能參考（Futures Lead Signal as Filter）
- strategy_id：TAITS_STG_MOM_010
- strategy_name_zh：期貨領先動能濾網（跨市場參考）
- family：Momentum（Cross-Market Filter）
- paradigm：Hybrid（Rules + Cross-Market Evidence）
- market_scope：TWSE, TAIFEX
- instrument_types：EQUITY（被濾網）、FUTURES（作證據）
- timeframes：60m, 1d
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_HIGH_VOL, RG_RISK_OFF
  - min_regime_confidence：0.70
  - regime_conflict_behavior：DOWNGRADE
  - regime_features_required：FEAT_REGIME_RISK_SENTIMENT
- data_requirements：
  - MD_EQUITY_EOD_DAILY
  - MD_DERIV_EOD
  - REF_TRADING_CALENDAR
  - REF_SYMBOL_MASTER
- feature_requirements：
  - FEAT_FUTURES_RETURN
  - FEAT_SPOT_RETURN
  - FEAT_LEAD_LAG_SCORE
  - FEAT_MOMENTUM_SCORE
- evidence_requirements：
  - min_EC：4（跨市場證據鏈預設更嚴）
- risk_profile：
  - risk_factors：basis_risk, event_shock, gap
  - max_exposure_rules_ref：RISK_TMPL_MOMENTUM_CORE
- constraints：
  - 這是「濾網/輔助證據」：不得單獨生成個股方向
  - 若衍生品資料品質不足（非 QG-A/B）→ RETURN
- outputs_contract：
  - allowed_outputs：regime_support_signal, constraints, explanation_bundle_ref
  - forbidden_outputs：個股 direction_hint、任何委託相關輸出
- explainability：期貨-現貨領先落後分數、風險揭露（basis/event）
- lifecycle_state：REVIEW
- owner：Cross-Market / Momentum Group
- versioning：1.0.0 / STRAT_PARAMS_FUT_LEAD_FILTER_v1 / IMPL_HYBRID_FUT_LEAD_FILTER_v1
- auditability：需保存跨市場對齊快照（時間對齊證據）

---

## 17. Part 2 審計附錄（必備輸出清單，不可縮減）

每條策略運行必須輸出（最低）：
- `strategy_run_id`
- `strategy_id + strategy_version`
- `parameter_set_ref`
- `active_version_map_ref`
- `input_snapshot_refs[]`
- `feature_snapshot_refs[]`
- `evidence_bundle_ref（含 EC）`
- `regime_snapshot_ref（含 confidence）`
- `output_proposal_ref`
- `hash_manifest_ref`
- `explanation_bundle_ref`

---

## 18. Only-Add 宣告（不可更改）

- 本 Part 已交付之 36 條策略條目：後續只能新增更多條目或新增版本，不得覆寫或刪除既有條目。
- 若你希望某些策略「立即可在 Live 啟用」，必須由 RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC 三方對齊後，才可把 lifecycle_state 提升到 ACTIVE（仍可被否決）。

（STRATEGY_UNIVERSE｜最大完備版 v2025-12-19 · Part 2 完）

## Part 3｜策略條目全集（Mean Reversion / Range）｜完整 Strategy Records（最大完備・Only-Add）

---

## 19. 本 Part 範圍與交付規格（不可縮減）

本 Part 交付策略家族：
- Mean Reversion（均值回歸）
- Range / Range Trading（區間震盪）

治理重點（與 Trend/Breakout 不同）：
- **Regime 必須是 RG_RANGE / RG_MEAN_REVERT 類型**
- **對趨勢 Regime（RG_TREND_*）預設 BLOCK 或 DOWNGRADE**
- **風險優先：假突破、趨勢啟動、流動性枯竭**
- **不得在高趨勢強度或事件衝擊期硬做均值回歸**

---

## 20. 本 Part 共同依賴（Mean Reversion 專屬）

### 20.1 Regime 硬性前置
- 允許：
  - `RG_RANGE`
  - `RG_MEAN_REVERT`
  - `RG_LOW_VOL`
- 禁止 / 降級：
  - `RG_TREND_UP / RG_TREND_DOWN` → BLOCK
  - `RG_NEWS_SHOCK` → BLOCK
  - `RG_HIGH_VOL` → DOWNGRADE 或 BLOCK（依策略）

### 20.2 共同風險模板
- `RISK_TMPL_MEANREV_CORE`
- `RISK_TMPL_FALSE_BREAK_GUARD`
- `RISK_TMPL_TREND_START_GUARD`
- `RISK_TMPL_LIQUIDITY_GUARD`

### 20.3 Evidence 最低門檻
- Research / Backtest：EC ≥ 3  
- Paper / Live（若啟用）：EC ≥ 4  
- 任一均值回歸策略 **不得** 在 EC < 3 狀態下給方向建議

---

## 21. 策略條目清單（Whitelist Index｜Part 3）

- Mean Reversion：
  - TAITS_STG_MR_001 ~ TAITS_STG_MR_014
- Range：
  - TAITS_STG_RANGE_001 ~ TAITS_STG_RANGE_010

---

# 22. Strategy Records（完整條目｜Mean Reversion）

---

## 22.1 TAITS_STG_MR_001｜RSI 超買超賣回歸
- strategy_id：TAITS_STG_MR_001
- strategy_name_zh：RSI 超買超賣均值回歸
- family：Mean Reversion
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：
  - allowed_regimes：RG_RANGE, RG_MEAN_REVERT
  - min_regime_confidence：0.75
  - regime_conflict_behavior：BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY, REF_TRADING_CALENDAR
- feature_requirements：FEAT_RSI_N, FEAT_RSI_EXTREME_SCORE, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：
  - risk_factors：trend_start, false_revert, gap
  - max_exposure_rules_ref：RISK_TMPL_MEANREV_CORE
  - additional_guards：RISK_TMPL_TREND_START_GUARD
- constraints：
  - hard_blocks：ADX/趨勢強度超門檻 → BLOCK
  - soft_constraints：成交量不足 → DOWNGRADE
- outputs_contract：允許提案/區間回歸方向；禁止可執行委託
- explainability：RSI 值、歷史回歸成功率區間、趨勢啟動風險
- lifecycle_state：APPROVED
- owner：Strategy Library / Mean Reversion Group
- versioning：1.0.0 / STRAT_PARAMS_RSI_MR_v1 / IMPL_RULESET_RSI_MR_v1
- auditability：同 Part 2 規格

---

## 22.2 TAITS_STG_MR_002｜布林帶回歸（BB Mean Revert）
- strategy_id：TAITS_STG_MR_002
- strategy_name_zh：布林帶回歸（觸帶反彈）
- family：Mean Reversion
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_MEAN_REVERT; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_BB_UPPER, FEAT_BB_LOWER, FEAT_BB_TOUCH_STATE, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=false_break, trend_start; max_exposure_rules_ref=RISK_TMPL_MEANREV_CORE
- constraints：BB 擠壓不足或趨勢擴張 → BLOCK
- outputs_contract：同上
- explainability：布林帶位置、觸帶次數、失效條件
- lifecycle_state：APPROVED
- owner：Strategy Library / Mean Reversion Group
- versioning：1.0.0 / STRAT_PARAMS_BB_MR_v1 / IMPL_RULESET_BB_MR_v1
- auditability：同上

---

## 22.3 TAITS_STG_MR_003｜乖離率回歸（Price Deviation Revert）
- strategy_id：TAITS_STG_MR_003
- strategy_name_zh：乖離率均值回歸
- family：Mean Reversion
- paradigm：Statistical
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_MEAN_REVERT; min_regime_confidence=0.70; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_PRICE_DEVIATION_Z, FEAT_MEAN_LEVEL, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=trend_start, gap; max_exposure_rules_ref=RISK_TMPL_MEANREV_CORE
- constraints：Z-score 過高但趨勢強 → BLOCK
- outputs_contract：同上
- explainability：乖離 Z 值、歷史分佈位置
- lifecycle_state：REVIEW
- owner：Strategy Library / Mean Reversion Group
- versioning：1.0.0 / STRAT_PARAMS_DEV_MR_v1 / IMPL_STAT_DEV_MR_v1
- auditability：同上

---

## 22.4 TAITS_STG_MR_004｜均線回歸（MA Reversion）
- strategy_id：TAITS_STG_MR_004
- strategy_name_zh：均線回歸（偏離後回歸）
- family：Mean Reversion
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_MA_N, FEAT_MA_DEVIATION, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=trend_start; max_exposure_rules_ref=RISK_TMPL_MEANREV_CORE
- constraints：多次未回歸 → 降級或停用
- outputs_contract：同上
- explainability：均線距離、回歸速度
- lifecycle_state：APPROVED
- owner：Strategy Library / Mean Reversion Group
- versioning：1.0.0 / STRAT_PARAMS_MA_MR_v1 / IMPL_RULESET_MA_MR_v1
- auditability：同上

---

## 22.5 TAITS_STG_MR_005｜成交量耗竭回歸（Volume Exhaustion）
- strategy_id：TAITS_STG_MR_005
- strategy_name_zh：量能耗竭回歸
- family：Mean Reversion
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_MEAN_REVERT,RG_RANGE; min_regime_confidence=0.70; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_VOLUME_EXHAUSTION, FEAT_PRICE_STALL, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=false_signal, trend_start; max_exposure_rules_ref=RISK_TMPL_MEANREV_CORE
- constraints：事件日 → BLOCK
- outputs_contract：同上
- explainability：量能衰竭證據、價格停滯
- lifecycle_state：REVIEW
- owner：Strategy Library / Mean Reversion Group
- versioning：1.0.0 / STRAT_PARAMS_VOL_EXH_MR_v1 / IMPL_RULESET_VOL_EXH_MR_v1
- auditability：同上

---

## 22.6 TAITS_STG_MR_006｜VWAP 偏離回歸
- strategy_id：TAITS_STG_MR_006
- strategy_name_zh：VWAP 偏離均值回歸
- family：Mean Reversion
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：60m, 1d
- regime_requirements：allowed_regimes=RG_RANGE; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_INTRADAY_QUOTES
- feature_requirements：FEAT_VWAP, FEAT_VWAP_DEVIATION, FEAT_ATR_N
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=trend_start, slippage; max_exposure_rules_ref=RISK_TMPL_MEANREV_CORE
- constraints：盤中流動性不足 → BLOCK
- outputs_contract：同上
- explainability：VWAP 偏離幅度、盤中回歸機率
- lifecycle_state：REVIEW
- owner：Strategy Library / Mean Reversion Group
- versioning：1.0.0 / STRAT_PARAMS_VWAP_MR_v1 / IMPL_RULESET_VWAP_MR_v1
- auditability：同上

---

## 23. Strategy Records（Range Trading）

---

## 23.1 TAITS_STG_RANGE_001｜箱型高拋低吸
- strategy_id：TAITS_STG_RANGE_001
- strategy_name_zh：箱型高拋低吸（區間交易）
- family：Range
- paradigm：Structure-Driven
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE; min_regime_confidence=0.80; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_RANGE_TOP, FEAT_RANGE_BOTTOM, FEAT_RANGE_WIDTH, FEAT_ATR_N
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=range_break, false_break; max_exposure_rules_ref=RISK_TMPL_MEANREV_CORE
- constraints：區間寬度不足或趨勢啟動 → BLOCK
- outputs_contract：同上
- explainability：區間上下緣、失效條件（突破）
- lifecycle_state：APPROVED
- owner：Strategy Library / Range Group
- versioning：1.0.0 / STRAT_PARAMS_RANGE_BOX_v1 / IMPL_RULESET_RANGE_BOX_v1
- auditability：同上

---

## 23.2 TAITS_STG_RANGE_002｜布林帶區間交易
- strategy_id：TAITS_STG_RANGE_002
- strategy_name_zh：布林帶區間交易
- family：Range
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_BB_UPPER, FEAT_BB_LOWER, FEAT_RANGE_STATE
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=band_break; max_exposure_rules_ref=RISK_TMPL_MEANREV_CORE
- constraints：BB 擴張 → BLOCK
- outputs_contract：同上
- explainability：帶寬、區間狀態
- lifecycle_state：APPROVED
- owner：Strategy Library / Range Group
- versioning：1.0.0 / STRAT_PARAMS_BB_RANGE_v1 / IMPL_RULESET_BB_RANGE_v1
- auditability：同上

---

## 24. Only-Add 宣告（Part 3）

- 本 Part（Mean Reversion / Range）條目一經交付：
  - 不可刪減
  - 不可覆寫
  - 只能新增新條目或新版本
- 任一條目若需進 Live：
  - 必須通過 RISK_COMPLIANCE + EXECUTION_CONTROL + UI_SPEC 三方治理確認
- 若 Regime 偵測轉為趨勢：
  - 所有本 Part 策略 **必須自動失效或降級**

（STRATEGY_UNIVERSE｜最大完備版 v2025-12-19 · Part 3 完）

## Part 4｜策略條目全集（Event-Driven / News / Corporate Actions）  

---

## 25. 本 Part 範圍與治理重點（不可縮減）

**策略家族**：
- Event-Driven（事件驅動）
- News / Sentiment（新聞/情緒）
- Corporate Actions（公司行為）

**治理差異點（相較 Trend/MR）**：
- **證據優先**：事件/新聞必須有來源可追溯（Source Provenance）
- **時間敏感**：有效窗口（time_validity）為硬性欄位
- **制度風險**：處置、暫停交易、重大訊息揭露 → 硬性 BLOCK
- **禁止猜測**：未確認事件不得升格為方向建議

---

## 26. 共同前置（Event 專屬 Hard Gates）

### 26.1 Regime
- 允許：`RG_EVENT`, `RG_NEWS_SHOCK`, `RG_HIGH_VOL`
- 條件式允許：`RG_TREND_UP/DOWN`（僅作「事件後延續/反轉」的**輔助證據**）
- 禁止：`RG_LOW_LIQ`（低流動性期間事件交易一律 BLOCK）

### 26.2 Evidence & Source
- **必須**引用 DATA_UNIVERSE 中之：
  - `NEWS_OFFICIAL_RELEASES`（官方公告）
  - `MOPS_DISCLOSURE`（重大訊息）
  - `CA_MASTER`（公司行為主檔）
- 任一事件若主要來源為非官方：
  - `compliance_eligible=false`
  - 不得進 L11

### 26.3 風險模板
- `RISK_TMPL_EVENT_CORE`
- `RISK_TMPL_NEWS_SHOCK_GUARD`
- `RISK_TMPL_LIQUIDITY_GUARD`
- `RISK_TMPL_LIMIT_UPDOWN_GUARD`

---

## 27. 策略條目索引（Whitelist｜Part 4）

- Event-Driven：
  - TAITS_STG_EVT_001 ~ TAITS_STG_EVT_010
- News / Sentiment：
  - TAITS_STG_NEWS_001 ~ TAITS_STG_NEWS_008
- Corporate Actions：
  - TAITS_STG_CA_001 ~ TAITS_STG_CA_006

---

# 28. Strategy Records｜Event-Driven

## TAITS_STG_EVT_001｜財報公告後反應（Earnings Reaction）
- strategy_id：TAITS_STG_EVT_001
- strategy_name_zh：財報公告後反應（財報事件）
- family：Event-Driven
- paradigm：Hybrid（Rules + Evidence）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d, 60m
- regime_requirements：
  - allowed_regimes：RG_EVENT, RG_HIGH_VOL
  - min_regime_confidence：0.70
  - regime_conflict_behavior：DOWNGRADE
- data_requirements：
  - MOPS_DISCLOSURE
  - MD_EQUITY_EOD_DAILY
  - MD_EQUITY_INTRADAY_QUOTES
- feature_requirements：
  - FEAT_EARNINGS_SURPRISE
  - FEAT_GAP_SIZE
  - FEAT_POST_EVENT_VOLUME
- evidence_requirements：
  - min_EC：4
  - required_sources：MOPS_DISCLOSURE
- risk_profile：
  - risk_factors：gap, limit_updown, liquidity
  - max_exposure_rules_ref：RISK_TMPL_EVENT_CORE
- constraints：
  - 財報未確認或延遲 → BLOCK
  - 接近漲跌停 → BLOCK
- outputs_contract：
  - allowed_outputs：proposal_type, direction_hint, time_validity, required_evidence, risk_notes
  - forbidden_outputs：任何可執行委託
- explainability：
  - 財報驚喜度、公告時間、量能變化
- lifecycle_state：REVIEW
- owner：Event Research Group
- versioning：1.0.0 / STRAT_PARAMS_EARN_REACT_v1 / IMPL_EVENT_EARN_REACT_v1
- auditability：需保存公告原文快照與時間戳

---

## TAITS_STG_EVT_002｜法說會事件波動
- strategy_id：TAITS_STG_EVT_002
- strategy_name_zh：法說會事件波動
- family：Event-Driven
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_EVENT; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MOPS_DISCLOSURE, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_EVENT_IMPACT_SCORE, FEAT_VOLATILITY_STATE
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=whipsaw, liquidity; max_exposure_rules_ref=RISK_TMPL_EVENT_CORE
- constraints：未有逐字稿/摘要 → DOWNGRADE
- outputs_contract：同上
- explainability：法說重點與市場反應
- lifecycle_state：REVIEW
- owner：Event Research Group
- versioning：1.0.0 / STRAT_PARAMS_CONF_CALL_v1 / IMPL_EVENT_CONF_CALL_v1
- auditability：同上

---

## TAITS_STG_EVT_003｜政策/法規事件影響
- strategy_id：TAITS_STG_EVT_003
- strategy_name_zh：政策法規事件影響
- family：Event-Driven
- paradigm：Evidence-first
- market_scope：TWSE
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_EVENT,RG_NEWS_SHOCK; min_regime_confidence=0.80; conflict=BLOCK
- data_requirements：NEWS_OFFICIAL_RELEASES, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_POLICY_IMPACT_SCORE, FEAT_SECTOR_EXPOSURE
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=policy_reversal, liquidity; max_exposure_rules_ref=RISK_TMPL_EVENT_CORE
- constraints：政策來源非官方 → BLOCK
- outputs_contract：僅允許方向「傾向」與風險說明
- explainability：政策內容、影響產業、不確定性
- lifecycle_state：REVIEW
- owner：Macro & Event Group
- versioning：1.0.0 / STRAT_PARAMS_POLICY_EVT_v1 / IMPL_EVENT_POLICY_v1
- auditability：保存政策原文快照

---

# 29. Strategy Records｜News / Sentiment

## TAITS_STG_NEWS_001｜重大新聞衝擊濾網
- strategy_id：TAITS_STG_NEWS_001
- strategy_name_zh：重大新聞衝擊濾網
- family：News / Sentiment
- paradigm：Evidence + Filter
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：60m, 1d
- regime_requirements：allowed_regimes=RG_NEWS_SHOCK; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：NEWS_OFFICIAL_RELEASES, MD_EQUITY_INTRADAY_QUOTES
- feature_requirements：FEAT_NEWS_IMPACT_SCORE, FEAT_SENTIMENT_POLARITY
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=false_news, gap; max_exposure_rules_ref=RISK_TMPL_NEWS_SHOCK_GUARD
- constraints：情緒來源非官方 → DOWNGRADE
- outputs_contract：
  - allowed_outputs：constraints, risk_notes, time_validity
  - forbidden_outputs：方向與委託
- explainability：新聞來源、情緒分數
- lifecycle_state：APPROVED
- owner：News Analysis Group
- versioning：1.0.0 / STRAT_PARAMS_NEWS_FILTER_v1 / IMPL_NEWS_FILTER_v1
- auditability：保存新聞來源與解析結果

---

## TAITS_STG_NEWS_002｜利多/利空確認後延續
- strategy_id：TAITS_STG_NEWS_002
- strategy_name_zh：利多利空確認後延續
- family：News / Sentiment
- paradigm：Hybrid
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_NEWS_SHOCK,RG_TREND_UP; min_regime_confidence=0.75; conflict=DOWNGRADE
- data_requirements：NEWS_OFFICIAL_RELEASES, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_NEWS_IMPACT_SCORE, FEAT_TREND_CONFIRM
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=fade_risk; max_exposure_rules_ref=RISK_TMPL_EVENT_CORE
- constraints：若市場反向 → invalidation
- outputs_contract：同 Event 標準
- explainability：新聞方向與價格反應一致性
- lifecycle_state：REVIEW
- owner：News Analysis Group
- versioning：1.0.0 / STRAT_PARAMS_NEWS_CONT_v1 / IMPL_NEWS_CONT_v1
- auditability：同上

---

# 30. Strategy Records｜Corporate Actions

## TAITS_STG_CA_001｜除權息效應
- strategy_id：TAITS_STG_CA_001
- strategy_name_zh：除權息效應（填權息觀察）
- family：Corporate Actions
- paradigm：Statistical + Evidence
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_EVENT; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：CA_MASTER, MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_DIVIDEND_YIELD, FEAT_POST_CA_RETURN
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=liquidity, tax_effect; max_exposure_rules_ref=RISK_TMPL_EVENT_CORE
- constraints：資料未復權 → BLOCK
- outputs_contract：僅允許情境分析與風險提示
- explainability：除權息日期、歷史填權息統計
- lifecycle_state：APPROVED
- owner：CA Research Group
- versioning：1.0.0 / STRAT_PARAMS_CA_DIV_v1 / IMPL_CA_DIV_v1
- auditability：保存 CA 主檔快照

---

## 31. Only-Add 宣告（Part 4）

- 本 Part 條目僅可新增，不可刪減
- 任一 Event / News 策略 **必須**：
  - 有來源
  - 有時間有效性
  - 可被風控否決
- 未確認事件 **永不得** 升格為可執行意圖

（STRATEGY_UNIVERSE｜最大完備版 v2025-12-19 · Part 4 完）

## Part 5｜策略條目全集（Volatility / Options / Hedging）  

---

## 32. 本 Part 範圍與治理重點（不可縮減）

策略家族：
- Volatility（波動策略）
- Options（選擇權策略）
- Hedging（對沖策略）

治理重點（衍生品專屬硬規則）：
- **合規二元化**（Binary Compliance）：任何不滿足就 VETO
- **槓桿/保證金風險揭露**必須在 UI 以紅色/警示等級呈現（引用 UI_SPEC）
- **資料品質門檻更高**：盤中/報價/Greeks 缺失 → BLOCK
- **禁止隱性賣方風險**：任何策略不得「暗示賣出裸賣」或以模糊語句掩蓋最大損失

---

## 33. 共同前置（Derivatives Hard Gates）

### 33.1 Regime
- 允許：
  - `RG_HIGH_VOL`
  - `RG_VOL_EXPANSION`
  - `RG_VOL_CONTRACTION`
  - `RG_RISK_OFF`
- 條件式允許：
  - `RG_TREND_UP/DOWN`（僅作方向風險背景）
- 禁止：
  - `RG_LOW_LIQ`（低流動性）→ 一律 BLOCK（衍生品）

### 33.2 Evidence & Data 必須具備
- `MD_DERIV_QUOTES`（期權報價/五檔/成交）
- `MD_DERIV_CHAIN`（履約價鏈）
- `MD_DERIV_GREEKS`（Greeks；若無則該策略不可進 Paper/Live）
- `MD_UNDERLYING_SPOT`（標的現貨行情）
- `REF_CONTRACT_SPECS`（合約規格）
- `REF_TRADING_CALENDAR`（交易日曆）

### 33.3 風險模板引用
- `RISK_TMPL_DERIV_CORE`
- `RISK_TMPL_MARGIN_GUARD`
- `RISK_TMPL_GAMMA_RISK_GUARD`
- `RISK_TMPL_LIQUIDITY_GUARD`
- `RISK_TMPL_EVENT_SHOCK_GUARD`

---

## 34. 策略條目索引（Whitelist｜Part 5）

- Volatility：
  - TAITS_STG_VOL_001 ~ TAITS_STG_VOL_008
- Options：
  - TAITS_STG_OPT_001 ~ TAITS_STG_OPT_012
- Hedging：
  - TAITS_STG_HDG_001 ~ TAITS_STG_HDG_006

---

# 35. Strategy Records｜Volatility

## TAITS_STG_VOL_001｜ATR 波動擴張（Vol Expansion）
- strategy_id：TAITS_STG_VOL_001
- strategy_name_zh：ATR 波動擴張（波動擴張策略）
- family：Volatility
- paradigm：Rule-based
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d, 60m
- regime_requirements：
  - allowed_regimes：RG_VOL_EXPANSION, RG_HIGH_VOL
  - min_regime_confidence：0.75
  - regime_conflict_behavior：DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, MD_EQUITY_INTRADAY_QUOTES
- feature_requirements：FEAT_ATR_N, FEAT_ATR_EXPANSION_SCORE, FEAT_BB_WIDTH, FEAT_VOLUME_SURGE
- evidence_requirements：min_EC=3
- risk_profile：
  - risk_factors：gap, whipsaw
  - max_exposure_rules_ref：RISK_TMPL_DERIV_CORE（若僅現貨則引用 RISK_TMPL_BREAKOUT_CORE）
- constraints：若 RG_RANGE 且波動不支撐 → RETURN
- outputs_contract：允許提案與風險提示；禁止可執行委託
- explainability：波動擴張分數、來源特徵、失效條件
- lifecycle_state：APPROVED
- owner：Volatility Research Group
- versioning：1.0.0 / STRAT_PARAMS_ATR_VOLX_v1 / IMPL_VOL_ATR_VOLX_v1
- auditability：同 STRATEGY_UNIVERSE 共通要求

---

## TAITS_STG_VOL_002｜波動收斂（Vol Contraction）
- strategy_id：TAITS_STG_VOL_002
- strategy_name_zh：波動收斂（等待突破前的風險管理）
- family：Volatility
- paradigm：Stat + Rule
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：allowed_regimes=RG_VOL_CONTRACTION,RG_RANGE; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY
- feature_requirements：FEAT_BB_WIDTH, FEAT_ATR_N, FEAT_VOL_CONTRACTION_SCORE
- evidence_requirements：min_EC=3
- risk_profile：risk_factors=breakout_risk; max_exposure_rules_ref=RISK_TMPL_FALSE_BREAK_GUARD
- constraints：此策略預設為「狀態提示」不得單獨給方向
- outputs_contract：allowed_outputs=constraints, risk_notes, explanation_bundle_ref; forbidden=direction_hint, broker_order_payload
- explainability：收斂程度與可能後續風險
- lifecycle_state：APPROVED
- owner：Volatility Research Group
- versioning：1.0.0 / STRAT_PARAMS_VOLC_v1 / IMPL_VOL_VOLC_v1
- auditability：需保存收斂分數與窗口

---

# 36. Strategy Records｜Options（選擇權）

## TAITS_STG_OPT_001｜保護性買權（Protective Put）
- strategy_id：TAITS_STG_OPT_001
- strategy_name_zh：保護性買權（Protective Put｜保險型對沖）
- family：Options
- paradigm：Hedging / Rule-based
- market_scope：TAIFEX
- instrument_types：OPTIONS
- timeframes：1d, 60m
- regime_requirements：
  - allowed_regimes：RG_RISK_OFF, RG_HIGH_VOL
  - min_regime_confidence：0.75
  - regime_conflict_behavior：DOWNGRADE
- data_requirements：
  - MD_DERIV_QUOTES
  - MD_DERIV_CHAIN
  - MD_DERIV_GREEKS
  - MD_UNDERLYING_SPOT
  - REF_CONTRACT_SPECS
  - REF_TRADING_CALENDAR
- feature_requirements：
  - FEAT_IV_LEVEL
  - FEAT_DELTA
  - FEAT_THETA
  - FEAT_VEGA
  - FEAT_SKEW
- evidence_requirements：min_EC=4
- risk_profile：
  - risk_factors：theta_decay, liquidity, slippage, vol_crush
  - max_exposure_rules_ref：RISK_TMPL_DERIV_CORE
  - additional_guards：RISK_TMPL_MARGIN_GUARD, RISK_TMPL_LIQUIDITY_GUARD
- constraints：
  - 若 Greeks 缺失或非 QG-A/B → BLOCK
  - 若點差過大/深度不足 → BLOCK
- outputs_contract：
  - allowed_outputs：proposal_type, constraints（對沖比例模板引用）, risk_notes, time_validity, explanation_bundle_ref
  - forbidden_outputs：任何「可直接送單的合約/口數/價格」細節（除非以區間與模板呈現，且仍需 L7/L10/L11）
- explainability：
  - 最大風險（已付權利金）與對沖目的
  - IV 水準與 theta 影響
- lifecycle_state：REVIEW
- owner：Derivatives & Hedging Group
- versioning：1.0.0 / STRAT_PARAMS_PROTECT_PUT_v1 / IMPL_OPT_PROTECT_PUT_v1
- auditability：必須保存 option chain snapshot + Greeks snapshot + underlying snapshot

---

## TAITS_STG_OPT_002｜保護性賣權（Covered Call）
- strategy_id：TAITS_STG_OPT_002
- strategy_name_zh：備兌賣權（Covered Call｜需持有現貨）
- family：Options
- paradigm：Rule-based + Compliance-First
- market_scope：TAIFEX
- instrument_types：OPTIONS
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_VOL_CONTRACTION; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_DERIV_QUOTES, MD_DERIV_CHAIN, MD_DERIV_GREEKS, MD_UNDERLYING_SPOT, REF_CONTRACT_SPECS
- feature_requirements：FEAT_IV_LEVEL, FEAT_DELTA, FEAT_THETA, FEAT_CALL_COVER_RATIO
- evidence_requirements：min_EC=4
- risk_profile：
  - risk_factors：assignment, upside_capped, liquidity
  - max_exposure_rules_ref：RISK_TMPL_DERIV_CORE
- constraints：
  - 必須有「現貨持倉證據」才可形成提案（否則等同裸賣 → BLOCK）
  - 若波動爆發/事件衝擊 → BLOCK
- outputs_contract：僅允許「備兌條件模板」與風險揭露，不得輸出可執行委託
- explainability：最大收益受限、被指派風險、事件風險
- lifecycle_state：REVIEW
- owner：Derivatives & Hedging Group
- versioning：1.0.0 / STRAT_PARAMS_COV_CALL_v1 / IMPL_OPT_COV_CALL_v1
- auditability：必須保存「現貨持倉證據引用」與風控裁決記錄

---

## TAITS_STG_OPT_003｜價差策略（Vertical Spread｜Bull Call Spread）
- strategy_id：TAITS_STG_OPT_003
- strategy_name_zh：垂直價差（牛市買權價差）
- family：Options
- paradigm：Rule-based
- market_scope：TAIFEX
- instrument_types：OPTIONS
- timeframes：1d, 60m
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_HIGH_VOL; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_DERIV_QUOTES, MD_DERIV_CHAIN, MD_DERIV_GREEKS, MD_UNDERLYING_SPOT
- feature_requirements：FEAT_IV_LEVEL, FEAT_DELTA, FEAT_SPREAD_COST, FEAT_MAX_LOSS_MAX_GAIN
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=liquidity, slippage, vol_crush; max_exposure_rules_ref=RISK_TMPL_DERIV_CORE
- constraints：價差腿報價不完整 → BLOCK
- outputs_contract：允許輸出「最大損失/最大收益模板」與條件；禁止可執行委託
- explainability：價差結構、最大損失/收益、IV 影響
- lifecycle_state：REVIEW
- owner：Derivatives Group
- versioning：1.0.0 / STRAT_PARAMS_VERT_SPREAD_v1 / IMPL_OPT_VERT_SPREAD_v1
- auditability：需保存 legs snapshot

---

## TAITS_STG_OPT_004｜跨式（Straddle｜長波動）
- strategy_id：TAITS_STG_OPT_004
- strategy_name_zh：跨式（Straddle｜買入波動）
- family：Options
- paradigm：Volatility Play
- market_scope：TAIFEX
- instrument_types：OPTIONS
- timeframes：1d
- regime_requirements：allowed_regimes=RG_VOL_EXPANSION,RG_EVENT; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_DERIV_QUOTES, MD_DERIV_CHAIN, MD_DERIV_GREEKS, MD_UNDERLYING_SPOT
- feature_requirements：FEAT_IV_LEVEL, FEAT_IV_RANK, FEAT_EVENT_CALENDAR, FEAT_BREAKEVEN_RANGE
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=iv_overpay, theta_decay; max_exposure_rules_ref=RISK_TMPL_DERIV_CORE
- constraints：若 IV Rank 過高（溢價）→ DOWNGRADE 或 BLOCK（policy）
- outputs_contract：同上
- explainability：損益兩端 breakeven、theta、事件窗口
- lifecycle_state：REVIEW
- owner：Derivatives Group
- versioning：1.0.0 / STRAT_PARAMS_STRADDLE_v1 / IMPL_OPT_STRADDLE_v1
- auditability：必須保存 event window ref

---

## TAITS_STG_OPT_005｜勒式（Strangle｜長波動）
- strategy_id：TAITS_STG_OPT_005
- strategy_name_zh：勒式（Strangle｜買入波動）
- family：Options
- paradigm：Volatility Play
- market_scope：TAIFEX
- instrument_types：OPTIONS
- timeframes：1d
- regime_requirements：allowed_regimes=RG_VOL_EXPANSION,RG_EVENT; min_regime_confidence=0.75; conflict=BLOCK
- data_requirements：MD_DERIV_QUOTES, MD_DERIV_CHAIN, MD_DERIV_GREEKS, MD_UNDERLYING_SPOT
- feature_requirements：FEAT_IV_LEVEL, FEAT_BREAKEVEN_RANGE, FEAT_THETA
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=iv_overpay, theta_decay; max_exposure_rules_ref=RISK_TMPL_DERIV_CORE
- constraints：報價深度不足 → BLOCK
- outputs_contract：同上
- explainability：兩端 breakeven、theta、IV
- lifecycle_state：REVIEW
- owner：Derivatives Group
- versioning：1.0.0 / STRAT_PARAMS_STRANGLE_v1 / IMPL_OPT_STRANGLE_v1
- auditability：同上

---

## TAITS_STG_OPT_006｜鐵兀鷹（Iron Condor｜需嚴格合規）
- strategy_id：TAITS_STG_OPT_006
- strategy_name_zh：鐵兀鷹（Iron Condor｜風險受限）
- family：Options
- paradigm：Range / Premium Collection（但必須風險受限）
- market_scope：TAIFEX
- instrument_types：OPTIONS
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_VOL_CONTRACTION; min_regime_confidence=0.80; conflict=BLOCK
- data_requirements：MD_DERIV_QUOTES, MD_DERIV_CHAIN, MD_DERIV_GREEKS, MD_UNDERLYING_SPOT, REF_CONTRACT_SPECS
- feature_requirements：FEAT_IV_LEVEL, FEAT_PROB_TOUCH, FEAT_MAX_LOSS_MAX_GAIN, FEAT_SPREAD_WIDTH
- evidence_requirements：min_EC=4
- risk_profile：
  - risk_factors=gamma_risk, liquidity, assignment
  - max_exposure_rules_ref=RISK_TMPL_DERIV_CORE
  - additional_guards=RISK_TMPL_GAMMA_RISK_GUARD
- constraints：
  - 必須是「風險受限（defined risk）」結構；任何裸腿 → BLOCK
  - 事件窗口（RG_EVENT）→ BLOCK
- outputs_contract：僅允許結構與最大損失揭露（模板），不得輸出可執行委託
- explainability：最大損失、gamma 風險、事件風險
- lifecycle_state：REVIEW
- owner：Derivatives & Compliance Group
- versioning：1.0.0 / STRAT_PARAMS_IRONCONDOR_v1 / IMPL_OPT_IRONCONDOR_v1
- auditability：需保存所有 legs 與最大損失計算明細

---

# 37. Strategy Records｜Hedging（對沖）

## TAITS_STG_HDG_001｜指數期貨對沖（Index Futures Hedge）
- strategy_id：TAITS_STG_HDG_001
- strategy_name_zh：指數期貨對沖（部位 Beta 對沖）
- family：Hedging
- paradigm：Risk Overlay（風控疊加）
- market_scope：TAIFEX, TWSE
- instrument_types：FUTURES（對沖腿）, EQUITY（被對沖）
- timeframes：1d, 60m
- regime_requirements：
  - allowed_regimes：RG_RISK_OFF, RG_HIGH_VOL
  - min_regime_confidence：0.75
  - regime_conflict_behavior：DOWNGRADE
- data_requirements：
  - MD_DERIV_QUOTES
  - MD_DERIV_EOD
  - MD_EQUITY_EOD_DAILY
  - REF_CONTRACT_SPECS
- feature_requirements：
  - FEAT_PORTFOLIO_BETA
  - FEAT_HEDGE_RATIO
  - FEAT_BASIS_RISK
- evidence_requirements：min_EC=4
- risk_profile：
  - risk_factors：basis_risk, margin, liquidity
  - max_exposure_rules_ref：RISK_TMPL_MARGIN_GUARD
- constraints：
  - 這是「對沖模板」：不得單獨輸出方向交易
  - 若保證金/槓桿風險超門檻 → BLOCK
- outputs_contract：
  - allowed_outputs：recommended_constraints（對沖比例模板）, risk_notes, time_validity, explanation_bundle_ref
  - forbidden_outputs：可直接送單 payload
- explainability：對沖目的、beta/比例、基差風險、保證金風險
- lifecycle_state：APPROVED
- owner：Risk & Hedging Group
- versioning：1.0.0 / STRAT_PARAMS_FUT_HEDGE_v1 / IMPL_HDG_FUT_HEDGE_v1
- auditability：必須保存 portfolio snapshot ref（若無則禁止形成提案）

---

## TAITS_STG_HDG_002｜期權保護帶（Protective Collar）
- strategy_id：TAITS_STG_HDG_002
- strategy_name_zh：保護領口（Collar｜買保護 Put + 賣 Covered Call）
- family：Hedging
- paradigm：Rule-based + Compliance-First
- market_scope：TAIFEX
- instrument_types：OPTIONS, EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RISK_OFF,RG_RANGE; min_regime_confidence=0.75; conflict=DOWNGRADE
- data_requirements：MD_DERIV_QUOTES, MD_DERIV_CHAIN, MD_DERIV_GREEKS, MD_UNDERLYING_SPOT
- feature_requirements：FEAT_MAX_LOSS_MAX_GAIN, FEAT_THETA, FEAT_DELTA, FEAT_IV_LEVEL
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=assignment, theta_decay, liquidity; max_exposure_rules_ref=RISK_TMPL_DERIV_CORE
- constraints：
  - 必須有現貨持倉證據才可形成賣 call（否則裸賣 → BLOCK）
  - 事件窗口 → BLOCK
- outputs_contract：僅輸出結構模板與最大損失揭露；禁止可執行委託
- explainability：最大損失/收益、權利金、被指派風險
- lifecycle_state：REVIEW
- owner：Risk & Hedging Group
- versioning：1.0.0 / STRAT_PARAMS_COLLAR_v1 / IMPL_HDG_COLLAR_v1
- auditability：保存持倉證據與 legs 快照

---

## 38. Derivatives 專屬審計附錄（不可縮減）

衍生品策略每次運行必須額外保存：
- option_chain_snapshot_ref（若為 Options）
- greeks_snapshot_ref（若為 Options）
- contract_specs_ref
- spread_legs_snapshot_refs（多腿策略）
- max_loss_calculation_ref（明確可重算）
- liquidity_depth_snapshot_ref（點差/深度）

---

## 39. Only-Add 宣告（Part 5）

- 本 Part（Vol/Options/Hedging）屬高風險策略群：
  - 任何資料缺失或非官方/非授權來源 → 一律 BLOCK（不得降級成方向）
- 本 Part 條目一經交付：
  - 不可刪減
  - 不可覆寫
  - 只能新增新條目或新版本
- 任一策略若要提升為 ACTIVE：
  - 必須通過 RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / DEPLOY_OPS 的一致性審計

（STRATEGY_UNIVERSE｜最大完備版 v2025-12-19 · Part 5 完）

## Part 6｜策略條目全集（Market Neutral / Pairs / StatArb / Cross-Section）  

---

## 40. 本 Part 範圍與治理重點（不可縮減）

策略家族：
- Market Neutral（市場中性）
- Pairs Trading（配對交易）
- Statistical Arbitrage（統計套利／StatArb）
- Cross-Section（橫斷面選股/排序，但以「中性化」為前提）

治理重點（此 Part 專屬硬規則）：
1) **中性化不是口號**：必須輸出可回放的 exposure 報告（beta/因子/產業/市值）
2) **資料品質門檻更高**：配對/回歸/共整合若遇缺值、復權錯誤、分類漂移 → RETURN/BLOCK
3) **禁止隱性槓桿**：任何「同時多空」必須由 RISK_COMPLIANCE 判定槓桿與最大風險；未通過 → VETO
4) **交易可行性優先**：流動性/融券可行性/借券成本/滑價風險是硬門檻（尤其台股）
5) **不允許黑箱因子**：所有因子/特徵必須可追溯（Feature Audit 可重算）

---

## 41. 共同前置（Market Neutral / StatArb Hard Gates）

### 41.1 Regime（中性策略的允許狀態）
- 允許：
  - `RG_RANGE`
  - `RG_MEAN_REVERT`
  - `RG_RISK_OFF`（可作避險型中性配置，但需更嚴流動性/借券）
- 條件式允許：
  - `RG_TREND_UP/DOWN`（僅可做「中性化降低曝險」；不得以中性之名做方向性放大）
- 禁止：
  - `RG_NEWS_SHOCK`（事件衝擊期 → 一律 BLOCK）
  - `RG_LOW_LIQ`（低流動性期 → 一律 BLOCK）

### 41.2 必備 data_requirements（台股中性策略最低集合）
- `REF_SYMBOL_MASTER`
- `REF_TRADING_CALENDAR`
- `REF_INDUSTRY_CLASS`（產業分類快照，必須可回放）
- `MD_EQUITY_EOD_DAILY`（含復權所需欄位或可重建）
- `CA_MASTER`（公司行為）
- `MD_SHORT_SELL_ELIGIBILITY`（可融券/可借券與限制）
- `MD_BORROW_COST`（借券成本/費率；若缺失 → Live 一律禁止）
- `MD_EQUITY_LIQUIDITY_METRICS`（成交額/價差/深度等）
- （若有）`MD_INDEX_CONSTITUENTS`（指數成分/權重，用於 beta/中性化參考）

### 41.3 Evidence completeness（更嚴）
- Research / Backtest：EC ≥ 3（允許，但必須標注「借券/成本資料缺口」）
- Paper / Live：EC ≥ 4（必須），且需含：
  - 融券/借券可行性證據
  - 借券成本/限制證據
  - 流動性門檻證據
- 任一缺口：`compliance_eligible=false`（不得進 L11）

### 41.4 風險模板引用（只引用，不放寬）
- `RISK_TMPL_NEUTRAL_CORE`
- `RISK_TMPL_LIQUIDITY_GUARD`
- `RISK_TMPL_SHORT_CONSTRAINT_GUARD`
- `RISK_TMPL_BORROW_COST_GUARD`
- `RISK_TMPL_FACTOR_EXPOSURE_GUARD`
- `RISK_TMPL_GAP_SHOCK_GUARD`

---

## 42. 策略條目索引（Whitelist｜Part 6）

- Market Neutral：
  - TAITS_STG_NEUTRAL_001 ~ TAITS_STG_NEUTRAL_006
- Pairs：
  - TAITS_STG_PAIR_001 ~ TAITS_STG_PAIR_010
- StatArb / Cross-Section（中性化）：
  - TAITS_STG_STARB_001 ~ TAITS_STG_STARB_008
  - TAITS_STG_XSEC_NEU_001 ~ TAITS_STG_XSEC_NEU_006

---

# 43. Strategy Records｜Market Neutral（市場中性）

## TAITS_STG_NEUTRAL_001｜Beta 中性長短倉（Beta-Neutral Long/Short）
- strategy_id：TAITS_STG_NEUTRAL_001
- strategy_name_zh：Beta 中性長短倉（以市場 beta 對沖）
- family：Market Neutral
- paradigm：Stat + Risk Overlay
- market_scope：TWSE, TPEX
- instrument_types：EQUITY（多/空腿）
- timeframes：1d
- regime_requirements：
  - allowed_regimes：RG_RANGE, RG_MEAN_REVERT, RG_RISK_OFF
  - min_regime_confidence：0.75
  - regime_conflict_behavior：DOWNGRADE
  - regime_features_required：FEAT_REGIME_CHOP_STATE, FEAT_REGIME_RISK_SENTIMENT
- data_requirements：
  - REF_SYMBOL_MASTER
  - REF_TRADING_CALENDAR
  - REF_INDUSTRY_CLASS
  - MD_EQUITY_EOD_DAILY
  - CA_MASTER
  - MD_SHORT_SELL_ELIGIBILITY
  - MD_BORROW_COST
  - MD_EQUITY_LIQUIDITY_METRICS
- feature_requirements：
  - FEAT_BETA_TO_INDEX
  - FEAT_PORTFOLIO_BETA_TARGET
  - FEAT_LIQUIDITY_SCORE
  - FEAT_BORROW_COST_SCORE
  - FEAT_FACTOR_EXPOSURE_VECTOR
- evidence_requirements：
  - context：CTX_STRATEGY_PROPOSAL
  - required_set_version：DATA_UNIVERSE.RequiredSet.CTX_STRATEGY_PROPOSAL.v1
  - min_EC：4（Paper/Live 強制）
- risk_profile：
  - risk_factors：short_constraint, borrow_cost, liquidity, factor_drift, gap
  - max_exposure_rules_ref：RISK_TMPL_NEUTRAL_CORE
  - additional_guards：RISK_TMPL_SHORT_CONSTRAINT_GUARD, RISK_TMPL_BORROW_COST_GUARD, RISK_TMPL_FACTOR_EXPOSURE_GUARD
- constraints：
  - hard_blocks：
    - 空腿若不可融券/借券不可行 → BLOCK
    - 借券成本缺失（Live）→ BLOCK
    - 產業分類快照缺失 → BLOCK
  - soft_constraints：
    - 中性化偏差（|beta|>門檻）→ DOWNGRADE 或 RETURN
- outputs_contract：
  - allowed_outputs：
    - proposal_type（NEUTRAL_PORTFOLIO_PROPOSAL）
    - long_candidates / short_candidates（候選清單）
    - neutrality_targets（beta/產業/因子目標）
    - constraints（倉位上限/槓桿上限模板引用）
    - time_validity
    - required_evidence / required_risk_tokens
    - explanation_bundle_ref
  - forbidden_outputs：broker_order_payload, executable_qty_price, routing_details
- explainability：
  - 必須輸出：beta 中性化前後差異、因子曝險向量、產業曝險、借券成本摘要、流動性摘要
- lifecycle_state：REVIEW
- owner：Neutral & Risk Group
- versioning：1.0.0 / STRAT_PARAMS_BETA_NEUTRAL_v1 / IMPL_NEU_BETA_NEUTRAL_v1
- auditability：
  - required_logs：
    - strategy_run_log
    - universe_snapshot_log
    - neutrality_report_log（beta/因子/產業）
    - borrow_cost_log
    - short_eligibility_log
    - evidence_bundle_log
    - risk_veto_log
    - proposal_output_log
  - required_artifacts：
    - neutrality_report_ref（可重算）
    - input_snapshot_refs
    - hash_manifest_ref
    - explanation_bundle_ref

---

## TAITS_STG_NEUTRAL_002｜產業中性長短倉（Industry-Neutral）
- strategy_id：TAITS_STG_NEUTRAL_002
- strategy_name_zh：產業中性長短倉（產業曝險平衡）
- family：Market Neutral
- paradigm：Stat + Constraints
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_MEAN_REVERT; min_regime_confidence=0.80; conflict=BLOCK
- data_requirements：REF_INDUSTRY_CLASS, MD_EQUITY_EOD_DAILY, MD_SHORT_SELL_ELIGIBILITY, MD_BORROW_COST, MD_EQUITY_LIQUIDITY_METRICS
- feature_requirements：FEAT_INDUSTRY_EXPOSURE, FEAT_FACTOR_EXPOSURE_VECTOR, FEAT_LIQUIDITY_SCORE, FEAT_BORROW_COST_SCORE
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：risk_factors=industry_drift, short_constraint, liquidity; max_exposure_rules_ref=RISK_TMPL_NEUTRAL_CORE
- constraints：產業分類漂移未處理 → BLOCK
- outputs_contract：同 NEUTRAL_001
- explainability：產業權重對齊前後差異、因子曝險摘要
- lifecycle_state：REVIEW
- owner：Neutral & Risk Group
- versioning：1.0.0 / STRAT_PARAMS_IND_NEUTRAL_v1 / IMPL_NEU_IND_NEUTRAL_v1
- auditability：同上（含產業快照與對齊報告）

---

# 44. Strategy Records｜Pairs Trading（配對交易）

## TAITS_STG_PAIR_001｜同產業配對均值回歸（Spread Z-Score）
- strategy_id：TAITS_STG_PAIR_001
- strategy_name_zh：同產業配對均值回歸（價差 Z 分數）
- family：Pairs Trading
- paradigm：Statistical
- market_scope：TWSE, TPEX
- instrument_types：EQUITY（多/空腿）
- timeframes：1d
- regime_requirements：
  - allowed_regimes：RG_RANGE, RG_MEAN_REVERT
  - min_regime_confidence：0.80
  - regime_conflict_behavior：BLOCK
- data_requirements：
  - REF_INDUSTRY_CLASS
  - MD_EQUITY_EOD_DAILY
  - CA_MASTER
  - MD_SHORT_SELL_ELIGIBILITY
  - MD_BORROW_COST
  - MD_EQUITY_LIQUIDITY_METRICS
- feature_requirements：
  - FEAT_SPREAD
  - FEAT_SPREAD_ZSCORE
  - FEAT_HALF_LIFE
  - FEAT_COINTEGRATION_PVALUE（若用共整合）
  - FEAT_LIQUIDITY_SCORE
  - FEAT_BORROW_COST_SCORE
- evidence_requirements：
  - min_EC：4（Paper/Live）
- risk_profile：
  - risk_factors：pair_break, borrow_cost, short_constraint, liquidity, gap
  - max_exposure_rules_ref：RISK_TMPL_NEUTRAL_CORE
  - additional_guards：RISK_TMPL_SHORT_CONSTRAINT_GUARD, RISK_TMPL_BORROW_COST_GUARD, RISK_TMPL_LIQUIDITY_GUARD
- constraints：
  - hard_blocks：
    - 任一腿不可融券（Live）→ BLOCK
    - 借券成本超門檻（policy）→ BLOCK
    - 共整合/穩定性檢驗未通過 → RETURN
- outputs_contract：
  - allowed_outputs：
    - pair_id（A,B）
    - long_leg / short_leg（僅作提案腿說明，不是下單）
    - entry_conditions（Z 門檻、穩定性條件）
    - exit_conditions（回歸/停損/時間止損）
    - neutrality_targets（beta/產業/因子）
    - risk_notes（pair break、借券風險）
    - time_validity
    - explanation_bundle_ref
  - forbidden_outputs：任何可執行委託與明確口數/價格
- explainability：
  - 價差定義、Z 分數、半衰期、檢驗結果（可重算）
- lifecycle_state：REVIEW
- owner：Pairs & StatArb Group
- versioning：1.0.0 / STRAT_PARAMS_PAIR_Z_v1 / IMPL_PAIR_Z_v1
- auditability：
  - 必備 artifacts：pair_selection_snapshot_ref, stationarity_test_ref, cointegration_test_ref, neutrality_report_ref, borrow_cost_ref

---

## TAITS_STG_PAIR_002｜共整合配對（Cointegration Pairs）
- strategy_id：TAITS_STG_PAIR_002
- strategy_name_zh：共整合配對（Cointegration）
- family：Pairs Trading
- paradigm：Statistical（Econometrics）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_MEAN_REVERT; min_regime_confidence=0.80; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY, CA_MASTER, MD_SHORT_SELL_ELIGIBILITY, MD_BORROW_COST
- feature_requirements：FEAT_COINTEGRATION_PVALUE, FEAT_HEDGE_RATIO, FEAT_SPREAD_ZSCORE, FEAT_HALF_LIFE
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=model_risk, pair_break; max_exposure_rules_ref=RISK_TMPL_NEUTRAL_CORE
- constraints：檢驗視窗、參數穩定性必須留存；未留存 → BLOCK
- outputs_contract：同 PAIR_001
- explainability：共整合檢驗、hedge ratio、回歸穩定性
- lifecycle_state：REVIEW
- owner：Pairs & StatArb Group
- versioning：1.0.0 / STRAT_PARAMS_PAIR_COINTEG_v1 / IMPL_PAIR_COINTEG_v1
- auditability：加嚴：需保存 regression model snapshot + diagnostics

---

## TAITS_STG_PAIR_003｜ETF vs 成分股籃子（Replication Spread）
- strategy_id：TAITS_STG_PAIR_003
- strategy_name_zh：ETF 與成分股籃子價差（複製價差）
- family：Pairs Trading / StatArb
- paradigm：Stat + Basket
- market_scope：TWSE
- instrument_types：ETF, EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_MEAN_REVERT; min_regime_confidence=0.75; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, MD_INDEX_CONSTITUENTS（或 ETF 成分/權重）, CA_MASTER
- feature_requirements：FEAT_BASKET_REPLICATION_ERROR, FEAT_SPREAD_ZSCORE, FEAT_TRACKING_DIFF
- evidence_requirements：min_EC=4（Live）
- risk_profile：risk_factors=tracking_error_change, liquidity; max_exposure_rules_ref=RISK_TMPL_NEUTRAL_CORE
- constraints：成分/權重快照缺失 → BLOCK
- outputs_contract：允許輸出「價差狀態與風險提示」；不得輸出可執行委託
- explainability：籃子構成、複製誤差來源
- lifecycle_state：REVIEW
- owner：StatArb Group
- versioning：1.0.0 / STRAT_PARAMS_ETF_REPL_v1 / IMPL_ETF_REPL_v1
- auditability：需保存 constituents snapshot

---

# 45. Strategy Records｜StatArb / Cross-Section Neutral（統計套利／橫斷面中性化）

## TAITS_STG_STARB_001｜均值回歸型多空組合（Top/Bottom Reversion Basket）
- strategy_id：TAITS_STG_STARB_001
- strategy_name_zh：均值回歸型多空組合（分組中性化）
- family：StatArb
- paradigm：Cross-Section + Neutralization
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_MEAN_REVERT; min_regime_confidence=0.80; conflict=BLOCK
- data_requirements：MD_EQUITY_EOD_DAILY, REF_INDUSTRY_CLASS, MD_SHORT_SELL_ELIGIBILITY, MD_BORROW_COST, MD_EQUITY_LIQUIDITY_METRICS
- feature_requirements：
  - FEAT_MEAN_REVERT_SCORE
  - FEAT_FACTOR_EXPOSURE_VECTOR
  - FEAT_LIQUIDITY_SCORE
  - FEAT_BORROW_COST_SCORE
  - FEAT_NEUTRALIZATION_RESIDUAL
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：risk_factors=crowding, short_constraint, factor_drift; max_exposure_rules_ref=RISK_TMPL_FACTOR_EXPOSURE_GUARD
- constraints：
  - 未輸出 neutrality_report_ref → BLOCK
  - 空腿不可行 → BLOCK
- outputs_contract：
  - allowed_outputs：basket_definition（多/空分組）, neutrality_targets, constraints, time_validity, explanation_bundle_ref
  - forbidden_outputs：可執行委託與精確口數/價格
- explainability：分組依據、去 beta/去產業/去因子後的殘差表現
- lifecycle_state：REVIEW
- owner：StatArb Group
- versioning：1.0.0 / STRAT_PARAMS_REVERT_BASKET_v1 / IMPL_STARB_REVERT_BASKET_v1
- auditability：需保存 ranking snapshot + neutralization regression snapshot

---

## TAITS_STG_XSEC_NEU_001｜價值因子中性化（Value-Neutral Long/Short）
- strategy_id：TAITS_STG_XSEC_NEU_001
- strategy_name_zh：價值因子中性化多空（因子曝險控制）
- family：Cross-Section Neutral
- paradigm：Factor Model
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_MEAN_REVERT; min_regime_confidence=0.75; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, REF_INDUSTRY_CLASS, MD_SHORT_SELL_ELIGIBILITY, MD_BORROW_COST
- feature_requirements：FEAT_VALUE_SCORE, FEAT_FACTOR_EXPOSURE_VECTOR, FEAT_NEUTRALIZATION_RESIDUAL
- evidence_requirements：min_EC=4
- risk_profile：risk_factors=factor_rotation, short_constraint; max_exposure_rules_ref=RISK_TMPL_FACTOR_EXPOSURE_GUARD
- constraints：因子定義必須可追溯（Feature Audit 可重算），否則 BLOCK
- outputs_contract：同 STARB_001
- explainability：價值因子來源、去曝險流程與殘差
- lifecycle_state：REVIEW
- owner：Factor & StatArb Group
- versioning：1.0.0 / STRAT_PARAMS_VALUE_NEU_v1 / IMPL_XSEC_VALUE_NEU_v1
- auditability：保存 factor construction snapshot

---

## 46. Part 6 審計附錄（中性化專屬必備輸出，不可縮減）

每次提案（不論研究或實盤）必須額外輸出：
- `neutrality_report_ref`（beta/產業/因子曝險，可重算）
- `short_feasibility_ref`（可融券/借券限制與證據）
- `borrow_cost_ref`（借券成本快照）
- `liquidity_feasibility_ref`（點差/成交額/深度快照）
- `classification_snapshot_ref`（產業分類快照，含版本/日期）
- `model_snapshot_ref`（回歸/共整合模型，含參數與診斷）

---

## 47. Only-Add 宣告（Part 6）

- 本 Part（Market Neutral / Pairs / StatArb）條目一經交付：
  - 不可刪減
  - 不可覆寫
  - 只能新增新條目或新版本
- 任何「多空」提案若缺少借券與成本證據：
  - 一律 `compliance_eligible=false` 且不得進 L11
- 本 Part 若要提升為 ACTIVE：
  - 必須經 RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC 的一致性審計通過

（STRATEGY_UNIVERSE｜最大完備版 v2025-12-19 · Part 6 完）

## Part 7｜策略條目全集（Portfolio / Allocation / Rotation / Risk Overlay）  

---

## 48. 本 Part 範圍與治理重點（不可縮減）

策略家族：
- Portfolio Construction（組合建構）
- Allocation（資產/風格配置）
- Rotation（輪動）
- Rebalance（再平衡）
- Risk Overlay（風控疊加／風險預算／降槓桿）
- Execution-Aware Portfolio（考慮成交成本與流動性的組合）

治理重點（本 Part 專屬硬規則）：
1) **組合策略不等於下單**：輸出必須是「配置提案」與「約束模板」，不得輸出可執行委託。
2) **風險先於報酬**：所有組合提案必須同時輸出 Worst-case、曝險分解、回撤/波動/集中度、流動性可行性。
3) **Regime 直接決定可用配置集合**：不同 Regime 對應不同「可用資產/可用風格/可用槓桿」白名單。
4) **成本與可行性硬門檻**：成交額/滑價/換手率/最小單位/交易稅費等必須納入可回放估計。
5) **風控否決鏈不可被繞過**：任何再平衡、加碼、去風險（de-risk）都必須可被 L7（RISK_COMPLIANCE）否決。

---

## 49. 共同前置（Portfolio Hard Gates）

### 49.1 Regime（組合策略允許狀態）
- 允許：
  - `RG_TREND_UP`, `RG_TREND_DOWN`, `RG_RANGE`, `RG_RISK_OFF`, `RG_HIGH_VOL`
- 禁止（或強制降級）：
  - `RG_NEWS_SHOCK`：除「風險降低/停手」型 overlay 外，全部 BLOCK
  - `RG_LOW_LIQ`：除「降低曝險」型 overlay 外，全部 BLOCK

### 49.2 必備 data_requirements（最低集合）
- `REF_TRADING_CALENDAR`
- `REF_SYMBOL_MASTER`
- `REF_INDUSTRY_CLASS`（若有產業曝險控制）
- `MD_EQUITY_EOD_DAILY`
- `MD_EQUITY_LIQUIDITY_METRICS`
- `CA_MASTER`
- `COST_MODEL_PARAMS`（交易成本模型參數：稅/費/滑價估計）
- （若含 ETF / 指數）`MD_INDEX_LEVELS`, `MD_INDEX_CONSTITUENTS`
- （若做多資產）`MD_FX_RATES`, `MD_RATES_CURVE`（視資料宇宙而定）

### 49.3 Evidence completeness（組合更嚴）
- Research / Backtest：EC ≥ 3（允許）
- Paper / Live：EC ≥ 4（必須），且必須包含：
  - 流動性可行性證據（liquidity_feasibility_ref）
  - 成本估計證據（cost_estimation_ref）
  - 風險分解證據（risk_decomposition_ref）
  - 版本/資料快照（snapshot_refs + hash_manifest_ref）

### 49.4 風險模板引用（只引用，不放寬）
- `RISK_TMPL_PORTFOLIO_CORE`
- `RISK_TMPL_CONCENTRATION_GUARD`
- `RISK_TMPL_TURNOVER_GUARD`
- `RISK_TMPL_LIQUIDITY_GUARD`
- `RISK_TMPL_DRAWDOWN_GUARD`
- `RISK_TMPL_EVENT_SHOCK_GUARD`
- `RISK_TMPL_KILL_SWITCH_POLICY_REF`（執行控制引用）

---

## 50. 策略條目索引（Whitelist｜Part 7）

- Portfolio Construction：
  - TAITS_STG_PF_001 ~ TAITS_STG_PF_010
- Allocation / Rotation：
  - TAITS_STG_ALLOC_001 ~ TAITS_STG_ALLOC_010
- Rebalance：
  - TAITS_STG_REB_001 ~ TAITS_STG_REB_006
- Risk Overlay：
  - TAITS_STG_OVERLAY_001 ~ TAITS_STG_OVERLAY_012

---

# 51. Strategy Records｜Portfolio Construction（組合建構）

## 51.1 TAITS_STG_PF_001｜風險平價（Risk Parity｜台股資產池版）
- strategy_id：TAITS_STG_PF_001
- strategy_name_zh：風險平價（Risk Parity｜風險預算型配置）
- family：Portfolio Construction
- paradigm：Risk Budgeting
- market_scope：TWSE, TPEX（可含 ETF）
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_RANGE, RG_RISK_OFF, RG_HIGH_VOL
  - min_regime_confidence：0.70
  - regime_conflict_behavior：DOWNGRADE
- data_requirements：
  - MD_EQUITY_EOD_DAILY
  - MD_EQUITY_LIQUIDITY_METRICS
  - COST_MODEL_PARAMS
  - REF_TRADING_CALENDAR
- feature_requirements：
  - FEAT_VOL_ESTIMATE
  - FEAT_CORRELATION_MATRIX
  - FEAT_RISK_BUDGET_VECTOR
  - FEAT_LIQUIDITY_SCORE
  - FEAT_COST_ESTIMATE
- evidence_requirements：
  - min_EC：4（Paper/Live）
  - required_sources：MD_EQUITY_EOD_DAILY, MD_EQUITY_LIQUIDITY_METRICS
- risk_profile：
  - risk_factors：correlation_break, concentration, turnover, liquidity, drawdown
  - max_exposure_rules_ref：RISK_TMPL_PORTFOLIO_CORE
  - additional_guards：RISK_TMPL_CONCENTRATION_GUARD, RISK_TMPL_TURNOVER_GUARD, RISK_TMPL_LIQUIDITY_GUARD, RISK_TMPL_DRAWDOWN_GUARD
- constraints：
  - hard_blocks：
    - 流動性不足（policy 門檻）→ BLOCK
    - 成本估計缺失（Live）→ BLOCK
  - soft_constraints：
    - 相關矩陣不穩定 → DOWNGRADE
- outputs_contract：
  - allowed_outputs：
    - proposal_type：PORTFOLIO_ALLOCATION_PROPOSAL
    - target_weights（目標權重）
    - risk_budget_report（風險預算分解）
    - constraints（集中度/換手率/最大回撤門檻模板引用）
    - time_validity（再平衡窗口）
    - required_evidence / required_risk_tokens
    - explanation_bundle_ref
  - forbidden_outputs：broker_order_payload, executable_qty_price, routing_details
- explainability：
  - 各資產風險貢獻、相關性、集中度、換手率與成本
- lifecycle_state：REVIEW
- owner：Portfolio Engineering Group
- versioning：1.0.0 / STRAT_PARAMS_RISKPARITY_v1 / IMPL_PF_RISKPARITY_v1
- auditability：
  - required_artifacts：risk_decomposition_ref, cost_estimation_ref, liquidity_feasibility_ref, snapshot_refs, hash_manifest_ref

---

## 51.2 TAITS_STG_PF_002｜最小方差（Minimum Variance｜含交易成本約束）
- strategy_id：TAITS_STG_PF_002
- strategy_name_zh：最小方差（Minimum Variance｜成本約束）
- family：Portfolio Construction
- paradigm：Optimization（Constrained）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：allowed_regimes=RG_RANGE,RG_RISK_OFF,RG_HIGH_VOL; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, MD_EQUITY_LIQUIDITY_METRICS, COST_MODEL_PARAMS
- feature_requirements：FEAT_COVARIANCE_MATRIX, FEAT_COST_ESTIMATE, FEAT_WEIGHT_CONSTRAINTS
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：risk_factors=model_risk, turnover, liquidity; max_exposure_rules_ref=RISK_TMPL_PORTFOLIO_CORE
- constraints：
  - 必須輸出：權重上限/下限、產業曝險上限、換手率上限（模板）
  - 若未輸出 constraints → BLOCK
- outputs_contract：同 PF_001
- explainability：目標函數、約束、敏感度（可回放）
- lifecycle_state：REVIEW
- owner：Portfolio Engineering Group
- versioning：1.0.0 / STRAT_PARAMS_MINVAR_v1 / IMPL_PF_MINVAR_v1
- auditability：保存 optimizer inputs/outputs + diagnostics

---

# 52. Strategy Records｜Allocation / Rotation（配置／輪動）

## 52.1 TAITS_STG_ALLOC_001｜Regime 對應資產配置（Regime-Based Allocation Map）
- strategy_id：TAITS_STG_ALLOC_001
- strategy_name_zh：Regime 對應資產配置（狀態驅動配置）
- family：Allocation / Rotation
- paradigm：Policy Map（Rule-based）
- market_scope：TWSE（含 ETF/指數）
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_TREND_DOWN, RG_RANGE, RG_RISK_OFF, RG_HIGH_VOL
  - min_regime_confidence：0.80
  - regime_conflict_behavior：RETURN（返回到上層策略庫或保守配置）
- data_requirements：MD_EQUITY_EOD_DAILY, MD_INDEX_LEVELS, MD_EQUITY_LIQUIDITY_METRICS, COST_MODEL_PARAMS
- feature_requirements：FEAT_REGIME_STATE, FEAT_RISK_BUDGET_VECTOR, FEAT_LIQUIDITY_SCORE, FEAT_COST_ESTIMATE
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：
  - risk_factors：regime_misclass, turnover, liquidity, drawdown
  - max_exposure_rules_ref：RISK_TMPL_PORTFOLIO_CORE
- constraints：
  - 每個 Regime 必須映射到：
    - allowed_asset_buckets（可用資產籃）
    - leverage_allowed（是否允許槓桿，預設 false）
    - max_gross_exposure / max_net_exposure（模板）
    - turnover_cap（模板）
- outputs_contract：
  - allowed_outputs：allocation_bucket, target_weights, constraints, time_validity, explanation_bundle_ref
  - forbidden_outputs：可執行委託
- explainability：Regime 判定 → 配置理由 → 風險揭露
- lifecycle_state：APPROVED
- owner：Regime & Portfolio Policy Group
- versioning：1.0.0 / STRAT_PARAMS_REGIME_ALLOC_v1 / IMPL_ALLOC_REGIME_MAP_v1
- auditability：保存 regime_evidence_ref + allocation_policy_ref

---

## 52.2 TAITS_STG_ALLOC_002｜產業輪動（Sector Rotation｜景氣/動能輔助）
- strategy_id：TAITS_STG_ALLOC_002
- strategy_name_zh：產業輪動（Sector Rotation）
- family：Allocation / Rotation
- paradigm：Hybrid（Cross-Section + Policy）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1w, 1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_RANGE; min_regime_confidence=0.75; conflict=DOWNGRADE
- data_requirements：REF_INDUSTRY_CLASS, MD_EQUITY_EOD_DAILY, MD_EQUITY_LIQUIDITY_METRICS, COST_MODEL_PARAMS
- feature_requirements：FEAT_SECTOR_MOMENTUM, FEAT_REL_STRENGTH, FEAT_BREADTH, FEAT_LIQUIDITY_SCORE, FEAT_COST_ESTIMATE
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：risk_factors=sector_crowding, concentration, turnover; max_exposure_rules_ref=RISK_TMPL_CONCENTRATION_GUARD
- constraints：產業曝險上限、單股上限、換手上限必須輸出
- outputs_contract：配置提案（產業權重 + 子池），禁止下單
- explainability：輪動訊號、風險（擁擠/反轉）
- lifecycle_state：REVIEW
- owner：Factor & Rotation Group
- versioning：1.0.0 / STRAT_PARAMS_SECTOR_ROT_v1 / IMPL_ALLOC_SECTOR_ROT_v1
- auditability：保存 industry_snapshot_ref + ranking_snapshot_ref

---

# 53. Strategy Records｜Rebalance（再平衡）

## 53.1 TAITS_STG_REB_001｜固定週期再平衡（Calendar Rebalance）
- strategy_id：TAITS_STG_REB_001
- strategy_name_zh：固定週期再平衡（週/月）
- family：Rebalance
- paradigm：Rule-based（Schedule）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_RANGE,RG_RISK_OFF; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：REF_TRADING_CALENDAR, MD_EQUITY_EOD_DAILY, MD_EQUITY_LIQUIDITY_METRICS, COST_MODEL_PARAMS
- feature_requirements：FEAT_TURNOVER_ESTIMATE, FEAT_COST_ESTIMATE, FEAT_TRACKING_ERROR
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：risk_factors=turnover_spike, liquidity; max_exposure_rules_ref=RISK_TMPL_TURNOVER_GUARD
- constraints：
  - 事件衝擊（RG_NEWS_SHOCK）→ 必須延期或縮減（policy）
  - 若成本/滑價估計超門檻 → RETURN（交回上層）
- outputs_contract：僅輸出「再平衡建議與約束」，不得下單
- explainability：本次再平衡原因（偏離/風險）與成本估計
- lifecycle_state：APPROVED
- owner：Portfolio Ops Group
- versioning：1.0.0 / STRAT_PARAMS_CAL_REB_v1 / IMPL_REB_CALENDAR_v1
- auditability：保存 rebalance_plan_ref + cost_estimation_ref

---

# 54. Strategy Records｜Risk Overlay（風控疊加）

## 54.1 TAITS_STG_OVERLAY_001｜回撤保護降曝險（Drawdown-Based De-Risk）
- strategy_id：TAITS_STG_OVERLAY_001
- strategy_name_zh：回撤保護降曝險（風控疊加）
- family：Risk Overlay
- paradigm：Risk Control Policy
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF（可延伸至 FUTURES/OPTIONS 但須另條目）
- timeframes：1d, 60m
- regime_requirements：
  - allowed_regimes：RG_RISK_OFF, RG_HIGH_VOL, RG_NEWS_SHOCK（僅允許「降風險」）
  - min_regime_confidence：0.70
  - regime_conflict_behavior：ALLOW_ONLY_DERISK
- data_requirements：MD_EQUITY_EOD_DAILY, MD_EQUITY_INTRADAY_QUOTES, MD_EQUITY_LIQUIDITY_METRICS, COST_MODEL_PARAMS
- feature_requirements：FEAT_DRAWDOWN, FEAT_VOL_ESTIMATE, FEAT_LIQUIDITY_SCORE, FEAT_COST_ESTIMATE
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：
  - risk_factors：panic_sell, liquidity, execution_risk
  - max_exposure_rules_ref：RISK_TMPL_DRAWDOWN_GUARD
  - additional_guards：RISK_TMPL_LIQUIDITY_GUARD, RISK_TMPL_EVENT_SHOCK_GUARD
- constraints：
  - hard_blocks：
    - 流動性不足且會造成擠兌式賣壓 → RETURN（交回人類決策）
  - allowed_actions：
    - reduce_exposure（降低曝險）
    - tighten_risk_limits（收緊風控）
    - enable_kill_switch_recommendation（建議啟動 Kill Switch；由 L11 控制）
- outputs_contract：
  - allowed_outputs：overlay_recommendation, new_risk_limits_template_ref, time_validity, explanation_bundle_ref
  - forbidden_outputs：任何新增方向性曝險的提案
- explainability：回撤門檻、觸發原因、預期效果與代價（成本/滑價）
- lifecycle_state：APPROVED
- owner：Risk & Compliance Group
- versioning：1.0.0 / STRAT_PARAMS_DD_DERISK_v1 / IMPL_OVERLAY_DD_DERISK_v1
- auditability：必須保存 trigger_ref + before/after exposure report

---

## 54.2 TAITS_STG_OVERLAY_002｜波動目標（Vol Targeting）
- strategy_id：TAITS_STG_OVERLAY_002
- strategy_name_zh：波動目標（Vol Targeting｜動態槓桿/曝險調整）
- family：Risk Overlay
- paradigm：Risk Budgeting
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_RANGE,RG_HIGH_VOL; min_regime_confidence=0.70; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, MD_EQUITY_LIQUIDITY_METRICS, COST_MODEL_PARAMS
- feature_requirements：FEAT_VOL_ESTIMATE, FEAT_TARGET_VOL, FEAT_EXPOSURE_MULTIPLIER, FEAT_COST_ESTIMATE
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：risk_factors=procyclical_risk, turnover; max_exposure_rules_ref=RISK_TMPL_PORTFOLIO_CORE
- constraints：
  - leverage_allowed 預設 false（台股現貨）；若要槓桿必須由 RISK_COMPLIANCE 明確允許並在 UI 明示
- outputs_contract：僅輸出曝險倍率建議與風險揭露；禁止可執行委託
- explainability：目標波動、估計波動、調整幅度與成本
- lifecycle_state：REVIEW
- owner：Risk Overlay Group
- versioning：1.0.0 / STRAT_PARAMS_VOL_TARGET_v1 / IMPL_OVERLAY_VOL_TARGET_v1
- auditability：保存 vol_estimation_ref + exposure_change_ref

---

## 55. Part 7 審計附錄（組合/配置專屬，不可縮減）

每次組合/配置提案必須輸出並保存：
- `risk_decomposition_ref`（波動/回撤/因子/產業/集中度）
- `liquidity_feasibility_ref`（成交額/深度/點差/可交易性）
- `cost_estimation_ref`（稅費/滑價/換手率成本）
- `turnover_report_ref`（換手率與再平衡明細）
- `exposure_report_ref`（beta/產業/因子曝險）
- `policy_map_ref`（Regime→配置映射，版本化）
- `snapshot_refs + hash_manifest_ref`（可回放）

---

## 56. Only-Add 宣告（Part 7）

- 本 Part（Portfolio/Allocation/Overlay）條目一經交付：
  - 不可刪減
  - 不可覆寫
  - 只能新增新條目或新版本
- 本 Part 所有輸出必須維持：
  - 「提案/約束/解釋/審計」四件套齊全
- 任何時候 RISK_COMPLIANCE 否決：
  - 必須在 UI（L10）可視化呈現 veto_reason_code 與證據鏈

（STRATEGY_UNIVERSE｜最大完備版 v2025-12-19 · Part 7 完）

## Part 8｜策略條目全集（ChanLun 纏論結構體系 × 策略家族封裝）  

---

## 57. 本 Part 的「定位」是纏論體系封裝，不是把纏論降格成單一策略（不可縮減）

TAITS 的纏論（ChanLun，以下簡稱「纏」）在系統定位為：
- **結構與判斷體系（Structure & Judgment Framework）**
- 其輸出屬於 **L4–L6（結構/特徵/證據/Regime）** 的核心證據之一
- 本 Part 的策略條目，是把「纏的結構輸出」封裝為 **可治理、可審計、可回放、可白名單化** 的策略家族（Strategy Family Wrappers）

嚴禁（Hard Prohibitions）：
- 把纏論輸出當作「直接下單」或「必然方向」
- 將纏論訊號寫成黑箱口號（例如：看到背馳就買）
- 在缺少結構證據鏈（Structure Evidence Bundle）時輸出方向建議
- 任何跨層回寫：纏論策略不得繞過 L7（RISK_COMPLIANCE）直達 L11

---

## 58. 共同前置（ChanLun Strategy Wrappers Hard Gates）

### 58.1 Regime（纏論策略的允許狀態）
- 允許：
  - `RG_TREND_UP`, `RG_TREND_DOWN`, `RG_RANGE`（依策略型態）
- 條件式允許：
  - `RG_HIGH_VOL`（僅允許「降曝險/停手」或更高風控門檻）
- 禁止：
  - `RG_NEWS_SHOCK`（事件衝擊）→ 全部 BLOCK（除非是風險降低型 overlay，且需另條目）
  - `RG_LOW_LIQ` → 全部 BLOCK

### 58.2 必備 data_requirements（結構生成最低集合）
- `MD_EQUITY_EOD_DAILY`（至少 OHLCV）
- `REF_TRADING_CALENDAR`
- （若盤中纏）`MD_EQUITY_INTRADAY_QUOTES`
- `CA_MASTER`（除權息復權一致性）
- `REF_SYMBOL_MASTER`

### 58.3 ChanLun 結構證據（Structure Evidence Bundle｜SEB）最低欄位（不可縮減）
每次輸出纏論封裝策略提案，必須伴隨 SEB：
- `seb_id`（唯一）
- `seb_timeframe`（1d/60m…）
- `seb_structure_version`（結構引擎版本）
- `seb_inputs_snapshot_ref`（輸入行情/復權快照）
- `seb_outputs`（至少包含）：
  - `bi_segments`（筆）
  - `xd_segments`（線段）
  - `zs_structures`（中樞：級別/區間/狀態）
  - `trend_state`（結構趨勢狀態）
  - `divergence_marks`（背馳標記與方法）
  - `buy_sell_points`（買賣點候選：一買/二買/三買/對稱賣點）
- `seb_invalidation_rules`（失效條件）
- `seb_confidence`（結構可信度）
- `seb_conflict_notes`（與其他證據衝突說明）

### 58.4 Evidence completeness（纏論策略更嚴）
- Research / Backtest：EC ≥ 3（允許，但必須保存 SEB）
- Paper / Live：EC ≥ 4（必須），且必須含：
  - `seb_ref`（完整 SEB 可回放）
  - `liquidity_feasibility_ref`
  - `risk_veto_log`（若否決）

### 58.5 風險模板引用（只引用，不放寬）
- `RISK_TMPL_CHANLUN_CORE`
- `RISK_TMPL_TREND_START_GUARD`
- `RISK_TMPL_FALSE_BREAK_GUARD`
- `RISK_TMPL_LIQUIDITY_GUARD`
- `RISK_TMPL_GAP_SHOCK_GUARD`
- `RISK_TMPL_POSITION_SIZING_POLICY_REF`（若涉及分批，僅模板引用）

---

## 59. 策略條目索引（Whitelist｜Part 8）

- ChanLun Structure Confirmation（結構確認型）：
  - TAITS_STG_CL_001 ~ TAITS_STG_CL_010
- ChanLun Buy/Sell Point Wrappers（買賣點封裝型）：
  - TAITS_STG_CL_BSP_001 ~ TAITS_STG_CL_BSP_010
- ChanLun Multi-Timeframe Alignment（多級別共振/一致性）：
  - TAITS_STG_CL_MTF_001 ~ TAITS_STG_CL_MTF_008
- ChanLun Risk Overlay（纏論風險疊加，僅降風險）：
  - TAITS_STG_CL_OVR_001 ~ TAITS_STG_CL_OVR_006

---

# 60. Strategy Records｜ChanLun Structure Confirmation（結構確認型）

## 60.1 TAITS_STG_CL_001｜中樞型態確認（ZS State Confirmation）
- strategy_id：TAITS_STG_CL_001
- strategy_name_zh：中樞型態確認（中樞狀態→情境提案）
- family：ChanLun / Structure Confirmation
- paradigm：Structure-Driven (Evidence-first)
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_TREND_DOWN, RG_RANGE
  - min_regime_confidence：0.75
  - regime_conflict_behavior：DOWNGRADE（降級為「僅解釋/不給方向」）
- data_requirements：MD_EQUITY_EOD_DAILY, CA_MASTER, REF_TRADING_CALENDAR
- feature_requirements：FEAT_CL_ZS_STATE, FEAT_CL_TREND_STATE, FEAT_CL_STRUCTURE_CONFIDENCE
- structure_evidence_requirements：
  - seb_required：true
  - min_seb_confidence：0.70
  - required_seb_outputs：zs_structures, trend_state, invalidation_rules
- evidence_requirements：min_EC=3（Research）/ 4（Paper/Live）
- risk_profile：
  - risk_factors：false_structure, trend_start, gap, liquidity
  - max_exposure_rules_ref：RISK_TMPL_CHANLUN_CORE
  - additional_guards：RISK_TMPL_TREND_START_GUARD, RISK_TMPL_LIQUIDITY_GUARD
- constraints：
  - hard_blocks：
    - seb_ref 缺失（Paper/Live）→ BLOCK
    - structure_version 未註記 → BLOCK
  - soft_constraints：
    - 結構與其他證據衝突 → DOWNGRADE
- outputs_contract：
  - allowed_outputs：
    - proposal_type：STRUCTURE_CONTEXT_PROPOSAL
    - structure_context（中樞狀態、趨勢狀態、可能路徑）
    - invalidation_rules（失效條件）
    - risk_notes
    - time_validity
    - seb_ref
    - explanation_bundle_ref
  - forbidden_outputs：broker_order_payload / executable_qty_price / 直接「買/賣」指令句
- explainability：
  - 中樞級別、區間、是否擴張/延伸、對應失效條件
- lifecycle_state：REVIEW
- owner：ChanLun Structure Group
- versioning：1.0.0 / STRAT_PARAMS_CL_ZS_CONF_v1 / IMPL_CL_ZS_CONF_v1
- auditability：
  - 必備：seb_ref、inputs_snapshot_ref、structure_engine_version、explanation_bundle_ref、risk_veto_log（如有）

---

## 60.2 TAITS_STG_CL_002｜線段趨勢確認（XD Trend State）
- strategy_id：TAITS_STG_CL_002
- strategy_name_zh：線段趨勢確認（線段/中樞一致性）
- family：ChanLun / Structure Confirmation
- paradigm：Structure-Driven
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_TREND_DOWN; min_regime_confidence=0.75; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, CA_MASTER
- feature_requirements：FEAT_CL_XD_STATE, FEAT_CL_ZS_ALIGNMENT, FEAT_CL_STRUCTURE_CONFIDENCE
- structure_evidence_requirements：seb_required=true; min_seb_confidence=0.70; required_seb_outputs=xd_segments,zs_structures,trend_state
- evidence_requirements：min_EC=3/4
- risk_profile：risk_factors=false_trend, gap; max_exposure_rules_ref=RISK_TMPL_CHANLUN_CORE
- constraints：結構衝突嚴重 → RETURN（交回上層 Evidence Resolver）
- outputs_contract：同 CL_001（偏情境提案）
- explainability：線段方向、回撤結構、失效點
- lifecycle_state：REVIEW
- owner：ChanLun Structure Group
- versioning：1.0.0 / STRAT_PARAMS_CL_XD_TREND_v1 / IMPL_CL_XD_TREND_v1
- auditability：同上

---

# 61. Strategy Records｜ChanLun Buy/Sell Point Wrappers（買賣點封裝型）

## 61.1 TAITS_STG_CL_BSP_001｜一買封裝（First Buy Point Wrapper）
- strategy_id：TAITS_STG_CL_BSP_001
- strategy_name_zh：纏論一買封裝（僅提案：條件與失效）
- family：ChanLun / Buy-Sell Point Wrappers
- paradigm：Structure + Risk Gate
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_RANGE
  - min_regime_confidence：0.80
  - regime_conflict_behavior：BLOCK（趨勢向下不做一買提案）
- data_requirements：MD_EQUITY_EOD_DAILY, CA_MASTER, REF_TRADING_CALENDAR
- feature_requirements：FEAT_CL_BSP_1, FEAT_CL_DIVERGENCE, FEAT_ATR_N, FEAT_LIQUIDITY_SCORE
- structure_evidence_requirements：
  - seb_required：true
  - min_seb_confidence：0.75
  - required_seb_outputs：buy_sell_points, divergence_marks, zs_structures, invalidation_rules
- evidence_requirements：min_EC=4（Paper/Live 強制）
- risk_profile：
  - risk_factors：false_bsp, trend_start_fail, gap, liquidity
  - max_exposure_rules_ref：RISK_TMPL_CHANLUN_CORE
  - additional_guards：RISK_TMPL_FALSE_BREAK_GUARD, RISK_TMPL_GAP_SHOCK_GUARD, RISK_TMPL_LIQUIDITY_GUARD
- constraints：
  - hard_blocks：
    - 無背馳證據鏈（divergence_marks 缺失）→ BLOCK
    - invalidation_rules 缺失 → BLOCK
  - soft_constraints：
    - 與其他 Evidence 強烈衝突 → DOWNGRADE（只解釋不提案）
- outputs_contract：
  - allowed_outputs：
    - proposal_type：BSP_PROPOSAL
    - bsp_type：BSP1
    - entry_conditions（以條件描述，不含可執行價格/口數）
    - invalidation_rules
    - risk_notes
    - time_validity
    - seb_ref
    - explanation_bundle_ref
  - forbidden_outputs：任何可執行委託與「保證勝率」敘述
- explainability：
  - 一買判定依據、背馳方法、失效點、風險（假一買）
- lifecycle_state：REVIEW
- owner：ChanLun Strategy Wrapper Group
- versioning：1.0.0 / STRAT_PARAMS_CL_BSP1_v1 / IMPL_CL_BSP1_v1
- auditability：必須保存 bsp_calc_ref（可重算）與 seb_ref

---

## 61.2 TAITS_STG_CL_BSP_002｜二買封裝（Second Buy Point Wrapper）
- strategy_id：TAITS_STG_CL_BSP_002
- strategy_name_zh：纏論二買封裝（回踩確認）
- family：ChanLun / Buy-Sell Point Wrappers
- paradigm：Structure + Confirmation
- market_scope：TWSE, TPEX
- instrument_types：EQUITY
- timeframes：1d
- regime_requirements：allowed_regimes=RG_TREND_UP,RG_RANGE; min_regime_confidence=0.80; conflict=DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, CA_MASTER
- feature_requirements：FEAT_CL_BSP_2, FEAT_CL_ZS_STATE, FEAT_LIQUIDITY_SCORE
- structure_evidence_requirements：seb_required=true; min_seb_confidence=0.75; required_seb_outputs=buy_sell_points,zs_structures,invalidation_rules
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：risk_factors=false_break, late_entry, gap; max_exposure_rules_ref=RISK_TMPL_CHANLUN_CORE
- constraints：若回踩破壞結構失效條件 → RETURN
- outputs_contract：同 BSP_001（bsp_type=BSP2）
- explainability：回踩位置、結構保持條件
- lifecycle_state：REVIEW
- owner：ChanLun Strategy Wrapper Group
- versioning：1.0.0 / STRAT_PARAMS_CL_BSP2_v1 / IMPL_CL_BSP2_v1
- auditability：同上

---

# 62. Strategy Records｜ChanLun Multi-Timeframe Alignment（多級別共振）

## 62.1 TAITS_STG_CL_MTF_001｜日線×週線共振（MTF Alignment）
- strategy_id：TAITS_STG_CL_MTF_001
- strategy_name_zh：纏論多級別共振（日×週一致性）
- family：ChanLun / Multi-Timeframe
- paradigm：Structure Aggregation
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d + 1w（多級別）
- regime_requirements：
  - allowed_regimes：RG_TREND_UP, RG_RANGE
  - min_regime_confidence：0.80
  - regime_conflict_behavior：DOWNGRADE
- data_requirements：MD_EQUITY_EOD_DAILY, CA_MASTER, REF_TRADING_CALENDAR
- feature_requirements：FEAT_CL_MTF_ALIGNMENT_SCORE, FEAT_CL_STRUCTURE_CONFIDENCE
- structure_evidence_requirements：
  - seb_required：true
  - seb_multi_tf_required：true
  - min_seb_confidence：0.75
  - required_seb_outputs：zs_structures, trend_state, buy_sell_points, invalidation_rules
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：
  - risk_factors：tf_conflict, lag, liquidity
  - max_exposure_rules_ref：RISK_TMPL_CHANLUN_CORE
- constraints：
  - 多級別衝突（alignment_score 低於門檻）→ RETURN（交回 Evidence Resolver）
- outputs_contract：
  - allowed_outputs：mtf_context_proposal（情境提案）, constraints, invalidation_rules, seb_refs（多級別）, explanation_bundle_ref
  - forbidden_outputs：可執行委託
- explainability：各級別結構摘要與衝突說明
- lifecycle_state：REVIEW
- owner：ChanLun MTF Group
- versioning：1.0.0 / STRAT_PARAMS_CL_MTF_v1 / IMPL_CL_MTF_v1
- auditability：必須保存多級別 seb_refs 與 alignment_calc_ref

---

# 63. Strategy Records｜ChanLun Risk Overlay（僅降風險）

## 63.1 TAITS_STG_CL_OVR_001｜結構破壞風險降曝險（Structure Breakdown De-Risk）
- strategy_id：TAITS_STG_CL_OVR_001
- strategy_name_zh：結構破壞降曝險（纏論風控疊加）
- family：ChanLun / Risk Overlay
- paradigm：Risk Control Policy（Derisk-only）
- market_scope：TWSE, TPEX
- instrument_types：EQUITY, ETF
- timeframes：1d, 60m
- regime_requirements：
  - allowed_regimes：RG_HIGH_VOL, RG_RISK_OFF, RG_NEWS_SHOCK（僅允許降風險）
  - min_regime_confidence：0.70
  - regime_conflict_behavior：ALLOW_ONLY_DERISK
- data_requirements：MD_EQUITY_EOD_DAILY, MD_EQUITY_INTRADAY_QUOTES, CA_MASTER
- feature_requirements：FEAT_CL_INVALIDATION_HIT, FEAT_CL_STRUCTURE_CONFIDENCE, FEAT_LIQUIDITY_SCORE
- structure_evidence_requirements：seb_required=true; min_seb_confidence=0.70; required_seb_outputs=invalidation_rules, trend_state, zs_structures
- evidence_requirements：min_EC=4（Paper/Live）
- risk_profile：
  - risk_factors：panic_sell, liquidity, whipsaw
  - max_exposure_rules_ref：RISK_TMPL_DRAWDOWN_GUARD（引用）+ RISK_TMPL_CHANLUN_CORE（引用）
- constraints：
  - allowed_actions：reduce_exposure / tighten_limits / recommend_kill_switch（僅建議）
  - forbidden_actions：任何增加曝險、任何方向性提案
- outputs_contract：
  - allowed_outputs：overlay_recommendation, invalidation_context, new_risk_limits_template_ref, time_validity, seb_ref, explanation_bundle_ref
  - forbidden_outputs：任何可執行委託與加碼建議
- explainability：何種結構破壞、觸發點、為何需要降風險
- lifecycle_state：APPROVED
- owner：Risk & ChanLun Overlay Group
- versioning：1.0.0 / STRAT_PARAMS_CL_DERISK_v1 / IMPL_CL_DERISK_v1
- auditability：保存 before/after exposure report + seb_ref + veto logs

---

## 64. Part 8 審計附錄（纏論封裝專屬，不可縮減）

每次運行必須額外保存：
- `seb_ref`（完整 SEB，含結構引擎版本與快照）
- `structure_engine_version` + `structure_ruleset_version`
- `bsp_calc_ref`（若輸出買賣點封裝）
- `mtf_alignment_calc_ref`（若輸出多級別共振）
- `conflict_resolution_ref`（若 Evidence Resolver 有處理衝突）
- `risk_veto_log`（如被否決，必須完整保留）

UI（L10）必須能呈現：
- 結構摘要（中樞/線段/背馳/買賣點）
- 失效條件（invalidation_rules）
- 與風控裁決（veto_reason_code）

---

## 65. Only-Add 宣告（Part 8）

- 纏論封裝策略一經交付：
  - 不可刪減
  - 不可覆寫
  - 只能新增新條目或新版本
- 纏論輸出永遠不得「直達下單」：
  - 必須經 L7（RISK_COMPLIANCE）+ L10（UI 人類主權）+ L11（Execution Control）流程
- 若結構證據不足：
  - 只能輸出解釋與缺口，禁止方向建議

（STRATEGY_UNIVERSE｜最大完備版 v2025-12-19 · Part 8 完）
