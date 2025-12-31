<!--
TAITS｜ACTIVE UPDATED（單檔內嵌更新版）
產出日期：2025-12-29（Asia/Taipei）
更新規格：單檔內嵌；可更新處直接更新並避免重複；不可更新處以 Appendix 內嵌 Only-Add 全文。
來源檔：TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219__ADDENDUM_20251228_FINAL.md
-->

---

# 📘 TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219

Deployment, Operations & Daily Governance Specification

doc_key：DEPLOY_OPS
治理等級：B（Deployment & Operations Governance｜執行前置治理，不具策略與裁決權）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（部署與營運層最大完備版，僅允許 Only-Add）
版本日期：2026-01-01
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX
平行參照：ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / LOCAL_ENV
變更原則：Only-Add（只可新增，不可刪減／覆寫／弱化治理邊界）

## L9–L11 最終語義定錨（單一正確版｜必須一致）

> 本節為 TAITS 在 L9／L10／L11 的**唯一正確語義**。  
> 任何文件中若出現與本節不一致之描述，視為舊錯口徑（不得保留於單一正確版）。

### L9｜投資報告（Investment Report｜可追蹤、可更新、可稽核）
L9 的產出定位為「**給人看的完整投資報告**」，不是一次性的口頭解說；必須可在後續事件/行情變動下持續更新並可追溯。
L9 最低交付物應包含（不限於）：
- **標的化**：標的識別、觀測起點、追蹤狀態（open/hold/watch/exit-candidate 等）、版本號與時間戳。
- **數據**：對應 L1–L8 的關鍵數據表（消息/基本/技術/籌碼/風險/制度），含來源、取樣時間、缺漏註記。
- **圖形**：至少包含價格走勢與關鍵技術指標狀態視覺化（例如均線、RSI、MACD；以「狀態」呈現，非主觀敘事）。
- **進出場建議（非下單）**：建議區間/觸發條件/失效條件（停損/停利/風險撤退），並明確標示「此為建議，不構成下單」。
- **情境更新（Regime/Event）**：當市場制度/事件/風險狀態改變，需能產生增量更新（delta）並保留回放鏈。
- **可稽核鏈**：引用到 L11 的 record_id / ledger_id（或等價識別），以確保報告可被回放與驗證。

### L10｜人類裁決與交易授權（Human Decision & Authorization｜唯一決策點）
L10 的定位為「**人類最高決策者的最終裁決介面與授權層**」。  
- **最終決策者永遠是人類**：你決定採取何種模式與是否授權交易。
- L10 可裁決/授權的動作包含（不限於）：**不動作／回測／模擬／半自動／全自動**。
- AI/Agent 在 L10 僅能提供「選項、理由、風險揭露與建議」，**不得自行構成下單行為**；下單/執行屬於 L10 授權後由執行控制規範承接。

### L11｜工程稽核與全層回放（Engineering Audit & Replay｜全層留痕）
L11 的定位為「**工程檢視與稽核回放層**」，不是下單層，也不是只記錄 L10。
- **全層留痕**：L11 必須覆蓋 L1–L11 每一層的關鍵輸入/輸出/裁決/否決/變更理由與時間戳。
- **雙料輸出**：同一筆紀錄需同時具備  
  1) 人話可讀（你能看懂，用於檢視系統是否合理）  
  2) 工程可用（可重現、可驗證、可追溯，用於開發/稽核/回放）
- **目的**：用來檢查每一層的功能是否合理、是否需要調整、以及自動/半自動/全自動在不同時點的決策依據是否一致可回放。


0. 文件定位（Deployment & Operations Charter）

本文件為 TAITS 在「可運行狀態」下的部署與日常營運治理母文件，
其存在目的僅有一個：

確保系統「可以被安全地啟動、持續運行、即時中止、完整追責」。

本文件負責

定義 系統上線前必須通過的部署與營運治理條件

定義 環境切換、版本啟用、凍結、回滾與停線流程

定義 日常營運、異常事件、事故處理的標準治理語義

本文件不負責（避免越權）

不定義策略與交易邏輯（→ STRATEGY_UNIVERSE）

不定義風控否決條文（→ RISK_COMPLIANCE）

不定義下單與執行細節（→ EXECUTION_CONTROL）

不定義 UI 行為與互動（→ UI_SPEC）

不裁決文件位階與衝突（→ DOCUMENT_INDEX）

1. 環境治理分級（Environment Governance）
1.1 官方環境類型（不可自行新增語義）
環境	定位	是否允許實際下單
Research	研究／設計	否
Backtest	歷史回測	否
Simulation	即時模擬	否
Paper	擬真紙交易	否
Live	真實運行	是

📌 任何新環境僅能以 Only-Add 方式新增，不得改寫既有語義。

1.2 環境切換鐵律

環境切換 ≠ 模式切換

環境切換必須：

重新檢查版本鎖定

重新檢查風控 Gate

重新檢查 Kill Switch 可用性

2. 上線前治理門檻（Pre-Deployment Gates）
2.1 進入 Live / Paper 的必要條件（缺一不可）

DOCUMENT_INDEX 可用且未被 Freeze

MASTER_ARCH / MASTER_CANON 版本鎖定

ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL 版本一致

VERSION_AUDIT 已建立可回放帳本

Kill Switch 通過 Preflight 自檢

Execution Channel Health = OK

無未解決 Critical / Major Incident

📌 任一條件未滿足 → 不得啟動系統。

2.2 Preflight Check（硬性）

Preflight 必須可審計，且包含：

檔案版本快照

環境參數快照

Kill Switch 測試結果

通道健康檢查結果

3. 部署流程語義（Deployment Lifecycle）
3.1 標準部署狀態機
BUILD → VALIDATE → STAGE → ACTIVATE → MONITOR


BUILD：產出可部署單元

VALIDATE：治理與版本驗證

STAGE：非生效狀態部署

ACTIVATE：版本正式生效

MONITOR：持續監控

📌 未經 VALIDATE 不得 ACTIVATE。

3.2 啟用（Activate）限制

Activate 僅允許：

已通過治理門檻的版本

已記錄於 VERSION_AUDIT

禁止：

熱修補未留痕

臨時覆寫版本

4. 版本治理與回滾（Rollback Governance）
4.1 回滾的治理定位

回滾是 治理行為，不是技術補救

回滾必須：

明確指定目標版本

留存回滾原因與裁決依據

不破壞既有審計與回放

4.2 回滾觸發條件（示例）

Execution 不一致

Risk Gate 行為異常

嚴重系統錯誤

合規事件

5. 停線與凍結（Stop-the-Line & Freeze）
5.1 停線（Stop-the-Line）

任何 Critical 事件可觸發

停線後：

禁止新交易

保留查詢與審計

等待治理裁決

5.2 凍結（Freeze）

Freeze 期間：

禁止文件結構性變更

僅允許事故修復

Freeze 來源：

RISK_COMPLIANCE

DEPLOY_OPS

DOCUMENT_INDEX 裁決

6. 日常營運規範（Daily Operations）
6.1 每日啟動檢查（Daily Start Checklist）

系統時間同步

通道健康

Kill Switch READY

版本一致性

無未解 Incident

6.2 每日結束檢查（Daily Close Checklist）

對帳完成

審計物寫入完成

異常事件歸檔

狀態快照封存

7. 事件與事故治理（Incident Governance）
7.1 Incident 分級
等級	定義
P0	立即威脅系統／資產
P1	嚴重功能失效
P2	可運行但異常
P3	觀測與改善項
7.2 Incident 必備欄位

incident_id

發生時間

影響範圍

當下版本

採取動作

是否觸發停線 / 凍結

8. Secrets / Key 與敏感設定治理

金鑰不得硬寫於程式碼

必須具備：

權限分級

定期輪替

存取審計

洩漏風險 → 視為 Critical Incident

9. 與其他文件的邊界對齊
文件	DEPLOY_OPS 關係
MASTER_ARCH	服從
MASTER_CANON	服從
ARCH_FLOW	對齊
RISK_COMPLIANCE	觸發與回應
EXECUTION_CONTROL	啟用與停用
UI_SPEC	呈現狀態
VERSION_AUDIT	版本帳本
10. 演進規則（Only-Add）

允許新增：

新環境類型

新 Incident 類型

新 Runbook

禁止：

改寫既有環境語義

弱化上線門檻

省略治理檢查

最終治理宣告（不可改寫）

系統能否運作，
不取決於它有多聰明，
而取決於它是否能被隨時安全地停下來。

（DEPLOY_OPS｜最大完備版 v2026-01-01 完）

---