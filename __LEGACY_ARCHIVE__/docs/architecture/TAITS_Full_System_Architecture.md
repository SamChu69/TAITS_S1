# TAITS_Full_System_Architecture.md
# TAITS — 全系統完整體架構白皮書（Master System Blueprint）

版本：Master / Full  
文件角色：**母體架構的完整展開（Executable Blueprint）**  
上位文件：TAITS_MASTER_ARCHITECTURE.md  

---

## 0. 文件定位（必讀）

本文件回答三個問題：

1. TAITS **有哪些模組**
2. 模組之間 **如何互動**
3. 資料與決策 **如何從頭流到尾**

任何工程實作、回測、實盤、AI 接入，  
👉 **都必須能對應回本文件中的某一節點**。

---

## 1. One-Page 系統總覽

```text
Data Sources
   ↓
Data Layer
   ↓
Indicator / Factor Layer
   ↓
Strategy Layer (355+)
   ↓
Agents Layer
   ↓
Market Regime Engine
   ↓
Fusion Engine
   ↓
Portfolio / Risk Engine
   ↓
Execution (Backtest / Paper / Live)
   ↓
Reporting / UI / Audit
````

---

## 2. Orchestrator（系統調度核心）

**Orchestrator 是 TAITS 的中樞神經**，負責：

* 週期調度（盤前 / 盤中 / 盤後）
* 事件調度（Tick / Bar / News）
* 模組依賴順序
* Mode 切換（Backtest / Paper / Live）

> 沒有任何模組可以繞過 Orchestrator 直接呼叫下游。

---

## 3. Data Flow（資料流）

### 3.1 資料取得

來源限制：

* 僅允許 `TAITS_DataSources_Universe.md` 中列出的資料源

流程：

```text
API / WebSocket / Scraper
 → Validation（合法性 / 交易日 / 缺值）
 → Normalize（格式統一）
 → Storage（DB / Cache）
```

---

### 3.2 Cache 與 Fallback

* Redis：盤中狀態、快取
* DB：歷史資料、回測依據
* Fallback：官方 → 次級 → 快取

---

## 4. Indicator / Factor Layer

職責：

* 不做交易決策
* 僅負責 **數值與結構抽象**

輸出對象：

* Strategies
* Agents
* Regime
* Risk

---

## 5. Strategy Layer（355+）

策略行為規範：

* 不可互相呼叫
* 不可下單
* 不可直接引用券商 API
* 只輸出結構化 Signal

輸出格式（統一）：

```python
{
  "strategy": "Name",
  "signal": "BUY | SELL | HOLD",
  "confidence": 0.0,
  "reason": "中文可解釋文字",
  "tags": []
}
```

---

## 6. Agents Layer（多智能體）

Agents 的任務是 **跨策略彙總與語意判斷**。

範例：

* TechnicalAgent：技術一致性
* ChipAgent：籌碼偏向
* MacroAgent：外部環境
* DerivativesAgent：期權風險
* RiskAgent：否決權

---

## 7. Market Regime Engine

Regime 是 **上層約束條件**：

* TREND / RANGE / VOLATILE / PANIC
* CHIP_DOMINATED
* DERIVATIVES_DOMINATED

Regime 影響：

* 策略是否啟用
* 策略權重
* 倉位上限
* 是否允許新倉

---

## 8. Fusion Engine（決策融合）

輸入：

* Strategy Signals
* Agent Bias
* Market Regime

輸出：

```json
{
  "final_bias": "BULL | BEAR | NEUTRAL",
  "confidence": 0.0,
  "why": "融合理由"
}
```

---

## 9. Portfolio / Risk Engine

定位：**硬閘門**

* 合規檢查
* 曝險控制
* 流動性
* 停損
* 熔斷

> 若 Risk = BLOCKED → 不得下單

---

## 10. Execution Layer

Execution 僅處理「怎麼下單」，不處理「要不要下單」。

模式：

* Backtest
* Paper
* Live（券商）

---

## 11. Reporting / Audit

所有決策必須留下：

* 輸入資料
* 策略輸出
* Agent 判斷
* Regime
* Fusion
* Risk

> **任何一筆交易都可被完整重建**

---

## 12. 與其他文件的關係

* 本文件 **展開** `TAITS_MASTER_ARCHITECTURE.md`
* 本文件 **依賴** `TAITS_DataSources_Universe.md`
* 本文件 **引用** `TAITS_Strategy_Universe_Complete.md`
* 本文件 **受制於** `TAITS_Risk_and_Compliance.md`

---

## 13. 一句話總結

> **如果你想知道
> TAITS「怎麼跑起來」，
> 就讀這一份。**

---
