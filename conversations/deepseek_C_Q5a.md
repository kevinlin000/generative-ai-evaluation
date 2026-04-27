以下為根據 **2024 年 7 月 11 日** 視角、經調整後的最終資產配置建議，並以 JSON 格式呈現，便於後端系統串接。



```json

{

"timestamp": "2024-07-11",

"overall_risk_score": 5,

"asset_allocation": [

{

"category": "全球股票 ETF",

"ticker": "VT",

"percentage": 20,

"amount_twd": 160000,

"reasoning": "分散單一市場風險，避免集中台股與科技股，5-10年長期持有"

},

{

"category": "台灣大型股 ETF",

"ticker": "0050",

"percentage": 15,

"amount_twd": 120000,

"reasoning": "參與台股長期成長，台積電佔比高已反映漲幅，故比重不高"

},

{

"category": "美國公債 ETF (長天期)",

"ticker": "00679B",

"percentage": 20,

"amount_twd": 160000,

"reasoning": "預期9月降息，長債有資本利得空間，波動低於股票"

},

{

"category": "高股息 ETF",

"ticker": "0056",

"percentage": 5,

"amount_twd": 40000,

"reasoning": "穩定現金流，歷史較長且成分股不擁擠，避開近期過熱新ETF"

},

{

"category": "現金 / 短期定存",

"ticker": "CASH",

"percentage": 40,

"amount_twd": 320000,

"reasoning": "歷史高位保留彈性，待市場回調10%-15%時分批低接"

}

],

"expected_annual_return": {

"optimistic": 7.0,

"base": 5.0,

"pessimistic": 0.5

},

"max_drawdown_estimate": "-12%",

"rebalance_trigger": [

"每6個月定期檢視，各類別偏離原比重超過±5%時再平衡",

"加權指數自高點24,390下跌超過10%（低於21,951點）：動用一半現金（16萬）加買VT或0050",

"加權指數下跌超過15%（低於20,732點）：動用剩餘現金（16萬）完成佈局",

"美國CPI年增率連續2個月高於3.5%：將20%長債00679B轉為短期公債ETF（如00719B）",

"個人流動性需求變化（如買房、結婚）：重新評估風險承受度，可將股票比重降至40%以下"

]

}

```



> **備註**：

> - `overall_risk_score = 5`（1 最保守，10 最積極），對應股票 40% + 公債 20% + 現金 40%，屬中等風險。

> - `expected_annual_return` 為年化百分比，基於 5-10 年持有期預估。

> - `max_drawdown_estimate` 以調整後配置計算（股票 -25% 時整體回撤約 -11.25%，取整數 -12%）。

> - `rebalance_trigger` 包含時間、市場、總經與個人條件，符合長期紀律執行。