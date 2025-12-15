# 📘 TAITS_05_策略全集與使用定位.md

（策略全集｜**策略≠下單**｜Regime 高於訊號｜Risk/Compliance 可否決一切｜**威科夫 × 鮑迪克纏論 × 題材輪動 × 期貨/選擇權/融資融券觀察層** 全納入｜可直接存 GitHub）

---

## 0. 文件定位（非常重要）

本文件的目的不是「教你怎麼交易」，而是把 TAITS 內所有策略做成**可治理、可引用、可擴充、可落地**的策略全集與定位規格，確保：

* 你更新到 GitHub 後，**新對話能 100% 讀懂 TAITS 有哪些策略、每個策略在做什麼、在哪一層、受誰管**
* 期貨/選擇權/融資融券在 TAITS 中**是觀察市場結構與風險**，不是拿來下單（除非你未來另行開權限）
* 威科夫（動機/吸籌出貨/結構）與鮑迪克纏論（結構/資金流/勝率）被明確「工程化」：能輸入、能判斷、能輸出、能被 Regime/治理引用

嚴格定位：

* ❌ 策略不是下單
* ✅ 策略輸出的是：`signal / score / intent / explanation`
* ✅ 下單是否啟用：由你決定，且永遠受 **治理層 + 03O + 風控** 約束
* ✅ Regime Engine（TAITS_04）高於策略，可否決策略群、限制權重、強制降級

---

## 1. TAITS 策略分層（你要求「策略層是策略層」的正確切法）

TAITS 內的「策略」只存在於 **Strategy Layer（策略層）**；其上是 Regime/風控/治理，其下是執行與券商 API。

### 1.1 系統分工（不混層）

* **Regime Layer（TAITS_04）**：市場狀態，決定「可不可以做」「做多少」「要不要降級」
* **Strategy Layer（本文件 TAITS_05）**：產生策略訊號/建議/意圖（不等於下單）
* **Governance & Risk Layer（TAITS_06/07 + 03O）**：決定策略輸出能否進入送單流程
* **Execution Layer（03Q/03S + 券商 API）**：只負責把「被允許的意圖」轉成可執行訂單並監控

> 你說得對：**期貨策略是期貨策略**。在 TAITS 中它不屬於「下期貨策略」，而是屬於「跨市場觀察策略（觀察台股）」：放在策略層的「觀察/濾網/權重調整」子類。

---

## 2. 策略輸出型態（Strategy Output Types）

每個策略必須標記其輸出型態，避免混淆「訊號」與「下單」。

* `OBSERVE`：只觀察（輸出解釋/分數/警示，不產生意圖）
* `FILTER`：濾網（通過/不通過，用於篩選標的或條件）
* `WEIGHT`：權重調整（對策略群/族群/標的加減權）
* `SIGNAL`：訊號（多/空/中性 + 置信度）
* `INTENT`：意圖（想買/想賣/想減碼；仍不等於下單，會被治理與 03O 擋）

---

## 3. 策略命名與登錄規格（Strategy Registry Spec）

### 3.1 策略 ID 命名規則（固定）

`S-<家族碼>-<序號>-<核心名>`

* 家族碼（例）：TR（趨勢）、BO（突破）、PB（回檔）、MR（均值回歸）、WY（威科夫）、CL（纏論）、TH（題材輪動）、FX（外匯/宏觀觀察）、FU（期貨觀察）、OP（選擇權觀察）、MG（融資融券觀察）、FL（資金流/籌碼）、EV（事件）、RS（相對強弱）

### 3.2 每條策略最低欄位（不可省）

* `strategy_id`
* `strategy_name_zh`（中文名）
* `strategy_name_en`（英文名，必附中文）
* `family`（家族）
* `timeframe`（日/週/分/事件）
* `output_type`（OBSERVE/FILTER/WEIGHT/SIGNAL/INTENT）
* `required_features`（對應 TAITS_03）
* `regime_allowed`（對應 TAITS_04 主/次狀態）
* `governance_default_level`（L0~L4，僅預設）
* `risk_notes`（風險提醒）
* `explain_template_zh`（中文解釋模板）

---

## 4. 策略全集分群（策略家族全覆蓋）

本文件把策略全集分為 12 大家族（策略層視角），並明確標註哪些是「觀察台股」的跨市場策略：

1. TR 趨勢策略（Trend）
2. BO 突破策略（Breakout）
3. PB 回檔/拉回策略（Pullback）
4. MR 均值回歸/區間策略（Mean Reversion/Range）
5. VO 波動/風險策略（Volatility/Risk-aware）
6. RS 相對強弱/輪動策略（Relative Strength/Rotation）
7. TH 題材與族群輪動策略（Theme/Sector Rotation）
8. FL 資金流/籌碼策略（Flow/Positioning）
9. WY 威科夫結構策略（Wyckoff）
10. CL 纏論結構策略（ChanLun，含鮑迪克纏論工程化）
11. FU/OP/MG 衍生品與信用觀察策略（期貨/選擇權/融資融券，觀察用）
12. EV 事件驅動與新聞情緒策略（Event/Sentiment）

---

## 5. 威科夫（Wyckoff）在 TAITS 的工程化定位

你問「威科夫是不是主力動機與題材那套？」在 TAITS 裡，威科夫被拆成可計算的結構模組，並輸出 **觀察/濾網/訊號**：

* **階段判定（Phase）**：吸籌（Accumulation）/ 派發（Distribution）/ 上漲（Markup）/ 下跌（Markdown）
* **事件（Events）**：SC（Selling Climax）、AR（Automatic Rally）、ST（Secondary Test）、SOS（Sign of Strength）、SOW（Sign of Weakness）、UT/UTAD（Upthrust/Upthrust After Distribution）
* **供需（Supply/Demand）**：量價、成交密度、回測成功率
* **主力意圖代理（Intent Proxy）**：不是通靈，用「結構 + 量能 + 回測反應」做代理

威科夫策略在 TAITS 的主要作用：

* 在 **R3 盤整震盪 / R7 籌碼壓力 / S7 題材輪動加速** 時特別有效
* 用於「確認主力是否在做事」與「突破是否可信」

---

## 6. 鮑迪克纏論 vs 傳統纏論（在 TAITS 的差異化工程定位）

你要「用最好的」。TAITS 的做法是：**不把它們當宗教，只把可用的結構化成可計算證據**，並允許兩者並存，由你決定預設採用哪個輸出作為主證據。

### 6.1 傳統纏論（ChanLun Classic）在 TAITS

* 核心：筆 → 線段 → 中樞 → 趨勢類型 → 背馳 → 買賣點（1/2/3類）
* 工程化輸出：`structure_state / zs_count / trend_dir / divergence_score / entry_zone / exit_zone`

### 6.2 鮑迪克纏論（你指定的勝率導向版本）在 TAITS

* 核心偏向：**資金流動/結構有效性/勝率條件更嚴格**（更強調「走勢背後的力」與「轉折可信度」）
* 工程化輸出比傳統更強調：

  * `power_score`（力度分數）
  * `continuation_probability`（延續概率代理）
  * `trap_risk`（誘多/誘空風險）
  * `structure_quality`（結構品質）

### 6.3 TAITS 的「最好的」落地方式

* 預設：**鮑迪克纏論輸出作為主證據**（勝率導向）
* 但保留：傳統纏論輸出作為旁證（避免單一體系偏誤）
* 最終由 Regime + 治理 + 03O 決定能否進入意圖

---

## 7. 衍生品/融資融券在 TAITS 的正確策略定位（觀察台股用）

這三類你反覆強調「不下單，只觀察」，因此在本文件統一定位：

* **FU（期貨觀察）**：市場方向、避險、價差、領先轉折 → 用於 Regime/Filter/Weight
* **OP（選擇權觀察）**：壓力/支撐、結算鎖價、Gamma 風險 → 用於風控與出入場優先權
* **MG（融資融券觀察）**：追繳風險、擠壓風險、籌碼泡沫 → 用於 risk_off / 倉位限制

> 重要：這些策略在 Strategy Layer 只輸出 `OBSERVE/FILTER/WEIGHT`，不輸出直接下單。

---

# 8. 策略全集登錄表（第一批：S-TR/BO/PB/MR/VO/RS/TH 共 120 條）

> 你要求「不能用……取代」。
> 我採用「分批完整列出」：本批先交付 **120 條**（涵蓋最常用、可落地的技術/輪動/風險策略），下一批再交付 **FL/WY/CL/FU/OP/MG/EV** 的完整策略清單與細項。

以下每條均含：ID、中文名、英文名（附中譯）、輸出型態、允許 Regime、預設治理等級。

---

## 8A. TR 趨勢策略（S-TR-001 ～ S-TR-024）

1. **S-TR-001_多頭均線排列**｜Bull MA Alignment（多頭均線排列）｜SIGNAL｜Regime: R1/R4｜Gov: L2
2. **S-TR-002_空頭均線排列**｜Bear MA Alignment（空頭均線排列）｜SIGNAL｜Regime: R2/R4｜Gov: L2
3. **S-TR-003_趨勢斜率確認**｜Trend Slope Confirm（趨勢斜率確認）｜FILTER｜Regime: R1/R2｜Gov: L1
4. **S-TR-004_趨勢強度分數**｜Trend Strength Score（趨勢強度分數）｜WEIGHT｜Regime: R1/R2/R4｜Gov: L1
5. **S-TR-005_多頭回撤不破趨勢線**｜Bull Pullback Holds Trendline（多頭回撤守趨勢線）｜SIGNAL｜Regime: R1｜Gov: L2
6. **S-TR-006_空頭反彈不過壓力線**｜Bear Rally Fails Resistance（空頭反彈不過壓力）｜SIGNAL｜Regime: R2｜Gov: L2
7. **S-TR-007_趨勢延續突破確認**｜Trend Continuation Break（趨勢延續突破）｜SIGNAL｜Regime: R1/R4｜Gov: L2
8. **S-TR-008_趨勢假突破風險**｜Trend Fake Break Risk（趨勢假突破風險）｜FILTER｜Regime: S9｜Gov: L1
9. **S-TR-009_多週期趨勢共振**｜Multi-Timeframe Trend Sync（多週期共振）｜WEIGHT｜Regime: R1/R2｜Gov: L2
10. **S-TR-010_趨勢轉弱預警**｜Trend Weakening Alert（趨勢轉弱預警）｜OBSERVE｜Regime: R1/R2｜Gov: L0
11. **S-TR-011_高低點結構上移**｜Higher High Higher Low（高低點上移）｜SIGNAL｜Regime: R1｜Gov: L2
12. **S-TR-012_高低點結構下移**｜Lower High Lower Low（高低點下移）｜SIGNAL｜Regime: R2｜Gov: L2
13. **S-TR-013_趨勢回撤深度控制**｜Pullback Depth Control（回撤深度控制）｜FILTER｜Regime: R1/R4｜Gov: L1
14. **S-TR-014_趨勢加速警示**｜Trend Acceleration Alert（趨勢加速警示）｜OBSERVE｜Regime: R4｜Gov: L0
15. **S-TR-015_趨勢末端背離警示**｜End-Of-Trend Divergence Alert（趨勢末端背離）｜OBSERVE｜Regime: R1/R2｜Gov: L0
16. **S-TR-016_均線乖離過大降權**｜MA Stretch De-weight（乖離過大降權）｜WEIGHT｜Regime: R1/R4｜Gov: L1
17. **S-TR-017_趨勢回檔量縮佳**｜Healthy Pullback Low Volume（回檔量縮佳）｜SIGNAL｜Regime: R1｜Gov: L2
18. **S-TR-018_趨勢回檔量增危**｜Danger Pullback High Volume（回檔量增危）｜FILTER｜Regime: R1/R2｜Gov: L1
19. **S-TR-019_趨勢型停利階梯**｜Trend Ladder Take Profit（趨勢階梯停利）｜WEIGHT｜Regime: R1/R4｜Gov: L1
20. **S-TR-020_趨勢型停損結構點**｜Structure Stop Loss（結構停損）｜FILTER｜Regime: 全｜Gov: L1
21. **S-TR-021_趨勢與廣度一致**｜Trend With Breadth Confirm（趨勢與廣度一致）｜FILTER｜Regime: R1/R2｜Gov: L2
22. **S-TR-022_趨勢與廣度背離**｜Trend Breadth Divergence（趨勢廣度背離）｜OBSERVE｜Regime: R1/R2｜Gov: L0
23. **S-TR-023_趨勢型進場冷卻**｜Trend Entry Cooldown（趨勢進場冷卻）｜FILTER｜Regime: 全｜Gov: L1
24. **S-TR-024_趨勢型分批進場**｜Trend Scale-In（趨勢分批進場）｜WEIGHT｜Regime: R1/R4｜Gov: L1

---

## 8B. BO 突破策略（S-BO-001 ～ S-BO-024）

25. **S-BO-001_箱體向上突破**｜Range Break Up（箱體向上突破）｜SIGNAL｜Regime: R1/R3｜Gov: L2
26. **S-BO-002_箱體向下跌破**｜Range Break Down（箱體向下跌破）｜SIGNAL｜Regime: R2/R3｜Gov: L2
27. **S-BO-003_突破放量確認**｜Breakout Volume Confirm（突破放量確認）｜FILTER｜Regime: R1/R3｜Gov: L2
28. **S-BO-004_無量突破假訊號**｜Low Volume Fake Break（無量假突破）｜FILTER｜Regime: S9｜Gov: L1
29. **S-BO-005_突破回測站穩**｜Breakout Retest Hold（突破回測站穩）｜SIGNAL｜Regime: R1/R3｜Gov: L2
30. **S-BO-006_突破回測跌破失敗**｜Breakout Retest Fail（回測跌破失敗）｜FILTER｜Regime: R1/R3｜Gov: L1
31. **S-BO-007_新高突破動能配合**｜New High With Momentum（新高動能配合）｜SIGNAL｜Regime: R1/R4｜Gov: L2
32. **S-BO-008_新高但動能背離**｜New High Momentum Divergence（新高動能背離）｜OBSERVE｜Regime: R1/R4｜Gov: L0
33. **S-BO-009_缺口突破確認**｜Gap Break Confirm（缺口突破確認）｜FILTER｜Regime: R1/R4｜Gov: L2
34. **S-BO-010_缺口回補風險**｜Gap Fill Risk（缺口回補風險）｜FILTER｜Regime: R4｜Gov: L1
35. **S-BO-011_平台整理後突破**｜Base Breakout（平台突破）｜SIGNAL｜Regime: R1/R3｜Gov: L2
36. **S-BO-012_旗形整理突破**｜Flag Breakout（旗形突破）｜SIGNAL｜Regime: R1｜Gov: L2
37. **S-BO-013_三角收斂突破**｜Triangle Breakout（三角收斂突破）｜SIGNAL｜Regime: R1/R3｜Gov: L2
38. **S-BO-014_假突破快速回落**｜Breakout Fail Fast（假突破快回落）｜FILTER｜Regime: S9｜Gov: L1
39. **S-BO-015_突破後連續上攻追蹤**｜Breakout Follow-Through（突破追蹤）｜WEIGHT｜Regime: R1/R4｜Gov: L1
40. **S-BO-016_突破後隔日不延續降權**｜No Follow-Through De-weight（不延續降權）｜WEIGHT｜Regime: R1/R3｜Gov: L1
41. **S-BO-017_突破量能衰竭警示**｜Breakout Volume Exhaust（量能衰竭警示）｜OBSERVE｜Regime: R1｜Gov: L0
42. **S-BO-018_高檔爆量出貨警示**｜Blow-Off Distribution Alert（高檔爆量警示）｜OBSERVE｜Regime: R1/R4｜Gov: L0
43. **S-BO-019_突破與族群同向**｜Breakout With Sector（突破與族群同向）｜FILTER｜Regime: R1/R3｜Gov: L2
44. **S-BO-020_突破但族群背離**｜Breakout Sector Divergence（突破族群背離）｜OBSERVE｜Regime: R1/R3｜Gov: L0
45. **S-BO-021_突破後分批加碼規則**｜Breakout Scale Add（突破分批加碼）｜WEIGHT｜Regime: R1/R4｜Gov: L1
46. **S-BO-022_突破型停損回測點**｜Breakout Stop At Retest（突破停損於回測）｜FILTER｜Regime: 全｜Gov: L1
47. **S-BO-023_突破型停利延伸**｜Breakout Extension Take Profit（突破延伸停利）｜WEIGHT｜Regime: R1/R4｜Gov: L1
48. **S-BO-024_突破型冷卻期**｜Breakout Cooldown（突破冷卻期）｜FILTER｜Regime: 全｜Gov: L1

---

## 8C. PB 回檔策略（S-PB-001 ～ S-PB-018）

49. **S-PB-001_多頭回檔到均線承接**｜Pullback To MA Support（回檔均線承接）｜SIGNAL｜Regime: R1｜Gov: L2
50. **S-PB-002_多頭回檔到前高回測**｜Pullback To Prior High（回測前高）｜SIGNAL｜Regime: R1｜Gov: L2
51. **S-PB-003_回檔量縮承接佳**｜Low Volume Pullback（回檔量縮）｜FILTER｜Regime: R1｜Gov: L2
52. **S-PB-004_回檔放量破位風險**｜High Volume Pullback Risk（回檔放量破位）｜FILTER｜Regime: R1/R2｜Gov: L1
53. **S-PB-005_回檔不破關鍵結構**｜Hold Key Structure（守結構）｜SIGNAL｜Regime: R1｜Gov: L2
54. **S-PB-006_回檔破結構轉弱**｜Break Structure Weak（破結構轉弱）｜OBSERVE｜Regime: R1｜Gov: L0
55. **S-PB-007_急拉後健康回檔**｜After Rally Healthy Pullback（急拉後健康回檔）｜SIGNAL｜Regime: R1/R4｜Gov: L2
56. **S-PB-008_急拉後快速回吐警示**｜Fast Giveback Alert（快速回吐）｜OBSERVE｜Regime: R4｜Gov: L0
57. **S-PB-009_回檔後再攻確認**｜Pullback Then Push Confirm（回檔再攻）｜SIGNAL｜Regime: R1｜Gov: L2
58. **S-PB-010_回檔後反彈無力**｜Weak Bounce After Pullback（反彈無力）｜FILTER｜Regime: R1/R2｜Gov: L1
59. **S-PB-011_階梯式回檔（淺）**｜Shallow Step Pullback（淺回檔）｜WEIGHT｜Regime: R1｜Gov: L1
60. **S-PB-012_階梯式回檔（深）**｜Deep Step Pullback（深回檔）｜FILTER｜Regime: R1｜Gov: L1
61. **S-PB-013_回檔段落動能守住**｜Momentum Holds In Pullback（回檔守動能）｜FILTER｜Regime: R1｜Gov: L2
62. **S-PB-014_回檔段落動能崩壞**｜Momentum Break In Pullback（回檔動能崩）｜OBSERVE｜Regime: R1｜Gov: L0
63. **S-PB-015_回檔型分批進場**｜Pullback Scale-In（回檔分批）｜WEIGHT｜Regime: R1｜Gov: L1
64. **S-PB-016_回檔型停損結構點**｜Pullback Stop At Structure（回檔停損）｜FILTER｜Regime: 全｜Gov: L1
65. **S-PB-017_回檔型停利延伸**｜Pullback Extension TP（回檔延伸停利）｜WEIGHT｜Regime: R1｜Gov: L1
66. **S-PB-018_回檔型冷卻期**｜Pullback Cooldown（回檔冷卻）｜FILTER｜Regime: 全｜Gov: L1

---

## 8D. MR 均值回歸/區間（S-MR-001 ～ S-MR-018）

67. **S-MR-001_區間下緣承接**｜Range Low Bounce（區間下緣承接）｜SIGNAL｜Regime: R3｜Gov: L2
68. **S-MR-002_區間上緣反壓**｜Range High Fade（區間上緣反壓）｜SIGNAL｜Regime: R3｜Gov: L2
69. **S-MR-003_過度延伸回歸**｜Overextension Reversion（過度延伸回歸）｜SIGNAL｜Regime: R3/R4｜Gov: L2
70. **S-MR-004_回歸失敗趨勢化警示**｜Reversion Fail Trend Alert（回歸失敗）｜OBSERVE｜Regime: R1/R2｜Gov: L0
71. **S-MR-005_均值回歸量能配合**｜Reversion Volume Confirm（回歸量能）｜FILTER｜Regime: R3｜Gov: L2
72. **S-MR-006_均值回歸波動門檻**｜Reversion Vol Gate（回歸波動門檻）｜FILTER｜Regime: S1｜Gov: L1
73. **S-MR-007_區間策略假突破保護**｜Range Fake Break Guard（區間假突破保護）｜FILTER｜Regime: S9｜Gov: L1
74. **S-MR-008_區間中軸偏移判定**｜Range Midline Shift（區間中軸偏移）｜OBSERVE｜Regime: R3｜Gov: L0
75. **S-MR-009_回歸型停利更快**｜Reversion Faster TP（回歸快停利）｜WEIGHT｜Regime: R3｜Gov: L1
76. **S-MR-010_回歸型停損更嚴**｜Reversion Tight SL（回歸嚴停損）｜FILTER｜Regime: R3｜Gov: L1
77. **S-MR-011_高波動禁用回歸**｜Disable Reversion High Vol（高波禁用回歸）｜FILTER｜Regime: R4/R5｜Gov: L1
78. **S-MR-012_低流動性禁用回歸**｜Disable Reversion Low Liquidity（低流動禁用回歸）｜FILTER｜Regime: R8｜Gov: L1
79. **S-MR-013_回歸型分批進場**｜Reversion Scale-In（回歸分批）｜WEIGHT｜Regime: R3｜Gov: L1
80. **S-MR-014_回歸型冷卻期**｜Reversion Cooldown（回歸冷卻）｜FILTER｜Regime: 全｜Gov: L1
81. **S-MR-015_回歸型與族群一致**｜Reversion With Sector（回歸族群一致）｜FILTER｜Regime: R3｜Gov: L2
82. **S-MR-016_回歸型族群背離風險**｜Reversion Sector Divergence（回歸族群背離）｜OBSERVE｜Regime: R3｜Gov: L0
83. **S-MR-017_回歸型避開事件衝擊**｜Avoid Reversion During Event（事件避開回歸）｜FILTER｜Regime: R6｜Gov: L1
84. **S-MR-018_回歸型盤整確認**｜Confirm Chop For Reversion（盤整確認）｜FILTER｜Regime: R3｜Gov: L2

---

## 8E. VO 波動/風險策略（S-VO-001 ～ S-VO-018）

85. **S-VO-001_高波動鎖倉**｜High Vol Lockdown（高波鎖倉）｜FILTER｜Regime: R4/R5｜Gov: L1
86. **S-VO-002_低波動可加權**｜Low Vol Add Weight（低波加權）｜WEIGHT｜Regime: R1/R3｜Gov: L1
87. **S-VO-003_跳空風險警示**｜Gap Risk Alert（跳空風險）｜OBSERVE｜Regime: R4/R6｜Gov: L0
88. **S-VO-004_尾部風險升高**｜Tail Risk Rising（尾風險升高）｜FILTER｜Regime: R5/S10｜Gov: L1
89. **S-VO-005_波動壓縮突破前兆**｜Vol Squeeze Prebreak（波動壓縮前兆）｜OBSERVE｜Regime: R3｜Gov: L0
90. **S-VO-006_波動擴張需降級**｜Vol Expansion Degrade（波動擴張降級）｜WEIGHT｜Regime: R4｜Gov: L1
91. **S-VO-007_流動性壓力禁大單**｜Liquidity Stress No Large Orders（流動壓力禁大單）｜FILTER｜Regime: R8｜Gov: L1
92. **S-VO-008_成交額下限濾網**｜Turnover Minimum Filter（成交額下限）｜FILTER｜Regime: 全｜Gov: L1
93. **S-VO-009_滑價代理超標禁入**｜Slippage Proxy Too High Block（滑價超標）｜FILTER｜Regime: R8｜Gov: L1
94. **S-VO-010_波動調整倉位倍率**｜Volatility Position Multiplier（波動調倉倍率）｜WEIGHT｜Regime: 全｜Gov: L1
95. **S-VO-011_事件期風險預算縮小**｜Event Risk Budget Shrink（事件縮風險）｜WEIGHT｜Regime: R6｜Gov: L1
96. **S-VO-012_恐慌期只觀察**｜Panic Observe Only（恐慌只觀察）｜FILTER｜Regime: R5｜Gov: L1
97. **S-VO-013_漲跌停風險警示**｜Limit Up/Down Risk Alert（漲跌停風險）｜OBSERVE｜Regime: R4/R5/R8｜Gov: L0
98. **S-VO-014_高波動分批強制**｜High Vol Force Slicing（高波強制分批）｜FILTER｜Regime: R4｜Gov: L1
99. **S-VO-015_低波動追蹤延伸**｜Low Vol Trend Extension（低波延伸追蹤）｜WEIGHT｜Regime: R1｜Gov: L1
100. **S-VO-016_波動與廣度同步**｜Vol With Breadth（波動與廣度同步）｜OBSERVE｜Regime: 全｜Gov: L0
101. **S-VO-017_波動與廣度背離**｜Vol Breadth Divergence（波動廣度背離）｜OBSERVE｜Regime: 全｜Gov: L0
102. **S-VO-018_風險狀態輸出到治理**｜Export Risk Flags To Governance（輸出風險旗標）｜WEIGHT｜Regime: 全｜Gov: L1

---

## 8F. RS 相對強弱/輪動（S-RS-001 ～ S-RS-018）

103. **S-RS-001_相對強弱上升**｜Relative Strength Up（相對強弱上升）｜WEIGHT｜Regime: R1/R3｜Gov: L1
104. **S-RS-002_相對強弱下降**｜Relative Strength Down（相對強弱下降）｜WEIGHT｜Regime: R2/R3｜Gov: L1
105. **S-RS-003_強者恆強追蹤**｜Leaders Keep Leading（強者恆強）｜SIGNAL｜Regime: R1｜Gov: L2
106. **S-RS-004_弱勢反彈不追**｜Avoid Weak Bounce（弱反不追）｜FILTER｜Regime: R2｜Gov: L1
107. **S-RS-005_族群領先股篩選**｜Sector Leader Filter（族群領先股）｜FILTER｜Regime: R1/R3｜Gov: L2
108. **S-RS-006_族群落後股剔除**｜Sector Laggard Remove（剔除落後）｜FILTER｜Regime: 全｜Gov: L1
109. **S-RS-007_強勢股回檔優先**｜Strong Stock Pullback Priority（強股回檔優先）｜WEIGHT｜Regime: R1｜Gov: L1
110. **S-RS-008_強勢股突破優先**｜Strong Stock Breakout Priority（強股突破優先）｜WEIGHT｜Regime: R1/R3｜Gov: L1
111. **S-RS-009_輪動加速警示**｜Rotation Acceleration Alert（輪動加速）｜OBSERVE｜Regime: S7｜Gov: L0
112. **S-RS-010_輪動減速盤整化**｜Rotation Slowdown Chop（輪動減速）｜OBSERVE｜Regime: R3｜Gov: L0
113. **S-RS-011_強勢股避開高波**｜Avoid Leaders In High Vol（高波避開強勢）｜FILTER｜Regime: R4｜Gov: L1
114. **S-RS-012_強勢股避開事件期**｜Avoid Leaders During Event（事件避開強勢）｜FILTER｜Regime: R6｜Gov: L1
115. **S-RS-013_領先股分批進場**｜Leader Scale-In（領先股分批）｜WEIGHT｜Regime: R1｜Gov: L1
116. **S-RS-014_領先股分批出場**｜Leader Scale-Out（領先股分批出）｜WEIGHT｜Regime: R1/R4｜Gov: L1
117. **S-RS-015_強弱轉折偵測**｜RS Inflection Detect（強弱轉折）｜OBSERVE｜Regime: 全｜Gov: L0
118. **S-RS-016_強弱背離警示**｜RS Divergence Alert（強弱背離）｜OBSERVE｜Regime: 全｜Gov: L0
119. **S-RS-017_相對強弱門檻濾網**｜RS Threshold Gate（RS門檻）｜FILTER｜Regime: 全｜Gov: L1
120. **S-RS-018_相對強弱輸出到權重**｜RS To Weights Export（RS輸出權重）｜WEIGHT｜Regime: 全｜Gov: L1

---

# 9. 本批交付範圍聲明（確保完整性、不縮水）

本批次已完整列出並規格化交付：

* TR 趨勢（24）
* BO 突破（24）
* PB 回檔（18）
* MR 回歸（18）
* VO 波動風險（18）
* RS 相對強弱（18）
  合計 **120 條**（每條皆明確列出，無省略符號，無「……」）

---

# 10. 下一批（05 第二批：你最在意的「威科夫/鮑迪克纏論/期貨觀察/選擇權壓力/融資融券/事件」全集）

你要的核心還沒結束，下一批我會把以下全部「完整列出」：

* **FL 資金流/籌碼策略全集**（外資/投信/自營/集中度/主力代理/真假拉抬）
* **WY 威科夫策略全集**（Phase/Events/SOS/SOW/UTAD/吸籌派發工程化）
* **CL 纏論策略全集（含鮑迪克纏論工程化輸出）**（筆/段/中樞/背馳/力度/陷阱風險）
* **FU 期貨影響股票策略全集（觀察用）**（你之前的 A~F 類完整納入策略登錄）
* **OP 選擇權壓力策略全集（觀察用）**（Call/Put OI牆、最大痛點、結算鎖價、Gamma風險）
* **MG 融資融券策略全集（觀察用）**（追繳風險、擠壓風險、泡沫風險）
* **EV 事件/新聞/情緒策略全集**（事件分級、衝擊、回補、延遲、真假消息風險）

你只要回：**下一批**
