import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
url = 'https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches'

source = requests.get(url)
def convert_to_eest(date):
    date_format = datetime.strptime(date, '%B %d, %Y - %H:%M %Z')
    date_result = date_format + timedelta(hours=3)
    result = date_result.strftime('%B %d, %Y - %H:%M %Z')
    return result
def get_content():
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'html.parser')
    exact_time = soup.find_all('span', class_="timer-object timer-object-countdown-only")
    left_team = soup.find_all('td', class_="team-left")
    right_team = soup.find_all('td', class_="team-right")
    tournament = soup.find_all('td', class_="match-filler")
    matches = []
    for i in range(5):
        exactly = convert_to_eest(exact_time[i].text)
        team_1 = left_team[i].find('a')['title'].split('(')
        team_2 = right_team[i].find('a')['title'].split('(')
        tourn = tournament[i].find('a')['title']
        # date = exactly.split(',')[0]
        match = {
            'time': exactly,
            'team_1': team_1[0],
            'team_2': team_2[0],
            'tournament': tourn,
            # 'date': date
        }
        if match not in matches:
            matches.append(match)
    return matches
get_content()

# def generate_notification():
#     content = get_content(source)
#     notifications = []
#     for i in range(5):
#         notification = f"{content[i]['team_1']} vs {content[i]['team_2']}, {content[i]['time']}, {content[i]['tournament']}"
#         notifications.append(notification)
#     print(notifications)
#     return notifications
# generate_notification()