# TAITS_GOVERNANCE_STATE__UNFREEZE_v1.1__251231
doc_key：GOVERNANCE_STATE_UNFREEZE_V1_1  
治理等級：A（Governance State｜治理狀態裁決文件）  
適用範圍：TAITS 全系統（僅限本次 L9–L11 語義全面重編之變更窗口）  
版本狀態：ARCHIVED（變更窗口已關閉；保留作為票據）  
版本日期：2025-12-31  
上位裁決：DOCUMENT_INDEX（A+）→ MASTER_ARCH（A）→ AI_GOV（A+）  
平行參照：VERSION_AUDIT / GOVERNANCE_GATE_SPEC / DEPLOY_OPS  
變更原則：**整併式覆寫（Merge-Overwrite）**：允許更新正文以消除語義歧義，但 **不得刪減既有內容**；舊文須移至 `DEPRECATED / Legacy` 附錄保留以供追溯。  

---

## 0. 文件定位（State Ticket）

本文件為一次性治理狀態「變更窗口票據」：  
用於授權並記錄「L9–L11 語義全面重編（B 路徑）」所需之整併式覆寫行為。

本票據不授權：
- 任何交易策略新增/改寫（→ STRATEGY_UNIVERSE）
- 任何風險合規否決權之弱化（→ RISK_COMPLIANCE）
- 任何執行控制流程的降級（→ EXECUTION_CONTROL）

---

## 1. 變更窗口授權範圍（Bounded Authorization）

### 1.1 唯一授權事項（Only Authorized Scope）
- **L9–L11 語義全面重編（B 路徑）**，目的：消除 AI 腦補、語義漂移與層級混線。  
  - L9：投資報告層（可見、可追蹤、可版本化）  
  - L10：人類裁決與交易授權  
  - L11：工程稽核（全層回放、雙料輸出）

### 1.2 強制約束（Hard Constraints）
- 不得刪除既有段落（可搬移至 DEPRECATED 附錄）。
- 不得摘要化導致語義縮減。
- 所有變更必須在 VERSION_AUDIT 留痕（含 approver）。

---

## 2. 窗口關閉（Closure）

本票據之變更窗口於完成下列事項後視為關閉：
- `TAITS_GOVERNANCE_STATE__FREEZE_v1.1__251231.md` 設為 ACTIVE（DOCUMENT_INDEX 裁決）
- VERSION_AUDIT 新增 `L9L10L11_SEMANTIC_REBASE` 條目

本文件保留為 ARCHIVED，僅供追溯。
