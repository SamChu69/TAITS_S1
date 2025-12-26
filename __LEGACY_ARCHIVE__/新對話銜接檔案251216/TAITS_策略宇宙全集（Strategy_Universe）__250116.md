# TAITS_策略宇宙全集（Strategy_Universe）__250116.md

> doc_key：STRATEGY_UNIVERSE  
> 治理等級：D（策略與研究層｜受制於 Regime / Risk / Governance）  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
> 版本狀態：ACTIVE（Only-Add，可擴充不可縮水）

---

## 0. 文件定位（Strategy-as-Hypothesis）

本文件定義 **TAITS 可被研究、測試與引用的「策略宇宙全集」**。  
在 TAITS 中，「策略」的法律地位為：

> **策略 = 可被驗證的假設（Hypothesis），  
> 而不是交易指令。**

📌 本文件：
- **不授權任何下單行為**
- **不保證策略有效**
- 僅定義「TAITS 允許存在、被研究的策略範圍」

---

## 1. 策略治理核心原則（不可違反）

### 1.1 策略 ≠ 交易行為

- 策略只能輸出：
  - 條件（Conditions）
  - 情境（Scenarios）
  - 假設（Hypotheses）
- 策略 **不得**：
  - 產生下單指令
  - 繞過 Regime / Risk / Governance

---

### 1.2 策略必須可定位（Traceable）

每一個策略，至少必須標註：

- 所屬策略類型
- 適用市場 Regime
- 依賴資料類型
- 不適用情境

📌 無法標註者，**視為非法策略**。

---

### 1.3 單一策略永不構成決策依據

- 再高勝率策略：
  - 也只能作為 Evidence Bundle 的一部分
- **單一策略觸發 ≠ 進場理由**

---

## 2. 策略宇宙分類總覽（Taxonomy）

TAITS 將策略劃分為九大類：

1. 趨勢型策略（Trend Following）
2. 均值回歸策略（Mean Reversion）
3. 突破與結構策略（Breakout / Structure）
4. 波動與狀態策略（Volatility / Regime）
5. 成交與流動性策略（Volume / Liquidity）
6. 基本面策略（Fundamental）
7. 事件與情境策略（Event / Scenario）
8. 跨市場與相對價值策略（Intermarket / RV）
9. 防禦與保護型策略（Defensive / Protection）

---

## 3. 趨勢型策略（Trend Following）

**核心假設**
- 價格在特定 Regime 下具有延續性

**常見方法**
- 均線系統（MA / EMA / GMMA）
- 趨勢通道
- 高低點結構

**適用 Regime**
- 中低波動趨勢市

**禁止**
- 盤整 Regime 強行使用

---

## 4. 均值回歸策略（Mean Reversion）

**核心假設**
- 價格偏離統計均值後回歸

**常見方法**
- RSI / Z-score
- Bollinger Bands
- 價差回歸

**適用 Regime**
- 低波動盤整

**風險**
- 趨勢市誤用風險極高

---

## 5. 突破與結構策略（Breakout / Structure）

**核心假設**
- 結構被突破後產生新定價區間

**常見方法**
- 區間突破
- 支撐壓力轉換
- 型態結構（旗形、三角）

**適用 Regime**
- 波動擴張前期

---

## 6. 波動與狀態策略（Volatility / Regime）

**核心假設**
- 波動本身具有可預測結構

**常見方法**
- ATR 狀態
- 波動收斂 / 發散
- Regime Switching

**用途**
- 策略啟停
- 部位調整

📌 通常作為 **輔助策略**。

---

## 7. 成交與流動性策略（Volume / Liquidity）

**核心假設**
- 成交行為反映市場意圖

**常見方法**
- 量價關係
- 成交密度
- 流動性斷層

**限制**
- 低流動性標的不適用

---

## 8. 基本面策略（Fundamental）

**核心假設**
- 價格長期反映基本面

**資料來源**
- 財報
- 公司治理
- 產業結構

**用途**
- 結構判斷
- Regime 輔助

📌 **不得作為短線進出依據**。

---

## 9. 事件與情境策略（Event / Scenario）

**核心假設**
- 特定事件改變市場狀態

**事件類型**
- 財報
- 法說
- 法規
- 重大公告

**限制**
- 必須搭配風控與 Regime

---

## 10. 跨市場與相對價值策略（Intermarket / RV）

**核心假設**
- 不同市場間存在結構關係

**例子**
- 指數 vs 期貨
- 類股輪動
- 股債關係

📌 僅 Observe-only，不可直轉訊號。

---

## 11. 防禦與保護型策略（Defensive）

**核心假設**
- 在高風險時降低損失

**例子**
- 停利停損邏輯
- 風險縮減
- 現金比重調整

📌 **此類策略優先於進攻策略。**

---

## 12. 策略與 Regime 對應原則

- 每一策略：
  - 必須標註可用 Regime
  - 必須標註禁用 Regime
- Regime 不相容：
  - 策略自動停用（非失效）

---

## 13. 與其他文件的關係

- 受制於：
  - MASTER_ARCH
  - MASTER_CANON
  - ARCH_FLOW
  - Risk_and_Compliance
- 被引用於：
  - Strategy_Feature_Index
  - Evidence Bundle 規範

---

## 14. 擴充與版本治理

- 可新增策略類型
- 不可刪除既有分類
- 新增需：
  - 定義假設
  - 定義 Regime 適用性
  - 更新 Document_Index

---

## 15. 終極策略宣告

> **TAITS 不缺策略，  
缺的是「知道什麼時候不該用策略」。**

---

（End of STRATEGY_UNIVERSE）
