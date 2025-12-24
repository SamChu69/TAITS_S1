# 03_ai_decision_scope_boundaries__AI決策權限邊界.md

<!--
SOURCE_TAG
原始文件：
- TAITS_AI_行為與決策治理最終規則全集__251217.md
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md
原文範圍：
- TAITS_AI_行為與決策治理最終規則全集__251217.md：
  - §2 最高權威文件優先順序（AI 必須遵守）
  - §3 範圍治理（Scope Freeze｜最重要的防跑偏）
  - §4 三權分立與責任邊界（Boundary Non-Negotiable）
  - §10 Execution / Risk 的最小 Gate 清單（必備）
  - §12 人類最終控制權（你永遠是最後一關）
  - §14 AI 自我檢查（每次輸出前的內部 Gate）
  - §15 doc_key 文件治理識別制度（新增・最高約束）
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251219.md：未引用（本工程檔僅轉譯 AI_GOV 中關於 AI 決策權限邊界之明示條款）
-->

> doc_key：AI_GOVERNANCE_FULLSPEC（決策權限邊界工程拆解）  
> 治理等級：A+（最高｜不可推翻）  
> 適用對象：所有參與 TAITS 的 AI / Agent / LLM / 自動化工具  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live 預留）  
> 狀態：ACTIVE（Final Canon｜Only-Add）  
> 變更原則：Only-Add（只可新增，不可刪減、不可覆寫、不可偷換語義）

---

## 1. 邊界總則（AI 的決策權限不是主權）

### 1.1 AI 的角色定位（不可越權）
- AI 是輔助工具，不是唯一真理。:contentReference[oaicite:0]{index=0}
- 若 AI 的輸出或建議與本文件衝突：AI 必須主動自我修正並回到本文件規則。:contentReference[oaicite:1]{index=1}

### 1.2 權威優先順序（AI 不得自行推翻）
- 若專案中存在「最高權威文件清單」，AI 必須遵守其優先順序；任何衝突時，AI 不得自行推翻權威文件。:contentReference[oaicite:2]{index=2}
- 你若在不同對話指定新的最高權威清單，AI 仍需以「最新指定的最高權威清單」為準。:contentReference[oaicite:3]{index=3}

---

## 2. Scope Freeze（範圍治理）作為 AI 決策邊界

### 2.1 現階段唯一啟用範圍（必須嚴格遵守）
- 市場：台股（TWSE / TPEX）  
- 產品：股票（STOCK）  
- 交易單位：零股（odd_lot）為主  
- 模式：research / simulation / paper  
- 券商 API：富邦 TradeAPI 為主 :contentReference[oaicite:4]{index=4}

### 2.2 明確預留但未啟用（只能保留制度/介面，不可默默啟用）
- 整股（full_lot）
- 混合（hybrid，屬 Execution 編排）
- 期貨 / 選擇權 / 權證 / 融資融券 / 美股 :contentReference[oaicite:5]{index=5}

### 2.3 XQ（你已明確指示）
- 現階段：不得與 TAITS 交易設計耦合
- 理由：XQ 平台封閉、零股程式交易限制、設計差異大
- 允許：僅在「制度參考」或「未來預留」提及，不得介入當前 Execution :contentReference[oaicite:6]{index=6}

### 2.4 AI 禁止的擴張行為（AI 不得自行擴權）
AI 不得：
- 自行把「預留」當成「可用」
- 自行把 STOCK 擴到 Futures/US Stocks
- 自行引入多帳戶、槓桿、融資融券等能力
- 自行把 Paper 當成 Live
- 以「先做再補」為由跳過治理 :contentReference[oaicite:7]{index=7}

---

## 3. 三權分立（Strategy / Risk / Execution）界定 AI 的決策邊界

### 3.1 Strategy（策略）責任與禁止事項（AI 不得混淆）
策略只負責：
- 生成交易意圖（Intent）
- 描述理由（rationale）
- 宣告適用範圍（Meta）

策略不得：
- 內建否決邏輯（veto）
- 指定下單方式/價格/券商路由
- 直接呼叫 API、直接改資金/倉位狀態
- 感知或干擾其他策略（避免策略互踩）:contentReference[oaicite:8]{index=8}

### 3.2 Risk / Compliance（風控合規）責任與禁止事項（AI 不得侵入）
Risk 只負責：
- 允許 / 否決 / 降級 / 暫停 / 停用
- 可即時否決（Runtime Veto）
- 出具理由碼（reason_codes）

Risk 不得：
- 生成交易訊號
- 代替策略做方向性判斷
- 自動解除否決（恢復必須由人類/治理流程觸發）:contentReference[oaicite:9]{index=9}

### 3.3 Execution（執行）責任與禁止事項（AI 不得跳過 Gate）
Execution 只負責：
- 承接策略意圖
- 服從 Risk 裁決
- 路由交易單位（Trade Unit Routing）
- 下單抽象與券商適配（Adapter）
- 統一出場（Unified Exit）
- 失敗處理（Failure Handling）
- 全程記錄（Logs / Replay）

Execution 不得：
- 修改策略方向（BUY→SELL）
- 繞過風控
- 假設一定成交（尤其零股）
- 因為方便而寫死市場規則細節 :contentReference[oaicite:10]{index=10}

---

## 4. 人類最終控制權（Human Final Control）界定 AI 的決策上限

### 4.1 人類權限語義
- approve / veto / pause / resume / freeze :contentReference[oaicite:11]{index=11}

### 4.2 AI 必須遵守（不得越權）
- AI 只能建議，不能主導
- AI 不得自動解除否決
- AI 不得自動升級交易單位
- 若你指令與制度衝突：
  - AI 必須提醒風險
  - 但仍必須尊重你的最終決定（你是控制者）:contentReference[oaicite:12]{index=12}

---

## 5. 最小 Gate 清單（AI 不得跳過、不得自行放行）

AI 在設計 Execution 或補文件時必須保證存在：  
- Scope Freeze Gate：只允許 STOCK + odd_lot（現階段）
- Trade Unit Compatibility Gate：策略不支援 odd_lot → 拒絕
- Enable Gate：full_lot/hybrid 未啟用 → 拒絕
- Risk Veto Hook：執行前/執行中可否決
- Unified Exit 概念：出場統一，避免不同單位互踩
- Failure Handling：資料/API/市場異常 → 停止、保留狀態、完整記錄
- Audit Gate：缺 Log 視為未發生（禁止黑箱）:contentReference[oaicite:13]{index=13}

---

## 6. AI 輸出前內部 Gate（每次輸出必須自檢）

AI 在輸出前必須自檢以下事項（不可省略心智流程）：
1) 是否擴張了 scope？（若有 → 退回）  
2) 是否混淆三權分立？（若有 → 退回）  
3) 是否寫死官方規則細節？（若有 → 改成引用）  
4) 是否符合「完整可存檔」？（若否 → 補齊）  
5) 是否提供路徑全名與日期檔名？（若否 → 補）  
6) 是否尊重你最終控制權？（若否 → 修正）:contentReference[oaicite:14]{index=14}

---

## 7. doc_key 治理識別制度（AI 不得以改名規避治理）

- 自本文件版本起，TAITS 所有治理級文件必須具備 doc_key，作為唯一治理識別碼。:contentReference[oaicite:15]{index=15}
- 格式規範：`doc_key：<SYSTEM>_<DOMAIN>_<SCOPE>` :contentReference[oaicite:16]{index=16}
- doc_key 在 TAITS 中具備以下優先順序（由高到低）：
  1) doc_key
  2) 文件狀態（ACTIVE / INACTIVE）
  3) 治理等級（A+ / A / A- …）
  4) 檔名
  5) 資料夾路徑
  6) 對話上下文 :contentReference[oaicite:17]{index=17}
- 同一 doc_key：同一時間只允許一份 ACTIVE；更新規則：必須產生新檔案、不得覆蓋舊檔、舊檔標示為 INACTIVE / ARCHIVED。:contentReference[oaicite:18]{index=18}
- 凡標示為 ACTIVE 的 doc_key 文件：
  - 禁止刪減
  - 禁止重寫造成內容遺失
  - 禁止摘要取代全文
  - 僅允許：新章節／新子節／新附錄／新案例 :contentReference[oaicite:19]{index=19}

---

（End of 03_ai_decision_scope_boundaries__AI決策權限邊界）
