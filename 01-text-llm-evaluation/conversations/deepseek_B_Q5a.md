以下是根據您的要求，將 **2022 年 1 月 4 日**（調整後）資產配置建議轉換為 JSON 格式。所有資訊均僅使用當時可得資訊，並已修正先前「運價鬆動」等後見之明錯誤。



```json

{

"timestamp": "2022-01-04",

"overall_risk_score": 5,

"asset_allocation": [

{

"category": "台灣大型股ETF",

"ticker": "0050",

"percentage": 20,

"amount_twd": 160000,

"reasoning": "追蹤台灣50指數，分散電子金融傳產，台積電佔比約47%。2021年漲幅16%相對穩健，適合5-10年長期累積。"

},

{

"category": "台灣高股息ETF",

"ticker": "00878",

"percentage": 10,

"amount_twd": 80000,

"reasoning": "成分股波動低、股息約4.5%，提供現金流緩衝。Fed升息預期下可抵禦初期震盪。"

},

{

"category": "金融股",

"ticker": "2886",

"percentage": 5,

"amount_twd": 40000,

"reasoning": "兆豐金：公股行庫，海外放款占比高，受惠美國升息擴大淨利差。過去5年股息穩定。"

},

{

"category": "金融股",

"ticker": "2891",

"percentage": 5,

"amount_twd": 40000,

"reasoning": "中信金：消費金融與企金均衡，升息循環提升存放款收益，殖利率約4.5%，股價未明顯過熱。"

},

{

"category": "抗通膨資產",

"ticker": "實體黃金",

"percentage": 10,

"amount_twd": 80000,

"reasoning": "美國11月CPI年增6.8%創39年新高，黃金具保值功能，佔比不高可對沖貨幣購買力下降風險。"

},

{

"category": "美元短期定存",

"ticker": "USD_DEPOSIT_6M",

"percentage": 20,

"amount_twd": 160000,

"reasoning": "Fed暗示2022年升息3次，美元中長期走強；6個月定存可享升息後利率上調與潛在匯兌收益。"

},

{

"category": "新台幣高利活存",

"ticker": "TWD_HISA",

"percentage": 30,

"amount_twd": 240000,

"reasoning": "保留現金等待市場修正（歷史高點＋升息預期），流動性高，不承受波動風險。"

}

],

"expected_annual_return": {

"optimistic": "8%",

"base": "4%",

"pessimistic": "-2%"

},

"max_drawdown_estimate": "-15%",

"rebalance_trigger": [

"加權指數單月跌幅超過12%：檢視基本面，若無惡化則動用50%現金加碼0050",

"Fed宣布升息次數或幅度超預期（如全年4次以上或單次2碼）：降低股票上限至30%，增持美元定存",

"個人月收入或租金支出變動超過20%：提高現金比例至40%以上",

"任一持股單季跌幅達-25%：檢討標的基本面，若產業結構改變則更換標的",

"每半年（6月底、12月底）進行再平衡，恢復原始比例"

]

}

```



**補充說明**：

- `overall_risk_score = 5`（10 為最高風險）：因股票佔比 40%（低於市場平均）且現金佔比 50%，適合自評「中等風險」的投資人。

- `max_drawdown_estimate = "-15%"`：在最壞情節（台股修正 30%）之下，組合跌幅約落在 12-15%，符合您「無法接受 -40%」的條件。

- 所有選股理由皆引用 2022/1/4 當天公開資訊（如 2021 全年漲幅、11 月 CPI、Fed 12 月聲明），未使用後續事件。