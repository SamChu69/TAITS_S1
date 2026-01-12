# TAITS_風險控管與合規最高否決權（RISK_COMPLIANCE）

## 文件頭（Document Header）

- doc_key：RISK_COMPLIANCE
- 治理位階：母體／憲法級（風險與合規最高否決權）
- 版本狀態：ACTIVE
- 版本日期：2026-01-11（Asia/Taipei）
- 基線日期：2026-01-11（Asia/Taipei）
- 裁決序位（自高至低）：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
- 適用範圍：TAITS 全系統（任何層級輸出、任何策略、任何執行）之最高否決／停機／降級／隔離與合規裁決

## 0. 文件定位（Risk & Compliance Charter｜最高否決權憲章）

本文件是 TAITS 的「風險控管與合規最高否決權」母文件，負責：

- 定義 **風險/合規的最高否決權（Supreme Veto）**
- 定義 **風險門檻、合規門檻、觸發條件、理由碼**
- 定義 **Risk/Compliance 在 Canonical Flow 的 Gate 機制與 UI 呈現義務**
- 定義 **審計證據（Evidence）與可回放（Replay）必備輸出**

本文件不負責（避免越權）：
- 不定義 Canonical 流程順序（由 MASTER_CANON / ARCH_FLOW 裁決）
- 不定義架構模組地圖（由 FULL_ARCH 裁決）
- 不定義下單細節與券商通道細則（由 EXECUTION_CONTROL 裁決）
- 不產生策略建議、不產生交易方向、不承諾績效

---


## 1. 最高鐵律（Hard Gates｜一票否決）

### 1.1 SOVEREIGNTY｜人類最高決策者唯一主權（不可牴觸）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令之生效。
- 風險與合規（Risk/Compliance）：
  - 在任何情況下保有最高否決權（VETO）。
  - 人類明確命令（HFI）不得覆寫否決；但必須觸發「強制揭露＋替代方案＋全紀錄」之承接。

### 1.2 Canonical Flow｜層級邊界承接（不重複定義）
- L1–L11 之層級定義與 Canonical Flow：一律以 doc_key=MASTER_CANON 為唯一正文來源。
- 本檔僅裁決風險/合規之否決、降級、隔離與放行條件；不得改寫 Canonical Flow 之層級定義或裁決路徑。

### 1.3 HFI｜人類明確命令（可執行觸發）
- 有效 HFI 存在時：仍必須執行風險/合規 Gate；如判定 VETO，仍必須 VETO。
- 同時必須輸出完整風險揭露、替代方案與可稽核留痕（不得省略）。
- HFI 相關之裁決承接、留痕與版本落帳：依 doc_key=VERSION_AUDIT 與本檔稽核區塊之規範執行。

### 1.4 Risk / Compliance 的法定位階（不可動搖）
- **Risk / Compliance 可否決一切**：策略、Agent、流程、人類裁決之「執行意圖」皆可被否決。
- 任何 VETO：
  - **立即中止流程**（依 ARCH_FLOW STOP / RETURN 規則）
  - **不得以績效、直覺、緊急性辯護**
  - **不得由人類覆寫**（Human Cannot Override Risk）

### 1.5 Binary Compliance（非黑即白）
- Gate 輸出僅允許：
  - `PASS`
  - `VETO`
- 禁止：
  - 模糊放行（Soft Pass）
  - 條件通融（Conditional Pass）
  - 以人工備註取代規則

### 1.6 Worst-case First（最壞情境優先）
- 所有風險評估必須以：
  - 交易失敗、滑價擴大、流動性枯竭、撮合異常、制度變動、資料污染
  作為基準情境。
- 禁止以「過去沒發生」作為安全理由。

### 1.7 Evidence First（沒有證據不得放行）
- 若 Evidence 不完整、不可追溯、不可回放：
  - **視為 SYS 類否決（SYS-AUD / SYS-PROV）**

### 1.8 Regime 高於策略
- Regime 判定為不可交易（或 Regime 不明確且風險升級）：
  - 可直接觸發 VETO（REG-VETO）

---


## 2. 官方制度與資料來源（Official Sources｜必須掛上來源入口）

本節提供 TAITS 制度/規則/合規的「官方入口」。
實作時不得以非官方網站裁決制度；可用非官方作補充，但不得作最終裁決依據。

- TWSE（臺灣證券交易所）規章/法規查詢（Rules & Regulations Directory）
  https://twse-regulation.twse.com.tw/
- TWSE 交易制度/交易機制（Trading Mechanism）
  https://www.twse.com.tw/en/products/system/trading.html
- TAIFEX（臺灣期貨交易所）規章與規則（Rules & Regulations）
  https://www.taifex.com.tw/enl/eng6/ruleRegulation
- FSC（金管會）法規資訊（Laws and Regulations）
  https://www.fsc.gov.tw/en/home.jsp?id=3&parentpath=0
- SFB（證期局）法規與規章入口（Securities and Futures Bureau）
  https://www.sfb.gov.tw/en/
- TDCC（集保結算所）清算交割/結算相關資訊（Clearing & Settlement）
  https://www.tdcc.com.tw/portal/en/equity/settlement

---


## 3. RISK_COMPLIANCE 在 Canonical Flow 的定位（L7 Gate）

### 3.1 所屬層級
- **L7：Risk & Compliance Layer（最高否決 Gate）**

### 3.2 上游輸入（Inputs）
- Evidence Bundle（L5）
- Regime State（L6）
- Strategy Proposal（L8：僅作「可用性/風險映射」，不得作下單）
- Account / Portfolio State（資金、倉位、未成交委託、曝險）
- Market Microstructure State（流動性、委買委賣深度、波動）
- 規則快照（TWSE/TAIFEX/券商限制/交易時段/停牌等）

### 3.3 Gate 輸出（Outputs）
- `risk_gate_decision`：PASS / VETO
- `veto_reason_codes[]`：若 VETO 必填（不可空）
- `risk_pass_token`：僅 PASS 生成，供 EXECUTION_CONTROL 驗證（不可偽造）
- `risk_evidence_snapshot_ref`：證據快照引用（可回放）

---


## 4. 風險/合規裁決層級與優先序（Risk Hierarchy）

優先序（由高至低）：
1) **Compliance（合規）**：制度/法規/交易規則硬限制（不可通融）
2) **System Safety（系統安全）**：審計、版本、金鑰、資料污染（不可通融）
3) **Market Integrity（市場完整性）**：停牌、撮合異常、極端波動、流動性枯竭
4) **Portfolio Safety（組合安全）**：曝險、集中度、槓桿、回撤、資金使用
5) **Execution Safety（執行安全）**：滑價、委託量、通道健康、Kill Switch 可用性
6) **Strategy Compatibility（策略相容）**：Regime/策略條件不符（可 VETO 或 RETURN）

任何高層級否決：
- 低層級不得覆寫或辯護。

---


## 5. 風險分類體系（Risk Taxonomy｜最大完備）

### 5.1 Compliance Risk（合規風險）
- 交易時段/撮合規則不符
- 停牌、處置、注意股、分盤交易、漲跌幅限制相關規則觸發
- 標的交易限制（如不可融券、不可當沖、或交易所/券商限制）
- 異常報價、超出可接受價格範圍（含錯價風險）
- 法規/規則版本未同步或不可追溯

### 5.2 System Risk（系統風險）
- 審計缺失（缺 correlation_id / 缺 hash / 缺 replay bundle）
- 版本不一致（doc_key/政策/模型版本對不上）
- 資料來源不可追溯（provenance 斷裂）
- 時間不同步（時鐘偏移、交易日判定錯誤）
- 金鑰/憑證風險（敏感資訊外洩、權限不當）
- 風控服務不可用或結果不可驗證

### 5.3 Market Risk（市場風險）
- 極端波動（Volatility spike）
- 跳空、閃崩、連續跌停/漲停造成無法退出
- 系統性風險事件（重大事件日、政策公布、颱風停市/臨時休市等）
- 市場結構異常（流動性突然消失、價量失真）

### 5.4 Liquidity & Slippage Risk（流動性/滑價風險）
- 委買委賣深度不足
- 量能不足（成交量過低、點差過大）
- 預估滑價超過容忍（含分段成交造成成本放大）

### 5.5 Portfolio / Exposure Risk（曝險/組合風險）
- 單一標的曝險過高（集中度）
- 產業/因子/相關性過高（隱性集中）
- 槓桿/保證金風險（期貨/選擇權時尤其嚴格）
- 回撤/連續虧損超標

### 5.6 Execution / Operational Risk（執行/營運風險）
- 通道異常（券商 API 不穩、回報延遲、重送風險）
- 風控/執行狀態不一致（已下單但系統以為未下）
- Kill Switch 不可用或未驗證
- 倉位回報延遲造成重複下單

### 5.7 Strategy Risk（策略風險，僅作相容性與限制映射）
- Regime 不匹配（策略在非適用市場狀態啟用）
- 過擬合跡象（僅研究警示，不作績效論證）
- 策略依賴資料不可用（特徵缺失/延遲）

---


## 6. Gate 結構（Risk Gate Architecture）

### 6.1 Gate 分層（內部結構，仍對外輸出 PASS/VETO）
- **C-Gate（Compliance Gate）**：合規硬否決
- **S-Gate（System Safety Gate）**：審計/版本/資料追溯硬否決
- **M-Gate（Market Integrity Gate）**：市場狀態與完整性否決
- **P-Gate（Portfolio Gate）**：曝險/集中度/資金安全否決
- **E-Gate（Execution Gate）**：通道/滑價/急停可用性否決
- **X-Gate（Cross-Gate Consistency）**：跨 Gate 一致性檢查（防止矛盾）

### 6.2 Gate 執行順序（由高至低）
合規（Compliance）、系統（System）、市場（Market）、投資組合（Portfolio）、執行（Execution）、交易所/通道（Exchange/Channel）
任何 Gate VETO：立即停止後續 Gate 計算（節省資源，避免事後辯護）。

---


## 7. 否決條件全集（Veto Conditions｜不可弱化）

規則設計原則：
- 可新增條件，但不得移除既有條件
- 任一條件命中即 VETO（除非明確標註為 RETURN 類型）
- 所有條件必須對應 reason_code（不可空）

### 7.1 合規硬否決（C-HARD VETO）
- 非交易時段/不允許交易狀態（C-SESSION）
- 標的不可交易（停牌/終止/暫停撮合等）（C-HALT）
- 交易規則限制命中（漲跌幅/分盤/處置相關硬限制）（C-RULE）
- 券商/通道限制命中（C-BROKER）
- 法規/規則版本不可追溯或失效（C-VERSION）

### 7.2 系統安全硬否決（S-HARD VETO）
- 缺審計（correlation_id / hash / artifact 缺漏）（S-AUDIT）
- 版本不一致（doc/policy/model mismatch）（S-VERSION）
- 資料來源不可追溯（provenance 斷裂）（S-PROV）
- 風控計算不可驗證（S-VERIFY）
- 金鑰/權限風險（S-KEY）

### 7.3 市場完整性硬否決（M-HARD VETO）
- Regime 不可交易或不明確且風險升級（M-REGIME）
- 極端波動狀態（M-VOL）
- 流動性枯竭/點差異常（M-LIQ）
- 市場異常事件旗標（M-EVENT）

### 7.4 組合曝險硬否決（P-HARD VETO）
- 單一標的曝險超標（P-CONC）
- 產業/因子曝險超標（P-SECTOR / P-FACTOR）
- 槓桿/保證金安全邊際不足（P-MARGIN）
- 回撤或損失限制觸發（P-DD / P-LOSS）

### 7.5 執行安全硬否決（E-HARD VETO）
- Kill Switch 不可用或未通過自檢（E-KILL）
- 通道健康檢查失敗（E-CHANNEL）
- 預估滑價超標（E-SLIP）
- 委託量/頻率限制命中（E-RATE）

### 7.6 可退回型否決（RETURN｜不是放行）
- Evidence 不足（RETURN-EVIDENCE；回寫至上游相關層，依 MASTER_CANON 定義）
- 策略在當前 Regime 無適用（RETURN-STRATEGY；回寫至上游相關層，依 MASTER_CANON 定義）
- 流動性不足但可等待（RETURN-LIQUIDITY；回寫至上游相關層，依 MASTER_CANON 定義）

---


## 8. 否決原因碼（Veto Reason Codes｜最大完備版）

格式：`[Domain]-[Category]-[Number]`
Domain：CMP（合規）/ SYS（系統）/ MKT（市場）/ LIQ（流動性）/ PTF（組合）/ EXE（執行）/ GOV（治理一致性）/ REG（Regime）

### 8.1 合規（CMP-*）
- CMP-SESSION-01：非交易時段 / 不允許交易狀態
- CMP-HALT-01：標的停牌/暫停撮合/不可交易
- CMP-RULE-01：交易所規則限制觸發（含漲跌幅/分盤/處置）
- CMP-BROKER-01：券商/通道限制觸發（含下單頻率/額度/權限）
- CMP-VERSION-01：規則版本不可追溯/未同步（制度風險）

### 8.2 系統（SYS-*）
- SYS-AUDIT-01：缺 correlation_id / 審計物不完整
- SYS-HASH-01：hash 驗證失敗（資料被改/不一致）
- SYS-VERSION-01：文件/政策/模型版本不一致
- SYS-PROV-01：資料來源不可追溯（provenance 斷裂）
- SYS-TIME-01：時間不同步（時鐘偏移/交易日判定錯）
- SYS-KEY-01：金鑰/敏感資訊風險
- SYS-VERIFY-01：風控結果不可驗證（不可重算/不可回放）

### 8.3 市場與流動性（MKT/LIQ-*）
- MKT-REGIME-01：Regime 判定不可交易
- MKT-REGIME-02：Regime 不明確且風險升級
- MKT-VOL-01：極端波動（Vol spike）
- MKT-EVENT-01：重大事件風險旗標（事件期禁入）
- LIQ-DEPTH-01：委買委賣深度不足
- LIQ-SPREAD-01：點差異常
- LIQ-VOL-01：成交量不足（低量風險）

### 8.4 組合（PTF-*）
- PTF-CONC-01：單一標的集中度超標
- PTF-SECTOR-01：產業集中度超標
- PTF-FACTOR-01：因子曝險集中超標
- PTF-MARGIN-01：保證金/槓桿安全邊際不足
- PTF-DD-01：回撤門檻觸發
- PTF-LOSS-01：損失門檻觸發
- PTF-CORR-01：相關性集中（隱性集中）超標

### 8.5 執行（EXE-*）
- EXE-KILL-01：Kill Switch 不可用/未通過自檢
- EXE-CHANNEL-01：通道健康檢查失敗（延遲/斷線/回報異常）
- EXE-SLIP-01：預估滑價超標
- EXE-RATE-01：下單頻率/速率限制觸發
- EXE-DUP-01：疑似重複下單風險（狀態不一致）

### 8.6 治理一致性（GOV-*）
- GOV-FLOW-01：流程跳層或不完整（違反 ARCH_FLOW）
- GOV-DOC-01：引用非 Index 文件（違反 DOCUMENT_INDEX）
- GOV-SCOPE-01：治理狀態 後越界變更（最大完備＋累積式更新 違規）

---


## 9. 風控門檻（Thresholds）治理規則（最大完備）

注意：門檻值屬「可配置政策」，不得硬寫死於程式碼。
本文件定義「門檻治理結構」與「必需存在的門檻種類」。
具體數值由 `Risk Policy Profile`（風控政策檔）管理，且必須版控與可回放（VERSION_AUDIT）。

### 9.1 必備門檻種類（Policy Must-Haves）
- 波動門檻：`vol_limit`
- 流動性門檻：`min_depth`, `max_spread`, `min_volume`
- 滑價門檻：`max_slippage_bps`
- 集中度門檻：`max_single_name_weight`, `max_sector_weight`
- 槓桿/保證金門檻：`min_margin_ratio`
- 回撤/損失門檻：`max_drawdown`, `max_daily_loss`, `max_weekly_loss`
- 下單頻率/速率門檻：`max_orders_per_min`, `max_cancel_rate`
- Regime 禁入門檻：`regime_blocklist`, `regime_confidence_min`
- 事件禁入門檻：`event_blackout_window`
- 系統健康門檻：`max_latency_ms`, `max_clock_skew_ms`, `audit_required=true`

### 9.2 門檻變更（最大完備＋累積式更新 + 可追溯）
任何門檻變更必須：
- 生成 `policy_version`（不可覆寫）
- 記錄 `change_id / reason / approver / effective_time`
- 保障舊回放可重算（Replay Compatible）

---


## 10. Risk PASS Token（放行憑證）規範

### 10.1 目的
防止任何模組（含人類 UI）繞過風控直接進入執行層。

### 10.2 Token 最小欄位
- `token_id`
- `correlation_id`
- `policy_version`
- `gate_decision=PASS`
- `issued_at`
- `expires_at`
- `input_hash_ref`（Evidence/State 版本）
- `signature/hash`（防偽）

### 10.3 Token 驗證規則
- EXECUTION_CONTROL 必須在下單前驗證：
  - token 未過期
  - correlation_id 一致
  - policy_version 存在且可回放
  - signature/hash 驗證成功
- 驗證失敗：視為 **SYS-VERSION / SYS-VERIFY** 類 VETO（並觸發急停保護）

---


## 11. UI 呈現義務（UI Must-Show｜不可模糊）

UI 詳規在 UI_SPEC；本節定義 RISK 必須交付 UI 的「不可省略欄位」。

UI 必須顯示：
- PASS / VETO（不可用模糊詞）
- Veto Reason Codes（可展開）
- 對應 證據快照（可點開）
- policy_version（可追溯）
- correlation_id（可稽核）
- 若為 RETURN：必須顯示「退回原因」與「需補齊清單」

禁止：
- 用「建議」「可能」「注意」取代否決
- 遮蔽否決原因碼
- 以績效圖表弱化風險揭露（風險揭露優先於績效）

---


## 12. 審計與回放（Audit / Replay）— Risk 專屬輸出

### 12.1 必備審計物（Artifacts）
- `risk_gate_decision.json`（或等價結構化輸出）
- `veto_reason_codes[]`
- `policy_version`
- `evidence_snapshot_ref`
- `regime_state_ref`
- `account_state_ref`
- `token_ref`（PASS 時）

### 12.2 「無審計 = 未放行」
- PASS 若缺上述任一審計物：
  - 視為 SYS-AUDIT-01，並觸發 VETO
- Replay 必須可重建：
  - 當下 Evidence/Regime/Policy/Account 的一致狀態

---


## 13. 不同運行模式的一致性（No Downgrade）

| 模式 | Risk/Compliance 是否生效 | 說明 |
|---|---|---|
| Research | 必須生效 | 防研究捷徑污染制度 |
| Backtest | 必須生效 | 回測要對齊實盤語義 |
| Simulation | 必須生效 | 驗證流程完整性 |
| Paper | 必須生效 | 與 Live 同構 |
| Live | 必須生效 | 合規/追責必需 |

禁止任何模式以「方便」降低風控級別。

---


## 14. 禁止事項（Forbidden｜一票否決）

- 任何形式的「人類覆寫風控否決」
- 以績效、勝率、回測曲線要求放行
- 以主觀緊急性跳過 Gate
- 以非 Index 文件或非官方來源裁決制度
- 未取得 Risk PASS Token 即進入 EXECUTION_CONTROL
- 以「文字備註」取代 reason_code
- 事後補審計（不得回填）

---


## 15. 與其他核心文件的邊界（Boundary）

- MASTER_ARCH：定義鐵律（本文件不得推翻）
- MASTER_CANON / ARCH_FLOW：定義流程（本文件只定義 Gate 與中斷理由）
- EXECUTION_CONTROL：定義如何下單/急停（本文件定義「可不可以」）
- VERSION_AUDIT：定義版本帳本與可追溯（本文件提供必需的 version_ref 與 artifacts）
- TWSE_RULES：收錄交易規則參考與觸發映射（本文件提供合規 Gate 的「裁決規則骨架」）

---


## 17. 終極裁決語句（不可更改）

只要存在不可接受風險，
就算錯過機會，也必須選擇不交易。

---

## 稽核區塊（Audit Section｜非正文）

### 1) Changelog（變更紀錄）
- 2026-01-11：Final QA 正文化覆蓋版；去除箭頭順位與字母標籤等非正文助記，正文措辭正規化與結構重排（不縮減制度條文），並重建稽核四件套與重算指紋。

### 2) 指紋清單（Hash Manifest）
- BODY_SHA256：eba8304c11bd7f4fc4bd0dc133ad975856d10a1f8ac3896f15a4bd514aa0e9b0

### 3) Scope（範圍）
- doc_key：RISK_COMPLIANCE
- baseline_date：2026-01-11（Asia/Taipei）
- version_date：2026-01-11（Asia/Taipei）
- scope_statement：本次覆蓋僅涉及正文正文化、去重收斂與結構重排；不變更既有制度裁決邏輯、否決權與約束強度。

### 4) Audit Hand-off（稽核交接）
- authority_basis（自高至低）：DOCUMENT_INDEX、MASTER_ARCH、AI_GOV
- canonical_reference：MASTER_CANON
- prepared_by：TAITS FINAL QA MODE
- handoff_status：READY_FOR_REVIEW
