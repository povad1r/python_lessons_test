# class Author:
#     def __init__(self, name):
#         self.name = name
#
#     def write(self):
#         print(f'{self.name} пише книгу')
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def read(self):
#         print(f'{self.title} - назва книги')
#         print(f'{self.author.name}')
#
# author1 = Author('Тарас Шевченко')
# book1 = Book('Кобзар', author1)
# book1.read()


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r * self.r * 3.14

