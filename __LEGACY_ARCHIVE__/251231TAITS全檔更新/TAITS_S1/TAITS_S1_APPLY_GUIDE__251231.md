# TAITS_S1｜套用與防漂移指南（工程用）
版本：v1.0（251231）

## 1. 本包定位
- 本包是 S1 工程落地支援檔
- 不直接取代 A/A+ 母法治理文件
- 但工程落地時，必須以本包的「L9–L11 鎖定語義」作為唯一口徑，避免 AI 腦補漂移

## 2. 工程引用規則（強制）
1) 在程式碼倉庫（或 Cursor 專案）建立 `docs/TAITS_S1/`，將本包檔案放入  
2) 所有涉及 L9/L10/L11 的實作、PR、Commit message，必須引用對應章節錨點（例如：`TAITS_S1_MASTER_SPEC__251231.md#2-l9l11...`）  
3) 任何對 L9/L10/L11 的描述若與本包不一致，一律視為錯誤，需回到本包修訂（S1）後再反映到母法（如需）

## 3. 防止 AI 減少內容的工程措施
- 把「必備欄位」寫成 schema（L9 metadata, L10 decision_record, L11 audit_manifest）
- 由程式在輸出時做 schema validation；缺欄位直接 fail，避免 AI 偷縮
- 對 L11：必須紀錄 model_id / runtime / prompt_hash / artifact_hash，確保可回放

## 4. 什麼時候需要回寫母法文件？
- 當你確認 S1 工程落地的語義與工件集合已穩定，且要鎖定為長期治理規則  
- 才進入「治理狀態切換（UNFREEZE/Freeze）」程序，做母法級全量覆寫（你裁決後執行）

（完）
