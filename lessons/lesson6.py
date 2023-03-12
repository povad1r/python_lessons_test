#sum = 0
#for number in range(1,100+1):
#    if number % 2 != 0:
#        print(number)
#        sum += number

#print('sum:', sum)

#count = 0
#word = input(f'Enter your word: ')
#for i in word:
#    first_letter = i
#    break
#for i in word:
#    if first_letter == i:
#        count += 1
#print(f'Amount of your letters {first_letter} {count}')

#my_list = [1, 4, [1, 24, [1, 3, 5], 5]]
#last_element_of_second_list = my_list[2][2][0]
#print(last_element_of_second_list)

#print(my_list)

#my_list = ['a', 'b', 'c']
#print(my_list)

#numbers = '1' '2' '3'
#numbers_list = list(numbers)
#print(numbers_list)
#my_list1 = list(('1','2','3'))

#age = int(input(f'Enter your age: '))
#fio_list = ['Ivan', 'Ivanov', {age},]
#print(fio_list)

#iterable = list('Python')
#first_element = iterable[0]
#second_element = iterable[1]
#last_element = iterable[5]
#print(iterable)
#print(first_element)
#print(second_element)
#print(last_element)

#my_list = [1, 2, 3, 5, 7, 10, 11, 23, 43, 65]
#my_list.pop(1)
#extension = [4, 6, 9]
#my_list.extend(extension)
#my_list.insert(1,2)    
#my_list.sort(reverse=True)

#print(len(my_list))

#copy_list = my_list.copy()
#print(copy_list)

#if 2 in my_list:
#    print('Okay')
#else:
#    print('Bad')

#for element in sorted(my_list):
#    print(element)

#goods = []
#sold_goods = []

#while True:
#    match = input('Вітаю в нашому магазині!\n Для показу всіх товарів натисніть 1.\n Для постачання товарів натисніть 2.\n Для продажу товарів натисніть 3. \n Для виводу проданних товарів за день натисніть 4. \n Для перегляду історії продажів натисніть 5. \n Для виходу натисніть 0: ')
#    if match == '0':
#        print('Thank you!')
#        break
#    elif match == '1':
#        for good in goods:
#            print(good)
#    elif match == '2':
#        print('Products delivery')
#        product = input('Enter product you would like to deliver: ')
#        goods.append(product)
#    elif match == '3':
#        print('Selling goods')
#        product = input('Enter the product you would like to buy')
#        goods.remove(product)
#    elif match == '4':
#        for good in sold_goods:
#            print(good)
#    elif match == '5':
#        for good in sold_goods.reverse():
#            print(good)


west_list = ['South America', 'North America', 'Antarctica']
print(f'{west_list} mainlands that located in western hemispehere')
east_list = ['Eurasia', 'Africa', 'Australia']
print(f'{east_list} mainlands that located in eastern hemisphere')
west_list.extend(east_list)
west_list.sort()
print(f'{west_list} each mainland that is on Earth sorted alphabetically')

name_list = [['Serhii', 'Petrenko'],['Andrii', 'Maksymuk'],['Andrii', 'Kornienko'],['Vasyl', 'Chernyak'],['Nikita', 'Smirnov']]
count = 0
for element in name_list:
    if element[0] == 'Andrii':
        count += 1
print(count)