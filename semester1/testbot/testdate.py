import requests
from bs4 import BeautifulSoup

url = 'https://liquipedia.net/dota2/DreamLeague/Season_19/Group_Stage_1#Matches'

source = requests.get(url)

soup = BeautifulSoup(source.content, 'html.parser')

date_names = soup.find_all('div', 'brkts-matchlist-title')
date_base = []

for date in date_names:
    date_value = {
        'date': date.text.strip().split('-')
    }
    date_base.append(date_value)
for i in range(len(date_names)):
    if i >=len(date_names):
        break
    print(date_base[i]['date'])
