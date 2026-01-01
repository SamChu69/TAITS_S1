# TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260101.md

doc_key：DOCUMENT_INDEX  
治理等級：A+（Authoritative Index & Override Gate｜唯一有效索引）  
適用範圍：TAITS 全系統（TWSE / TAIFEX；Research / Backtest / Simulation / Paper / Live）  
版本狀態：ACTIVE（本文件為裁決依據；可演進但必須可追溯）  
版本日期：2026-01-01

---

## 全局定錨｜單一口徑（S1）

### 1) 人類最高決策者主權（SOVEREIGNTY）
- TAITS 之唯一最高主權屬於人類最高決策者（產品負責人／架構裁決者）。
- 任何治理閘門、程序規則、Agent、文件等級不得凌駕人類主權；不得以程序性理由阻止人類明確命令（HFI）之生效。
- 風險與合規（Risk/Compliance）在無人類明確命令時可否決；在有人類明確命令時必須輸出完整風險揭露與替代方案，並以「強制揭露＋確認＋全紀錄」承接；不得以程序卡死更新或裁決承接。

### 2) L9–L11 最終語義（跨文件一致）
- **L9（投資報告層）**：可追蹤、可更新、可標的化投資報告；必含數據、圖形、條件式進出場建議（非指令）、風險敘述、追蹤欄位（狀態/更新時間/依據來源），並支援事件驅動滾動更新。
- **L10（人類裁決與交易決策層）**：由人類最高決策者裁決「不動作/回測/模擬/半自動/全自動」等；任何交易型態皆以 L10 明確裁決為準。
- **L11（全層工程稽核回放層）**：對 L1–L11 全層輸入/處理/輸出/裁決/執行鏈路留痕，供人類與工程端可讀、可查、可回放；**L11 非下單層**。

### 3) HFI｜人類明確命令（可執行觸發）
- 格式：`HFI: <scope> | <action> | <intent> | <acknowledgement>`
- 有效 HFI 存在時：Freeze/Only-Add/Gate **不得**阻擋 scope 範圍內之更新/覆寫/重排版；並必須同步產生稽核承接（VERSION_AUDIT 落帳、CHANGELOG、HASH_MANIFEST）。

---

## 0. 文件定位（Why DOCUMENT_INDEX Is Power）

本文件為 TAITS 之「治理有效文件索引」與「裁決覆蓋總閘（Index Gate）」：

- **索引裁決**：任何文件、章節、條文若未被本表納入「治理有效清單」，不得被當作治理依據。
- **覆蓋裁決**：當多份文件之表述彼此衝突或產生張力時，本文件定義「覆蓋規則」與「衝突裁決程序」，並提供可機器化檢核的引用格式。
- **一致化定錨**：本文件負責鎖定跨文件一致之語義口徑（尤其 L9–L11 定錨、doc_key 合法性、治理等級分桶）。

---

## 1. 治理鐵律（Hard Laws）

### 1.1 A+ 母法不可被覆寫
A+ 文件（含本文件）為最高裁決來源；任何 A/B/C 文件不得改寫其裁決。

### 1.2 Index 裁決（未列入＝無效）
任何「規則、流程、制度、策略、操作指南、工程文件」若不在本文件 §5 的 Authoritative Index 內：
- 不得主張治理效力
- 不得作為 Gate PASS/VETO、下單、合規裁決、版本有效性判定之依據

### 1.3 上位覆蓋下位（無需協調）
覆蓋分桶僅有四級：**A+ > A > B > C**。  
任何 B+/C+、S 等字樣僅屬**顯示標籤**，不構成新的治理等級。

### 1.4 Only-Add（只增不減）
在未有有效 HFI 前提下，ACTIVE 文件的演進以 Only-Add 為常態；禁止偷換語義、弱化邊界、刪除否決鏈或縮減欄位。

### 1.5 無稽核＝未發生（Audit Supremacy）
任何影響治理有效性的更新（新增/改狀態/改覆蓋/改裁決程序）必須可追溯：  
至少包含 CHANGELOG + HASH_MANIFEST + Scope + Audit Hand-off（交由 VERSION_AUDIT 落帳）。

---

## 2. doc_key 制度（唯一性、可追溯、不可偽造）

### 2.1 doc_key 的法定位
- `doc_key` 是文件治理身份（Identity），高於檔名與路徑。
- 一切引用、稽核、回放、Gate 檢核以 doc_key 為主鍵。

### 2.2 doc_key 唯一性（Hard Gate）
- 任一治理有效文件必須擁有且僅擁有一個 doc_key。
- 同一 doc_key 在同一時間只能有一個 ACTIVE 版本（除非本文件另有明文允許之多版本並存機制；默認不允許）。

### 2.3 doc_key 與檔名（Filename）的關係
- 檔名是可讀性與版本標示；doc_key 才是治理身份。
- 引用端不得以「檔名近似」推定 doc_key；必須明示 doc_key。

---

## 3. 治理等級（Governance Level）與裁決力

### 3.1 等級分桶（唯一有效）
- **A+**：最高母法與索引裁決（AI_GOV、DOCUMENT_INDEX）
- **A**：憲法級／主權級／最高否決權與執行控制（MASTER_ARCH、MASTER_CANON、RISK_COMPLIANCE、EXECUTION_CONTROL、GOVERNANCE_STATE_*）
- **B**：制度/規格/架構/資料/策略宇宙（FULL_ARCH、ARCH_FLOW、DATA_SOURCES…）
- **C**：操作/教學/README（不得主張治理裁決）

### 3.2 覆蓋規則（Override Rules）
- A+ 覆蓋 A/B/C  
- A 覆蓋 B/C  
- B 覆蓋 C  
- 同桶衝突：依 §6 衝突裁決程序處置（保守處置優先）

### 3.3 顯示標籤（Label）之法律定位
- `S`、`B+`、`C+`、`LOCK_CANDIDATE` 等字樣：僅為顯示/完備度/嚴格度標籤，不得改寫 §3.2 覆蓋規則。
- 若其他文件以箭頭字串宣稱覆蓋順位（例如「X → Y → Z」）：一律視為助記，不得取代本節。

---

## 4. 版本狀態（Version Status）與有效性

### 4.1 狀態定義（最小集合）
- **ACTIVE**：治理有效，可被引用裁決
- **DEPRECATED**：仍可讀取/回放，但不得作為新裁決依據（除非另有明文）
- **RETIRED**：封存，只供歷史回放；不得作為任何裁決依據

### 4.2 ACTIVE 唯一性（同 doc_key）
- 同一 doc_key 同時只能存在一個 ACTIVE。
- 任何「替換 ACTIVE 指向」必須在 VERSION_AUDIT 留痕，並更新本文件 §5 的索引表。

---

## 5. TAITS 治理有效文件清單（Authoritative Index｜唯一有效）

原則：**不在本清單內＝不具治理效力。**  
註：本表之「治理等級」以 §3 分桶為準；B+/C+ 等僅作顯示標籤。

### 5.1 A+（Supreme Canon）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_AI_行為與決策治理最終規則全集__260101.md | AI_GOV | A+ | ACTIVE | 2026-01-01 | 全系統 AI 行為與決策治理母法 |
| TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260101.md | DOCUMENT_INDEX | A+ | ACTIVE | 2026-01-01 | 文件位階裁決最高層（本文件） |

### 5.2 A（Constitutional / State）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260101.md | MASTER_ARCH | A | ACTIVE | 2026-01-01 | 人類主權、鐵律、三權分立、邊界與否決鏈 |
| TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__260101.md | MASTER_CANON | A | ACTIVE | 2026-01-01 | L1–L11 Canonical Flow 最高總綱與全資訊體系 |
| TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__260101.md | RISK_COMPLIANCE | A | ACTIVE | 2026-01-01 | 最高否決權（PASS/VETO）、理由碼、合規保守處置 |
| TAITS_交易執行與控制規範（EXECUTION_CONTROL）__260101.md | EXECUTION_CONTROL | A | ACTIVE | 2026-01-01 | 執行控制、Token、Kill Switch、Human-in-the-Loop |
| TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260101__單一檔.md | GOVERNANCE_STATE_FREEZE_V1 | A | ACTIVE | 2026-01-01 | 治理狀態宣告：Freeze v1.0 生效（對變更施加門檻） |

### 5.3 B（Governance / Spec）
| 文件名稱（檔名） | doc_key | 治理等級 | 顯示標籤 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|---|
| TAITS_全系統架構總覽（FULL_ARCH）__260101.md | FULL_ARCH | B |  | ACTIVE | 2026-01-01 | 橫向模組 × 縱向層級架構地圖 |
| TAITS_系統架構與流程細化說明（ARCH_FLOW）__260101.md | ARCH_FLOW | B | B+（顯示） | ACTIVE | 2026-01-01 | 流程層細化（承接 MASTER_CANON），不得改寫 Canonical |
| TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__260101.md | GOVERNANCE_GATE_SPEC | B |  | ACTIVE | 2026-01-01 | Gate 規則：完整性、引用合法性、拒絕與退回語義 |
| TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）__260101.md | VERSION_AUDIT | B |  | ACTIVE | 2026-01-01 | 變更帳本、回放、稽核證據、可追溯治理 |
| TAITS_資料來源全集（DATA_SOURCES）__260101.md | DATA_SOURCES | B |  | ACTIVE | 2026-01-01 | 官方優先、來源追溯、Fallback、Provenance |
| TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260101.md | TWSE_RULES | B |  | ACTIVE | 2026-01-01 | 交易規則參考、觸發映射、制度快照 |
| TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__260101.md | STRATEGY_UNIVERSE | B |  | ACTIVE | 2026-01-01 | 策略白名單、生命週期、輸出契約；策略≠下單 |
| TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__260101.md | STRATEGY_FEATURE_INDEX | B |  | ACTIVE | 2026-01-01 | 特徵/因子定義與審計；禁止信號化偷換 |
| TAITS_使用者介面與人機決策規範（UI_SPEC）__260101.md | UI_SPEC | B |  | ACTIVE | 2026-01-01 | UI 決策可視化、否決呈現、Decision Trace |
| TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__260101.md | DEPLOY_OPS | B |  | ACTIVE | 2026-01-01 | 部署、回滾、停機、Runbook、Live 運作制度 |

### 5.4 C（Operational / Guide｜不具治理裁決力）
| 文件名稱（檔名） | doc_key | 治理等級 | 版本狀態 | 版本日期 | 說明 |
|---|---|---|---|---|---|
| TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__260101.md | BEGINNER_GUIDE | C | ACTIVE | 2026-01-01 | 新手操作引導；不得新增治理權力 |
| README__260101.md | README | C | ACTIVE | 2026-01-01 | 專案總覽與使用方式；不得越權 |
| TAITS_PROJECT_PROMPT__260101.md | PROJECT_PROMPT | C | ACTIVE | 2026-01-01 | 專案對話啟動與行為規範（操作級） |
| TAITS_本地執行與運算環境規範（LOCAL_ENV）__260101.md | LOCAL_ENV | C | ACTIVE | 2026-01-01 | 金鑰隔離、環境檢核、敏感資料禁止入 repo |

> 註：上述清單合計 **21 份治理有效文件**（依 TAITS 專案已生效之核心治理文件集合）。任何未列入者不得主張治理效力。

---

## 6. 衝突裁決程序（Conflict Resolution Procedure）

當兩份（或多份）文件對同一事項產生衝突、張力、或可疑的語義偷換時，必須依序處置：

1) **確認 doc_key 合法性**：引用文件必須存在於 §5。  
2) **確認治理分桶**：依 §3 判定 A+ / A / B / C。  
3) **套用覆蓋規則**：依 §3.2 直接覆蓋；無需協調。  
4) **同桶衝突**：採保守處置（Fail Closed），並：
   - 退回（RETURN）要求補足引用格式（見 §7）或證據鏈
   - 或要求由人類最高決策者以 L10 裁決承接  
5) **全程留痕**：衝突裁決過程必須能在 L11 回放；必要時由 VERSION_AUDIT 落帳。

---

## 7. 引用合法性（Citation Legality）與最小格式（Hard Gate）

任何模組／AI／人類若聲稱「依據文件」，必須同時提供：

- `doc_key`
- `版本日期`（YYYY-MM-DD 或檔名日期碼）
- `章節定位`（如：§3.2 / 章-節-項）
- `引用目的`（用於：否決／流程／UI 呈現／部署裁決／資料來源裁決等）

缺任一項：**引用無效**。  
引用無效時，只允許輸出「缺口清單」與「如何補足」，不得輸出裁決性結論（PASS/VETO/APPROVE/ACTIVE 等）。

---

## 8. 模組可引用範圍矩陣（Authority Usage Matrix｜防越權）

> 本節為「引用邊界的摘要性矩陣」，目的在於降低越權與新舊混讀風險；不創造新的覆蓋規則，覆蓋裁決仍以 §3–§7 為準。

| 模組/角色 | 可引用（作為裁決依據） | 不可引用（不得作為裁決依據） | 備註 |
|---|---|---|---|
| Index / Governance Gate | A+ / A / B / C（但 C 僅作操作說明） | 任何未列入 §5 的文件 | Gate 以 §7 引用格式機器化檢核 |
| Risk/Compliance（L7） | A+ / A / B（含 TWSE_RULES、DATA_SOURCES） | 任何 C 作為否決依據 | 最高否決權以 RISK_COMPLIANCE 為準 |
| Execution Control（執行控制） | A+ / A（EXECUTION_CONTROL、RISK_COMPLIANCE）＋必要之 B（如 DEPLOY_OPS） | 任何策略文件作為送單依據 | 送單行為須符合 EXECUTION_CONTROL；L11 非下單層 |
| Strategy / Research（L8/L9） | DATA_SOURCES / STRATEGY_UNIVERSE / STRATEGY_FEATURE_INDEX / ARCH_FLOW（僅流程語義） | 以 EXECUTION_CONTROL 作為「我可以下單」依據 | 策略 ≠ 下單；提案需可被 L7/L10 否決 |
| UI / Human Decision（L10） | UI_SPEC / RISK_COMPLIANCE / EXECUTION_CONTROL / MASTER_CANON | 任何 C 作為裁決法源 | L10 才是交易型態裁決層 |
| Deploy/Ops | DEPLOY_OPS / VERSION_AUDIT / GOVERNANCE_GATE_SPEC | 以 README/教學文件作為制度改寫依據 | 變更需可回滾、可停機、可稽核 |
| Onboarding / Beginner | BEGINNER_GUIDE / README | 任何治理裁決 | 僅能教怎麼做，不得定義「做了就算通過」 |

---

## 9. 治理狀態（GOVERNANCE_STATE）之索引規則

- 治理狀態文件以 `doc_key = GOVERNANCE_STATE_*` 命名族群管理，屬 A 分桶。  
- 任一時點治理狀態以「唯一 ACTIVE」為準。  
- 任何狀態切換（例如 Freeze → Unfreeze）必須：
  1) 新增一份新的 GOVERNANCE_STATE_* 文件（不得覆寫舊狀態文件）  
  2) 納入本文件 §5  
  3) 以 VERSION_AUDIT 留痕（包含變更原因、影響範圍與回滾策略）

---

## 10. 非治理有效文件（Non-Authoritative｜允許存在但不得裁決）

下列文件可作為工程協作、開發節奏與工作定錨之參考，但 **不具治理裁決力**，不得用於：
- 宣稱文件位階、覆蓋順序、ACTIVE 指向
- Gate PASS/VETO
- Risk/Compliance 否決法源
- Execution Control 下單授權

### 10.1 常見工程支援文件（示例）
- TAITS｜程式開發流程定錨文件（Unified Process Anchor）__260101.md（建議 doc_key：PROCESS_ANCHOR；**不入 §5**）

---

## 11. 最終宣告（Final Declaration）

- **Index 不是參考，而是裁決**：文件合法性、位階、覆蓋、引用格式、衝突處置，皆以本文件為唯一入口。
- **策略 ≠ 下單**、**Agent ≠ 策略**、**AI ≠ 唯一真理**：任何企圖以流程或工具繞過 L7/L10/L11 邊界者，一律視為越權。
- **L11 非下單層**：L11 的職責是全鏈路留痕與可回放，不得被偷換為「下單決策層」。

---

# 稽核留痕（Audit Section｜不屬正文）

> 本段落為「本次融合更新」之留痕；不構成新增治理規則。  
> 如需獨立稽核檔，允許整段剪貼為 `DOCUMENT_INDEX__260101__AUDIT.md`，正文仍以本檔案上半部（§0–§11）為準。

## A. Scope（適用範圍）
- scope_doc_key: DOCUMENT_INDEX
- scope_files_modified: 僅本文件（覆寫重排版產生單一正文）
- downstream_impact: 所有 Gate / Audit / Loader / UI / Engineering 讀取「治理有效清單」「覆蓋規則」「引用格式」之行為

## B. Changelog（變更清單）
1) 產出「單一正確正文」：移除舊版補丁樣式段落（Addendum/Appendix/Freeze 註記等）之混讀風險，將有效內容整合為 §0–§11 的連貫正文。
2) Authoritative Index（§5）歸一：以 2026-01-01 之現行檔名重建清單；治理分桶一致化為 A+/A/B/C，並明確定義 B+ 僅為顯示標籤。
3) doc_key／引用合法性機器化：補齊最小引用格式（§7）與衝突裁決程序（§6），以支援 Gate 自動檢核與 L11 回放。
4) 將「工程支援文件」明確降權：集中於 §10（Non-Authoritative），禁止越權引用造成新舊混讀。

## C. Hash Manifest（指紋清單）
- hash_algo: SHA-256
- hash_target: 正文區段（§0–§11，不含本章「稽核留痕」）
- hash_value_sha256: 2659bdbc4c7b17ad6cfdd406260f115f64ba47728371660861dd56e3be6f401d

## D. Audit Hand-off（裁決承接）
請將以下條目以「單一交易」落入 `VERSION_AUDIT`（doc_key=VERSION_AUDIT）：

- change_id: DI-FUSION-260101-0001
- change_type: FUSION_UPDATE_REWRITE
- target_doc_key: DOCUMENT_INDEX
- effective_date: 2026-01-01
- rationale: 依 HFI 授權進行融合更新，產出單一正確正文，消除新舊混讀風險，並完成索引分桶一致化與引用合法性強化。
- artifacts:
  - changelog_ref: 本文件「稽核留痕」§B
  - hash_manifest_ref: 本文件「稽核留痕」§C
- governance_checklist:
  - L9/L10/L11 semantic anchor preserved: YES
  - override rules unchanged: YES（A+ > A > B > C）
  - deleted_information: NO（僅重排/整併/去混讀）
