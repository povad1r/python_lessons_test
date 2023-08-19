# class Person():
#     name = ''
#     age = 0
#     gender = ''

#     def say_hello(self):
#         print(f'Hello, my name is {self.name}')

# person1 = Person()
# person1.name = 'Yaroslav'
# person1.age = 16
# person1.gender = 'Male'

# print(person1.name)
# person1.say_hello()
# print(person1.__dict__)

# class Animal():
#     name = ''
#     age = 0
#     sound = ''   

#     def say_sound(self):
#         print(f'{self.name} say {self.sound}') 
#     def say_info(self):
#         print(f'Hello my name is {self.name} and I am {self.age} years old')

# cat = Animal()
# cat.name = 'Mice'
# cat.age = 10
# cat.sound = 'Meow'
# cat.say_sound()

# dog = Animal()
# dog.name = 'Casper'
# dog.age = 3
# dog.sound = 'Gav'
# dog.say_sound()

# class Book():
#     name = ''
#     author = ''
#     year = 0
#     genre = ''
#     def __str__(self):
#         return f"{self.name} ({self.year}) - {self.author} ({self.genre})"

# class Library():
#     def __init__(self):
#         self.collection_of_books = []

#     def add_book(self, book):
#         self.collection_of_books.append(book)

#     def delete_book(self, book):
#         self.collection_of_books.remove(book)

# Book1 = Book()
# Book1.name = 'Harry Potter'
# Book1.author = 'J.Rowling' 
# Book1.year = 1997
# Book1.genre = 'fantasy'

# Book2 = Book()
# Book2.name = 'Murder on the Orient Express'
# Book2.author = 'A.Kristy'
# Book2.year = 1933
# Book2.genre = 'detective'

# Book3 = Book()
# Book3.name = 'The Little Prince'
# Book3.author = 'A.de Saint-Exupéry'
# Book3.year = 1943
# Book3.genre = 'Children`s literature'

# library = Library()

# library.add_book(Book1)
# library.add_book(Book2)
# library.add_book(Book3)
# print("\nList of books in the library:")
# for book in library.collection_of_books:
#     print(book)
# choice = input('Do you want to remove book?Y or N ')
# if choice == 'Y':
#     remove_book = input('Enter the name of Book which you want to delete: ')
#     for book in library.collection_of_books:
#         if book.name == remove_book:
#             library.delete_book(book)
#             break
#     print("\nList of books in the library after removal:")
#     for book in library.collection_of_books:
#         print(book)
# elif choice == 'N':
#     print('List of books in the library:')
#     for book in library.collection_of_books:
#         print(book)
# else:
#     print('Incorrect! Enter either "Y" or "N"')


# class Bank_Account:
#     def __init__(self, owner_name: str, account_number: int, balance: int):
#         self.owner_name = owner_name   
#         self.account_number = account_number
#         self.balance = balance


#     def add_money(self, invoice):
#         self.balance += invoice
#         print(f'Now your balance is: {self.balance}')

#     def withdrawal(self):
#         money = int(input('How much money you want to withdraw? '))
#         if money > self.balance:
#             print('You can`t withdraw this amount')
#         else: 
#             print(f'Now your balance is {self.balance-money}')

# Account1 = Bank_Account(owner_name='Yaroslav', account_number=1234, balance=5000)
# Account1.add_money(2000)

