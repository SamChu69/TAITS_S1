# TAITS_風險控管與合規最高否決權（RISK_COMPLIANCE）__251219
doc_key：RISK_COMPLIANCE  
治理等級：A（Risk & Compliance Supreme Veto｜高於策略、高於績效、高於主觀）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（最高否決權文件，Only-Add 演進）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX（Index 裁決）  
平行參照：FULL_ARCH / ARCH_FLOW / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化否決權/偷換定義）  
核心裁決：Binary Compliance（PASS / VETO）＋ Worst-case First（最壞情境優先）

---

---

# Addendum 2025-12-27｜Only-Add：MASTER_CANON「S」標籤定位 × Veto 母文件引用口徑對齊 × 裁決字串助記化（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、弱化否決權、偷換既有語義）  
> 適用文件：TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md（doc_key：RISK_COMPLIANCE）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：AI_GOV（A+）＋Index Gate（DOCUMENT_INDEX）＋治理等級覆蓋（A+ > A > B > C）＋衝突裁決程序（DOCUMENT_INDEX §6）  
> 口徑對齊：  
> - MASTER_CANON｜Addendum 2025-12-27（S 標籤定位：Label ≠ Governance Grade）  
> - DOCUMENT_INDEX｜Addendum 2025-12-27（裁決順序字串統一 × 歧義消解）  
> - DOCUMENT_INDEX｜Addendum 2025-12-27-B（B+/C+ 子級標籤定義 × 覆蓋規則對位）〔檔名：TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251220__ADDENDUM_20251227B_FINAL.md〕  
> - GOVERNANCE_GATE_SPEC｜Addendum 2025-12-27（字串助記定位 × 雙軌裁決消歧）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（建議新增條目：`VA-METADATA_FIX-20251227-0008`）  
> 目的：在不改寫本文件任何風險/合規否決權語義的前提下，修補本文件對 MASTER_CANON「治理等級 S」之引用歧義；固定本文件在引用上位文件時的唯一合法口徑，使 Gate / Audit / 回放鏈一致可檢核。

---

## 0. 適用範圍（Hard Boundary）

本 Addendum 僅處理「引用端歧義消解」與「裁決字串法律定位」：
1) MASTER_CANON「S」之法律定位（Label ≠ Governance Grade）  
2) 本文件在引用 MASTER_CANON / DOCUMENT_INDEX / AI_GOV 時的最小合規引用格式  
3) 本文件內「裁決順序字串」之助記化定位（Mnemonic ≠ Override Rule）  

本 Addendum **不**：
- 不改寫任何否決權（VETO）條款、reason_codes、證據要求、保守停止規則  
- 不改寫 Canonical Flow（L1–L11）  
- 不新增新治理層級或重排覆蓋規則（A+ > A > B > C）  
- 不削弱風險與合規最高否決權（如有張力，依既有條款與上位裁決處置）

---

## 1. MASTER_CANON「S」之法律定位（Label ≠ Governance Grade）

### 1.1 統一裁決：S 僅為敘事/版本標籤
凡本文件（含附錄）出現「MASTER_CANON（治理等級 S）」或等價表述，其唯一合法解讀為：

- **S（Supreme Canon）僅為 MASTER_CANON 的敘事/版本定位標籤（Label）**  
- MASTER_CANON 之治理等級／ACTIVE 狀態／doc_key 等身份性中繼資料，**一律以 DOCUMENT_INDEX 表格裁決為準**  
- 因此在治理等級體系中，MASTER_CANON 應視為 DOCUMENT_INDEX 裁決之 **A（Constitutional）｜ACTIVE**（不因 S 標籤而改變覆蓋規則）

> 兼容處理（不改原文）：本文件既有「治理等級 S」字樣保留為歷史敘事標籤；其治理等級法律效力由本 Addendum 限定並對齊 Index。

---

## 2. Veto 母文件的引用口徑（Gate-Friendly Reference）

### 2.1 引用 DOCUMENT_INDEX（合法性/等級/衝突裁決程序）
```text
ref_doc_key = DOCUMENT_INDEX
ref_purpose = index_gate_and_conflict_resolution
ref_section = <例如：§3 / §6 / §7 / §9 / Addendum 2025-12-27 / Addendum 2025-12-27-B>
ref_notes = 覆蓋規則以 A+ > A > B > C 為準；B+/C+ 為子級標籤（bucket 化）
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0008
```

### 2.2 引用 MASTER_CANON（流程語義/層級邊界；S 僅為 Label）
```text
ref_doc_key = MASTER_CANON
ref_purpose = canonical_flow_semantics_and_layer_boundaries
ref_gov_grade = A            # 以 DOCUMENT_INDEX 裁決為準；S 僅為 Label
ref_section = <例如：L7/L10/L11 邊界、衝突裁決秩序段落>
ref_notes = S（Supreme Canon）僅為敘事/版本標籤，不構成新治理層級
```

### 2.3 引用 AI_GOV（AI 行為/越權最高約束）
```text
ref_doc_key = AI_GOV
ref_purpose = ai_behavior_and_non_overreach_constraints
ref_section = <AI 不得補完制度／不得逾權裁決等條款>
```

### 2.4 禁止誤用（不可放寬）
- 禁止將 `ref_gov_grade = S` 作為任何裁決依據  
- 禁止以「S 標籤」推導 MASTER_CANON 可凌駕 DOCUMENT_INDEX 或 AI_GOV  
- 若引用端無法提供必要欄位（doc_key/version/section）：僅允許列缺口，不允許裁決性輸出（尤其不得以推測代替證據）

---

## 3. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）

本文件內若出現任何「裁決順序字串」或箭頭序列（例：`X → Y → Z`）：
- 一律視為閱讀/操作助記（Mnemonic）  
- **不得**被用作覆蓋規則或裁決權重新分配  
- 若與 DOCUMENT_INDEX §3（覆蓋規則）或 §6（衝突裁決程序）產生張力：**一律回到 DOCUMENT_INDEX**（不可跳步）

---

## 4. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫任何既有正文。  
- 本文件的 VETO 條款、reason_codes、證據要求與保守停止規則仍維持原樣，且不因本 Addendum 而弱化。  
- MASTER_CANON 之「S」在本文件中僅為 Label；治理等級回歸 DOCUMENT_INDEX 裁決之 A+ / A / B / C 體系。  
- 缺少引用必要欄位時：依 DOCUMENT_INDEX §6 保守處置，並以 VERSION_AUDIT 留痕。

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）


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

### 1.1 Risk / Compliance 的法定位階（不可動搖）
- **Risk / Compliance 可否決一切**：策略、Agent、流程、人類裁決之「執行意圖」皆可被否決。
- 任何 VETO：
  - **立即中止流程**（依 ARCH_FLOW STOP / RETURN 規則）
  - **不得以績效、直覺、緊急性辯護**
  - **不得由人類覆寫**（Human Cannot Override Risk）

### 1.2 Binary Compliance（非黑即白）
- Gate 輸出僅允許：
  - `PASS`
  - `VETO`
- 禁止：
  - 模糊放行（Soft Pass）
  - 條件通融（Conditional Pass）
  - 以人工備註取代規則

### 1.3 Worst-case First（最壞情境優先）
- 所有風險評估必須以：
  - 交易失敗、滑價擴大、流動性枯竭、撮合異常、制度變動、資料污染
  作為基準情境。
- 禁止以「過去沒發生」作為安全理由。

### 1.4 Evidence First（沒有證據不得放行）
- 若 Evidence 不完整、不可追溯、不可回放：
  - **視為 SYS 類否決（SYS-AUD / SYS-PROV）**

### 1.5 Regime 高於策略
- Regime 判定為不可交易（或 Regime 不明確且風險升級）：
  - 可直接觸發 VETO（REG-VETO）

---

## 2. 官方制度與資料來源（Official Sources｜必須掛上來源入口）

> 本節提供 TAITS 制度/規則/合規的「官方入口」。  
> 實作時不得以非官方網站裁決制度；可用非官方作補充，但不得作最終裁決依據。

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
- Rulebook Snapshot（TWSE/TAIFEX/券商限制/交易時段/停牌等）

### 3.3 Gate 輸出（Outputs）
- `risk_gate_decision`：PASS / VETO
- `veto_reason_codes[]`：若 VETO 必填（不可空）
- `risk_pass_token`：僅 PASS 生成，供 EXECUTION_CONTROL 驗證（不可偽造）
- `risk_evidence_snapshot_ref`：證據快照引用（可回放）

---

## 4. 風險/合規裁決層級與優先序（Risk Hierarchy）

優先序（高 → 低）：
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

### 6.2 Gate 執行順序（高 → 低）
C → S → M → P → E → X  
任何 Gate VETO：立即停止後續 Gate 計算（節省資源，避免事後辯護）。

---

## 7. 否決條件全集（Veto Conditions｜不可弱化）

> 規則設計原則：  
> - 可新增條件，但不得移除既有條件  
> - 任一條件命中即 VETO（除非明確標註為 RETURN 類型）  
> - 所有條件必須對應 reason_code（不可空）

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
- Evidence 不足（RETURN-EVIDENCE → 回到 L4/L5）
- 策略在當前 Regime 無適用（RETURN-STRATEGY → 回到 L6/L8）
- 流動性不足但可等待（RETURN-LIQUIDITY → 回到 L3/L4）

---

## 8. 否決原因碼（Veto Reason Codes｜最大完備版）

> 格式：`[Domain]-[Category]-[Number]`  
> Domain：CMP（合規）/ SYS（系統）/ MKT（市場）/ LIQ（流動性）/ PTF（組合）/ EXE（執行）/ GOV（治理一致性）/ REG（Regime）

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
- GOV-SCOPE-01：Freeze 後越界變更（Only-Add 違規）

---

## 9. 風控門檻（Thresholds）治理規則（最大完備）

> 注意：門檻值屬「可配置政策」，不得硬寫死於程式碼。  
> 本文件定義「門檻治理結構」與「必需存在的門檻種類」。  
> 具體數值由 `Risk Policy Profile`（風控政策檔）管理，且必須版控與可回放（VERSION_AUDIT）。

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

### 9.2 門檻變更（Only-Add + 可追溯）
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

> UI 詳規在 UI_SPEC；本節定義 RISK 必須交付 UI 的「不可省略欄位」。

UI 必須顯示：
- PASS / VETO（不可用模糊詞）
- Veto Reason Codes（可展開）
- 對應 Evidence Snapshot（可點開）
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
  - 視為 SYS-AUDIT-01 → VETO
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

## 16. 演進規則（Only-Add）

允許新增：
- 新的風險類型
- 新的否決條件
- 新的 reason_code
- 新的政策檔 Profile（policy_version）
- 新的 UI 呈現欄位（不得刪舊欄位）

禁止：
- 刪除任何既有否決條件或理由碼
- 弱化否決權
- 改寫既有 reason_code 的語義

---

## 17. 終極裁決語句（不可更改）

> 只要存在不可接受風險，  
> 就算錯過機會，也必須選擇不交易。  

（RISK_COMPLIANCE｜最大完備版 v2025-12-19 完）

---

# Appendix A｜RISK_COMPLIANCE × MASTER_CANON 對位補充（Only-Add）
（Only-Add · Alignment Addendum · Freeze v1.0）

## A.0 補充性質聲明（不可省略）
- 適用文件：RISK_COMPLIANCE（doc_key=RISK_COMPLIANCE）
- 補充類型：Addendum / Alignment Guideline（對位補充；不改寫 Canonical）
- 生效狀態：GOVERNANCE_STATE = Freeze v1.0
- 變更原則：Only-Add（只可新增，不可刪減/覆寫/偷換既有語義）
- 衝突裁決序：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON
- 範圍限定：僅針對本文件與 MASTER_CANON（含附錄 Z）在 **L7 Gate 職責語義、輸入輸出、否決權位階、全紀錄原則與人機分工邊界** 之一致性對位

## A.1 與 MASTER_CANON 的定位差異（法源分工）
> 本節僅用於「裁決對位」，不得被理解為新增 Canonical Flow 或改寫 L1–L11。

### A.1.1 MASTER_CANON（治理等級 S）在本議題的法源角色
MASTER_CANON 負責裁決（與本文件相關者）：
- Canonical Flow（L1–L11）之語義不可變核心（含 L7 的存在性與輸入/輸出語義）
- L7：Risk & Compliance 的 **PASS/VETO 二元裁決**、**禁止 Soft Pass**、**禁止以績效辯護否決**
- L9a/L10/L11 人機分工與全紀錄原則（附錄 Z）：確保「分析敘事」「人類決策」「系統執行」三者不可混用，且所有關鍵結論必須可回指 Evidence（可驗證/可否決/可稽核）

### A.1.2 RISK_COMPLIANCE（治理等級 A）在本議題的法規角色
本文件負責把母法級要求落地為：
- L7 Gate 的 **最高否決權（Supreme Veto）** 制度化定義（位階、不可覆寫、即刻生效）
- 風險分類體系（Risk Taxonomy）、否決條件全集（Veto Conditions）、否決原因碼（Reason Codes）
- Risk PASS Token（放行憑證）之結構、簽章/防偽、有效期、版本引用與審計物要求
- Gate 與 UI 的交付義務（PASS/VETO + reason codes + Evidence/Policy 版本可追溯）
- 審計與回放（Audit/Replay）之最小集合，並與 ARCH_FLOW / VERSION_AUDIT / EXECUTION_CONTROL 形成可對帳的工件鏈

## A.2 對位結論（一致性宣告）
- MASTER_CANON 定義「L7 是什麼、可輸出什麼、禁止什麼」；RISK_COMPLIANCE 定義「如何以制度條文把 L7 落地為可驗證、可否決、可回放」。
- 任何歧義：一律回到 MASTER_CANON 的語義裁決，再以 Only-Add 方式在本文件附錄增補可驗證條件；不得反向改寫母法。

## A.3 MASTER_CANON 的 L7 語義鎖定：對位映射（不改主文）
MASTER_CANON 對 L7 的語義要求（摘要）：
- 目的：對所有意圖做 PASS/VETO 裁決  
- 輸入：Regime State + Evidence + Account/Portfolio + Rules  
- 輸出：PASS / VETO + reason codes + token（PASS only）  
- 禁止：Soft Pass；以績效辯護否決

本文件對位落點（主文既有內容）：
- §1.2 Binary Compliance（PASS/VETO）＝對位「禁止 Soft Pass」
- §3.3 Gate 輸出（PASS/VETO + reason codes + token）＝對位「輸出 token（PASS only）」
- §1.1、§7（否決條件）與 §14（禁止事項）＝對位「不得以績效/直覺/緊急性辯護否決」

---

# Appendix B｜對位 MASTER_CANON 附錄 Z：人機分工邊界對 L7 的限制（Only-Add）
（Only-Add · Boundary Lock for L7 · Freeze v1.0）

## B.0 補充性質聲明
- 適用文件：RISK_COMPLIANCE
- 補充類型：Guideline（邊界鎖定指引；不改寫 Canonical）
- 生效狀態：GOVERNANCE_STATE = Freeze v1.0
- 目的：將 MASTER_CANON 附錄 Z 所述「L9a 敘事 / L10 決策 / L11 執行」不可混用邊界，落到 L7 Gate 的行為限制，避免風控越權或被誤用為「決策替代」。

## B.1 L7 的合法輸出形態（嚴格限制）
L7 對外（供 L9/L10/L11）唯一合法輸出僅允許：
- `risk_gate_decision = PASS | VETO`
- `veto_reason_codes[]`（VETO 必填且不可空）
- `risk_pass_token`（僅 PASS 生成）
- `risk_evidence_snapshot_ref`（可回放）

禁止 L7 輸出：
- 任何交易方向建議、進出場條件建議、標的偏好（屬 L8/L9a 範圍）
- 任何「替代 L10 的批准/拒絕敘事」或情緒性語句（L7 只能裁決 PASS/VETO + 理由碼）
- 任何以 L9a 人話敘事替代 Evidence 的放行（Evidence First）

## B.2 L7 不得被 L9a 影響其裁決語義（Evidence > Narrative）
- 附錄 Z 要求：L9a 的關鍵敘述必須可回指 Evidence，且僅作 L10 參考。
- 因此，L7 的裁決必須以 **Evidence + Rules + Account/Portfolio + Regime** 為唯一有效依據；
- 若輸入中存在僅敘事、無可回指 Evidence 的主張，視為 Evidence 不完整：依主文 §1.4 直接觸發 SYS 類否決（SYS-AUD / SYS-PROV）。

## B.3 L7 與 L10 的不可替代關係（Veto ≠ Decision）
- L7 的 PASS 不是「建議下單」，只是「風險/合規層不否決」。
- L7 的 VETO 不是「投資建議」，而是「制度上禁止進入執行」。
- L10 人類裁決（APPROVE/REJECT/ABORT）不得被 L7 的 PASS 誤解為自動批准；UI 必須明確區隔「PASS」與「APPROVE」。

---

# Appendix C｜L7 全紀錄原則：Risk Gate 工件鏈與 Replay 最小集（Only-Add）
（Only-Add · Audit/Replay Hardening for L7 · Freeze v1.0）

## C.0 補充性質聲明
- 適用文件：RISK_COMPLIANCE
- 補充類型：Appendix（工件鏈補強附錄；不取代主文）
- 生效狀態：GOVERNANCE_STATE = Freeze v1.0
- 目的：對位 MASTER_CANON「可驗證、可否決、可稽核」之全紀錄原則，將 L7 必備工件鏈落地為可被 ARCH_FLOW / VERSION_AUDIT / EXECUTION_CONTROL 一致引用的最小集合。

## C.1 L7 Gate 審計事件最小欄位集（Risk Gate Decision Minimal Fields）
任何一次 L7 Gate 計算（無論 PASS 或 VETO）至少必須寫入：
- `correlation_id`
- `layer_id = L7`
- `timestamp_utc`
- `risk_gate_decision = PASS | VETO`
- `veto_reason_codes[]`（PASS 可空；VETO 不可空）
- `policy_version`
- `rulebook_snapshot_ref`
- `regime_state_ref`
- `evidence_bundle_ref`（或等價引用）
- `account_state_ref`（資金/倉位/未成交/曝險快照引用）
- `input_hash_ref`（Evidence/State 的 hash）
- `output_hash_ref`（決策輸出的 hash）
- `documents_active_map_ref`（ACTIVE 文件版本映射快照）
- `immutability_flag`（append-only/immutable）

缺任一欄位 → 視為 `SYS-AUDIT-01` 或等價否決，並不得產生有效 PASS Token。

## C.2 Risk PASS Token 的「不可否認性」最低要求（對位 EXECUTION_CONTROL）
為確保 EXECUTION_CONTROL 可驗證且不可偽造，本文件主文 §10.2 之 Token 最小欄位在 Freeze v1.0 下補強如下（Only-Add）：
- `token_id`
- `correlation_id`
- `policy_version`
- `issued_at` / `expires_at`
- `gate_decision = PASS`
- `input_hash_ref`（指向 Evidence/Regime/Account/Rules 的 hash 清單或 manifest）
- `documents_active_map_ref`
- `signature`（不可否認簽章/摘要；具可驗證性）
- `scope`（可選；若存在，至少包含 mode 與標的/帳戶範圍之限制，避免 token 跨模式濫用）

Token 若缺 `signature` 或 `documents_active_map_ref` → 視為不可驗證（SYS-VERIFY-01）→ VETO。

## C.3 ARCH_FLOW Replay Bundle 的 L7 子集（Risk Sub-Bundle）
L7 必須能提供 Replay 子集（可被整體 Replay Bundle 引用）：
- `risk_gate_decision_ref`
- `veto_reason_codes[]`
- `policy_version`
- `rulebook_snapshot_ref`
- `risk_pass_token_ref`（PASS only）
- `regime_state_ref`
- `evidence_bundle_ref`
- `account_state_ref`
- `documents_active_map_ref`
- `hash_manifest_ref`

要求：相同 Replay 子集必須可重算得到相同 PASS/VETO 結論；否則視為污染（Pollution）並必須阻斷後續同類執行，直到人工介入。

---

# Appendix D｜L7→L10→L11 交接契約（Handoff Contract）與 UI 呈現補強（Only-Add）
（Only-Add · Handoff Integrity · Freeze v1.0）

## D.0 補充性質聲明
- 適用文件：RISK_COMPLIANCE
- 補充類型：Checklist / Contract Appendix（交接契約附錄；不取代主文）
- 生效狀態：GOVERNANCE_STATE = Freeze v1.0
- 目的：把 L7 Gate 的輸出，規範為 UI（L10）與執行層（L11）可直接驗證的交接契約，防止「PASS 被誤當 APPROVE」「Token 被誤用」「理由碼被遮蔽」。

## D.1 L7→L10（UI）交付欄位（Must-Deliver to UI）
UI（L10）在展示給人類裁決前，必須收到且能呈現：
- `risk_gate_decision`（PASS/VETO，禁止模糊）
- `veto_reason_codes[]`（VETO 必須可展開、不可遮蔽）
- `risk_evidence_snapshot_ref`（可點開回放）
- `policy_version`（可追溯）
- `rulebook_snapshot_ref`（制度快照版本）
- `correlation_id`（稽核主鍵）
- `documents_active_map_ref`（本次運行 Active 版本映射）

UI 禁止：
- 以「建議」「注意」取代 VETO
- 以績效圖表弱化風險揭露（風險揭露優先於績效）
- 在 VETO 時仍允許進入 APPROVE（必須硬阻斷）

## D.2 L7→L11（Execution Control）交付欄位（Must-Deliver to Execution）
當且僅當 `risk_gate_decision=PASS`，L7 必須交付：
- `risk_pass_token_ref`（含 token 可驗證內容）
- `policy_version`
- `documents_active_map_ref`
- `input_hash_ref` / `hash_manifest_ref`

並且明確規範（對位 EXECUTION_CONTROL）：
- L11 送單前必驗：token 未過期、correlation_id 一致、policy_version 存在且可回放、signature 可驗證、scope 不越界
- 驗證失敗：視為 SYS-VERSION / SYS-VERIFY 類 VETO，並觸發執行層保護（BLOCK/SAFE MODE）

## D.3 交接一致性檢查（Consistency Checks｜全部不通過＝BLOCK）
1) PASS ≠ APPROVE  
- UI 必須明確標示：Risk PASS 只是「未否決」，仍需 L10 人類 APPROVE 才能進入 L11。

2) Token 不可跨模式濫用  
- Simulation/Paper/Live 的 token 不得互用；任何不一致屬 `TOKEN_SCOPE_MISMATCH` → BLOCK。

3) Reason Codes 不可空與不可遮蔽  
- VETO 時 reason_codes 必須非空且 UI 可見；遮蔽視為 `SYS-AUDIT` 等價重大缺失 → VETO。

4) Evidence 必須可回放  
- risk_evidence_snapshot_ref 不可用「文字敘事」替代；不可回放視為 Evidence 不完整 → VETO。

---

（RISK_COMPLIANCE｜Only-Add Addendum Pack：Appendix A–D · Freeze v1.0 生效）
---

## Appendix 2025-12-28｜Only-Add：Trace ID / Evidence Chain 最小欄位貫穿（RISK_COMPLIANCE）對齊 DEPLOY_OPS（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md（doc_key：RISK_COMPLIANCE）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：RISK_COMPLIANCE（A）＋EXECUTION_CONTROL（A）＋DOCUMENT_INDEX（A+）＋AI_GOV（A+）  
> 平行對齊：DEPLOY_OPS｜Addendum 2025-12-27（D2/D3：Evidence Chain 最小欄位與結構）  
> 目的：將 Trace ID / Evidence Chain 的「最小可回放欄位」貫穿到本文件所管轄的產物/紀錄/裁決輸出；不改既有流程，只固定最低輸出格式。

### EC1. 最小引用標頭（Minimum Legal Citation Header）
本文件所生成或要求的任何「決策/裁決/執行/呈現」紀錄，至少必須包含下列引用標頭（欄位可多不可少）：

```text
trace_id = <全域唯一>
session_id = <本次對話/流程>
event_id = <本次事件/操作>
actor = <human/agent/module>
timestamp = <ISO-8601>
doc_key = RISK_COMPLIANCE
doc_title = TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:<對應條目（若有）>
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
```

### EC2. Evidence Chain 最小結構（對齊 DEPLOY_OPS D3）
當本文件涉及「可回放產物」或「稽核必需證據」時，Evidence Chain 至少包含：

- `env_fingerprint`（環境指紋）  
- `dependency_manifest`（依賴清單）  
- `run_evidence`（執行證據：命令/時間/產物/日誌）  
- `failure_recovery`（失敗與回復：PASS/FAIL 與處置）

> 欄位定義與格式以 DEPLOY_OPS｜D3 為準；本附錄不重複改寫其語義，僅宣告「必帶」。

### EC3. Gate 行為（缺欄位之保守處置）
- 若缺少 EC1/EC2 最小欄位：不得視為「可回放/可稽核」輸出。  
- 涉及風險/合規裁決時：依 RISK_COMPLIANCE 與 GOVERNANCE_GATE_SPEC 之保守處置機制，採 **STOP/RETURN** 以補齊引用資訊（不得以推測補值）。
---

## Appendix 2025-12-28｜Only-Add：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md（doc_key：RISK_COMPLIANCE）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 Addendum/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`RISK_COMPLIANCE`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=RISK_COMPLIANCE` + `canonical_filename=TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

# Addendum 2025-12-28｜Only-Add：GLOBAL_ALIGNMENT_PATCH（MASTER_CANON 對齊全域補丁）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219__ADDENDUM_20251227_FINAL.md（doc_key：RISK_COMPLIANCE）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0021`）  
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

- 本文件 `doc_key` 既有標示為 `RISK_COMPLIANCE`；本 Addendum 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

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
