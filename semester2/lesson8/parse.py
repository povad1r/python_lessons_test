from bs4 import BeautifulSoup

with open('semester2\lesson8\index.html') as file:
    soup = BeautifulSoup(file, 'html.parser')
hobbies = soup.select_one('.hobbies').find_next('ul').text.strip()
plans = soup.select_one('.plans').find_next('ol').text.strip()
print(f'Hobbies: \n{hobbies}\n\nPlans for the future: \n{plans}')
