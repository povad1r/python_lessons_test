#number = float(input('Enter your number: '))
#if number % 1 == 0:
#    print('Integer')
#else:
#    print('Float')
#kind_of_number = 'Integer' if number % 1 == 0 else 'Float'
#print(kind_of_number)

#number = float(input('Enter your number: '))
#if number % 5 == 0 or number % 10 == 0:
#    print(f'Ваше число ділиться націло на 5 або на 10')
#else:
#    print(f'Ваше число не ділиться націло на 5 або на 10')

#side_1 = float(input(f'Enter your 1 side: '))
#side_2 = float(input(f'Enter your 2 side: '))

#if side_1 == side_2:
#    print(f'This is square')
#else:
#    measurement = int(input(f'What do you want to measure? 1 - area 2 - perimeter: '))
#    if measurement == 1:
#        print(f'Area is {side_1*side_2}')
#    elif measurement == 2:
#        print(f'Perimeter is {2*(side_1*side_2)}')
#    else:
#        print('Wrong input!')

#day = int(input(f'Enter your day of birth: '))
#month = int(input(f'Enter your month of birth: '))
#if month>=13 or day>=32:
#    print(f'Wrong information!')
#elif month == 2 and day>=29:
#    print(f'Wrong information')
#else:
#    print(f'Your date of birth is {day}.{month}')

#date_of_birth = 'Wrong information' if month>=13 or day>=32 else f'Your date of birth is {day}{month}'
#print(date_of_birth)

#week_day = int(input(f'Day: '))
#if week_day == 1:
#    print('Monday')
#elif week_day == 2:
#    print('Tuesday')
#elif week_day == 3:
#    print('Wednesday')
#elif week_day == 4:
#    print('Thursday')
#elif week_day == 5:
#    print('Friday')
#elif week_day == 6:
#    print('Saturday')
#elif week_day == 7:
#    print('Sunday')
#else:
#    print('Wrong input!')

#match week_day:
#    case 1:
#        print('Monday')
#    case 2:
#        print('Tuesday')
#    case 3:
#        print('Wednesday')
#    case 4:
#        print('Thursday')
#    case 5:
#        print('Friday')
#    case 6:
#        print('Saturday')
#    case 7:
#        print('Sunday')
#    case _:
#        print('Wrong input!')

#number_1 = int(input(f'Enter first number: '))
#number_2 = int(input(f'Enter second number: '))

#print(number_1+number_2)
#print(f'{number_1}{number_2}')

#name = input('Enter your name: ')
#city = input('Enter your city: ')
#city1 = 'з міста '
#hello = 'Привіт '
#print(hello + name + city1 + city)

#name = input('Enter your name: ')
#if not name: 
#    print('Ви не ввели ім\'я тому не отримаєте знижку')
#elif name == 'Андрій':
#    print('Ви отримуєте знижку "25%"')
#else:
#    print('Ви отримуєте знижку "15%"')

#number = float(input('Enter your number: '))
#print("even") if number % 2 == 0 else print('Це число не парне ')

#a = int(input('Enter your first angle: '))
#b = int(input('Enter your second angle: '))
#c  = int(input('Enter your third angle: '))
#if a+b+c==180:
#    print('Your triangle is valid')
#    if a>b and a>c:
#        print(f'{a} це найбільший кут')
#    elif b>a and b>c:
#        print(f'{b} це найбільший кут')
#    elif c>a and c>b:
#        print(f'{c} це найбільший кут')
#    else:
#        print('Всі кути рівні')
#else:
#    print('Your triangle is not valid')

a = int(input('Enter your first side: '))
b = int(input('Enter your second side: '))
c  = int(input('Enter your third side: '))
if a+b<=c:
    print('Your triangle is not valid')
elif a+c<=b:
    print('Your triangle is not valid')
elif c+b<=a:
    print('Your triangle is not valid')
else:
    print('Your triangle is valid')