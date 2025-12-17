# 📘 TAITS_12A_Regime回測與驗證計畫.md

（Regime Backtest & Validation Master Plan｜**完整落地版**｜可審計｜可迭代｜不自欺欺人）

---

## 0. 文件定位（非常重要）

本文件是 TAITS 的 **Regime 系統驗證總計畫**。
它回答一個核心問題：

> **Regime 判得對不對？對策略與風控的幫助有多大？如何迭代而不過擬合？**

本文件不是策略、不是下單規則，而是：

* **Regime Engine（TAITS_11）** 的科學驗證方法
* 與 **策略矩陣（TAITS_10）**、治理層（TAITS_06）、風控（TAITS_07）連動的回測計畫
* 可直接落地成「每日/每週/每月的驗證流水線」

---

## 1. 世界一流內部評分標準（12 的 10/10 必要條件）

1. **驗證對象清楚**：Regime 本身、Regime→策略、Regime→風控三層都驗
2. **可重現**：任何日期可回放、同樣資料重算同結果
3. **防過擬合**：走窗、分段、跨市場、跨題材
4. **含台股特化**：漲跌停、夜盤、融資融券、結算週
5. **含中小型股爆發**：不能只驗證權值股/ETF
6. **含事件/極端**：R5/R6/R8 必須可驗且可解釋
7. **指標全面**：分類準確度 + 交易績效提升 + 風控改善
8. **可審計**：輸出 log、版本、超參數、資料指紋（hash）
9. **可迭代**：提供調參流程、灰度、回滾
10. **能落地自動化**：形成 pipeline（每日/每週/每月）

---

## 2. 驗證範圍總覽（你要的「全」：三層驗證）

TAITS_12 的驗證分三層（缺一不可）：

### L1：Regime 本體驗證（Regime Quality）

* Regime 是否穩定、可解釋、不亂跳
* Regime 是否與市場狀態相符

### L2：Regime → 策略矩陣驗證（Decision Quality）

* 有 Regime gating vs 沒有 gating 的差異
* 策略在不同 Regime 的勝率/報酬/回撤差異

### L3：Regime → 風控效果驗證（Risk Quality）

* Regime 是否能提前降風險、避免錯誤追價
* R5/R6/R8/R9 是否有效降低尾部風險

---

## 3. 必備資料集與分層資料版本（Data & Versioning）

> 不偷工：回測失真通常都死在資料。這段要完整。

### 3.1 必備資料（Core）

* 台股大盤/加權指數（OHLCV）
* 市場廣度（漲跌家數、漲跌停、創高創低）
* 產業分類與成分股（含時間變動）
* 成交額/流動性指標（用於 R8）

### 3.2 強烈建議資料（Overlay）

* TAIFEX 指數期貨：價、量、OI、夜盤（用於 FU 與 Regime overlay）
* 選擇權：OI 壓力牆、PCR/IV 代理（用於 OP）
* 融資融券：餘額與變化（用於 MG）
* 事件資料：財報日、政策、國際突發（用於 EV）

### 3.3 資料版本化（必做）

每一次回測都要固定：

* `data_snapshot_id`（資料快照 ID）
* `data_hash_manifest`（每個表的 hash）
* `feature_version`（特徵工廠版本）
* `regime_engine_version`（Regime 引擎版本）
* `strategy_matrix_version`（TAITS_10 版本）

> 沒有版本化，就沒有科學驗證。

---

## 4. Regime 標註與「真值」問題（Ground Truth Design）

Regime 驗證的難點是：**市場狀態沒有絕對真值**。
因此 TAITS 採用 **多視角真值（Multi-Label Proxy）**：

### 4.1 趨勢真值（Trend Proxy）

* 以多時間框架斜率/破高破低結構作為趨勢代理
* 用於驗證 R1/R2

### 4.2 盤整真值（Range Proxy）

* 波動收斂 + 上下界反覆測試
* 用於驗證 R3

### 4.3 高波動/恐慌真值（Vol/Panic Proxy）

* 波動極端分位 + 大跌/跌停比例 + 融資去槓桿
* 用於驗證 R4/R5

### 4.4 事件真值（Event Proxy）

* 財報週、政策日、重大新聞日（事件清單）
* 用於驗證 R6

### 4.5 流動性失真真值（Liquidity Proxy）

* 成交額分位下降 + 滑價代理上升 + 小型股成交蒸發
* 用於驗證 R8

### 4.6 假突破真值（Fakeout Proxy）

* 突破後 N 日快速回落 + 量能不足 + 期現背離
* 用於驗證 R9

### 4.7 結構轉換/輪動真值（Transition Proxy）

* 強弱排名翻轉 + 題材擴散（點→線→面）+ 量能回流
* 用於驗證 R7

---

## 5. L1：Regime 本體驗證（Regime Quality Metrics）

### 5.1 穩定度與抖動（Stability）

* **Switch Rate**：每月切換次數（越少越好，但不可僵化）
* **Churn Index**：短時間來回切換比例
* **Min Hold Compliance**：是否遵守最小維持期

### 5.2 置信度校準（Calibration）

* 信心 0.8 的日子，是否真的較少失敗？
* 低信心是否合理掉到 R10？

### 5.3 可解釋性（Explainability）

* 每次 Regime 輸出必須帶 evidence_bundle
* Top features 是否穩定一致

### 5.4 覆蓋一致性（Override Correctness）

* R5/R6/R8 插入是否合理？是否過度插入？

---

## 6. L2：Regime → 策略矩陣驗證（最重要）

> 這才是你真正要的：「Regime 有沒有提高勝率」。

### 6.1 基準組（Baselines）

必須比較至少四種系統：

1. **B0：無 Regime（全開）**
2. **B1：僅使用 R1/R2 趨勢濾網**
3. **B2：使用完整 R1~R10 + 治理**
4. **B3：使用完整 Regime + 風控否決（TAITS_07 全開）**

### 6.2 策略層評估指標（Per-Strategy / Per-Cluster）

對每一條策略（或策略族群）計算：

* 勝率（Win Rate）
* 期望值（Expectancy）
* 平均盈虧比（Payoff Ratio）
* 最大回撤（Max Drawdown）
* 交易次數與覆蓋率（Coverage）
* 交易成本敏感度（Slippage Sensitivity）
* 對 R7 中小型股的捕捉率（Small-cap Capture Rate）

### 6.3 Regime 交叉矩陣分析（你要的「都要」）

對每個 Regime 做：

* 策略族群勝率排行
* 策略族群回撤排行
* 哪些策略在某 Regime 會「系統性失效」
* 哪些策略在 R7 才有 alpha（輪動核心）

輸出至少三張報表（可落地生成）：

* `Strategy x Regime Performance Table`
* `Regime Coverage Heatmap`
* `Failure Mode Attribution Table`

---

## 7. L3：Regime → 風控驗證（尾部風險才是關鍵）

### 7.1 尾部事件集合（必含台股特殊）

* 金融危機/疫情/重大政策
* 大盤單日暴跌、連續跌停潮
* 財報週大幅跳空
* 結算週行情扭曲
* 夜盤劇烈變動隔日影響

### 7.2 風控評估指標

* 最大回撤降低幅度（ΔMDD）
* 95% / 99% 壞分位（Tail Loss）
* 恐慌日曝險（Exposure on Panic Days）
* 高波動期間追價次數（Chase Count）
* R8 期間滑價損失（Slippage Loss）

---

## 8. 台股專用測試切片（你要求的「每個時期都不一樣」）

Regime 必須在不同題材輪動下都有效，因此必做切片：

### 8.1 產業輪動切片（Sector Rotation Slices）

* DRAM、AI、機器人、PCB、材料、工具、航運、金融、傳產等
* 每個切片：R7 捕捉率、R9 假突破率、R8 流動性警示率

### 8.2 市值切片（Market Cap Slices）

* 大型權值
* 中型
* 小型
* 微型（最容易失真）

> 必須證明：系統不只會做權值股，也能「合理納入中小型爆發」。

### 8.3 流動性切片（Liquidity Slices）

* 高流動性
* 中流動性
* 低流動性（必須被限制但不能完全忽略）

---

## 9. 走窗與防過擬合（Walk-Forward & Anti-Overfit）

### 9.1 Walk-Forward 設計（必做）

* 訓練窗：例如 12–24 個月
* 測試窗：例如 3–6 個月
* 滑動更新：每月/每季滾動

### 9.2 不可做的事（明確禁止）

* 用整段資料調到最好再宣稱有效
* 用同一批事件資料調參後再驗證同事件

### 9.3 參數限制（Regularization）

* 閾值只能小幅調整（上限/步進）
* Regime 切換頻率必須受控（狀態機限制）

---

## 10. 校準與調參流程（你要的「可演進」）

### 10.1 調參順序（不可亂）

1. 修資料與特徵（先確保可重算）
2. 修 Override 門檻（R8/R6/R5）
3. 修 R9 假突破檢測
4. 修 R7 輪動特徵
5. 最後才修 R1/R2/R3 的邊界

### 10.2 調參輸出（必留痕）

* 改了哪個閾值
* 影響了哪些 Regime
* 交易績效改善多少
* 風控改善多少
* 是否有副作用（例如 R10 變多）

---

## 11. 驗證輸出交付物（每次回測必須產生）

### 11.1 必備報告（Artifacts）

* `RegimeQualityReport.md`
* `RegimeSwitchAuditLog.csv`
* `StrategyRegimePerformance.csv`
* `RiskImpactReport.md`
* `FailureModeReport.md`
* `VersionManifest.json`

### 11.2 儀表板（可選但建議）

* Regime 時序圖（含 confidence）
* 策略覆蓋熱力圖
* 事件期間風險曲線

---

## 12. 驗證通過門檻（Definition of Done）

> 你要的不是「看起來很強」，而是 **可被質疑也站得住**。

### 12.1 L1 通過門檻

* 切換頻率合理（不抖動）
* R10 只在合理時出現
* Override 不過度

### 12.2 L2 通過門檻

* B2/B3 相對 B0：

  * 回撤降低
  * 期望值提升或至少維持
  * 假突破追價明顯降低
  * R7 的中小型捕捉率提升

### 12.3 L3 通過門檻

* 尾部風險顯著降低（尤其 R5/R8）

---

## 13. 12A / 12B 分批交付規劃（避免一次爆量）

你要「完整詳細版」，此文件仍很大，我已交付：

✅ **TAITS_12A：驗證總計畫（本文件）**

# 📘 TAITS_12B_Regime回測流程與Pipeline工程規格.md

（Backtest & Validation Pipeline｜**工程可落地版**｜不中斷｜可重跑｜可審計）

---

## 0. 文件定位（12B 是「怎麼跑」）

如果說：

* **TAITS_12A**：回答「驗什麼、為什麼驗、驗對算成功」
* **TAITS_12B**：回答 **「每天、每週、每月，系統實際怎麼跑」**

這一份文件是給 **工程實作 / Cursor / CI Pipeline** 用的，
但 **不依賴任何 XQ、不綁特定語言**，純結構規格。

---

## 1. 世界一流內部評分標準（12B 專用）

本文件要達到 10/10，必須：

1. **Pipeline 可完全自動化**
2. 任一步失敗 **可定位、可重跑**
3. 每次結果 **可審計、可回放**
4. 支援 **日 / 週 / 月 三種節奏**
5. 支援 **單 Regime / 多 Regime / 全系統**
6. 支援 **台股特性（夜盤、結算、事件）**
7. 支援 **版本鎖定與回滾**
8. 支援 **未來資料擴充（不破壞舊結果）**
9. 結果輸出 **直接可供決策**
10. 新對話只靠 12A + 12B 就能落地

---

## 2. Pipeline 總覽（高層）

### 2.1 三條主 Pipeline

```
P1：Daily Validation Pipeline（日常）
P2：Weekly Analysis Pipeline（分析）
P3：Monthly Full Backtest Pipeline（驗證）
```

### 2.2 共用模組（所有 Pipeline 都會用）

```
Data Loader
→ Feature Factory
→ Regime Engine
→ Strategy Matrix Engine
→ Backtest Engine
→ Risk Evaluator
→ Report Generator
→ Artifact Store
```

---

## 3. Pipeline 共用基礎規格

### 3.1 Pipeline 輸入（Input）

每次執行 Pipeline，**必須明確指定**：

```yaml
pipeline_run:
  run_id: TAITS_YYYYMMDD_HHMM
  pipeline_type: daily | weekly | monthly
  data_snapshot_id: <string>
  feature_version: <semver>
  regime_engine_version: <semver>
  strategy_matrix_version: <semver>
  risk_engine_version: <semver>
  time_range:
    start: YYYY-MM-DD
    end: YYYY-MM-DD
```

---

### 3.2 Pipeline 輸出（Output）

**每一次 run 必須產出一個完整目錄**：

```
/runs/<run_id>/
├── manifest.json
├── data/
│   └── data_hashes.json
├── features/
│   └── feature_manifest.json
├── regime/
│   ├── regime_timeseries.csv
│   ├── regime_confidence.csv
│   └── regime_evidence.json
├── backtest/
│   ├── trades.csv
│   ├── equity_curve.csv
│   └── metrics.json
├── risk/
│   └── risk_report.json
├── reports/
│   ├── regime_quality.md
│   ├── strategy_regime_performance.md
│   ├── risk_impact.md
│   └── summary.md
└── logs/
    └── pipeline.log
```

> **缺任何一個 = 該次驗證無效**

---

## 4. P1｜Daily Validation Pipeline（日常）

### 4.1 目的

* 驗證 **Regime 今日是否合理**
* 檢查 **是否出現異常（資料 / 邏輯）**
* 為隔日策略使用提供「可信狀態」

### 4.2 流程（逐步）

```
Step D1：Load 當日資料（含夜盤）
Step D2：資料完整性檢查
Step D3：產生 Features（僅必要特徵）
Step D4：執行 Regime Engine（Intraday + Daily）
Step D5：Regime Evidence 檢查
Step D6：異常檢測（切換過頻 / R10 過多）
Step D7：輸出 Daily Regime Report
```

### 4.3 關鍵輸出

* 今日 Regime
* Regime confidence
* 是否觸發 Override
* 是否需要人工檢視（Flag）

---

## 5. P2｜Weekly Analysis Pipeline（分析）

### 5.1 目的

* 檢查 **Regime 是否穩定**
* 分析 **策略在各 Regime 的表現**
* 找出 **輪動 / 中小型股捕捉是否正常**

### 5.2 流程

```
Step W1：Load 一週資料
Step W2：完整 Feature Factory
Step W3：Daily Regime 回放
Step W4：Strategy × Regime 矩陣統計
Step W5：風控影響分析
Step W6：生成週報
```

### 5.3 必備分析（不能省）

* Regime 切換次數
* R7 覆蓋率與命中率
* R9 假突破觸發率
* R8 流動性警示比例
* 中小型股績效 vs 權值股

---

## 6. P3｜Monthly Full Backtest Pipeline（核心）

> **這是「驗證你整套系統值不值得信」的 Pipeline**

### 6.1 目的

* 驗證 Regime 系統 **是否真的提高勝率 / 降低風險**
* 比較不同設定（A/B）
* 為參數調整提供依據

---

### 6.2 流程（完整）

```
Step M1：鎖定資料快照（Freeze）
Step M2：Feature Factory（全量）
Step M3：Regime 回放（全期間）
Step M4：建立 Strategy × Regime 可用矩陣
Step M5：執行 Backtest（多組 Baseline）
Step M6：風控層注入（TAITS_07）
Step M7：績效與風險統計
Step M8：失敗模式歸因
Step M9：生成完整報告
```

---

## 7. Backtest Engine 規格（核心模組）

### 7.1 Backtest 模式（必須全支援）

| 模式               | 說明            |
| ---------------- | ------------- |
| Single Strategy  | 單一策略在多 Regime |
| Strategy Cluster | 策略族群          |
| Full System      | 全系統（334 條）    |
| Baseline Compare | B0/B1/B2/B3   |

---

### 7.2 Backtest 必備參數

```yaml
backtest_config:
  execution_model: next_open | close | vwap_proxy
  transaction_cost:
    commission: fixed | rate
    slippage_model: linear | liquidity_based
  capital_model:
    fixed_capital
    risk_weighted
  position_sizing:
    equal_weight
    volatility_scaled
```

---

## 8. Risk Evaluator 規格（TAITS_07 對齊）

### 8.1 風控注入點

* 下單前（Regime gating）
* 持倉中（降級 / 停止加碼）
* 事件 / 恐慌 / 流動性失真即時介入

### 8.2 必算指標

* MDD
* Tail Loss（95/99）
* Exposure on Panic Days
* Slippage Loss（R8 專用）
* Chase Count（追價次數）

---

## 9. 失敗模式歸因（Failure Attribution）

> 不只看賺多少，還要知道 **為什麼虧**

每次 Monthly Pipeline 必須輸出：

* 哪些 Regime 判錯？
* 哪些策略在錯誤 Regime 被啟用？
* 是資料問題 / 特徵問題 / 閾值問題？
* 是否需要調參？調哪一層？

---

## 10. Experiment 與版本管理（極重要）

### 10.1 Experiment ID 規則

```
EXP_<YYYYMM>_<RegimeVer>_<FeatureVer>_<MatrixVer>
```

### 10.2 可回滾保證

* 舊結果 **永遠可重算**
* 新調整 **不覆蓋舊實驗**

---

## 11. Pipeline 錯誤處理與重跑

### 11.1 失敗分類

* DataError
* FeatureError
* RegimeError
* BacktestError
* ReportError

### 11.2 重跑策略

* 可從任一 Step checkpoint 重跑
* 不得默默跳過失敗步驟

---

## 12. 自動化與排程（Scheduler）

| Pipeline | 建議頻率  |
| -------- | ----- |
| Daily    | 每日收盤後 |
| Weekly   | 週末    |
| Monthly  | 每月固定日 |

---

## 13. 最終交付聲明（12B）

* ✔ Pipeline 結構完整
* ✔ 不綁任何特定工具
* ✔ 支援台股與輪動
* ✔ 可直接交給工程實作
* ✔ 與 12A / 11 / 10 / 07 完全對齊
* ✔ **無偷工減料**
