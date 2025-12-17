# TAITS_一致性與審查清單（CHECKLIST）__251218.md

> doc_key：CHECKLIST  
> 治理等級：A+（流程鎖定與一致性審查｜不可跳步）  
> 適用範圍：TAITS 全系統（文件 / 架構 / 策略 / 風控 / 執行 / AI 行為）  
> 狀態：ACTIVE（Only-Add｜只能新增不可縮水）  
> 最後更新：2025-12-18（Asia/Taipei）

---

## 0. 文件定位（Why This Exists）

本文件是 **TAITS 的「流程鎖」**。  
用途不是說明架構，而是**規定「現在要檢查到哪一步、能不能往下走」**。

📌 若未完成本清單對應步驟：
- **不得進入下一階段**
- **不得啟動新對話的實質討論**
- **不得進行任何程式或策略開發**

---

## 1. 使用規則（Hard Rules）

- 本清單 **必須照順序執行**
- **不得跳步**
- 任一步驟若為「未通過」：
  - 立即停止
  - 回到該步驟補齊
- 本清單 **約束 AI，不約束人類最終決策權**

---

## 2. Phase 0｜Repo 與 Canon 基礎確認（不可跳）

### Step 0.1｜Repo 結構確認
- [ ] 僅存在一份 `README.md`
- [ ] 舊檔案已移入 `__LEGACY_ARCHIVE__` 或刪除
- [ ] `.cursorignore` 已存在並生效

**未通過 → 禁止繼續**

---

### Step 0.2｜DOCUMENT_INDEX 權威確認
- [ ] 已讀取 `DOCUMENT_INDEX`
- [ ] 確認 Canon 文件清單與實際 Repo 一致
- [ ] 無未列入索引的活躍文件

**未通過 → 禁止繼續**

---

## 3. Phase 1｜架構與流程一致性檢查

### Step 1.1｜架構文件一致性
- [ ] MASTER_ARCH 已存在
- [ ] ARCH_FLOW 已存在
- [ ] MASTER_VERSION 已存在
- [ ] 三者無邏輯衝突

---

### Step 1.2｜流程不可跳步檢查
- [ ] Data → Feature → Regime → Strategy → Risk → Execution
- [ ] 任一 Gate 均可否決
- [ ] 無策略直連 Execution 行為

---

## 4. Phase 2｜資料與策略治理檢查

### Step 2.1｜資料來源治理
- [ ] DATASOURCE_UNIVERSE 已存在
- [ ] 官方來源優先
- [ ] 易變動規則未寫死

---

### Step 2.2｜策略宇宙確認
- [ ] STRATEGY_UNIVERSE 已存在
- [ ] 零股 / 整股 / 混合標註清楚
- [ ] 策略不包含下單邏輯

---

### Step 2.3｜特徵治理確認
- [ ] FEATURE_INDEX 已存在
- [ ] 特徵有用途與限制
- [ ] 特徵不可直接觸發交易

---

## 5. Phase 3｜風控與制度最高優先檢查

### Step 3.1｜風控否決權
- [ ] RISK_COMPLIANCE 已存在
- [ ] 明確宣告最高否決權
- [ ] Kill Switch 定義完整

---

### Step 3.2｜官方制度引用
- [ ] OFFICIAL_REF 已存在
- [ ] 官方規則未被寫死
- [ ] 易變動資訊僅引用入口

---

## 6. Phase 4｜執行、環境與營運檢查

### Step 4.1｜Execution 邊界
- [ ] EXEC_CONTROL 已存在
- [ ] 僅授權後可執行
- [ ] 僅使用富邦 TradeAPI

---

### Step 4.2｜本地環境治理
- [ ] LOCAL_ENV 已存在
- [ ] 環境分級清楚
- [ ] 使用者實際設備已備註

---

### Step 4.3｜部署與營運
- [ ] DEPLOY_OPS 已存在
- [ ] 未進入 Live 狀態
- [ ] 監控與回放機制存在

---

## 7. Phase 5｜UI 與人類控制確認

### Step 5.1｜UI 治理
- [ ] UI_SPEC 已存在
- [ ] UI 不直接下單
- [ ] 人類可否決一切

---

## 8. Phase 6｜AI 行為鎖定（新對話必做）

### Step 6.1｜AI 規則確認
- [ ] AI_RULES 已存在
- [ ] AI 嚴禁偷工減料
- [ ] AI 不可越權、不腦補

---

### Step 6.2｜新對話啟動宣告
- [ ] AI 宣告已讀 DOCUMENT_INDEX
- [ ] AI 宣告依 Canon 行事

**未完成 → 新對話不得進入實質討論**

---

## 9. Phase 7｜封版前最終確認

- [ ] 本 CHECKLIST 全部通過
- [ ] 無 Pending 項目
- [ ] 使用者確認「可以進入開發」

📌 **未經使用者確認，不得進入程式或策略實作。**

---

## 10. 最終宣告

> **如果沒有照這份清單一步一步來，  
> 那不是 TAITS。**

---

（End of CHECKLIST）
