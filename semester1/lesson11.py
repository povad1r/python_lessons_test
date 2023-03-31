# a = {1, 3, 5}
# b = {0, 1, 2, 4, 4}

# print('Intersection using &:', a&b)
# print('Intersection useing intersection():', a.intersection(b))

# print('Union using | :', a | b)
# print('Union using:',a.union(b))

# A = {2, 3, 5}
# B = {1, 2, 6}

# print('Difference using -:', A - B)
# print('Difference using difference():', A.difference(B))

# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}
# print(A.issubset(B))

# number = int(input('Enter the number: '))

# a = str(number)

# b = a[::-1]

# pre_result = list(b)

# print(pre_result)

# for i in range(0, len(pre_result)):
#     pre_result[i] = int(pre_result[i])
# print(pre_result)

# string = input()
# count = -1
# main_count = 0
# word = ''
# curr_word = ''
# for i in string:
#         count += 1
#         if i == " ":
#             curr_word = string[main_count:count]
#             main_count = count + 1
#             if len(word) < len(curr_word):
#                 word = curr_word

# print(word)

string = input() + ' '
space = string.find(' ')
if space == -1:
    print(f'У вас лише одне слово у рядку, тому слово {string} буде найдовшим')
else:
    word = string[0:space]
    count = len(string.split())
    print(count)
    for i in range(count):
        space_old = space
        space = string.find(' ', space+1)
        current_word = string[space_old+1:space]
        if len(word) < len(current_word):
            word = current_word
    print(f'{word} - це найдовше слово у вашому рядку')


