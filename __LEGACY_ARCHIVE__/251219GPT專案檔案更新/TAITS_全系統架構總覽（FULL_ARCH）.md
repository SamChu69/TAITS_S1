# TAITS_全系統架構總覽（FULL_ARCH）
## Taiwan Alpha Intelligence Trading System
### FULL SYSTEM ARCHITECTURE OVERVIEW
### 版本日期：2025-12-19
### 治理等級：B（Canonical · 系統架構總覽）
### 狀態：ACTIVE（同版融合更新）
### 覆寫權限：僅人類主權

---

## 0. 文件定位（Architecture-as-Map）

本文件為 **TAITS 的「系統架構地圖」**。

其目的不是重述流程細節，而是：

- 說明 **整個 TAITS 由哪些模組構成**
- 說明 **模組如何沿著 11 層 Canonical Flow 排列**
- 明確劃出：
  - 模組邊界
  - 模組責任
  - 模組禁止事項

📌 若你只看流程，不看本文件，  
你知道「怎麼走」，但不知道「整個系統長什麼樣」。

---

## 1. 架構總體設計原則（不可違反）

TAITS 全系統架構遵守以下原則：

1. **Layered, not tangled**  
   - 嚴格分層
   - 禁止跨層捷徑

2. **Modules with jurisdiction**  
   - 每個模組都有明確職權
   - 無模糊責任區

3. **Governance over performance**  
   - 治理優先於效能
   - 可慢，但不可失控

4. **AI is contained**  
   - AI 必須被模組包裹
   - 不得成為自由行為體

---

## 2. 架構視角一｜縱向：11 層 Canonical Flow

以下為 **從上到下的系統縱向結構**：

L1 Data Ingestion
L2 Data Normalization
L3 Market Snapshot
L4 Feature & Methodology
L5 Evidence Bundle
L6 Market Regime
L7 Risk & Compliance
L8 Strategy & Universe
L9 Governance Gate
L10 UI & Human Decision
L11 Execution & Control

yaml
複製程式碼

📌 本文件不重複各層細節，  
詳細行為定義請見 **ARCH_FLOW**。

---

## 3. 架構視角二｜橫向：核心模組群（Modules）

TAITS 由以下 **七大核心模組群** 組成：

1. Data & Ingestion Module  
2. Snapshot & State Module  
3. Feature & Evidence Module  
4. Regime & Risk Module  
5. Strategy & Research Module  
6. Governance & Audit Module  
7. Execution & Ops Module  

---

## 4. 模組群 × Canonical 層級對照

### 4.1 Data & Ingestion Module
**對應層級**
- L1 / L2

**職責**
- 取得資料
- 正規化
- 封存原始狀態

**禁止**
- 推論
- 補值
- 資料裁剪

---

### 4.2 Snapshot & State Module
**對應層級**
- L3

**職責**
- 建立可回放市場狀態
- 提供所有後續分析的唯一基準

**禁止**
- 動態未封存狀態
- 僅即時計算

---

### 4.3 Feature & Evidence Module
**對應層級**
- L4 / L5

**職責**
- 特徵計算
- 證據整合
- 衝突與完整度標註

**禁止**
- 產生交易方向
- 隱性策略

---

### 4.4 Regime & Risk Module
**對應層級**
- L6 / L7

**職責**
- 市場狀態判定
- 風險與合規否決

**權限**
- 跨模組即時否決

**禁止**
- 為績效讓步
- 被策略影響結論

---

### 4.5 Strategy & Research Module
**對應層級**
- L8

**職責**
- 產生策略假設
- 管理策略宇宙

**限制**
- 永遠不下單
- 永遠受 Regime / Risk 約束

---

### 4.6 Governance & Audit Module
**對應層級**
- L9（橫向貫穿）

**職責**
- 流程合法性檢查
- 文件一致性檢查
- 版本與行為審計

**禁止**
- 預設放行
- 隱性例外

---

### 4.7 Execution & Ops Module
**對應層級**
- L11（承接 L10）

**職責**
- 執行人類指令
- 即時監控
- Kill Switch

**禁止**
- 無人值守
- 自動補單

---

## 5. AI 在系統架構中的位置（嚴格受控）

在 TAITS 中：

- AI **不是一個模組**
- AI 是：
  - 嵌入於模組內的「輔助能力」
- AI 的所有輸出：
  - 必須標註所屬模組
  - 必須符合該模組治理規範

📌 不存在「AI 自由層」。

---

## 6. 模組之間的通訊原則

- 僅允許：
  - 相鄰層級通訊
  - 向下流動（資料 → 決策 → 執行）
- 禁止：
  - 逆向回寫
  - 橫向繞過 Regime / Risk

---

## 7. 擴充與演進原則

- 可新增：
  - 模組內子元件
  - 新分析方法
- 不可：
  - 改變模組邊界
  - 合併模組以求效率
  - 將 AI 提升為模組級主體

---

## 8. FULL_ARCH 最終宣告

> **如果 Canonical Flow 是法律條文，  
FULL_ARCH 就是城市地圖。  
沒有地圖，  
你不知道自己現在站在哪裡。**

---

