# TAITS_Local_Execution_Environment.md
（TAITS 本地落地環境規格｜API/Python 主軸｜可回放｜可測試｜可部署）

> 文件定位：落地環境規格（Implementation Support）
> 目的：讓 TAITS 可以在你的電腦「真的跑起來」，而且可回放、可測試、可擴充。
> 注意：本檔描述「如何落地跑」，不改寫母體邏輯。

---

## 0. 最高原則（避免走歪）

1) 以 Python + API 為主，不依賴 XQ  
2) 先跑通「只建議（Advisory Only）」再談自動下單  
3) 必須能做 Snapshot 與 Replay（可回放）  
4) 沒有審計（Audit）就不算 TAITS  
5) 任何時間資料不足 → 系統必須能降級（Observe-only / R10）

---

## 1. 建議本地目錄結構（可直接照建）

```text
TAITS_RUNTIME/
├── config/
│   ├── datasources.yaml
│   ├── regimes.yaml
│   ├── governance.yaml
│   ├── risk.yaml
│   └── runtime.yaml
│
├── data/
│   ├── raw/                  # 原始來源保存
│   ├── normalized/           # 標準化後
│   ├── snapshots/            # 快照（回放用）
│   └── audit/                # 審計紀錄（決策/事件）
│
├── logs/
├── reports/
└── services/
    ├── collector/            # 資料收集服務
    ├── feature_factory/      # 指標/特徵工廠
    ├── regime_engine/        # Regime 判定
    ├── strategy_engine/      # 策略訊號（不下單）
    ├── fusion_engine/        # 融合與權重
    ├── governance_gate/      # 策略治理閘門
    ├── risk_gate/            # 風控合規閘門
    ├── decision_api/         # 對外輸出（UI/報告）
    └── audit_replay/         # 回放工具
2. 本地執行模式（由你決定）
2.1 Advisory Only（只建議，預設）
不送單

輸出：

Regime

策略訊號集合

治理結果

風控結果

候選池與權重建議

報告（Report）

2.2 Semi-Auto（半自動）
會產生 Execution Plan（下單計畫）

但「是否送單」由你按確認

2.3 Auto（全自動）
需最高授權

必須啟用 KillSwitch、全程 Audit、風控上限

3. Snapshot（快照）與 Replay（回放）規格
3.1 Snapshot 必須包含
timestamp（時間戳）

source_manifest（來源清單：哪個 API、哪個端點、哪個 query）

raw_data_hash（原始資料雜湊）

normalized_data（標準化後資料）

feature_vector

derivatives_observation（期貨/選擇權：僅觀察）

credit_observation（融資融券：僅觀察）

data_quality（缺值/延遲/異常）

run_id、system_version

3.2 Replay 的最低能力
指定 snapshot_id → 重跑 Regime/策略/治理/風控

產出結果必須一致（除非版本變更；需記錄差異）

4. 測試（Testing）最低要求（落地必備）
4.1 單元測試（Unit）
Feature 計算正確性（尤其 GMMA/CBL/威科夫/鮑迪克的特徵輸出）

Regime Engine 在固定快照輸出一致

Governance / Risk Gate 規則可預期

4.2 整合測試（Integration）
資料源斷線 → 降級是否生效

延遲上升 → 是否禁追價策略

事件旗標觸發 → 是否進入 SOFT/HARD/KILL

4.3 回放測試（Replay）
任一歷史 snapshot 可完整重建當時輸出

5. 監控與告警（本地也要有）
必監控：

資料源健康（UP/DOWN/DEGRADED）

延遲（latency）

異常跳價/量暴衝（anomaly）

Gate 結果分佈（是否常被擋）

風控觸發原因統計

6. 安全與權限（本地也要防呆）
config 需版本化

API key 不可寫死在程式碼（放 .env / secrets）

Auto 模式必須有「雙重確認」與 KillSwitch

7. 完成宣告（本檔做到什麼）
本檔定義：

TAITS 在本地落地的最小可行環境（不依賴 XQ）

Snapshot/Replay/Audit 的硬要求

三種運作模式（由你決定是否送單）

yaml
複製程式碼

---

## ✅ 11/12 — `TAITS_Beginner_Teaching_Rules.md`（請整份覆蓋貼上）

```md
# TAITS_Beginner_Teaching_Rules.md
（TAITS 新手協作規則｜你不寫程式也能推進｜避免 AI 偷工與亂改）

> 文件定位：新手協作規範（你已明確說你是小白、你只負責貼上）
> 目的：讓你不需要懂程式，也能把 TAITS 推到可落地。
> 本規範同時約束 AI：不得縮水、不得亂改、不得通靈。

---

## 0. 角色分工（強制）

你（使用者）：
- 不寫程式、不 debug
- 只做：複製貼上、建立檔案、上傳 GitHub、回覆「下一批」

我（AI）：
- 必須提供可直接貼上的完整內容
- 不給 diff、不給片段、不要求你補齊
- 資料太長要分批，但「不能少」

---

## 1. 你要 AI 的輸出格式（固定）

每次你說「開始給我/下一批」我必須：
- 清楚標註：第幾批、第幾份檔案（例如 05/12）
- 提供：整份 md 內容（可直接覆蓋貼上）
- 不可用「……」省略
- 不可把關鍵內容改成抽象描述

---

## 2. 你如何驗收（不懂技術也能驗）

你只要檢查四件事：

1) 檔名是否正確（你看得懂）
2) 內容是否「完整有層級」（不是摘要）
3) 是否有把你的要求寫進去：
   - Regime-first
   - Risk/Governance 可否決
   - 期貨/選擇權/融資融券只觀察
   - 消息面不能消失
   - 題材輪動與中小型股不能被嚴苛篩掉
4) 是否能被新對話讀懂（不用靠記憶）

---

## 3. 你推進專案的正確順序（最穩）

### Step 1｜先把 12 份檔案全部「定稿」進 GitHub
- 你現在正在做的事情就是這個

### Step 2｜再建立 00–12 中文母體檔案（新體系）
- 這會是第二輪，從你現有 12 份檔案萃取成正式母體

### Step 3｜最後才進入 13+ 實作（API 服務/回放/部署）
- 先跑 Advisory Only（只建議）

---

## 4. 常見錯誤與糾正（你遇到就照做）

- AI 把 10 層改成 5 層：→ 直接判定不合格，要求「只能新增備註，不可縮水」
- AI 說資料太大不能列：→ 允許分批，但不能少、不能用省略號
- AI 沒寫資料來源網址：→ 不合格，資料檔必須可追溯
- AI 把觀察型產品寫成可下單：→ 違反憲章，直接要求重寫

---

## 5. 你要我切換「嚴格對齊模式」時代表什麼

當你說「嚴格對齊模式」：
- 我必須只依你已確立的 TAITS 憲章與檔案體系輸出
- 不做未經授權的改名/縮減/替換
- 不把未知內容當已存在（不通靈）
- 任何需要擴充的內容只能「新增」或「附錄」

---

## 6. 完成宣告

本文件確立：
- 你能用「只貼上」把 TAITS 推進到可落地
- AI 不得偷工減料或縮水
