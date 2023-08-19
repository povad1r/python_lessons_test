import sqlite3
import requests
from bs4 import BeautifulSoup as bs



def create_table(name):
    connection = sqlite3.connect("C:semester2/sqlite3/database.db")
    cursor = connection.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name}
                    (id INTEGER PRIMARY KEY, name VARCHAR NOT NULL, price FLOAT NOT NULL);''')
    connection.commit()
    connection.close()
create_table('cur')

def add_data(name, price):
    connection = sqlite3.connect("C:semester2/sqlite3/database.db")
    cursor = connection.cursor()
    cursor.execute('''INSERT into cur (name, price) VALUES (?, ?);''', (name, price))
    connection.commit()
    connection.close()

def get_data():
    connection = sqlite3.connect("C:semester2/sqlite3/database.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cur;')
    data = cursor.fetchall()
    connection.close()
    return print(data)

URL_TEMPLATE = "https://privatbank.ua/rates-archive"
r = requests.get(URL_TEMPLATE)
def parse():
    soup = bs(r.text, "html.parser")
    cur = soup.find_all('div', class_='purchase')
    name = soup.find_all('div', class_='names')
    curr = []
    names = []
    count = 0
    for a in cur:
        count += 1
        if count < 4: 
            curr.append(float(a.span.text))
    count2 = 0
    for b in name:
        if count2 < 3:  
            names.append(b.span.text.split()[0])
            count2 += 1
    number = 0
    for a in range(3):
        add_data(names[number], curr[number])
        number += 1


    get_data()