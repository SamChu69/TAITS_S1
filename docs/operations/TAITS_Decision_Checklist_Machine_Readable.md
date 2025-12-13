# 📘 TAITS_Decision_Checklist_Machine_Readable.md
## TAITS 機器可讀決策檢查表（Authoritative）

---

## 0. 文件定位（不可模糊）

本文件是 TAITS **唯一允許被執行的決策流程定義**。

- 所有 Decision Engine / Agent / Script
- 必須逐項執行本檢查表
- 不得跳步、不得省略、不得重新排序

> 若人工或 AI 行為與本文件不一致，
> 視為 **系統風控破壞行為**。

---

## 1. Decision Output Enum（唯一合法輸出）

```yaml
DECISION:
  - TRADE
  - WAIT
  - NO_TRADE
````

---

## 2. Gate Layer（最高否決層）

### G1. Market Regime Check

```yaml
G1_MARKET_REGIME:
  allowed:
    - TREND
    - RANGE
  restricted:
    - HIGH_VOL
    - EVENT
  rule:
    if regime in restricted:
      decision_bias: NO_TRADE
```

---

### G2. Manipulation Risk (MR)

```yaml
G2_MANIPULATION_RISK:
  levels:
    MR_0: normal
    MR_1: caution
    MR_2: restricted
    MR_3: blocked
  rules:
    MR_3:
      decision: NO_TRADE
    MR_2:
      constraints:
        allow_entry: true
        allow_add: false
        exposure_cap: LOW
```

---

### G3. Compliance / Hard Block

```yaml
G3_COMPLIANCE:
  status:
    - PASS
    - BLOCK
  rule:
    if status == BLOCK:
      decision: NO_TRADE
```

---

## 3. Risk Layer（風險與曝險）

### R1. System Risk State

```yaml
R1_SYSTEM_STATE:
  states:
    NORMAL:
      trade_allowed: true
    CAUTION:
      trade_allowed: true
      exposure_cap: LOW
    LOCKDOWN:
      trade_allowed: false
```

---

### R2. Exposure Budget

```yaml
R2_EXPOSURE:
  max_single_position_pct: CONFIG
  max_daily_exposure_pct: CONFIG
  allow_add_position:
    default: false
```

---

## 4. Evidence Layer（證據摘要）

### E1. Tier-1 Structural Evidence

```yaml
E1_STRUCTURAL_EVIDENCE:
  signals:
    - DISTRIBUTION
    - FAKE_BREAK
    - SETTLEMENT_DISTORTION
    - MANIPULATION_ALERT
  rule:
    if any(signals == true):
      decision_bias: WAIT_OR_NO_TRADE
```

---

### E2. Tier-2 Contextual Evidence

```yaml
E2_CONTEXTUAL_EVIDENCE:
  fields:
    - FUNDAMENTAL_SUPPORT
    - VALUATION_OK
    - INDUSTRY_TAILWIND
  usage:
    purpose: "determine worth waiting"
    decision_direct: false
```

---

### E3. Tier-3 Tactical Evidence

```yaml
E3_TACTICAL_EVIDENCE:
  allowed_only_if:
    gate_passed: true
    MR <= MR_1
  usage:
    purpose: "timing"
    decision_direct: false
```

---

### E4. Tier-4 Uncertainty Flags

```yaml
E4_UNCERTAINTY:
  flags:
    - VOLATILITY_EXPANSION
    - DISTRIBUTION_UNSTABLE
    - MODEL_UNCERTAINTY
  rule:
    if any(flags == true):
      adjust:
        exposure: DOWN
        bias: WAIT
```

---

## 5. Governance Layer（策略治理）

### S1. Strategy Availability

```yaml
S1_STRATEGY_AVAILABILITY:
  allowed_groups:
    - LANE_A
    - LANE_B
    - LANE_C
  rule:
    if strategy_group not in allowed_groups:
      strategy_state: DISABLED
```

---

### S2. Decision Lane Enablement

```yaml
S2_DECISION_LANE:
  lanes:
    LANE_A: STRUCTURE
    LANE_B: VALUE
    LANE_C: EXECUTION
  rule:
    if lane_disabled:
      ignore_all_signals_from_lane
```

---

## 6. Final Decision Resolver（固定順序）

```yaml
FINAL_DECISION:
  order:
    - Gate
    - Risk
    - Evidence
    - Governance
  resolution:
    if any(Gate.decision == NO_TRADE):
      output: NO_TRADE
    elif Risk.trade_allowed == false:
      output: NO_TRADE
    elif Evidence.bias == WAIT:
      output: WAIT
    else:
      output: TRADE
```

---

## 7. Audit & Logging（必須）

```yaml
AUDIT_LOG:
  required_fields:
    - date
    - regime
    - MR_level
    - system_state
    - evidence_summary
    - decision
```

---

## 8. TAITS 決策鐵律（不可移除）

> Decision Engine 不追求「做最多交易」，
> 只追求「在允許的情境下，做最少但正確的交易」。

---
