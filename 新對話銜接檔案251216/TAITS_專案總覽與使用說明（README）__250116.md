# TAITS_專案總覽與使用說明（README）__250116.md

> doc_key：README  
> 治理等級：A（專案入口與定位說明｜對外唯一入口）  
> 適用範圍：TAITS 全專案  
> 版本狀態：ACTIVE（Only-Add，可擴充不可縮水）

---

## 0. 專案定位（Project Positioning）

**TAITS – Taiwan Alpha Intelligence Trading System**  
是一套為 **台灣市場（TWSE / TPEx / TAIFEX）** 所設計的：

- 長期可演進
- 可實盤、可審計
- 以 **Regime × Risk × Governance** 為核心
- AI 輔助、但 **人類主權最終裁決**

的完整智能交易系統母體。

📌 TAITS 不是 Demo  
📌 不是教學系統  
📌 不是自動下單工具  

> **TAITS 是一套「知道什麼時候不該交易」的系統。**

---

## 1. 核心設計哲學（不可動搖）

TAITS 的所有設計，遵循以下不可違反原則：

- 策略 ≠ 下單
- Agent ≠ 策略
- AI ≠ 唯一真理
- **Regime 高於任何單一訊號**
- **Risk / Compliance 具最高否決權**
- 官方資料優先，多層 fallback
- 架構必須可長期演進、不可縮水

---

## 2. TAITS 在做什麼（What TAITS Does）

TAITS 將交易行為拆解為一條 **不可跳步的 Canonical Flow**：

1. 蒐集資料
2. 正規化與快照
3. 建立證據
4. 判定 Regime
5. 風控與合規否決
6. 策略僅作為假設
7. 人類決策
8. 受控執行
9. 全流程可回放、可審計

📌 **交易只是結果，不是目標。**

---

## 3. 文件體系總覽（Documentation System）

TAITS 的所有行為，**必須以文件為最高依據**。  
文件之間的效力關係，統一由：

- `DOCUMENT_INDEX`

進行裁決。

### 文件等級概覽

| 等級 | 說明 |
|----|----|
| A | 母體 / 索引 |
| B | Canonical / 架構 |
| C | 營運 / 治理 |
| D | 策略 / 分析 |
| E | 風控 / 合規 |
| F | 教學 / 操作 |

📌 **低等級文件不得影響高等級裁決。**

---

## 4. 新使用者如何開始（Quick Start）

### 建議流程

1. 閱讀：
   - MASTER_CANON
   - FULL_ARCH
2. 理解：
   - 為什麼 TAITS 不自動下單
3. 熟悉：
   - DATA_UNIVERSE
   - STRATEGY_FEATURE_INDEX
4. 練習：
   - 在 Evidence 不完整時選擇「不行動」

📌 新手 **不得直接進入 Live**。

---

## 5. TAITS 與 AI 的關係

- AI：
  - 協助分析
  - 協助整理證據
  - 協助風險提示
- AI **不得**：
  - 取代人類決策
  - 繞過風控
  - 自行下單

> **AI 是副駕，不是駕駛。**

---

## 6. TAITS 的長期演進方向

TAITS 被設計為：

- 可新增策略
- 可新增 Agent
- 可新增資料來源
- 可新增市場

但：

- Canonical Flow 不被破壞
- Risk / Compliance 不被稀釋
- Document_Index 永遠是裁決來源

---

## 7. 使用與修改的基本原則

- 所有修改：
  - 必須新增版本
  - 必須可追溯
- 不確定是否能改：
  - 先查 Document_Index
- 覺得系統「太保守」：
  - 代表系統正在正常運作

---

## 8. 最終專案宣告（Final Statement）

> **TAITS 的目標不是擊敗市場，  
而是在市場不值得參與時，  
能夠理直氣壯地選擇不參與。**

---

（End of README）
