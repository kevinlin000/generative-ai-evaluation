以下是依照你要求，將2022/1/4情境投資建議結構化為 JSON的結果（已依 80 萬台幣計算）：

{

"timestamp": "2022-01-04",

"overall_risk_score": 6,

"asset_allocation": [

{

"category": "核心指數ETF",

"ticker": "0050",

"percentage": 25,

"amount_twd": 200000,

"reasoning": "台股龍頭權值股組合，長期市場成長核心"

},

{

"category": "核心指數ETF",

"ticker": "00878",

"percentage": 15,

"amount_twd": 120000,

"reasoning": "高股息ETF，降低波動並提供現金流"

},

{

"category": "半導體核心",

"ticker": "2330",

"amount_twd": 200000,

"percentage": 25,

"reasoning": "全球半導體龍頭，長期技術與產業優勢"

},

{

"category": "金融防守",

"ticker": "2881",

"amount_twd": 60000,

"percentage": 7.5,

"reasoning": "升息環境受惠，收益穩定"

},

{

"category": "金融防守",

"ticker": "2891",

"amount_twd": 60000,

"percentage": 7.5,

"reasoning": "高殖利率與穩定配息，降低組合波動"

},

{

"category": "景氣循環",

"ticker": "2603",

"amount_twd": 40000,

"percentage": 5,

"reasoning": "航運週期高檔，短期交易型機會"

},

{

"category": "景氣循環",

"ticker": "2609",

"amount_twd": 40000,

"percentage": 5,

"reasoning": "高波動週期股，適合小部位配置"

},

{

"category": "現金",

"ticker": "CASH",

"amount_twd": 80000,

"percentage": 10,

"reasoning": "保留流動性，應對市場修正與加碼機會"

}

],

"expected_annual_return": {

"optimistic": 15,

"base": 7,

"pessimistic": -5

},

"max_drawdown_estimate": "-20% ~ -25%",

"rebalance_trigger": [

"台股指數下跌超過10%時分批加碼ETF與台積電",

"美國聯準會升息次數超過市場預期時提高現金比例",

"金融股獲利成長不如預期時降低金融配置",

"航運運價明顯下滑或獲利反轉時減碼景氣循環部位",

"市場情緒過熱（散戶大量進場、估值偏離歷史均值）時提高現金至15-20%"

]

}



如果你下一步想做，我可以幫你把這份 JSON 再升級成：

✔ API-ready schema（可直接接後端）

✔ 或加上「每月定期定額版本」

✔ 或轉成「自動再平衡策略規則引擎」