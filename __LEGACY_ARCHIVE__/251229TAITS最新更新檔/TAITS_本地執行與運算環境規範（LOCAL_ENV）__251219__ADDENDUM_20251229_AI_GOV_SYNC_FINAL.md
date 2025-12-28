# TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219
doc_key：LOCAL_ENV  
治理等級：C（Local Execution & Compute Environment｜環境治理與敏感隔離）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（環境規範可 Only-Add 擴充）  
版本日期：2025-12-19  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / DOCUMENT_INDEX / VERSION_AUDIT（環境亦屬可追溯治理）  
平行參照：DEPLOY_OPS / FULL_ARCH / EXECUTION_CONTROL / RISK_COMPLIANCE / UI_SPEC / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化：金鑰隔離、可回放稽核、最小權限、可回滾/可停機）  
核心鐵律：敏感不入 repo；環境可重建；版本可追溯；審計不可變更；Live/Paper 與 Research 的隔離不可被打破

---

## 0. 文件定位（Local Environment Governance Charter）

本文件定義 TAITS 的「本地執行與運算環境」治理規範，目的在於：

- 統一 TAITS 在本地（Windows / Linux / WSL / Docker 等）的環境配置原則
- 建立「可重建、可稽核、可隔離」的環境標準，避免：
  - 依賴個人電腦狀態造成不可回放
  - 金鑰/憑證/個資進入 repo 或 log
  - Research 環境誤觸 Paper/Live 通道
- 把環境納入 VERSION_AUDIT 的可追溯治理範圍（environment as versioned object）

📌 本文件不負責（避免越權）：
- 不定義部署上線流程（→ DEPLOY_OPS）
- 不定義風控否決條文（→ RISK_COMPLIANCE）
- 不定義執行細節（→ EXECUTION_CONTROL）
- 專注：本地環境如何「穩、可重建、可隔離、不洩漏、可回放」

---

## 1. 官方參考入口（Official References｜環境與安全基準）

- Python 官方文件  
  https://docs.python.org/
- pip 官方文件  
  https://pip.pypa.io/en/stable/
- Python venv 官方文件  
  https://docs.python.org/3/library/venv.html
- Conda 官方文件（若使用）  
  https://docs.conda.io/
- Docker 官方文件  
  https://docs.docker.com/
- Git 官方文件  
  https://git-scm.com/doc
- GitHub Docs（Secrets / Security / Actions 等）  
  https://docs.github.com/
- OWASP Top 10（應用安全基準）  
  https://owasp.org/www-project-top-ten/
- NIST Cybersecurity Framework  
  https://www.nist.gov/cyberframework

---

## 2. 環境治理四大硬性目標（Hard Objectives）

1) **可重建（Reproducible）**  
   同一份版本映射與環境規格，能在另一台機器重建同等運作環境。

2) **可追溯（Traceable）**  
   任一回測/模擬/裁決/執行，必須能指出使用哪一份環境版本（env_version_ref）。

3) **可隔離（Isolated）**  
   Research/Backtest/Simulation 必須能與 Paper/Live 的 Secrets/通道隔離，防止誤觸。

4) **不外洩（Non-leaking）**  
   金鑰、token、券商憑證、個資不得進 repo、不得出現在 log/UI、不得以明文散落。

---

## 3. 環境分級（Environment Tiers）與隔離規則

### 3.1 Tier 定義（至少三層，Only-Add）
- **Tier-0：Research / Backtest / Simulation（本地研究層）**
  - 可離線
  - 可使用歷史資料
  - 禁止接觸 Live Secrets
- **Tier-1：Paper（仿真交易層）**
  - 治理強度等同 Live
  - 允許使用模擬通道或券商仿真
- **Tier-2：Live（實盤層）**
  - 最嚴格隔離
  - 最小權限
  - 完整稽核與回放

### 3.2 硬性隔離規則（Hard Isolation Rules）
- Tier-0：
  - 禁止存放 Live/Paper 的任何金鑰
  - 禁止設定任何「可下真單」端點
- Tier-1/2：
  - 必須使用 Secrets Manager / OS 安全儲存 / KMS（由 DEPLOY_OPS 定義）
  - 必須啟用 EXECUTION_CONTROL 的 Kill Switch Preflight 與 Token 驗證鏈
  - 必須可寫入不可變更審計儲存（Immutable Store）

---

## 4. 目錄與檔案治理（Repo Layout & Governance）

> 原則：**能進 repo 的只有「非敏感、可版本化、可重建」的東西。**

### 4.1 可進 repo（Allowed in Repo）
- `requirements.txt` / `pyproject.toml` / `poetry.lock`（擇一體系，不得混亂）
- `env.example`（僅示例鍵名，不含值）
- `config/`（非敏感設定）
- `schemas/`（Contract / Artifact schema）
- `docs/`（doc_key 文件）
- `scripts/`（不含密鑰、不含硬編碼券商憑證）

### 4.2 禁止進 repo（Forbidden in Repo｜硬禁）
- `.env`（含任何秘密值）
- `*.key` / `*.pem` / 憑證檔（除非是公開測試憑證且不具任何權限）
- `secrets.json` / `token.txt` / `passwords.*`
- 券商 API key / refresh token / session token
- 任何個資、帳戶資訊、下單紀錄原始回報（若含敏感，需脫敏或只存引用）

### 4.3 `.gitignore` 硬性清單（必須納入）
- `.env`
- `*.log`
- `data/`（若含原始資料，改用引用或分離資料倉）
- `secrets/`
- `keys/`
- `*.pem` `*.key`
- `__pycache__/` `.pytest_cache/` `.mypy_cache/`
- `.DS_Store`

---

## 5. Python 環境規格（Python Runtime Standard）

### 5.1 版本原則
- **Python 主版本固定**（例如 3.11 或 3.12，依專案決策）
- 禁止：
  - 同一專案同時混用多個 Python major/minor 造成不可重建
  - 未鎖定依賴版本就宣稱可回放

### 5.2 虛擬環境（venv/conda）硬規則
- 每個 repo / workspace 必須使用獨立虛擬環境
- 虛擬環境路徑不得混用到其他專案
- 依賴必須可完整導出（lockfile 或 requirements freeze）

### 5.3 依賴鎖定（Dependency Locking）
至少擇一（不可混亂）：
- `requirements.txt` + `requirements.lock`（freeze）
- `poetry.lock`
- `conda env export`（但仍需能被稽核引用）

---

## 6. 敏感資訊治理（Secrets Governance｜本地環境硬門檻）

### 6.1 Secrets 分類
- **S0：不可存在本地**（Live 私鑰/最高權限憑證；應只在受控環境）
- **S1：可存在本地但必須受 OS 安全機制保護**（Paper keys、測試 keys）
- **S2：可明文存在但仍不得進 repo**（純公開端點、非敏感 token 名稱示例）

### 6.2 本地 Secrets 存放方式（允許清單）
- Windows Credential Manager
- macOS Keychain
- Linux Secret Service / keyring
- 受控的 Secrets Manager（本地代理）
- `.env`（僅限 Tier-0/測試；仍不得進 repo；且不得含 Live secrets）

### 6.3 禁止事項（硬禁）
- 把 secrets 寫入：
  - log
  - UI
  - exception trace（需脫敏）
  - commit message
- 在任何文件中貼上可用的 key 值
- 用共享帳號操作 Paper/Live

---

## 7. 本地資料（Data at Rest）與快照策略

### 7.1 資料分級（Data Classification）
- D0：公開資料（可進 repo 的示例）
- D1：可重建資料（可下載重拉，存引用）
- D2：需保留快照資料（用於回放/稽核，存不可變更儲存或分離倉）
- D3：敏感資料（帳戶/券商回報/個資；需加密、脫敏、最小化）

### 7.2 Snapshot/Replay 的本地要求（對齊 FULL_ARCH / VERSION_AUDIT）
- Snapshot 必須落盤（不可只在記憶體）
- Replay 必須保存：
  - active_version_map_ref
  - input_refs/output_refs
  - hash_manifest_ref
- 本地若無法提供不可變更儲存，至少要：
  - append-only 檔案策略 + hash 校驗（最低替代方案）
  - 並在 DEPLOY_OPS 上線環境使用正式 immutable store

---

## 8. 本地執行模式（Local Run Modes）與硬性阻斷

### 8.1 模式旗標（必須明確）
- `MODE=RESEARCH`
- `MODE=BACKTEST`
- `MODE=SIMULATION`
- `MODE=PAPER`
- `MODE=LIVE`

### 8.2 硬性阻斷條件（Block Conditions）
只要成立任一條件，必須阻斷並提示原因碼：
- MODE=LIVE 但偵測到：
  - 無 Kill Switch Preflight
  - 無 immutable audit 寫入能力
  - 無 risk_pass_token 驗證鏈
  - secrets 來源不合規（例如 .env 明文）
- MODE=RESEARCH 卻偵測到 Live/Paper 端點或 Live keys
- 無 active_version_map_ref（SYS-VERSION）
- 無 hash_manifest_ref（SYS-HASH/SYS-AUDIT）

---

## 9. 本地審計（Local Audit）與最小輸出

> 原則：即便本地研究，仍要能「回放」與「追溯」。

### 9.1 本地最小稽核輸出（不可縮減）
- `active_version_map.json`（引用或檔案）
- `run_manifest.json`（本次執行摘要：mode、時間、入口、correlation_id）
- `artifact_index.json`（輸入/輸出 refs 清單）
- `hash_manifest.json`（校驗）
- `logs/`（脫敏後）

### 9.2 日誌脫敏（Redaction）
- 任何疑似 key/token/email/account_id：
  - 必須遮罩（例如只保留前後 2~4 碼）
- Exception stack trace 需過濾敏感欄位

---

## 10. 本地網路與端點治理（Network & Endpoints）

### 10.1 官方資料端點優先（對齊 DATA_UNIVERSE 原則）
- 若同時存在官方與第三方來源：
  - 預設官方優先
  - 第三方作 fallback（需標記 provenance）

### 10.2 端點白名單（Endpoint Allowlist）
- Tier-0 可允許官方公開端點、資料下載端點
- Tier-1/2 端點白名單必須更嚴格：
  - 券商 API 端點（明確列出）
  - 稽核儲存端點
  - 禁止任意外連

---

## 11. 開發工具鏈規範（Dev Toolchain Standard）

### 11.1 Git 規範（對齊 VERSION_AUDIT）
- 所有重要行為必須有 commit ref（或等價版本 ref）
- 禁止：
  - 直接在 Live 環境「改程式不留痕」
  - 用未稽核的 zip/手動拷貝替代版本控管

### 11.2 IDE 與執行器（Cursor/VSCode/Terminal）
- 允許使用 Cursor / VSCode
- 但必須遵守：
  - secrets 不得被 IDE 同步到雲端
  - logs 不得含敏感
  - 任何 Paper/Live 操作需明確二次確認（UI_SPEC 原則）

---

## 12. 本地安全基線（Security Baseline）

### 12.1 最小權限（Least Privilege）
- 本地帳號/程序權限需最小化
- 程序只取得執行所需資料與權限

### 12.2 防止誤觸 Live（Anti-Accident Controls）
- Live 模式啟動必須具備：
  - 明確環境變數 `MODE=LIVE`
  - 明確雙重確認（UI 或命令列）
  - Kill Switch Preflight 成功
  - Risk token 驗證鏈可用
  - immutable audit 可寫入
- 缺任一項 → BLOCK（不得啟動）

---

## 13. Mermaid｜本地環境治理與隔離架構圖

```mermaid
flowchart TB
  subgraph T0[Tier-0 Research/Backtest/Simulation]
    DEV[IDE/Notebook/Runner]
    VENV[Isolated Python Env]
    DATA[Local Data Cache]
    AUD[Local Append-only Audit + Hash]
  end

  subgraph T1[Tier-1 Paper]
    PUI[UI L10]
    PRISK[Risk Gate L7]
    PEXE[Execution L11]
    PIMM[Immutable Store]
    PSEC[Secrets Manager]
  end

  subgraph T2[Tier-2 Live]
    LUI[UI L10]
    LRISK[Risk Gate L7]
    LEXE[Execution L11]
    LIMM[Immutable Store (WORM)]
    LSEC[Secrets/KMS (Strict)]
  end

  DEV --> VENV --> DATA --> AUD
  T0 -. "No Live/Paper secrets" .- T1
  T0 -. "No Live endpoints" .- T2

  PSEC --> PRISK
  PSEC --> PEXE
  PUI --> PRISK --> PEXE --> PIMM

  LSEC --> LRISK
  LSEC --> LEXE
  LUI --> LRISK --> LEXE --> LIMM
14. 本地環境檢核清單（Local Env Checklist｜必做）
14.1 每次執行前（必做）
 MODE 明確（Research/Backtest/Simulation/Paper/Live）

 虛擬環境啟用（與其他專案隔離）

 依賴鎖定存在（lockfile 或 freeze）

 active_version_map 生成成功

 logs 脫敏規則啟用

 Snapshot 落盤路徑可寫入

 若 Paper/Live：Kill Switch Preflight 成功 + token 驗證鏈可用 + immutable store 可寫入

14.2 每次執行後（必做）
 產生 run_manifest + artifact_index + hash_manifest

 重要事件生成 replay bundle refs

 若有任何 BLOCK/VETO：保全證據並記錄 reason codes

15. Only-Add 演進規則（LOCAL_ENV 專屬）
允許新增：

新的環境層級（例如 staging/canary）

新的安全檢核項目與阻斷條件（更嚴格）

新的 secrets 管理方式（更安全）

新的資料分級與脫敏策略

禁止：

把敏感值放進 repo

弱化 Paper/Live 的隔離

取消 active_version_map / hash_manifest / audit 最小輸出

允許 Live 在缺 Kill Switch/Token/Immutable Audit 的狀態啟動

16. 終極裁決語句（不可更改）
環境不是個人習慣，而是治理的一部分。
任何不可重建、不可追溯、不可隔離、會洩漏敏感的環境，都不允許成為 TAITS 的執行基礎。

（LOCAL_ENV｜最大完備版 v2025-12-19 完）
---

# Addendum 2025-12-28｜Only-Add：Evidence Chain Template（LOCAL_ENV）對齊 DEPLOY_OPS D3 × 回放必需最小結構（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md（doc_key：LOCAL_ENV）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（A+）＋MASTER_ARCH（A）＋MASTER_CANON（A）＋AI_GOV（A+）  
> 平行對齊：DEPLOY_OPS｜Addendum 2025-12-27（D3：Evidence Chain 最小結構）  
> 目的：補齊 LOCAL_ENV 之「Evidence Chain Template」章節，使部署/營運/稽核在引用 LOCAL_ENV 時具備唯一可指向之段落；不改寫既有環境規範，只新增模板。

---

## LE-EC1. Evidence Chain Template（最小結構｜欄位可多不可少）

### LE-EC1.1 環境指紋（Environment Fingerprint）
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
    ref_section: LE-EC1.1
```

### LE-EC1.2 依賴清單（Dependency Manifest）
```text
dependency_manifest:
  lockfile: <requirements.txt / poetry.lock / uv.lock / package-lock.json 等>
  hash: <sha256 可選>
  generated_at: <ISO-8601>
```

### LE-EC1.3 執行證據（Run Evidence）
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

### LE-EC1.4 失敗與回復（Failure/Recovery）
```text
failure_recovery:
  status: <PASS/FAIL>
  error_summary: <如 FAIL，摘要>
  recovery_action: <回滾/修復行動>
  notes: <可選>
```

---

## LE-EC2. 引用方式（供 DEPLOY_OPS / VERSION_AUDIT / GOV Gate 使用）

- 本模板之合法引用段落：`LOCAL_ENV §LE-EC1`（本 Addendum）  
- 任何需要「可回放證據鏈」的產物/紀錄，至少包含 LE-EC1 結構；並在引用標頭中填入：
  - `doc_key=LOCAL_ENV`
  - `ref_section=LE-EC1`
---

## Appendix 2025-12-28｜Only-Add：治理識別（doc_key）× 實體檔名（Physical Filename）對齊宣告（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md（doc_key：LOCAL_ENV）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（A+｜Authoritative Index）→ MASTER_ARCH（A）→ MASTER_CANON（A）＋AI_GOV（A+）  
> 目的：在不改寫本文件既有任何章節內容與語義的前提下，補齊「引用合法性」所需的識別資訊與檔名映射規則；避免因 Addendum/下載副本檔名差異導致 Gate / 稽核引用失配。

### A1. 本文件之唯一治理身份（Canonical Identity）
- canonical_filename（Index 裁決檔名）：`TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md`
- canonical_doc_key（Index 裁決識別碼）：`LOCAL_ENV`
- 版本狀態：ACTIVE（Freeze v1.0；Only-Add）

### A2. 本專案目錄中的實體檔案（Physical Artifact）
- physical_filename（目前專案內實際檔名）：`TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md`
- 法律定位：實體檔名僅為「存放/分發/下載」之載體；治理裁決與引用身份一律以 **A1** 為準。

### A3. 引用合法性最小規則（不新增制度，只固定寫法）
- 任何跨文件引用本文件時，必須使用：`doc_key=LOCAL_ENV` + `canonical_filename=TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md`。  
- 若需指向本專案內實體檔案（physical_filename），必須同時保留 **A1** 之 canonical identity，以避免「引用找得到檔案但身份不合法」的 Gate 風險。  
- ACTIVE 集合、文件數量、或任何快照清單，均不得覆蓋 DOCUMENT_INDEX 的 Authoritative Index 裁決。

---

# Addendum 2025-12-28｜Only-Add：GLOBAL_ALIGNMENT_PATCH（MASTER_CANON 對齊全域補丁）｜Freeze v1.0

> 補充性質：Only-Add（只可新增，不可刪減、覆寫、偷換既有語義）  
> 適用文件：TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md（doc_key：LOCAL_ENV）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決序列：DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON（AI 行為規範仍受 AI_GOV 最高約束；衝突裁決流程依 DOCUMENT_INDEX §6）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger（條目：`VA-METADATA_FIX-20251228-0012`）  
> 目的：以 MASTER_CANON 為主導，對齊「引用合法性、doc_key 身份、子級標籤（Label）解讀、資料治理別名（alias）封口、最小可稽核引用格式」之全域一致口徑；不改寫任何既有正文條款。

---

## G0. 適用範圍（Hard Boundary）

本 Addendum 僅處理下列事項（不創造新制度、不改寫主文）：
1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。  
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。  
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。  
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。  

本 Addendum **不處理**：
- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

- 本文件 `doc_key` 既有標示為 `LOCAL_ENV`；本 Addendum 仍以 Index Gate 口徑再次鎖定其引用端合法身份。

並統一裁決：
- 任何文件「是否可引用」＝以 DOCUMENT_INDEX 之 Authoritative Index（ACTIVE 表格）為準  
- 任何文件「治理等級 bucket」＝以 DOCUMENT_INDEX 之 A+ / A / B / C 分桶為準  
- 文件內自述之等級/狀態若與 Index 有張力：依 DOCUMENT_INDEX §6 採「保守處置」（STOP/RETURN/BLOCK；以既有 Gate/風控規範語義為準）

---

## G2. 子級標籤（Label）之唯一合法解讀（S / B+ / C+）

凡本文件或引用鏈中出現：
- `S`：視為「Supreme Canon 的顯示標籤」或「完備度標籤」，**不構成**新的治理等級 bucket。  
- `B+` / `C+`：視為「嚴格度/完備度子級標籤」，**不構成**新的治理等級 bucket。  

治理覆蓋規則仍固定為：**A+ > A > B > C**（以 DOCUMENT_INDEX 為準）。  

---

## G3. DATA_UNIVERSE（alias）封口（資料治理引用回歸 DATA_SOURCES）

統一裁決：
- 任何出現之 `DATA_UNIVERSE` 一律視為「資料宇宙（Data Universe）」概念別名（alias），**不得**作為 doc_key。  
- 任何需要引用資料來源治理時，唯一合法 doc_key：`DATA_SOURCES`。  
- 若 Evidence/Audit/UI Trace/Gate 引用欄位出現 `doc_key=DATA_UNIVERSE`：  
  - 一律視為「引用非法」→ 依 GOVERNANCE_GATE_SPEC 進行 BLOCK/RETURN（依其既有語義；不得補救）。

---

## G4. 最小可稽核引用格式（Minimum Legal Citation Format｜可直接貼用）

凡聲稱「依據治理文件」之輸出（含：Evidence、Risk/Compliance、Governance Gate、UI Decision、Execution Control、Audit）一律必須同時提供：

```text
ref_doc_key = <DOC_KEY>
ref_file = <完整檔名>
ref_version = <版本日期或檔名日期碼>
ref_section = <章節定位（§ / Heading Path）>
ref_purpose = <用途：例如 gate_check / risk_veto / ui_decision / execution_policy / audit_replay>
ref_notes = <可選：alias/Label 解讀備註>
```

缺任一欄位：
- 依 DOCUMENT_INDEX §6 採保守處置：不得形成裁決性輸出（PASS/APPROVE/EXECUTE 等）；必要時 RETURN/BLOCK。

---

## G5. 最終宣告（Freeze v1.0）

- 本 Addendum 為 Only-Add；不改寫本文件任何既有條款。  
- 本 Addendum 之解讀與適用，均以 DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON 為最終裁決順序；AI 行為仍以 AI_GOV 為最高約束。  
- 本 Addendum 目的僅在於消解引用歧義、避免 Gate 因 metadata/格式缺口而誤判，並確保全鏈路可稽核、可回放。

（Addendum 2025-12-28｜Only-Add｜Freeze v1.0 完）
---

# Addendum 2025-12-29｜Only-Add：AI制度全量對齊（Index Gate × 引用最小格式 × 稽核錨點）（Freeze v1.0）

> 補充性質：Only-Add（只可新增，不可刪減／覆寫／偷換既有語義）  
> 適用文件：TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219__ADDENDUM_20251229_AI_GOV_SYNC_FINAL.md（doc_key：LOCAL_ENV）  
> 生效狀態：GOVERNANCE_STATE = Freeze v1.0  
> 上位裁決：DOCUMENT_INDEX（Index Gate／衝突裁決）＋ MASTER_ARCH（鐵律）＋ MASTER_CANON（Canonical Flow）＋ AI_GOV（A+ 行為/引用約束）  
> 稽核對位：VERSION_AUDIT｜Appendix A｜METADATA_FIX Ledger｜VA-METADATA_FIX-20251229-0001（BATCH-20251229-AI_GOV_SYNC-0001）  

---

## 0. 適用範圍（Hard Boundary）

本 Addendum 僅補強「引用合法性」與「裁決依據可稽核」之共用口徑，不改寫本文件任何既有條款；亦不新增任何新的治理權力、裁決權或流程捷徑。

---

## 1. Index Gate（DOCUMENT_INDEX）唯一裁決

1) **文件有效性（Governance Validity）**：凡未被 DOCUMENT_INDEX Authoritative Index 表格裁決為有效（ACTIVE 且對應 doc_key/治理等級），不得作為：  
- 系統行為依據  
- AI 推論依據  
- Gate / Risk / Compliance / Human Decision 之裁決依據  

2) **衝突裁決（Conflict Resolution）**：凡本文件內任何敘述與 DOCUMENT_INDEX 之覆蓋規則／衝突裁決程序產生張力，一律回到 DOCUMENT_INDEX 裁決，不得跳步。

---

## 2. 引用合法性最小格式（Minimum Legal Citation Format｜G2 對位）

凡本文件條文（或其被引用時）涉及「依據某文件／某規範」之主張，最少必須包含下列欄位（缺一視為未引用）：

- `ref_file`：完整檔名  
- `ref_doc_key`：doc_key  
- `ref_version_date`：版本日期（YYYY-MM-DD 或 __yymmdd）  
- `ref_section`：章節定位（heading path / §x.y）  
- `audit_anchor`：對應 VERSION_AUDIT 的稽核錨點  

缺任一欄位 → 一律視為「未引用」→ 不得作為裁決性輸出之依據（依 DOCUMENT_INDEX §6 保守處置並留痕）。

---

## 3. 裁決順序字串一律視為助記（Mnemonic-Only）

本文件內若出現任何「裁決順序字串」或箭頭序列（例如：`DOCUMENT_INDEX → MASTER_ARCH → MASTER_CANON`），一律視為閱讀/操作助記：  
- 不得被用作覆蓋規則或裁決權重新分配  
- 若與 DOCUMENT_INDEX 之覆蓋規則或衝突裁決程序產生張力：一律回到 DOCUMENT_INDEX

---

## 4. 稽核錨點（Audit Anchor）與本次批次識別

- 本次全量對齊批次識別：`BATCH-20251229-AI_GOV_SYNC-0001`  
- 本文件本次補強之稽核錨點：`VA-METADATA_FIX-20251229-0001`  
- 後續任何引用/裁決輸出，若涉及本 Addendum 之口徑，應以本錨點作為 audit 對位起點。

---

## 5. 最終宣告

- 本 Addendum 為 Only-Add；不改寫本文件任何既有條款。  
- 本 Addendum 僅用於確保「引用合法性」與「可稽核/可回放」的一致口徑。  

（Addendum 2025-12-29｜Only-Add｜Freeze v1.0 完）
