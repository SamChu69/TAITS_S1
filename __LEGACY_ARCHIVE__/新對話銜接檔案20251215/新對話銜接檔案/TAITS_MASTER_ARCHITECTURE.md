# TAITS_MASTER_ARCHITECTURE.md
# TAITS — Taiwan Alpha Intelligence Trading System（台灣阿爾法智能交易系統）
版本：Master Architecture（Full, Unified, Non-Phase-Limited）
用途：GitHub 主體規格（所有後續 S1/S2/S3 只能裁剪，不得違背）
最後整合依據：
- TAITS_Architecture_and_Flow.md（分層架構 + 全流程）:contentReference[oaicite:0]{index=0}
- TAITS_S1_主開發說明文件.md（Plugin/Agents/策略體系/介面要求）:contentReference[oaicite:1]{index=1}
- TAITS_S1_補充資料20251210.md（55 資料源、102 策略補強、Regime/Fusion 細節、TAIFEX 強化）:contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}
- TAITS_S1_補充.md（工程/回測/交易架構參考來源）:contentReference[oaicite:4]{index=4}

---

## 0. 你要的「母體版」定義（重要）
TAITS Master Architecture 是「完整母體」，包含：
- 台股現貨（TWSE/TPEX/MOPS/集保等）
- 台灣期貨/選擇權（TAIFEX：台指期、選擇權、OI、大額交易人、P/C、IV/SKEW…）
- 多資料源 + fallback（可靠性）
- 指標/因子（含纏論/型態/籌碼/宏觀/衍生品因子）
- 285+ 策略宇宙（主策略庫）＋ 102 策略補強（補充庫）
- 多智能體（Agents）＋ Regime Engine ＋ Fusion Engine
- 風控/資金/組合管理
- 回測/模擬/實盤（券商介接）
- 報告/稽核/監控/UI

> 注意：開發階段（S1/S2/S3）只是「交付順序」，不是「系統內容」邊界。

---

## 1. 全域分層架構（Master Layers）
本架構採「分層 + Orchestrator 統一調度」的交易系統設計：:contentReference[oaicite:5]{index=5}

```text
Layer 0 ─ Infra Layer（基礎設施）
Layer 1 ─ Data Layer（資料層）
Layer 2 ─ Feature/Indicator/Factor Layer（特徵/指標/因子）
Layer 3 ─ Strategy Layer（策略層：285+）
Layer 4 ─ Agents Layer（多智能體：10+）
Layer 5 ─ Regime + Fusion + Decision Layer（市場狀態+融合決策）
Layer 6 ─ Portfolio + Risk Layer（資金、部位、風控）
Layer 7 ─ Execution Layer（模擬/券商下單/交易模式）
Layer 8 ─ UI + Reporting + Monitoring + Audit（可視化、報告、監控、稽核）

              ↑
     Orchestrator / Scheduler 統一調度
````

---

## 2. GitHub 專案總目錄（建議落盤結構）

> 你目前 repo 實作可先用精簡版；此處是 Master 版「最終目錄」，可逐步補齊。

```text
TAITS/
│── main.py
│── config.yaml
│
├── config/
│   ├── settings.py
│   ├── logging.yaml
│   └── secrets.example.yaml
│
├── data_sources/
│   ├── base_loader.py
│   ├── yahoo_loader.py
│   ├── twse_loader.py
│   ├── finmind_loader.py
│   ├── macro_loader.py
│   ├── taifex_loader.py
│   ├── news_loader.py
│   ├── sentiment_loader.py
│   ├── fallback_manager.py
│   └── cache_manager.py
│
├── engine/
│   ├── orchestrator.py
│   ├── data_validator.py
│   ├── indicator_manager.py
│   ├── strategy_manager.py
│   ├── agent_manager.py
│   ├── market_regime_engine.py
│   ├── fusion_engine.py
│   ├── signal_aggregator.py
│   ├── portfolio_manager.py
│   ├── risk_engine.py
│   ├── report_formatter.py
│   └── report_md_formatter.py
│
├── indicators/
│   ├── base_indicator.py
│   ├── trend/
│   ├── momentum/
│   ├── volatility/
│   ├── volume/
│   ├── candle/
│   ├── chip/
│   ├── derivatives/
│   ├── macro/
│   ├── chanlun/
│   └── ai/
│
├── strategies/
│   ├── base_strategy.py
│   ├── registry.py
│   ├── trend/
│   ├── breakout/
│   ├── reversal/
│   ├── chip/
│   ├── fundamental/
│   ├── derivatives/
│   ├── sector/
│   ├── news/
│   ├── behavior/
│   ├── chan/
│   └── ai/
│
├── agents/
│   ├── base_agent.py
│   ├── technical_agent.py
│   ├── chip_agent.py
│   ├── fundamental_agent.py
│   ├── news_agent.py
│   ├── sentiment_agent.py
│   ├── macro_agent.py
│   ├── derivatives_agent.py
│   ├── event_agent.py
│   ├── ai_model_agent.py
│   ├── chan_agent.py
│   ├── pattern_agent.py
│   ├── risk_agent.py
│   └── summary_agent.py
│
├── models/
│   ├── slow_brain/
│   ├── fast_brain/
│   └── providers/
│
├── backtest/
│   ├── backtester.py
│   ├── event_bus.py
│   ├── slippage_model.py
│   ├── fee_model.py
│   ├── survivorship_filter.py
│   ├── position_manager.py
│   └── report.py
│
├── paper_trading/
│   ├── simulator.py
│   └── matching_engine.py
│
├── trading/
│   ├── base_broker.py
│   ├── broker_fubon.py
│   ├── order_manager.py
│   ├── risk_manager.py
│   └── execution_router.py
│
├── ui/
│   ├── dashboard.py
│   ├── charts.py
│   └── components/
│
├── monitoring/
│   ├── logger.py
│   ├── metrics.py
│   ├── alerts.py
│   └── audit_trail.py
│
├── docs/
│   ├── TAITS_MASTER_ARCHITECTURE.md   ← 本文件（母體）
│   ├── datasources/
│   ├── strategies/
│   ├── agents/
│   ├── risk/
│   └── ui/
│
└── tests/
    ├── test_engine_flow.py
    ├── test_indicators.py
    ├── test_strategies.py
    ├── test_agents.py
    ├── test_backtest.py
    └── test_trading.py
```

---

## 3. Layer 0 — Infra Layer（基礎設施層）

目標：把「一堆 Python 檔」升級成「可長期運行的交易平台」。

### 3.1 必備元件（Master）

* TimescaleDB：歷史行情/籌碼/新聞向量/策略訊號存放（回測與研究）
* Redis：盤中快取（Tick、Fast Brain、Slow Brain、熔斷標記）
* EventBus（Async）：行情事件/預測事件/風控事件分發給策略層、風控層、UI 等
* Docker：封裝環境避免依賴衝突
* Logger + Audit Trail：訊號、下單、熔斷皆留痕以利稽核

### 3.2 運行模式（Master）

* Research：離線研究、資料清洗、因子製作
* Backtest：事件驅動回測（Lean-like）
* Paper：模擬撮合（近似盤中）
* Live：券商 API（富邦）實盤

---

## 4. Layer 1 — Data Layer（資料層：全資料宇宙）

TAITS 以「官方 / 開放 / 合法 / 可持續」為優先，並建立完整資料護城河。

### 4.1 資料來源 Universe（55 項級別，Master 清單範式）

補充資料明確定義「資料來源完整清單（55 項）」與其用途歸位。

#### 4.1.1 官方資料源（TWSE / TPEX / MOPS / 集保）

示例（補充文件列舉）：TWSE、TPEX、MIS 即時行情、集保股權分散、法人買賣超、當沖統計、MOPS 財報/月營收/重訊、央行匯率、data.gov.tw 等。

#### 4.1.2 台灣期交所（TAIFEX）

補充文件明確把 TAIFEX 列為官方安全來源之一。

#### 4.1.3 宏觀資料（API / 自動化來源）

宏觀資料來源（示例）：FRED、OECD、ISM、IMF、Yahoo Finance、Investing.com、主計總處、中經院、TrendForce、SEMI、SCFI、PTT、Dcard 等。

> 宏觀在 TAITS 的定位：宏觀不是直接下單策略，而是「決定策略何時啟用/停用」的上層約束。

### 4.2 Data Flow（資料流）

```text
外部資料源（API / 抓取 / WebSocket）
    ↓
清洗 / 對齊 / 缺值處理 / 交易日曆對齊
    ↓
寫入 DB（歷史） + Cache（盤中）
    ↓
提供給：Indicators / Strategies / Agents / Regime / Risk / UI
```

---

## 5. Layer 2 — Feature / Indicator / Factor（指標/因子層）

指標層是「可插拔（plugin）」設計：

### 5.1 指標分類（Master）

* Trend：SMA/EMA/GMMA、趨勢斜率、均線乖離
* Momentum：RSI、MACD、動能、ROC
* Volatility：ATR、歷史波動、布林帶寬
* Volume：OBV、量能 Z-score、成交額因子
* Candle/Pattern：K 線型態、缺口、吞沒、Doji
* Chip：三大法人、融資融券、借券、集保分布、分點（若合法取得）
* Derivatives：期現價差、OI 變化、十大交易人、P/C、IV/SKEW
* Macro：匯率、利率、國際指數（SOX/美股/原物料/航運）
* Chanlun（纏論）：分型、筆、線段、中樞、背馳（作為結構因子）
* AI：Fast/Slow brain 輸出轉換為可加權 signal

### 5.2 指標輸出原則

* 以 DataFrame 欄位新增為主（避免破壞原資料）
* 必須可追溯來源與計算參數（Audit）
* 盤中與盤後版本需一致（同定義、不同資料頻率）

---

## 6. Layer 3 — Strategy Layer（策略層：285+ Universe）

策略系統為 plugin 架構：每個策略獨立、互不依賴、繼承 base_strategy、由 manager 自動發現。

### 6.1 策略輸出統一格式（Master）

```python
{
  "name": "StrategyName",
  "signal": "BUY" / "SELL" / "HOLD",
  "confidence": 0.0 ~ 1.0,
  "reason": "中文說明",
  "tags": ["trend", "chip", "derivatives", "chan", ...],
  "weight_hint": 0.0 ~ 2.0
}
```

### 6.2 策略 Universe（主庫 + 補強庫）

* 主策略庫：285+（V3.1/策略全集）
* 補充策略庫：102（補充資料 20251210）
  補充中包含「衍生品策略」「AI 策略」等分類示例：

> 原則：策略數量不是重點；重點是 **可註冊、可禁用、可加權、可回測、可稽核**。

---

## 7. Layer 4 — Agents Layer（多智能體層：10+）

Agents 定位：每個 Agent 專注一種分析邏輯，避免重疊，並輸出統一格式。

### 7.1 Agents 清單（Master）

主規格明確列出多 Agent 範圍：technical、chip、sentiment、news、fundamental、macro、pattern、chan、ai、risk。

### 7.2 Agent 輸出統一格式（Master）

```python
{
  "name": "AgentName",
  "bias": "BULL" / "BEAR" / "NEUTRAL",
  "confidence": 0.0 ~ 1.0,
  "comment": "中文摘要（可被報告層直接使用）",
  "evidence": {
    "key_features": [...],
    "key_rules": [...],
    "data_coverage": {...}
  }
}
```

---

## 8. Layer 5 — Market Regime Engine + Fusion Engine（核心決策層）

補充資料明確定義：Regime 會影響 Fusion、風控、倉位、AI 模型選擇。

### 8.1 Regime 類型（Master）

補充資料列出 Regime 類型，並新增「衍生品主導」狀態：DERIVATIVES_DOMINATED。

```text
TREND / RANGE / CHIP_DOMINATED / VOLATILE / PANIC / NORMAL / DERIVATIVES_DOMINATED
```

### 8.2 Regime 特徵（TAIFEX 強化）

補充明確要求加入 TAIFEX 特徵（例：期現價差、外資 OI、小台散戶、IV/SKEW、P/C Ratio）。

### 8.3 Fusion Engine（策略融合）

Fusion 的任務：把「策略 + Agents + Regime」融合成單一決策；加權因子包含類型權重、Regime 權重、策略歷史表現、Agent 偏向、策略自帶權重等。

### 8.4 Fusion 輸出（Master）

補充定義輸出欄位應包含 final_signal、confidence、regime、contributing_strategies、summary_comment 等：

---

## 9. Layer 6 — Portfolio + Risk（資金/部位/風控）

目標：把「看起來會賺」變成「活得久」。

### 9.1 Risk Engine（Master）

* 合規檢查（交易時間、漲跌幅、最小跳動、零股限制、券商拒單原因）
* 熔斷（連續虧損、波動爆表、風險事件）
* 最大曝險（單檔/產業/總曝險）
* 倉位上限（Regime 動態調整）
* 停損停利（固定/ATR/結構化）

### 9.2 Portfolio Manager（Master）

* 資金分配（策略/Agent 置信度加權）
* 部位管理（分批、加減碼）
* 交易成本模型（手續費/交易稅/滑價）
* 生存者偏差（退市/成分變動）— 交由 backtest 層落地

---

## 10. Layer 7 — Execution（模擬/實盤執行層）

### 10.1 Execution Router（Master）

輸入：FusionDecision + RiskDecision + PositionPlan
輸出：BrokerOrder（下單/改單/刪單）+ OrderState

### 10.2 三模式（Master）

* Backtest（事件驅動）
* Paper（模擬撮合）
* Live（富邦 API）

---

## 11. Layer 8 — UI / Reporting / Monitoring / Audit

### 11.1 Reporting（Master）

* JSON：機器可讀（供稽核/回放）
* TXT：人類快速掃描
* Markdown：正式報告（可進 GitHub 留存）

### 11.2 Monitoring（Master）

* metrics：策略命中率、回撤、暴露、延遲、資料覆蓋率
* alerts：熔斷、資料中斷、券商拒單、異常波動
* audit_trail：每次決策的「證據鏈」

---

## 12. TAITS 總流程（Master End-to-End）

主規格定義核心流程骨架（Data → Indicators → Strategies → Agents → Aggregation → Orchestrator → Backtest/Sandbox/Live）。

### 12.1 日級/盤後（Batch）流程

```text
(1) 拉取歷史資料（多來源 fallback）
(2) 清洗對齊 + 寫入 DB
(3) 計算指標/因子
(4) 跑策略宇宙（285+）
(5) 跑 Agents（10+）
(6) Regime 判斷
(7) Fusion 融合出決策
(8) 生成報告（JSON/TXT/MD）+ 指標圖表（可選）
(9) 若為回測：送入 Backtest Engine
```

### 12.2 盤中（Event-driven）流程

```text
(1) Tick/Bar 事件進入 EventBus
(2) 更新快取（Redis）
(3) Fast Brain / 快速指標更新（可選）
(4) 觸發策略子集（低延遲策略）
(5) 更新 Agents 關鍵結論（只更新必要的）
(6) Regime 若變化 → 重估權重
(7) Fusion 產生最新決策
(8) Risk Gate（合規/曝險/熔斷/零股限制）
(9) Execution Router → 券商 API（或 Paper）
(10) 回報/成交/狀態 → Audit + UI
```

---

## 13. 關鍵介面與資料結構（Master Contract）

補充資料要求定義 StrategyResult / AgentResult / MarketRegimeInfo / FusionDecision 等 TypedDict 作為模組交換契約。

### 13.1 StrategyResult（範式）

```python
StrategyResult = {
  "name": str,
  "signal": "BUY|SELL|HOLD",
  "confidence": float,
  "reason": str,
  "tags": list[str],
  "weight_hint": float,
  "meta": dict
}
```

### 13.2 AgentResult（範式）

```python
AgentResult = {
  "name": str,
  "bias": "BULL|BEAR|NEUTRAL",
  "confidence": float,
  "comment": str,
  "evidence": dict
}
```

### 13.3 MarketRegimeInfo（範式）

```python
MarketRegimeInfo = {
  "regime": str,
  "confidence": float,
  "features": dict,
  "why": str
}
```

### 13.4 FusionDecision（範式）

```python
FusionDecision = {
  "final_bias": "BULL|BEAR|NEUTRAL",
  "confidence": float,
  "reason": str,
  "regime": str,
  "contributing_strategies": list[dict],
  "contributing_agents": list[dict],
  "risk_flags": list[str]
}
```

---

## 14. 四大優化（你要求必須納入母體）

> 這四項是你最早要求我「世界級」必須做到的系統性優化，全部納入 TAITS Master 主幹。

1. 多資料源 + 多層 fallback（可靠性）
2. 嚴格模組化 + plugin 化（可維護、可擴展）
3. 合規與真實交易可行性（台股制度、券商拒單、風控）
4. Hybrid：AI + 傳統策略分層可替換（模型快速演進不影響系統）

（對應補充與主規格的整體精神：模組化/自動化/多智能體/可加權統一輸出）

---

## 15. 文件落地建議（你現在要存 GitHub 的最低集合）

> 你說「檔多沒關係，但要清楚且不遺漏」，這裡先給母體文件的落地建議。

必存（第一優先）：

* docs/TAITS_MASTER_ARCHITECTURE.md（本文件）
* docs/TAITS_Architecture_and_Flow.md（現有）
* docs/TAITS_S1_主開發說明文件.md（現有）
* docs/TAITS_S1_補充資料20251210.md（現有）
* docs/V3.1_285_Strategies.md（現有）

次優先（後續再逐檔補齊）：

* docs/datasources/TAITS_DataSources_Universe.md
* docs/strategies/TAITS_Strategy_Universe.md
* docs/agents/TAITS_Agents_Spec.md
* docs/risk/TAITS_Risk_and_Compliance.md
* docs/ui/TAITS_UI_Spec.md

---

（EOF）

---

# 【TAITS 主架構差異補齊（D01–D12）｜母體級正式規格】
## 版本：v2025-12-16
## 性質：Only-Add（追加，不覆蓋既有內容）

本章節用於補齊「原專案中未顯性化、但實際已被 TAITS 使用或你已明確要求的核心能力」。
本章節不取代、不否定任何既有段落，而是作為 **母體級補齊與差異說明**。

---

## D01｜證據包中樞（Evidence Bundler）【對應層級：L5】

### 定位
Evidence Bundler 是 TAITS 的 **解釋與審計中樞**，負責把所有判斷依據封裝成可引用、可回放的證據包。

### 為什麼需要
原架構中存在「策略有結果，但理由分散在各模組」的問題，導致：
- 新對話無法重建判斷依據
- 風控/否決難以追溯
- UI 只能顯示結果，無法顯示原因

### 固定輸出格式（缺一不可，缺則標示缺失）
- snapshot_ref
- trigger_rules[]
- technical_summary
- event_flags[]
- narrative_evidence[]
- heat_score
- rumor_risk_tags[]
- wyckoff_bundle
- bodick_bundle
- cross_market_flags
- cross_market_risk_tags[]

### 使用範圍
Evidence Bundle 為以下層級的**唯一證據來源**：
- L6 Market Regime
- L7 Risk / Compliance
- L8 Strategy Engine
- L9 Governance Gate
- L10 UI / Report

---

## D02｜威科夫（Wyckoff）工程化規格【L4 / L5 / L8 / L10】

### 定位
威科夫在 TAITS 中 **不是策略本身**，而是「主力行為與階段判斷的證據來源」。

### wyckoff_bundle 固定欄位
- wyckoff_stage（吸籌 / 推升 / 派發 / 下跌）
- wyckoff_events[]
- wyckoff_volume_price_alignment
- wyckoff_confidence（0–100）
- wyckoff_risk_tags[]
- wyckoff_notes（中文說明）

### 使用限制
- 不得直接觸發下單
- 僅可作為 Filter / Weight Adjuster / Exit Priority / Risk Tag

---

## D03｜鮑迪克纏論工程化規格【L4 / L5 / L8 / L10】

### 定位
鮑迪克纏論用於 **提高勝率與結構確認**，負責判斷：
- 結構段落位置
- 背離真偽
- 多級別一致性

### bodick_bundle 固定欄位
- bodick_structure_state（推進 / 回撤 / 整理 / 轉折）
- bodick_divergence_type
- bodick_segment_strength（0–100）
- bodick_consistency_score（0–100）
- bodick_resonance
- bodick_risk_tags[]
- bodick_notes（中文說明）

---

## D04｜Observe-only 跨市場資料硬規格【L1 / L4 / L6 / L7 / L8 / L9 / L10】

### 覆蓋資料
- 期貨（Futures）
- 選擇權（Options）
- 融資融券（Credit）

### 硬規則（母體級）
- 僅可影響股票策略
- 禁止對其商品下單
- 僅能作為：
  - Regime Evidence
  - Risk Override
  - Weight Adjuster
  - Exit Priority Modifier

### 固定輸出
- futures_regime_flags[]
- options_pressure_flags[]
- credit_heat_flags[]
- cross_market_risk_tags[]
- weight_multiplier
- forbidden_strategy_list[]

---

## D05｜消息 / 社群 / 題材輪動顯性化【L1 / L4 / L5 / L8 / L10】

### 必備輸出欄位
- event_flags[]
- narrative_evidence[]
- heat_score（0–100）
- diffusion_chain[]
- rumor_risk_tags[]

### 核心原則
TAITS **不得因「難以量化」而忽略題材與消息**，
只能顯示證據強弱與風險，最終決定權在你。

---

## D06｜官方 OpenAPI 來源白名單【L1 / L3】

### 必列官方來源
- TWSE OpenAPI：https://openapi.twse.com.tw/
- TPEx OpenAPI：https://www.tpex.org.tw/openapi/
- TAIFEX OpenAPI：https://openapi.taifex.com.tw
- MOPS：https://mopsov.twse.com.tw/mops/web/index

### 要求
- 每筆資料必須可回查 source_ref + captured_at + batch_id
- Snapshot Manifest 必須列出使用的官方來源

---

## D07｜Snapshot / Replay 強制制度【L3 → 全層】

### 硬規則
凡影響以下行為者，必須綁定 snapshot_ref：
- Regime 判定
- Risk 否決
- Strategy 啟用 / 停用
- Gate 決策

無 snapshot_ref → 判定無效。

---

## D08｜Regime-first 證據引用規格【L6】

### 固定輸出
- regime_state
- regime_confidence
- regime_snapshot_ref
- regime_evidence_refs[]

---

## D09｜Risk / Compliance 否決審計包【L7】

### Risk Audit Bundle
- risk_trigger_rules[]
- risk_snapshot_ref
- risk_evidence_refs[]
- blocked_actions[]
- weight_adjustments
- exit_priority_changes

---

## D10｜Universe 三池硬規則【L8】

### 三池必須同時存在
1. 穩定池（權值 / 高流動）
2. 輪動池（題材主線 / 次主線）
3. 爆發池（中小型 / 供應鏈尾端）

### 禁止行為
- 任何條件不得直接刪除爆發池
- 只能降權或標註風險

---

## D11｜治理層 Gate 與修改授權模型【L9】

### 修改等級
- Append：允許
- Modify：需你授權
- Refactor：需你主動要求

### Gate 輸出
- permission_state
- gate_reason
- gate_snapshot_ref

---

## D12｜UI / 報告必須顯示「為什麼」【L10】

### UI 強制顯示
- Evidence Bundle 全欄位
- Regime / Risk / Gate 的證據引用
- snapshot_ref

---

# 【End of TAITS_MASTER_ARCHITECTURE 差異補齊】

