# TAITS_系統架構與流程細化說明（ARCH_FLOW）
## Taiwan Alpha Intelligence Trading System
### ARCHITECTURE & FLOW DEEP DIVE
### 版本日期：2025-12-19
### 治理等級：B（Canonical · 流程細化）
### 狀態：ACTIVE（同版融合更新）
### 覆寫權限：僅人類主權

---

## 0. 文件定位（Flow-as-Law）

本文件為 **TAITS Canonical Flow 的逐層細化說明**。

其職責是將《TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）》中的
**11 層不可跳步流程**，拆解為：

- 每一層的 **輸入（Inputs）**
- 每一層的 **處理（Processing）**
- 每一層的 **輸出（Outputs）**
- 每一層的 **禁止事項（Hard Prohibitions）**

📌 本文件 **不定義策略、不定義實作細節**，  
📌 僅定義 **「在治理上什麼是合法流程」**。

---

## 1. L1｜Data Ingestion（資料蒐集層）

### 1.1 合法輸入
- 官方行情資料（TWSE / TPEx）
- 官方公告與法規（MOPS / TWSE）
- Observe-only 資料（期貨、選擇權、情緒）

### 1.2 處理行為
- 取得
- 原始封存
- 標註來源、時間、版本

### 1.3 輸出
- 原始資料集（Raw Data Snapshot）

### 1.4 禁止事項
- 資料補值
- 資料推測
- 選擇性忽略不利資料

---

## 2. L2｜Data Normalization（資料正規化）

### 2.1 合法輸入
- L1 原始資料

### 2.2 處理行為
- 欄位對齊
- 時間對齊
- 格式統一
- 異常值標記（非修正）

### 2.3 輸出
- 正規化資料集（Normalized Dataset）

### 2.4 禁止事項
- 改寫原始數值
- 內插不存在資料
- 隱藏缺失欄位

---

## 3. L3｜Market Snapshot（市場快照）

### 3.1 合法輸入
- 正規化資料集

### 3.2 處理行為
- 建立「某一時刻」的市場狀態
- 固化為可回放快照

### 3.3 輸出
- Market Snapshot（含時間戳）

### 3.4 強制要求
- 必須可回放
- 必須可審計

### 3.5 禁止事項
- 即時計算但不封存
- 僅存在於記憶體

---

## 4. L4｜Feature & Methodology（特徵與方法）

### 4.1 合法輸入
- Market Snapshot

### 4.2 處理行為
- 計算特徵（MA、ATR、RSI 等）
- 標註適用 / 禁用 Regime
- 標註資料來源

### 4.3 輸出
- Feature Set（特徵集合）

### 4.4 禁止事項
- 產生買賣方向
- 產生進出場點位
- 隱性策略邏輯

---

## 5. L5｜Evidence Bundle（證據包）

### 5.1 合法輸入
- Feature Set
- 結構性資料
- Observe-only 輔助資料

### 5.2 處理行為
- 多證據整合
- 衝突標註
- 完整度評估

### 5.3 輸出
- Evidence Bundle（含完整度指標）

### 5.4 核心鐵律
- 單一證據 **永遠不可構成決策依據**

---

## 6. L6｜Market Regime（市場狀態）

### 6.1 合法輸入
- Evidence Bundle
- 波動與結構特徵

### 6.2 處理行為
- 判定市場所屬狀態
- 標註 Regime 信心度

### 6.3 輸出
- Regime Label

### 6.4 禁止事項
- Regime 作為預測工具
- Regime 直接產生交易方向

---

## 7. L7｜Risk & Compliance（最高否決）

### 7.1 合法輸入
- Regime Label
- Evidence Bundle
- 法規與限制條件

### 7.2 處理行為
- 風險評估
- 合規檢查
- Worst-case 分析

### 7.3 輸出
- Pass / Reject
- Reject Reason（強制）

### 7.4 核心權限
- 跨層級即時否決
- 不接受績效辯護

---

## 8. L8｜Strategy & Universe（策略假設層）

### 8.1 合法輸入
- Regime 通過
- Risk Pass

### 8.2 處理行為
- 產生策略假設
- 標註適用條件

### 8.3 輸出
- Strategy Hypotheses（非指令）

### 8.4 禁止事項
- 策略直連下單
- 隱性轉為交易訊號

---

## 9. L9｜Governance Gate（治理門）

### 9.1 合法輸入
- 策略假設
- 全流程紀錄

### 9.2 處理行為
- 流程完整性檢查
- 文件一致性檢查

### 9.3 輸出
- Allow / Block

### 9.4 禁止事項
- 人工或程式繞過
- 默認放行

---

## 10. L10｜UI & Human Decision（人類決策）

### 10.1 合法輸入
- 全 Evidence
- Risk / Reject 說明
- Strategy Hypotheses

### 10.2 處理行為
- 視覺化呈現
- 人類決策

### 10.3 輸出
- 明確人類指令（或不行動）

### 10.4 鐵律
- 最終決策僅存在於此層

---

## 11. L11｜Execution & Control（受控執行）

### 11.1 合法輸入
- 人類明確指令
- 合規確認

### 11.2 處理行為
- 下單執行
- 即時監控
- Kill Switch

### 11.3 輸出
- Execution Log
- 可回放紀錄

### 11.4 禁止事項
- 自動補單
- 無人值守執行

---

## 12. 跨層通用禁止事項（Global Hard No）

- 跳層輸出
- 隱性策略
- AI 自主下單
- 省略風控或 Regime

---

## 13. ARCH_FLOW 最終宣告

> **TAITS 的流程不是為了加速交易，  
而是為了確保：  
每一步都能被問責。**

---

（End of ARCH_FLOW）
