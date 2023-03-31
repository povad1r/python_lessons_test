#age = int(input('Your age: '))
#if age>=18:
#    print('You are adult!')
#else:
#    print('You are infant!')

#a = int(input('Enter the number: '))
#a = int(a)
#if a>0:
#    print('Число додатнє')
#elif a<0:
#    print('Число від\'ємне')
#else:
#    print('Число - 0')

#money = 1
#if not money:
#    print('You have no money')
#else:
#    print(f'Balance = {money}')

#name = input('Your name: ')
#if not name:
#    print(f'Hello Anonymous')
#else:
#    print(f'Hello {name}!')

#name = 'Ivan'
#age = 19
#has_driver_license = False
#if age>=18 and has_driver_license:
#    print(f'{name} може орендувати авто')
#else:
#    print(f'{name} не може орендувати авто')

#print(True and True)
#print(1 or None)
#print(not 2<0)

#year = int(input(f'Your year: '))
#if (year % 400 == 0) or (year % 4 == 0 and year % 100!= 0):
#    print(f'{year} - високосний рік')
#else:
#    print(f'{year} - не високосний')

#is_nice = False
#state = 'nice' if is_nice else 'bad'
#print(state)

#a = 12
#b = 8
#c = a if a>b else b
#print(c)

#x = int(input('Enter x: '))
#y = int(input('Enter y: '))

#if x>=0:
#    if y>=0:
#        print(f'1 чверть')
#    else:
#        print(f'4 чверть')
#else:
#    if y>=0:
#        print(f'2 чверть')
#    else:
#        print(f'3 чверть')

x = int(input('Enter x: '))
y = int(input('Enter y: '))

if y>=0:
    if x>=0:
        print(f'I чверть')
    else:
        print(f'II чверть')
else:
    if x>=0:
        print(f'IV чверть')
    else:
        print(f'III чверть')

surname = input(f'Enter your surname: ')
score = int(input(f'Enter your score: '))
if score>80:
    print(f'{surname} склав іспит')
else:
    print(f'Іспит не складено') 