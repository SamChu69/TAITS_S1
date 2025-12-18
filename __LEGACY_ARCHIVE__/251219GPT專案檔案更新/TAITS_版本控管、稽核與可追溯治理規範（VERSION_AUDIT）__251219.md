治理等級： B（架構／制度級）
裁決依據： DOCUMENT_INDEX（A+）__251219

# TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）
## Versioning, Audit & Traceability Governance (Governance-Aligned)

版本日期：2025-12-19  
適用狀態：S0 / S1（Freeze 前後）  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217

---

## 前言｜Why Versioning Is Governance

在 TAITS 中，「版本」不是工程細節，而是**治理有效性的存在條件**。  
任何無法被回放、被審計、被追責的變更，**在制度上視為不存在**。

---

## 第 1 章｜文件位階、適用範圍與法律地位

### 1.1 文件位階
- 治理等級：**B（治理／制度級）**
- 上位文件：
  - `TAITS_AI_行為與決策治理最終規則全集__251217`（A+）
  - `TAITS_MASTER_ARCHITECTURE`（A）
  - `DOCUMENT_INDEX（A+）`
- 平行約束：
  - `ARCH_FLOW`
  - `RISK_COMPLIANCE`
  - `DEPLOY_OPS`

### 1.2 適用範圍
本文件規範以下對象之**版本控管、稽核、回放與追溯**：
- 文件（A+ / A / B / C）
- 策略中介工件（Evidence / Feature 定義）
- 設定檔（非敏感）
- 部署版本（Build / Release）
- 事件（Incident / Freeze / Kill）

📌 **任何未納入本規範的變更，視為未授權。**

---

## 第 2 章｜Hard Gates（硬性門檻）

### 2.1 Only-Add 原則（AI_GOV §7, §11）
- 允許：新增（Append）
- 禁止：覆寫、刪改、回填歷史

📌 **修正錯誤 ≠ 覆寫歷史；必須以新版本補正。**

### 2.2 可回放（Replayable）原則（AI_GOV §11）
- 任一變更，必須可在指定時間點被完整回放：
  - 生效版本
  - 依據文件
  - 影響範圍
  - 當時決策軌跡

### 2.3 Freeze 約束（AI_GOV §15）
- 進入 S1 Freeze 後：
  - A+ / A：**完全禁止**
  - B：**僅允許紀錄性補充**
  - C：**僅允許說明性修訂**

---

## 第 3 章｜版本命名、狀態與生命週期

### 3.1 版本命名規範
- 格式：`__YYYYMMDD`
- 禁止：
  - `latest`
  - `final`
  - 無日期版本

### 3.2 版本狀態（Status）
- `DRAFT`：未生效
- `ACTIVE`：唯一生效版本（僅 1）
- `FROZEN`：Freeze 鎖定
- `DEPRECATED`：停止使用（可回放）
- `MERGED`：職責已合併（無正文）

📌 **同一 doc_key 僅能存在一個 ACTIVE。**

---

## 第 4 章｜變更類型與允許矩陣

| 變更類型 | 允許 | 說明 |
|---|---|---|
| 新增章節 | ✅ | Only-Add |
| 條文補正 | ⚠️ | 需標記 Correction |
| 條文刪除 | ❌ | 永久禁止 |
| 歷史回填 | ❌ | 永久禁止 |
| Freeze 後結構變更 | ❌ | 永久禁止 |

---

## 第 5 章｜Change Ledger（變更帳冊）【必填】

### 5.1 Ledger 最小欄位
- `change_id`（唯一）
- `doc_key`
- `from_version`
- `to_version`
- `change_type`
- `reason_code`
- `requested_by`
- `approved_by`
- `effective_time`
- `freeze_state`
- `audit_ref`

### 5.2 Reason Codes（範例）
- `ERR_CORRECTION`
- `SCOPE_CLARIFICATION`
- `COMPLIANCE_UPDATE`
- `INCIDENT_RESPONSE`

📌 **缺任一欄位 → 變更無效。**

---

## 第 6 章｜審計（Audit）與回放（Replay）

### 6.1 必備審計能力
- 查詢任一時間點：
  - 生效文件版本
  - ACTIVE 狀態
  - Freeze 狀態
- 回放：
  - Decision Trace
  - Evidence 來源
  - Veto / Override 記錄

### 6.2 Replay Spec（最小）
- `timestamp`
- `actor`（Human / AI / System）
- `doc_refs[]`
- `inputs`
- `outputs`
- `veto_flags`

---

## 第 7 章｜違規與處置（Enforcement）

### 7.1 違規定義
- 覆寫既有版本
- 未記錄變更即部署
- Freeze 期間修改 B 級結構
- 無法回放之版本

### 7.2 處置等級
- **Minor**：補記 Ledger
- **Major**：流程中止
- **Critical**：Freeze / Kill

📌 **績效、緊急性不得作為抗辯理由。**

---

## 第 8 章｜AI 與人類邊界

### 8.1 AI
- 可讀取：版本、Ledger、審計結果
- 不得：
  - 合理化缺失紀錄
  - 推論「應該存在的版本」

### 8.2 Human
- 有決策權
- **無版本解釋權**
- 任何操作必須留痕

---

## 附錄 A｜Version Checklist（上線前）

- [ ] ACTIVE 唯一
- [ ] Ledger 完整
- [ ] Replay 可用
- [ ] Freeze 狀態一致
- [ ] DOCUMENT_INDEX 對齊

---

## 結語｜Closing

在 TAITS 中，  
**沒有被版本化的東西，等於沒有被允許。**  
版本不是歷史負擔，而是**責任的錨點**。

（VERSION_AUDIT 完）

治理等級： B（架構／制度級）
裁決依據： DOCUMENT_INDEX（A+）__251219
對齊母法： TAITS_AI_行為與決策治理最終規則全集__251217

# TAITS_全系統架構總覽（FULL_ARCH）
## Full System Architecture Overview (Governance-Aligned)

版本日期：2025-12-19  
適用狀態：S0 / S1（Freeze 前後）  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217

---

## 前言｜Why FULL_ARCH Exists

FULL_ARCH 的任務不是描述流程細節，  
而是**界定模組邊界、通訊限制與治理責任歸屬**。

> **流程屬於 ARCH_FLOW；  
> 邊界與權限，屬於 FULL_ARCH。**

---

## 第 1 章｜文件位階、適用範圍與不可動搖原則

### 1.1 文件位階
- 治理等級：**B（架構／制度級）**
- 上位文件：
  - `TAITS_AI_行為與決策治理最終規則全集__251217`（A+）
  - `TAITS_MASTER_ARCHITECTURE`（A）
  - `MASTER_CANON`（A）
- 平行約束：
  - `ARCH_FLOW`
  - `RISK_COMPLIANCE`
  - `EXECUTION_CONTROL`
  - `UI_SPEC`
  - `DEPLOY_OPS`

### 1.2 適用範圍
本文件定義：
- 系統模組劃分
- 模組責任與權限
- 模組間通訊邊界
- 禁止事項（Hard No）

📌 **本文件不定義策略、不定義決策、不定義下單。**

---

## 第 2 章｜Hard Gates（硬性門檻）

### 2.1 模組邊界不可混用（AI_GOV §4, §6, §14）
- 每一模組僅能執行其被授權的職責
- 禁止跨模組回寫狀態

### 2.2 AI 不得升格為模組（AI_GOV §14）
- AI 僅能作為：
  - 分析者
  - 描述者
  - 輔助者
- **不得**：
  - 成為裁決模組
  - 成為執行模組
  - 擁有狀態主權

### 2.3 單一真實來源（Single Source of Truth）
- 任一治理事實：
  - 僅能存在於一個模組
- 其他模組僅能讀取，不得複製

---

## 第 3 章｜TAITS 模組總覽（Module Map）

### 3.1 模組分類總表

| 類別 | 模組 |
|---|---|
| 資料層 | Data Ingest / Data Validation |
| 分析層 | Feature Engine / Evidence Builder |
| 狀態層 | Regime Engine |
| 風控層 | Risk & Compliance |
| 策略層 | Strategy Selector |
| 決策層 | Human Decision Interface |
| 執行層 | Execution Engine |
| 治理層 | Audit / Version / Freeze |
| 展示層 | UI / Reporting |

📌 **分類僅用於治理，非技術實作限制。**

---

## 第 4 章｜核心模組責任與禁止事項

### 4.1 Data Ingest Module
- 職責：
  - 收集官方／授權資料
- 禁止：
  - 推論缺失資料
  - 自行補值裁決

### 4.2 Feature Engine
- 職責：
  - 計算 Feature（描述性）
- 禁止：
  - 形成方向性結論
  - 產生 Signal

### 4.3 Evidence Builder
- 職責：
  - 組合 Feature 為 Evidence
- 禁止：
  - 跳過 Evidence 直接給策略

### 4.4 Regime Engine
- 職責：
  - 市場狀態裁定
- 禁止：
  - 直接影響下單

### 4.5 Risk & Compliance
- 職責：
  - 否決一切不合規行為
- 禁止：
  - 以績效為理由放行

### 4.6 Strategy Selector
- 職責：
  - 策略可用性判斷
- 禁止：
  - 產生交易指令

### 4.7 Human Decision Interface
- 職責：
  - 人類最終裁決
- 禁止：
  - 隱性自動化

### 4.8 Execution Engine
- 職責：
  - 嚴格依裁決執行
- 禁止：
  - 自行判斷方向

---

## 第 5 章｜模組通訊與資料流限制

### 5.1 允許的通訊方向（摘要）
- Data → Feature → Evidence → Regime → Strategy → Human → Execution

### 5.2 永久禁止的通訊
- Execution → Strategy
- Strategy → Regime
- Feature → Execution
- AI → Execution

📌 **任何逆向通訊 = 治理違規。**

---

## 第 6 章｜Module × Layer 映射（審計輸出）

| 模組 | 對應 Layer |
|---|---|
| Data Ingest | L1–L3 |
| Feature Engine | L4 |
| Evidence Builder | L5 |
| Regime Engine | L6 |
| Risk & Compliance | L7 |
| Strategy Selector | L8 |
| Decision Interface | L10 |
| Execution Engine | L11 |

---

## 第 7 章｜審計輸出（Audit Artifacts）

### 7.1 必須產出
- 模組呼叫紀錄
- 輸入／輸出摘要
- 否決／放行標記
- 版本與 Freeze 狀態

### 7.2 稽核重點
- 是否跨模組越權
- 是否跳層
- 是否 AI 升格

---

## 結語｜Closing

TAITS 的強度，不來自模組數量，  
而來自**模組不做不該做的事**。

> **當每個模組都被邊界約束，  
> 系統才可能長期存活。**

（FULL_ARCH 完）

