# TAITS_GPT_ECR_LEDGER（GPT 編輯工作包帳本｜Append-only）__ADDENDUM_20251228R_FINAL

> 文件定位：GPT Project Editing Ledger（工程支援；非治理裁決文件）  
> 規則：Append-only（只追加，不覆寫、不刪除）  
> 用途：新對話續編時，快速取回「做到哪 / 改了什麼 / 依據什麼 / 產物在哪」。  

---

## 1. 欄位說明（最小欄位）

- ecr_id：工作包編號（你自訂，但要唯一；建議 `ECR-YYYYMMDD-####`）
- created_at：建立時間（Asia/Taipei）
- work_type：REPORT_ONLY / ONLY_ADD_EDIT / GATE_CHECK
- target_doc_key：本次目標 doc_key
- target_file：你實際要貼入/更新的檔名（或「產出檔」）
- insert_point：插入位置（章節/段落路徑；Report-only 可填 N/A）
- change_summary：一句話摘要（Only-Add）
- ref_min_citation：引用摘要（至少包含：ref_file / ref_doc_key / ref_version_date / ref_section / audit_anchor）
- gate_result：PASS / RETURN / BLOCK（若未做 Gate 檢核則填 N/A）
- output_artifact：輸出產物路徑或檔名（例如：新增段落標題 / addendum 檔）
- next_step：下一個工作包要做什麼（務必寫一句話）

---

## 2. Ledger Entries（只追加）

| ecr_id | created_at | work_type | target_doc_key | target_file | insert_point | change_summary | ref_min_citation | gate_result | output_artifact | next_step |
|---|---|---|---|---|---|---|---|---|---|---|
| ECR-20251228-0001 | 2025-12-28 00:00 | ONLY_ADD_EDIT | (EXAMPLE) DOCUMENT_INDEX | (EXAMPLE) <file>.md | (EXAMPLE) §X 末 | (EXAMPLE) 新增：引用格式補強段 | ref_file=...; ref_doc_key=...; ref_version_date=...; ref_section=...; audit_anchor=... | N/A | (EXAMPLE) 段落標題/產出檔 | (EXAMPLE) 下一包：Only-Add 增補 MASTER_ARCH |
| ECR-20251228-0002 | 2025-12-28 00:00 | REPORT_ONLY | (EXAMPLE) MASTER_CANON | (EXAMPLE) <file>.md | N/A | (EXAMPLE) 盤點：L1–L11 邊界缺口 | ref_file=...; ref_doc_key=...; ref_version_date=...; ref_section=...; audit_anchor=... | N/A | (EXAMPLE) 報告摘要 | (EXAMPLE) 下一包：Only-Add 補一段於 §Y 末 |

> 實際使用時：每完成一個工作包，就在表格最後新增一列；不要改舊列。
