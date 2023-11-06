from datetime import datetime, timedelta

class Human:
    def __init__(self, title, hp, stamina, speed, level, attack, reload) -> None:
        self.title = title
        self.hp = hp
        self.stamina = stamina
        self.speed = speed
        self.level = level
        self.attack = attack
        self.reload = reload
        self.last_attack = None

    def __str__(self) -> str:
        return f'Race: {self.title}'

    def check_attack(self):
        if self.last_attack and datetime.now()-self.last_attack < timedelta(microseconds=self.reload):
            return False
        else:
            return True

    def attack_func(self):
        if self.check_attack():
            self.last_attack = datetime.now()
            return self.last_attack
        else:
            print('Please wait')
            return 0



class Archer(Human):
    def __init__(self, level) -> None:
        self.title = "Archer"
        super().__init__(self.title, 80 + level*20, 95 + level*5, 3, level, 40+level*5, 3)


class Warrior(Human):
    def __init__(self, level) -> None:
        self.title = "Warrior"
        super().__init__(self.title, 100 + level*40, 95 + level*5, 1, level, 30+level*10, 5)


class Wizard(Human):
    def __init__(self, level) -> None:
        self.title = "Wizard"
        super().__init__(self.title, 50 + level*20, 95 + level*5, 2, level, 70+level*15, 10)