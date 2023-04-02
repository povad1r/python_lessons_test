# bytes = b'Hello'
# print(bytes[0])

# bytes_str = 'Hello World!'.encode()

# print(list(bytes_str))

# numbers = [0, 128, 255]
# bytes_numbers = bytes(numbers)
# print(bytes_numbers)

# for i in numbers:
    # print(hex(i))

# symbol = 'a'
# print(ord(symbol))
# symbol_bytes = 97
# print(chr(symbol_bytes))

# check = ['⚓', '🐔', '🥚', '🐍']
# print(sorted(check))
# a = '🐔'.encode()
# b = '🥚'.encode()
# print(a > b)

with open('semester1/lesson25/data.bin', 'wb') as file:
    file.write(b'Hello World!')