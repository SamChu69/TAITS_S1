# 📘 TAITS_Versioning_ChangeLog_and_Evolution_Rules.md

**（版本治理 × 變更紀錄 × 非破壞式演進規範｜Final）**

---

## 0. 文件定位（最高治理層）

本文件定義 **TAITS 如何隨時間演進而不崩壞**。
它確保三件事同時成立：

1. **任何結果可回放（Reproducible）**
2. **任何變更可審計（Auditable）**
3. **任何擴充不破壞母體（Non-Destructive）**

> 本文件 **高於** 個別策略、模組與實作決策。

---

## 1. 世界一流內部評分標準（10/10 必要條件）

* 單一、不可歧義的版本規則
* 任何人照規則操作都能得到一致結果
* 支援長期（≥10 年）演進
* 與 TAITS_00–12 完全對齊
* 不允許「偷偷改」
* 明確區分：**母體變更 vs 實作變更**

---

## 2. 版本命名規則（唯一合法）

### 2.1 母體版本（System Mother Version）

> 適用於 **TAITS_00–12**（系統母體）

```
TAITS-SYS vMAJOR.MINOR.PATCH
```

* **MAJOR**：設計原則 / 分層 / 核心邏輯變更（極少）
* **MINOR**：新增模組或規範（不破壞既有語義）
* **PATCH**：文字修正、補充說明、不影響語義

**範例：**

* `TAITS-SYS v1.0.0`（首次封板）
* `TAITS-SYS v1.1.0`（新增 13+ 擴充規範）
* `TAITS-SYS v1.1.1`（說明補強，無語義變更）

> 📌 **原則**：00–12 一起升版，不分別升版。

---

### 2.2 引擎與矩陣版本（可獨立）

以下允許獨立版本（但必須在 Manifest 中綁定）：

* Regime Engine
* Strategy Matrix
* Risk Engine
* Feature Factory
* Pipeline

```
<Module>-vMAJOR.MINOR.PATCH
```

---

## 3. CHANGELOG 規範（強制）

### 3.1 CHANGELOG 檔名與位置

```
CHANGELOG.md   （Repo 根目錄）
```

### 3.2 CHANGELOG 結構（不可省略）

```markdown
# CHANGELOG

## [TAITS-SYS v1.0.0] - YYYY-MM-DD
### Added
- 初始封板：00–12 系統母體文件

### Changed
- 無

### Deprecated
- 無

### Removed
- 無

### Fixed
- 無

### Impact
- 首次可落地版本
```

---

### 3.3 變更分類定義（嚴格）

* **Added**：新增能力，不影響舊邏輯
* **Changed**：語義或行為改變（需說明影響）
* **Deprecated**：宣告未來將移除（仍可用）
* **Removed**：正式移除（需提供替代方案）
* **Fixed**：錯誤修正（不改語義）
* **Impact**：對回測、策略、風控的實際影響

> ❗ **沒有 Impact 說明的變更，一律視為不合格。**

---

## 4. 非破壞式演進（Non-Destructive Evolution）

### 4.1 絕對禁止事項

* ❌ 覆寫或刪除 00–12 的既有語義
* ❌ 改名造成歷史文件不可對照
* ❌ 未升版直接改母體
* ❌ 讓舊回測無法重現

---

### 4.2 合法演進方式（唯一）

1. **新增附錄（Appendix）**

   * 不改原文，只補充

2. **新增新文件（13+）**

   * 僅引用 00–12
   * 不反向依賴

3. **MINOR 升版**

   * 明確列出影響範圍
   * 提供遷移說明

---

## 5. 實驗與回測的版本綁定（強制）

任何回測或驗證 **必須輸出 Manifest**：

```json
{
  "system_version": "TAITS-SYS v1.0.0",
  "regime_engine_version": "RE-v1.2.0",
  "strategy_matrix_version": "SM-v1.1.3",
  "risk_engine_version": "RK-v1.0.2",
  "feature_factory_version": "FF-v1.3.1",
  "data_snapshot_id": "DATA_2024Q4_A",
  "run_id": "RUN_20250115_001"
}
```

> 📌 **沒有 Manifest 的結果，一律不可採信。**

---

## 6. 審計與回滾（Audit & Rollback）

* 每個版本必須：

  * 可指出「從哪個版本來」
  * 可回滾到上一穩定版
* 發現重大問題時：

  * 標記為 `Deprecated`
  * 不直接刪除

---

## 7. 與 GitHub Flow 的關係（建議）

* `main`：只放穩定母體版本
* `develop`：準備下一個 MINOR
* `experiment/*`：實驗性（不可合併 main）

---

## 8. 責任分界（防爭議）

* **TAITS-SYS 版本**：系統架構責任
* **Module 版本**：工程 / 研究責任
* **Execution / API**：實作責任（不影響母體）

---

## 9. 首次封板聲明（建議寫入 CHANGELOG）

```markdown
## [TAITS-SYS v1.0.0] - YYYY-MM-DD
### Added
- 完整 00–12 系統母體文件
- 334 條策略宇宙
- Regime R1–R10 判定與驗證 Pipeline
- 治理與風控否決機制

### Impact
- TAITS 正式進入可落地、可驗證、可演進狀態
```

---

## 10. C 檔完成聲明

* ✔ 版本規則唯一
* ✔ CHANGELOG 可直接使用
* ✔ 支援長期演進
* ✔ 不破壞既有成果
* ✔ 與 README / Index / 00–12 完全對齊

---

## 🎯 主幹完成確認

至此，你已完整擁有：

* **README.md（A）**
* **Index & Cross-Reference（B）**
* **Versioning & CHANGELOG（C）**
* **TAITS 00–12 系統母體**

👉 **TAITS GitHub 最終主幹正式完成。**
