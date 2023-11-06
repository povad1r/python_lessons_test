# class My_class:
#     def __init__(self):
#         self.public_attribute = 'Python'
#         self.__private_attribute = 'Python2'
#         self._protected_attribute = 'Python3'
#
#     def public(self):
#         print('Це публічний метод')
#
#
#     def __private(self):
#         print('Це приватний метод')
#
#
#     def _protected(self):
#         print('Це приватний метод')
#
#
# element_1 = My_class()

# print(element_1.public_attribute)
# print(element_1._protected_attribute)
# print(element_1.__private_attribute)
#
# element_1.public()
# element_1.__private()

class Motor:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print('Мотор запущений')

    def stop(self):
        print('Мотор зупинений')

class Car(Motor):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type

    def start(self):
        print('Машина їде')

class Bike(Motor):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def start(self):
        print('Байк їде')


car1 = Car('BMW', 2023, 'Легкова')
print(car1.year)
print(car1.brand)
print(car1.type)
car1.start()
car1.stop()

bike1 = Bike('Suzuki', 2020, 'Black')
print(bike1.brand)
print(bike1.year)
print(bike1.color)
bike1.start()
bike1.stop()