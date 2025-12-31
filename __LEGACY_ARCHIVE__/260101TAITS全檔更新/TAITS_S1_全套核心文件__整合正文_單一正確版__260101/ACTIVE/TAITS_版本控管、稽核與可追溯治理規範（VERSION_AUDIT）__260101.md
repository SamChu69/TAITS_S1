# TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）


版本日期：2026-01-01
版本狀態：ACTIVE


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

## S1｜整合正文更新稽核承接（本次交付）

- 本文件承接本次「S1｜單一正確版｜整合正文」全套核心文件更新之稽核與可追溯要求。
- 核心原則：**正文只保留單一有效口徑**；所有歷史/補丁/整併註記/舊標記移出正文，改存於 `ARCHIVE_ORIGINALS/`；其移除摘要與指紋對帳存於 `AUDIT/`。

## HFI Ledger｜人類明確命令留痕（Mandatory）

- hfi_id：
- authority_actor：
- authority_time（Asia/Taipei）：
- scope：
- action：
- intent：
- acknowledgement：
- affected_docs（doc_key 清單）：
- apply_order：
- hash_manifest_ref：
- changelog_ref：

## S1 Package Ledger｜本次同步更新清單（摘要）
- TAITS_AI_行為與決策治理最終規則全集__260101.md  （source=TAITS_AI_行為與決策治理最終規則全集__251231.md｜sha256_out=7ef6548a8fa9…｜removed_chars=16092）
- TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260101.md  （source=TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__251231.md｜sha256_out=42143eea072e…｜removed_chars=182929）
- TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260101.md  （source=TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251231.md｜sha256_out=92f1bf5e5d1c…｜removed_chars=10828）
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__260101.md  （source=TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__260101.md｜sha256_out=31a4b3463e7b…｜removed_chars=5577）
- TAITS_全系統架構總覽（FULL_ARCH）__260101.md  （source=TAITS_全系統架構總覽（FULL_ARCH）__251231.md｜sha256_out=941b1a2f019d…｜removed_chars=28205）
- TAITS_系統架構與流程細化說明（ARCH_FLOW）__260101.md  （source=TAITS_系統架構與流程細化說明（ARCH_FLOW）__251231.md｜sha256_out=0e99267e98b9…｜removed_chars=15487）
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__260101.md  （source=TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__251231.md｜sha256_out=9f2a65dcb75d…｜removed_chars=24696）
- TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__260101.md  （source=TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__251231.md｜sha256_out=acffaffe299f…｜removed_chars=16256）
- TAITS_交易執行與控制規範（EXECUTION_CONTROL）__260101.md  （source=TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251231.md｜sha256_out=176671ab7379…｜removed_chars=17464）
- TAITS_使用者介面與人機決策規範（UI_SPEC）__260101.md  （source=TAITS_使用者介面與人機決策規範（UI_SPEC）__251231.md｜sha256_out=a01017ac3b3d…｜removed_chars=16941）
- TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__260101.md  （source=TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__251231.md｜sha256_out=e78176ae3459…｜removed_chars=20895）
- TAITS_本地執行與運算環境規範（LOCAL_ENV）__260101.md  （source=TAITS_本地執行與運算環境規範（LOCAL_ENV）__251231.md｜sha256_out=861e821d4cd5…｜removed_chars=5518）
- TAITS_資料來源全集（DATA_SOURCES）__260101.md  （source=TAITS_資料來源全集（DATA_SOURCES）__251231.md｜sha256_out=8128955cc74e…｜removed_chars=68392）
- TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260101.md  （source=TAITS_TWSE交易規則參考彙編（TWSE_RULES）__251231.md｜sha256_out=a88ad40a70c2…｜removed_chars=14768）
- TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__260101.md  （source=TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251231.md｜sha256_out=de1f9df3c343…｜removed_chars=70441）
- TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__260101.md  （source=TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251231.md｜sha256_out=3ccfac973cb2…｜removed_chars=53908）
- TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__260101.md  （source=TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__251231.md｜sha256_out=e78176ae3459…｜removed_chars=9208）
- README__260101.md  （source=README__251231.md｜sha256_out=4673fdaea81a…｜removed_chars=11512）
- TAITS_PROJECT_PROMPT__260101.md  （source=TAITS_PROJECT_PROMPT__251231.md｜sha256_out=a5daa6c7d2fe…｜removed_chars=12028）
- TAITS｜程式開發流程定錨文件（Unified Process Anchor）__260101.md  （source=TAITS｜程式開發流程定錨文件（Unified Process Anchor）__251231.md｜sha256_out=e18f04256250…｜removed_chars=32134）
- TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260101.md  （source=TAITS_GOVERNANCE_STATE__FREEZE_v1.0__251231__單一檔.md｜sha256_out=f16548ce37e7…｜removed_chars=0）

## HASH_MANIFEST｜全檔指紋清單（本包）

- README__260101.md: 4673fdaea81a1b35bf2cb7eebaa26a67444ac96ecf1c069dbfd02d4319e02b67
- TAITS_AI_行為與決策治理最終規則全集__260101.md: 7ef6548a8fa9fc05890d6011d79cf1413517c3d5bc44c4c16f628e5d089085ac
- TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260101.md: f16548ce37e79071ecd141d3d843ca7f42c6851ab64a0bb422aafae722c72ec6
- TAITS_PROJECT_PROMPT__260101.md: a5daa6c7d2fea0e4e98ffbdce56276963cd5201d88e932972cbb13dce51163e2
- TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260101.md: a88ad40a70c22ea98ce6e117be3850f677a48960926ece42f064221a031e53c8
- TAITS_交易執行與控制規範（EXECUTION_CONTROL）__260101.md: 176671ab737979faba4da9d05cc56b14587962b2085a8d5544474b96cf4e8ccf
- TAITS_使用者介面與人機決策規範（UI_SPEC）__260101.md: a01017ac3b3d25419ed43aed03b5c9ebee2cabeee214643ba181fd4407be6718
- TAITS_全系統架構總覽（FULL_ARCH）__260101.md: 941b1a2f019d5dc14749f7fca6fabc5b2df2b8af72d9e605be760c6ac1017252
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__260101.md: 31a4b3463e7bc51d5f0fd1754ef8cfc24a28a8c55fd377efc0a2877334967610
- TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260101.md: 42143eea072e43a0f6f9d15292833ac93c083e774af4a6183ad8066c39d5c8d3
- TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__260101.md: e78176ae3459bd339ff083372213f8d53bffe75ad108f6b352eddf7aa5bff3c0
- TAITS_本地執行與運算環境規範（LOCAL_ENV）__260101.md: 861e821d4cd5c58589c533abbbbea4ef74dde60b60641710eac0586ce2af5734
- TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260101.md: 92f1bf5e5d1c0b08f50e341c6683c1f45d7ff4ad344b459ec22cd96fa0e26cec
- TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__260101.md: acffaffe299f3a5db89b016f4d7539dc9f7cda5e99e19cad09ecb0c1efd6285f
- TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__260101.md: de1f9df3c34351503faf6ff44d798fffe1c7700dd3e2785618a7be7a4e17f5eb
- TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__260101.md: 3ccfac973cb2dfa2eb44a17774a43922b9789a9192e993b12949608e4e3014fd
- TAITS_系統架構與流程細化說明（ARCH_FLOW）__260101.md: 0e99267e98b9d219d9f897621f496751b0da83420af674526fed20289ae19275
- TAITS_資料來源全集（DATA_SOURCES）__260101.md: 8128955cc74edd0a112517caa795d58f2b3d78306218378156a30645e2c369eb
- TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__260101.md: e78176ae3459bd339ff083372213f8d53bffe75ad108f6b352eddf7aa5bff3c0
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__260101.md: 9f2a65dcb75dbe35ec372afdc605d6158988516d87a333329ec17c0f045bcb73
- TAITS｜程式開發流程定錨文件（Unified Process Anchor）__260101.md: e18f042562509799177b18bfe247190fe92671c6b4aa4c582fd3af7eb71c8fef
