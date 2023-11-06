from gameRPG import Wizard, Archer, Warrior
from datetime import datetime, timedelta


print('Welcome to the game')
name = input('Enter your name: ')
answer = 0

while answer not in [1, 2, 3]:
    answer = int(input('Choose your role\n1: Archer\n2: Warrior\n3: Wizard '))
    if answer == 1:
        hero = Archer(1)
    elif answer == 2:
        hero = Warrior(1)
    elif answer == 3:
        hero = Wizard(1)
    else:
        print('Error! Try again')

print(hero)
enemy1 = Warrior(1)
print(enemy1.hp)
enemy1.hp -= hero.attack_func()
enemy1.hp -= hero.attack_func()
print(enemy1.hp)