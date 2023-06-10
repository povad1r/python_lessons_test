import requests
from bs4 import BeautifulSoup

response = requests.get('http://yermilovcentre.org/medias/')
soup = BeautifulSoup(response.content, 'html.parser')

for media in soup.select('.row-fluid > .col-6 > a'):
    print(f'{media.text.strip()} - http://yermilovcentre.org{media.get("href")}')