# TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）
## Taiwan Alpha Intelligence Trading System

---

## Canonical 前言（Why This Canon Exists）

本文件為 **TAITS 的 Canonical Master 文件**。

若《MASTER_ARCH》回答的是：
> **「什麼永遠不能被違反？」**

那麼《MASTER_CANON》回答的是：
> **「TAITS 是如何被正確地運作？」**

本文件的存在目的不是加速交易，  
而是確保 **任何一筆交易的生成，都經過可回放、可審計、可否決的完整過程**。

---

## 第 1 章｜MASTER_CANON 的法律地位與使用規則

### 1.1 文件位階
- 治理等級：**A（Canonical）**
- 位階關係：
  - 受制於：`MASTER_ARCH`
  - 上位於：`ARCH_FLOW`、`FULL_ARCH`、`RISK_COMPLIANCE`、`EXECUTION_CONTROL`

📌 下位文件**不得修改 Canonical 定義**，僅能展開實作細節。

---

### 1.2 Canonical 的含義（不可誤解）
在 TAITS 中，「Canonical」意指：

- **唯一正確的運作方式**
- **不可被策略、績效、便利性取代**
- **違反即視為系統錯誤**

Canonical ≠ 建議  
Canonical = **法定流程**

---

## 第 2 章｜TAITS 的核心世界觀（Worldview）

### 2.1 Evidence First，而非 Signal First
TAITS 不相信：
- 單一指標
- 單一模型
- 單一勝率

TAITS 只承認：
> **Evidence Bundle（證據包）**

所有行為，必須先問：
- 證據是否完整？
- 證據是否可回放？
- 證據是否彼此衝突？

---

### 2.2 Regime 是「適用性判定」，不是預測
- Regime 的角色：
  - 判定「哪些策略**不能用**」
- Regime **不負責**：
  - 預測漲跌
  - 給出方向

📌 Regime 是剎車，不是油門。

---

### 2.3 Risk / Compliance 是最終裁決者
在 TAITS 中：
- 報酬潛力 **永遠不是通行證**
- 任何風控否決：
  - 不接受辯護
  - 不接受事後合理化

---

### 2.4 Human-in-the-Loop 是設計前提
- 沒有人類確認：
  - 不得 Execution
- 沒有人類主權：
  - 系統視為不完整

---

## 第 3 章｜11 層 Canonical Flow 全覽（Overview）

TAITS 的所有行為，**必須依序通過以下 11 層**：

1. **Data Ingestion**  
2. **Data Normalization**  
3. **Market Snapshot**  
4. **Feature & Methodology**  
5. **Evidence Bundle**  
6. **Market Regime**  
7. **Risk & Compliance**  
8. **Strategy & Universe**  
9. **Governance Gate**  
10. **UI & Human Decision**  
11. **Execution & Control**

📌 **任何一層不可合併、不可省略、不可倒序。**

---

## 第 4 章｜為什麼一定要 11 層？（Necessity by Layer）

### 4.1 若沒有 Data Ingestion
- 無法確保資料來源合法
- 無法審計原始狀態

---

### 4.2 若沒有 Data Normalization
- 特徵計算不可重現
- 回測與實盤不可比

---

### 4.3 若沒有 Market Snapshot
- 系統行為不可回放
- 決策時間點不可定位

---

### 4.4 若沒有 Feature & Methodology
- Evidence 無法被結構化
- 訊號與雜訊無法區分

---

### 4.5 若沒有 Evidence Bundle
- 決策將退化為直覺
- 單一訊號被誤用

---

### 4.6 若沒有 Market Regime
- 策略適用性失效
- 高勝率策略被錯用

---

### 4.7 若沒有 Risk & Compliance
- 系統無法拒絕錯誤交易
- 法規風險被忽略

---

### 4.8 若沒有 Strategy & Universe
- 系統無法產生假設
- 僅剩觀察，無研究能力

---

### 4.9 若沒有 Governance Gate
- 流程可被繞過
- 錯誤無法被阻斷

---

### 4.10 若沒有 UI & Human Decision
- 人類主權被剝奪
- 系統變成黑箱

---

### 4.11 若沒有 Execution & Control
- 決策無法落地
- 風控無法即時介入

---

## 第 5 章｜資訊生命週期（Information Lifecycle）

本章定義 **TAITS 中「資訊如何誕生、轉化、被引用、被封存、被回放」的全過程**。  
任何不符合本生命週期的資料或結論，**在治理上視為不可用**。

---

### 5.1 資訊的法定狀態轉換

TAITS 對資訊的狀態轉換定義如下（不可跳步）：

1. **Raw Data（原始資料）**  
2. **Normalized Data（正規化資料）**  
3. **Snapshot（快照）**  
4. **Feature（特徵）**  
5. **Evidence（證據）**  
6. **Decision Context（決策脈絡）**  
7. **Execution Record（執行紀錄）**

📌 **未完成前一狀態，不得進入下一狀態。**

---

### 5.2 Raw Data 的法律地位
- 必須標註：
  - 官方來源
  - 取得時間
  - 版本
- 必須：
  - 原樣保存
  - 不得補值、不得推論

📌 Raw Data 是**唯一可以追溯真實市場狀態的證據來源**。

---

### 5.3 Normalized Data 的限制
- 僅允許：
  - 欄位對齊
  - 時間對齊
  - 單位轉換
- 不允許：
  - 修改數值
  - 製造不存在資料

📌 正規化是為了**一致性**，不是為了「看起來完整」。

---

### 5.4 Snapshot 的不可變性
- Snapshot 一旦生成：
  - 不得修改
  - 不得覆寫
- Snapshot 必須：
  - 可回放
  - 可被引用

📌 **沒有 Snapshot，就沒有可審計的決策。**

---

### 5.5 Feature 的角色界定
- Feature 是：
  - 對 Snapshot 的計算結果
- Feature 不是：
  - 交易建議
  - 決策方向

📌 Feature 必須標註：
- 計算方法
- 參數
- 適用 Regime

---

### 5.6 Evidence 的整合規則
Evidence 必須：
- 由多個 Feature 組成
- 標註：
  - 支持點
  - 反證點
  - 不確定性

📌 **單一 Feature 永遠不足以構成 Evidence。**

---

### 5.7 決策脈絡（Decision Context）
- Decision Context 包含：
  - Evidence Bundle
  - Regime 判定
  - Risk 結果
- Decision Context 本身：
  - 不等於決策
  - 僅供人類判斷

---

## 第 6 章｜Evidence Bundle 的法律地位與結構

### 6.1 Evidence Bundle 的法定定義
Evidence Bundle 為：
> **某一時間點，所有可用證據的完整集合**

Evidence Bundle 必須能回答：
- 為什麼支持？
- 為什麼反對？
- 哪裡不確定？

---

### 6.2 Evidence Bundle 的最小結構（強制）

每一個 Evidence Bundle **至少包含**：

1. 資料來源清單  
2. Feature 列表  
3. 支持證據  
4. 反證  
5. 衝突說明  
6. 完整度評估（Completeness Score）

📌 缺一 → **Evidence 不成立**。

---

### 6.3 Evidence 與策略的關係
- Evidence：
  - 不輸出交易方向
- Strategy：
  - 僅能引用 Evidence
  - 不得改寫 Evidence

📌 Strategy 若扭曲 Evidence，視為違規。

---

### 6.4 Evidence 的時效性
- Evidence 僅對應：
  - 特定 Snapshot
  - 特定時間
- 過期 Evidence：
  - 不得直接沿用
  - 必須重新生成

---

## 第 7 章｜Regime × Strategy × Risk 的先後關係（Order of Authority）

### 7.1 三者的權限排序（不可改）
**Regime → Risk / Compliance → Strategy**

📌 任何倒置順序，皆屬違反 Canonical。

---

### 7.2 Regime 的職權
- 判定：
  - 哪些策略**不可用**
- 不負責：
  - 預測
  - 給方向

---

### 7.3 Risk / Compliance 的職權
- 可：
  - 即時否決
  - 暫停
  - 降級
- 不可：
  - 給交易方向

---

### 7.4 Strategy 的職權
- 可：
  - 產生假設
  - 提出條件
- 不可：
  - 繞過 Regime / Risk
  - 要求例外

---

### 7.5 常見錯誤順序（永久禁止）
- 因策略好用 → 忽略 Regime  
- 因勝率高 → 降低風控  
- 因想交易 → 找證據  

📌 **這三種行為，正是 TAITS 要防止的核心錯誤。**

---

## 第 8 章｜Governance Gate 的法定角色（Process Legality Gate）

### 8.1 Governance Gate 的存在目的
Governance Gate 是 **Canonical Flow 的合法性閘門**。  
其目的不是提高效率，而是**阻止任何不合規、不完整、不可審計的流程前進**。

Governance Gate 必須回答三個問題：
1. 流程是否完整？
2. 證據是否可回放？
3. 行為是否符合治理文件？

📌 任一問題為否 → **立即 Block**。

---

### 8.2 Governance Gate 的輸入（Mandatory Inputs）
- Evidence Bundle（完整）
- Regime 判定結果
- Risk / Compliance 裁決
- 流程紀錄（L1–L8）
- 版本與 doc_key 參照

📌 缺任一輸入 → **Gate 不得放行**。

---

### 8.3 Governance Gate 的輸出（Binary）
- **Allow**：允許進入 L10  
- **Block**：阻止後續所有行為

📌 Governance Gate **不提供建議、不調整策略、不給例外**。

---

### 8.4 Governance Gate 的不可越權事項
- 不得覆寫 Risk / Compliance
- 不得修改 Evidence
- 不得代替人類決策
- 不得因績效、急迫性而放行

---

### 8.5 Governance Gate 的審計要求
每一次 Gate 裁決必須記錄：
- Gate ID
- 裁決結果（Allow / Block）
- 依據條款（doc_key + 章節）
- 時間戳
- 關聯 Correlation ID

📌 **無 Gate Log → 流程視為未通過**。

---

## 第 9 章｜Human-in-the-Loop 的制度化落地（Human Authority by Design）

### 9.1 為何必須有人類介入
TAITS 明確拒絕「全自動正確性」的幻想。  
人類介入的目的，是承擔**價值判斷與最終責任**。

---

### 9.2 人類介入的唯一合法層級
- 人類介入僅存在於：
  - **L10｜UI & Human Decision**

📌 人類**不得**：
- 在 L7 取代風控
- 在 L8 修改策略邏輯
- 在 L11 直接下指令繞過流程

---

### 9.3 人類決策的法定輸入
UI 必須完整呈現：
- Evidence Bundle（支持 / 反證 / 不確定）
- Regime 與其信心度
- Risk / Compliance 裁決與原因
- Governance Gate 狀態

📌 **缺任一項 → 人類不得被要求做決策**。

---

### 9.4 人類決策的法定輸出
合法的人類決策必須：
- 明確（Approve / Reject / Defer）
- 可記錄
- 可回放

不得使用：
- 模糊語句
- 條件式授權（如「看情況」）

---

### 9.5 人類主權與責任的對應
- 人類擁有：
  - 最終裁決權
- 人類承擔：
  - 最終責任

📌 **權責不可分離**。

---

## 第 10 章｜Execution 僅是結果，不是目標（Execution as Outcome）

### 10.1 Execution 的角色重新定義
在 TAITS 中，Execution 不是目的，而是**合法流程完成後的結果**。

沒有完整流程：
> **就不該有 Execution。**

---

### 10.2 Execution 的前置條件（全部必須滿足）
1. Canonical L1–L9 全部完成
2. Governance Gate = Allow
3. 人類於 L10 明確批准
4. Risk / Compliance 仍為 Pass

📌 任一失效 → **立即中止**。

---

### 10.3 Execution 的行為邊界
Execution 只能：
- 接收人類明確指令
- 執行合法委託
- 即時監控
- 觸發 Kill Switch

Execution 不得：
- 推論意圖
- 補單
- 追單
- 改寫策略

---

### 10.4 Execution 的即時中止（Kill Switch）
Kill Switch 可由以下來源觸發：
- Risk / Compliance
- 系統完整性檢測
- 人類主權

📌 Kill Switch **不需理由、立即生效**。

---

### 10.5 Execution 的審計輸出
必須生成：
- Execution Log
- Order / Fill 明細
- 中止原因（若有）
- 關聯 Correlation ID

📌 **無 Execution Log → 行為視為未發生**。

---

## 第 11 章｜全系統 Log、審計與回放的 Canonical 要求

### 11.1 為何審計是 Canonical 的一部分
在 TAITS 中：
- **沒有 Log 的行為，視為未發生**
- **無法回放的決策，視為不可被接受**

審計不是事後檢查，而是**行為合法性的前置條件**。

---

### 11.2 最小必要 Log（Mandatory Logs）
任何完整流程，**至少**必須產生以下 Log：

1. **Data Ingestion Log**  
   - 資料來源（官方）
   - 取得時間
   - 版本／批次識別

2. **Snapshot Log**  
   - Snapshot ID
   - 時間戳
   - 參照的 Raw / Normalized 資料

3. **Evidence Log**  
   - Feature 清單
   - 支持 / 反證
   - Completeness Score

4. **Regime Log**  
   - Regime 類型
   - 信心度
   - 適用與禁用策略清單

5. **Risk / Compliance Log**  
   - 裁決結果（Pass / Reject）
   - Reason Codes
   - 觸發條款

6. **Governance Gate Log**  
   - Allow / Block
   - 依據條款（doc_key + 章節）

7. **Human Decision Log**  
   - 決策類型（Approve / Reject / Defer）
   - 決策人
   - 時間戳

8. **Execution Log**（若有）  
   - 委託與成交明細
   - Kill Switch 事件
   - Correlation ID

📌 任一缺失 → **流程不完整**。

---

### 11.3 Correlation ID（因果鏈）
- 每一次流程必須：
  - 使用同一 Correlation ID
- 用於串接：
  - 資料 → 證據 → 風控 → 決策 → 執行

📌 **無 Correlation ID → 無法審計**。

---

### 11.4 回放（Replay）的最低要求
- 任一歷史流程必須能：
  - 重建 Snapshot
  - 重現 Evidence
  - 檢視當時有效文件版本
- 回放結果：
  - 不需與實際結果相同
  - 但必須**邏輯一致**

---

### 11.5 機密與隔離
- API Key / 憑證：
  - **不得進入 Repo**
- Log：
  - 不得洩漏敏感資訊
  - 必須遮罩必要欄位

---

## 第 12 章｜與下位文件的 Canonical 條款映射（必實作清單）

本章定義 **MASTER_CANON 條款 → 下位文件必須實作的位置**。  
下位文件未實作者，視為**不合格文件**。

---

### 12.1 Canonical 條款映射表

| MASTER_CANON 條款 | 必須實作文件 |
|---|---|
| 11 層不可跳步 | ARCH_FLOW |
| Evidence 結構與完整度 | ARCH_FLOW / STRATEGY_FEATURE_INDEX |
| Regime 先於 Strategy | RISK_COMPLIANCE / STRATEGY_UNIVERSE |
| Risk 最高否決 | RISK_COMPLIANCE |
| Governance Gate | ARCH_FLOW / UI_SPEC |
| Human-in-the-Loop | UI_SPEC / EXECUTION_CONTROL |
| Execution 僅承接人類指令 | EXECUTION_CONTROL |
| Log / Replay | VERSION_AUDIT / DEPLOY_OPS |

📌 下位文件若與本表不一致，**以本表為準**。

---

### 12.2 下位文件的最低責任
每一份下位文件，**至少**必須回答：
1. 我實作了哪一條 Canonical 條款？
2. 我在哪個流程層級生效？
3. 我的審計輸出是什麼？

---

## Canonical 最終宣告（Canonical Closing）

《MASTER_CANON》不是為了讓系統「更聰明」，  
而是為了讓系統**永遠保持可問責**。

在 TAITS 中：

- 快速但不可審計 → **不可接受**  
- 聰明但不可否決 → **不可接受**  
- 有績效但違反流程 → **不可接受**

> **只有當一套系統，  
> 能在誘惑、壓力與績效面前，  
> 仍然選擇遵守流程與責任，  
> 它才配被稱為「Canonical」。**

---
