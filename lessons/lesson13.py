# currencies = {
#     'USD': 36.9,
#     'EUR': 38.18,
#     'GBP': 43.87
# }
# currencies['PLN'] = 8.18
# currencies['USD'] = 39
# currencies['EUR'] = 41
# currencies['GBP'] = 44
# currencies['CNY'] = 5.3
# currencies['CAD'] = 27.03
# currencies['AUD'] = 25.05
# print(currencies)

# currency = input('Enter the currency you would like to exchange: ')
# if currency not in currencies.keys():
#     print('We can not exchange this currency')
# else:
#     amount = float(input('How much money you would like to exchange: '))
#     result = round(amount*currencies[currency], 2)
#     print('Here is your {} UAH'.format(result))

# numbers = {
#     1: 'one',
#     2: 'two',
#     3: 'three'
# }

# for i in numbers:
#     print(i)

# for i in numbers.keys():
#     print(i)

# for i in numbers.values():
#     print(i)

# for key, value in numbers.items():
#     print(key, value)

# for key in numbers.keys():
#     numbers[key] = numbers[key]*2

# print(numbers)

# transport = {
#     'AA1111AA': 'Іванов Іван',
#     'IVANOV'  : 'Іванов Іван',
#     'AA0007AA': 'Семенов Андрій',
#     'AA007AA' : 'Іванов Іван',
#     'AВ1111AВ': 'Вінниця Водоканал',
#     'AІ1010КК': 'Семенов Андрій',
# }

# transport['II6767AO'] = 'Петренко Петро'
# transport['CA8888CE'] = 'Іванов Олексій'

# car_plate = input('Enter the plate to find car owner: ')

# car_owner = transport.get(car_plate, 'Not found')
# print('Car owner of plate {} is {}'.format(car_plate, car_owner))
# car_owners = dict()
# # {'Ivanov': 1, 'Petrov': 2}
# for owner in transport.values():
#     if car_owners.get(owner, 0) == 0:
#         car_owners[owner] = 1
#     else:
#         auto_count = car_owners[owner]
#         auto_count += 1
#         car_owners[owner] = auto_count

# for owner, auto_count in car_owners.items():
#     if auto_count>1:
#         print(f'Owner {owner} has {auto_count} cars')

marks = {
    'Petrenko' : 5,
    'Vasilenko' : 4,
    'Kyrylenko' : 3,
    'Matvienko' : 2,
    'Logvinenko' : 4
}
excellent_grades = dict()
for surname,mark in marks.items():
    if mark >= 4:
        excellent_grades[surname] = mark
print(excellent_grades)

temperature = {
    'Kyiv' : 12,
    'London' : 3,
    'Budapest' : 6,
    'Warszawa' : 8,
    'Berlin' : 5,
    'Paris' : 13
}
total_temperature = 0
count = 0
for temperature in temperature.values():
    count+=1
    total_temperature += temperature
average = total_temperature/count
print(round(average, 2))
