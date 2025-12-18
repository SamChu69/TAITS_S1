📘 TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219
PART 1｜文件定位 × 營運的法律地位 × 環境治理原則

# TAITS_部署、營運與日常運作規範（DEPLOY_OPS）
## Deployment, Operations & Daily Runbook Specification

---

## 營運前言（Why Operations Is Governance）

在多數系統中，  
部署與營運被視為「工程或維運問題」。

在 TAITS 中，  
**營運本身即是治理行為**。

一套在文件中正確、  
但在日常運作中被「便宜行事」的系統，  
在制度上等同於失敗。

---

## 第 1 章｜DEPLOY_OPS 的治理位階與適用範圍

### 1.1 文件位階
- 治理等級：**B（營運治理級）**
- 上位文件：
  - `MASTER_ARCH`
  - `MASTER_CANON`
  - `ARCH_FLOW`
  - `RISK_COMPLIANCE`
- 平行約束：
  - `EXECUTION_CONTROL`
  - `UI_SPEC`

📌 **任何營運便利性不得凌駕治理與風控。**

---

### 1.2 適用範圍（Scope）
本文件適用於：

- 本地環境（Local / Research）
- 模擬環境（Paper / Sim）
- 實盤環境（Live）

📌 不同環境可有不同設定，  
📌 但 **治理鐵律不可分環境例外**。

---

### 1.3 營運的法律地位
在 TAITS 中：

> **任何持續運作的系統狀態，  
> 都被視為一種制度選擇，  
> 必須可被審計、可被中止。**

📌 沒有「暫時跑一下」這種合法狀態。

---

## 第 2 章｜部署環境分類與治理要求

### 2.1 環境分類（Mandatory）
TAITS 僅承認以下三種環境：

1. **Local / Research**
2. **Simulation / Paper**
3. **Production / Live**

📌 未標示環境 → 視為違規部署。

---

### 2.2 Local / Research 環境規範
用途：
- 架構驗證
- 策略研究
- UI 測試

限制：
- ❌ 不得連接真實下單 API
- ❌ 不得產生實盤 Execution
- ✅ 允許資料回放與模擬

📌 Local 永遠不具備任何實盤權限。

---

### 2.3 Simulation / Paper 環境規範
用途：
- 流程完整性測試
- Execution 模擬
- UI 人類流程演練

限制：
- ❌ 不得影響真實資金
- ❌ 不得繞過風控或 Gate
- ✅ 必須完整走 Canonical Flow

📌 模擬不等於簡化。

---

### 2.4 Production / Live 環境規範
用途：
- 真實市場參與

強制條件：
- 完整文件版本鎖定
- Governance Gate 啟用
- Risk / Compliance 即時監控
- Kill Switch 可用

📌 **Live 環境的任何異常，  
都必須以「停機」為預設反應。**

---

## 第 3 章｜部署前的強制治理檢查（Pre-Deployment Gate）

### 3.1 為何部署前也需要 Gate
部署本身即代表：
- 系統可能影響真實世界
- 風險從理論進入現實

📌 **部署是第一個「可能造成後果」的行為。**

---

### 3.2 部署前 Gate 的最小條件
任何環境（含 Local）部署前，**必須確認**：

1. 文件版本一致（doc_key + version）
2. Correlation ID 機制正常
3. Risk / Compliance 模組啟用
4. Execution 預設為 Disable（非 Live）
5. Log / Audit 模組可寫入

📌 任一項未通過 → **禁止部署**。

---

### 3.3 部署紀錄（Deployment Log）
每一次部署，必須記錄：

- Deployment ID
- 環境類型
- 文件版本
- 啟用模組清單
- 時間戳與負責人

📌 **無 Deployment Log → 視為未部署。**

---

（DEPLOY_OPS · PART 1 結束）

PART 2｜日常營運模式 × 即時監控告警 × 事件處理機制

## 第 4 章｜日常營運模式（Run Modes）

### 4.1 Run Mode 的治理定位
Run Mode 並非技術設定，而是**制度選擇**。  
每一種 Run Mode，代表系統在當下**被允許做到什麼程度**。

📌 未明確宣告 Run Mode → 系統視為 **不可營運狀態**。

---

### 4.2 合法 Run Mode 類型（唯一白名單）

TAITS 僅承認以下 Run Mode：

1. **Disabled**
2. **Observe-only**
3. **Simulated Execution**
4. **Live Execution**

📌 任何其他自訂模式 → **違規**。

---

### 4.3 Disabled Mode（完全停用）
用途：
- 系統維護
- 重大異常後的安全狀態

特性：
- ❌ 不產生 Execution
- ❌ 不要求人類決策
- ✅ 允許資料蒐集與 Log

📌 Disabled 是**安全狀態，不是失敗狀態**。

---

### 4.4 Observe-only Mode（觀察模式）
用途：
- 市場觀察
- 人類訓練
- 策略假設驗證（不承擔風險）

特性：
- ❌ 不允許 Execution
- ✅ 完整走 Canonical Flow（L1–L10）
- ✅ 產生 Human Decision Log（Defer 為主）

📌 Observe-only 是 **預設推薦的營運模式**。

---

### 4.5 Simulated Execution Mode（模擬執行）
用途：
- 執行流程測試
- Execution 控制驗證

特性：
- ❌ 不影響真實市場
- ✅ 模擬下單 / 成交
- ✅ 觸發 Kill Switch / Failure 流程

📌 模擬必須 **完整模擬錯誤與中止**，不得只跑順境。

---

### 4.6 Live Execution Mode（實盤執行）
用途：
- 真實市場參與

強制條件：
- Governance Gate 啟用
- Risk / Compliance 即時監控
- Kill Switch 隨時可觸發
- 人類裁決流程不可省略

📌 **Live 是例外狀態，不是常態。**

---

## 第 5 章｜即時監控、告警與中止（Monitoring & Alerting）

### 5.1 監控的治理目的
監控不是為了「知道發生什麼」，  
而是為了在**錯誤尚未擴大前中止行為**。

📌 無法即時中止的監控，沒有治理價值。

---

### 5.2 強制監控項目（Mandatory）
所有 Run Mode（除 Disabled）**必須監控**：

- Risk / Compliance 狀態
- Governance Gate 狀態
- Execution 狀態（即使為 Observe-only）
- 系統健康度（API、延遲、錯誤率）
- Log / Audit 寫入狀態

📌 任一監控失效 → **自動降級或停機**。

---

### 5.3 告警分級（Alert Severity）
告警必須分級處理：

- **INFO**：狀態通知
- **WARN**：需關注但不需中止
- **CRITICAL**：立即中止（Kill Switch）

📌 不得將 CRITICAL 降級處理。

---

### 5.4 告警的處置原則
- 告警出現時：
  - 預設採取 **保守行為**
- 無法判斷影響時：
  - 預設 **中止執行**

📌 **不確定性本身就是風險。**

---

## 第 6 章｜營運中異常與事件處理（Incident Response）

### 6.1 事件的定義
事件（Incident）指：
> **任何偏離預期、  
> 可能影響治理、風控或人類主權的狀態。**

---

### 6.2 事件分級
- **Minor**：不影響治理（紀錄即可）
- **Major**：影響流程完整性（需停機）
- **Critical**：可能造成實際損失（立即 Kill）

📌 分級以 **最壞情境** 為準。

---

### 6.3 事件處理三步驟（不可跳過）
1. **Stop**：停止相關行為
2. **Stabilize**：確保系統不再擴散錯誤
3. **Record**：完整記錄事件

📌 **修復永遠在事後進行。**

---

### 6.4 事件記錄（Incident Log）
每一事件必須記錄：

- Incident ID
- 類型與等級
- 發生時間
- 影響範圍
- 採取行動
- Correlation ID

📌 **無 Incident Log → 視為未處理事件。**

---

（DEPLOY_OPS · PART 2 結束）

PART 3｜例行營運節奏 × 變更治理 × 營運最終宣告

## 第 7 章｜日常例行檢查與營運節奏（Operational Runbook）

### 7.1 為何需要 Runbook
在 TAITS 中，  
**「照表操課」不是低階操作，而是治理穩定性的來源**。

Runbook 的存在，是為了防止：
- 人為疏忽
- 長期營運下的習慣性鬆動
- 「今天先這樣跑」的破口

---

### 7.2 每日啟動前檢查（Daily Pre-Run Checklist）
每個營運日開始前，**必須完成以下檢查**：

1. 環境確認（Local / Sim / Live）
2. Run Mode 明確標示
3. Risk / Compliance 模組狀態 = 正常
4. Governance Gate 可用
5. Kill Switch 測試通過
6. Log / Audit 寫入正常

📌 任一未通過 → **當日不得進入 Live**。

---

### 7.3 盤中監控節奏（Intra-Day Operations）
盤中必須：

- 持續監控：
  - Risk 狀態
  - Execution 狀態
  - 告警等級
- 當出現：
  - CRITICAL 告警  
  → 立即中止所有 Execution

📌 **盤中不處理結構性變更，只做中止與紀錄。**

---

### 7.4 盤後檢查（Post-Run Review）
每個營運日結束後，必須完成：

- Execution Summary
- Incident Review（若有）
- 未解決告警清單
- Log 完整性檢查

📌 **盤後檢查不做績效評分，只做事實確認。**

---

## 第 8 章｜變更、升級與治理凍結（Change Management & Freeze）

### 8.1 變更的治理定位
在 TAITS 中：

> **任何變更，都是對風險結構的重新定義。**

因此，變更本身即是高風險行為。

---

### 8.2 變更類型分類
TAITS 僅承認以下變更類型：

1. **文件變更**
2. **設定變更**
3. **模組升級**
4. **治理規則變更**

📌 未分類變更 → **違規**。

---

### 8.3 變更前的強制要求
任何變更前，必須：

- 停止 Live Execution
- 切換至 Disabled 或 Observe-only
- 完成變更說明與影響評估
- 記錄 Change Request

📌 **不允許「熱更新」Live 系統。**

---

### 8.4 治理凍結（Governance Freeze）
在以下情境，必須啟動治理凍結：

- 實盤階段（S1）
- 發生重大 Incident 後
- 監管或制度風險提高時

凍結期間：
- ❌ 不允許結構性變更
- ❌ 不允許策略擴張
- ✅ 僅允許修復型變更（需審計）

---

### 8.5 解除凍結的條件
解除治理凍結前，必須：

- 完成事件回顧
- 通過風控與治理審查
- 更新文件版本
- 重新部署並驗證

📌 **凍結不是結束，而是重新確認。**

---

## DEPLOY_OPS 最終宣告（Closing）

在 TAITS 中，  
**部署與營運不是背景工作，  
而是系統能否長期存活的前線防線**。

如果一套系統：
- 在文件中嚴謹
- 在營運中隨便
- 在異常時猶豫

那它終將在壓力下崩潰。

> **真正成熟的系統，  
> 不是靠天才操作活下來，  
> 而是靠制度讓普通日子不出錯。**

---

（DEPLOY_OPS · PART 3 完成）
