# TAITS_MASTER_ARCHITECTURE｜母體總憲法與核心鐵律（MASTER_ARCH）
版本：2025-12-19  
doc_key：MASTER_ARCH  
治理等級：A+（Supreme Constitution｜最高不可覆寫）  
版本狀態：ACTIVE · LOCKABLE  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217  
變更原則：**Only-Add（僅可新增，不可刪減、不可弱化、不可覆寫）**

---

## 0. 文件地位聲明（不可省略）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）之最高母體憲法**，  
其法律位階高於所有模組、策略、流程、Agent、UI、執行層與 AI 行為。

**任何文件、程式、AI 回覆、Agent 推論，只要與本文件衝突：**
> **一律以本文件為準，且視衝突方為「治理違規」。**

---

## 1. 不可動搖的核心排序（Supreme Priority Order）

TAITS 全系統之最終排序如下（不可更動）：

Human Sovereignty
→ Risk & Compliance (Supreme Veto)
→ Regime
→ Evidence
→ Strategy
→ Execution
→ Performance / Optimization

yaml
複製程式碼

### 1.1 強制解釋
- **人類主權**：AI 永不具最終決策權  
- **風險與合規**：可否決任何高績效策略  
- **Regime**：高於任何單一訊號或模型  
- **策略**：永遠只是「建議與假設」  
- **績效**：不能為任何違規辯護  

---

## 2. 人類主權（Human Sovereignty）鐵律

### 2.1 定義
TAITS 為 **Human-in-the-Loop 強制系統**。

### 2.2 禁止事項
- AI 不得：
  - 自動下單
  - 自動解除風控
  - 自動修改治理規則
- 不存在「完全無人值守交易」

### 2.3 違規判定
若任何模組、Agent、Prompt、文件出現：
- 「AI 自主決策」
- 「自動交易」
- 「系統自行判斷即可」

👉 **直接判定為 A 級治理違規**

---

## 3. Risk / Compliance 最高否決權（Supreme Veto）

### 3.1 否決權定義
Risk / Compliance 擁有跨層、跨模組、跨策略的**最高即時否決權**。

### 3.2 否決不需理由充分性
- 不需解釋績效
- 不需證明錯誤
- 只需符合風險或合規疑慮

### 3.3 禁止事項
- 不得以「長期績效」對抗否決
- 不得以「回測成功」解除否決

---

## 4. Regime 高於一切單一訊號

### 4.1 定義
Regime = 市場狀態母判斷（非策略、非指標）

### 4.2 強制規則
- Regime 不符 → 策略 **不得啟用**
- Regime 衝突 → 系統必須：
  - 降級策略
  - 或完全 BLOCK

### 4.3 禁止事項
- 不得「忽略 Regime」
- 不得「用策略反推 Regime」

---

## 5. Evidence 第一原則（Evidence-First）

### 5.1 定義
所有判斷必須來自 **可回放、可審計、可追溯** 的 Evidence。

### 5.2 Evidence 最低標準
- 來源明確
- 時點可重建
- 不可僅存在於記憶體

### 5.3 禁止事項
- 傳聞
- 主觀感覺
- 無法重現的經驗敘事

---

## 6. Strategy ≠ Execution（策略與下單嚴格分離）

### 6.1 Strategy 定位
Strategy 只允許輸出：
- proposal
- context
- risk_adjust
- avoid / observe

### 6.2 禁止事項
- 直接輸出：
  - 價格
  - 數量
  - 買賣方向
- 不得直連任何下單模組

---

## 7. Structure ≠ Strategy（結構不可升格）

### 7.1 結構系統定位
- 纏論 / 結構 / 型態  
  → **僅為結構描述語法**

### 7.2 結構允許輸出
- structure_state
- completeness_score
- conflict_flag
- warning

### 7.3 明確禁止
- 結構 = 買點
- 背離 = 反轉
- 中樞 = 突破

---

## 8. Annotation 永遠為 Non-Binding

### 8.1 定義
Annotation 僅供人類理解與語意對齊。

### 8.2 禁止事項
- Annotation 升格為條件
- Annotation 被程式解析
- Annotation 被用於回測或實盤

---

## 9. Only-Add 演進鐵律（不可逆）

### 9.1 定義
TAITS 只允許「擴充」，不允許「刪減或弱化」。

### 9.2 不可逆條款
- 治理條款不可刪
- 否決權不可弱化
- 人類主權不可調降

---

## 10. AI 行為邊界（AI Behavior Boundary）

### 10.1 AI 允許行為
- 整理
- 分析
- 建議
- 風險提示

### 10.2 AI 禁止行為
- 自行定義新策略類型
- 自行修改治理文件
- 自行假設可執行性

---

## 11. 違規等級與處置（Enforcement）

### 11.1 違規等級
- **A 級**：觸碰人類主權、風控否決、治理鐵律
- **B 級**：越權推論、策略下單化
- **C 級**：文件簡化、語意誤導

### 11.2 處置原則
- A 級：立即停止、回滾、封鎖
- B 級：降級、重審
- C 級：文件修正

---

## 12. 與其他文件之關係（Hierarchy）

本文件為所有下列文件之上位約束：

- MASTER_CANON
- ARCH_FLOW
- RISK_COMPLIANCE
- EXECUTION_CONTROL
- STRATEGY_UNIVERSE
- STRATEGY_FEATURE_INDEX
- UI_SPEC
- DOCUMENT_INDEX

---

## 13. 最終鎖定聲明（Final Lock）

> **本文件一經標示為 ACTIVE + LOCKABLE，  
> 即視為 TAITS 永久治理母憲法。**

任何未來 AI、Agent、新對話：
- 不得重新解釋
- 不得簡化
- 不得繞過

---

（TAITS_MASTER_ARCHITECTURE｜母體總憲法與核心鐵律｜最大完備版 完）
