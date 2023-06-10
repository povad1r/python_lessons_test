import requests
from bs4 import BeautifulSoup

# response = requests.get('https://www.univ.kiev.ua/ua/departments')
# soup = BeautifulSoup(response.content, 'html.parser')

# for faculties in soup.select_one('.b-references'):
#     print(faculties.text.strip())

# response = requests.get('https://shop.karazin.ua/kantselyariya/')
# soup = BeautifulSoup(response.content, 'html.parser')

# for item in soup.select('.catalogCard-info'):
#     print(item.text.strip())

# response = requests.get('https://uk.wikipedia.org/wiki/%D0%9C%D1%83%D0%B7%D0%B5%D1%97_%D0%9A%D0%B8%D1%94%D0%B2%D0%B0')
# soup = BeautifulSoup(response.content, 'html.parser')

# for row in soup.select('td > b > a'):
#     print(row.text)