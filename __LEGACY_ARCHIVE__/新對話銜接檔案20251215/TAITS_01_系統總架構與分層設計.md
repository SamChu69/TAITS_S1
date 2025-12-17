# 📘 **TAITS_01_系統總架構與分層設計.md**

（最完整落地版｜十層主架構 × 模組責任 × 介面契約 × 資料流/事件流 × 文字結構圖/流程圖）

---

## 0. 文件定位（01 的任務）

本文件是 TAITS 的 **系統骨架與責任邊界規格書**，用來：

1. 把 `TAITS_00` 的憲章落成 **可實作的系統結構**
2. 明確定義 **十層主架構（不可縮減）**
3. 定義每層：

   * 輸入（Input）
   * 輸出（Output）
   * 職責（Responsibility）
   * 禁止事項（Prohibitions）
   * 與上下游的介面契約（Contract）
4. 提供：

   * **文字結構圖（Structure Diagram）**
   * **文字流程圖（Flow Diagram）**
   * **事件流（Event Flow）**
   * **錯誤/降級（Degrade）規則**

📌 本文件不列策略全集（策略在 05）
📌 本文件不寫指標公式（在 03）
📌 本文件不寫 Regime 細節（在 04、11、12）
但會把「Regime 如何嵌入全系統」寫到可以落地。

---

## 1. TAITS 架構總覽（文字結構圖）

### 1.1 十層主架構（L1–L10）

```
L1  治理層（Governance Layer）
L2  資料治理層（Data Governance Layer）
L3  跨市場資訊層（Cross-Market Intelligence Layer）
L4  市場狀態層（Market Regime Layer）
L5  事件與題材層（Event & Theme Layer）
L6  指標與特徵層（Indicator & Feature Layer）
L7  策略層（Strategy Layer）
L8  融合與權重層（Fusion & Weighting Layer）
L9  組合與曝險層（Portfolio & Exposure Layer）
L10 決策閘門層（Decision Gateway Layer）
```

### 1.2 系統「心臟文件」對應（不可缺）

> 00–09 是主線，10–12 是心臟與神經，不是附錄

* **10**：策略×特徵×Regime 使用矩陣（策略使用許可表）
* **11**：Regime 判定引擎規格（Regime 如何算、如何產生狀態）
* **12**：Regime 回測與驗證計畫（Regime 本身也要被驗證）

---

## 2. TAITS 核心運行思想（落地級）

TAITS 不採用「策略直接輸出買賣」的架構，而是採用：

> **證據鏈（Evidence Chain）＋ 治理否決（Governance Veto）＋ 狀態先行（Regime First）**

其運行順序的核心原則為：

1. **資料先可信**（L2）
2. **跨市場先看風險與結構**（L3）
3. **先定市場狀態**（L4）
4. **再看事件題材為何而動**（L5）
5. **再算特徵**（L6）
6. **策略只產生候選**（L7）
7. **融合做共識與衝突處理**（L8）
8. **組合做曝險與集中度管理**（L9）
9. **最後進決策閘門**（L10）
10. **治理與風控可以隨時否決**（L1、L7）

---

## 3. 十層架構逐層規格（完整）

> 本段為 01 的核心，任何人按此即可開始實作系統骨架。

---

### L1｜治理層（治理與權限最高層）

#### 3.1 職責

* 定義全系統運行規則、策略許可、風控否決條件
* 生成「策略/模組是否可執行」的 **Permission Token（許可令牌）**
* 對任何層級輸出具有 **最高否決權**

#### 3.2 輸入

* L2 資料品質狀態（Data Quality State）
* L4 Regime 狀態快照（Regime Snapshot）
* L7 策略候選（Strategy Candidates）
* L9 曝險狀態（Exposure State）
* 外部治理配置（策略白名單/黑名單、最大曝險、禁用清單）

#### 3.3 輸出

* `GovernanceDecision`（允許/限制/否決）
* `StrategyPermissionToken`（策略允許令牌）
* `RiskLock`（風險鎖定：凍結/降槓桿/降頻）

#### 3.4 禁止事項

* 不做資料抓取
* 不算指標
* 不產生策略訊號
* 不觸發下單

#### 3.5 介面契約（Contract）

* **任何策略輸出進入 L8 前必須先通過 L1（至少不被否決）**
* **任何資料品質不合格 → L1 必須能強制凍結 L7/L8/L9/L10**

---

### L2｜資料治理層（資料可信與對齊）

#### 3.1 職責

* 對所有資料來源做：

  * 完整性檢查（缺值/斷檔）
  * 合理性檢查（極端值/負值/時間錯位）
  * 版本化（抓取時間、來源、hash）
* 輸出 **可被特徵層使用的標準化資料**

#### 3.2 輸入

* 02 定義之所有資料源（TWSE/TPEx/TAIFEX/MOPS/新聞/社群/宏觀）
* 各資料源回傳原始格式（JSON/CSV/RSS/文本）

#### 3.3 輸出

* `StandardizedMarketData`（標準化資料集）
* `DataQualityState`（資料品質狀態：OK/WARN/FAIL）
* `MissingDataReport`（缺失報告）
* `AnomalyReport`（異常報告）

#### 3.4 禁止事項

* 不解讀市場
* 不判 Regime
* 不產生策略

#### 3.5 介面契約

* `DataQualityState = FAIL` → **上游 L1 必須可否決全系統推進**
* 所有資料必須轉為統一欄位（在 02 定義），否則拒收

---

### L3｜跨市場資訊層（只觀察，不交易）

#### 3.1 職責

* 將「非股票本體」但會影響股市的資料轉為 **跨市場特徵**
* 典型輸入：

  * 期貨（TAIFEX OpenAPI）
  * 選擇權（TAIFEX OpenAPI）
  * 融資融券（TWSE/TPEx）
  * 匯率/宏觀（央行/國際）
* 輸出供 L4/L7/L8 使用的 **CrossMarket Feature Set**

#### 3.2 輸入

* L2 標準化資料集（含 TAIFEX、融資融券、匯率等）

#### 3.3 輸出

* `CrossMarketFeatures`

  * `FuturesBias`（期貨偏多/偏空/盤整）
  * `BasisState`（期現價差狀態）
  * `OIImpulse`（OI 動量）
  * `OptionsPressure`（選擇權壓力）
  * `MarginCrowding`（融資擁擠度）
  * `FXRisk`（匯率風險）

#### 3.4 禁止事項

* 不生成「買/賣」信號
* 不允許把期貨/選擇權當交易標的

#### 3.5 介面契約

* L3 的輸出只能作為：

  * Regime 輔助（L4）
  * 策略權重調整（L8）
  * 風險警示（L1/L7）
* **不得**繞過 L4 直接指揮策略方向

---

### L4｜市場狀態層（Regime 核心）

#### 3.1 職責

* 產生「市場狀態快照」：主狀態＋次狀態＋信心度
* Regime 必須可回測、可驗證（詳見 11、12）

#### 3.2 輸入

* L2 標準化市場資料（指數、廣度、價量）
* L3 跨市場特徵（期貨/選擇權/融資/匯率）
* L5 事件題材標記（若已產生）

#### 3.3 輸出

* `RegimeSnapshot`

  * `PrimaryRegime`（主狀態）
  * `SecondaryRegime`（次狀態）
  * `ConfidenceScore`（信心度）
  * `RiskMode`（風險模式：Normal/RiskOff/Crisis）
  * `RegimeEvidence`（證據鏈摘要）

#### 3.4 禁止事項

* 不產生策略候選
* 不下單

#### 3.5 介面契約

* L4 輸出的 `PrimaryRegime` 必須被 L1、L7、L8 引用
* 策略若不符合 10 的 Regime 使用矩陣 → 必須被治理層否決

---

### L5｜事件與題材層（新聞/社群/公告的結構化）

#### 3.1 職責

* 把「公告/新聞/社群」轉為結構化事件：

  * 事件類型
  * 影響範圍（市場/產業/個股）
  * 題材強度（強/中/弱）
  * 時效性（即時/短期/中期）
* 此層不判真假，只負責「把資訊變成可用輸入」

#### 3.2 輸入

* MOPS 公告
* 新聞來源（RSS/API/授權抓取）
* 社群（公開文本）
* 搜尋熱度（Google Trends 等）

#### 3.3 輸出

* `EventThemePack`

  * `EventList`
  * `ThemeClusters`
  * `ThemeHeatScore`
  * `NarrativeShiftSignal`（敘事轉折）

#### 3.4 禁止事項

* 不直接輸出買賣建議
* 不取代 L4 的 Regime 判定

---

### L6｜指標與特徵層（Feature 工廠）

#### 3.1 職責

* 把 L2 的標準化資料轉為可比較特徵：

  * 趨勢、動能、波動、結構、量能、廣度、籌碼、衍生品壓力、情緒熱度
* 特徵必須版本化、可回測（在 03 定義）

#### 3.2 輸入

* `StandardizedMarketData`
* `CrossMarketFeatures`
* `EventThemePack`

#### 3.3 輸出

* `FeatureSet`

  * `PriceTrendFeatures`
  * `MomentumFeatures`
  * `VolatilityFeatures`
  * `MarketBreadthFeatures`
  * `StructureFeatures`
  * `ChipFeatures`
  * `DerivativesPressureFeatures`
  * `SentimentFeatures`

#### 3.4 禁止事項

* 不直接下結論（那是 L4/L8 的事）
* 不產生策略候選

---

### L7｜策略層（只產生候選，不下單）

#### 3.1 職責

* 根據 L4 Regime + L6 FeatureSet + L5 EventThemePack
  產生：

  * 策略候選（Candidate）
  * 理由（Evidence）
  * 風險（Risk）
  * 適用條件（Applicable Conditions）

#### 3.2 輸入

* `RegimeSnapshot`
* `FeatureSet`
* `EventThemePack`
* 治理配置（策略白名單/黑名單）

#### 3.3 輸出

* `StrategyCandidateList`

  * `CandidateID`
  * `StrategyFamily`
  * `ApplicableRegime`
  * `EntryLogicSummary`
  * `ExitLogicSummary`
  * `RiskFlags`
  * `ConfidenceScore`
  * `EvidenceChain`

#### 3.4 禁止事項

* 不得自動啟動策略
* 不得繞過 L1、L10

---

### L8｜融合與權重層（共識/衝突處理）

#### 3.1 職責

* 將多策略候選做：

  * 共識評分
  * 衝突偵測（同標的多空衝突、跨族群衝突）
  * 權重調整（受 Regime、風險、情緒影響）

#### 3.2 輸入

* `StrategyCandidateList`
* `RegimeSnapshot`
* `CrossMarketFeatures`
* `GovernanceDecision`

#### 3.3 輸出

* `UnifiedSignalBook`

  * `RankedCandidates`
  * `WeightMap`
  * `ConflictReport`

#### 3.4 禁止事項

* 不下單
* 不推翻治理層否決

---

### L9｜組合與曝險層（整體風險視角）

#### 3.1 職責

* 在「全局」視角做：

  * 集中度
  * 相關性
  * 同題材曝險
  * 流動性與容量限制（Capacity）

#### 3.2 輸入

* `UnifiedSignalBook`
* 持倉/資金狀態（若有）
* 市場流動性資料（D1/D2）

#### 3.3 輸出

* `ExposureState`

  * `ConcentrationRisk`
  * `SectorExposure`
  * `ThemeExposure`
  * `LiquidityRisk`
  * `SuggestedPositionSizing`

#### 3.4 禁止事項

* 不下單

---

### L10｜決策閘門層（人機交會點）

#### 3.1 職責

* 把所有輸出整理成「你能做決策的版本」
* 支援三種模式（由你設定）：

  1. 手動（只給建議）
  2. 半自動（你確認後才執行）
  3. 全自動（你允許時才可執行）

#### 3.2 輸入

* `UnifiedSignalBook`
* `ExposureState`
* `GovernanceDecision`
* `RegimeSnapshot`

#### 3.3 輸出

* `DecisionPacket`

  * Top Candidates + 理由 + 風險 + 建議倉位
  * 治理允許狀態
  * 你需要確認的事項清單（Checklist）

#### 3.4 禁止事項

* 未經你授權，不得執行交易

---

## 4. 文字流程圖（Data Flow + Decision Flow）

### 4.1 資料流（Data Flow）

```
(外部資料源：TWSE/TPEx/TAIFEX/MOPS/新聞/社群/宏觀)
        ↓
L2 資料治理：抓取 → 清洗 → 對齊 → 品質判定
        ↓
L3 跨市場資訊：期貨/選擇權/融資/匯率 → CrossMarketFeatures
        ↓
L5 事件題材：公告/新聞/社群 → EventThemePack
        ↓
L6 特徵工廠：MarketData + Cross + Event → FeatureSet
        ↓
L4 Regime：FeatureSet + Cross → RegimeSnapshot
        ↓
L7 策略：Regime + Feature + Event → StrategyCandidateList
        ↓
L1 治理：策略許可/否決（可插入任意時間點）
        ↓
L8 融合：共識/衝突/權重 → UnifiedSignalBook
        ↓
L9 組合：曝險/集中/容量 → ExposureState
        ↓
L10 決策閘門：DecisionPacket → 你決定
```

---

## 5. 事件流（Event Flow：觸發系統運行的事件）

TAITS 的運行採用「事件驅動」，典型事件如下：

* `E1: MarketClose`（收盤後批次）
* `E2: MarketOpen`（開盤前更新）
* `E3: IntradayTick`（盤中更新，若啟用）
* `E4: NewsBreak`（重大新聞觸發）
* `E5: MOPSAnnouncement`（公告觸發）
* `E6: DataQualityFail`（資料品質失效）
* `E7: RiskLockTrigger`（風控鎖定）

事件流核心規則：

* `E6`、`E7` 觸發時 → **L1 必須能立即凍結後續決策**
* 盤中與盤後可採不同頻率（由你設定）

---

## 6. 降級與容錯（Degrade Rules：不准通靈）

當資料缺失或來源失效時，TAITS 必須：

1. **標記缺失**（MissingDataReport）
2. **不猜測補值**（除非明確定義可補的統計插值）
3. **降級運行**（只輸出能被證據支持的部分）
4. **必要時凍結**（DataQualityState=FAIL）

降級範例：

* TAIFEX OpenAPI 失效
  → L3 缺「衍生品壓力」特徵
  → L4 信心度下降
  → L1 可能限制策略使用（風險上升）

---

## 7. 介面契約總表（給落地工程用）

### 7.1 核心物件（必須存在的資料結構）

* `StandardizedMarketData`
* `DataQualityState`
* `CrossMarketFeatures`
* `EventThemePack`
* `FeatureSet`
* `RegimeSnapshot`
* `StrategyCandidateList`
* `UnifiedSignalBook`
* `ExposureState`
* `GovernanceDecision`
* `DecisionPacket`

### 7.2 生命線（不可破）

* 沒有 `DataQualityState=OK/WARN` → 不得產生策略候選
* 沒有 `RegimeSnapshot` → 策略不得進入融合層
* `GovernanceDecision=VETO` → L8/L9/L10 全部停止

---

## 8. 本文件鎖定聲明（不可縮減）

* 十層主架構 **不可改成五層、不可合併縮水**
* 每層職責與禁止事項 **不得越界**
* 治理層（L1）與 Regime（L4）為全系統最高優先
* 若要新增模組，只能：

  * 放進既有層級
  * 或新增子模組，不得改變主層
