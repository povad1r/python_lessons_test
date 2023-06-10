import requests
from bs4 import BeautifulSoup as bs


response = requests.get('http://books.toscrape.com/')
soup = bs(response.content, "html.parser")


with open('semester2\\lesson10\\file.txt', 'w+', encoding='utf-8') as file:
    for row in soup.select(".product_pod > h3 > a"):
        a = f"{row.text} - {row.get('href')}\n"
        file.write(a)
