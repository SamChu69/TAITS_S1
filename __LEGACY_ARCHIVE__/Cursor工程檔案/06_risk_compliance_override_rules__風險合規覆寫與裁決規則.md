# 06_risk_compliance_override_rules__風險合規覆寫與裁決規則.md

<!--
SOURCE_TAG
原始文件：
- TAITS_AI_行為與決策治理最終規則全集__251217.md
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md
原文範圍：
- AI_GOV：第 4 章（三權分立與責任邊界）／第 12 章（人類最終控制權）
- RISK_COMPLIANCE：第 1 章（最高鐵律）／第 4 章（風險/合規裁決層級與優先序）／第 10–14 章（PASS Token、UI 呈現義務、審計回放、No Downgrade、Forbidden）
-->

---

## 0. 文件定位（本工程檔目的）

本工程檔將 Canonical 的「覆寫 / 裁決」語義，轉譯為工程可落地之**裁決優先序、不可覆寫邊界、放行憑證（Risk PASS Token）驗證規則、禁止事項**，供後續系統落地時作為 L7 Gate（Risk & Compliance Layer）之裁決基準。

> 注意：本檔不新增制度；僅轉譯既有 Canonical 原文語義為可實作結構。

---

## 1. 三權分立下的裁決與覆寫邊界（不可混淆）

### 1.1 Risk / Compliance 的責任（只做裁決，不做訊號）
- Risk 只負責：允許 / 否決 / 降級 / 暫停 / 停用；可即時否決（Runtime Veto）；出具理由碼（reason_codes）。
- Risk 不得：生成交易訊號；代替策略做方向性判斷；自動解除否決（恢復必須由人類/治理流程觸發）。

### 1.2 Execution 的責任（只能服從裁決，不得覆寫）
- Execution 只負責：承接策略意圖；**服從 Risk 裁決**；路由交易單位；下單抽象與券商適配；統一出場；失敗處理；全程記錄（Logs / Replay）。
- Execution 不得：修改策略方向（BUY→SELL）；繞過風控；假設一定成交；因為方便而寫死市場規則細節。

### 1.3 不可違反鎖定句（Boundary Non-Negotiable）
> 策略不得包含任何否決邏輯；  
> Risk 不得生成交易訊號；  
> Execution 不得更改策略意圖。

---

## 2. 覆寫與裁決的最高規則（Hard Gates｜一票否決）

### 2.1 Risk / Compliance 可否決一切（覆寫方向為「向下否決」，非「向上通融」）
- Risk / Compliance 可否決：策略、Agent、流程、人類裁決之「執行意圖」。
- 任何 VETO：
  - 必須**立即中止流程**（依 Canonical 所指之 STOP / RETURN 语义）
  - 不得以績效、直覺、緊急性辯護
  - **不得由人類覆寫**（Human Cannot Override Risk）

### 2.2 Binary Compliance（裁決輸出僅允許 PASS / VETO）
- Gate 輸出僅允許：
  - `PASS`
  - `VETO`
- 禁止：
  - 模糊放行（Soft Pass）
  - 條件通融（Conditional Pass）
  - 以人工備註取代規則

### 2.3 Evidence First（沒有證據不得放行）
- 若 Evidence 不完整、不可追溯、不可回放：
  - 視為 SYS 類否決（SYS-AUD / SYS-PROV）

---

## 3. 裁決層級（Risk Hierarchy）與覆寫優先序（高 → 低）

### 3.1 層級排序（高層優先）
1) Compliance（合規）：制度/法規/交易規則硬限制（不可通融）  
2) System Safety（系統安全）：審計、版本、金鑰、資料污染（不可通融）  
3) Market Integrity（市場完整性）：停牌、撮合異常、極端波動、流動性枯竭  
4) Portfolio Safety（組合安全）：曝險、集中度、槓桿、回撤、資金使用  
5) Execution Safety（執行安全）：滑價、委託量、通道健康、Kill Switch 可用性  
6) Strategy Compatibility（策略相容）：Regime/策略條件不符（可 VETO 或 RETURN）

### 3.2 覆寫規則（禁止低層覆寫高層）
- **任何高層級否決：低層級不得覆寫或辯護。**

---

## 4. Risk PASS Token（放行憑證）作為「不可被繞過」的工程裁決鎖

### 4.1 目的
- 防止任何模組（含人類 UI）繞過風控直接進入執行層。

### 4.2 Token 最小欄位（工程必備）
- `token_id`
- `correlation_id`
- `policy_version`
- `gate_decision=PASS`
- `issued_at`
- `expires_at`
- `input_hash_ref`（Evidence/State 版本）
- `signature/hash`（防偽）

### 4.3 Token 驗證規則（EXECUTION_CONTROL 下單前必驗）
- 下單前必須驗證：
  - token 未過期
  - correlation_id 一致
  - policy_version 存在且可回放
  - signature/hash 驗證成功
- 驗證失敗：
  - 視為 **SYS-VERSION / SYS-VERIFY** 類 VETO（並觸發急停保護）

> 工程語義：即使上游顯示 PASS，若 Token 驗證失敗，仍必須以 VETO 結束執行意圖（不可通融）。

---

## 5. UI 呈現義務（不可用 UI 弱化裁決）

### 5.1 UI 必須顯示（不得省略）
- PASS / VETO（不可用模糊詞）
- Veto Reason Codes（可展開）
- 對應 Evidence Snapshot（可點開）
- policy_version（可追溯）
- correlation_id（可稽核）
- 若為 RETURN：必須顯示「退回原因」與「需補齊清單」

### 5.2 UI 禁止事項（屬於裁決弱化＝違規）
- 用「建議」「可能」「注意」取代否決
- 遮蔽否決原因碼
- 以績效圖表弱化風險揭露（風險揭露優先於績效）

---

## 6. 審計與回放（Audit / Replay）作為裁決有效性的必要條件

### 6.1 必備審計物（Artifacts）
- `risk_gate_decision.json`（或等價結構化輸出）
- `veto_reason_codes[]`
- `policy_version`
- `evidence_snapshot_ref`
- `regime_state_ref`
- `account_state_ref`
- `token_ref`（PASS 時）

### 6.2 無審計 = 未放行（覆寫規則）
- PASS 若缺上述任一審計物：
  - 視為 SYS-AUDIT-01 → VETO
- Replay 必須可重建：
  - 當下 Evidence / Regime / Policy / Account 的一致狀態

---

## 7. No Downgrade（跨運行模式不可降級覆寫）

| 模式 | Risk/Compliance 是否生效 | 說明 |
|---|---|---|
| Research | 必須生效 | 防研究捷徑污染制度 |
| Backtest | 必須生效 | 回測要對齊實盤語義 |
| Simulation | 必須生效 | 驗證流程完整性 |
| Paper | 必須生效 | 與 Live 同構 |
| Live | 必須生效 | 合規/追責必需 |

- 禁止任何模式以「方便」降低風控級別。

---

## 8. Forbidden（禁止事項＝直接 VETO）

- 任何形式的「人類覆寫風控否決」
- 以績效、勝率、回測曲線要求放行
- 以主觀緊急性跳過 Gate
- 以非 Index 文件或非官方來源裁決制度
- 未取得 Risk PASS Token 即進入 EXECUTION_CONTROL
- 以「文字備註」取代 reason_code
- 事後補審計（不得回填）

---

## 9. 人類最終控制權之「不衝突」解釋邊界（僅限本檔引用的 Canonical）

### 9.1 人類權限語義（存在，但不構成覆寫風控否決）
- approve / veto / pause / resume / freeze

### 9.2 AI 必須遵守（與風控否決不可被覆寫並存）
- AI 只能建議，不能主導
- AI 不得自動解除否決
- AI 不得自動升級交易單位
- 若你指令與制度衝突：AI 必須提醒風險；但仍必須尊重你的最終決定（你是控制者）

> 工程落地語義：本段僅描述「人類主權存在」與「AI 行為限制」，不構成「人類可覆寫 Risk VETO」之授權；因為 RISK_COMPLIANCE 明示禁止「人類覆寫風控否決」。
