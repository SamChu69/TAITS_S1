# TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260102.md
doc_key：TWSE_RULES  
治理等級：B（Market Rule Reference & Compliance Trigger Map｜制度參考與合規觸發映射）  
適用範圍：TAITS 台灣市場（TWSE / TPEX / TAIFEX 之「制度引用」層；裁決以官方為準）  
版本狀態：ACTIVE（最大完備／累積式更新：允許融合更新、覆寫修正、重排版；禁止摘要縮水；未被新內容明確取代者必保留；被取代者可移除但須留痕承接）
版本日期：2026-01-02（Asia/Taipei）
變更原則：最大完備＋累積式更新（允許融合更新／覆寫修正／重排版；不得只保留重點；舊內容未被新內容明確取代者一律保留累積；僅被新內容明確取代之舊資訊可省略但須於稽核留痕承接）
核心鐵律：**制度不得被寫死**；TAITS 只保存「參考彙編＋觸發映射＋快照引用」；所有合規裁決必須可追溯到官方來源與制度快照（Rulebook Snapshot）


## 目錄（依序排列）

- 全局定錨｜單一口徑（S1）
  - 1. 人類最高決策者主權（SOVEREIGNTY）
  - 2. L9–L11 最終語義（跨文件一致）
  - 3. HFI｜人類明確命令（可執行觸發）
- 治理補強（已整合為正文）
- 0. 適用範圍（Hard Boundary）
- 1. DATA_UNIVERSE 的法律定位（Alias ≠ doc_key）
  - 1.1 統一裁決：DATA_UNIVERSE 僅為概念別名
  - 1.2 引用合法性硬規則（Gate-Friendly）
- 2. Rulebook Snapshot / Trigger Map 與 doc_key 對位（避免誤綁）
  - 2.1 本文件之資料治理引用應固定到 DATA_SOURCES
  - 2.2 最小合規引用模板（可直接貼用）
- 3. 檔頭「平行參照」之兼容解釋（最大完備＋累積式更新（舊口徑已淘汰），不改原文）
- 0. 文件定位（Rule Reference Charter）
- 1. 官方制度來源（Official Sources｜必須提供可追溯網址）
  - 1.1 TWSE（臺灣證券交易所）官方制度
  - 1.2 TPEX（櫃買中心）官方制度
  - 1.3 TAIFEX（臺灣期貨交易所）官方制度
  - 1.4 金管會（FSC）與相關制度（必要時）
- 2. Rulebook Snapshot（制度快照）治理（核心制度）
  - 2.1 為什麼必須快照
  - 2.2 Snapshot 最小內容（不可縮減）
  - 2.3 Snapshot 與 VERSION_AUDIT 的關係
- 3. 制度不是條文堆疊：Rule Trigger Map（觸發映射）
  - 3.1 Trigger Map 的定義
  - 3.2 Trigger Map 的輸出位置
- 4. TAITS 合規判定架構（Compliance Decision Architecture）
  - 4.1 合規判定的二元性（Binary Compliance）
  - 4.2 合規判定不可被績效辯護
- 5. 規則分類（Rule Taxonomy｜最大完備骨架）
  - 5.1 Trading Session & Calendar Rules（交易時段/交易日曆）
  - 5.2 Instrument Eligibility Rules（標的可交易性）
  - 5.3 Price Limit & Auction Rules（漲跌幅/撮合/價格限制）
  - 5.4 Order Type & Quantity Rules（委託類型/數量/單位）
  - 5.5 Short Selling / Margin Rules（融資融券/放空相關）
  - 5.6 Corporate Actions & Symbol Changes（除權息/代碼變更）
  - 5.7 Market-Wide Controls（市場級管制）
  - 5.8 Derivatives-Specific Rules（期貨/選擇權特有）
- 6. 合規 Reason Codes（原因碼）與制度引用（Mapping）
  - 6.1 原因碼映射最小欄位（不可縮減）
  - 6.2 常見原因碼類型（骨架）
- 7. 合規觸發點（Hard Triggers｜在哪一層必查）
  - 7.1 L7（Risk/Compliance Gate）必查項目（不可省略）
  - 7.2 L11（Execution Preflight）必查項目（不可省略）
  - 7.3 UI（L10）必呈現項目（不可省略）
- 8. Rule Trigger Map（制度觸發映射）資料結構（可落地）
  - 8.1 Trigger Map Record（單筆）
- 9. Mermaid｜制度觸發到合規否決的流程圖（可放入 md）
- 治理補強（已整合為正文）
  - A1. 本文件之唯一治理身份（Canonical Identity）
  - A2. 本專案目錄中的實體檔案（Physical Artifact）
  - A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 治理補強（已整合為正文）
- G0. 適用範圍（Hard Boundary）
- G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）
- G2. 子級標籤（Label）之唯一合法解讀（S / B+ / C+）
- G3. DATA_UNIVERSE（alias）封口（資料治理引用回歸 DATA_SOURCES）
- G4. 最小可稽核引用格式（Minimum Legal Citation Format｜可直接貼用）
- G5. 最終宣告（以 GOVERNANCE_STATE 現況為準（若見 Freeze 字樣，視為歷史標記））

---


## 全局定錨｜單一口徑（S1）

### 1. 人類最高決策者主權（SOVEREIGNTY）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接，不得卡死更新。

### 2. L9–L11 最終語義（跨文件一致）
- L9（投資報告層）：可追蹤、可更新、可標的化投資報告；必含數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源），並支援事件驅動滾動更新。
- L10（人類裁決層）：由人類最高決策者裁決不動作/回測/模擬/半自動/全自動等；任何交易型態皆以 L10 明確裁決為準。
- L11（工程稽核回放層）：對 L1–L11 全層輸入/處理/輸出/裁決/執行鏈路留痕，供人類與工程端可讀、可查、可回放；L11 非下單決策層。

### 3. HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：Freeze/最大完備＋累積式更新（舊口徑已淘汰）/Gate 不得阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。

---

---

## 治理補強（已整合為正文）

上位裁決：Index Gate（DOCUMENT_INDEX）＋治理等級覆蓋（A+ > A > B > C）＋衝突裁決程序（DOCUMENT_INDEX §6）＋AI_GOV（A+）最高約束  

---

## 0. 適用範圍（Hard Boundary）

- 本文件仍可使用「DATA_UNIVERSE」作為概念名詞（Data Universe／資料宇宙）或閱讀別名（alias）

---

## 1. DATA_UNIVERSE 的法律定位（Alias ≠ doc_key）

### 1.1 統一裁決：DATA_UNIVERSE 僅為概念別名
本文件（含檔頭平行參照與正文段落）中出現之「DATA_UNIVERSE」：
- 一律視為「資料宇宙」之概念名詞／閱讀別名（alias）
- **不得**被解讀為治理文件 doc_key
- **不得**被寫入任何引用欄位（doc_key / evidence_doc_key / audit_doc_key / ui_doc_key / gate_doc_key）

### 1.2 引用合法性硬規則（Gate-Friendly）
凡本文件需要引用「資料來源治理文件」時（例如：資料來源 Provenance、來源證據、資料取得責任界面）：
- 唯一合法 doc_key **必須**為：`DATA_SOURCES`
- 若任何輸出（含 Evidence / Audit / UI Trace / Rulebook Snapshot 記錄）出現 `doc_key=DATA_UNIVERSE`：
  - 一律視為「引用非法」
  - 依 Gate 規則裁決為 BLOCK（不得以推測補救）

---

## 2. Rulebook Snapshot / Trigger Map 與 doc_key 對位（避免誤綁）

### 2.1 本文件之資料治理引用應固定到 DATA_SOURCES
凡本文件第 2 章（Rulebook Snapshot）與第 3/8 章（Trigger Map 結構）所述之以下欄位：
- `source_urls[]`
- `source_evidence_refs[]`
- `evidence_refs[]`
- `audit_refs[]`
- `hash_manifest_ref`
- `active_version_map_ref`（與版本映射相關）

其「資料來源治理」之引用口徑一律採：
- `ref_doc_key = DATA_SOURCES`
- `ref_doc_name = TAITS_資料來源全集（DATA_SOURCES）__251219.md`
- `alias_note = DATA_UNIVERSE 僅為概念別名，不具 doc_key 法律效力`

### 2.2 最小合規引用模板（可直接貼用）
```text
ref_doc_key = DATA_SOURCES
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0001
```

---

## 3. 檔頭「平行參照」之兼容解釋（最大完備＋累積式更新（舊口徑已淘汰），不改原文）

- 在 以 GOVERNANCE_STATE 現況為準（若見 Freeze 字樣，視為歷史標記） 下不覆寫原文
- 任何系統性引用（doc_key 層級）一律回歸 `DATA_SOURCES`

## 0. 文件定位（Rule Reference Charter）

本文件為 TAITS 的「台灣市場交易規則參考彙編與合規觸發映射（Rule Trigger Map）」文件，目的在於：

- 提供 TAITS 進行「合規判定」時所需的制度參考框架（非取代官方裁決）
- 建立制度的 **Rulebook Snapshot（規則快照）** 與 **Trigger Map（觸發映射）**：
  - 哪一條制度對應哪一類交易行為
  - 何時應觸發風控/合規檢查
  - 觸發後是 PASS / VETO / RETURN / BLOCK
- 確保 TAITS 遵守：
  - **Binary Compliance（合規二元裁決：PASS/VETO）**
  - **Evidence 法律地位（無快照/無引用＝不可裁決）**
  - **最大完備＋累積式更新（舊口徑已淘汰）（制度更新用新快照追加，不覆寫舊內容）**
- 支援 TWSE（上市）、TPEX（上櫃）、TAIFEX（期貨/選擇權）制度引用（擴充性）

📌 本文件不做的事（避免越權）：
- 不宣稱本文件內容永遠正確或最新（制度以官方更新為準）
- 不把制度內容「寫死在程式」作永久裁決
- 不替代 RISK_COMPLIANCE 的否決條文與 reason codes 設計
- 專注：制度引用如何進入 TAITS 的「合規快照＋觸發映射＋稽核可回放」

---

## 1. 官方制度來源（Official Sources｜必須提供可追溯網址）

TAITS 任何合規裁決，必須能回指到以下官方來源之一（或其官方等價入口），並在 Rulebook Snapshot 中保存引用證據。

### 1.1 TWSE（臺灣證券交易所）官方制度
- TWSE 規章／法規查詢（Regulation Search / Rules）  
  https://twse-regulation.twse.com.tw/
- TWSE 官方網站（公告/市場資訊）  
  https://www.twse.com.tw/

### 1.2 TPEX（櫃買中心）官方制度
- 櫃買中心官方網站（法規/制度/公告）  
  https://www.tpex.org.tw/

### 1.3 TAIFEX（臺灣期貨交易所）官方制度
- TAIFEX 規章制度（Rules & Regulations）  
  https://www.taifex.com.tw/

### 1.4 金管會（FSC）與相關制度（必要時）
- 金管會官方網站（法規/公告）  
  https://www.fsc.gov.tw/

📌 規則引用原則（硬規則）  
- 合規裁決不得只引用「第三方整理文章」  
- 若因技術或權限限制暫時無法抓取官方文本，也必須記錄：
  - 來源嘗試、時間戳、替代來源（fallback）、並標記「未達可裁決等級」→ RETURN/BLOCK

---

## 2. Rulebook Snapshot（制度快照）治理（核心制度）

### 2.1 為什麼必須快照
交易制度會更新。若 TAITS 直接寫死制度條文：
- 會造成合規判定不可追溯、不可回放、不可稽核
- 會造成「回測/回放」與「當下制度」混淆

因此 TAITS 必須以 Rulebook Snapshot 形式管理制度：
- **每一次合規裁決都綁定一份 `rulebook_snapshot_ref`**
- Snapshot 以 最大完備＋累積式更新（舊口徑已淘汰） 管理（新增版本，不覆寫舊版本）

### 2.2 Snapshot 最小內容（不可縮減）
每一份 `rulebook_snapshot` 至少包含：

- `rulebook_snapshot_id`
- `scope`：TWSE / TPEX / TAIFEX / FSC（可多選）
- `captured_at`：擷取時間
- `source_urls[]`：官方網址清單（必填）
- `source_evidence_refs[]`：擷取證據（HTML/PDF 截圖/回應頭/Hash）
- `normalized_ruleset_ref`：制度正規化後的結構化表示（條款→觸發→判定）
- `hash_manifest_ref`：不可竄改校驗
- `notes`：僅能補充，不能取代官方內容

### 2.3 Snapshot 與 VERSION_AUDIT 的關係
- `rulebook_snapshot_ref` 必須被納入 Active Version Map
- 缺 snapshot → 視為 `CMP-RULEBOOK-MISSING` → VETO/BLOCK（依 RISK_COMPLIANCE）

---

## 3. 制度不是條文堆疊：Rule Trigger Map（觸發映射）

最大完備的關鍵不在「抄條文」，而在「把制度變成可執行的觸發映射」並可稽核可回放。

### 3.1 Trigger Map 的定義
Trigger Map 將「交易行為」映射到「必須檢查的制度/規則類型」：

- **行為（Action）**：送單、改單、撤單、下市值/限價、盤中/盤後、零股、信用交易、ETF、期貨等
- **情境（Context）**：交易時段、標的狀態（處置/暫停/全額交割等）、市場狀態（熔斷/跌停等）
- **規則（Rule）**：制度條款（以 snapshot 引用）
- **結果（Decision）**：PASS / VETO / RETURN / BLOCK
- **原因碼（Reason Codes）**：必須能對應 RISK_COMPLIANCE 的 reason_code

### 3.2 Trigger Map 的輸出位置
- Risk/Compliance Engine（L7）必須使用 Trigger Map 做合規裁決
- UI（L10）必須可視化「是哪一條制度觸發了哪個原因碼」
- Audit（VERSION_AUDIT）必須保存「觸發鏈」以回放

---

## 4. TAITS 合規判定架構（Compliance Decision Architecture）

### 4.1 合規判定的二元性（Binary Compliance）
- 合規輸出必須是：
  - `PASS` 或 `VETO`
- `RETURN` 只用於「資料不足不可裁決」情況（例如缺官方快照、缺標的狀態資料）
- `BLOCK` 用於「系統完整性不足」情況（例如缺版本映射、稽核不可寫入）

### 4.2 合規判定不可被績效辯護
- 任何策略績效、回測勝率、AI 建議都不得推翻合規 VETO

---

## 5. 規則分類（Rule Taxonomy｜最大完備骨架）

下列分類用於制度正規化與 reason codes 對齊；具體條文內容以 snapshot 連結保存。
本節是「骨架」，避免寫死制度，並支援 最大完備＋累積式更新（舊口徑已淘汰） 擴充。

### 5.1 Trading Session & Calendar Rules（交易時段/交易日曆）
- 交易日/非交易日
- 開收盤時段、盤中、盤後
- 例外交易日、臨時停市等（以官方公告為準）

**觸發點**：L7 合規必查（任何送單）

### 5.2 Instrument Eligibility Rules（標的可交易性）
- 是否可交易（停止交易、暫停、下市/下櫃）
- 特殊狀態（處置股票、全額交割、警示、注意等）
- 標的屬性（股票/ETF/權證/受益憑證等）

**觸發點**：L7 合規必查（標的層級）

### 5.3 Price Limit & Auction Rules（漲跌幅/撮合/價格限制）
- 漲跌停限制與可接受價格區間
- 撮合規則（集合競價/逐筆交易等）

**觸發點**：L11 Preflight + L7 合規（避免送出制度不允許委託）

### 5.4 Order Type & Quantity Rules（委託類型/數量/單位）
- 限價/市價/其他委託類型（依市場/商品）
- 最小交易單位、零股交易規則、單筆上限等

**觸發點**：L11 Intent Compiler + L7 合規

### 5.5 Short Selling / Margin Rules（融資融券/放空相關）
- 信用交易資格、可融/可借券狀態、限制條款等

**觸發點**：L7 合規（帳戶權限 + 標的狀態 + 交易行為）

### 5.6 Corporate Actions & Symbol Changes（除權息/代碼變更）
- 除權息、分割、合併、停止過戶期間等影響可交易性/價格調整

**觸發點**：L2/L3 資料正規化 + L7 合規（防止用錯價格基準）

### 5.7 Market-Wide Controls（市場級管制）
- 熔斷、緊急措施、臨時撮合調整等

**觸發點**：L6 Regime/Market State + L7 合規 + L11 Circuit Breaker

### 5.8 Derivatives-Specific Rules（期貨/選擇權特有）
- 商品規格、到期、漲跌停、保證金、交易時段等

**觸發點**：L7 合規 + L11 preflight（TAIFEX）

---

## 6. 合規 Reason Codes（原因碼）與制度引用（Mapping）

Reason Codes 的命名與完整清單以 RISK_COMPLIANCE 為裁決。
本文件提供「映射框架」：每個原因碼必須可回指制度快照與觸發條件。

### 6.1 原因碼映射最小欄位（不可縮減）
- `reason_code`
- `category`：CMP / MKT / EXE / SYS
- `trigger_condition`：觸發條件（結構化）
- `rulebook_snapshot_ref`
- `official_source_urls[]`
- `evidence_refs[]`（例如標的狀態/交易時段/價格區間計算）
- `ui_display_text_zh`（繁中顯示）
- `severity`：VETO/BLOCK/RETURN

### 6.2 常見原因碼類型（骨架）
- `CMP-SESSION-CLOSED`：交易時段不允許
- `CMP-INSTRUMENT-HALTED`：標的暫停/停止交易
- `CMP-INSTRUMENT-RESTRICTED`：處置/限制
- `CMP-ORDER-TYPE-NOT-ALLOWED`：委託類型不符
- `CMP-PRICE-OUT-OF-BOUNDS`：價格超出可接受區間
- `CMP-LOT-SIZE-INVALID`：交易單位不符（整股/零股）
- `CMP-MARGIN-NOT-ELIGIBLE`：信用交易不符資格
- `CMP-RULEBOOK-MISSING`：制度快照缺失（系統級合規不可裁決）

注意：以上僅為分類示意；正式 reason codes 由 RISK_COMPLIANCE 統一裁決。

---

## 7. 合規觸發點（Hard Triggers｜在哪一層必查）

### 7.1 L7（Risk/Compliance Gate）必查項目（不可省略）
- 交易時段/交易日曆（Session/Calendar）
- 標的可交易性（Eligibility）
- 帳戶權限限制（例如信用交易）
- 制度快照存在與可追溯（Rulebook Snapshot）

### 7.2 L11（Execution Preflight）必查項目（不可省略）
- 送單前再次核對：
  - 風控 PASS Token
  - 通道健康
  - 委託內容合法性（價格區間、數量單位、委託類型）
- 任何 mismatch → BLOCK 並回報 UI（UI 顯示原因碼）

### 7.3 UI（L10）必呈現項目（不可省略）
- 本次裁決使用的 `rulebook_snapshot_ref`
- 觸發的制度分類與原因碼
- 官方來源連結（至少可點開看到 source_urls）

---

## 8. Rule Trigger Map（制度觸發映射）資料結構（可落地）

這是一個可直接作為工程資料表/JSON schema 的規格骨架（最大完備）。
實際存放可由 DATA_UNIVERSE/DEPLOY_OPS 決定，但語義不得改。

### 8.1 Trigger Map Record（單筆）
- `trigger_id`
- `market_scope`：TWSE/TPEX/TAIFEX
- `action_type`：SUBMIT / MODIFY / CANCEL / QUERY / RECONCILE
- `instrument_type`：EQUITY / ETF / WARRANT / FUTURES / OPTIONS …
- `order_type`：LIMIT / MARKET / …（若適用）
- `time_context`：PREOPEN / REGULAR / POST / OFF_SESSION
- `conditions`：
  - `symbol_state`（halted/restricted/normal…）
  - `price_bounds`（需引用計算證據）
  - `lot_rules`（整股/零股）
  - `account_permissions`（margin/short/derivatives…）
- `decision`：PASS/VETO/RETURN/BLOCK
- `reason_codes[]`
- `rulebook_snapshot_ref`
- `official_source_urls[]`
- `audit_refs[]`（evidence refs, calculations, snapshots）
- `ui_text_zh`

---

## 9. Mermaid｜制度觸發到合規否決的流程圖（可放入 md）

```mermaid
```
flowchart TB
  A[L1-L2 Data + Calendar + Symbol State] --> B[L5 Evidence Bundle]
  B --> C[L6 Regime/Market State]
  C --> D[L7 Compliance Trigger Map Lookup]
  D --> E{Rulebook Snapshot Exists?}
  E -->|NO| X[RETURN/BLOCK<br/>CMP-RULEBOOK-MISSING]
  E -->|YES| F[Evaluate Rule Conditions]
  F --> G{Compliance Decision}
  G -->|PASS| H[Issue PASS + Token]
  G -->|VETO| I[VETO + reason_codes + source_urls]
  I --> UI[UI shows VETO + Codes + Official Links]
  H --> UI2[UI shows PASS + snapshot_ref]
10. 常見落地情境（Scenario Coverage｜最大完備）
本節不是抄條文，而是把 TAITS 需要處理的情境「制度化」成觸發類型，便於工程實作與稽核。

10.1 非交易時段送單
觸發：CMP-SESSION-CLOSED

依據：TWSE/TPEX/TAIFEX 官方交易時段公告（source_urls）

輸出：VETO（Binary）

10.2 標的暫停/停止交易（halted）
觸發：CMP-INSTRUMENT-HALTED

證據：symbol_state snapshot + 官方公告 ref

輸出：VETO

10.3 處置/限制股票
觸發：CMP-INSTRUMENT-RESTRICTED

證據：處置清單或公告 ref（source_urls）

輸出：VETO 或更嚴格限制（由 policy 裁決）

10.4 零股 vs 整股交易單位不符
觸發：CMP-LOT-SIZE-INVALID

證據：order intent + lot rules

輸出：VETO 或 RETURN（若缺 lot rule snapshot）

10.5 價格超出允許區間
觸發：CMP-PRICE-OUT-OF-BOUNDS

證據：price bounds 計算（以快照資料與制度快照為準）

輸出：VETO

10.6 信用交易/放空資格不符
觸發：CMP-MARGIN-NOT-ELIGIBLE

證據：account permission snapshot + 標的可融/可借券狀態 + 制度快照

輸出：VETO

10.7 制度快照缺失或不可追溯
觸發：CMP-RULEBOOK-MISSING / SYS-VERSION

輸出：BLOCK（系統級阻斷，因不可裁決）

11. 審計輸出（Audit Outputs｜必須落地）
本節是「最大完備」強制要求：每次合規裁決都要留下可回放證據。

每一次 L7 合規判定，必須產生：

risk_gate_decision_ref（包含 compliance 部分）

rulebook_snapshot_ref

trigger_map_evaluation_ref

reason_codes[]

official_source_urls[]

evidence_refs[]（交易時段、標的狀態、價格區間計算等）

hash_manifest_ref

納入 active_version_map_ref

UI（L10）必須顯示：

rulebook_snapshot_ref

reason_codes[]

official_source_urls[]（可點開）

不得用模糊語句取代 VETO

12. 制度更新策略（No-Write-Dead Rules｜不得寫死）
12.1 更新方式（最大完備＋累積式更新（舊口徑已淘汰））
任何制度更新：

新增 rulebook_snapshot

新增 Trigger Map 條目（如需要）

更新 policy/version map 指向（切換 ACTIVE 版本）

禁止：

覆寫舊快照內容

把舊快照刪掉

用「改程式碼」取代制度快照治理

12.2 更新頻率（建議，不是裁決）
每日開盤前：檢查制度來源與公告更新（DEPLOY_OPS Runbook）

發生重大事件/公告：立即生成新快照並追加稽核事件

13. 最大完備＋累積式更新（舊口徑已淘汰） 演進規則（TWSE_RULES 專屬）
允許新增：

新市場/商品範圍（TPEX/TAIFEX）

新制度分類（Rule Taxonomy）

新觸發映射（Trigger Map Records）

新 reason codes 映射欄位（更嚴格、更可追溯）

新的官方來源入口（例如新增公告頁面類型）

禁止：

把制度內容「寫死」作永久裁決

移除官方來源網址或快照引用

允許缺快照仍做合規 PASS

用第三方資料裁決制度（只能作 fallback 並降級為不可裁決 → RETURN/BLOCK）

14. 終極裁決語句（不可更改）
合規不是「看起來合理」，而是「可回指官方、可回放快照、可稽核觸發鏈」。
任何缺快照、缺來源、缺觸發映射的合規判定，都不允許通過。

（TWSE_RULES｜最大完備版 v2025-12-19 完）
---

## 治理補強（已整合為正文）

上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`TWSE_RULES`
- 版本狀態：ACTIVE（以 GOVERNANCE_STATE 現況為準（若見 Freeze 字樣，視為歷史標記）；最大完備＋累積式更新（舊口徑已淘汰））

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=TWSE_RULES` + `canonical_filename=TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251219.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

## 治理補強（已整合為正文）

上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
目的：以 MASTER_CANON 為主導，對齊「引用合法性、doc_key 身份、子級標籤（Label）解讀、資料治理別名（alias）封口、最小可稽核引用格式」之全域一致口徑；不改寫任何既有正文條款。

---

## G0. 適用範圍（Hard Boundary）

1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。  
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。  
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。  
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。  

- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

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

## G5. 最終宣告（以 GOVERNANCE_STATE 現況為準（若見 Freeze 字樣，視為歷史標記））

# 稽核留痕（Audit Section｜不屬正文）

## A. Scope（適用範圍）
- doc_key：TWSE_RULES
- 檔案：TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260102.md
- 適用狀態：ACTIVE
- 適用時間：2026-01-02（Asia/Taipei）
- 本次作業：融合更新（口徑統一：Only-Add → 最大完備＋累積式更新）、重排版（新增目錄依序排列）、稽核留痕分離（Scope/Changelog/Hash/Audit Hand-off）。

## B. Changelog（變更清單）
1) 口徑統一：將全文殘留之「只能加/只可新增/只增不減/不得覆寫」等描述，統一改寫為「最大完備＋累積式更新」治理口徑（允許融合更新/覆寫修正/重排版；禁止摘要縮水；未被新內容明確取代者必保留；被取代者可移除但須留痕承接）。
2) 混讀防護：將 Freeze/FREEZE 等標記改為「以 GOVERNANCE_STATE 現況為準（若見 Freeze 字樣，視為歷史標記）」的表述，避免狀態混讀。
3) 重排版：新增「目錄（依序排列）」以提升定位效率；正文內容不減少。
4) 稽核留痕：新增本檔 Scope／Changelog／Hash Manifest／Audit Hand-off，並與正文分離。

## C. Hash Manifest（指紋清單）
- file_name: TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260102.md
- hash_algo: sha256
- hash_value_sha256: 4b09079754df26878a52b5a2a9dad2049a17c6bd969db8aa6c2a618e8484d510

## D. Audit Hand-off（裁決承接）
- 裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV（如有衝突以此序為準）。
- 承接聲明：本檔為規則參考彙編（治理等級 B），不得越權覆寫 RISK_COMPLIANCE 之最高否決權與 MASTER_CANON 的 L9/L10/L11 定錨。
- L9/L10/L11 定錨：L9＝投資報告層（含數據/圖形/進出場建議/可追蹤更新）；L10＝人類裁決與交易決策層；L11＝全層工程稽核回放層（L1–L11全留痕），且 L11 非下單層。
