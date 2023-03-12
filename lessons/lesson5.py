#word = 'apple'
#for char in word:
#    print(char, sep='-')

#print('aaa', 'sfsf', sep='---')

#numbers = [int(i) for i in input().split()]

#numbers = input().split()

#for number in numbers:
#    int(number)
#print(numbers)

#print(type(numbers))

#sum = 0 

#for number in numbers:
#    print(number)
#    sum += number

#print(sum)

#colors = ['red', 'green', 'blue', 'yellow']
#for color in colors:
#    print(color)
#else: 
#    print('Done!')

#numbers = [1, 3, 2, 45, 22, 664]
#for number in numbers:
#    if number % 2 == 0:
#        print(number)

#start = int(input(f'Enter your start number: '))
#end = int(input('Enter your last number: '))
#sum = 0 
#for i in range(0, end+1):
#    print(i)
#    sum += i
#else: 
#    print(sum)

#for i in range(1,11):
#    for j in range(1,11):
#        print(i*j, end = ' ')
#
#    print('')

#max = int(input('The size of the table: '))

#for row in range(1, max+1):
#    for column in range(1, max+1):
#        print(column*row, end = '\t')
#
#    print('')

#a = 1 

#while a<=5:
#    a+=2
#    print(a)

#max = int(input('Enter your last number: '))
#sum = 0
#count = 0 

#for a in range(0,max):
#    if a % 3 == 0:
#        sum += a
#        count += 1 
#print(f'AVG = {sum / count}')

#a = 0 
#while True: 
#    print(a)
#    if a>= 20:
#        break
#    a = a + 1

#while True:
#    name = input('Enter name: ')
#    if name == 'stop':
#        print('Stopped!')
#        break
#    print('Hello', name)

#a = 0
#while a < 6:
#    a = a + 1 
#    if not a % 2: 
#        continue
#    print(a)

#while True: 
#    i = int(input())
#
#    if i>100:
#        break
#    if i<20:
#        continue

#sum = 0
#for i in range(1,100+1):
#        if i % 2 != 0:
#            sum += i 
#print(sum)


count = 0
word = input(f'Enter your word: ')
for i in word:
    first_letter = i
    break
for i in word:
    if first_letter == i:
        count += 1
print(count)