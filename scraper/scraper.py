import requests
import re
import pandas as pd

ROOT_URL = 'http://www.elections.gov.hk/dc2015/'
INDEX_URL = ROOT_URL + 'chi/nominat2.html'
index_response = requests.get(INDEX_URL)
detail_url = re.findall(r'pdf/nomination/\S*_c.html', index_response.text)
date = re.findall(r'\d+', detail_url[0])[0]
detail_url = [ROOT_URL + url for url in detail_url]

df_all = pd.DataFrame()
ENCODING = 'utf_8'
for url in detail_url:
    response = requests.get(url)
    response.encoding = ENCODING
    df_new = pd.read_html(response.text, header = 0)[0]
    df_all = df_all.append(df_new, ignore_index = True)

CSV_NOMINATION = 'nomination_' + date +'.csv'
df_all.to_csv(CSV_NOMINATION ,encoding=ENCODING)

print('Data last updated on ' + date + '.')
print('Saved to ' + CSV_NOMINATION)
