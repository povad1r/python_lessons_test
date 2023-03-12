# def func(a, b):
#     c = (a**2 + b**2)
#     print(c**0.5)
# func(3,4)

# import math

# def func(a, b):
#     c = sqrt()

# def function(list):
#     return print(sum(list)/len(list))

# function([1,3,4,5,6,7,8])


# def function(str):
#     return print(len(str))

# function('abcdefghijklmnoprstqu')

# def function(dict, key):
#     return print(dict.get(key))

# dict = {'tomato': 1, 'tea': 2, 'milk': 3}
# key = 'milk'
# function(dict, key)

# def function(str):
#     return str[::-1]
# print(function('abvcfjkrjq'))

def function(str):
    reverse = ''
    for i in range(len(str)-1, 0, -1):
        reverse += str[i]
    return reverse
print(function('abvcfjk'))




