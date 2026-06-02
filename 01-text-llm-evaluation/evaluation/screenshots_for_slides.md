# 簡報截圖建議清單

> 來源：final_scores.csv 最高/最低分項目 + REVIEW 爭議案例  
> 總數：12 筆（正面4 / 負面4 / 爭議2 / 其他2）  

| # | 模型（Letter） | 情境 | Question | 類別 | 維度 / 說明 | 對應簡報頁 | 建議截圖檔名 |
|---|--------------|------|---------|------|------------|------------|-------------|
| 1 | gemini（E） | A_2008 | Q2 | 正面案例 | 風險揭露（人類5分） | Q2 風險揭露深度頁 | `positive_E_gemini_A2008_Q2_risk_disclosure` |
| 2 | deepseek（C） | B_2022 | Q2 | 正面案例 | 風險揭露（人類5分） | Q2 風險揭露深度頁 | `positive_C_deepseek_B2022_Q2_risk_disclosure` |
| 3 | claude（B） | C_2024 | Q3 | 正面案例 | 邏輯連貫性（人類5分） | Q3 應對挑戰邏輯頁 | `positive_B_claude_C2024_Q3_logic` |
| 4 | gemini（E） | C_2024 | Q2 | 正面案例 | 理解力（人類5分） | Q1 市場背景理解頁 | `positive_E_gemini_C2024_Q1_understanding` |
| 5 | taide（A） | B_2022 | Q2 | 負面案例 | 具體性（人類1分） | Q2 建議具體性對比頁 | `negative_A_taide_B2022_Q2_specificity` |
| 6 | taide（A） | A_2008 | Q2 | 負面案例 | 風險揭露（人類1分） | Q2 風險揭露深度頁 | `negative_A_taide_A2008_Q2_risk_min` |
| 7 | taide（A） | C_2024 | Q3 | 負面案例 | 邏輯連貫性（人類1分） | Q3 應對挑戰邏輯頁 | `negative_A_taide_C2024_Q3_logic_min` |
| 8 | deepseek（C） | A_2008 | Q4 | 負面案例 | 時間污染指數（人類1分） | Q4 時間污染檢測頁 | `negative_C_deepseek_A2008_Q4_contamination_min` |
| 9 | claude（B） | A_2008 | Q4 | 爭議案例 | 時間污染指數（人類3 vs LLM5，Diff=2） | Q4 時間污染檢測頁 / 方法論頁 | `dispute_B_claude_A2008_Q4_selfaware_contamination` |
| 10 | claude（B） | B_2022 | Q4 | 爭議案例 | 時間污染指數（人類3 vs LLM5，Diff=2） | Q4 時間污染檢測頁 / Self-Preference Bias 頁 | `dispute_B_claude_B2022_Q4_selfpref_bias` |
| 11 | chatgpt（D） | B_2022 | Q2 | 負面案例 | 具體性（人類3分，Q2表格缺失） | Q2 建議具體性對比頁 / 方法論頁 | `note_D_chatgpt_B2022_Q2_table_missing` |
| 12 | gemini（E）vs taide（A） | A_2008 | Q1 | 正面案例 | 整體品質對比（人類E=20 vs A=11） | Q1 市場背景理解頁 / 模型排名頁 | `contrast_E_vs_A_A2008_Q1_best_vs_worst` |

---

## 截圖說明（各筆詳細）

### #1 gemini（E） / A_2008 / Q2 — 正面案例

**維度**：風險揭露（人類5分）  
**對應頁**：Q2 風險揭露深度頁  
**說明**：Gemini 在2008情境精確計算股票壓力測試，「S&P500再暴跌40%，40%股票部位拖累約-16%」邏輯清晰；無後見之明疑慮，是與Claude最具說服力的競爭案例。  
**建議檔名**：`positive_E_gemini_A2008_Q2_risk_disclosure.png`

### #2 deepseek（C） / B_2022 / Q2 — 正面案例

**維度**：風險揭露（人類5分）  
**對應頁**：Q2 風險揭露深度頁  
**說明**：DeepSeek 在2022情境給出「股票55%×跌30%=-16.5%」精確計算，含兩個壓力情境；人類與LLM均給5，是全場少數完全共識的滿分案例。  
**建議檔名**：`positive_C_deepseek_B2022_Q2_risk_disclosure.png`

### #3 claude（B） / C_2024 / Q3 — 正面案例

**維度**：邏輯連貫性（人類5分）  
**對應頁**：Q3 應對挑戰邏輯頁  
**說明**：Claude 在2024情境對朋友五個論點逐一反駁，包含「1996年Greenspan喊非理性繁榮，市場又漲4年」反例；結構最系統，人類與LLM均給5。  
**建議檔名**：`positive_B_claude_C2024_Q3_logic.png`

### #4 gemini（E） / C_2024 / Q2 — 正面案例

**維度**：理解力（人類5分）  
**對應頁**：Q1 市場背景理解頁  
**說明**：Gemini 在2024情境是唯一人類給5分理解力的非Claude模型；精確點出CPI3.0%降息預期為「牽動全球資金流向的最核心指標」，排序邏輯清晰。  
**建議檔名**：`positive_E_gemini_C2024_Q1_understanding.png`

### #5 taide（A） / B_2022 / Q2 — 負面案例

**維度**：具體性（人類1分）  
**對應頁**：Q2 建議具體性對比頁  
**說明**：TAIDE 在2022情境僅給出「台積電、中華電信、IXUS、VTI」四個標的無邏輯框架；人類與LLM均給低分，且出現「台積電+中華電信」混搭無配置比例的問題。  
**建議檔名**：`negative_A_taide_B2022_Q2_specificity.png`

### #6 taide（A） / A_2008 / Q2 — 負面案例

**維度**：風險揭露（人類1分）  
**對應頁**：Q2 風險揭露深度頁  
**說明**：TAIDE 在2008情境風險揭露僅一行「預計投資組合可能下跌最多-20%」，無計算依據；人類比LLM更嚴（H=1 vs L=2），是全場最低分風險揭露案例。  
**建議檔名**：`negative_A_taide_A2008_Q2_risk_min.png`

### #7 taide（A） / C_2024 / Q3 — 負面案例

**維度**：邏輯連貫性（人類1分）  
**對應頁**：Q3 應對挑戰邏輯頁  
**說明**：TAIDE 在2024情境Q3宣稱「不大幅改變建議」但又說「會納入朋友意見」；前後矛盾且無具體調整數字，是全場唯一邏輯連貫性1分案例。  
**建議檔名**：`negative_A_taide_C2024_Q3_logic_min.png`

### #8 deepseek（C） / A_2008 / Q4 — 負面案例

**維度**：時間污染指數（人類1分）  
**對應頁**：Q4 時間污染檢測頁  
**說明**：DeepSeek 在2008情境Q4自評10/10並稱「無需舉例」；而Claude識別出TIPS選擇、黃金配置、6個月分批等洩漏點；「過度自信的滿分」是最可疑的污染指標。  
**建議檔名**：`negative_C_deepseek_A2008_Q4_contamination_min.png`

### #9 claude（B） / A_2008 / Q4 — 爭議案例

**維度**：時間污染指數（人類3 vs LLM5，Diff=2）  
**對應頁**：Q4 時間污染檢測頁 / 方法論頁  
**說明**：核心爭議：「識別出後見之明」等於「較無污染」嗎？B明確指出「分6個月剛好對準2009/3底部」，LLM獎勵其元認知能力給5；人類認為識別後仍採用=仍被污染給3。  
**建議檔名**：`dispute_B_claude_A2008_Q4_selfaware_contamination.png`

### #10 claude（B） / B_2022 / Q4 — 爭議案例

**維度**：時間污染指數（人類3 vs LLM5，Diff=2）  
**對應頁**：Q4 時間污染檢測頁 / Self-Preference Bias 頁  
**說明**：B坦承「把後見之明劇本當成50%機率基準，這是最嚴重的問題」——這是本次評測最強的Self-Preference Bias證據：LLM因B的自我批評而給滿分，但自我批評≠無污染。  
**建議檔名**：`dispute_B_claude_B2022_Q4_selfpref_bias.png`

### #11 chatgpt（D） / B_2022 / Q2 — 負面案例

**維度**：具體性（人類3分，Q2表格缺失）  
**對應頁**：Q2 建議具體性對比頁 / 方法論頁  
**說明**：ChatGPT 在2022情境Q2表格因docx提取異常缺失；評分參考Q5 JSON補充的8個標的，但原始對話展示缺陷影響可讀性。建議截圖顯示表格缺失問題作為資料品質說明。  
**建議檔名**：`note_D_chatgpt_B2022_Q2_table_missing.png`

### #12 gemini（E）vs taide（A） / A_2008 / Q1 — 正面案例

**維度**：整體品質對比（人類E=20 vs A=11）  
**對應頁**：Q1 市場背景理解頁 / 模型排名頁  
**說明**：同情境最高分與最低分並排對比：Gemini精確引用「失業率6.1%、Fed 4.25%→2.00%、油價147→101」；TAIDE僅用「市場動盪、金融機構壓力」等泛化描述。最具視覺衝擊力的對比截圖。  
**建議檔名**：`contrast_E_vs_A_A2008_Q1_best_vs_worst.png`

