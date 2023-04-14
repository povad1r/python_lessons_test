import requests
from bs4 import BeautifulSoup
import datetime 
url = 'https://liquipedia.net/dota2/DreamLeague/Season_19/Group_Stage_1#Matches'

source = requests.get(url)

def get_content(source):
    soup = BeautifulSoup(source.content, 'html.parser')
    exact_time = soup.find_all('div', 'match-countdown-block')
    team_names = soup.find_all('div', 'brkts-popup-header-opponent')
    date_names = soup.find_all('span', 'timer-object-date')
    print(len(date_names))
    matches = []
    for teams in range(0, len(team_names), 2):
        if teams == 112:
            break
        else:
            if teams<33:
                date_names = 'April 9'
            elif 65>teams>33:
                date_names = 'April 10'
            elif 97>teams>65:
                date_names = 'April 11'
            elif 112>teams>97:
                date_names = 'April 12'
            match = {
                'team_1': team_names[teams].text.strip().split('\n')[0],
                'team_2': team_names[teams+1].text.strip().split('\n')[0],
                'date': date_names,
                'exact_time': exact_time[teams//2].text.strip()
        }
            matches.append(match)
    return print(matches)
get_content(source)
