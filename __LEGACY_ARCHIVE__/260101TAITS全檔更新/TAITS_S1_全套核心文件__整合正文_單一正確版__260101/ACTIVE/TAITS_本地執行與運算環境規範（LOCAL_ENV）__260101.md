<!--
TAITS｜ACTIVE UPDATED（單檔內嵌更新版）
產出日期：2025-12-29（Asia/Taipei）
更新規格：單檔內嵌；可更新處直接更新並避免重複；不可更新處以 Appendix 內嵌 Only-Add 全文。
來源檔：TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md
-->

# TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219
doc_key：LOCAL_ENV  
治理等級：C（Local Execution & Compute Environment｜環境治理與敏感隔離）  
適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（環境規範可 Only-Add 擴充）  
版本日期：2026-01-01  
對齊母法：TAITS_AI_行為與決策治理最終規則全集__251217（A+）  
上位約束：MASTER_ARCH / DOCUMENT_INDEX / VERSION_AUDIT（環境亦屬可追溯治理）  
平行參照：DEPLOY_OPS / FULL_ARCH / EXECUTION_CONTROL / RISK_COMPLIANCE / UI_SPEC / TWSE_RULES  
變更原則：Only-Add（只可新增，不可刪減/覆寫/弱化：金鑰隔離、可回放稽核、最小權限、可回滾/可停機）  
核心鐵律：敏感不入 repo；環境可重建；版本可追溯；審計不可變更；Live/Paper 與 Research 的隔離不可被打破

## SOVEREIGNTY｜人類最高決策者唯一主權（不可牴觸｜單一口徑）

1. TAITS 之**唯一最高主權**屬於人類最高決策者（產品負責人／架構裁決者）。
2. 任何文件治理等級（A+／A／B／C）、任何治理閘門（Gate）、任何 Agent、任何程序性規則不得高於人類主權；不得以程序性理由阻止人類明確命令之生效。
3. 風險與合規（Risk/Compliance）之「最高否決權」屬**系統內最高否決**：在**無人類明確命令**時可否決；在**有人類明確命令**時必須輸出完整風險揭露與替代方案，但不得將其結果升格為阻止命令之否決，改以「強制揭露＋確認＋全紀錄」承接。

## L9–L11｜最終語義定錨（跨文件一致｜單一口徑）

- **L9（投資報告層）**：輸出「可追蹤、可更新、可標的化」投資報告；必含數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源）。報告需可因市場事件/風險變化滾動更新。
- **L10（人類裁決層）**：人類最高決策者基於 L9 與治理/風控資訊裁決：不動作/回測/模擬/半自動/全自動等；任何交易型態皆以 L10 明確裁決為準。
- **L11（工程稽核回放層）**：對 **L1–L11 全層**輸入/處理/輸出/裁決/執行鏈路留痕，供你與工程端可讀、可查、可回放；L11 非下單決策層。

## HFI｜人類明確命令（可執行觸發｜單一口徑）

本系統承認以下最小格式之人類明確命令（HFI：Human Final Instruction），以確保主權可執行且不再被 Freeze/Only-Add/Gate 以程序性理由阻擋：

- `HFI: <scope> | <action> | <intent> | <acknowledgement>`

當有效 HFI 存在時：Freeze/Only-Add/Gate 不得阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。


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
