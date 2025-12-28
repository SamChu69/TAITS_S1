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
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：STRATEGY_UNIVERSE / ARCH_FLOW / RISK_COMPLIANCE / VERSION_AUDIT / UI_SPEC / DATA_SOURCES / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減、不可覆寫、不可改寫既有語義、不可弱化邊界）  
核心宣告：Feature ≠ Signal ≠ Strategy ≠ Order（特徵非訊號、非策略、非下單）  

---
---

# Addendum 2025-12-27｜Only-Add：B+「子級標籤」法律定位 × Index Gate 對齊 × 引用/裁決字串助記化（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219.md（doc_key：STRATEGY_FEATURE_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：AI_GOV（A+）＋Index Gate（DOCUMENT_INDEX）＋MASTER_ARCH（A）＋MASTER_CANON（A）  
> 口徑對齊：  
> - DOCUMENT_INDEX｜Addendum 2025-12-27（治理等級 bucket 與裁決規則）  
> - DOCUMENT_INDEX｜Addendum 2025-12-27-B（B+/C+ 子級標籤定義：Label ≠ Governance Grade）  
> - MASTER_CANON｜Addendum 2025-12-27（S 為 Label；治理等級回歸 Index）  
> - GOVERNANCE_GATE_SPEC｜Addendum 2025-12-27（裁決字串助記化定位）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（建議新增條目：`VA-METADATA_FIX-20251227-0009`）  
> 目的：在不改寫本文件任何既有治理條款與內容的前提下，消解「治理等級：B+」可能被誤讀為新治理層級之歧義；將本文件之治理身份、引用合法性、裁決序列字串全面對齊 DOCUMENT_INDEX；確保 Freeze v1.0 下跨文件引用一致、可稽核、可回放。

---

## A0. B+ 的法律定位（Label ≠ Governance Grade｜不可誤讀）

### A0.1 統一裁決：B+ 僅為子級顯示標籤（Sub-Label）
本文件檔頭與正文若出現「治理等級：B+」或等價字樣，其唯一合法解讀為：

- **B+ 為子級顯示標籤（Sub-Label），用於描述「B 等級文件中的較高嚴格度/較高完備度定位」**  
- **B+ 不構成新的治理等級 bucket**；治理覆蓋規則仍為：**A+ > A > B > C**  
- 本文件在治理等級 bucket 上，一律視為 **B（ACTIVE）**，並以 DOCUMENT_INDEX 的 Authoritative Index 表格裁決為準

> 兼容處理（不改原文）：本文件既有「B+」字樣保留；其法律效力由本 Addendum 限定為 Sub-Label。

### A0.2 本文件的「有效性/ACTIVE」裁決來源（Index Gate Only）
- 本文件是否為 ACTIVE、其 doc_key、版本日期、治理等級 bucket 之裁決來源：**僅能且必須為 DOCUMENT_INDEX 表格**  
- 本文件任何內文描述（含快照清單/平行參照）不得用以覆蓋 Index Gate 裁決

---

## A1. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）

本文件內若出現任何「裁決優先序」或箭頭序列（例：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`）：
- 一律視為閱讀/操作助記（Mnemonic）  
- **不得**被用作重排覆蓋規則或重新分配裁決權  
- 如與 DOCUMENT_INDEX §3（覆蓋規則）或 §6（衝突裁決程序）產生張力：**一律回到 DOCUMENT_INDEX**（不可跳步）

---

## A2. 引用合法性最小格式（Minimum Legal Citation Format）

為確保「新對話可展開」且不越權，本文件在被引用/引用他文時，最小引用格式必須包含：

- 文件名（完整檔名）  
- doc_key  
- 版本日期（version_date）  
- 章節定位（section / heading path）

缺任一欄位 → 一律視為「未引用」→ 不得裁決性輸出（尤其不得推導策略/下單語義）。

建議固定引用標頭（可直接貼用）：
```text
〔TAITS 引用標頭｜Freeze v1.0｜Only-Add〕
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0009
〔/TAITS 引用標頭〕
```

---

## A3. 本文件的硬邊界再宣告（不新增制度；僅重申合法解讀）

本 Addendum 僅為避免誤讀與越權：  
- **Feature ≠ Signal ≠ Strategy ≠ Order** 為本文件既有硬邊界（原義不變）  
- 本文件任何「方法論」段落皆必須被解讀為 Feature 層的描述性輸出規範，不得被引用為策略規則或下單觸發器  
- 任何嘗試將 Feature 直接映射成交易方向/行為（買賣、進出、長短、下單）均屬治理違規（依本文件既有違規碼與上位母法裁決）

---

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）

> 【文件閱讀與 Canonical 對位指引（Only-Add）】
>
> 本文件主體內容定義 STRATEGY_FEATURE_INDEX 之特徵分類、語義與治理規範。
> 自文件最末之「Appendix Y｜STRATEGY_FEATURE_INDEX × MASTER_CANON × STRATEGY_UNIVERSE 同步對位附錄」起，
> 為依據 MASTER_CANON 與 STRATEGY_UNIVERSE（Part 8 新增策略模板）
> 所新增之 Canonical 對位與接口一致性補充。
>
> 本指引僅作閱讀與治理定位說明，
> 不構成對主文條款之修改，
> 裁決優先序仍依 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為準。

---

## 0. 文件定位（最大完備｜全知識自洽）

本文件是 TAITS 的 **「策略特徵與因子索引」**，其定位不是列清單而已，而是提供一份**即使新對話只讀這一份，也能合法展開策略研究所需的「語義憲法＋知識索引」**。

本文件同時滿足兩個目標：

1) **治理封頂（Hard Governance）**  
- 明確定義 Feature 的法定意義  
- 明確定義 Feature 的合法使用路徑（Feature→Evidence→Regime→Risk→Strategy→Human→Execution）  
- 明確列出禁止事項與違規判定（可被審計、可被阻斷）

2) **全知識自洽（Knowledge Self-Contained）**  
- 將常用方法論（GMMA、顧比倒數線、威科夫、鮑迪克纏論等）落在 Feature 層，並以「描述性輸出」表達  
- 提供 Feature → Evidence 組裝方式 → Regime 對應 → Strategy 適用邏輯 的展開規則  
- 提供「備註」讓新對話能清楚理解每類 Feature 常用到的資料、指標、結構語義與常見陷阱（lookahead、資料延遲、過度信號化）

📌 本文件不負責（避免越權）：  
- 不定義 Canonical Flow 順序（由 MASTER_CANON / ARCH_FLOW 裁決）  
- 不定義否決門檻與理由碼全集（由 RISK_COMPLIANCE 裁決）  
- 不定義 UI 外觀（由 UI_SPEC 裁決）  
- 不輸出交易方向、不輸出下單指令、不承諾績效  

---

## 1. Feature 的法定定義（不可改寫）

### 1.1 Feature 是什麼（Legal Definition）
Feature（特徵/因子）是：

> 對市場、標的、參與者行為或環境狀態的「可量化/可描述」表徵，  
> 其輸出必須是**描述性（Descriptive）**，不可被直接解釋為方向或行動。

Feature 的必備屬性：
- **可追溯（Provenance）**：知道來自哪個資料源、哪個版本、哪個時間戳  
- **可回放（Replayable）**：同一資料/版本輸入可重建同一輸出  
- **可審計（Auditable）**：能被記錄到審計物，無紀錄視為不存在  
- **非決策（Non-Decisive）**：不得直接產生買賣建議或行為指令  

### 1.2 Feature 不是什麼（Hard Negation）
Feature 永遠不是：
- 交易訊號（Signal）  
- 策略（Strategy）  
- 建議（Recommendation）  
- 指令（Instruction）  
- 下單觸發器（Order Trigger）  

---

## 2. Feature ≠ Signal ≠ Strategy ≠ Order（治理鐵律）

### 2.1 層級隔離（Layer Isolation｜硬邊界）
唯一合法路徑如下（不可跳步）：

Feature（L4輸出）
→ Evidence（L5）
→ Regime（L6）
→ Risk/Compliance Gate（L7）
→ Strategy Proposal（L8）
→ Governance Gate（L9）
→ Human Decision（L10）
→ Execution（L11）

任何違反此路徑的行為，均屬治理違規：
- `GOV-FEATURE-JUMP`：Feature 越級輸出到 Strategy/Execution  
- `GOV-FEATURE-SIGNALIZE`：Feature 被信號化（用方向性語言呈現或被當作買賣條件）  
- `GOV-FEATURE-OVERRIDE`：Feature 試圖覆寫 Risk/Compliance 或 Human 裁決  

---

## 3. Feature 的合法用途（Only Legal Uses）

Feature 只能用於：
1) 組成 Evidence Bundle 的元素（L5）  
2) 協助 Regime 判定（作為狀態描述輸入，不是方向輸入）（L6）  
3) 約束策略「適用性」與「可信度條件」（L8：策略是否可被提出，而非是否要交易）  
4) 提供審計/解釋/回放素材（L10 UI 解釋與 L11 回放）  

Feature 永遠不能用於：
- 單一 Feature 直接下結論（例如「GMMA 轉多＝買」）  
- 以 Feature 單獨形成策略（策略必須是 Evidence＋Regime＋Risk＋Human 的產物）  
- 以 Feature 作為績效辯護或績效承諾依據  

---

## 4. Feature 禁止事項（Hard Prohibition Blacklist）

### 4.1 語義違規（Semantic Violations）
- 將 Feature 的數值/狀態直接翻譯成「買/賣/進/出」  
- 使用方向性詞彙描述 Feature 輸出（如：看多/看空/必漲/必跌/進場/出場）  
- 在 Feature 層做「訊號強弱排行」並當作下單依據  

### 4.2 技術濫用（Technical Abuse）
- 以 Feature 對齊績效做超參數最佳化（Optimization / Overfitting）  
- 以 Feature 的單一結果做回測歸因（Feature Attribution ≠ Profit Attribution）  
- 以 Feature 作為模型的單一損失目標（導致 Feature 變成信號）

### 4.3 治理違規（Governance Violations）
- Feature 直接輸出到 Execution  
- Feature 繞過 Evidence / Regime / Risk Gate  
- 缺審計物仍允許 Feature 參與決策鏈  
- Feature 被以 UI 或文字暗示為「推薦行為」  

---

## 5. Feature 的標準資料結構（Feature Meta Schema｜最大完備）

> 本節為工程與治理共用：任何 Feature 必須能被「結構化」描述。  
> 可擴充，不可縮減。

### 5.1 FeatureMeta（最小必填）
- `feature_id`：唯一 ID（建議：`FTR.<domain>.<family>.<name>.<version>`）  
- `feature_name_zh`：中文名  
- `feature_name_en`：英文名（如有）  
- `domain`：資料面向（TECH/FUND/FLOW/SENT/MACRO/RISK/STRUCT/EXEC）  
- `family`：家族（Trend/Momentum/Volatility/Structure/Valuation/Quality/Growth/Liquidity/Event…）  
- `methodology_tags`：方法論標籤（GMMA/Wyckoff/ChanLun_Bodick…可多選）  
- `timeframe`：適用週期（Tick/1m/5m/1h/1D/1W/1M…）  
- `inputs`：所需原始欄位（對應 DATA_SOURCES 的欄位命名或 Canonical Field）  
- `lookahead_policy`：前視禁令聲明（必填）  
- `data_latency`：資料延遲性（即時/延遲/公告延遲/不定期）  
- `output_type`：輸出型態（Scalar/Vector/Label/State/Distribution）  
- `output_semantics`：描述性語義（不得含方向）  
- `quality_checks`：品質檢查（缺值/異常/停牌/分盤）  
- `audit_requirements`：審計要求（hash/provenance/snapshot）  
- `allowed_uses`：允許用途（只能列本文件第3節允許項）  
- `forbidden_uses`：禁止用途（對應第4節）  

### 5.2 FeatureOutput（描述性輸出規範）
Feature 輸出只允許：
- **狀態（State）**：例如「趨勢結構：延續/盤整/破壞」  
- **標籤（Label）**：例如「威科夫階段：A/B/C/D/E」  
- **量化度量（Metric）**：例如「波動率、趨勢強度、分佈偏態」  
- **完整度/信賴度（Completeness/Confidence）**：描述資料與結構完備程度  

🚫 禁止輸出：
- `BUY/SELL/LONG/SHORT/ENTRY/EXIT`  
- `should_trade`（應否交易）  
- `expected_profit`（預期獲利）  

---

## 6. Feature → Evidence 組裝規則（Evidence Assembly Rules｜最大完備）

### 6.1 Evidence 的最低要求（不可弱化）
Evidence Bundle 必須：
- 至少包含 **2 種以上不同 domain** 的 Feature（例如 TECH + FLOW，或 FUND + TECH）  
- 至少包含 **1 個結構/狀態類（STRUCT/REGIME）** 或可替代的狀態描述  
- 必須附帶：
  - `snapshot_ref`（L3 快照）  
  - `provenance_map_ref`（來源追溯）  
  - `version_ref`（文件/政策/模型版本）  

### 6.2 常見 Evidence 組裝模板（可直接展開）
- **趨勢延續型 Evidence**：Trend Structure（TECH/STRUCT）＋ Flow/Liquidity（FLOW/LIQ）＋ Volatility（VOL）  
- **區間盤整型 Evidence**：Range State（STRUCT）＋ Volatility Compression（VOL）＋ Orderflow Balance（FLOW）  
- **基本面價值型 Evidence**：Valuation（FUND）＋ Quality（FUND）＋ Technical Position（TECH）  
- **事件風險型 Evidence**：Event Flag（EVENT）＋ Vol Spike（VOL）＋ Liquidity Stress（LIQ）  

📌 以上模板**不等於策略**，只是 Evidence 的「組裝語法」。

---

## 7. Feature 與 Regime 的對位（Regime Alignment Map）

> Regime 高於策略；Feature 只提供 Regime 判定所需的描述性輸入。

### 7.1 常見 Regime 類型（示意，實際以 Regime Engine 為準）
- Trend（趨勢延續）  
- Range（區間盤整）  
- Transition（結構轉換/趨勢切換）  
- Volatility Shock（波動衝擊）  
- Liquidity Stress（流動性壓力）  
- Event Risk（事件期）  
- Manipulation/Abnormal（異常/失真疑慮）  

### 7.2 Feature → Regime 常見映射（描述性）
- 趨勢結構完整度↑、均線群組有序、波動穩定 → Trend 的候選描述  
- 波動收斂、價格在區間內均值回歸、量能偏低 → Range 的候選描述  
- 波動突增、跳空、點差擴大、深度不足 → Volatility Shock / Liquidity Stress 候選描述  
- 事件密度高、公告窗口內、政策時點 → Event Risk 候選描述  
- 價量嚴重背離、撮合異常、長時間無量 → Abnormal 候選描述  

📌 以上都只是「候選描述」，最終裁決由 Regime Engine 與治理規則決定。

---

## 8. 方法論落地：GMMA / 顧比倒數線 / 威科夫 / 鮑迪克纏論（Feature 層展開）

> 本節是你選 B 的核心：把方法論「降維」成 Feature，並明確禁止信號化。

---

### 8.1 GMMA（顧比多重移動平均線）— Feature 化（非信號）

#### 8.1.1 GMMA 的 Feature 家族
- `FTR.TECH.TREND.GMMA_BAND_STRUCTURE.v1`（GMMA 群組結構）  
- `FTR.TECH.TREND.GMMA_BAND_SPREAD.v1`（群組擴張/收斂幅度）  
- `FTR.TECH.TREND.GMMA_BAND_SLOPE.v1`（群組斜率一致性）  
- `FTR.TECH.TREND.GMMA_LONG_SHORT_RELATION.v1`（短群/長群相對關係）  
- `FTR.TECH.STRUCT.GMMA_PHASE_LABEL.v1`（GMMA 階段標籤：描述性）  

#### 8.1.2 GMMA 輸出語義（只允許描述）
- `band_orderliness`：群組有序程度（0~1）  
- `band_spread_state`：收斂/擴張/中性  
- `slope_consistency`：斜率一致性（0~1）  
- `short_vs_long_relation`：上方/交疊/下方（描述相對位置）  
- `phase_label`：例如「擴張延續/收斂盤整/扭曲轉換」（不得寫「轉多/轉空」）

#### 8.1.3 GMMA 常用 Evidence 組裝（示例）
- Trend Evidence：GMMA 群組有序＋Flow/Liquidity 正常＋波動不失真  
- Range Evidence：GMMA 收斂＋波動收斂＋量能偏低

🚫 GMMA 禁止用法（明文）
- 「短群上穿長群＝買」  
- 「群組擴張＝追」  
- 「顏色變化＝做多做空」  
以上皆屬 `GOV-FEATURE-SIGNALIZE`。

---

### 8.2 顧比倒數線（你提到的「顧比倒數線」）— Feature 化

> 由於市場上「顧比倒數線」存在多種實作版本（不同計算方式/參數），  
> TAITS 在 Feature 層採「語義統一」：只定義輸出語義，不把某一種實作當作唯一真理。  
> （具體公式可在研究層以策略擴充，但不得改寫本語義。）

#### 8.2.1 Feature 家族
- `FTR.TECH.MOMENTUM.GUPPY_COUNTDOWN_STATE.v1`（倒數狀態）  
- `FTR.TECH.MOMENTUM.GUPPY_COUNTDOWN_INTENSITY.v1`（倒數強度/接近程度）  

#### 8.2.2 輸出語義（描述性）
- `countdown_state`：倒數進行中/完成/重置/無效  
- `countdown_progress`：0~1（進度，不代表方向）  
- `intensity`：0~1（強度，不代表建議）

🚫 禁止用法
- 「倒數完成＝買/賣」  
- 「倒數快滿＝必漲/必跌」

---

### 8.3 威科夫操盤法（Wyckoff）— Feature 化（階段/事件，不是方向）

#### 8.3.1 Wyckoff Feature 家族
- `FTR.STRUCT.WYCKOFF.PHASE_LABEL.v1`（A/B/C/D/E 階段標籤）  
- `FTR.STRUCT.WYCKOFF.EVENT_FLAGS.v1`（PS/SC/AR/ST/SOS/LPS…事件旗標）  
- `FTR.STRUCT.WYCKOFF.RANGE_BOUNDARY.v1`（區間邊界與有效性）  
- `FTR.STRUCT.WYCKOFF.SUPPLY_DEMAND_BALANCE.v1`（供需平衡度量）  
- `FTR.STRUCT.WYCKOFF.EFFORT_RESULT_DIVERGENCE.v1`（量價努力/結果背離描述）  

#### 8.3.2 輸出語義（描述性）
- `phase_label`：A~E（不帶多空）  
- `event_flags`：事件集合（僅標記）  
- `range_boundary`：上界/下界/寬度/有效性（描述）  
- `balance_score`：供需偏移度（-1~1 但不得命名為看多看空）  
- `effort_result_div`：背離程度（0~1）

#### 8.3.3 Wyckoff Evidence 組裝（示例）
- Accumulation/Ranging Evidence：Phase B/C + Range 有效 + 量價背離描述 + 流動性正常  
- Distribution/Ranging Evidence：Phase B/C + Range 有效 + 供需偏移描述 + 事件密度

🚫 禁止用法
- 「Phase D＝買」  
- 「SOS 出現＝一定漲」  
- 「LPS＝進場」  
以上皆屬信號化違規。

---

### 8.4 鮑迪克纏論（ChanLun｜Bodick Variant）— Feature 化（結構、段落、背馳描述）

> 纏論在 TAITS 中定位為「結構與判斷體系」，不是單一策略。  
> 在 Feature 層，纏論只能輸出「結構描述」，不允許輸出方向。

#### 8.4.1 ChanLun Feature 家族（核心）
- `FTR.STRUCT.CHANLUN.BI_SEGMENT_STATE.v1`（筆段落狀態：形成/延伸/完成）  
- `FTR.STRUCT.CHANLUN.ZS_CENTER_STATE.v1`（中樞狀態：形成/擴展/破壞/重構）  
- `FTR.STRUCT.CHANLUN.TREND_STAGE_LABEL.v1`（趨勢階段標籤：描述性）  
- `FTR.STRUCT.CHANLUN.DIVERGENCE_SCORE.v1`（背馳程度：0~1）  
- `FTR.STRUCT.CHANLUN.STRUCTURE_COMPLETENESS.v1`（結構完備度：0~1）  
- `FTR.STRUCT.CHANLUN.PIVOT_RELATION.v1`（中樞相對關係：上移/下移/重疊/離散）  

#### 8.4.2 鮑迪克版本（Bodick Variant）備註（治理口徑）
鮑迪克版本通常強調：
- 結構定義更工程化（可標記、可判準、可回放）  
- 對「段落完成/中樞有效/背馳判定」有更嚴格的一致性要求  

TAITS 在 Feature 層採用原則：
- **允許多版本算法並存（Only-Add）**  
- **但必須輸出同一套語義欄位**（如上 Feature 家族）  
- 版本差異只體現在 `method_version` 與 `calculation_notes`，不得改寫語義

#### 8.4.3 ChanLun 輸出語義（描述性）
- `bi_state`：forming/extending/completed（中文可寫：形成/延伸/完成）  
- `zs_state`：forming/expanding/broken/rebuilt（形成/擴展/破壞/重構）  
- `divergence_score`：0~1（背馳程度，不是反轉信號）  
- `structure_completeness`：0~1  
- `pivot_relation`：上移/下移/重疊/離散（描述相對關係）

🚫 禁止用法
- 「背馳＝買/賣」  
- 「中樞破壞＝必跌」  
- 「筆完成＝進場」  
以上皆屬 `GOV-FEATURE-SIGNALIZE`。

---

## 9. Feature 全域分類樹（Taxonomy Tree｜最大完備）

> 這是新對話「如何展開」的地圖。  
> 每個 Family 都給出：定義、常用方法論、常見輸入、常見輸出語義、常見陷阱。

---

### 9.1 TECH｜技術面（Technical）
#### A) Trend（趨勢結構）
- 定義：描述趨勢的「結構與延續性」，非方向  
- 常用方法論：GMMA、均線群組、趨勢線結構、結構斜率一致性  
- 典型輸入：close/high/low/open/volume、均線序列  
- 輸出語義：有序度、斜率一致性、延續/盤整/轉換標籤  
- 常見陷阱：把「穿越」直接當買賣信號

#### B) Momentum（動能）
- 定義：描述加速度/動量狀態  
- 常用方法論：動能振盪、倒數線狀態、動量分解（描述）  
- 輸出語義：強度、過熱程度、衰減程度（不可叫多空）  
- 陷阱：把超買超賣直接當方向

#### C) Volatility（波動）
- 定義：描述不確定性、波動程度、波動型態  
- 常用：ATR/歷史波動/波動收斂擴張型態  
- 輸出語義：波動水平、收斂/擴張狀態、極端標記  
- 陷阱：波動高≠可賺；波動低≠安全（需配合流動性與制度）

#### D) Structure（結構）
- 定義：描述區間、型態、中樞、段落、階段  
- 常用：威科夫階段、纏論結構、型態識別（描述）  
- 輸出語義：階段標籤、區間有效性、中樞狀態、完備度  
- 陷阱：把「形態名稱」等同策略與勝率

---

### 9.2 FUND｜基本面（Fundamental）
#### A) Valuation（估值）
- 定義：描述相對估值狀態（便宜/昂貴只能作描述性區間，不是買賣）  
- 常用：本益比分位數、股價淨值比分位數、殖利率分位數  
- 重要治理：公告延遲、資料可用時點、避免 lookahead  
- 陷阱：用事後財報做回測推論（典型前視）

#### B) Quality（品質）
- 定義：描述財務品質（穩健/惡化）  
- 常用：毛利率/營益率/ROE/現金流品質（描述）  
- 陷阱：用單一季度劇烈變動作結論

#### C) Growth（成長）
- 定義：描述成長/衰退速度與穩定性  
- 常用：YoY/MoM 變化率、趨勢穩定度  
- 陷阱：季節性與基期效應造成誤判

#### D) Risk（財務風險）
- 定義：描述槓桿、償債、營運風險（描述性）  
- 陷阱：把風險指標當作做空信號（仍需 Regime/Risk Gate）

---

### 9.3 FLOW｜籌碼/交易行為（Flow / Positioning）
#### A) Participation（參與度）
- 定義：描述參與者活躍程度  
- 常用：成交量結構、量能分佈、換手率  
- 陷阱：量大≠安全；量小≠不可交易（需配合點差/深度）

#### B) Institutional/Dealer（法人/大戶）
- 定義：描述資金行為，不等於方向  
- 治理：資料延遲與可得性（多為 T+1 或更慢）  
- 陷阱：把法人買超直接當買入指令

#### C) Liquidity（流動性）
- 定義：描述點差、深度、成交可行性  
- 常用：委買委賣深度、點差、成交量門檻  
- 治理：此類特徵與 RISK_COMPLIANCE 強耦合（可能觸發 VETO/RETURN）

---

### 9.4 EVENT｜事件/消息（Event / News / Calendar）
- 定義：描述事件存在與強度，不做方向判斷  
- 常用：重大公告旗標、事件密度、政策時點、財報窗口  
- 治理：事件期可直接升級為風控禁入條件（由 RISK_COMPLIANCE 裁決）  
- 陷阱：把消息情緒當作方向信號

---

### 9.5 MACRO｜宏觀（Macro）
- 定義：描述宏觀環境（利率/匯率/景氣）  
- 治理：多為低頻、延遲資料，僅作 Regime 背景  
- 陷阱：用宏觀單一指標對短線交易下結論

---

## 10. Feature → Strategy 的「展開備註」規則（你要的「清楚」）

> 本節提供「新對話如何展開」：不是告訴你買賣，而是告訴你每種策略家族通常會用到哪些 Feature、怎麼組裝 Evidence、怎麼對位 Regime。

---

### 10.1 Trend（趨勢類策略）常用 Feature 備註
- 常見 Feature：
  - GMMA 群組結構（有序度/收斂擴張）
  - 趨勢完整度（結構完備度）
  - 波動狀態（避免極端波動失真）
  - 流動性狀態（點差/深度）
- Evidence 組裝：
  - Trend Structure（TECH/STRUCT）＋ Vol（VOL）＋ Liquidity（LIQ）
- Regime 對位：
  - Trend / Transition（可用）
  - Volatility Shock / Liquidity Stress（通常禁入或降級，依 Risk）
- 常見陷阱：
  - 把「均線穿越」當信號
  - 忽略流動性造成滑價與撤單風險

---

### 10.2 Mean Reversion（均值回歸/區間）常用 Feature 備註
- 常見 Feature：
  - Range 邊界有效性（STRUCT）
  - 波動收斂（VOL）
  - 供需平衡（Wyckoff balance）
- Evidence 組裝：
  - Range State（STRUCT）＋ Vol Compression（VOL）＋ Flow Balance（FLOW）
- Regime 對位：
  - Range（可用）
  - Trend（多半不適用，回到 Regime 判定）
- 陷阱：
  - 在趨勢期硬做回歸（違反 Regime 高於策略）

---

### 10.3 Breakout（突破）常用 Feature 備註
- 常見 Feature：
  - 結構轉換標籤（Transition）
  - 量價努力/結果背離（Wyckoff）
  - 波動擴張（VOL）
  - 流動性與點差（LIQ）
- Evidence 組裝：
  - Transition（STRUCT）＋ Effort/Result（FLOW/STRUCT）＋ Vol Expansion（VOL）
- Regime 對位：
  - Transition（可用，但通常風控更嚴）
- 陷阱：
  - 把單根長紅/長黑當突破
  - 忽略分盤/處置等制度（TWSE_RULES 可能觸發）

---

### 10.4 Fundamental Tilt（基本面傾斜/因子）常用 Feature 備註
- 常見 Feature：
  - Valuation 分位數（FUND）
  - Quality 指標（FUND）
  - Growth 穩定性（FUND）
  - 技術位置（TECH Position）
- Evidence 組裝：
  - Valuation＋Quality＋Technical Position（避免完全脫離交易結構）
- Regime 對位：
  - 多用於中長週期；短線只作背景，不可取代短週期風控
- 陷阱：
  - lookahead（公告延遲）
  - 用財報「事後已知」資料做回測歸因

---

### 10.5 Structure-Based（結構體系：威科夫/纏論）常用 Feature 備註
- 常見 Feature：
  - Wyckoff Phase/Event Flags
  - ChanLun 中樞/段落狀態、完備度、背馳程度（描述）
- Evidence 組裝：
  - 結構狀態（STRUCT）＋ 波動/流動性（VOL/LIQ）＋ 交易行為（FLOW）
- Regime 對位：
  - Range/Transition/Trend 均可能，但需明確 Regime Label
- 陷阱：
  - 把背馳當反轉指令
  - 結構判定不一致（需版本一致與回放）

---

## 11. Feature 的審計/回放要求（Feature-Level Audit）

每個 Feature 的計算與使用必須留下：
- `correlation_id`（串起一次流程）  
- `snapshot_id`（對應 L3）  
- `feature_id` / `feature_version`  
- `input_hash` / `output_hash`  
- `provenance_map_ref`  
- `quality_state`（資料品質狀態）  
- `used_in_evidence`（是否被納入 Evidence）  
- `rejected_reason_codes`（若未納入，必填原因）  

📌 無審計＝不存在（治理語義）

---

## 12. Feature 的 Only-Add 演進規則（更嚴）

允許新增：
- 新 Feature  
- 新 family  
- 新 methodology_tags  
- 新 output 欄位（不得刪舊欄位）

禁止：
- 改寫既有 Feature 的 output_semantics  
- 將描述性輸出改成方向性輸出  
- 合併 Feature 造成語義模糊  
- 任何「為了簡化」而刪減既有治理條文  

---

## 13. 終極治理宣告（不可改寫）

> Feature 的存在，是為了把世界描述清楚，  
> 不是為了讓系統更容易下決策。  
> 只要 Feature 被用來「直接做交易」，它就已經被用錯了。

---

（STRATEGY_FEATURE_INDEX｜全知識自洽最大完備版 v2025-12-19 完）

# TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219
doc_key：STRATEGY_FEATURE_INDEX  
治理等級：B+（Feature Governance & Semantic Boundary Charter｜全知識自洽最大完備版）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（特徵層治理封頂＋可展開知識索引，Only-Add 演進）  
版本日期：2025-12-19  
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

（STRATEGY_FEATURE_INDEX｜Part 2：附錄A v2025-12-19 完）

# TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219
doc_key：STRATEGY_FEATURE_INDEX  
治理等級：B+（Feature Governance & Semantic Boundary Charter｜全知識自洽最大完備版）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（特徵層治理封頂＋可展開知識索引，Only-Add 演進）  
版本日期：2025-12-19  
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

（STRATEGY_FEATURE_INDEX｜Part 3：附錄B v2025-12-19 完）

# TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219
doc_key：STRATEGY_FEATURE_INDEX  
治理等級：B+（Feature Governance & Semantic Boundary Charter｜全知識自洽最大完備版）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（特徵層治理封頂＋可展開知識索引，Only-Add 演進）  
版本日期：2025-12-19  
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
  domain: "TECH"                     # TECH/FUND/NEWS/MACRO/MKT/STRUCT/LIQ/ORDERFLOW/RISK/SYS/EVENT
  family: "TREND"                    # 族群分類：TREND/MOMENTUM/VOL/LIQ/STRUCT/VALUATION/QUALITY/...
  subfamily: "GMMA"                  # 子族群：GMMA/WYCKOFF/CHANLUN_BODICK/...
  description: >
    描述長短期均線群之間的擴散程度，用於刻畫趨勢有序度與動能狀態，
    僅輸出連續數值，不輸出買賣方向。
  output_semantics: "ratio_non_directional"  # 必須是描述性語義
  unit: "ratio"
  value_type: "float"                # float/int/bool/category/struct
  value_range: "[0, +inf)"
  default_timeframe: "D"             # 1m/5m/15m/60m/D/W/M
  computation:
    formula_summary: "spread = mean(abs(short_group - long_group))/price"
    lookahead_policy: "NO_LOOKAHEAD"
    required_inputs:
      - "PRICE.CLOSE"
      - "TECH.MA(3,5,8,10,12,15,30,35,40,45,50,60)"
    dependencies:
      - "DATA_SOURCES:TWSE_OHLCV"
      - "FEATURES:TECH.MA_GROUPS"
  tier: "T3"                         # T0/T1/T2/T3/T4
  status: "ACTIVE"                   # DRAFT/ACTIVE/DEPRECATED/RETIRED
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
    missing_policy: "FLAG"           # FLAG/IMPUTE/STOP (STOP 必須升級治理)
    outlier_policy: "WINSORIZE"      # NONE/WINSORIZE/FLAG/STOP
    halt_handling: "FREEZE_LAST"     # FREEZE_LAST/FLAG/STOP/NA
  provenance_requirements:
    require_provenance_map: true
    require_input_hash: true
    require_output_hash: true
    require_available_at: false      # FUND/EVENT/NEWS 類通常 true
  audit_requirements:
    audit_layer: "L4"
    must_emit_artifacts:
      - "FeatureValueRecord"
      - "ProvenanceMapRef"
      - "QualityFlags"
  versioning:
    feature_version: "1.0.0"
    impl_version: "impl_2025-12-19_001"
    change_policy: "SEMANTIC_CHANGE=>bump_feature_version"
  ui_explain:
    explain_level: "L2"              # L1/L2/L3（UI_SPEC 對位）
    display_hint: "可視化為趨勢有序度/擴散程度，禁止顯示買賣箭頭"
C2. FeatureValueRecord 模板（值紀錄｜必備可回放）
FeatureValueRecord 是「某一次計算出的特徵值」：必須可回放、可稽核。

json
複製程式碼
{
  "record_type": "FeatureValueRecord",
  "correlation_id": "CID-20251219-000001",
  "session_id": "SID-20251219-000009",
  "timestamp_utc": "2025-12-19T00:01:23Z",
  "market_time": "2025-12-19T13:31:00+08:00",
  "layer_id": "L4",
  "module_id": "FEATURE_ENGINE",
  "feature_id": "TECH.TREND.GMMA_SPREAD_RATIO",
  "feature_version": "1.0.0",
  "impl_version": "impl_2025-12-19_001",
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
  "created_at_utc": "2025-12-19T00:01:23Z",
  "instrument": "TWSE:2330",
  "timeframe": "D",
  "inputs": [
    {
      "field": "PRICE.CLOSE",
      "source": "DATA_SOURCES:TWSE_OHLCV",
      "source_priority": "OFFICIAL_PRIMARY",
      "time_range": ["2025-10-01", "2025-12-19"],
      "raw_ref": "RAWSET-...-CLOSE",
      "transform_chain": ["canonicalize", "adjust_corporate_actions"]
    },
    {
      "field": "TECH.MA_GROUPS",
      "source": "FEATURES:TECH.MA_GROUPS",
      "source_priority": "INTERNAL_DERIVED",
      "time_range": ["2025-10-01", "2025-12-19"],
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

（STRATEGY_FEATURE_INDEX｜Part 4：附錄C v2025-12-19 完）

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
  feature_id: "TECH.GMMA_SPREAD_RATIO"      # 必須對應本檔 feature_id（唯一鍵）
  feature_version_min: "1.0.0"             # 最低可接受版本（語義不破壞）
  allowed_uses_required:
    - "EVIDENCE_INPUT"
  forbidden_uses_assert:
    - "DIRECT_SIGNAL"
    - "DIRECT_STRATEGY"
    - "DIRECT_ORDER"
  quality_requirements:
    missing_policy: "FLAG|STOP"            # 僅允許引用本檔定義的政策集合
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
    explain_level: "L1|L2|L3"               # 對位 UI_SPEC 顯示階層（僅接口，不越權 UI 規範）
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

# Addendum 2025-12-28｜Only-Add：GLOBAL_ALIGNMENT_PATCH（MASTER_CANON 對齊全域補丁）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219__ADDENDUM_20251227_FINAL.md（doc_key：STRATEGY_FEATURE_INDEX）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0017`）  
> 目的：以 MASTER_CANON 為主導，對齊「引用合法性、doc_key 身份、子級標籤（Label）解讀、資料治理別名（alias）封口、最小可稽核引用格式」之全域一致口徑；不改寫任何既有正文條款。

---

## G0. 適用範圍（Hard Boundary）

本 Addendum 僅處理下列事項（不創造新制度、不改寫主文）：
1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。  
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。  
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。  
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。  

本 Addendum **不處理**：
- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

- 本文件 `doc_key` 既有標示為 `STRATEGY_FEATURE_INDEX`；本 Addendum 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

並統一裁決：
- 任何文件「是否可引用」＝以 DOCUMENT_INDEX 之 Authoritative Index（ACTIVE 表格）為準  
- 任何文件「治理等級 bucket」＝以 DOCUMENT_INDEX 之 A+ / A / B / C 分桶為準  
- 文件內自述之等級/狀態若與 Index 有張力：依 DOCUMENT_INDEX §6 採「保守處置」（STOP/RETURN/BLOCK；以既有 Gate/風控規範語義為準）

---

## G2. 子級標籤（Label）之唯一合法解讀（S / B+ / C+）

凡本文件或引用鏈中出現：
- `S`：視為「Supreme Canon 的顯示標籤」或「完備度標籤」，**不構成**新的治理等級 bucket。  
- `B+` / `C+`：視為「嚴格度/完備度子級標籤」，**不構成**新的治理等級 bucket。  

治理覆蓋規則仍固定為：**A+ > A > B > C**（以 DOCUMENT_INDEX 為準）。  

---

## G3. DATA_UNIVERSE（alias）封口（資料治理引用回歸 DATA_SOURCES）

統一裁決：
- 任何出現之 `DATA_UNIVERSE` 一律視為「資料宇宙（Data Universe）」概念別名（alias），**不得**作為 doc_key。  
- 任何需要引用資料來源治理時，唯一合法 doc_key：`DATA_SOURCES`。  
- 若 Evidence/Audit/UI Trace/Gate 引用欄位出現 `doc_key=DATA_UNIVERSE`：  
  - 一律視為「引用非法」→ 依 GOVERNANCE_GATE_SPEC 進行 BLOCK/RETURN（依其既有語義；不得補救）。

---

## G4. 最小可稽核引用格式（Minimum Legal Citation Format｜可直接貼用）

凡聲稱「依據治理文件」之輸出（含：Evidence、Risk/Compliance、Governance Gate、UI Decision、Execution Control、Audit）一律必須同時提供：

```text
ref_doc_key = <DOC_KEY>
ref_file = <完整檔名>
ref_version = <版本日期或檔名日期碼>
ref_section = <章節定位（§ / Heading Path）>
ref_purpose = <用途：例如 gate_check / risk_veto / ui_decision / execution_policy / audit_replay>
ref_notes = <可選：alias/Label 解讀備註>
```

缺任一欄位：
- 依 DOCUMENT_INDEX §6 採保守處置：不得形成裁決性輸出（PASS/APPROVE/EXECUTE 等）；必要時 RETURN/BLOCK。

---

## G5. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫本文件任何既有條款。  
- 本 Addendum 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。  
- 本 Addendum 目的僅在於消解引用歧義、避免 Gate 因 metadata/格式缺口而誤判，並確保全鏈路可稽核、可回放。

（Addendum 2025-12-28｜Only-Add｜Freeze v1.0 完）
