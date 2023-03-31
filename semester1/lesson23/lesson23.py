import random

# a = 5
# while a !=0:
#     print(a)
#     a -= 1

# while True: 
#     username = input('Enter your name: ')
#     if username == '0':
#         break
#     else:
#         print(username)

# b = [1, 2, 3]
# a = random.choice(b)
# print(a)
# random_number = random.randint(0, 20)
# print(random_number)

# def greeting(name):
#     return f'Hello {name}!'

# print(greeting('Ivan'))

# def greetings(name, number, *args, **kwargs):
#     greetings_string = f'Hello {name}!'
#     print(args)
#     print(kwargs)
#     result = [greetings_string, number, sum(args), kwargs]
#     return result

# a = greetings('Yaroslav', 1,2,3,4,5,22,23,45,76, b=6, c='John', d=123)
# print(a)
# numbers = [6, 2, 1, 8, 10]
# def minmax ():
#     start_a = numbers[0]
#     start_b = numbers[0]
#     sum = 0
#     for a in numbers:
#         if a > start_a:
#             start_a = a
#     sum+=start_a
#     for b in numbers:
#         if b < start_b:
#             start_b = b
#     sum+=start_b
#     numbers.remove(start_b)
#     numbers.remove(start_a)
#     return sum 
# print(minmax())

# def minmax():
#     sum_minmax = 0
#     sum_minmax += min(numbers) 
#     sum_minmax += max(numbers)
#     numbers.remove(max(numbers))
#     numbers.remove(min(numbers))
#     return sum_minmax
# print(minmax())

# def sum_left():
#     sum2 = 0
#     for number in numbers: 
#         sum2+=number
#     return sum2
# print(sum_left())

# def func(list):
#     return {
#         'sum_of_max_and_min': max(list) + min(list),
#         'sum_of_the_rest': sum(list) - max(list) - min(list)
#     }

# file = open('lessons/lesson23/test.txt', 'w')
# symbols_written = file.write('hello!')
# print(symbols_written)
# file.close()

# file = open('lessons/lesson23/test.txt', 'w+')
# file.write('hello!')
# file.seek(0)

# first_two_symbols = file.read(2)
# print(first_two_symbols)
# file.close()

# file = open('lessons/lesson23/test.txt', 'w')
# file.write('Hello\nWorld')
# file.close()

# file = open('lessons/lesson23/test.txt', 'r')
# all_file = file.read()
# print(all_file)
# file.close

# file = open('lessons/lesson23/test.txt', 'w')
# file.write('Hello\nWorld')
# file.close()

# file = open('lessons/lesson23/test.txt', 'r')
# while True:
#     symbol = file.read(1)
#     if len(symbol) == 0:
#         break
#     print(symbol)

# file.close()