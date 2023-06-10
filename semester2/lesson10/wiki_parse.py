import requests 
from bs4 import BeautifulSoup

response = requests.get('https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D1%96%D0%B2_%D1%81%D1%82%D0%B0%D0%BD%D1%83_HTTP')
soup = BeautifulSoup(response.content, 'html.parser')

for row in soup.select(".toclevel-1 > a"):
    a = f"{row.text.strip()}\n"
    print(a)