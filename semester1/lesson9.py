# name = 'bebebe'

# print(name)

# b = 'abcdefg'
# print(len(b))
# print (b.count('ab', 0, 3))
# c = 'BBBBBBBBBBBBBBBBBBBBb'
# print(c.lower())
# c = 'bbbbbbbbbbbbbb'
# print(c.upper())
# c = 'title method'
# print(c.title())
# print(c.capitalize())
# c = 'AjdvsnvKSJDhafnvajkck'
# print(c.swapcase())

# my_string = 'Lorem ipsum dolor sit amet'
# n = int(input())
# if n>len(my_string):
#     print('Wrong input!')
# else:
#     new_string = my_string[n:]
#     print(new_string)

# a = 'I am learning strings in Python. Some new methods got now.'
# sentences = a.split('. ')
# sentences.pop(-1)
# print(sentences)

# dsa = input().split
# print(len(dsa))

# sentences = ["I am learning strings in Python", "Some new methods got now."]
# text = '. '.join(sentences)
# print(text)

# clean = '  spacious  '.strip()
# print(clean)

# dogs_text = 'All dogs bark like dogs'
# cat_text = dogs_text.replace('dogs', 'cats')
# print(cat_text)

# map = {
#     ord('з'): 'z',
#     ord ('р'): 'r'
# }
# translated = 'зр'.translate(map)
# print(translated)

# s = 'Мене звати %s. Мені %d років.' % ('Олег', 14)
# print(s)

# a = input('Enter the string: ')
# print(f'Symbols - {len(a)}')
# b = a.split()
# print(b)
# print(f'Words - {len(b)}')

# print('pi: {:0.6}'.format(3.1415926))

# print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))

# print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))

surname = input('Enter your surname: ')
count_letter = surname.count(surname[0])
letter = surname[0]
for i in surname:
    if surname.count(i)>count_letter:
        letter = i
        count_letter = surname.count(i)
print(f'The letter that occurs the most times({count_letter}) in your surname is - {letter}, ')

string = input('Enter your string: ')
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in string: 
    for j in number_list: 
        if j==i:
            output = string.replace(i, '')
            string = output
print(string)