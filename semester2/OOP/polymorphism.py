# class Shape:
#     def area(self):
#         print('It returns area')

#     def calc_area(self):
#         print('It returns area')


# class Rectangular(Shape):
#     def __init__(self, a, b) -> None:
#         super().__init__()
#         self.a = a
#         self.b = b

#     def calc_area(self):
#         self.area = self.a * self.b
#         return self.area
    

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__()
#         self.r = radius

#     def calc_area(self):
#         self.area = 3.14 * self.r**2
#         return self.area

# c = Circle(4)
# print(c.calc_area())

class Shape:
    def perimeter(self):
        print('It returns perimeter')

    def calc_perimeter(self):
        print('It returns perimeter')


class Rectangular(Shape):
    def __init__(self, a, b) -> None:
        super().__init__()
        self.a = a
        self.b = b

    def calc_perimeter(self):
        self.perimeter = (self.a + self.b) * 2
        return self.perimeter
    

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.r = radius

    def calc_perimeter(self):
        self.perimeter = 3.14 * self.r * 2
        return self.perimeter
    
c = Circle(3)
print(c.calc_perimeter())