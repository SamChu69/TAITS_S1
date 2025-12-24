# 04_risk_compliance_veto_authority__風險與合規最高否決權.md

<!--
SOURCE_TAG
原始文件：
- TAITS_AI_行為與決策治理最終規則全集__251217.md
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md
原文範圍：
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md：全文（0–17 章）
- TAITS_AI_行為與決策治理最終規則全集__251217.md：涉及「Risk/Compliance 可否決一切」「不得 Soft Pass」「不得以績效辯護否決」「Human 不得覆寫 VETO」之相關段落（全文內對應條款）
-->

# TAITS_風險控管與合規最高否決權（RISK_COMPLIANCE）__251219
doc_key：RISK_COMPLIANCE  
治理等級：A（最高否決權憲章｜Risk/Compliance Supremacy）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（最高否決權規範，Only-Add 演進）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：ARCH_FLOW / FULL_ARCH / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / DATA_SOURCES / DEPLOY_OPS / LOCAL_ENV / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化否決權/偷換定義）  
核心裁決：Binary PASS/VETO；VETO 不可被覆寫；無審計＝未放行；Risk PASS Token 為 L11 唯一放行憑證

---

## 0. 文件定位（Risk & Compliance Charter｜最高否決權憲章）

本文件為 TAITS 的 **Risk/Compliance 最高否決權憲章**，目的在於：

- 將「風險控管」與「合規」提升為 **全系統最高 Gate（L7）**
- 定義 **PASS / VETO** 的唯一合法輸出型態（Binary Compliance）
- 定義 **否決條件全集（Veto Conditions）** 的不可弱化規則
- 定義 **Risk PASS Token**（放行憑證）之規範：L11 無 Token 不得執行
- 定義 UI 必須呈現的否決原因碼與證據快照（不可模糊）
- 定義 Risk 專屬審計與回放輸出（Audit / Replay）

📌 本文件不做的事（避免越權）：
- 不定義策略（策略在 STRATEGY_UNIVERSE）
- 不定義執行細節（執行在 EXECUTION_CONTROL）
- 不改寫 Canonical Flow（以 MASTER_CANON / ARCH_FLOW 為準）
- 不替代官方制度裁決入口（制度以 TWSE_RULES 與官方公告為準）

---

## 1. 最高鐵律（Hard Gates｜一票否決）

### 1.1 Risk / Compliance 的法定位階（不可動搖）
- Risk/Compliance 是 TAITS 全系統最高否決 Gate。
- 一旦 VETO 成立：
  - 流程必須停止或退回（依上位流程定義）
  - 不得以任何理由通融
  - 不得以績效辯護否決
  - 不得由 Human 或 AI 覆寫 VETO

### 1.2 Binary Compliance（非黑即白）
- Risk/Compliance 對外輸出只能是：
  - PASS（放行）
  - VETO（否決）
- 禁止：
  - Soft Pass
  - 灰色放行
  - 以「警告」取代 VETO

### 1.3 Worst-case First（最壞情境優先）
- 若存在不確定性或缺證據：
  - 預設採最壞情境推定
  - 以保守否決/退回為優先

### 1.4 Evidence First（沒有證據不得放行）
- 沒有足夠 Evidence：
  - 不得 PASS
  - 必須 RETURN / VETO（依條件）
- Evidence 必須可追溯、可回放、可審計

### 1.5 Regime 高於策略
- Regime（L6）為 Risk（L7）裁決之必要上游條件：
  - Regime 不明確或不可交易：Risk 不得放行
  - 策略不得以任何理由繞過 Regime 約束

---

## 2. 官方制度與資料來源（Official Sources｜必須掛上來源入口）

- 市場制度、撮合規則、交易限制：
  - 必須指向官方制度入口（TWSE / TPEX / TAIFEX / FSC / MOPS 等）
  - 不得以第三方裁決制度
- Risk/Compliance 的裁決引用，必須可回指：
  - 來源入口
  - 當下版本快照（Rulebook Snapshot）

---

## 3. RISK_COMPLIANCE 在 Canonical Flow 的定位（L7 Gate）

### 3.1 所屬層級
- Canonical Flow：L7（Risk & Compliance）

### 3.2 上游輸入（Inputs）
Risk Gate 的裁決輸入至少包含：
- Evidence Bundle（L5）
- Regime State（L6）
- Account / Portfolio 狀態（曝險、持倉、資金）
- Rules / Policy（合規與風控門檻快照）
- Mode（Research / Backtest / Simulation / Paper / Live）

### 3.3 Gate 輸出（Outputs）
Risk Gate 對外輸出必須是：
- `PASS` 或 `VETO`
- `reason_codes[]`（原因碼集合，VETO 必須具備）
- `risk_pass_token`（僅 PASS 時簽發）
- `risk_snapshot_ref`（證據/版本/門檻快照引用）

---

## 4. 風險/合規裁決層級與優先序（Risk Hierarchy）

- Compliance（合規）優先於一切：任何合規不成立 → 直接 VETO
- System Safety（系統安全）優先於策略與績效
- Market Integrity（市場完整性）優先於執行便利
- Liquidity/Slippage（流動性/滑價）優先於預期收益
- Portfolio/Exposure（曝險/組合）優先於單筆機會
- Execution/Operational（執行/營運）優先於「想成交」
- Strategy Risk（策略風險）僅作相容性與限制映射，不得取代以上層級

---

## 5. 風險分類體系（Risk Taxonomy｜最大完備）

### 5.1 Compliance Risk（合規風險）
- 交易規則違反
- 監管限制違反
- 黑名單/禁交易標的
- 不合規來源或缺乏制度引用

### 5.2 System Risk（系統風險）
- 系統異常、時鐘漂移、資料延遲/缺漏
- 審計不可寫入、版本映射缺失
- Kill Switch / Circuit Breaker 不可用
- 關鍵模組健康度不足

### 5.3 Market Risk（市場風險）
- 市場不可交易狀態（由 Regime 或制度判定）
- 異常波動、跳空、事件風險（以證據呈現）

### 5.4 Liquidity & Slippage Risk（流動性/滑價風險）
- 流動性不足
- 預期滑價超限
- 交易單位限制造成成交不可控（特別是零股）

### 5.5 Portfolio / Exposure Risk（曝險/組合風險）
- 淨曝險超限
- 單一標的/產業集中度超限
- 相關性風險超限
- 槓桿/保證金（若未啟用則視為不允許）

### 5.6 Execution / Operational Risk（執行/營運風險）
- 券商通道不穩、回報異常
- 下單失敗率過高
- 對帳/回放鏈路不完整

### 5.7 Strategy Risk（策略風險，僅作相容性與限制映射）
- 策略不支援當前交易單位/模式
- 策略宣告條件未滿足（Meta 不一致）

---

## 6. Gate 結構（Risk Gate Architecture）

### 6.1 Gate 分層（內部結構，仍對外輸出 PASS/VETO）
- Compliance Rules Engine
- System Safety Checker
- Market/Regime Eligibility Checker
- Liquidity/Slippage Checker
- Portfolio Exposure Analyzer
- Execution/Operational Readiness Checker
- Strategy Compatibility Checker（僅相容性）

### 6.2 Gate 執行順序（高 → 低）
1) Compliance
2) System Safety
3) Market/Regime
4) Liquidity/Slippage
5) Portfolio/Exposure
6) Execution/Operational
7) Strategy Compatibility

---

## 7. 否決條件全集（Veto Conditions｜不可弱化）

### 7.1 合規硬否決（C-HARD VETO）
- 任何制度/合規不成立
- 缺少官方制度引用或不可回指
- 禁交易標的/禁交易時段/禁交易狀態
- 其他合規規則命中（依 policy）

### 7.2 系統安全硬否決（S-HARD VETO）
- 审计不可写入 / 版本映射缺失
- Kill Switch 不可用
- 关键模块 DOWN / 不可恢复退化
- 数据时间戳异常、时钟漂移超限（依 policy）

### 7.3 市場完整性硬否決（M-HARD VETO）
- Regime 判定不可交易或不明確
- 市场状态异常且证据不足以放行
- 重大事件/处置状态（以制度与证据为准）

### 7.4 組合曝險硬否決（P-HARD VETO）
- 净曝险超限
- 单一标的/产业集中超限
- 组合风险指标超限（依 policy）

### 7.5 流動性/滑價硬否決（L-HARD VETO）
- 流动性不足以满足最小执行安全条件
- 预期滑价超限
- 零股成交不可控且无法满足保守条件（依 policy）

### 7.6 執行/營運硬否決（E-HARD VETO）
- 券商通道不稳定、回报异常
- 订单状态机不可用或去重保护失效
- 对账/回放链路不可用（无审计＝未放行）

---

## 8. 原因碼（Reason Codes）規範（不可缺）

- 任何 VETO 必须输出 `reason_codes[]`
- reason codes 必须可映射到：
  - 风险分类（Taxonomy）
  - 对应证据快照（refs）
  - 对应 policy 版本（version_ref）
- 原因码分域（示例命名结构）：
  - `C-*` 合规
  - `SYS-*` 系统
  - `MKT/LIQ-*` 市场与流动性
  - `PTF-*` 组合
  - `EXE-*` 执行
  - `GOV-*` 治理一致性

---

## 9. 風控門檻（Thresholds）治理規則（最大完備）

### 9.1 必備門檻種類（Policy Must-Haves）
- 合规门槛
- 系统健康门槛
- 市场/Regime 可交易门槛
- 流动性/滑价门槛
- 曝险/集中度门槛
- 执行/营运门槛

### 9.2 門檻變更（Only-Add + 可追溯）
- 门槛规则必须版本化
- 变更必须可追溯（VERSION_AUDIT）
- 不得以“优化”为由弱化既有否决权

---

## 10. Risk PASS Token（放行憑證）規範

### 10.1 目的
- Token 是 L7 放行的唯一凭证
- L11 执行必须验证 Token，缺 Token 一律阻断

### 10.2 Token 最小欄位
- `token_id`
- `issued_at`
- `expires_at`（若有）
- `correlation_id`
- `policy_version_ref`
- `evidence_bundle_ref`
- `regime_state_ref`
- `hash_manifest_ref`
- `signature`（不可伪造）

### 10.3 Token 驗證規則
- L11 必须验证：
  - token 未过期（若有）
  - policy_version 一致
  - correlation_id 一致
  - evidence/regime refs 一致
  - signature 有效
- 任何验证失败：BLOCK

---

## 11. UI 呈現義務（UI Must-Show｜不可模糊）

- UI 必须呈现：
  - PASS/VETO 状态
  - reason codes（尤其 VETO）
  - 风险分类与证据引用
  - policy 版本（version_ref）
  - token 状态（仅 PASS 时）
- 禁止：
  - 用模糊词替代否决
  - 用绩效遮盖风险揭露

---

## 12. 審計與回放（Audit / Replay）— Risk 專屬輸出

### 12.1 必備審計物（Artifacts）
- `risk_gate_decision_ref`
- `reason_codes_ref`
- `policy_snapshot_ref`
- `evidence_snapshot_refs`
- `token_ref`（仅 PASS）
- `active_version_map_ref`

### 12.2 「無審計 = 未放行」
- 若审计物无法生成/落盘：
  - 视为未放行
  - 必须 VETO/BLOCK（依条件）

---

## 13. 不同運行模式的一致性（No Downgrade）

- Research / Backtest / Simulation / Paper / Live：
  - Risk/Compliance 不得降级
  - PASS/VETO 规则一致
  - 审计密度不得降低

---

## 14. 禁止事項（Forbidden｜一票否決）

- Soft Pass
- 以绩效辩护否决
- Human 覆写 VETO
- AI 覆写 VETO
- 无证据放行
- 无审计放行
- 无 Token 执行

---

## 15. 與其他核心文件的邊界（Boundary）

- Canonical Flow：以 MASTER_CANON / ARCH_FLOW 为准
- Execution 细节：以 EXECUTION_CONTROL 为准
- UI 呈现：以 UI_SPEC 为准
- 数据来源：以 DATA_SOURCES 为准
- 制度裁决入口：以 TWSE_RULES 与官方来源为准

---

## 16. 演進規則（Only-Add）

- 本文件只可新增，不可删减、不可覆写、不可弱化否决权
- 新增内容必须保持：
  - 二元裁决（PASS/VETO）
  - VETO 不可覆写
  - 审计与回放不可降级

---

## 17. 終極裁決語句（不可更改）

- Risk/Compliance 可跨层否决
- 任何 VETO：流程必须停止或退回
- 无 Token 不得执行
- 无审计 = 未放行

---

（End of 04_risk_compliance_veto_authority__風險與合規最高否決權）
