class BankAccount:
    def __init__(self, name, balance, passport) -> None:
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def __str__(self) -> str:
        return f'User {self.__name} have {self.__balance}'


    def getBalance(self):
        return self.__balance

    def setBalance(self, new_balance):
        if new_balance < '100':
            print('Сума дуже маленька')
        else:
            self.__balance = new_balance

account1 = BankAccount('Sergiy Ivanov', 5000, 'MP676567')

print(account1)
