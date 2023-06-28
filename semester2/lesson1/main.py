# file = open("semester2\lesson1\my_name.txt", 'w')
# file.write('My name is Yaroslav')
# file.close()

# file = open("semester2\lesson1\my_name.txt", 'a')
# file.write('\n\nI am 15')
# file.close()

# file = open("semester2\lesson1\my_name.txt", 'r')
# # info = file.read(22)
# # print(repr(info))
# # print(info)
# print(file.readlines()[::-1])
# file.close()

file = open("semester2\lesson1\my_name.txt", 'w')
file.write('My name is Yaroslav\n\nI am 15\n\nI live in Kyiv')
file.close()

file = open("semester2\lesson1\my_name.txt", 'a')
file.write('\n\nI have dog')
file.close()

file = open("semester2\lesson1\my_name.txt", 'r')
print(file.readlines()[0:3])
file.close()

