# TAITS_Document_Index.md
（TAITS 專案導覽索引｜強制閱讀順序｜交叉引用｜新對話 100% 重建）

> 文件定位：GitHub 導覽中樞（Navigation Hub）
> 目的：任何人不需要通靈，只要照順序讀，就能完整理解 TAITS。

---

## 0. 強制規則（不照做一定走歪）

1) 禁止只看策略檔就想做決策  
2) 禁止未理解 Regime 就調策略  
3) 禁止繞過 Governance / Risk Gate  
4) 禁止把觀察型產品（期貨/選擇權/融資融券）當成下單標的  
5) 對話內容不算系統文件；能被引用的只有 repo 內檔案

---

## 1. 你現在 repo 的 12 份檔案（現況）

- TAITS_MASTER_ARCHITECTURE.md（憲章）
- TAITS_Full_System_Architecture.md（總架構藍圖）
- TAITS_Architecture_and_Flow.md（流程與事件）
- TAITS_DataSources_Universe.md（資料來源全集）
- TAITS_Strategy_Universe_Complete.md（策略宇宙）
- TAITS_Risk_and_Compliance.md（風控合規）
- TAITS_UI_Spec.md（UI 規格｜建議屬實作層）
- TAITS_Local_Execution_Environment.md（本地環境｜建議屬部署/運維）
- TAITS_Beginner_Teaching_Rules.md（新手教學規範）
- TAITS_GitHub_Save_Rules.md（GitHub 存檔規範）
- TAITS完整總架構 × 總流程 × 全資訊體系（MASTER VERSION）.md（歷史整合檔｜建議保留但避免成為第二權威）
- TAITS_Document_Index.md（本檔）

> 重要：為避免「雙重真實來源」，歷史整合檔請視為參考；權威以本 Index 指定的順序與檔案責任為準。

---

## 2. 官方閱讀順序（唯一合法）

### Phase A｜先理解 TAITS 的憲章與邊界
1) TAITS_MASTER_ARCHITECTURE.md  
2) TAITS_Full_System_Architecture.md  

### Phase B｜理解資料與市場語言
3) TAITS_DataSources_Universe.md  
4) （指標/特徵全集將被整理進 Strategy/Flow 中引用，後續會補齊獨立檔或附錄）

### Phase C｜理解系統怎麼跑
5) TAITS_Architecture_and_Flow.md  

### Phase D｜理解策略如何被使用（不是下單）
6) TAITS_Strategy_Universe_Complete.md  

### Phase E｜理解治理與否決（生存）
7) TAITS_Risk_and_Compliance.md  

### Phase F｜輔助性文件（不屬母體）
8) TAITS_GitHub_Save_Rules.md  
9) TAITS_Beginner_Teaching_Rules.md  
10) TAITS_UI_Spec.md  
11) TAITS_Local_Execution_Environment.md  
12) TAITS完整總架構 × 總流程 × 全資訊體系（MASTER VERSION）.md（參考）

---

## 3. 各檔案責任摘要（避免重複與混淆）

- MASTER_ARCHITECTURE：不可違反原則與優先序
- FULL_SYSTEM_ARCHITECTURE：十層分層與模組邊界
- ARCHITECTURE_AND_FLOW：流程/事件/可回放規格
- DATASOURCES_UNIVERSE：資料來源、可靠度、備援策略
- STRATEGY_UNIVERSE：策略宇宙（訊號集合，不下單）
- RISK_AND_COMPLIANCE：否決與極端情境（最高權力）

---

## 4. 新對話如何快速接手（3 分鐘）

新對話只要做三件事：
1) 先讀：MASTER_ARCHITECTURE（知道不能做什麼）
2) 再讀：FULL_SYSTEM_ARCHITECTURE（知道系統怎麼拆）
3) 最後讀：ARCHITECTURE_AND_FLOW（知道系統怎麼跑）

讀完以上三份，就能避免 90% 以上的誤解。

---

## 5. 版本與變更（簡版規則）

- 任何重要變更請在 repo 根目錄建立 CHANGELOG
- 不覆寫歷史語義，只能新增或附錄
- 風控與憲章文件變更需最高審慎

---

## 6. Index 完成宣告

本索引是 TAITS 專案在 GitHub 的導覽中樞。  
任何新增文件必須更新本索引，否則視為未納入系統。
