# 📘 TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219

Deployment, Operations & Daily Governance Specification

doc_key：DEPLOY_OPS
治理等級：B（Deployment & Operations Governance｜執行前置治理，不具策略與裁決權）
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）
版本狀態：ACTIVE（部署與營運層最大完備版，僅允許 Only-Add）
版本日期：2025-12-19
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX
平行參照：ARCH_FLOW / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / VERSION_AUDIT / LOCAL_ENV
變更原則：Only-Add（只可新增，不可刪減／覆寫／弱化治理邊界）

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

（DEPLOY_OPS｜最大完備版 v2025-12-19 完）
