# TAITS｜L9–L11 語義全面重編（B 路徑）｜套用順序（APPLY_ORDER）__251231

生效日：2025-12-31（Asia/Taipei）

本更新包為「整併式覆寫（Merge-Overwrite）」：正文已完成語義重編並消歧，舊口徑一律移至 DEPRECATED/Legacy 附錄保留以供追溯。

## 套用順序（強制）

1) 先放入治理狀態票據（狀態文件）
- `TAITS_GOVERNANCE_STATE__UNFREEZE_v1.1__251231.md`（ARCHIVED：票據留存）
- `TAITS_GOVERNANCE_STATE__FREEZE_v1.1__251231.md`（ACTIVE：最終鎖定）
- `TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231.md`（更新為 ARCHIVED）

2) 更新裁決索引與稽核帳本（使全系統不再誤讀舊狀態）
- `TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md`
- `TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__251231.md`

3) 再更新其餘治理文件（已全量插入 L9–L11 Binding 段落）
- 其餘 20 份文件（含 MASTER_CANON / ARCH_FLOW / EXECUTION_CONTROL / UI_SPEC / RISK_COMPLIANCE 等）

## 核心驗收（你可以用來快速檢查）

- 任一文件中看到「L9=Gate」或「L11=Execution」：必須被明確標記為 DEPRECATED，且不得出現在現行裁決主線。
- 任一文件中，L9–L11 的現行解讀必須與 Binding 段落一致：
  - L9：投資報告（數據/圖形/進出建議/追蹤鍵）
  - L10：人類裁決與交易授權
  - L11：工程稽核（全層留痕 + 雙料輸出）
- LOCAL_ENV 必須包含「Windows 11 + RAM 32GB」之工作站基線。
