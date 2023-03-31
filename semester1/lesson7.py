#import random

#my_list = [1, 66, 8, 30, 2, 2, 2]
#sum = 0 

#for element in my_list:
#    sum+=element
#print(sum(my_list))
#multi = 1
#for element in my_list:
#    multi*=element
#print(multi)

#max = 0

#for element in my_list:
#    if element > max:
#        max = element
#print(max)
#print(max(my_list))
#print(min(my_list))

#my_list = ['abc', 'xyz', 'aba', '1221']
#count = 0 
#for element in my_list:
#    if len(element) >= 2 and element[0] == element[-1]:
#        print(element)
#        count += 1
#print(count)


#list_1 = [1,2,3,4,5]
#list_2 = [5,6,7,8,9]

#result = False

#for j in list_1:
#    for i in list_2:
#        if i == j:
#            result = True
#            break

#print(result)

#color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#for element in color_list:
#    if element == 'Green' or element == 'Red':
#        color_list.remove(element)
#print(color_list)

#number_list = [7,8, 120, 25, 44, 20, 27]
#for number in number_list:
#    if number % 2 != 0:
#        number_list.remove(number)

#print(f'Result: {number_list}')

#while True:
#    name = input(f'Enter your name:')
#    if name == '':
#        name = input(f'Enter your name:')
#    else:
#        print(f'{name} is very beatiful name')
#        break

#while True:
#    name = input(f'Enter your name:')
#    if name:
#        print(f'{name}')
#        break
#    else:
#        print('Ім\'я не введено')

#random_number = random.randint(0,5)

#while True:
#    guess = int(input(f'Try to guess the number from 0-5: '))
#    if guess == random_number:
#        print('Congratulations')
#        break
#    else: 
#        print('Try again')

#name = input('Enter your name: ')
#surname = input('Enter your surname: ')
#symbol_count = 0
#for element in name:
#    symbol_count += 1
#for element in surname:
#    symbol_count += 1 
#print(symbol_count)

#name = input('Enter your name: ')
#surname = input('Enter your surname: ')
#name = list(f'{name}')
#surname = list(f'{surname}')
#name.extend(surname)
#count = 0
#for element in name:
#    count += 1
#print(count)

#my_list = [1, 2, [3, 4, 7, 3, 1, 3, 6, 8, 0]]
#print(my_list)
#for element in my_list:
#    if type(element) == list:
#        element.sort()
#        print(element)
#print(my_list)