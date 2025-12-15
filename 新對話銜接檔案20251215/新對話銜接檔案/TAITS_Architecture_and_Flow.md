# TAITS_Architecture_and_Flow.md
（TAITS 架構與流程細節｜Data Flow × Decision Flow × Event Flow｜完整運作說明）

> 文件定位：全流程說明（End-to-End Flow）
> 目的：回答「TAITS 到底怎麼運作？」並提供工程落地所需的流程與事件規格。

---

## 0. 名詞中譯

- Data Flow：資料流
- Decision Flow：決策流
- Event Flow：事件流
- Snapshot：快照（可回放）
- Gate：閘門（可阻擋）
- Observe-only：僅觀察（不送單）
- Evidence Bundle：證據包（可審計依據）

---

## 1. TAITS 的三條主流程（總覽）

TAITS 同時運行三條流程，缺一不可：

1) **資料流（Data Flow）**：把市場變成可用資料  
2) **決策流（Decision Flow）**：把資料變成可治理的策略建議  
3) **事件流（Event Flow）**：把所有決策可回放、可追蹤、可告警

---

## 2. 資料流（Data Flow）— 從來源到快照

### 2.1 資料來源分類（高層）
- 官方交易資料：TWSE/TPEX/TAIFEX
- 公司公告：MOPS
- 宏觀/利率/匯率：央行、主計總處、國際來源
- 新聞/社群/情緒：多來源（需可靠度標註）
- 觀察型衍生品：期貨/選擇權（只觀察）
- 融資融券：只觀察資金槓桿與風險

### 2.2 標準化流程（必做）
- 欄位統一（Field Mapping）
- 時間對齊（Time Alignment）
- 缺值策略（Missing Policy）
- 異常偵測（Anomaly Flag）
- 產出 `MarketSnapshot`

### 2.3 快照策略（Replayable Snapshot）
- 每次決策都引用「同一份快照」
- 快照需附：
  - snapshot_id
  - timestamp
  - data_quality（缺哪些資料、哪些異常）

---

## 3. 特徵流（Feature Flow）— 指標與方法論被工程化

### 3.1 Feature Factory 產出內容（對齊 03）
- 技術指標：均線、量能、波動、趨勢、動能等
- 結構方法論特徵：
  - GMMA（顧比均線組）— 趨勢群組與擴散/收斂
  - CBL（顧比倒數線）— 節奏/倒數/轉折壓力（以你定義為準）
  - Wyckoff（威科夫）— 吸籌/派發/彈升/回落等階段證據（方法論中譯必備）
  - Bodick ChanLun（鮑迪克纏論）— 結構段落/背離/資金流向（方法論中譯必備）

> 注意：方法論不是「單一訊號」，是「多特徵證據組」。

---

## 4. Regime 決策流（Regime-First）

### 4.1 Regime Engine 輸入
- MarketSnapshot
- FeatureVector
- 觀察型證據（期貨/選擇權/融資融券）

### 4.2 Regime Engine 輸出（RegimeResult）
- regime_id（R1–R10）
- confidence（置信度）
- evidence_bundle（證據包）
- override_applied（是否被高層覆蓋）
- data_quality_notes（資料不足則走 R10）

### 4.3 R10（資料不足/不判斷）
- 若關鍵資料缺失或異常：
  - regime = R10
  - 系統強制 Observe-only 或限制策略集合

---

## 5. 策略訊號流（Strategy Signals，但不下單）

### 5.1 策略訊號輸入
- FeatureVector
- RegimeResult
- Universe（標的池）與流動性/風險約束

### 5.2 策略訊號輸出
- StrategySignals（334 策略的成立/不成立、強度、證據）
- 每條策略的輸出不得包含「直接送單」

---

## 6. 融合（Fusion）與建議權重（Weighting）

融合引擎輸入：
- StrategySignals
- RegimeResult
- 代理證據（技術/基本面/消息/情緒/宏觀/事件）
- 風控指標（波動/滑價/流動性）

融合引擎輸出：
- CandidateStrategySet（候選策略集合）
- CandidateWeights（候選權重）
- Explanation（可解釋摘要）

---

## 7. 策略治理閘門（Governance Permission Gate）

### 7.1 Governance Gate 輸入
- CandidateStrategySet
- RegimeResult
- Governance Rules（06）

### 7.2 Governance Gate 輸出
- PASS（允許）
- DOWNGRADE（降級：降低權重/縮小標的/縮短持有）
- MANUAL_REVIEW（需人工覆核）
- BLOCK（禁止）

> Governance 是「策略能不能用」的制度化答案。

---

## 8. 風控合規閘門（Risk/Compliance Gate + KillSwitch）

### 8.1 Risk Gate 輸入
- GovernanceDecision
- Portfolio / Exposure
- Volatility / Liquidity / Slippage
- Event Flags（重大事件/極端情境）

### 8.2 Risk Gate 輸出
- PASS：可繼續
- SOFT_BLOCK：只允許低風險模式（Observe/小倉/不追價）
- HARD_BLOCK：全面禁止執行
- KILL_SWITCH：立即停止所有送單（仍可觀察）

---

## 9. 執行層（Execution）— 只有在你決定「允許送單」才會啟動

> Execution 屬於 13+（Implementation）：
> - Execution Planner：把「意圖」轉為拆單計畫
> - Broker Adapter：券商格式轉換（不做判斷）
> - Order State：追蹤生命週期
> - Audit Store：寫入可回放資料

TAITS 的規範是：
- 沒有 Governance + Risk 雙簽章，Execution 不得送單
- 若你選擇「不自動下單」，Execution 僅提供計畫與模擬

---

## 10. 事件流（Event Flow）— 可觀測、可審計、可回放

最小事件集合（不得省略）：
- MARKET_SNAPSHOT_READY
- FEATURE_VECTOR_READY
- REGIME_EVALUATED
- STRATEGY_SIGNAL_SET_READY
- FUSED_SIGNAL_READY
- GOVERNANCE_DECISION_READY
- RISK_DECISION_READY
- EXECUTION_PLAN_READY（如啟動執行）
- ORDER_STATUS_UPDATE（如送單）
- AUDIT_LOG_WRITTEN

每個事件必須帶：
- timestamp
- snapshot_id
- decision_id（若有）
- version_manifest
- evidence_reference（可追溯）

---

## 11. 失效與降級（Failure & Degradation）

任何以下狀態，系統必須降級：
- 行情延遲/異常
- 來源缺失（官方 API 掛）
- 重大事件旗標觸發
- Regime 置信度不足
- 滑價/流動性惡化

降級結果：
- 強制 R10 或 Observe-only
- 禁止追價策略
- 降低倉位上限

---

## 12. 交叉引用（你要找的都在這）

- 系統憲章：TAITS_MASTER_ARCHITECTURE.md
- 全系統分層：TAITS_Full_System_Architecture.md
- 資料來源：TAITS_DataSources_Universe.md
- 策略宇宙：TAITS_Strategy_Universe_Complete.md
- 風控合規：TAITS_Risk_and_Compliance.md
- 導覽索引：TAITS_Document_Index.md
