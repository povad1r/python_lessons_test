# a = 'dafqgglfbshjsj'
# b = list(a)
# print(b)

# some_str = 'This is awesome string'
# print(some_str[0:5]+'aaa')

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = numbers[:-1:2]
# print(numbers[2:-1:3])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[0:6])
# print(numbers[6:])

# b = numbers.copy()
# c = numbers[:]

# print(b)
# print(c)

# print(numbers[-2:])
# print(numbers[:-2])

# print(numbers[::-1])


# pip = 'Ivan Ivanov'
# delimiter = ' '
# space = pip.find(delimiter)
# name = pip[0:space]
# last_name = pip[space+1:]
# print(name, last_name)

# phones = ['+38(067) 999-99-99', '+38(066) 999-99-99','+38(067) 888-88-88', '+38(068) 777-77-77']
# kyivstar = ['067', '097', '068']
# count = 0
# for phone in phones:
#     operator_code = phone[4:7]
#     if operator_code in kyivstar:
#         count+=1 
# print(f'{count} - стільки абонентів київстар у списку')

# a = set('hello')
# b = {1, 2, 3, 4}
# print(b)

# code = {'067', '066', '050', '095', '068'}
# print(code)

# numbers = {1, 2, 3}
# numbers.add(4)
# numbers.remove(3)
# numbers.discard(6)
# print(numbers)


# goods = {'milk', 'eggs', 'bananas', 'mango'}
# print(goods)
# goods.add('apple')
# goods.add('pineapple')
# goods.add('tomato')
# print(goods)
# goods.remove('milk')
# print(goods)
# goods.discard('cucumber')
# print(goods)


# a = set('hello')
# b = set('hi there!')

# print(a)
# print(b)
# print(a^b)
# print(a.difference(b))
# print(a|b)
# print(a.union(b))

# print(a&b)
# print(a.intersection(b))



customers_A = {'Ivanov', 'Petrov', 'Sidorov'}
customers_B = {'Ivanova', 'Petrova', 'Sidorov'}

customers_A_B = customers_A & customers_B
print(customers_A_B)
all_customers = customers_A | customers_B
print(all_customers)
