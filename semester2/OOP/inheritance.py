class Vehicle:
    def __init__(self, brand, year) -> None:
        self.brand = brand
        self.year = year

    def drive(self):
        print('The vehicle is in motion')

    def stop(self):
        print('The vehicle has stopped')

class Car(Vehicle):
    def __init__(self, brand, year, fuel_type) -> None:
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    def drive(self):
        print('The car is driving on the road.')

class Bicycle(Vehicle):
    def __init__(self, brand, year, color, _serial_id) -> None:
        super().__init__(brand, year)
        self.color = color
        self._serial_id = _serial_id
    
    def drive(self):
        print('The bicycle is driving on the grass')
        

bicycle1 = Bicycle('Hero', 2016, 'Black')
bicycle1.drive()