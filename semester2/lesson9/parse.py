import requests
from bs4 import BeautifulSoup as bs
# response = requests.get('http://quotes.toscrape.com/')
# soup = bs(response.content, 'html.parser')

# for post in soup.select('.text'):
#     for author in soup.select('.author'):
#         print(author.text, post.text)

response = requests.get('http://start.karazin.ua/page/dopushcheni#reiting')
soup = bs(response.content, "html.parser")


with open('semester2\\lesson9\\file.txt', 'w+', encoding='utf=8') as file:
    for row in soup.select(".right-nav.table-cell.ic-evaluation > .item > a"):
        a = f"{row.text} - {row.get('href')}\n"
        file.write(a)
