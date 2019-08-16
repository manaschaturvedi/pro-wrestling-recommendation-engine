import requests
from bs4 import BeautifulSoup
import pandas as pd

matches = []
for page_num in range(100):
    url = 'https://www.cagematch.net/?id=111&view=list&s=' + str(page_num)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for elem in soup.findAll('tr', {'class' : 'TRow1'}):
        details = [x.text if index!= 2 else x.find('img', alt=True)['alt']  for index,x in enumerate(elem)]
        matches.append(details)
    print('done for', page_num)

columns = ['ID', 'date', 'promotion', 'match_fixture', 'meltzer_rating', 'match_type', 'rating', 'votes']
df = pd.DataFrame(matches, columns=columns)
df.to_csv('matches.csv')
print(df)