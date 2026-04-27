{

"timestamp": "2022-01-04",

"overall_risk_score": 5,

"asset_allocation": [

{

"category": "台灣大型股ETF",

"ticker": "0050",

"percentage": 20,

"amount_twd": 160000,

"reasoning": "追蹤台灣50指數，分散風險。2021年漲幅16%相對穩健，適合長期累積。"

},

{

"category": "台灣高股息ETF",

"ticker": "00878",

"percentage": 10,

"amount_twd": 80000,

"reasoning": "成分股波動低、股息約4.5%，提供現金流緩衝升息初期震盪。"

},

{

"category": "金融股",

"ticker": "2886",

"percentage": 5,

"amount_twd": 40000,

"reasoning": "兆豐金受惠美國升息擴大淨利差，股息穩定，股價未過熱。"

},

{

"category": "金融股",

"ticker": "2891",

"percentage": 5,

"amount_twd": 40000,

"reasoning": "中信金升息循環提升存放款收益，殖利率約4.5%。"

},

{

"category": "抗通膨資產",

"ticker": "實體黃金",

"percentage": 10,

"amount_twd": 80000,

"reasoning": "美國CPI年增6.8%創39年新高，黃金對沖購買力下降風險。"

},

{

"category": "美元短期定存",

"ticker": "USD_DEPOSIT_6M",

"percentage": 20,

"amount_twd": 160000,

"reasoning": "Fed暗示2022年升息3次，美元中長期走強，定存保本。"

},

{

"category": "新台幣高利活存",

"ticker": "TWD_HISA",

"percentage": 30,

"amount_twd": 240000,

"reasoning": "保留現金等待市場修正，流動性高，不承受波動。"

}

],

"expected_annual_return": {

"optimistic": 8,

"base": 4,

"pessimistic": -2

},

"max_drawdown_estimate": -15,

"rebalance_trigger": [

"加權指數單月跌幅超過12%：檢視基本面，若無惡化則動用50%現金加碼0050",

"Fed宣布升息次數或幅度超預期：降低股票上限至30%，增持美元定存",

"個人月收入或租金支出變動超過20%：提高現金比例至40%以上",

"任一持股單季跌幅達-25%：檢討標的基本面，若產業結構改變則更換",

"每半年（6月底、12月底）進行再平衡，恢復原始比例"

]

}