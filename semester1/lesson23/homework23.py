file = open('semester1/lesson23/test.txt', 'a')
while True:
    name = input('Enter your name: ')
    if name == 'q':
        break
    file.write(name+'\n')
file.close() 
