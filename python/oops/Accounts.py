#Example of account class
class Account():
    counter = 0
    def __init__(self, holder, number, balance,credit_line=1500):
        self.__Holder = holder
        self.Number = number
        self.__Balance = balance
        self.__CreditLine = credit_line
        

    def deposit(self, amount):
        self.Balance = amount

    def withdraw(self, amount):
        if(self.Balance - amount < self.CreditLine):
            # coverage insufficient
            return False
        else:
            self.Balance -= amount
            return True

    def balance(self):
        return self.__Balance

    def transfer(self, target, amount):
        if(self.Balance-amount<self.CreditLine):
            # coverage insufficient
            return False
        else:
            self.Balance -= amount
            target.Balance += amount
            return True
'''
from Accounts import Account
a1 = Account('Arun',1234,100)
print ('Balance in account 1:',a1.balance())
a2 = Account('Techcovery',1234,100)
print('Balance in account 2:',a2.balance())
print('Class Variable Counter:',Account.counter)
'''


#Example 2 - Init and Develete methods
class Greeting:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print("Destructor started")
    def SayHello(self):
        print("Hello", self.name)
'''
from Accounts import Greeting

x1 = Greeting("Guido")
x2 = x1
del x1
del x2
'''
