# clients = [
#     ['White House', 'Іванов', 3],
#     ['Shelter', 'Іванова', 5], 
#     ['Верховина', 'Іванова', 5], 
#     ['Буковель', 'Іванова', 5],
#     ['Shelter', 'Іванова', 7]
# ]

# hotels = dict()

# for voucher in clients:
#     voucher_hotel = voucher[0]
#     voucher_clients = voucher[2]
#     if hotels.get(voucher_hotel, 0) == 0: 
#         hotels[voucher_hotel] = voucher_clients
#     else:
#         hotels[voucher_hotel] += voucher_clients

# for hotel, clients in hotels.items():
#     print(f'У готелі {hotel} наразі проживає {clients} клієнтів ')

# def say_hello():
#     print('Hello, World')
# say_hello()

# def name():
#     print('Yaroslav Rogovets')
# name()

# def print_sum(a,b):
#     a = 7
#     b = 9 
#     print(a+b)
# print_sum(7,9)

# def draw_box():
#     print('*' * 10)
#     for i in range(12):
#         print('*' + ' ' * 8 + '*')
#     print('*' * 10)
# draw_box()

# def draw_triangle():
#     count = 0
#     for i in range(10):
#         count += 1
#         print('*' * count)
# draw_triangle()

# def draw_triangle():
#     for i in range(10):
#         i += 1
#         print('*' * i)
# draw_triangle()

# def draw_triangle(x):
#     for i in range(x):
#         i += 1
#         print('*' * i)
# draw_triangle(15)

# def print_max(a,b):
#     if a>b:
#         print(f'Max - {a}')
#     elif a == b:
#         print('They are equal')
#     else:
#         print(f'Max - {b}')
# x = 8
# y = 98
# print_max(x,y)

# surname = input('Enter your surname: ')
# def congratulations(surname):
#     print(f'{surname} - вітаємо ')
# congratulations(surname)

# def plus (a,b):
#     result = a + b
#     return result
# plus(3,4)

# def sum(a,b):
#     return a + b

# def subtraction(a,b):
#     return a - b

# def power(a,b):
#     return a ** b

# def multiply(a,b):
#     return a*b

# def calculation(operand_A, operand_B, operator):
#     if operator not in ['+', '-', '*', '^']:
#         print('Invalid operator')
#     else:
#         match operator:
#             case '+':
#                 result = sum(operand_A, operand_B)
#             case '-':
#                 result = subtraction(operand_A, operand_B)
#             case '^':
#                 result = power(operand_A, operand_B)
#             case '*':
#                 result = multiply(operand_A, operand_B)
#         print(operand_A, operator, operand_B, '=', result)

# a = float(input('Enter your number: '))
# b = float(input('Enter your number: '))
# print('Available operators - [+, -, ^, *]')
# operator = input('Enter your operation: ')
# calculation(a, b, operator)

string = input('Enter your string: ').lower()
char_count = {
}
for char in string:
    if char != ' ':
        if char not in char_count:
            char_count[char] = string.count(char)

# chars = list(char_count.items())

# for i in range(len(chars)):
#     for j in range(i + 1, len(chars)):
#         if chars[j][1] > chars[i][1]:
#             chars[i], chars[j] = chars[j], chars[i]

# for item in chars[:3]:
#     print(f'Letter {item[0]} was used {item[1]} times')

counter_list = sorted(list(char_count.items()), key=lambda x: x[1])
counter_list.reverse()
for element in counter_list[:3]:
    print(f'{element[0]} - {element[1]}')