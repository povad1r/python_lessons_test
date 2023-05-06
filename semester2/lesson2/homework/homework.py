import pandas as pd
data = pd.read_excel('semester2\lesson2\homework\Cake.xlsx', usecols=['Назва продукту', 'Ціна'])
print(data)

data = pd.read_excel('semester2\lesson2\homework\Cake.xlsx')
total_weight = data['Маса(г)'].sum()
total_sum = data['Ціна'].sum()

print(f'Загальна маса = {total_weight}, Загальна ціна = {total_sum}')
