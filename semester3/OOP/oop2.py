class Animal:
    def walk(self):
        print('I can walk and I can run')

    def eat(self):
        print('I can eat')

    def makeSound(self):
        print('Animal make sound')


class Dog(Animal):
    def bark(self):
        print('I can bite enemy')

    def makeSound(self):
        print('Woof-Woof')


class Cat(Animal):
    def play(self):
        print('I play with tail')

    def makeSound(self):
        print('Meow-Meow')


murka = Cat()
haski = Dog()

murka.walk()
haski.eat()
haski.makeSound()
cat.makeSound()