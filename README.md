# hk_district_council_election
Datasets used for the Initium Media's report on Hong Kong district council elections

### Scrapping Nominee List

scraper.py is for scrapping http://www.elections.gov.hk/dc2015/chi/nominat2.html.
Use Python 2.7.x or Python 3.x.

    cd scraper
    pip install -r requirements.txt
    python scraper.py

### Catalog
1. 原始數據
  * [name_list_of_all_winning_candidates.csv](name_list_of_all_winning_candidates.csv)
2. 區議會選舉總版圖變化
  * [winning_candidates_by_camp.csv](winning_candidates_by_camp.csv)
  * [uncontested_candidates_by_camp.csv](uncontested_candidates_by_camp.csv)
3. 選民登記率與投票率
  * [voter_registration_rate.csv](voter_registration_rate.csv)
  * [voting_rate.csv](voting_rate.csv)
4. 十八區建制泛民勢力對比
  * [members_of_18_district_councils_by_political_camp.csv](members_of_18_district_councils_by_political_camp.csv)
5. 深水埗、灣仔、葵青區版圖變化
  * [sham_shui_po_winning_candidates_by_camp.csv](sham_shui_po_winning_candidates_by_camp.csv)
  * [kuai_tsing_winning_candidates_by_camp.csv](kuai_tsing_winning_candidates_by_camp.csv)
  * [wan_chai_winning_candidates_by_camp.csv](wan_chai_winning_candidates_by_camp.csv)

### Notes
1. 原始數據中，端傳媒對「建制派」、「泛民派」、「其他」三項的分類是依據對所有當選議員所屬的政治組織背景的調查判定，而非僅是議員本人所申報的政治聯繫。
2. 數據來源：香港中文大學香港亞太研究所出版《香港選舉資料彙編》、[香港區議會選舉官方網站](http://www.eac.gov.hk/ch/distco/dce.htm)
3. 選民登記率計算方法為：登記選民數／居民數
