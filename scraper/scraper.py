import requests
import re
import pandas as pd

root_url = 'http://www.elections.gov.hk/dc2015/'
index_url = root_url + 'chi/nominat2.html'
index_response = requests.get(index_url)
detail_url = re.findall(r'pdf/nomination/\S*_c.html', index_response.text)
date = re.findall(r'\d+', detail_url[0])[0]
detail_url = [root_url + url for url in detail_url]

df_all = pd.DataFrame()
encode_name='utf_8'
for url in detail_url:
    response = requests.get(url)
    response.encoding = encode_name
    df_new = pd.read_html(response.text, header = 0)[0]
    df_all = df_all.append(df_new, ignore_index = True)
    df_all.to_csv('nomination_' + date +'.csv',encoding=encode_name)

print('Data last updated on ' + date + '.')
print('Saved to nomination_' + date + '.csv')
