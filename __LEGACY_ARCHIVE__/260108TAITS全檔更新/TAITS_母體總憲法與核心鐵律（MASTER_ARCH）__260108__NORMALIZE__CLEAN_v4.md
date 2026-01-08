# TAITS_母體總憲法與核心鐵律（MASTER_ARCH）

## 文件頭（Document Header）

- doc_key：MASTER_ARCH  
- 治理等級：A（母體／憲法級｜母體總憲法與核心鐵律）  
- 適用範圍：TAITS 全系統（最高架構公理／不可違反鐵律／裁決序位／系統邊界與權責）  
- 版本狀態：ACTIVE（最大完備覆蓋版）  
- 版本日期：2026-01-08（Asia/Taipei）  
- 基線日期：2026-01-08（Asia/Taipei）  
- 裁決序位：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV  

---

## 0. 文件地位聲明（不可省略）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）之最高母體憲法**，  
其法律位階高於所有模組、策略、流程、Agent、UI、執行層與 AI 行為。

**任何文件、程式、AI 回覆、Agent 推論，只要與本文件衝突：**
**一律以本文件為準，且視衝突方為「治理違規」。**

---

## 1. 不可動搖的核心排序（Supreme Priority Order）

TAITS 全系統之最終排序如下（不可更動）：

Human Sovereignty
→ Risk & Compliance (Supreme Veto)
→ Regime
→ Evidence
→ Strategy
→ Execution
→ Performance / Optimization
### 1.1 強制解釋
- **人類主權**：AI 永不具最終決策權  
- **風險與合規**：可否決任何高績效策略  
- **Regime**：高於任何單一訊號或模型  
- **策略**：永遠只是「建議與假設」  
- **績效**：不能為任何違規辯護  

---

## 2. 人類主權（Human Sovereignty）鐵律

### 2.1 定義
TAITS 為 **Human-in-the-Loop 強制系統**。

### 2.2 禁止事項
- AI 不得：
  - 自動下單
  - 自動解除風控
  - 自動修改治理規則
- 不存在「完全無人值守交易」

### 2.3 違規判定
若任何模組、Agent、Prompt、文件出現：
- 「AI 自主決策」
- 「自動交易」
- 「系統自行判斷即可」

👉 **直接判定為 A 級治理違規**

---



### 2.4 HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：治理狀態/最大完備＋累積式更新/Gate 不得阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 留痕、HASH_MANIFEST、CHANGELOG）。

---

### 2.5 人類主權之最小落地口徑（可稽核、可回放）

#### 2.5.1 定義（在本母法中的落地口徑）
- **人類最高決策者**：TAITS 專案之產品負責人／架構裁決者（Human Authority / Architecture Arbiter）。  
- **明確命令**：可被稽核回放之明示指令（須具備：發令者身份、時間戳、命令內容、引用 doc_key/章節定位、目的與風險告知）。  

#### 2.5.2 原則（不可阻擋，但必須留痕）
1) 當存在「人類最高決策者的明確命令」時：  
   - 系統之任何文件條款、Gate/Reason Code、Agent/AI 內規，**不得以程序性理由阻止命令生效**。  
   - 但必須以制度化方式完成：告警呈現、風險揭露、稽核留痕、可回放紀錄。  
2) 當不存在「明確命令」時：  
   - 系統依本母法既有之治理序位運作；風險與合規否決機制維持既有語義（可 STOP/RETURN/BLOCK）。  

#### 2.5.3 與「Risk & Compliance（Supreme Veto）」之關係（消歧義）
- 本母法既有之 **Risk & Compliance 最高否決權**，在「無人類明確命令」情境下保持完全效力。  
- 在「有人類最高決策者明確命令」情境下：  
  - Risk/Compliance 必須輸出完整否決理由與風險告知（可升級至最高等級告警），  
  - 但其結果 **不得轉為阻止人類明確命令之執行**；改以「強制揭露＋雙重確認＋全紀錄」承接。  

#### 2.5.4 最小留痕欄位（可直接貼用）
凡屬人類最高決策者之明確命令，至少需記錄：

- authority_role = Human Sovereignty（人類最高決策者）  
- authority_actor = <姓名/識別>  
- authority_time = <Asia/Taipei 時戳>  
- authority_command = <命令全文>  
- ref_doc_key = <DOC_KEY>  
- ref_section = <§ / Heading Path>  
- ref_purpose = <用途：rule_change / gate_override / deploy_decision / etc.>  
- risk_disclosure = <Risk/Compliance 提示摘要與引用>  
- acknowledgement = <確認紀錄（例如雙重確認）>
---


## 3. Risk / Compliance 最高否決權（Supreme Veto）

### 3.1 否決權定義
Risk / Compliance 擁有跨層、跨模組、跨策略的**最高即時否決權**。

### 3.2 否決不需理由充分性
- 不需解釋績效
- 不需證明錯誤
- 只需符合風險或合規疑慮

### 3.3 禁止事項
- 不得以「長期績效」對抗否決
- 不得以「回測成功」解除否決

---

## 4. Regime 高於一切單一訊號

### 4.1 定義
Regime = 市場狀態母判斷（非策略、非指標）

### 4.2 強制規則
- Regime 不符 → 策略 **不得啟用**
- Regime 衝突 → 系統必須：
  - 降級策略
  - 或完全 BLOCK

### 4.3 禁止事項
- 不得「忽略 Regime」
- 不得「用策略反推 Regime」

---

## 5. Evidence 第一原則（Evidence-First）

### 5.1 定義
所有判斷必須來自 **可回放、可審計、可追溯** 的 Evidence。

### 5.2 Evidence 最低標準
- 來源明確
- 時點可重建
- 不可僅存在於記憶體

### 5.3 禁止事項
- 傳聞
- 主觀感覺
- 無法重現的經驗敘事

---

## 6. Strategy ≠ Execution（策略與下單嚴格分離）

### 6.1 Strategy 定位
Strategy 只允許輸出：
- proposal
- context
- risk_adjust
- avoid / observe

### 6.2 禁止事項
- 直接輸出：
  - 價格
  - 數量
  - 買賣方向
- 不得直連任何下單模組

---

## 7. Structure ≠ Strategy（結構不可升格）

### 7.1 結構系統定位
- 纏論 / 結構 / 型態  
  → **僅為結構描述語法**

### 7.2 結構允許輸出
- structure_state
- completeness_score
- conflict_flag
- warning

### 7.3 明確禁止
- 結構 = 買點
- 背離 = 反轉
- 中樞 = 突破

---

## 8. Annotation 永遠為 Non-Binding

### 8.1 定義
Annotation 僅供人類理解與語意對齊。

### 8.2 禁止事項
- Annotation 升格為條件
- Annotation 被程式解析
- Annotation 被用於回測或實盤

---

## 9. 最大完備＋累積式更新 演進鐵律（不可逆）

### 9.1 定義
TAITS 只允許「擴充」，不允許「刪減或弱化」。

### 9.2 不可逆條款
- 治理條款不可刪
- 否決權不可弱化
- 人類主權不可調降

---

## 10. AI 行為邊界（AI Behavior Boundary）

### 10.1 AI 允許行為
- 整理
- 分析
- 建議
- 風險提示

### 10.2 AI 禁止行為
- 自行定義新策略類型
- 自行修改治理文件
- 自行假設可執行性

---

## 11. 違規等級與處置（Enforcement）

### 11.1 違規等級
- **A 級**：觸碰人類主權、風控否決、治理鐵律
- **B 級**：越權推論、策略下單化
- **C 級**：文件簡化、語意誤導

### 11.2 處置原則
- A 級：立即停止、回滾、封鎖
- B 級：降級、重審
- C 級：文件修正

---

## 12. 與其他文件之關係（Hierarchy）

- MASTER_CANON
- ARCH_FLOW
- RISK_COMPLIANCE
- EXECUTION_CONTROL
- STRATEGY_UNIVERSE
- STRATEGY_FEATURE_INDEX
- UI_SPEC
- DOCUMENT_INDEX

### 12.1 統一裁決：清單/數量一律視為 Snapshot（不裁決）

凡本文件（MASTER_ARCH）內部出現之：
- 「目前共有 X 份文件」  
- 「ACTIVE 文件數 = X」  
- 任何列舉文件清單、推薦載入清單、快捷載入集合  

- Snapshot（歷史快照/導覽用途）  
- **不具治理裁決效力**（不得用以判定 ACTIVE、doc_key、治理等級、覆蓋關係）

### 12.2 唯一裁決來源：Index Gate First

凡涉及：
- ACTIVE 文件集合  
- doc_key 合法性  
- 版本有效性（version_date / 治理狀態）  

一律以 **DOCUMENT_INDEX 的 Authoritative Index 表格**裁決為準。

---
## 13. 最終鎖定聲明（Final Lock）

**本文件一經標示為 ACTIVE + LOCKABLE，  
即視為 TAITS 永久治理母憲法。**

任何未來 AI、Agent、新對話：
- 不得重新解釋
- 不得簡化
- 不得繞過

---

（TAITS_MASTER_ARCHITECTURE｜母體總憲法與核心鐵律｜最大完備版 完）
---

## G0. 適用範圍（Hard Boundary）

1) **引用端身份**：doc_key / 治理等級 bucket / ACTIVE 狀態之裁決來源固定回歸 DOCUMENT_INDEX。  
2) **子級標籤**：S / B+ / C+ 等字樣一律視為顯示標籤（Label），不構成新的治理等級 bucket。  
3) **資料治理別名封口**：凡出現「DATA_UNIVERSE」字樣，一律視為 alias（概念名詞），治理引用 doc_key 必須回歸 DATA_SOURCES。  
4) **最小可稽核引用格式**：補上統一模板，避免 Gate 因引用缺口而 BLOCK/RETURN。  

- 不變更 Canonical Flow（L1–L11）任何順序/語義（MASTER_CANON 為準）  
- 不新增任何新 doc_key、不新增新治理位階、不調整覆蓋規則  
- 不新增策略內容、不新增下單規範、不改寫風控/合規否決條款  
- 不為任何缺失資訊進行「模型推測補完」

---

## G1. Index Gate 身份裁決（doc_key / 等級 / ACTIVE 的唯一裁決來源）

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

## G5. 最終宣告（治理狀態 v1.0）

---

### 治理補強—人類主權條款落地（HFI/Human Authority）
對齊上位裁決：DOCUMENT_INDEX（A+）之「HUMAN SOVEREIGNTY｜最高裁決置頂條款」

## 稽核區塊（Audit Section｜非正文）

### 1) 變更清單（Changelog）
- 2026-01-08：NORMALIZE（正文乾淨／無重複／最大完備）
  - 收斂檔首雙表頭為單一「文件頭（Document Header）」
  - 移除補丁式段落（含舊檔名/助記規則/治理補強標題），避免正文污染與混讀
  - 維持母法鐵律、硬邊界與裁決序位；L1–L11 語義以 MASTER_CANON 為唯一正文來源（本檔不重複定義）
  - 移除非必要之標籤/助記型敘述（正文乾淨）
  - 僅保留稽核四件套（無 Legacy Snapshot）

### 2) 指紋清單（Hash Manifest）
- HASH_RULE：SHA-256（UTF-8，LF；Body=本檔「稽核區塊」之前全文，含結尾換行）
- BODY_SHA256：0040cfac54834f198d02b14bb8805bc842adc6dc14312aa3592581a242c93d70

### 3) 適用範圍（Scope）
- scope_doc_key：MASTER_ARCH
- scope_change_type：NORMALIZE（去重收斂／結構重排／不新增投資或交易建議）
- scope_excludes：稽核區塊以外不得殘留補丁式語句或對話痕跡

### 4) 稽核交接（Audit Hand-off）
- handoff_to：VERSION_AUDIT（如需落帳）
- handoff_notes：本次變更為文件正常化；裁決序位不變（DOCUMENT_INDEX → MASTER_ARCH → AI_GOV）

