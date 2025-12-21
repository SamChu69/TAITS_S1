# 📘 TAITS_Decision_Core_Inputs_Index.md
## TAITS 決策核心輸入索引（Decision Core Inputs – Single Allowed List）

---

## 0. 文件定位（必讀）

本文件定義：TAITS 的 Decision Core 在產生最終輸出（TRADE / WAIT / NO_TRADE）時，
**唯一允許引用的輸入項目清單**。

> 除本文件列出的輸入以外：
> - 一律不得直接進入 Decision Core
> - 必須先被歸類到 Evidence / Gate / Governance 層
> - 並在該層完成「可否決、可降權、可關閉」治理

此文件屬於：[SPEC] + [GOV] 交界的「硬約束索引」。

---

## 1. Decision Core 的唯一輸出（不可更改）

Decision Core 只能輸出其一：

- TRADE
- WAIT
- NO_TRADE

Decision Core 不負責：
- 預測價格
- 輸出多個互斥結論
- 直接產生下單指令（Execution 層處理）

---

## 2. 輸入分類（由高到低，權限遞減）

Decision Core 的輸入分成四大類，且必須依序處理：

1) **Gate Inputs（最高否決）**
2) **Risk Budget Inputs（風險與曝險上限）**
3) **Evidence Inputs（證據解讀）**
4) **Governance Inputs（策略治理與可用性）**

> 原則：Gate > Risk > Evidence > Governance >（策略訊號）

---

## 3. Gate Inputs（最高否決權）

### G1｜Market Regime State
- 允許值（範例）：TREND / RANGE / HIGH_VOL / EVENT_DISTORTION
- 規則：Regime 不相容 → 禁止任何策略啟用 → NO_TRADE 或 WAIT

### G2｜Manipulation Risk Level（MR）
- 允許值：MR-0 / MR-1 / MR-2 / MR-3
- 規則：
  - MR-3 → 強制 NO_TRADE
  - MR-2 → 降權、降倉、禁追價、禁加碼
  - MR-0~1 → 正常

### G3｜Compliance / Hard Blocks
- 允許值：PASS / BLOCK
- 規則：BLOCK → NO_TRADE

> Gate Inputs 的任何一項不通過，Decision Core 不得往下處理。

---

## 4. Risk Budget Inputs（風險預算與曝險約束）

### R1｜Max Exposure Policy
- 內容：最大持倉比例、單筆最大風險、單日最大損失等

### R2｜Position Sizing Mode
- 內容：依 Regime/MR 決定「允許倉位上限」與「加碼是否允許」

### R3｜Drawdown / Stop State
- 內容：回撤狀態（例如：NORMAL / CAUTION / LOCKDOWN）
- 規則：LOCKDOWN → NO_TRADE 或僅允許減倉行為

---

## 5. Evidence Inputs（證據，不是進場按鈕）

Evidence 必須以「可被引用的證據」形式提供（不可直接等同下單）：

### E1｜Market Structure Evidence（含威科夫）
- 內容：吸籌/派發、UT/UTAD、Spring 等「證據標記」
- 用法：偏向否決與降權（避免被割）

### E2｜Fundamental Evidence（基本面）
- 內容：財報品質、估值區間、安全邊際、產業趨勢（Explore 主導）

### E3｜News/Sentiment Evidence（消息/情緒）
- 內容：可信度、熱度、風險提示（可導致 WAIT/NO_TRADE）

### E4｜Cross-Market Evidence（期貨/選擇權影響）
- 內容：僅允許作為 Regime/Filter/Weight Adjuster
- 禁止：不可作為直接「方向預測」或「進場保證」

### E5｜Uncertainty Flags（不確定性旗標）
- 內容：波動擴張、分布不穩、模型不確定性（例如 Kronos 類）
- 規則：只能降權/降倉/提高 NO_TRADE 傾向，禁止當作 Alpha

---

## 6. Governance Inputs（策略治理輸入）

### S1｜Strategy Group Availability
- 內容：當前允許啟用的策略群（由 Regime/MR 決定）
- 規則：不在允許群組內 → 即使訊號成立也不得進場

### S2｜Decision Lane Enablement（Multi-Lane）
- 內容：Lane A/B/C 是否允許存在（不是固定比例）
- 規則：Lane 未被允許 → 視為不存在

### S3｜Signal Consensus Summary（匯總，不是細節）
- 內容：策略融合後的「摘要分數/信心」而非每條訊號原始值
- 規則：不得以單一訊號繞過 Gate 與 Governance

---

## 7. 明確禁止輸入（Hard Prohibited）

以下輸入不得直接進入 Decision Core：

- 下一根 K 線方向/價格預測值（單獨使用）
- 「模型說會漲所以要加碼」類推論
- 未經驗證的單一消息
- 未經治理的自定義指標（必須先進 Evidence 層與 Governance 層）

---

## 8. Decision Core 執行順序（固定）

1) 讀 Gate Inputs → 任一否決則結束
2) 套用 Risk Budget → 設定曝險上限
3) 讀 Evidence → 形成「可被引用」的風險/優勢摘要
4) 讀 Governance → 限定可用策略與 Lane
5) 輸出 TRADE / WAIT / NO_TRADE（唯一）

---

## 9. TAITS 官方準則（可引用）

> TAITS 的 Decision Core 不追求預測，
> 只追求在 Gate 允許的情況下，
> 用證據與治理做出單一可執行決策，
> 並保留 NO_TRADE 作為最高品質選項。
