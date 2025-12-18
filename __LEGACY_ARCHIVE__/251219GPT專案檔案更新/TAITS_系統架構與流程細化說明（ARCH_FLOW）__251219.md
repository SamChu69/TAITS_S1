📘 TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219
PART 1｜文件定位 × Canonical Flow 工程化原則 × L1–L2
# TAITS_系統架構與流程細化說明（ARCH_FLOW）
## Architecture & Canonical Flow Specification

---

## 架構說明前言（Why ARCH_FLOW Exists）

若《MASTER_CANON》定義的是：
> **「正確的流程長什麼樣子」**

那麼《ARCH_FLOW》定義的是：
> **「每一層實際要負什麼責任、產出什麼、留下什麼證據」**

本文件的角色是 **把 Canonical Flow 變成不可偷懶的工程事實**。

---

## 第 1 章｜ARCH_FLOW 的治理位階與約束

### 1.1 文件位階
- 治理等級：**B（架構實作級）**
- 上位文件：
  - `MASTER_ARCH`
  - `MASTER_CANON`
- 下位文件：
  - `EXECUTION_CONTROL`
  - `RISK_COMPLIANCE`
  - `UI_SPEC`

📌 本文件 **不得創造新流程，只能展開 Canonical Flow**。

---

### 1.2 本文件的禁止事項
- 不得：
  - 合併流程層級
  - 以「實務方便」為由省略層
  - 以績效或速度合理化跳步
- 不得：
  - 讓 Strategy / AI 取得非其層級的權限

---

### 1.3 工程化三原則（Engineering Laws）

**原則一｜層級即責任**
- 每一層必須：
  - 有唯一責任
  - 有明確邊界

**原則二｜輸入輸出可驗證**
- 每一層：
  - 必須明確定義 Input / Output
  - Output 必須可被下一層驗證

**原則三｜無 Log 即無行為**
- 任一層未留下 Log：
  - 該層視為未執行
  - 整條流程失效

---

## 第 2 章｜Canonical Flow 全層責任總覽

| 層級 | 名稱 | 核心責任 |
|---|---|---|
| L1 | Data Ingestion | 合法取得原始資料 |
| L2 | Data Normalization | 資料一致化 |
| L3 | Market Snapshot | 凍結市場狀態 |
| L4 | Feature & Methodology | 結構化計算 |
| L5 | Evidence Bundle | 證據整合 |
| L6 | Market Regime | 適用性判定 |
| L7 | Risk & Compliance | 最高否決 |
| L8 | Strategy & Universe | 假設生成 |
| L9 | Governance Gate | 合法性檢查 |
| L10 | UI & Human Decision | 人類裁決 |
| L11 | Execution & Control | 合法執行 |

📌 本表僅為索引，**細節以下逐層定義**。

---

## 第 3 章｜L1：Data Ingestion（資料取得層）

### 3.1 層級目的（Purpose）
確保所有後續分析與決策，**建立在合法、可追溯、未加工的原始資料上**。

---

### 3.2 合法輸入（Inputs）
- 官方資料來源（列於 `DataSources_Universe`）
- API / 檔案 / 串流
- 明確的來源識別（Source ID）

---

### 3.3 輸出（Outputs）
- Raw Data Record
- Ingestion Metadata：
  - Source
  - Timestamp
  - Version / Batch ID

📌 L1 **不得輸出任何分析結果**。

---

### 3.4 永久禁止事項
- 不得：
  - 補值
  - 推論
  - 平滑
  - 填補缺失
- 不得：
  - 合併不同來源數據
  - 改寫原始欄位

📌 L1 的責任只有一個：**忠實記錄**。

---

### 3.5 審計與 Log 要求
必須產生：
- Data Ingestion Log
- 原始檔案或 Payload Hash
- Correlation ID

📌 無 Hash → 無法證明資料未被改動。

---

## 第 4 章｜L2：Data Normalization（資料正規化層）

### 4.1 層級目的
讓不同來源、不同格式的資料，  
**在不改變事實的前提下具備可比較性**。

---

### 4.2 合法輸入
- 僅能來自：
  - L1 Raw Data

---

### 4.3 合法輸出
- Normalized Data
- Normalization Rule Set（版本化）

---

### 4.4 允許行為
- 時間對齊
- 欄位重新命名
- 單位轉換
- 缺失值標註（非補值）

---

### 4.5 永久禁止事項
- 製造不存在資料
- 使用未聲明的補值邏輯
- 因模型需求改寫數值

📌 **正規化是格式處理，不是數據修正。**

---

### 4.6 審計與 Log 要求
- Normalization Log
- Rule Set ID
- 前後資料 Hash 比對
- Correlation ID

---

（ARCH_FLOW · PART 1 結束）

PART 2｜L3 市場狀態凍結 × L4 方法論與特徵工程

## 第 5 章｜L3：Market Snapshot（市場狀態凍結層）

### 5.1 層級目的（Purpose）
L3 的唯一目的，是在**某一確定時間點**，將市場狀態**不可逆地凍結**，  
使後續所有分析、證據、決策，**都能回到同一個事實基準**。

📌 **沒有 Snapshot，就不存在可審計的決策。**

---

### 5.2 合法輸入（Inputs）
- 僅能來自：
  - L2 Normalized Data
- 必須附帶：
  - 完整 Correlation ID
  - Normalization Rule Set ID

---

### 5.3 Snapshot 的法定內容（Mandatory Fields）
每一個 Snapshot **至少**包含：
- 市場時間（Exchange Time）
- 標的 Universe
- 價格 / 成交量 / 委買賣（依資料來源）
- 市場狀態附註（如：開盤、盤中、收盤）
- 資料完整度標記（Completeness Flag）

📌 Snapshot **不是單一表格**，而是**一組不可變資料集合**。

---

### 5.4 不可變性（Immutability）
- Snapshot 一旦生成：
  - ❌ 不得修改
  - ❌ 不得覆寫
  - ❌ 不得補資料
- 任何修正需求：
  - 必須生成 **新的 Snapshot**

📌 **修正 = 新事實，不是修補舊事實。**

---

### 5.5 Snapshot 與時間的關係
- Snapshot 僅對應：
  - 一個時間點
- 不得：
  - 延用到其他時間
  - 合併多時間點

---

### 5.6 永久禁止事項
- 以最新資料覆寫舊 Snapshot
- 在 Snapshot 後補寫當時不存在的資料
- 將 Feature 當作 Snapshot 內容

---

### 5.7 審計與 Log 要求
- Snapshot ID
- Snapshot Time
- Input Data Hash
- Completeness Flag
- Correlation ID

📌 **缺任一項 → Snapshot 視為不合法。**

---

## 第 6 章｜L4：Feature & Methodology（特徵與方法論層）

### 6.1 層級目的
L4 的目的，是將凍結的市場狀態，  
**以可解釋、可重現、可審計的方法轉換為結構化描述**。

📌 L4 是**計算層**，不是決策層。

---

### 6.2 合法輸入
- 僅能來自：
  - L3 Snapshot
- 必須標註：
  - Snapshot ID
  - Methodology Version

---

### 6.3 合法輸出
- Feature Set
- Methodology Descriptor：
  - 計算公式
  - 參數
  - 適用 Regime
  - 已知限制

---

### 6.4 Feature 的法律地位
- Feature 是：
  - 對 Snapshot 的描述
- Feature **不是**：
  - 訊號
  - 建議
  - 方向

📌 **Feature ≠ Signal ≠ Decision**

---

### 6.5 允許的 Methodology 類型（示例）
- 技術指標計算（EMA、ATR、ADX 等）
- 統計量（分位數、偏態、波動）
- 結構描述（趨勢段、震盪區）
- 流動性與成交結構

📌 是否「好用」**不構成合法性**。

---

### 6.6 永久禁止事項
- 使用未定義方法論
- 將未來資料滲入計算（Look-ahead）
- 因策略需求調整 Feature 定義
- 將 Feature 包裝成交易建議

---

### 6.7 Feature 與 Regime 的關係
- 每一 Feature **必須標註**：
  - 適用 Regime
  - 不適用 Regime
- 未標註 → Feature **不得被 Evidence 引用**

---

### 6.8 審計與 Log 要求
- Feature ID
- Methodology Version
- Input Snapshot ID
- Feature Value Hash
- Correlation ID

📌 **無 Methodology 描述 → Feature 不合法。**

---

（ARCH_FLOW · PART 2 結束）

PART 3｜L5 證據整合 × L6 市場狀態判定（治理密度核心）

## 第 7 章｜L5：Evidence Bundle（證據整合層）

### 7.1 層級目的（Purpose）
L5 的目的，是將 **L4 產生的多個 Feature**，  
在不給方向、不下結論的前提下，  
**組織成可被質疑、可被反證、可被回放的「證據包」**。

📌 L5 是 **決策前最後一道「非方向性」層級**。

---

### 7.2 合法輸入（Inputs）
- 僅能來自：
  - L4 Feature Set
- 必須附帶：
  - Feature ID
  - Methodology Version
  - 適用 / 不適用 Regime 標註
  - 完整 Correlation ID

---

### 7.3 Evidence Bundle 的最小結構（強制）
每一個 Evidence Bundle **至少必須包含**：

1. **Feature 清單（Feature Inventory）**  
   - 含 Feature ID、來源、版本

2. **支持證據（Supporting Evidence）**  
   - 支持某一市場描述的 Feature

3. **反證（Contradictory Evidence）**  
   - 與支持證據相衝突的 Feature

4. **衝突說明（Conflict Analysis）**  
   - 為何衝突
   - 衝突是否可解釋

5. **不確定性（Uncertainty Notes）**  
   - 資料不足
   - 方法限制

6. **完整度評估（Completeness Score）**  
   - 覆蓋面
   - 資料新鮮度
   - 一致性

📌 缺任一項 → **Evidence Bundle 不成立**。

---

### 7.4 Evidence 的法律地位
- Evidence 是：
  - 描述市場狀態的證據集合
- Evidence **不是**：
  - 交易建議
  - 策略輸出
  - 決策結論

📌 **Evidence 只能被引用，不能被改寫。**

---

### 7.5 永久禁止事項
- 只呈現支持證據、隱藏反證
- 為配合策略而刪除 Evidence
- 將 Evidence 分數化後直接給方向
- 用績效結果回頭篩選 Evidence

---

### 7.6 Evidence 的時間與效力
- Evidence 僅對應：
  - 單一 Snapshot
- 不得：
  - 跨 Snapshot 混用
  - 事後補寫

---

### 7.7 審計與 Log 要求
- Evidence Bundle ID
- Feature Inventory
- 衝突說明紀錄
- Completeness Score
- Correlation ID

📌 **Evidence 無法回放 → 視為不存在。**

---

## 第 8 章｜L6：Market Regime（市場狀態判定層）

### 8.1 層級目的
L6 的目的，是在 Evidence Bundle 的基礎上，  
**判定「哪些策略類型不適用」**，  
而不是預測市場將如何變動。

📌 Regime 是**適用性裁決者，不是方向預測器**。

---

### 8.2 合法輸入
- 僅能來自：
  - L5 Evidence Bundle
- 不得直接引用：
  - Feature 原始值
  - 歷史績效

---

### 8.3 合法輸出
- Regime Label（可多重）
- Regime Confidence（信心區間）
- 禁用策略類型清單
- Regime 限制說明

📌 Regime 的輸出 **必須以「禁用」為主語**。

---

### 8.4 Regime 的法律邊界
Regime **可以**：
- 禁止某類策略啟用
- 限制某些風險假設

Regime **不得**：
- 指定買或賣
- 推薦策略
- 否決 Risk / Compliance

---

### 8.5 常見錯誤用法（永久禁止）
- 用 Regime 當方向訊號
- 用 Regime 信心度當下單依據
- 用 Regime 事後解釋虧損

---

### 8.6 Regime 的不確定性處理
- 若 Evidence 衝突過高：
  - Regime 必須：
    - 標註為「不穩定 / 混合」
- 不穩定 Regime：
  - 預設 **提高風控嚴格度**
  - 預設 **縮小策略白名單**

---

### 8.7 審計與 Log 要求
- Regime ID
- Evidence Bundle ID
- Regime Label 與信心區間
- 禁用策略清單
- Correlation ID

📌 **Regime 不可回放 → 全流程無效。**

---

（ARCH_FLOW · PART 3 結束）

PART 4｜L7 最高否決 × L8 假設生成（風控與策略的分水嶺）

## 第 9 章｜L7：Risk & Compliance（最高否決層）

### 9.1 層級目的（Purpose）
L7 的唯一目的，是在**最壞情境（Worst-case）視角下**，  
對任何可能進入交易流程的行為，行使**即時、不可協商的否決權**。

📌 **L7 不追求「合理」，只追求「安全與合規」。**

---

### 9.2 合法輸入（Inputs）
- 僅能來自：
  - L6 Regime 判定結果
  - L5 Evidence Bundle
- 必須附帶：
  - Regime 限制說明
  - Evidence Completeness Score
  - 完整 Correlation ID

📌 L7 **不得**直接引用 Feature 原始值或策略績效。

---

### 9.3 合法輸出（Binary）
- **Pass**：允許流程前進  
- **Reject**：立即否決（可附帶降級建議）

📌 Reject 一經產生，**不得被任何下位層覆寫**。

---

### 9.4 否決的法定理由（Reason Codes）
否決理由必須屬於以下類型之一（可多選）：
- 法規 / 交易所規則風險
- 流動性不足
- 風險集中度過高
- Evidence 不完整或衝突過高
- Regime 不穩定
- 系統完整性異常

📌 **不得使用模糊理由（如「感覺不安全」）。**

---

### 9.5 L7 的權限邊界
L7 **可以**：
- 直接否決
- 降級建議（如：Observe-only）

L7 **不得**：
- 建議買賣方向
- 推薦策略
- 指定交易參數

---

### 9.6 永久禁止事項
- 因績效壓力降低否決標準
- 事後合理化未否決行為
- 將 L7 視為形式流程

📌 **一個不敢否決的風控，不是風控。**

---

### 9.7 審計與 Log 要求
- Risk Decision ID
- 裁決結果（Pass / Reject）
- Reason Codes
- 依據條款（doc_key + 章節）
- Correlation ID

📌 **無 Reason Code 的裁決 → 視為不合法。**

---

## 第 10 章｜L8：Strategy & Universe（假設生成層）

### 10.1 層級目的
L8 的目的，是在 **Regime 已裁決、Risk 未否決** 的前提下，  
生成**可被人類評估的交易假設**。

📌 L8 生成的是 **Hypothesis，不是 Order**。

---

### 10.2 合法輸入
- 必須同時滿足：
  - L7 = Pass
  - L6 Regime 限制
  - L5 Evidence Bundle
- 不得輸入：
  - Execution 結果
  - 人類偏好（除非文件化）

---

### 10.3 合法輸出
- Strategy Hypothesis
- 適用 Universe
- 前提假設清單
- 失效條件（Invalidation Conditions）

📌 無失效條件 → 策略假設不成立。

---

### 10.4 Strategy Hypothesis 的最低內容
每一個策略假設 **至少包含**：
- 為何在此 Regime 可能有效
- Evidence 支持與反證
- 預期風險型態
- 何時應該放棄（Invalidation）

---

### 10.5 Strategy 的法律邊界
Strategy **可以**：
- 描述條件
- 提出可能性

Strategy **不得**：
- 要求例外放行
- 繞過風控
- 指定下單細節

---

### 10.6 Universe 的治理要求
- Universe 必須：
  - 符合 Scope Freeze
  - 可被審計
- Universe 不得：
  - 動態擴張未記錄
  - 因策略需求臨時放寬

---

### 10.7 永久禁止事項
- 在 L7 = Reject 時生成策略
- 事後調整策略理由以通過審計
- 將策略假設包裝成「必然性」

---

### 10.8 審計與 Log 要求
- Strategy Hypothesis ID
- Evidence Bundle ID
- Regime 參照
- Invalidation Conditions
- Correlation ID

📌 **無 Invalidation → 無合法策略。**

---

（ARCH_FLOW · PART 4 結束）

PART 5｜L9 合法性總檢 × L10 人類裁決 × L11 合法執行（最終閉環）

## 第 11 章｜L9：Governance Gate（合法性總檢層）

### 11.1 層級目的（Purpose）
L9 的目的，是在**任何人類或系統行為發生之前**，  
對整條 Canonical Flow 進行**一次不可跳過的合法性總檢**。

📌 L9 是「流程是否存在」的裁判，而不是效率加速器。

---

### 11.2 合法輸入（Mandatory Inputs）
L9 僅在以下輸入**全部齊備**時才可啟動：

- L1–L8 全流程 Log（完整）
- L7 Risk / Compliance = Pass
- Strategy Hypothesis（含 Invalidation）
- Scope Freeze 驗證結果
- 文件版本參照（doc_key + version）
- 完整 Correlation ID

📌 任一缺失 → **Gate 必須 Block**。

---

### 11.3 合法輸出（Binary）
- **Allow**：允許進入 L10  
- **Block**：中止流程（不得提示繞過）

📌 L9 **不給建議、不調整內容、不給例外**。

---

### 11.4 L9 的不可越權事項
- 不得覆寫 L7 否決
- 不得修改 Strategy 假設
- 不得預測人類決策
- 不得因時間壓力放行

---

### 11.5 審計與 Log 要求
- Governance Gate ID
- Allow / Block
- Block Reason（doc_key + 章節）
- 時間戳
- Correlation ID

📌 **無 Gate Log → 流程視為未通過。**

---

## 第 12 章｜L10：UI & Human Decision（人類裁決層）

### 12.1 層級目的
L10 是 **TAITS 中唯一允許人類主權介入的層級**。

其目的不是提高勝率，  
而是讓人類在**完整知情、可被追責**的前提下，  
做出是否承擔風險的選擇。

---

### 12.2 合法輸入（UI 必須完整呈現）
UI **必須同時呈現**：

- Evidence Bundle（支持 / 反證 / 不確定）
- Regime 判定與限制
- Risk / Compliance 裁決與 Reason Codes
- Strategy Hypothesis（含失效條件）
- Governance Gate = Allow
- 文件版本與 Correlation ID

📌 缺任一項 → **不得要求人類做決策**。

---

### 12.3 合法輸出（Human Decision）
人類只能輸出以下三種之一：

- **Approve**：同意進入 Execution
- **Reject**：終止流程
- **Defer**：暫不行動（Observe-only）

📌 不得輸出模糊或條件式決策。

---

### 12.4 人類裁決的責任對應
- Approve：
  - 人類承擔執行後果
- Reject / Defer：
  - 系統必須尊重
  - 不得再推進流程

📌 **系統不得對人類裁決進行價值評分。**

---

### 12.5 審計與 Log 要求
- Human Decision ID
- 決策類型
- 決策人
- 時間戳
- Correlation ID

📌 **無 Human Decision Log → Execution 不得啟動。**

---

## 第 13 章｜L11：Execution & Control（合法執行層）

### 13.1 層級目的
L11 的目的，是在**所有合法條件都已滿足後**，  
將人類明確決策轉換為實際執行行為，  
並在執行過程中持續接受風控與中止控制。

📌 Execution 是結果，不是權力。

---

### 13.2 合法輸入（全部必須成立）
- L10 Human Decision = Approve
- L9 Governance Gate = Allow
- L7 Risk / Compliance = Pass（仍有效）
- Scope Freeze 驗證通過
- Execution 參數（明確、可審計）
- Correlation ID

📌 任一失效 → **不得執行**。

---

### 13.3 Execution 的行為邊界
Execution **可以**：
- 下達合法委託
- 監控成交與狀態
- 即時回報

Execution **不得**：
- 推論未給定參數
- 追單、補單
- 改寫策略假設

---

### 13.4 即時中止與 Kill Switch
Kill Switch 可由以下觸發：
- Risk / Compliance
- 系統完整性檢測
- 人類主權

📌 Kill Switch **立即生效、不可延遲、不可質疑**。

---

### 13.5 審計與 Log 要求
- Execution Log
- Order / Fill 明細
- Kill Switch 事件（若有）
- Correlation ID

📌 **無 Execution Log → 行為視為未發生。**

---

## ARCH_FLOW 最終整體約束宣告（Closing）

《ARCH_FLOW》存在的目的，  
不是讓 TAITS「跑起來」，  
而是確保 **TAITS 永遠不會在錯誤的狀態下跑起來**。

在 TAITS 中：

- 跳過任何一層 = 整條流程無效  
- 無法回放的流程 = 不存在  
- 未經人類確認的執行 = 違規  

> **一套真正可長期運作的系統，  
> 不是跑得最快，  
> 而是最不容易在壓力下犯錯。**

---

（ARCH_FLOW · PART 5 完成）
