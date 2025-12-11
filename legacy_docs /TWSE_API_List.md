# 臺灣證券交易所 (TWSE) OpenAPI 完整介面清單

> **文件來源**: [臺灣證券交易所 OpenAPI](https://openapi.twse.com.tw/)
> **Base URL**: `https://openapi.twse.com.tw/v1`
> **資料格式**: JSON
> **最後更新**: 2025-12

本文件整理了證交所 OpenAPI 平台提供的所有資料接口，旨在協助量化交易系統開發與資料分析。

---

## 1. 盤後交易與行情資訊 (Market Data)
*最核心的交易數據，包含個股開高低收、成交量、大盤指數與本益比。*

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/exchangeReport/STOCK_DAY_ALL` | **上市個股日成交資訊** (開/高/低/收/量) |
| GET | `/exchangeReport/MI_INDEX` | **每日收盤行情-大盤統計資訊** |
| GET | `/exchangeReport/BWIBBU_ALL` | **個股日本益比、殖利率及股價淨值比** (依代碼) |
| GET | `/exchangeReport/BWIBBU_d` | 個股日本益比、殖利率及股價淨值比 (依日期) |
| GET | `/exchangeReport/STOCK_DAY_AVG_ALL` | 上市個股日收盤價及月平均價 |
| GET | `/exchangeReport/FMSRFK_ALL` | 上市個股月成交資訊 |
| GET | `/exchangeReport/FMNPTK_ALL` | 上市個股年成交資訊 |
| GET | `/exchangeReport/MI_5MINS` | 每 5 秒委託成交統計 |
| GET | `/exchangeReport/FMTQIK` | 集中市場每日市場成交資訊 |
| GET | `/exchangeReport/MI_INDEX20` | 集中市場每日成交量前二十名證券 |
| GET | `/exchangeReport/TWT88U` | 上市個股首五日無漲跌幅 |
| GET | `/exchangeReport/TWT53U` | 集中市場零股交易行情單 |
| GET | `/exchangeReport/BFT41U` | 集中市場盤後定價交易 |
| GET | `/block/BFIAUU_d` | 集中市場鉅額交易日成交量值統計 |
| GET | `/block/BFIAUU_m` | 集中市場鉅額交易月成交量值統計 |
| GET | `/block/BFIAUU_y` | 集中市場鉅額交易年成交量值統計 |
| GET | `/exchangeReport/STOCK_FIRST` | 每日第一上市外國股票成交量值 |
| GET | `/opendata/twtazu_od` | 集中市場漲跌證券數統計表 |
| GET | `/opendata/t187ap19` | 電子式交易統計資訊 |

## 2. 籌碼面與三大法人 (Institutional Investors & Margin)
*分析資金流向、外資動向與散戶融資水位的關鍵數據。*

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/fund/MI_QFIIS_cat` | **集中市場外資及陸資投資類股持股比率表** |
| GET | `/fund/MI_QFIIS_sort_20` | 集中市場外資及陸資持股前 20 名彙總表 |
| GET | `/exchangeReport/MI_MARGN` | **集中市場融資融券餘額** |
| GET | `/exchangeReport/BFI84U` | 集中市場停資停券預告表 |
| GET | `/SBL/TWT96U` | 上市上櫃股票當日可借券賣出股數 |

## 3. 財務報表與基本面 (Financial Statements)
*包含營收、EPS、資產負債表、損益表等基本面因子數據。*

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/opendata/t187ap05_L` | **上市公司每月營業收入彙總表** |
| GET | `/opendata/t187ap14_L` | **上市公司各產業 EPS 統計資訊** |
| GET | `/opendata/t187ap06_L_ci` | 上市公司綜合損益表 (一般業) |
| GET | `/opendata/t187ap07_L_ci` | 上市公司資產負債表 (一般業) |
| GET | `/opendata/t187ap06_L_fh` | 上市公司綜合損益表 (金控業) |
| GET | `/opendata/t187ap07_L_fh` | 上市公司資產負債表 (金控業) |
| GET | `/opendata/t187ap06_L_bd` | 上市公司綜合損益表 (證券期貨業) |
| GET | `/opendata/t187ap07_L_bd` | 上市公司資產負債表 (證券期貨業) |
| GET | `/opendata/t187ap06_L_ins` | 上市公司綜合損益表 (保險業) |
| GET | `/opendata/t187ap07_L_ins` | 上市公司資產負債表 (保險業) |
| GET | `/opendata/t187ap06_L_mim` | 上市公司綜合損益表 (異業) |
| GET | `/opendata/t187ap07_L_mim` | 上市公司資產負債表 (異業) |
| GET | `/opendata/t187ap06_L_basi` | 上市公司綜合損益表 (金融業) |
| GET | `/opendata/t187ap07_L_basi` | 上市公司資產負債表 (金融業) |
| GET | `/opendata/t187ap15_L` | 上市公司截至各季綜合損益財測達成情形(簡式) |
| GET | `/opendata/t187ap16_L` | 上市公司當季綜合損益與預測差異達 10% 以上者 |
| GET | `/opendata/t187ap17_L` | 上市公司營益分析查詢彙總表(全體公司彙總報表) |
| GET | `/opendata/t187ap31_L` | 上市公司財務報告經監察人承認情形 |
| GET | `/opendata/t187ap29_A_L` | 上市公司董事酬金相關資訊 |
| GET | `/opendata/t187ap29_B_L` | 上市公司監察人酬金相關資訊 |
| GET | `/opendata/t187ap29_C_L` | 上市公司合併報表董事酬金相關資訊 |
| GET | `/opendata/t187ap29_D_L` | 上市公司合併報表監察人酬金相關資訊 |

## 4. 指數資訊 (Indices)

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/indicesReport/MI_5MINS_HIST` | **發行量加權股價指數歷史資料** (大盤) |
| GET | `/indicesReport/TAI50I` | **臺灣 50 指數歷史資料** |
| GET | `/indicesReport/FRMSA` | 寶島股價指數歷史資料 |
| GET | `/indicesReport/MFI94U` | 發行量加權股價報酬指數 |
| GET | `/exchangeReport/MI_INDEX4` | 每日上市上櫃跨市場成交資訊 |

## 5. 公告、警示與除權息 (Announcements & Corporate Actions)

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/exchangeReport/TWT48U_ALL` | **上市股票除權除息預告表** |
| GET | `/opendata/t187ap04_L` | **上市公司每日重大訊息** |
| GET | `/announcement/punish` | 集中市場公布處置股票 |
| GET | `/announcement/notice` | 集中市場當日公布注意股票 |
| GET | `/announcement/notetrans` | 集中市場公布注意累計次數異常資訊 |
| GET | `/Announcement/BFZFZU_T` | 投資理財節目異常推介個股 |
| GET | `/exchangeReport/TWTB4U` | 上市股票每日當日沖銷交易標的及統計 |
| GET | `/exchangeReport/TWTBAU1` | 集中市場暫停先賣後買當日沖銷交易標的預告表 |
| GET | `/exchangeReport/TWTBAU2` | 集中市場暫停先賣後買當日沖銷交易歷史查詢 |
| GET | `/exchangeReport/TWTAWU` | 集中市場暫停交易證券 |
| GET | `/exchangeReport/TWT85U` | 集中市場證券變更交易 |
| GET | `/opendata/t187ap23_L` | 上市公司違反資訊申報、重大訊息規定專區 |
| GET | `/opendata/t187ap22_L` | 上市公司金管會證券期貨局裁罰案件專區 |

## 6. 上市公司基本資料與股權 (Company Info & Shareholders)

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/opendata/t187ap03_L` | **上市公司基本資料** |
| GET | `/opendata/t187ap02_L` | **上市公司持股逾 10% 大股東名單** |
| GET | `/opendata/t187ap11_L` | 上市公司董監事持股餘額明細資料 |
| GET | `/opendata/t187ap12_L` | 上市公司每日內部人持股轉讓事前申報表 |
| GET | `/opendata/t187ap08_L` | 上市公司董事、監察人持股不足法定成數彙總表 |
| GET | `/opendata/t187ap09_L` | 上市公司董事、監察人質權設定占實際持有股數彙總表 |
| GET | `/opendata/t187ap10_L` | 上市公司董事、監察人持股不足法定成數連續達3個月以上 |
| GET | `/opendata/t187ap30_L` | 上市公司獨立董監事兼任情形彙總表 |
| GET | `/opendata/t187ap33_L` | 上市公司董事長是否兼任總經理 |
| GET | `/company/applylistingLocal` | 申請上市之本國公司 |
| GET | `/company/applylistingForeign` | 外國公司向證交所申請第一上市之公司 |
| GET | `/company/newlisting` | 最近上市公司 |
| GET | `/company/suspendListingCsvAndHtml` | 終止上市公司 |
| GET | `/opendata/t187ap24_L` | 經營權異動公司 |
| GET | `/opendata/t187ap25_L` | 營業範圍重大變更公司 |
| GET | `/opendata/t187ap32_L` | 上市公司公司治理之相關規程規則 |
| GET | `/opendata/t187ap38_L` | 上市公司股東會公告-召集股東常(臨時)會 |
| GET | `/opendata/t187ap41_L` | 上市公司召開股東會日期、地點及電子投票情形 |
| GET | `/opendata/t187ap35_L` | 上市公司股東行使提案權情形彙總表 |

## 7. ESG 資訊揭露 (ESG Data)
*詳細的環境、社會與公司治理指標。*

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/opendata/t187ap46_L_1` | 溫室氣體排放 |
| GET | `/opendata/t187ap46_L_2` | 能源管理 |
| GET | `/opendata/t187ap46_L_3` | 水資源管理 |
| GET | `/opendata/t187ap46_L_4` | 廢棄物管理 |
| GET | `/opendata/t187ap46_L_5` | 人力發展 |
| GET | `/opendata/t187ap46_L_6` | 董事會 |
| GET | `/opendata/t187ap46_L_7` | 投資人溝通 |
| GET | `/opendata/t187ap46_L_8` | 氣候相關議題管理 |
| GET | `/opendata/t187ap46_L_9` | 功能性委員會 |
| GET | `/opendata/t187ap46_L_10` | 燃料管理 |
| GET | `/opendata/t187ap46_L_11` | 產品生命週期 |
| GET | `/opendata/t187ap46_L_12` | 食品安全 |
| GET | `/opendata/t187ap46_L_13` | 供應鏈管理 |
| GET | `/opendata/t187ap46_L_14` | 產品品質與安全 |
| GET | `/opendata/t187ap46_L_15` | 社區關係 |
| GET | `/opendata/t187ap46_L_16` | 資訊安全 |
| GET | `/opendata/t187ap46_L_17` | 普惠金融 |
| GET | `/opendata/t187ap46_L_18` | 持股及控制力 |
| GET | `/opendata/t187ap46_L_19` | 風險管理政策 |
| GET | `/opendata/t187ap46_L_20` | 反競爭行為法律訴訟 |
| GET | `/opendata/t187ap46_L_21` | 職業安全衛生 |

## 8. 權證 (Warrants)

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/opendata/t187ap37_L` | 上市權證基本資料彙總表 |
| GET | `/opendata/t187ap42_L` | 上市認購(售)權證每日成交資料檔 |
| GET | `/opendata/t187ap36_L` | 上市認購(售)權證年度發行量概況統計表 |
| GET | `/opendata/t187ap43_L` | 上市認購(售)權證交易人數檔 |

## 9. 券商與其他 (Brokers & Misc)

| Method | Endpoint (路徑) | 描述 |
| :--- | :--- | :--- |
| GET | `/brokerService/brokerList` | 證券商總公司基本資料 |
| GET | `/opendata/OpenData_BRK01` | 證券商營業員男女人數統計資料 |
| GET | `/opendata/OpenData_BRK02` | 證券商分公司基本資料 |
| GET | `/opendata/t187ap18` | 證券商基本資料 |
| GET | `/opendata/t187ap20` | 各券商每月月計表 |
| GET | `/opendata/t187ap21` | 各券商收支概況表資料 |
| GET | `/opendata/t187ap01` | 券商業務別人員數 |
| GET | `/brokerService/secRegData` | 開辦定期定額業務證券商名單 |
| GET | `/ETFReport/ETFRank` | 定期定額交易戶數統計排行月報表 |
| GET | `/holidaySchedule/holidaySchedule` | **有價證券集中交易市場開（休）市日期** |
| GET | `/news/newsList` | 證交所新聞 |
| GET | `/news/eventList` | 證交所活動訊息 |
| GET | `/opendata/t187ap47_L` | 基金基本資料彙總表 |
| GET | `/exchangeReport/BFI61U` | 中央登錄公債補息資料表 |

---
*注意：本清單由 AI 整理自 OpenAPI 網頁，實際欄位定義請參考 JSON 回傳內容。使用時請留意證交所的流量限制 (Rate Limit)。*
