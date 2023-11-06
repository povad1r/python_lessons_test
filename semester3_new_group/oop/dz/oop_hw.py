class Menu:
    def __init__(self, price, mass):
        self.price = price
        self.mass = mass

    def start(self):
        print('Меню принесли')

    def stop(self):
        print('Меню забрали')


class Soup(Menu):
    def __init__(self, price, mass, secret_ingredient):
        super().__init__(price, mass)
        self.__secret_ingredient = secret_ingredient

    def bring_soup(self):
        print('Суп принесли')

    def take_soup(self):
        print('Суп забрали')

    def __private(self):
        print('Суп має невідомий секретний інгредієнт')


class Meat(Menu):
    def __init__(self, price, mass, type):
        super().__init__(price, mass)
        self._type = type

    def bring_meat(self):
        print('М\'ясо принесли')

    def take_meat(self):
        print('М\'ясо забрали')

    def _protected(self):
        print('Кодове слово 123')

borsch = Soup('150UAH', '300g', 'beet')
print(borsch.price, borsch.mass)


steak = Meat('300UAH', '400g', 'beef')
print(steak.price, steak.mass)

