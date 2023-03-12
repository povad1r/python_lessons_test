# a = 'My_awesome_string'
# b = 'My_awesome_string'
# song = '''
# Jingle bells, jingle bells
# Jingle all the way'''
# print(b)
# print(song)

# # an integer to a String
# s = str(15)
# print(type(s))

# # a list to a string
# s = str([12, 11])
# print(type(s))

# s = 'ABCDEFGHI'
# first_element = s[0]
# last_element = s[-1]
# e = s[4]
# print(e)

# a = 'Ovanov Ivan'
# first_element_surname = a[0]
# first_element_name = a[-4]
# if first_element_name == first_element_surname:
#     print(f'Перші літери вашого ім\'я та прізвища співпадають!')
# else:
#     print(f'Перші літери вашого ім\'я та прізвища не співпадають!')

# s = 'abcdefghijk'

# print(s[3:5])

# print(s[:6])

# print(s[3:])

# print(s[-1:-6:-2])

# is_palindrome = 'otto'

# if is_palindrome == is_palindrome[::-1]:
#     print(True)
# else:
#     print(False)

# my_list = [1, 2, 3]

# my_list[0] = 4 

# print(my_list)

# s = 'abcdefghijk'

# s[0] = 'z'

# a = 'Hello, '
# b = 'World'

# print(a+b)

# delimeter = '-' * 25
# print(len(delimeter))

# song = ' Jingle bells, jingle bells\n Jingle all the way\n Oh, what fun it is to ride\n In a one horse open sleigh'
# print(song)
# for char in song:
#     print(char)

# a = 'Hello world'
# print(a.lower())
# print(a.upper())
# print(a.capitalize())
# print(a.swapcase())
# print(a.title())
# print(a.swapcase().title())

# s = 'Hi there!'
# start = 0
# end = 5

# print(s.find('er', 0, 7))
# print(s.find('i'))

# e = 'Big, bigger, biggest'
# x = e.rfind('big')
# print(big)

stop_words = ['купити', 'продати', 'реклама']
sms = input('Enter your message: ')

for stop_word in stop_words:
    if sms.find(stop_word) != -1:
        print('It is spam message!')
        break
else: 
    print(f'It is not spam')