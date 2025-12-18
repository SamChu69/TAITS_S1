# TAITS_全系統架構總覽（FULL_ARCH）

doc_key: FULL_ARCH  
治理等級: B（系統架構治理級）  
版本日期: 2025-12-19  
對齊母法: TAITS_AI_行為與決策治理最終規則全集__251217  
變更原則: Only-Add（禁止覆寫、禁止刪改）

---

## §0 文件憲政定位（不可覆寫）

本文件為 **TAITS 系統「靜態結構與權力邊界」之最高說明文件**。

- 本文件裁定「有哪些模組」
- 本文件裁定「模組能做什麼、不能做什麼」
- 本文件 **不描述流程（交由 ARCH_FLOW）**
- 本文件 **不描述策略內容（交由 STRATEGY_UNIVERSE）**

📌 若任何文件與本文件衝突：
→ **本文件優先**

---

## §1 架構治理最高鐵律（Hard Gates）

### §1.1 AI 不得成為系統主體（AI_GOV §1, §4）
- AI 僅存在於「分析／輔助層」
- AI 不得：
  - 生成最終決策
  - 直接影響 Execution
  - 擁有任何模組主權

### §1.2 策略 ≠ 系統（AI_GOV §6）
- Strategy 永遠是輸入物件
- 系統結構不可因策略存在而改變

### §1.3 Regime 高於一切訊號（AI_GOV §4）
- Regime Engine 具否決權
- 單一訊號不得凌駕 Regime

---

## §2 系統層級與模組總覽（L1–L11）

| Layer | 模組 | 權限 |
|---|---|---|
| L1 | Data Source | 僅收集 |
| L2 | Data Normalization | 僅清洗 |
| L3 | Feature Engine | 僅特徵 |
| L4 | Evidence Builder | 僅描述 |
| L5 | Regime Engine | 狀態裁定 |
| L6 | Strategy Universe | 可用性 |
| L7 | Risk & Compliance | 最高否決 |
| L8 | Decision Interface | 人類裁決 |
| L9 | Execution Control | 嚴格執行 |
| L10 | Audit Engine | 全程留痕 |
| L11 | Version Engine | Only-Add |

---

## §3 模組權限與禁止事項（逐模組裁決）

### Feature Engine
- ✅ 允許：數值、結構化特徵
- ❌ 禁止：方向、買賣、信號

### Strategy Universe
- ✅ 允許：白名單管理
- ❌ 禁止：直接產生交易

### Execution Control
- ✅ 允許：依裁決執行
- ❌ 禁止：自行判斷、補單

（其餘模組同理，不得越權）

---

## §4 模組間「永久禁止通訊矩陣」

| From | To | 判定 |
|---|---|---|
| Strategy | Execution | ❌ |
| AI | Execution | ❌ |
| Feature | Decision | ❌ |
| Execution | Strategy | ❌ |

違反即構成 **治理失效事件**。

---

## §5 審計輸出（Audit Artifacts）

每一模組 **必須產出**：
- module_id
- input_hash
- output_hash
- timestamp
- correlation_id
- version_ref

📌 無審計紀錄 = 未發生。

---

## §6 Freeze 規則

- Freeze 後：
  - 模組結構 ❌ 不可變更
  - 僅允許新增審計說明（Only-Add）

---

## §7 治理後果條款

任何違反本文件之行為：
- 立即視為系統失效
- 必須回退至最後合規版本
- 不得以績效辯護

（FULL_ARCH 完）

