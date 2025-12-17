# TAITS_AI_自動審查Checklist__251217.md

> doc_key：AI_AUTO_AUDIT_CHECKLIST  
> 治理等級：A（強制 Gate｜不可略過）  
> 適用對象：所有 AI / Agent / 自動化輸出  
> 適用範圍：TAITS 全系統  
> 狀態：ACTIVE（Final｜Only-Add）

---

## 0. 文件定位（Mandatory Gate）

本文件定義 **AI 在 TAITS 專案中，每一次輸出之前，必須完成的自動審查清單**。

📌 未通過本 Checklist：
- 不得輸出
- 不得合併
- 不得進入 Canon

---

## 1. 啟動條件（When to Run）

以下任一情況，**必須執行本 Checklist**：

- 產出任何 `.md` 文件
- 補充或修改架構 / 流程 / 策略
- 設計 Execution / Risk / Strategy 行為
- 新對話第一次回覆 TAITS 相關內容
- 嘗試擴充交易產品或交易單位

---

## 2. P0 Gate｜Scope 與範圍檢查（最高優先）

### 2.1 市場與產品
- [ ] 僅限台股（TWSE / TPEX）
- [ ] 僅限股票（STOCK）
- [ ] 未引入期貨 / 選擇權 / 美股 / 權證 / 融資融券

### 2.2 交易單位（Trade Unit）
- [ ] 零股（odd_lot）為唯一啟用
- [ ] 整股（full_lot）/ 混合（hybrid）僅標示為預留
- [ ] 無任何自動升級描述

❌ 任一不符合 → **NO-GO**

---

## 3. P0 Gate｜三權分立檢查

### 3.1 Strategy
- [ ] 僅生成交易意圖（Intent）
- [ ] 不含否決（Veto）邏輯
- [ ] 不指定下單方式 / 價格 / API

### 3.2 Risk / Compliance
- [ ] 僅允許 / 否決 / 降級 / 暫停
- [ ] 不生成交易訊號
- [ ] 不自動解除否決

### 3.3 Execution
- [ ] 服從 Risk 裁決
- [ ] 不修改策略方向
- [ ] 不假設一定成交

❌ 任一越權 → **NO-GO**

---

## 4. P0 Gate｜治理與權威對齊

- [ ] 遵守最新 TAITS Canon
- [ ] 未推翻已確認規範
- [ ] 符合 Only-Add 原則
- [ ] 未因方便弱化治理或風控

---

## 5. P0 Gate｜官方來源引用

- [ ] 僅引用官方來源
- [ ] 不寫死易變動細節
- [ ] 採用語義描述 + 官方連結

---

## 6. P0 Gate｜文件完整性（關鍵）

### 6.1 完整可存檔
- [ ] 完整 Markdown 檔案
- [ ] 非片段 / 非摘要 / 非 diff
- [ ] 若拆分，每份仍可獨立存檔

### 6.2 路徑與命名
- [ ] 提供完整路徑
- [ ] 檔名包含主題 + 範圍 + 日期（`__YYMMDD`）
- [ ] 更新內容不覆蓋舊檔

---

## 7. P0 Gate｜策略治理（如涉及）

- [ ] 使用 Strategy Meta
- [ ] 標註適用產品與交易單位
- [ ] 符合策略生命週期
- [ ] 非 ENABLED 策略不進 Execution

---

## 8. P0 Gate｜Execution / Risk Gate（如涉及）

- [ ] Scope Freeze Gate
- [ ] Trade Unit Compatibility Gate
- [ ] Enable Gate（full_lot / hybrid）
- [ ] Risk Veto Hook（前 / 中）
- [ ] Unified Exit 概念
- [ ] Failure Handling 與完整紀錄

---

## 9. P0 Gate｜Log / 審計

- [ ] Decision Log
- [ ] Risk Decision Log
- [ ] Execution Log
- [ ] correlation_id 串接因果鏈

---

## 10. P0 Gate｜人類最終控制權

- [ ] 人類保有最終裁決權
- [ ] AI 非最終決策者
- [ ] 衝突時提醒但尊重人類裁決

---

## 11. 最終審查結果（必填）

- 審查結果：
  - [ ] PASS
  - [ ] FAIL

- 未通過項目（若 FAIL）：
  - …

- 再審日期：
  - __YYMMDD__

---

## 12. 最終聲明

> **未通過審查的輸出，  
在 TAITS 中視為不存在。**

---

（End of AI_AUTO_AUDIT_CHECKLIST）
