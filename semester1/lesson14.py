# a = [
#     {'asdqfq' :  132},
#     {'qeqrqfq' :  2123},
#     {'pariruri' : 231123}
# ]
# for bems in a:
#     for key in bems:
#         print(bems[key])

# prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
# if 3 in prime_numbers:
#     print(f'3 входить у вашу множину')
# else:
#     print('3 не входить у вашу множину')

# user = {
#     'name' : 'Bill',
#     'surname' : 'Bosh',
# }
# for key, value in user.items():
#     if key == 'age':
#         if value>=18:
#             print('Ви повнолітній')
#         else: 
#             print('Ви неповнолітній')
#     else:
#         print('У користувача не вказаний вік)
# if 'age' in user.keys():
#     print(f'User {user["name"]}, age - {user["age"]}')
# else:
#     print(f'{user["name"]}, {user["surname"]}')

# password = input('Enter your password: ')
# if len(password)<8:
#     print('The password is too short')
# else:
#     print('ok')

# alphabet = 'abcdefghijklmnopqrstuwxyz'
# for i in alphabet:
#     print(i)

# cities = {
#     'Київ'    : 0, 
#     'Вінниця' : 240, 
#     'Харків'  : 470, 
#     'Ужгород' : 808, 
#     'Львів'   : 540, 
#     'Житомир' : 120, 
#     'Одеса'   : 430
# }
# start_value = 0
# start_city = ''
# for key,value in cities.items():
#     if value>start_value:
#         start_value = value
#         start_city = key
# print(f'{start_city}, {start_value}')


post_ukr = {'Київ', 'Фастів', 'Ірпінь', 'Боярка', 'Харків'}

post_new = {'Київ', 'Фастів', 'Кагарлик', 'Узин', 'Ірпінь', 'Гатне', 'Боярка', 'Гостомель'}

city = input('Enter your city: ')
if city in post_ukr and city in post_new:
    print('Ми можемо відправити УкрПоштою і Новою Поштою')
    choice = input('Оберіть пошту якою ви б хотіли отримати пошту (1-УкрПошта, 2-Нова Пошта): ')
    if choice == '1':
        print('Ми відішлемо посилку УкрПоштою')
    elif choice == '2':
        print('Ми відішлемо посилку Новою Поштою')
elif city in post_ukr:
    print('Ми можемо надіслати вам посилку УкрПоштою')
elif city in post_new:
    print('Ми можемо надіслати вам посилку Новою Поштою')
else:
    print('Ми не можемо надіслати посилку у ваше місто, оберіть самовивіз')