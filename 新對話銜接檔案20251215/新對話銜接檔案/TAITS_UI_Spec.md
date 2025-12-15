# TAITS_UI_Spec.md
（TAITS UI 規格｜API-first｜Decision/Audit-first｜不污染母體｜可交接）

> 文件定位：介面規格（實作層輔助文件）
> 原則：UI 不做決策，UI 只呈現決策與允許你下指令（由你決定是否下單）。

---

## 0. UI 設計總原則（不可違反）

1) UI 不得內嵌策略邏輯（策略邏輯只在母體/服務端）
2) UI 必須能展示 Evidence Bundle（證據包）
3) UI 必須能展示 Governance/Risk Gate 的「為什麼擋」
4) UI 必須支援三種模式切換：
   - Advisory Only（只建議）
   - Semi-Auto（你確認才送）
   - Auto（全自動，需最高授權）
5) UI 必須支援「中小型題材輪動」的觀察與候選池（避免只看權值股）

---

## 1. UI 資訊架構（IA）

### 1.1 主選單（左側）
1) 市場總覽（Market Overview）
2) Regime 狀態（Regime Dashboard）
3) 題材/輪動（Themes & Rotation）
4) 候選池（Universe / Candidates）
5) 策略訊號（Strategy Signals）
6) 治理與權限（Governance Gate）
7) 風控（Risk Gate）
8) 交易建議（Decision Output）
9) 審計回放（Audit & Replay）
10) 系統健康（Health / Data Quality）
11) 設定（Settings）

---

## 2. 每個頁面必備內容（不偷工：逐頁列）

### 2.1 市場總覽
- 指數/類股/成交額/廣度（Breadth）
- 今日事件旗標（公告/重大新聞/結算週）
- Data Quality 面板（延遲/缺失/異常）

### 2.2 Regime Dashboard
- 當前 Regime（R1–R10）
- 置信度（confidence）
- Evidence Bundle（至少 3 個核心證據）
- Regime 變化歷史（timeline）
- 若 R10：顯示「缺什麼資料」與降級原因

### 2.3 題材/輪動 Themes & Rotation
- 題材排行榜（熱度/擴散/領漲梯隊）
- 題材證據拆解：
  - 價格擴散
  - 量能擴散
  - 領漲/跟隨
  - 消息旗標（降權顯示）
- 你可手動標註「我關注題材」（形成 Watchlist，不是策略）

### 2.4 Universe / Candidates
- 兩段式：
  1) 全市場篩選（流動性/風險基本門檻）
  2) 題材/策略候選池（保留中小型爆發股）
- 每檔顯示：
  - 核心特徵摘要
  - 風險旗標
  - 所屬題材/族群

### 2.5 Strategy Signals
- 策略列表（可搜尋）
- 每策略顯示：
  - 成立/不成立
  - 強度
  - 證據
  - 適用 Regime
  - 風險提示

### 2.6 Governance Gate
- 當前策略集合的治理結果：
  - PASS / DOWNGRADE / MANUAL / BLOCK
- 顯示：
  - 哪條規則觸發
  - 需要你確認的項目（若 MANUAL）

### 2.7 Risk Gate
- PASS / SOFT_BLOCK / HARD_BLOCK / KILL_SWITCH
- 顯示：
  - 觸發的風控規則清單
  - 建議降級方式（縮倉/不追價/只出不進）

### 2.8 Decision Output（交易建議）
- 只輸出「建議」與「限制」
- 內容：
  - 候選標的（Top N）
  - 建議策略組合
  - 建議倉位（risk budget）
  - 禁止事項（例如：禁止追價、禁止隔日）
- 模式切換：
  - Advisory Only：只能匯出報告/下單計畫（不送）
  - Semi-Auto：你按下確認才送
  - Auto：需要高權限開關（預設關）

### 2.9 Audit & Replay
- 依 run_id / snapshot_id 搜尋
- 回放內容：
  - 當時看到的快照
  - 當時的 Regime
  - 當時的策略輸出
  - 當時的 Gate 結果
  - 最終建議/（若有）執行結果

### 2.10 Health / Data Quality
- 各資料源健康（UP/DOWN/DEGRADED）
- 延遲監控
- 斷線與重連紀錄
- 降級觸發紀錄

---

## 3. UI 與後端 API 契約（摘要）

UI 只呼叫三類 API：
1) Market API（市場快照）
2) Decision API（Regime/策略/治理/風控/建議）
3) Audit API（回放與審計）

> API 詳細規格在 13+（Implementation）中定義；母體不放執行細節。

---

## 4. 完成宣告

本 UI 規格確保：
- API-first、可審計、可回放
- 不污染母體（UI 不做決策）
- 能支援題材輪動與中小型爆發股的觀察與候選池
