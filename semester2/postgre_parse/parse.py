from bs4 import BeautifulSoup as bs
import requests


HEADERS = {
    "User-Agent":  'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
}
URL_TEMPLATE = 'https://comfy.ua/smartfon/brand__apple/'
response = requests.get(URL_TEMPLATE, headers=HEADERS)

soup = bs(response.content, "html.parser")
devices = soup.select('div.products-list-item')


for device in devices:
    item = {
        "name": device.select_one('.products-list-item__name').text,
        "code": device.select_one('.products-list-item__code').text.strip().replace('Код: ', ''),
        "old_price": int(device.select_one('.products-list-item__actions-price-old').text[:20].replace('₴', '').replace('\n', '').replace(' ', '').strip()),
        "current_price": int(device.select_one('.products-list-item__actions-price-current').text[:20].replace('₴', '').replace('\n', '').replace(' ', '').strip()),
        "reviews": int(device.select_one('.products-list-item__reviews').text)
    }
    print(item)