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

## S1｜整合正文同步更新（本次交付）

- `ACTIVE/` 為唯一可讀正文版本；已移除所有建置註記/舊標記/附錄/補丁全文。
- `ARCHIVE_ORIGINALS/` 保留來源檔原文全文（追溯用，不參與正文裁決）。
- `AUDIT/` 保存移除摘要與 HASH_MANIFEST（稽核用）。

## HASH_MANIFEST｜ACTIVE 全檔指紋（本包）

- README__260101.md: c081257c457037944504b546b82f20630a5b2320a88f1b57a49ef1de812f0f88
- TAITS_AI_行為與決策治理最終規則全集__260101.md: 485e02374ba066bdd3e1dcd81d32161bab63e0ca5ab640fde4b085941125b059
- TAITS_GOVERNANCE_STATE__FREEZE_v1.0__260101.md: 1bb86bfefbe4ba809516c1c3a6a07d4bb7aae6a4a94aaa1fae880f633c5644c2
- TAITS_PROJECT_PROMPT__260101.md: 7c3f94381aa38c1a4c48d65759b1fbe9b6231d866537663beb0239f7230aed09
- TAITS_TWSE交易規則參考彙編（TWSE_RULES）__260101.md: 80bbfd4a258eee54b164a3ed70c608191cb0d4984326b5054164cd8b89d9b5f6
- TAITS_交易執行與控制規範（EXECUTION_CONTROL）__260101.md: 433a4bbc3b6dd45ad9c2dc4d387fbece9c13d006a74d55b00ccf6e353aaeaed0
- TAITS_使用者介面與人機決策規範（UI_SPEC）__260101.md: e0e55735645ce7d9e11d2c31cfdd7da340b2d284b6913ea555a7cda5dd083dd0
- TAITS_全系統架構總覽（FULL_ARCH）__260101.md: b79d002c5edbce46f656084ce12a10c8fa7e9abca9d31440c52bf8fad2705d86
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__260101.md: 5be917a1246d912beb08e3dd521e07ce792baf45a7a2d4fe8c394da8e6776a46
- TAITS_文件索引與治理對照表（DOCUMENT_INDEX）__260101.md: 7cd849f09a87d3a1a14f078dd1432319dc6ab3ed3ceea214a2c71eb2f41174ce
- TAITS_新手教學與操作引導總則（BEGINNER_GUIDE）__260101.md: 3ffee089adb609fcdef2f1d88eeb407014a54878fcc80d85a1b8ad2f1c2cf3e1
- TAITS_本地執行與運算環境規範（LOCAL_ENV）__260101.md: 4f94f5b0ff89be4030de1c175fac42229f30ff5dc1683500a5d97f651342f4f3
- TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__260101.md: 8aff93e9e67935f3ec4a5473742fd1344236dfda9062f485cc04f7ded6bc0766
- TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）__260101.md: 6b802547a053a5c6daa54c031bb91c685b6ed1aee12f5c4e9af10971dad5e41f
- TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__260101.md: 88d8eb08089a477cec5d10871e9a36540971d01453a7f0401e2eee59311abd89
- TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__260101.md: bdcf93ffad8eb9dd83756b8a06c690f6ca24c2b31118b8845d570b710fa58dce
- TAITS_系統架構與流程細化說明（ARCH_FLOW）__260101.md: 025fb49b8b8d038ba5520f403cac24f477f4eaf9fc7bb24316e31c45bcad32b3
- TAITS_資料來源全集（DATA_SOURCES）__260101.md: 9a990149d22b2ba6f323e381bb62d564b247135ba3492d5bdecd627a95d4c22d
- TAITS_部署、營運與日常運作規範（DEPLOY_OPS）__260101.md: 3ffee089adb609fcdef2f1d88eeb407014a54878fcc80d85a1b8ad2f1c2cf3e1
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）__260101.md: 134f737a353428392c9a1c333ed9e5faea8e4bbacf1e9a562e9c1c1e245cb7d1
- TAITS｜程式開發流程定錨文件（Unified Process Anchor）__260101.md: 21d00cb8b39d9860254a92fe199a42ab028acb7bb5d142f44386a34190e3e418
