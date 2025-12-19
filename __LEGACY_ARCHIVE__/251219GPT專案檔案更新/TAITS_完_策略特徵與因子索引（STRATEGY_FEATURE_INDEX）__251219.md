# TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219
doc_key：STRATEGY_FEATURE_INDEX  
治理等級：B（Feature & Factor Index｜治理對齊版｜承接 STRATEGY_UNIVERSE / ARCH_FLOW / DATA_SOURCES）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（特徵/因子索引母表；Only-Add 演進；不可縮減語義）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX（Index 裁決）  
平行參照：STRATEGY_UNIVERSE / ARCH_FLOW / FULL_ARCH / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化邊界/偷換定義）  
核心鐵律：Feature ≠ Signal ≠ Strategy ≠ Order（特徵不是訊號、不是策略、不是下單）＋ Evidence First（證據先於判斷）＋ Regime > Strategy（狀態高於策略）＋ Risk/Compliance 可否決一切

---

## 0. 文件定位（Why This Document Exists）

本文件是 TAITS 的「策略特徵與因子索引」母表，目的在於：

1. 定義 TAITS 全系統中可被使用的 **特徵（Feature）/因子（Factor）/指標（Indicator）/結構輸出（Structure Output）** 的標準語義、產生來源、輸入輸出、限制與審計義務  
2. 讓任何策略（STRATEGY_UNIVERSE）只能「引用」特徵，而不是「暗藏」特徵；避免形成隱性策略  
3. 強制落實治理邊界：  
   - 特徵不產生交易方向  
   - 特徵不具下單權  
   - 特徵不能繞過 Evidence/Regime/Risk/Governance  
4. 建立「可回放/可追溯」的 Feature Provenance（來源追溯）與 Version Alignment（版本一致性）標準  
5. 使 UI、審計、回測、實盤可用同一語義，不允許研究捷徑污染實盤

📌 本文件不負責（避免越權）：
- 不定義 L1–L11 流程順序（由 MASTER_CANON / ARCH_FLOW 裁決）
- 不定義策略宇宙內容（由 STRATEGY_UNIVERSE 裁決）
- 不定義風控否決條文（由 RISK_COMPLIANCE 裁決）
- 不定義下單與通道（由 EXECUTION_CONTROL 裁決）
- 不承諾績效、不產生交易方向、不提供自動下單暗示

---

## 1. 治理總則（Hard Gates｜不可動搖）

### 1.1 名詞與地位（不可偷換）
- **Raw Data（原始資料）**：L1 取得之來源資料（官方優先），不可被特徵層改寫  
- **Canonical Data（標準化資料）**：L2 清洗後，具一致欄位與單位  
- **Snapshot（快照）**：L3 固化的市場狀態，可回放  
- **Feature（特徵）**：L4 將資料轉為「可解釋輸出」，不具方向性裁決權  
- **Indicator（指標）**：Feature 的一種（如 MA、RSI），屬於可重算特徵  
- **Factor（因子）**：Feature 的一種，但常用於橫斷面（cross-sectional）或組合層面（如價值/動能/品質）  
- **Structure Output（結構輸出）**：結構分析（例如趨勢段、盤整區、纏論結構、威科夫階段）之「描述性輸出」  
- **Signal（訊號）**：屬於策略層（L8）內部的「條件判斷結果」，不可在本文件定義為 Feature  
- **Strategy（策略）**：L8 的建議/假設生成器，不得直連下單  
- **Order（委託）**：L11 才能生成；須 Human + Risk PASS Token

### 1.2 四大禁令（Forbidden）
1) **禁止把 Feature 寫成「買/賣/多/空」**  
2) **禁止把 Feature 當作策略**（Feature 只能被引用、不能自行形成交易結論）  
3) **禁止 Feature 產生/暗示下單**（不得出現「直接買進/直接賣出」）  
4) **禁止跳過 Evidence/Regime/Risk/Governance**（任何 Feature 若需決策裁決，必須走 L5–L10）

### 1.3 Evidence First 與可回放
- Feature 產出必須引用：  
  - `snapshot_ref`（L3）  
  - `data_provenance_ref`（來源追溯）  
  - `feature_version_ref`（版本）  
- 缺上述任一：視為 **不可用特徵（Feature Invalid）**，不得進入 L5 Evidence Bundle

---

## 2. 特徵分層（Feature Layering｜與 Canonical Flow 對齊）

本文件的 Feature 定義以 L4 為中心，但必須與 L1–L11 對位：

- **L1–L2**：決定資料是否可被合法使用（來源/清洗/一致性）  
- **L3**：決定 Feature 計算的時間點與狀態（Snapshot 固化）  
- **L4**：產生 Feature / Indicator / Factor / Structure Output  
- **L5**：Feature 被組裝成 Evidence（含衝突處理與完整性檢查）  
- **L6**：Regime 會引用部分 Feature 但仍屬「狀態裁決」  
- **L7**：Risk/Compliance 可否決使用某些 Feature（例如資料延遲、不可追溯、制度限制）  
- **L8**：策略引用 Feature 形成條件，但策略不得「把 Feature 直接當作訊號」繞過 Evidence/Regime  
- **L9–L10**：治理與人類裁決需可視化 Feature 的來源與解釋  
- **L11**：不得直接接收 Feature 作為下單參數（必須透過 Human Approved Intent）

---

## 3. Feature Meta Schema（特徵治理欄位｜不可縮減）

> 本節是 Feature 在治理上的「最小資料結構」。  
> 任何新增 Feature 必須完整填寫；不可只寫名稱與公式。

### 3.1 必填欄位（Mandatory）
- `feature_id`：唯一 ID（不可重複）  
- `feature_name_zh`：中文名稱（必填）  
- `feature_name_en`：英文名稱（可填）  
- `feature_family`：所屬家族（見 §4）  
- `feature_type`：Indicator / Factor / Structure / RiskMetric / QualityMetric / EventTag / Meta  
- `timeframe`：資料頻率（tick/1m/5m/15m/60m/1d/1w/1mo…）  
- `inputs`：輸入欄位（必須可追溯到 DATA_SOURCES 的欄位定義）  
- `calculation`：計算方式（可文字 + 公式；不得只寫「同 XX 指標」）  
- `output`：輸出定義（數值範圍/單位/維度）  
- `interpretation`：可解釋性說明（描述性，不得變成買賣建議）  
- `constraints`：使用限制（資料缺失、交易時段、標的限制、冷啟動期、lookahead 禁止等）  
- `audit_requirements`：審計欄位（至少 snapshot_ref/provenance/version/hash）  
- `provenance`：來源（官方/第三方/內部推導；必須可追溯）  
- `versioning`：版本策略（Only-Add；不可覆寫舊語義）  
- `used_by`：被哪些策略類別/Regime/Risk 引用（引用而非綁死）

### 3.2 禁止欄位（Not Allowed）
- 不得含 `order_action` / `buy` / `sell` / `long` / `short` 作為 output  
- 不得含「直接下單」的描述  
- 不得把策略的 entry/exit 規則寫入 feature（那是 L8 的事）

---

## 4. Feature 家族總覽（Feature Families｜最大完備）

> 這裡不是策略，而是「可被引用的輸出類型」。  
> 每個家族都必須可追溯、可回放、可審計。

### 4.1 價格與報酬（Price & Return）
- 報酬率（log return / simple return）
- 缺口（gap）
- 連續漲跌（streak）
- 震盪幅度（range/true range）
- 位置（相對區間高低）

### 4.2 成交量與金流（Volume & Flow）
- 成交量（volume）
- 成交金額（turnover）
- 均量/量比（volume ratio）
- 量能分佈（volume profile：如可得）
- 大單/小單（若資料合法可得）

### 4.3 波動與風險度量（Volatility & Risk Metrics）
- ATR、Historical Vol、Parkinson Vol（若適用）
- 下行波動、偏態、峰度（研究用，需標註）
- VaR/ES（組合層面，需政策與審計）

### 4.4 趨勢類（Trend）
- MA/EMA/WMA（各期）
- MACD 類（線/柱/背離描述）
- ADX / DMI 類
- 多均線排列（例如 GMMA 類「群組特徵」：只輸出排列/收斂/擴張的描述性量化，不輸出買賣）

### 4.5 動能類（Momentum）
- ROC、RSI、Stoch、CCI
- 多周期動能向量（研究用）
- 相對強弱（RS：相對於基準）

### 4.6 均值回歸與極端（Mean Reversion & Extremes）
- z-score（以窗口統計）
- Bollinger band 位置/寬度
- percentile rank（分位數）

### 4.7 結構與型態（Structure & Pattern）
- 支撐/壓力（以算法定義的區域/強度/距離）
- 盤整區（consolidation box：區間、寬度、持續時間）
- 突破/假突破的「事後描述」特徵（不可當訊號）
- K 線型態分類（僅作描述；嚴禁直接給買賣建議）

### 4.8 市場微結構（Market Microstructure｜若資料可得）
- 點差（spread）、深度（depth）、委買委賣失衡（imbalance）
- 成交衝擊 proxy（impact proxy）

### 4.9 Regime 相關特徵（Regime Features）
- 趨勢/震盪/高波動/低流動性等狀態的「觀測量」
- Regime engine 的輸入候選（但 Regime 的裁決仍在 L6）

### 4.10 事件與消息標籤（Event & News Tags）
- 財報日/法說/重大公告窗口（以官方日曆或公告可追溯）
- 停牌/處置/分盤/注意股狀態（以 TWSE_RULES/官方公告追溯）
- 宏觀事件（僅標籤，不裁決方向）

### 4.11 基本面因子（Fundamental Factors｜以可追溯資料為前提）
- 估值：PE/PB/EV/EBITDA（若資料可得且定義清楚）
- 品質：ROE/ROA/毛利率/營益率
- 成長：營收 YoY/MoM、EPS 成長
- 財務安全：負債比、流動比、利息保障倍數
- 需標註：資料頻率、公告延遲、可用時點（避免 lookahead）

### 4.12 籌碼與法人（Institutional / Positioning｜資料合法可得才納入）
- 三大法人買賣超、持股比例變化（以官方/可信來源追溯）
- 融資融券、借券、當沖占比（以官方來源追溯）
- 必須標註：發布延遲、可用時間、落後性（禁止偷看未來）

### 4.13 期貨/選擇權衍生（Derivatives Features｜TAIFEX）
- 期貨基差、正逆價差狀態（描述性）
- Put/Call Ratio、OI 變化（描述性）
- 波動率指標（若資料可得）
- 不得直接輸出「做多/做空」

### 4.14 風控/合規特徵（Compliance/Risk Features）
- 可交易狀態（是否停牌/分盤/處置/禁買賣等）
- 下單限制（交易時段/價格幅度/數量限制的「狀態」）
- 這些特徵是 Gate 的輸入，不是策略訊號

---

## 5. Feature → Evidence（L4 → L5）組裝規範（避免特徵信號化）

### 5.1 Evidence Item 的最小形狀（概念）
- `evidence_item_id`
- `feature_refs[]`（引用哪些 feature）
- `claim`（可驗證的描述性主張，不得是下單指令）
- `supporting_metrics`（可量化佐證）
- `confidence`（若有，必須可追溯算法與版本）
- `conflicts_with[]`（衝突 evidence 參照）
- `provenance_map_ref` / `snapshot_ref` / `hash` / `version_ref`

### 5.2 嚴禁「特徵即證據即訊號」
- Feature 只能是 Evidence 的「材料」，不是結論  
- Evidence 也不是策略建議  
- 策略建議必須在 L8，且必須引用 Evidence/Regime/Risk 結果

---

## 6. Feature 計算的資料治理（Source / Timing / Lookahead 防線）

### 6.1 官方優先與來源追溯（對齊 DATA_SOURCES）
- 所有輸入欄位必須能對應到 DATA_SOURCES 的 source_id / 欄位定義
- 禁止以非官方網站裁決制度狀態（制度以官方/規則彙編裁決）

### 6.2 Timing Policy（可用時點）
每個 Feature 必須標註：
- `asof_time`：此輸出在時間上何時成立  
- `publish_delay`：資料發布延遲（例如財報、法人籌碼）  
- `effective_time`：可合法用於決策的最早時間（避免偷看未來）

### 6.3 Lookahead 禁止（Hard Gate）
- 回測/研究/模擬不得使用「當時不可能知道」的值
- 任何違反：必須在審計中標記 `SYS-PROV` 或 `SYS-AUDIT` 類違規，並阻斷進入 L5/L6/L7

---

## 7. Feature 審計與回放（Audit / Replay）規範（無紀錄=未發生）

### 7.1 Feature Audit Fields（最小集合）
- `correlation_id`
- `snapshot_ref`
- `feature_id`
- `inputs_hash`
- `output_hash`
- `feature_version_ref`
- `data_provenance_ref`
- `compute_env_ref`（LOCAL_ENV 對位）
- `timestamp_utc`

### 7.2 Replay 要求（同輸入同輸出）
- 相同 snapshot_ref + 相同 version_ref + 相同 inputs_hash  
  → 必須產生相同 output（容許浮點誤差需明示規格）

---

## 8. Feature 與 Risk/Compliance 的互動（可否決）

### 8.1 Risk/Compliance 可以否決 Feature 使用的典型情境
- 資料來源不可追溯（SYS-PROV）
- 版本不一致（SYS-VERSION）
- 審計缺失（SYS-AUDIT）
- 資料延遲或不在可用時點（CMP/ SYS 類）
- 制度狀態禁止交易（CMP-*：停牌/分盤/處置等）

### 8.2 特徵不可「反向否決」風控
- Feature 只能提供材料，不能辯護放行  
- 風控否決不可被 Feature/策略/人類覆寫（對齊 RISK_COMPLIANCE）

---

## 9. UI 呈現義務（Feature 層必須可解釋）

> UI 詳規在 UI_SPEC；本節定義特徵層必交付 UI 的最小資訊。

UI 必須可呈現：
- feature_name_zh / feature_id
- 輸入來源（provenance）
- snapshot 時點
- 計算窗口與參數（若有）
- 輸出值與單位
- 限制/禁用原因（若不可用）
- 版本引用（feature_version_ref）

禁止：
- UI 把 feature 顯示成「直接買/賣」按鈕或暗示語  
- 用模糊詞掩蓋資料延遲/不可追溯

---

## 10. 變更治理（Only-Add）與版本控管（對齊 VERSION_AUDIT）

### 10.1 Feature 版本策略（不可覆寫）
- 新增 feature：新增 feature_id（或在同 feature_id 下新增 version_ref，但不得改舊語義）
- 修改定義：只能以新版本追加，不得覆寫舊文件段落

### 10.2 Change Ledger（變更帳本最小欄位）
- `change_id`
- `changed_feature_ids[]`
- `reason`
- `approver`
- `effective_time`
- `backward_compatibility_note`（如何不破壞舊回放）

---

## 11. Feature 索引主表（Index Tables｜最大完備骨架）

> 本節提供「可擴充的主表骨架」。  
> 你可以先用這個骨架，逐步把特徵填滿；但骨架本身就是治理必要內容（不可省略）。  
> 若特徵數量龐大，允許拆成多段 Part 1/2/3…（Only-Add）。

### 11.1 Core Technical Indicators（技術指標核心組）
| feature_id | feature_name_zh | family | timeframe | inputs（概念） | output（概念） | constraints（概念） |
|---|---|---|---|---|---|---|
| F-PRICE-RET-001 | 報酬率（simple return） | Price&Return | 任意 | close | r_t | 需定義窗口/基準點 |
| F-PRICE-RET-002 | 對數報酬率（log return） | Price&Return | 任意 | close | log r_t | 同上 |
| F-VOL-TR-001 | True Range | Volatility | 任意 | high/low/close | TR | 需有前一收盤 |
| F-VOL-ATR-001 | ATR（平均真實波幅） | Volatility | 任意 | TR | ATR(n) | 冷啟動期 n |
| F-TREND-MA-001 | 簡單移動平均 MA | Trend | 任意 | close | MA(n) | 冷啟動期 n |
| F-TREND-EMA-001 | 指數移動平均 EMA | Trend | 任意 | close | EMA(n) | 冷啟動期 n |
| F-MOMO-RSI-001 | RSI | Momentum | 任意 | close | RSI(n) | 冷啟動期 n |
| F-MOMO-ROC-001 | ROC | Momentum | 任意 | close | ROC(n) | 冷啟動期 n |
| F-MR-BB-001 | 布林通道位置 | MeanReversion | 任意 | close | position | 需定義上下軌算法 |

### 11.2 Structure Outputs（結構輸出組｜描述性）
| feature_id | feature_name_zh | family | timeframe | inputs | output（描述性/量化） | constraints |
|---|---|---|---|---|---|---|
| F-STR-SR-001 | 支撐/壓力距離 | Structure | 任意 | price series | 距離/強度 | 需定義算法；不得變成買賣訊號 |
| F-STR-RANGE-001 | 盤整箱體寬度/持續時間 | Structure | 任意 | price series | width/duration | 需定義箱體識別規則 |
| F-STR-BREAKDESC-001 | 突破事件描述（事後） | Structure | 任意 | price/volume | breakout_desc | 僅描述，不可當入場指令 |

### 11.3 Fundamental Factors（基本面因子組｜需公告延遲）
| feature_id | feature_name_zh | family | timeframe | inputs | output | constraints |
|---|---|---|---|---|---|---|
| F-FUND-VAL-PE-001 | 本益比 PE | Fundamental | 季/年 | EPS/price | PE | 必須標註公告延遲與可用時點 |
| F-FUND-VAL-PB-001 | 股價淨值比 PB | Fundamental | 季/年 | BVPS/price | PB | 同上 |
| F-FUND-QUAL-ROE-001 | ROE | Fundamental | 季/年 | net income/equity | ROE | 同上 |

### 11.4 Chips / Institutional（籌碼/法人｜需追溯）
| feature_id | feature_name_zh | family | timeframe | inputs | output | constraints |
|---|---|---|---|---|---|---|
| F-CHIP-INS-001 | 三大法人買賣超 | Institutional | 日 | official net buy/sell | net | 必須標註發布延遲 |
| F-CHIP-MARGIN-001 | 融資融券餘額變化 | Institutional | 日 | margin balance | delta | 必須標註可用時點 |

### 11.5 Derivatives（期權衍生｜TAIFEX）
| feature_id | feature_name_zh | family | timeframe | inputs | output | constraints |
|---|---|---|---|---|---|---|
| F-DER-BASIS-001 | 期貨基差狀態（描述性） | Derivatives | 日/分 | spot/future | basis_desc | 不得輸出多空指令 |
| F-DER-PCR-001 | Put/Call Ratio | Derivatives | 日 | options volume/OI | PCR | 必須標註資料來源與延遲 |

### 11.6 Compliance/Status Features（合規/狀態特徵）
| feature_id | feature_name_zh | family | timeframe | inputs | output | constraints |
|---|---|---|---|---|---|---|
| F-CMP-TRADEABLE-001 | 可交易狀態旗標 | Compliance | 即時/日 | TWSE/券商狀態 | tradeable_flag | 以官方/券商狀態裁決 |
| F-CMP-SESSION-001 | 交易時段狀態 | Compliance | 即時 | 時段規則 | session_state | 以 TWSE_RULES/官方入口裁決 |

---

## 12. STRATEGY_UNIVERSE 引用規則（Feature 引用，而非重複定義）

### 12.1 策略文件必須引用 feature_id
- 任何策略/模組若使用特徵，必須列出 `feature_refs[]`
- 禁止在策略內重新定義特徵公式（除非以「引用本文件」方式指向同一 feature_id）

### 12.2 Feature 與策略的責任切分
- Feature：定義可重算輸出與解釋  
- Strategy：定義如何在特定 Regime 下組合 Evidence、形成建議（仍不得下單）  
- Risk：定義可否決條件（不可被策略反推）

---

## 13. Mermaid｜Feature → Evidence → Strategy（治理防線示意）

```mermaid
flowchart TB
  L3[Snapshot] --> L4[Feature Engine]
  L4 -->|feature_refs + audit| L5[Evidence Bundle]
  L5 --> L6[Regime Engine]
  L6 --> L7[Risk/Compliance Gate]
  L7 -->|PASS| L8[Strategy Proposal]
  L7 -->|VETO| STOP[STOP + Audit]
  L8 --> L9[Governance Gate]
  L9 --> L10[Human Decision]
  L10 --> L11[Execution Control]
14. Only-Add 演進規則（本文件專屬）
允許新增：

新 feature_id（新增家族/新增市場資料/新增結構輸出）

新欄位（增加審計、增加 provenance、增加 UI 可解釋資訊）

新索引分段（Part 1/2/3…）

禁止：

刪除既有 feature 定義或改寫其語義

把 feature 變成買賣建議或下單指令

以「簡化」為由移除 provenance/audit/version 字段

以研究方便為由忽略公告延遲與可用時點

15. 封版宣告（不可更改）
TAITS 的 Feature/Factor/Indicator 只負責「可追溯的描述性輸出」。
特徵不是訊號、不是策略、不是下單；任何越界皆屬治理違規。

（STRATEGY_FEATURE_INDEX｜最大完備・治理對齊版 v2025-12-19 完）
