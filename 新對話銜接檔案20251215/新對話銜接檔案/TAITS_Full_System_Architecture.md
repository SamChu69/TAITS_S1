# TAITS_Full_System_Architecture.md
（TAITS 全系統總架構｜分層設計｜模組責任｜可落地藍圖）

> 文件定位：全系統藍圖（Blueprint）
> 目的：把 TAITS 拆成可維護、可演進、可審計的分層模組；並明確禁止事項，避免「越做越混」。

---

## 0. 名詞中譯

- Layer：層
- Module：模組
- Data Flow：資料流
- Decision Flow：決策流
- Event Flow：事件流
- Gate：閘門（可阻擋）
- Observe-only：僅觀察（不可送單）

---

## 1. TAITS 分層總覽（母體層 00–12 的工程映射）

TAITS 以「母體（規格）→ 實作（工程）」兩大域組成：

### 1.1 母體域（System Mother：00–12）
- 定義：原則、資料、指標、Regime、策略宇宙、治理、風控、回測、驗證、使用流程

### 1.2 實作域（Implementation：13+）
- 定義：資料匯流排、即時服務、券商適配、下單執行、監控告警、部署、運維、回放工具

> 本文件描述「整體架構」；細節流程見 TAITS_Architecture_and_Flow.md。

---

## 2. 十層架構（嚴格不縮水：你原本的 10 層保留）

> 注意：這是「系統層級」，不是「策略層級」。

### L1｜Data Source Layer（資料來源層）
- TWSE/TPEX/MOPS/TAIFEX 官方、公開資訊、新聞社群、宏觀資料、替代數據
- 輸出：原始資料（Raw Data）

### L2｜Data Ingestion & Normalization（資料接入與標準化層）
- 清洗、對齊、時間戳、欄位標準、缺值策略
- 輸出：標準化資料（Normalized Data）

### L3｜Storage & Snapshot（儲存與快照層）
- 時序資料庫/物件儲存/快照（Snapshot）與版本鎖定
- 輸出：可回放資料快照（Replayable Snapshot）

### L4｜Feature Factory（指標/特徵工廠層）
- 03 文件定義的指標與特徵（含 GMMA/CBL/威科夫/鮑迪克）
- 輸出：Feature Vector（特徵向量）

### L5｜Regime Engine（市場狀態判定層）
- 11 文件規格：輸出 R1–R10 + confidence + evidence
- 輸出：RegimeResult（盤勢結果）

### L6｜Strategy Signal Engine（策略訊號層）
- 05 策略宇宙：334 策略訊號判斷（注意：不是下單）
- 輸出：StrategySignals（策略訊號集合）

### L7｜Fusion & Weighting（融合與權重層）
- 多策略、多代理證據融合
- 產出：建議策略組合與權重（Candidate Portfolio）

### L8｜Governance Permission Gate（策略治理閘門）
- 06 文件規格：允許/降級/人工/禁止
- 產出：GovernanceDecision（放行結果）

### L9｜Risk & Compliance Gate + Kill Switch（風控合規閘門）
- 07 文件規格：PASS/SOFT_BLOCK/HARD_BLOCK/KILL
- 產出：RiskDecision（可否執行）

### L10｜Execution & Operations（執行與運維層）
- 13+：Execution Planner、Broker Adapter、Order Lifecycle、監控告警、回放
- 輸出：訂單狀態/成交回報/審計紀錄

---

## 3. 模組責任邊界（避免互相污染）

### 3.1 Strategy（策略）模組禁止事項
- ❌ 不可直接下單
- ❌ 不可寫死券商 API
- ❌ 不可繞過 Gate

### 3.2 Regime 模組禁止事項
- ❌ 不可被策略覆蓋（只能被更高層 Risk 覆蓋）
- ❌ 不可依賴單一指標或單一資料源

### 3.3 Risk 模組禁止事項
- ❌ 不可被任何下游覆蓋（Risk 是最高否決）

---

## 4. 核心資料物件（全系統通用）

### 4.1 Market Snapshot（市場快照）
- 由資料層產生，作為所有判定的「同一份事實」
- 必備：timestamp、data_quality、index、breadth、event_flags、derivatives_observation、credit_observation

### 4.2 Evidence Bundle（證據包）
- 每個 Regime、每次治理決策、每次風控決策，都必須帶 evidence
- 目的：可審計、可回放、可質疑

### 4.3 Version Manifest（版本清單）
- system_version、module_versions、data_snapshot_id、run_id
- 沒有 Manifest 的結果不可採信

---

## 5. 實盤與回測的一致性（同一套邏輯）

- 回測與實盤必須使用同一套：
  - Feature 定義
  - Regime 判定
  - Governance / Risk Gate
- 差異只允許出現在：
  - 資料頻率（日/分/秒）
  - 延遲處理策略
  - 交易成本模型

---

## 6. 與「觀察型產品」的定位（期貨/選擇權/融資融券）

在 TAITS 中，這些不是交易標的，而是：

- Regime Evidence（狀態證據）
- Cross-Market Filter（跨市場濾網）
- Weight Adjuster（權重調整器）
- Risk Override（風險覆蓋條件）

> 任何實作若把它們變成「直接下單策略」，視為違反憲章。

---

## 7. 檔案交叉引用（你要找的都在這）

- 架構流程細節：TAITS_Architecture_and_Flow.md
- 資料來源全集：TAITS_DataSources_Universe.md
- 策略宇宙：TAITS_Strategy_Universe_Complete.md
- 風控合規：TAITS_Risk_and_Compliance.md
- 導覽索引：TAITS_Document_Index.md

---

## 8. 完成定義（Definition of Done）

本架構可被視為落地完成，必須：
- 每層都有明確輸入/輸出
- Gate 可真實阻擋下單
- 可回放、可審計、可演進
