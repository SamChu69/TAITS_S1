
# TAITS × V3.1 五層架構 — 差異補充文件（新增內容專用）

本文件列出「整合後架構」相較於原先兩份專案檔案：

1. **V3.1_Spec_Full_Final.md**  
2. **V3.1_285_Strategies.md**

所新增、強化或改動的部分，用於正式加入 TAITS 專案文件。

---

# 1. 全新新增的架構層（原始 Spec 無）

## 1.1 Layer 0 — Infra Layer（全新新增）
原 Spec 無以下項目，本次整合新增：

- **TimescaleDB**（統一儲存 K 線 / 籌碼 / Kronos）
- **Redis 快取層**（盤中毫秒級狀態）
- **EventBus**（Async Tick 分發機制）
- **Docker 化運行環境**

> 原 Spec 完全沒有 Infra 層，本次為重大擴充。

---

# 2. 原 Spec 沒有的核心概念與系統

## 2.1 雙腦架構（Fast Brain + Slow Brain）
**新增功能：**

### Slow Brain（1 分鐘分析）
- TradingAgents 升級版  
- 新增深度推理  
- 新聞、宏觀、法人、族群輪動整合  

### Fast Brain（5 秒級預測）
- Kronos 新模式  
- 5~10 根 K 線的未來預測  

### 全新訊號融合（Signal Fusion）
原 Spec 無此決策矩陣。

---

# 3. 原 Spec 沒有的 Lean 五模組

以下五個模組皆為新增：

1. **Universe Selection**  
2. **Alpha Model（訊號融合器）**  
3. **Portfolio Construction**  
4. **Risk Management（智能風控）**  
5. **Execution Model（下單模型）**

> 原 Spec 僅有 Strategy → Agents → Summary → Execution，無完整 Lean 架構。

---

# 4. 交易模式的重大新增

原 Spec 只有：

- Backtest  
- Sandbox  
- Paper  
- Live  

新增：

| 模式 | 說明 |
|------|------|
| Ignore | 只分析不交易 |
| PaperTrade（強化版） | 模擬滑價、委託機率 |
| Semi-Auto | 你按「確定」才下單 |
| Auto | 全自動執行 |

此為完整交易人機介面模式。

---

# 5. 盤中運行架構差異

## 5.1 原 Spec
- 無明確節奏  
- 無快軌 Vs 慢軌  
- 無 Tick 同步機制  

## 5.2 新增內容
- 慢軌（1 分鐘：深度分析）  
- 快軌（5 秒：Kronos 監控）  
- 事件驅動 EventBus  
- Redis 狀態同步  

> 使 TAITS 具備「盤中專業交易平台」的行為。

---

# 6. UI 新增項目（原 Spec 無）

- Kronos 未來 K 線預測圖  
- 族群輪動熱力圖  
- 新聞情緒雷達  
- 四模式切換介面  
- 盤中 Event & 狀態燈號  

---

# 7. 與 285 策略全集的差異

## 7.1 本次新增邏輯框架
- 策略不再單獨作用  
- 全部進入 Universe / Alpha / Portfolio Chain  
- 支援「多智能體 × 深度推理 × 短線預測」的策略流程  

## 7.2 新增可開發策略（原 285 無）
- 雙腦策略（LLM × Kronos 融合）  
- 快軌反轉策略（Kronos）  
- 慢軌盤勢策略（Agents）  
- 多模策略（Slow × Fast × Alpha）  

---

# 8. 原 Spec 無的「每日生命週期」

新增三階段明確化：

1. **Pre-Market（開盤前）**  
2. **In-Market（盤中快慢雙軌）**  
3. **Post-Market（收盤後）**  

原 Spec 內容較分散，此為新增完整週期架構。

---

# 9. 原 Spec 無的「整合後 TAITS 架構圖」

```
Layer 0: Infra
Layer 1: Data
Layer 2: Model (Slow Brain + Fast Brain)
Layer 3: Strategy (Lean 5 Modules)
Layer 4: Execution (4 Modes)
Layer 5: UI
```

此為新增整合版全景結構。

---

# 10. 結論：可加入 TAITS 的新增內容總表

| 類別 | 在原 Spec 是否存在 | 本次新增內容 |
|------|--------------------|---------------|
| Infra | ❌ 無 | TimescaleDB / Redis / EventBus / Docker |
| Model | 部分 | 雙腦架構 / Signal Fusion |
| Strategy | 有 | Lean 5 模組（完全新增） |
| Execution | 部分 | 四模式交易 |
| UI | 部分 | 未來 K 線、族群輪動、情緒雷達 |
| Data Flow | 部分 | 盤中快/慢軌、事件驅動、Redis 快取 |
| Life Cycle | ❌ 無 | Pre/In/Post 三階段 |

此 MD 文件應被放入：

```
docs/TAITS_v31_diff_supplement.md
```

作為專案正式補充說明。
