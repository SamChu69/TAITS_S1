# 05_risk_compliance_trigger_conditions__風險與合規觸發條件.md

<!--
SOURCE_TAG
原始文件：
- TAITS_AI_行為與決策治理最終規則全集__251217.md
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md
原文範圍：
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md：
  - §1 最高鐵律（Hard Gates｜一票否決）
  - §3 RISK_COMPLIANCE 在 Canonical Flow 的定位（L7 Gate）
  - §4 風險/合規裁決層級與優先序（Risk Hierarchy）
  - §6 Gate 結構與執行順序（C→S→M→P→E→X）
  - §7 否決條件全集（Veto Conditions｜不可弱化）含 7.1–7.5
  - §10 Risk PASS Token（放行憑證）規範（含驗證失敗即 VETO）
  - §11 UI 呈現義務（VETO/RETURN 顯示義務）
  - §12 審計與回放（無審計＝未放行）
- TAITS_AI_行為與決策治理最終規則全集__251217.md：涉及「Risk/Compliance 可否決一切」「不得 Soft Pass」「不得覆寫 VETO」之對齊條款（文件內相關段落）
-->

> doc_key：RISK_COMPLIANCE（Trigger Conditions 工程拆解）  
> 治理等級：A（Risk & Compliance Supreme Veto）  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
> 版本狀態：ACTIVE（Only-Add）  
> 變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化/偷換定義）  

---

## 1. 觸發條件之定義（Trigger Conditions）

本文件所稱「觸發條件」是指：

- 在 L7（Risk & Compliance Gate）內，任一 Gate 或任一條件命中後，
- 必須產生 **明確的裁決型輸出**（PASS / VETO；或明確標註為 RETURN 類型者），
- 並輸出 **reason_code**（不可空）與可回放之證據引用。 :contentReference[oaicite:0]{index=0}

---

## 2. Gate 執行順序與觸發語義（C→S→M→P→E→X）

### 2.1 Gate 順序（高→低）
- C → S → M → P → E → X :contentReference[oaicite:1]{index=1}

### 2.2 觸發即短路（Short-circuit）
- **任何 Gate VETO：立即停止後續 Gate 計算**（節省資源，避免事後辯護）。 :contentReference[oaicite:2]{index=2}

---

## 3. 觸發條件總則（適用所有 Gate）

### 3.1 觸發可新增、不可移除（Only-Add）
- 可新增條件，但不得移除既有條件。 :contentReference[oaicite:3]{index=3}

### 3.2 命中即裁決（Match → Decision）
- 任一條件命中即 **VETO**（除非明確標註為 **RETURN** 類型）。 :contentReference[oaicite:4]{index=4}

### 3.3 理由碼必填（Reason Code Required）
- 所有觸發條件必須對應 **reason_code（不可空）**。 :contentReference[oaicite:5]{index=5}

---

## 4. 觸發條件全集（Veto Conditions｜不可弱化）

> 本節為「觸發條件的核心清單」，其內容以 reason_code 命名為準；任何新增只能加新條件/新碼，不得改寫既有碼的語義。

### 4.1 C-Gate｜合規硬否決（C-HARD VETO）
觸發條件（命中即 VETO）：
- 非交易時段 / 不允許交易狀態（`C-SESSION`）  
- 標的不可交易（停牌/終止/暫停撮合等）（`C-HALT`）  
- 交易規則限制命中（漲跌幅/分盤/處置相關硬限制）（`C-RULE`）  
- 券商 / 通道限制命中（`C-BROKER`）  
- 法規 / 規則版本不可追溯或失效（`C-VERSION`） :contentReference[oaicite:6]{index=6}

### 4.2 S-Gate｜系統安全硬否決（S-HARD VETO）
觸發條件（命中即 VETO）：
- 缺審計（correlation_id / hash / artifact 缺漏）（`S-AUDIT`）  
- 版本不一致（doc/policy/model mismatch）（`S-VERSION`）  
- 資料來源不可追溯（provenance 斷裂）（`S-PROV`）  
- 風控計算不可驗證（`S-VERIFY`）  
- 金鑰/權限風險（`S-KEY`） :contentReference[oaicite:7]{index=7}

### 4.3 M-Gate｜市場完整性硬否決（M-HARD VETO）
觸發條件（命中即 VETO）：
- Regime 不可交易或不明確且風險升級（`M-REGIME`）  
- 極端波動狀態（`M-VOL`）  
- 流動性枯竭 / 點差異常（`M-LIQ`）  
- 市場異常事件旗標（`M-EVENT`） :contentReference[oaicite:8]{index=8}

### 4.4 P-Gate｜組合曝險硬否決（P-HARD VETO）
觸發條件（命中即 VETO）：
- 單一標的曝險超標（`P-CONC`）  
- 產業/因子曝險超標（`P-SECTOR` / `P-FACTOR`）  
- 槓桿/保證金安全邊際不足（`P-MARGIN`）  
- 回撤或損失限制觸發（`P-DD` / `P-LOSS`） :contentReference[oaicite:9]{index=9}

### 4.5 E-Gate｜執行安全硬否決（E-HARD VETO）
觸發條件（命中即 VETO）：
- Kill Switch 不可用或未通過自檢（`E-KILL`）  
- 通道健康檢查失敗（`E-CHANNEL`）  
- 預估滑價超標（`E-SLIP`）  
- 委託量 / 頻率限制命中（`E-RATE`） :contentReference[oaicite:10]{index=10}

---

## 5. Token 與審計作為「必然觸發器」

### 5.1 Risk PASS Token 驗證失敗即觸發否決
- EXECUTION_CONTROL 下單前必須驗證：
  - token 未過期
  - correlation_id 一致
  - policy_version 存在且可回放
  - signature/hash 驗證成功
- 驗證失敗：視為 **SYS-VERSION / SYS-VERIFY 類 VETO**（並觸發急停保護）。 :contentReference[oaicite:11]{index=11}

### 5.2 無審計＝未放行（審計缺漏直接觸發否決）
- PASS 若缺「必備審計物」任一項：視為 `SYS-AUDIT-01 → VETO`。 :contentReference[oaicite:12]{index=12}

---

## 6. UI 對觸發條件的呈現義務（不可模糊）

- UI 必須顯示：
  - PASS / VETO（不可用模糊詞）
  - Veto Reason Codes（可展開）
  - 對應 Evidence Snapshot（可點開）
  - policy_version（可追溯）
  - correlation_id（可稽核）
  - 若為 RETURN：必須顯示「退回原因」與「需補齊清單」 :contentReference[oaicite:13]{index=13}
- 禁止：
  - 用「建議」「可能」「注意」取代否決
  - 遮蔽否決原因碼
  - 以績效圖表弱化風險揭露（風險揭露優先於績效） :contentReference[oaicite:14]{index=14}

---

（End of 05_risk_compliance_trigger_conditions__風險與合規觸發條件）
