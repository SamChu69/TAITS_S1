# TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219
doc_key：DEPLOY_OPS  
治理等級：C（Deployment / Operations / Runbook｜營運級治理規範）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（營運規範，可隨系統擴充 Only-Add）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / MASTER_CANON / DOCUMENT_INDEX  
平行參照：FULL_ARCH / ARCH_FLOW / VERSION_AUDIT / LOCAL_ENV / RISK_COMPLIANCE / EXECUTION_CONTROL / UI_SPEC / DATA_UNIVERSE / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化：回滾能力、急停能力、稽核可回放、金鑰隔離、責任可追溯）  
核心鐵律：可回滾、可停機、可稽核、可回放、可追責（缺一不可上線）

---

## 0. 文件定位（Deployment & Operations Charter）

本文件定義 TAITS 的部署、營運與日常運作（Ops）最高規範，用於回答：

- 如何將 TAITS 從本地/研究模式逐步推進到 Paper / Live，且**不破壞治理**
- 如何確保部署與上線過程遵守：
  - Only-Add
  - 版本可追溯（Active Version Map）
  - 稽核可回放（Replay Bundle）
  - Human-in-the-Loop（UI 裁決仍是唯一入口）
  - Risk/Compliance 最高否決權
- 如何落地 Runbook（操作手冊）與 Incident（事件處置），確保可停機、可回滾、可保全證據

📌 本文件不負責（避免越權）
- 不改寫交易制度內容（→ TWSE_RULES + 官方來源裁決）
- 不改寫風控否決條文（→ RISK_COMPLIANCE）
- 不改寫執行安全細節（→ EXECUTION_CONTROL）
- 不改寫版本稽核母帳本（→ VERSION_AUDIT）
- 專注於：部署與營運如何「不讓治理破功」

---

## 1. 官方參考入口（Official References｜部署/營運依據）

> 本節提供可核對之官方文件入口（不取代 TAITS 母法裁決）。

- Git 官方文件（Git Documentation）  
  https://git-scm.com/doc
- GitHub Docs（分支保護 / PR / Actions / 環境）  
  https://docs.github.com/
- Docker 官方文件（Containers）  
  https://docs.docker.com/
- Kubernetes 官方文件（若採 K8s）  
  https://kubernetes.io/docs/
- OWASP Top 10（應用安全基準）  
  https://owasp.org/www-project-top-ten/
- NIST Cybersecurity Framework（營運安全框架）  
  https://www.nist.gov/cyberframework
- TWSE 規章（Regulations）  
  https://twse-regulation.twse.com.tw/
- TAIFEX 規章（Rules & Regulations）  
  https://www.taifex.com.tw/enl/eng6/ruleRegulation

---

## 2. 部署與營運的四大硬性目標（Hard Objectives）

1) **可回滾（Rollbackable）**  
   任一上線必須可回到上一個可用版本（透過切換 Active Version Map，而非覆寫）。

2) **可停機（Stoppable）**  
   任一異常必須能立即停止執行（Kill Switch / Safe Mode），並阻斷新單。

3) **可稽核（Auditable）**  
   任一部署、切換、設定變更必須產生不可變更審計物（Append-only）。

4) **可回放（Replayable）**  
   任一重要事件（尤其 Live/Paper）必須保留回放所需資料引用與版本映射。

---

## 3. 環境分級（Environments）與治理強度

TAITS 環境至少分為五類（可新增不可縮減）：

- **Research**：研究（本地或共享環境）
- **Backtest**：回測（可離線，但仍需版本映射）
- **Simulation**：模擬（語義上遵守 Gate）
- **Paper**：仿真下單（與 Live 同級治理，僅通道不同）
- **Live**：實盤

### 3.1 不變項（所有環境必須同樣遵守）
- Active Version Map 必須存在（缺＝阻斷）
- 稽核與回放輸出不可省略（缺＝未發生）
- Risk/Compliance 的二元裁決語義不可被模糊化
- UI 人類裁決入口不可被繞過

### 3.2 允許差異（僅三類差異）
- 資料來源（歷史/即時）
- 時間推進方式（模擬/真實）
- 交易通道（模擬/真實券商）

---

## 4. 部署拓樸（Deployment Topologies｜Only-Add）

> FULL_ARCH 定義模組域；此處定義營運上可採的佈署型態與隔離原則。

### 4.1 單機拓樸（Local）
- 適用：Research/Backtest/Simulation
- 要求：
  - 稽核物仍需落盤（不可只在記憶體）
  - 金鑰隔離（即便本地也不得入 repo）
  - 若啟用 Paper/Live 通道，必須轉為 Live 級治理

### 4.2 分層服務拓樸（Service-based）
- 適用：Paper/Live
- 必要隔離：
  - Execution（L11）與 Secrets/Keys 最高隔離
  - Risk/Compliance（L7）高可用與不可變更審計
  - Version Ledger / Immutable Store（稽核儲存）必須可靠

### 4.3 高可用拓樸（HA）
- 允許：多副本、跨區、故障轉移
- 硬性要求：
  - 不得破壞去重/冪等（idempotency）
  - 不得破壞稽核不可變更
  - 不得破壞 Kill Switch 可用性

---

## 5. 上線門檻（Release Gates｜不可跳過）

任何版本要進入 Paper/Live，必須全部通過：

### 5.1 文件與版本門檻（VERSION_AUDIT Gate）
- [ ] `DOCUMENT_INDEX` 中 doc_key 狀態一致（ACTIVE 唯一）
- [ ] Active Version Map 產生成功（docs/policy/model/config/code）
- [ ] Change Ledger（Only-Add 變更帳本）已追加事件
- [ ] 回放所需 artifact 類型已就緒（Replay Bundle Schema 可用）

### 5.2 風控合規門檻（RISK_COMPLIANCE Gate）
- [ ] Policy 版本可追溯（policy_version 可定位）
- [ ] 規則快照（rulebook_snapshot_ref）可回放
- [ ] Veto Reason Codes 映射完整（UI/Log 可呈現）

### 5.3 執行安全門檻（EXECUTION_CONTROL Gate）
- [ ] Kill Switch Preflight 成功（可觸發/可回報/可稽核）
- [ ] Channel Health Check 成功
- [ ] Idempotency / De-dup Guard 啟用
- [ ] Pre/In/Post Execution Logs 不可變更寫入可用
- [ ] Reconciliation（對帳）流程可用

### 5.4 UI 與人類主權門檻（UI_SPEC Gate）
- [ ] APPROVE 必須兩段式確認
- [ ] VETO/RETURN 狀態 APPROVE 必須禁用
- [ ] UI Trace 不可變更寫入可用
- [ ] UI 能顯示版本映射與原因碼

---

## 6. 部署流程（Deployment Pipeline｜最大完備）

> 你不需要固定工具（GitHub Actions、Jenkins、GitLab CI 都可），  
> 但流程語義必須一致且可稽核。

### 6.1 Pipeline 階段（不得省略語義）
1) **Build**：產生可部署產物（artifact）
2) **Test**：單元/整合/合規語義測試（含 Gate 測試）
3) **Package**：封裝（container/image）
4) **Sign/Hash**：產物簽章或 hash（不可抵賴）
5) **Deploy**：佈署到目標環境
6) **Verify**：健康檢查 + Gate 驗證（含 Kill Switch Preflight）
7) **Activate**：切換 Active Version Map（Only-Add）
8) **Monitor**：監控與告警上線
9) **Audit Record**：把部署事件寫入不可變更稽核儲存

### 6.2 部署事件（Deployment Event）必備欄位
- `deploy_event_id`
- `environment`（Research/Backtest/Simulation/Paper/Live）
- `artifact_ref`（build 產物引用）
- `code_commit_ref`
- `active_version_map_ref`（切換前/後）
- `operator_id`
- `timestamp`
- `result`（SUCCESS/FAIL/ROLLED_BACK）
- `reason_codes[]`（FAIL/ROLLBACK 必填）
- `hash_manifest_ref`
- `runbook_ref`（採用哪個 Runbook）

---

## 7. 設定管理（Config Management）與變更控制

### 7.1 設定分類
- **可進 repo 的設定**（非敏感）：例如欄位映射、模組啟用旗標、非機密的資料源端點
- **不可進 repo 的設定**（敏感）：API keys、token、私鑰、券商憑證、個資

### 7.2 變更控制原則
- 任何配置變更視同版本變更：
  - 必須產生 `config_version`
  - 必須記錄 Change Ledger（Only-Add）
  - 必須綁定 Active Version Map
- 禁止「直接改線上設定檔不留痕」

---

## 8. 金鑰與敏感資訊治理（Secrets & Keys Governance｜硬門檻）

> 本節與 LOCAL_ENV 相互約束；此處定義營運層面的強制規則。

### 8.1 硬性禁止
- 金鑰/密碼/券商憑證進 repo
- 金鑰寫入 log、UI、錯誤訊息
- 用共享帳號操作 Live

### 8.2 必須做到
- Secrets 必須由 KMS/Secrets Manager/安全儲存管理
- 最小權限（Least Privilege）
- 金鑰輪替（Rotation）：
  - 有計畫、可稽核、可回滾
- Secrets 使用必須可追溯：
  - `who/when/for correlation_id/for what action`

---

## 9. 監控與告警（Monitoring & Alerting｜最大完備）

### 9.1 必監控指標（最小集合）
- 系統健康：
  - CPU/Mem/Disk/Network
  - 服務存活與延遲
- 資料品質：
  - ingestion 失敗率、延遲、缺漏比例
- Gate 狀態：
  - Risk PASS/VETO 比率與 reason codes 分佈
  - Governance RETURN 缺口類型
- 執行安全：
  - Order 提交/拒單/撤單/成交事件速率
  - Channel latency
  - Idempotency hit（去重觸發次數）
  - Reconciliation 不一致事件
- 急停/熔斷：
  - Kill Switch 觸發次數與原因
  - Circuit Breaker 觸發次數與原因

### 9.2 告警分級（必須）
- **P0（立即停機）**：疑似重複下單、對帳不一致、Kill Switch 不可用、token 驗證失敗仍嘗試送單
- **P1（立即處置）**：通道不健康、連續拒單、資料 provenance 斷裂
- **P2（需追蹤）**：資料延遲、feature 品質下降、Evidence completeness 下降

---

## 10. 事件處置（Incident Response｜Runbook 必備）

### 10.1 事件分類（最小集合）
- `INC-EXE`：執行層事件（重複/錯單/拒單/對帳）
- `INC-RISK`：風控/合規事件（規則快照失效、reason code 激增）
- `INC-DATA`：資料事件（延遲、缺漏、provenance 斷裂）
- `INC-UI`：介面事件（APPROVE 被誤啟用、trace 失效）
- `INC-SEC`：安全事件（疑似金鑰外洩/權限異常）
- `INC-OPS`：部署事件（上線失敗、回滾）

### 10.2 P0 標準處置序列（硬性）
1) 觸發 Kill Switch（或確認已觸發）
2) 阻斷新單（Execution Safe Mode）
3) 保全證據（鎖定稽核物、快照、log）
4) 對帳（reconciliation）並記錄結果
5) 通知 UI 顯示狀態與原因碼（不可靜默）
6) 依 Runbook 決定回滾或修復
7) 追加 Incident Report 到不可變更儲存（Only-Add）

---

## 11. 回滾（Rollback）與停機（Stop-the-Line）機制

### 11.1 回滾定義（嚴格）
- 回滾不是覆寫，而是：
  - 切回上一個 Active Version Map（並記錄 Rollback Event）
- 回滾必須可稽核、可回放

### 11.2 Stop-the-Line（停線）條件（最小集合）
- Kill Switch 不可用（EXE-KILL-01）
- Token 驗證鏈失效（SYS-VERIFY）
- 對帳不一致（EXE-RECON-FAIL）
- 稽核不可寫入（SYS-AUDIT）
- Provenance 斷裂（SYS-PROV）

---

## 12. 營運日常作業（Daily Ops Checklist｜最大完備）

> 以下清單建議每天/每次啟動 Paper/Live 前執行（可自動化，但不得省略稽核）。

### 12.1 開盤前（Pre-Session）
- [ ] 交易日曆與時段狀態正確（TWSE/TAIFEX）
- [ ] Data sources 健康檢查（官方優先 + fallback）
- [ ] 規則快照可載入（rulebook_snapshot_ref）
- [ ] Risk policy 版本可定位（policy_version）
- [ ] Active Version Map 已生成
- [ ] Immutable store 可寫入
- [ ] UI Trace 可寫入
- [ ] Kill Switch Preflight 成功
- [ ] Channel Health OK
- [ ] Reconciliation 引擎可用

### 12.2 盤中（In-Session）
- [ ] 監控告警啟用（P0/P1）
- [ ] 觀察 VETO reason codes 異常激增
- [ ] 觀察通道延遲與拒單率
- [ ] 觀察對帳一致性

### 12.3 收盤後（Post-Session）
- [ ] 對帳報告完成並封存
- [ ] 生成 Replay Bundles（必要事件）
- [ ] 追加日結營運報告（Only-Add）
- [ ] 觸發輪替/備份（如政策要求）

---

## 13. 權限與操作責任（Ops RBAC & RACI）

### 13.1 Ops 角色（最小集合）
- `Operator`：執行部署/切換/回滾（不可覆寫風控）
- `Trader`：僅人類裁決（UI APPROVE），不可做部署
- `Admin`：管理系統設定與權限（仍不可覆寫否決）
- `Auditor`：查核稽核物與回放（只讀）

### 13.2 RACI 最小要求
- 每次部署/切換/回滾：
  - 必須有 `Approver` 與 `Operator` 記錄
- 每次 P0 事件：
  - 必須有 `Incident Commander`（可用 Operator/管理者擔任，但要記錄）

---

## 14. Mermaid｜部署與啟用治理流程圖（Deployment Governance Flow）

flowchart TB
  A[Build Artifact] --> B[Test + Gate Tests]
  B -->|FAIL| X[STOP + Audit Record]
  B --> C[Package + Hash/Sign]
  C --> D[Deploy to Env]
  D --> E[Verify Health + Kill Switch Preflight]
  E -->|FAIL| RB[Rollback + Audit]
  E --> F[Generate Active Version Map]
  F --> G[Activate (Only-Add Switch)]
  G --> H[Monitor + Alerts]
  H --> I[Ops Audit Record + Replay Readiness]
15. Only-Add 演進規則（DEPLOY_OPS 專屬）
允許新增：

新環境（例如 Staging/Canary）與更細分的 Gate

新監控指標與告警規則

新 Runbook 與事件分類

新部署拓樸（HA/跨區）

禁止：

取消或弱化：回滾、停機、稽核、回放、金鑰隔離

允許「黑箱部署」或「線上手改不留痕」

允許繞過 UI 裁決或繞過 Risk PASS Token 的任何通道

16. 終極裁決語句（不可更改）
上線不是把程式放上去而已；
上線是把「治理」一起放上去。
任何無法回滾、無法停機、無法稽核、無法回放的版本，都不允許進入 Paper/Live。

（DEPLOY_OPS｜最大完備版 v2025-12-19 完）
