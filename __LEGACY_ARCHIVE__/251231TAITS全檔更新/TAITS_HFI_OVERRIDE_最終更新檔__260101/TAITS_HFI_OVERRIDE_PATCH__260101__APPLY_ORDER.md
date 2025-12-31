# TAITS_HFI_OVERRIDE_PATCH__260101｜套用指引（APPLY_ORDER）

本補丁的目的：讓「人類最高決策者」之明確授權命令具備可執行觸發機制（HFI：Human Final Instruction），使 Freeze/Only-Add 不再造成「實務上無法更新」之卡死；同時以稽核留痕承接（可回放、可追溯）。

## 0) 套用前置
- 先備份原檔（建議保留原檔原名於備份資料夾）。
- 本補丁為 **Only-Add**：僅新增條款，不刪減、不覆寫原有語義段落。

## 1) 建議套用順序（強制）
1. DOCUMENT_INDEX（A+）：新增 HFI 定義與 Override 規則（最高裁決入口）
2. GOVERNANCE_STATE__FREEZE（A）：新增 Freeze 例外條款（HFI Override）
3. VERSION_AUDIT（B）：新增 HFI Ledger（強制留痕欄位）
4. MASTER_ARCH（A）：新增消歧義（Human Sovereignty vs Supreme Veto）

## 2) 套用方式（推薦）
將本資料夾內四份 `__HFI_OVERRIDE_READY_TO_REPLACE.md` 以「同文件對應」方式替換回 TAITS 專案檔案庫（由你人工決定是否改檔名或以新版本檔名併存）。

## 3) 對帳
請使用 `TAITS_HFI_OVERRIDE_PATCH__260101__SHA256_MANIFEST.json` 進行對帳，確保落盤內容一致。

