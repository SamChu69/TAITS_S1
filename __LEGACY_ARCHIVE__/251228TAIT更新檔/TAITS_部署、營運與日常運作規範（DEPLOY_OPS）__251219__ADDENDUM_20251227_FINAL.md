---

# Addendum 2025-12-27｜Only-Add：營運/部署證據鏈最小欄位強制 × Evidence Chain 對齊 LOCAL_ENV × Index Gate 唯一裁決（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251219.md（doc_key：DEPLOY_OPS）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：AI_GOV（A+）＋DOCUMENT_INDEX（A+｜Authoritative Index）＋MASTER_ARCH（A）＋MASTER_CANON（A）  
> 平行對齊：  
> - LOCAL_ENV｜Addendum 2025-12-27（Evidence Chain Template）  
> - UI_SPEC｜Addendum 2025-12-27（UI Trace 引用最小欄位）  
> - PROJECT_PROMPT｜Addendum 2025-12-27（Index Gate First／ACTIVE 不固化／引用最小格式）  
> - VERSION_AUDIT｜Addendum 2025-12-27（METADATA_FIX Ledger 批次補登）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（建議新增條目：`VA-METADATA_FIX-20251227-0012`）  
> 目的：在不改寫既有部署/營運流程與責任分工的前提下，補強「營運與部署產物」的可回放、可稽核最低欄位；將 Evidence Chain 輸出格式對齊 LOCAL_ENV；並固定 ACTIVE/doc_key/治理等級之唯一裁決來源為 DOCUMENT_INDEX，避免營運現場因快照清單/固定文件數量而誤用治理法源。

---

## D0. 適用範圍（Hard Boundary）

本 Addendum 僅補強：
1) 部署/營運產物（Release Note、Runbook、Incident、Log、回放包）之最小引用欄位  
2) Evidence Chain 格式對齊 LOCAL_ENV（不改流程，只固定輸出格式）  
3) Index Gate 唯一裁決來源（ACTIVE/doc_key/等級不由營運自行裁決）  
4) 裁決順序字串助記化定位（Mnemonic ≠ Override Rule）

本 Addendum **不**：
- 不修改既有部署架構、環境策略、SOP 流程、權限模型  
- 不修改 Canonical Flow（L1–L11）  
- 不新增新治理層級  
- 不弱化 Risk/Compliance 否決權（若有張力，回到上位裁決與既有條款）

---

## D1. Index Gate 唯一裁決（營運不得自行裁決 ACTIVE/doc_key）

凡部署/營運流程涉及「依據文件」之裁決（例如：是否可上線、是否符合規範、是否可啟動某模組）：

- ACTIVE 文件集合、doc_key 合法性、治理等級 bucket、版本有效性  
  **一律以 DOCUMENT_INDEX 的 Authoritative Index 表格裁決為準**。  
- Runbook / Release Note / Incident 文檔中的「文件清單、文件數量、快捷載入集合」  
  一律視為 Snapshot（導覽用途），不得作為治理裁決依據。

---

## D2. 部署/營運產物最小引用欄位（Minimum Legal Citation Fields）

### D2.1 強制欄位（缺一視為未引用）
凡部署/營運產物中出現「依據某文件」或「符合某規範」之描述，必須至少包含：

- `ref_file`：完整檔名  
- `ref_doc_key`：doc_key  
- `ref_version_date`：版本日期（YYYY-MM-DD 或 __yymmdd）  
- `ref_section`：章節定位（heading path / §x.y）  
- `audit_anchor`：對應 VERSION_AUDIT 的稽核錨點（可先以本批次 `VA-METADATA_FIX-20251227-0012`）

缺任一欄位 → 一律視為「未引用」→ 不得作為上線/裁決依據；需要裁決時必須 STOP/RETURN 以補齊引用資訊。

### D2.2 建議固定引用標頭（可直接貼用）
```text
〔TAITS Deploy/Ops 引用標頭｜Freeze v1.0｜Only-Add〕
artifact_id = <release_id / incident_id / run_id>
ref_file = <完整檔名>
ref_doc_key = <DOC_KEY>
ref_version_date = <YYYY-MM-DD / __yymmdd>
ref_section = <章節/段落路徑>
ref_notes = <可選：本次用途>
audit_anchor = VERSION_AUDIT:VA-METADATA_FIX-20251227-0012
index_gate = DOCUMENT_INDEX（Authoritative Index）裁決為準
〔/TAITS Deploy/Ops 引用標頭〕
```

---

## D3. Evidence Chain 對齊 LOCAL_ENV（不改流程，只固定輸出格式）

為確保部署/營運產物可回放、可重現、可稽核，本文件後續所有「上線證據/回放包/事故復盤包」的輸出，必須至少包含下列結構（欄位可多不可少）：

### D3.1 環境指紋（Environment Fingerprint）
```text
env_fingerprint:
  os: <例如 Ubuntu 22.04>
  cpu: <型號/核心數>
  ram_gb: <數值>
  gpu: <可選>
  runtime: <例如 python 3.11 / node 20>
  package_manager: <pip/conda/uv/npm>
  repo_commit: <git hash>
  local_env_doc_ref:
    doc_key: LOCAL_ENV
    ref_section: <章節定位>
```

### D3.2 依賴清單（Dependency Manifest）
```text
dependency_manifest:
  lockfile: <requirements.txt / poetry.lock / uv.lock / package-lock.json 等>
  hash: <sha256 可選>
  generated_at: <ISO-8601>
```

### D3.3 執行證據（Run Evidence）
```text
run_evidence:
  command: <實際執行命令>
  start_time: <ISO-8601>
  end_time: <ISO-8601>
  outputs:
    - path: <產物路徑>
      hash: <sha256 可選>
  logs:
    - path: <log 路徑>
      hash: <sha256 可選>
```

### D3.4 失敗與回復（Failure/Recovery）
```text
failure_recovery:
  status: <PASS/FAIL>
  error_summary: <如 FAIL，摘要>
  recovery_action: <回滾/修復行動>
  notes: <可選>
```

---

## D4. 裁決順序字串之法律定位（Mnemonic ≠ Override Rule）

本文件內若出現任何「裁決順序字串」或箭頭序列（例如：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`）：
- 一律視為閱讀/操作助記（Mnemonic）  
- 不得被用作覆蓋規則或裁決權重新分配  
- 若與 DOCUMENT_INDEX §3（覆蓋規則）或 §6（衝突裁決程序）產生張力：一律回到 DOCUMENT_INDEX（不可跳步）

---

## D5. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫任何既有部署/營運流程。  
- 部署/營運產物的引用合法性必須滿足 D2 最小欄位；Evidence Chain 至少包含 D3 結構。  
- 缺少必要欄位時：依 DOCUMENT_INDEX §6 保守處置，並以 VERSION_AUDIT 留痕。

（Addendum 2025-12-27｜Only-Add｜Freeze v1.0 完）

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
