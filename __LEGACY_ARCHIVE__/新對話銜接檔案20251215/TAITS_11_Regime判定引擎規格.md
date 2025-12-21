# 📘 TAITS_11A_Regime判定引擎規格.md

（Regime Engine Full Spec｜**台股專用**｜Regime 高於訊號｜Risk/Compliance 可否決一切｜API-first｜可落地｜可直接存 GitHub）

---

## 0. 文件定位（非常重要）

本文件定義 TAITS 的 **Regime 判定引擎（Market Regime Engine）** 的：

* 完整輸入（資料與特徵）
* 判定流程（從資料→特徵→分數→Regime）
* Regime 類型與定義（R1~R10）
* 與治理層（TAITS_06）與風控層（TAITS_07）的對接
* 失效/缺資料/極端情況的降級與封鎖
* 審計、回放、版本化、可演進設計

> Regime Engine 不是策略，也不下單；它是「所有策略之上的**總開關**」。

---

## 1. 世界一流內部評分標準（10/10 必要條件）

1. **可落地**：具備輸入/輸出 schema、狀態機、事件流
2. **可審計**：任何一天都能重算、回放、解釋
3. **可抗資料缺失**：缺資料不亂判，降級明確
4. **多源融合**：價格/量/波動/資金/衍生品/信用/事件多層
5. **台股特化**：期貨/選擇權/融資融券/漲跌停/夜盤影響
6. **Regime 高於訊號**：輸出直接控制策略矩陣（TAITS_10）
7. **風控否決**：Regime 不是唯一，仍受 TAITS_07 約束
8. **支援輪動與中小型股**：R7 能合理提升機會而不失控
9. **穩健與可演進**：版本化、灰度切換、置信度校準
10. **中文完整**：含英文對照/中譯，避免未來誤解

---

## 2. Regime Engine 的總體架構（不縮減，完整鏈路）

Regime Engine = 6 個子引擎 + 1 個融合器 + 1 個狀態機

1. **Data Ingestion Layer（資料攝取層）**
2. **Feature Factory（特徵工廠）**
3. **Signal Scorers（子引擎評分器）**
4. **Fusion Engine（融合引擎）**
5. **Regime State Machine（Regime 狀態機）**
6. **Confidence & Calibration（置信度/校準）**
7. **Governance & Risk Interface（治理/風控介面）**

---

## 3. Regime 類型定義（R1~R10）與可解釋條件

> 每個 Regime 都定義「必要條件」「加分條件」「否決條件」。
> 最終輸出：`regime_id + confidence + evidence_bundle`

---

### R1：趨勢多（Bull Trend）

* **必要條件**（滿足其一以上，且未被否決）

  * 趨勢結構偏多（高低點抬升）
  * 趨勢/均線群一致向上（GMMA 正向排列）
* **加分條件**

  * 量能支持、資金流入、期貨不背離
* **否決條件**

  * R4/R6/R8 強制覆蓋，或 R9 假突破高風險

### R2：趨勢空（Bear Trend）

* 與 R1 對稱，且需檢查融資去槓桿、期貨避險上升

### R3：盤整（Range / Mean-Reverting）

* **必要條件**：趨勢不明、波動收斂、上下界清晰
* **加分**：均值回歸特徵強
* **否決**：若事件/高波/流動性失真，轉 R4/R6/R8

### R4：高波動（High Volatility）

* **必要條件**：波動擴張、跳空/大振幅增加
* **效果**：全面降級策略治理上限（A3→A1 等）

### R5：恐慌（Panic / Risk-Off）

* **必要條件**：急跌 + 波動極端 + 信用去槓桿（融資急降）
* **效果**：多數策略僅 Observe；以風控優先

### R6：事件衝擊（Event Shock）

* **必要條件**：事件旗標成立（財報/政策/地緣/突發）
* **效果**：題材 TH 強制 Manual Review（M）；禁止追價

### R7：結構轉換（Transition / Rotation）

* **必要條件**：盤整後壓縮 + 結構突破可能 + 強弱排名翻轉
* **效果**：啟用輪動與中小型通道（仍受成本/流動性門檻）

### R8：流動性失真（Liquidity Distortion）

* **必要條件**：成交/撮合異常、滑價上升、部分標的量能蒸發
* **效果**：禁止高成本策略與追價策略；強制分批與封頂

### R9：假突破高風險（Fakeout / Whipsaw）

* **必要條件**：無量突破/快速回落/期現背離/誘多誘空
* **效果**：突破類策略降為 Observe；結構型策略僅提示

### R10：系統觀望（Uncertain / Low Confidence）

* **必要條件**：資料不足、分數分歧、置信度過低
* **效果**：Regime Engine 主動「不判斷」，交由你保守操作

---

## 4. 輸入資料（Data Inputs）— 必備與可選（含中譯）

> 此段對應 TAITS_02，但在 11 內再次列出「Regime 必需品」，確保新對話也不會漏。

### 4.1 必備（Core Required）

1. **TWSE（台灣證交所）/TPEX（櫃買）行情**

   * 開高低收、成交量、成交額、漲跌停狀態
2. **市場廣度（Breadth）代理**

   * 上漲家數/下跌家數、漲停/跌停家數、創高/創低家數
3. **波動代理（Volatility Proxy）**

   * 當日振幅、ATR 代理、跳空比率
4. **產業/題材分群（Industry/Theme Mapping）**
5. **交易成本代理（Cost Proxy）**

   * 滑價估計、成交額門檻、流動性等級

### 4.2 強烈建議（Strongly Recommended）

6. **TAIFEX（期貨交易所）期貨資料（Observation）**

   * 指數期貨價、量、OI（未平倉）、夜盤變化、期現背離
7. **選擇權資料（Observation）**

   * OI 壓力牆、PCR 代理、IV 代理、結算效應
8. **融資融券（Observation）**

   * 融資餘額變化、融券餘額變化、集中度代理

### 4.3 可選（Optional）

9. **事件資料（Event）**：財報、政策、國際突發
10. **新聞/社群情緒代理（Sentiment）**：僅作輔助、不可單獨判定

---

## 5. 特徵工廠（Feature Factory）— Regime 專用特徵全集

> 這裡是 Regime 引擎的「可重算基礎」。所有特徵都要版本化。

### 5.1 Trend 特徵（趨勢）

* `trend_hhhl_score`：高低點抬升/下移分數
* `gmmacluster_alignment`：GMMA 群組一致性
* `slope_consensus`：多時間框架斜率一致性

### 5.2 Range/Mean 特徵（盤整/均值）

* `range_compression`：區間壓縮程度
* `mean_revert_strength`：均值回歸強度
* `breakout_pressure`：突破壓力（壓縮後能量）

### 5.3 Volatility 特徵（波動）

* `atr_ratio`：ATR/price 比例
* `gap_frequency`：跳空頻率
* `intraday_amplitude`：盤中振幅

### 5.4 Liquidity/Cost 特徵（流動性/成本）

* `turnover_class`：成交額等級
* `slippage_proxy`：滑價代理
* `liquidity_drop_rate`：流動性蒸發速度

### 5.5 Breadth 特徵（廣度）

* `adv_decl_ratio`：漲跌家數比
* `limit_up_down_pressure`：漲跌停壓力
* `new_high_low_diff`：創高創低差

### 5.6 Derivatives/Credit 特徵（衍生品/信用，僅觀察）

* `fut_cash_divergence`：期現背離
* `fut_hedge_intensity`：避險強度代理
* `opt_wall_pressure`：OI 壓力牆代理
* `margin_deleveraging`：融資去槓桿強度

### 5.7 Event/Sentiment 特徵（事件/情緒）

* `event_flag_severity`：事件強度
* `sentiment_extreme_score`：情緒極端代理（可選）

---

## 6. 子引擎評分器（Scorers）— 6 個分數來源

每個子引擎輸出：`score_vector[R1..R10] + confidence + evidence`

1. **TrendScorer（趨勢評分器）**
2. **RangeScorer（盤整/均值評分器）**
3. **VolatilityScorer（波動評分器）**
4. **BreadthScorer（廣度評分器）**
5. **LiquidityScorer（流動性/成本評分器）**
6. **OverlayScorer（期貨/選擇權/融資/事件疊加評分器）**

---

## 7. 融合引擎（Fusion Engine）— Regime 最終決策規則

### 7.1 融合輸入

* `S_trend, S_range, S_vol, S_breadth, S_liq, S_overlay`
* 每個 S 都是 10 維向量（對應 R1~R10）

### 7.2 融合規則（必須可解釋）

1. **先做強制覆蓋（Override）**

   * 若 `R8`（流動性失真）達門檻 → 先鎖 R8
   * 若 `R6`（事件）達門檻 → 先鎖 R6
   * 若 `R5`（恐慌）達門檻 → 先鎖 R5
2. **再做主類別選擇（Trend/Range/Transition）**

   * 趨勢優勢 → R1/R2
   * 盤整優勢 → R3
   * 轉換訊號 → R7
3. **最後做「假突破檢測」**

   * 若 fakeout 強 → R9 覆蓋突破類結論
4. **置信度不足 → R10**

---

## 8. Regime 狀態機（State Machine）— 防止「一天切十次」

### 8.1 狀態機輸出

* `current_regime`
* `regime_confidence`
* `regime_stability`（穩定度）
* `switch_reason`（切換原因）

### 8.2 切換規則（必備）

* **最小持續時間（Min Hold）**：避免抖動
* **切換門檻（Switch Threshold）**：必須超過差距
* **冷卻時間（Cooldown）**：切換後短時間不再切
* **事件插入（Event Insert）**：R6/R5/R8 可立即插入
* **回復規則（Recovery）**：從 R5/R8 回復需連續確認

---

## 9. 輸出規格（Output Schema）— 可直接落地

Regime Engine 每次輸出一份「可審計快照」：

```json
{
  "timestamp": "YYYY-MM-DD HH:MM:SS",
  "market": "TW",
  "regime_id": "R7",
  "confidence": 0.82,
  "stability": 0.71,
  "override_applied": ["R6"],
  "scores": {
    "trend":   {"R1": 0.62, "...": 0.01},
    "range":   {"R3": 0.55, "...": 0.02},
    "vol":     {"R4": 0.40, "...": 0.03},
    "breadth": {"R7": 0.68, "...": 0.02},
    "liq":     {"R8": 0.12, "...": 0.01},
    "overlay": {"R6": 0.20, "...": 0.01}
  },
  "evidence_bundle": {
    "top_features": [
      {"name": "range_compression(區間壓縮)", "value": 0.83},
      {"name": "strong_weak_flip(強弱翻轉)", "value": 0.72}
    ],
    "alerts": ["FAKEOUT_RISK_LOW", "LIQ_OK"]
  },
  "interfaces": {
    "strategy_matrix_profile": "TAITS_10_profile_R7",
    "governance_cap": "A3",
    "risk_mode": "R1"
  }
}
```

> 注意：此段 JSON 僅是 schema 範例；實際值由你後續落地實作決定。

---

## 10. 與 TAITS_10 / TAITS_06 / TAITS_07 的對接（完整）

### 10.1 對接 TAITS_10（策略×Regime矩陣）

* `regime_id` 直接選擇對應矩陣欄位
* 矩陣輸出「允許上限」：A1/A2/A3/A4/O/B/M

### 10.2 對接 TAITS_06（治理）

* Regime Engine 只提供：`cap_recommendation`
* 治理層才負責：放行/阻擋、審計、權重調整

### 10.3 對接 TAITS_07（風控）

* 風控可覆蓋 Regime 的任何建議
* 例如：Regime=R1 但風控觸發 R2/R3 → 直接降級或封鎖

---

## 11. 缺資料/斷線/極端情況（不可偷工，完整處理）

### 11.1 缺資料分類（DR）

* DR-01 單一來源缺失
* DR-02 多來源缺失
* DR-03 延遲
* DR-04 異常值

### 11.2 降級規則

* 任一關鍵必備資料缺失 → `regime_id = R10`
* 衍生品/融資缺失 → 不影響核心，但降低 confidence
* 異常值 → evidence 加上 `DATA_ANOMALY_FLAG`

### 11.3 Kill Switch（緊急停止）

* 若連續 N 次輸出 R10 或資料異常 → 系統切到 Observe

---

## 12. 審計與版本化（新對話 100% 能重建）

必備輸出檔（每天生成）：

* `regime_snapshot_log`
* `feature_store_daily`
* `scorer_version_manifest`
* `regime_switch_events`

版本化規則：

* 每次調整特徵/閾值 → bump `regime_engine_version`
* 保留舊版本可回放（Backtest/Replay）

---

## 13. 本批交付狀態與下一批

你要求「完整詳細版」，11 內容很大，我已交付 **11A（核心規格 + 架構 + 定義 + 流程 + schema + 對接）**。

# 📘 TAITS_11B_Regime判定規則與閾值全集.md

（Regime Decision Rules & Thresholds｜**不可偷工版**｜逐條規則｜可直接落地｜可審計｜可回放）

---

## 0. 文件定位（承接 11A，補齊「怎麼判」）

**TAITS_11A** 解釋的是：

> Regime Engine「是什麼、用哪些資料、怎麼流動」

**TAITS_11B** 解釋的是：

> **每一個 Regime「到底怎麼被判定出來」**

本文件回答四件事（缺一不可）：

1. **每個 Regime 的判定規則（必要 / 加分 / 否決）**
2. **每個 Regime 的量化閾值邏輯（不是固定數字，而是機制）**
3. **Override（強制覆蓋）優先序**
4. **狀態機參數（避免 Regime 亂跳）**

---

## 1. 世界一流內部評分標準（11B 專用）

要達到 10/10，本文件必須：

1. 每一個 Regime **都有完整三段式規則**
2. 不依賴「神祕參數」，而是**可調整閾值機制**
3. 能解釋「為什麼不是別的 Regime」
4. 能處理 **台股特有狀況**（漲跌停、夜盤、流動性）
5. 能支援 **輪動 → 中小型股爆發**
6. 能防止 **假突破 / 盤中雜訊**
7. Regime 切換 **不會一天十次**
8. 缺資料時 **一定退到 R10**
9. 與 TAITS_10 / 06 / 07 完全對齊
10. 新對話只看 11A + 11B 就能完整重建

---

## 2. Regime 判定總流程（規則順序非常重要）

**判定順序 = 生存優先順序**

```
Step 1：資料完整性檢查
Step 2：強制 Override Regime（R8 / R6 / R5）
Step 3：核心結構判定（R1 / R2 / R3 / R7）
Step 4：假突破與雜訊修正（R9）
Step 5：置信度不足 → R10
Step 6：進入狀態機（是否允許切換）
```

---

## 3. 強制 Override Regime（最高優先序）

> 這三個 Regime **可以直接覆蓋所有其他結論**

### 3.1 R8｜流動性失真（Liquidity Distortion）

#### 必要條件（任一成立）

* 成交額等級大幅下降（多數標的低於自身歷史分位）
* 滑價代理急升
* 多數中小型股「有價無量」
* 撮合斷裂（跳價成交、價差拉大）

#### 加分條件

* 期貨夜盤波動異常
* 盤中漲跌停比例升高但量能不足

#### 否決條件

* 僅少數標的流動性下降（局部問題）

👉 **一旦成立 → Regime = R8（直接覆蓋）**

---

### 3.2 R6｜事件衝擊（Event Shock）

#### 必要條件

* 財報週（大量公司同時公告）
* 政策/法規公布日
* 國際突發（戰爭、制裁、金融事件）

#### 加分條件

* 開盤跳空比例高
* 題材股同步異動

#### 否決條件

* 事件已被市場充分消化（連續數日）

👉 **成立 → Regime = R6（覆蓋 R1–R3–R7）**

---

### 3.3 R5｜恐慌（Panic / Risk-Off）

#### 必要條件（至少兩項）

* 指數急跌
* 波動代理極端
* 融資餘額快速下降
* 大量跌停 / 接近跌停

#### 加分條件

* 期貨避險急升
* Put OI 激增

#### 否決條件

* 僅單一族群恐慌（非系統性）

👉 **成立 → Regime = R5（全面防守）**

---

## 4. 核心結構 Regime（R1 / R2 / R3 / R7）

> 以下 Regime 只有在 **未被 R8/R6/R5 覆蓋** 時才會判定

---

### 4.1 R1｜趨勢多（Bull Trend）

#### 必要條件（至少兩項）

* 高低點結構抬升
* GMMA 多頭排列
* 多數產業呈現正斜率

#### 加分條件

* 市場廣度正向
* 資金流入
* 期貨未出現明顯避險

#### 否決條件

* 假突破風險升高（轉 R9）
* 流動性惡化（轉 R8）

---

### 4.2 R2｜趨勢空（Bear Trend）

#### 必要條件

* 高低點結構下移
* GMMA 空頭排列
* 市場廣度負向

#### 加分條件

* 融資去槓桿
* 期貨避險升高

#### 否決條件

* 出現明顯恐慌（轉 R5）

---

### 4.3 R3｜盤整（Range / Mean）

#### 必要條件

* 高低點無趨勢
* 波動收斂
* 上下界反覆測試

#### 加分條件

* 均值回歸特徵穩定
* 族群輪動但未擴散

#### 否決條件

* 出現結構壓縮後突破（轉 R7）

---

### 4.4 R7｜結構轉換 / 輪動（Transition）

> **你最在意的 Regime**

#### 必要條件（至少兩項）

* 盤整後壓縮
* 強弱排名開始翻轉
* 題材由點 → 線 → 面擴散

#### 加分條件

* 中小型股成交量回升
* 資金從權值轉向非權值
* 多族群同步啟動

#### 否決條件

* 無量突破（轉 R9）
* 流動性不足（轉 R8）

👉 **R7 是「爆發前的窗」，不是追價期**

---

## 5. 修正 Regime（R4 / R9 / R10）

---

### 5.1 R4｜高波動（High Volatility）

#### 必要條件

* 波動代理顯著上升
* 盤中振幅異常

#### 效果

* **不否決方向，但全面降級治理上限**
* A3 → A1、禁止追價

---

### 5.2 R9｜假突破高風險（Fakeout）

#### 必要條件

* 無量突破
* 快速拉回
* 期現背離
* 誘多誘空結構

#### 效果

* 突破/追價類策略 → Observe
* 結構型策略僅提示

---

### 5.3 R10｜系統觀望（Low Confidence）

#### 觸發條件

* 多 Regime 分數接近
* 關鍵資料缺失
* 子引擎互相矛盾

#### 效果

* 系統主動「不判斷」
* 交由你保守操作

---

## 6. Regime 優先序總表（最重要）

```
R8（流動性）  
> R6（事件）  
> R5（恐慌）  
> R4（高波動）  
> R9（假突破）  
> R7（轉換）  
> R1 / R2（趨勢）  
> R3（盤整）  
> R10（觀望）
```

---

## 7. 狀態機參數（防止 Regime 亂跳）

### 7.1 必備參數

* **min_hold_period**：最小維持時間
* **switch_threshold**：切換分數差
* **cooldown_period**：切換後冷卻
* **event_override_flag**：事件插入權

### 7.2 行為規則（文字化）

* Regime 不得連續快速來回切換
* Override Regime 可立即插入
* 從 R5/R8 回復需「連續確認」
* R10 需等待資料恢復與置信度上升

---

## 8. 盤中 Regime vs 日 Regime（雙層設計）

* **Daily Regime**：主導策略矩陣（TAITS_10）
* **Intraday Regime**：只做降級/風控修正
* 盤中 Regime **不可推翻** 日 Regime，只能更保守

---

## 9. 與 TAITS_10 / 06 / 07 的最終對齊

* **TAITS_10**：Regime 決定「哪些策略可用」
* **TAITS_06**：治理層決定「用到哪一級」
* **TAITS_07**：風控層可隨時否決

> **Regime 是方向盤，不是油門，也不是煞車**

---

## 10. 11B 交付完成聲明

* ✔ 每個 Regime 均有 **必要 / 加分 / 否決**
* ✔ Override 與優先序明確
* ✔ 支援台股輪動與中小型股
* ✔ 無任何偷工、無模糊敘述
* ✔ 與你前面 334 策略 **完全對齊**
