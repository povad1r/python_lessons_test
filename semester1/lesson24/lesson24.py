# file = open('semester1/lesson24/test.txt', 'w')
# file.write('hello\n')
# file.writelines(['world\n'])
# file.write('world!\n')
# file.close()

# file = open('semester1/lesson24/test.txt')
# split = open('semester1/lesson24/split.txt', 'w')
# for char in file.read():
#     split.write(char + '\n')


# while True:
#     symbol = file.read(1)
#     if len(symbol) == 0:
#         print('The end of the file')
#         break
#     else:
#         print(symbol)
#         split.write(symbol + '\n')
# file.close()
# split.close()

file = open('semester1/lesson24/test.txt', 'r')
# print(fh.read(2))
file.seek(2)
print(file.read(1))
file.close()