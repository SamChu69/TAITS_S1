# TAITS_Risk_and_Compliance.md
（TAITS 風控與合規｜最高否決權｜極端情境處理｜Observe-only｜KillSwitch）

> 文件定位：TAITS 最高否決層（對齊 00/07/09）
> 核心：Risk/Compliance 可否決一切（Regime、策略、執行）。

---

## 0. 名詞中譯

- Risk Gate：風控閘門（可阻擋）
- Compliance：合規（規則/限制/授權）
- Veto：否決（高層覆蓋低層）
- Kill Switch：緊急停止（立即禁止送單）
- Drawdown：回撤（資金從高點回落）
- Exposure：曝險（持倉風險暴露）
- Leverage：槓桿
- Slippage：滑價
- Liquidity：流動性
- Observe-only：僅觀察（不送單）

---

## 1. 風控最高原則（不可違反）

1) 風控層可以否決任何策略與任何執行  
2) 風控層的否決必須在工程上「真的能擋」  
3) 資料品質不足時，風控必須偏保守（轉 Observe-only）  
4) 期貨/選擇權/融資融券在 TAITS 中是觀察證據，但其風險訊號可以觸發 RiskOverride  
5) 任何輸出若無 Evidence Bundle（證據包），視為不可採信

---

## 2. Risk Gate 輸入與輸出（工程契約）

### 2.1 輸入（Input）
- RegimeResult（R1–R10 + confidence）
- GovernanceDecision（允許/降級/人工/禁止）
- PortfolioState（持倉、成本、曝險）
- MarketSnapshot（含 data_quality）
- LiquidityModel（可成交量估計）
- SlippageModel（滑價估計）
- EventFlags（重大事件旗標：公告/結算/極端波動）
- DerivativesObservation（期貨/選擇權觀察）
- CreditObservation（融資融券觀察）

### 2.2 輸出（Output）
- PASS：可進入下一步（但不代表一定要送單）
- SOFT_BLOCK：限制模式（縮倉/禁止追價/只允許低風險策略）
- HARD_BLOCK：禁止任何送單
- KILL_SWITCH_ON：立即停止所有送單（直到解除）

---

## 3. 風控分層（你要的「可落地」）

### 3.1 系統級風控（System Risk）
- 資料源故障/延遲
- 行情異常跳價
- 關鍵端點不可用
- Snapshot 不一致（同一 run 看到不同事實）

處置：
- 直接 HARD_BLOCK 或 KILL_SWITCH
- 轉 Observe-only
- 強制 Regime=R10 或置信度下調

### 3.2 市場級風控（Market Risk）
- 波動爆發（Volatility Spike）
- 大盤急殺急拉（Intraday Shock）
- 結算週/結算日釘住風險（Pinning）
- 選擇權 OI 壓力牆造成的反向風險

處置：
- SOFT_BLOCK（禁止追價、禁止短線高杠桿）
- 降低倉位上限
- 出場優先權提升（Profit Protect）

### 3.3 策略級風控（Strategy Risk）
- 單策略連敗
- 失效條件觸發（例如假突破濾網）
- 策略與 Regime 不相容

處置：
- Governance DOWNGRADE / BLOCK
- 該策略冷卻（cooldown）
- 權重下調

### 3.4 投組級風控（Portfolio Risk）
- 單一持股曝險過高
- 類股集中風險（你提到題材輪動很快，集中更危險）
- 相關性上升（全部一起跌）

處置：
- 限制集中度
- 相關性上升 → 降總曝險
- 強制分散（或縮倉）

---

## 4. 核心風控規則清單（可直接工程化）

> 下面是 TAITS 必備的「硬規則」，不依賴主觀。

### 4.1 交易前硬限制（Pre-Trade Hard Limits）
- 單筆最大風險（R）：不得超過帳戶淨值的 X%
- 單日最大損失：超過即 HARD_BLOCK
- 單策略最大損失：超過即策略 BLOCK
- 最大持倉檔數：超過即禁止新增
- 流動性門檻：預估可成交量不足 → 禁止進場

### 4.2 滑價與流動性（Slippage/Liquidity）
- 預估滑價 > 門檻 → SOFT_BLOCK（只允許更低急迫性/限價/縮倉）
- 量能乾涸 → 禁止追價、禁止短線策略

### 4.3 回撤（Drawdown Control）
- 連續回撤達 DD1：降倉（risk budget 下調）
- 連續回撤達 DD2：Observe-only（只出不進）
- 連續回撤達 DD3：KILL_SWITCH（停機復盤）

### 4.4 重大事件（Event Flags）
- 公司重大訊息/處置/異常交易：提高風險等級
- 財報/法說附近：策略降級（視策略類型）
- 指數結算/選擇權結算：短線策略降級、釘住風險提示

### 4.5 觀察型衍生品觸發（Observe-only Products Triggers）
- 期貨高波動/急反轉 → 禁止追價策略
- 期現價差異常擴大 → 降曝險
- 選擇權 OI 壓力牆靠近 → 出場優先權提升
- 融資急升且價格加速 → 追高策略降級（避免踩踏）

---

## 5. 合規（Compliance）與授權模式（你說要由你決定）

TAITS 必須支援三種運作模式（由你決定開哪個）：

1) **Advisory Only（只建議）**
   - 系統永遠不送單，只產出建議與限制
2) **Semi-Auto（半自動）**
   - 系統產出 Execution Plan，但要你確認才送
3) **Auto（全自動）**
   - 必須通過 Governance + Risk 雙閘門
   - 必須啟用 KillSwitch 與全程 Audit

> 默認建議：先從 Advisory Only 跑通，再逐步升級。

---

## 6. Kill Switch（緊急停止）規格（不可省）

### 6.1 觸發條件（任一即觸發）
- 資料源大規模故障
- 訂單回報異常（狀態不一致、重複成交等）
- 單日損失超過上限
- 極端行情（你定義的黑天鵝條件）
- 人為手動觸發（最高權限）

### 6.2 觸發後行為
- 禁止任何新單
- 允許：撤單、減倉、風險對沖（若你允許）
- 仍可觀察、仍產出報告、必須寫入 Audit

---

## 7. 審計（Audit）最低要求

每次輸出必須保存：
- snapshot_id
- regime_id + confidence
- governance_decision
- risk_decision
- 觸發的風控規則列表
- evidence_bundle（至少：3 個核心證據）
- run_id + version_manifest

---

## 8. 完成宣告

本文件確立：
- 風控/合規最高否決權
- Observe-only 的衍生品與槓桿觀察如何觸發降級
- KillSwitch 的工程級規格
- 全程可審計、可回放

任何模組若試圖繞過本文件規則，即不屬 TAITS。
