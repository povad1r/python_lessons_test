# class User:
#     def __init__(self, name, last_name, age) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#
#     def print_user(self):
#         print(f"User {self.name} {self.last_name} (age={self.age})")

class Dog:
    def __init__(self, name, age, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print("Woof-Woof")


mops = Dog(name='Tolik', age='3', weight='2kg')
mops.bark()
