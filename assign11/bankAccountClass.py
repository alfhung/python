# define a type to represent a single bank account
class BankAccount:

    # construct a BankAccount object with balance
    # provided by the parameter
    def __init__(self, balance):
        self.__balance = balance

    # access an accounts balance
    def getBalance(self):
        return self.__balance

    # make a deposit of the amount provided
    # by the parameter
    def deposit(self, amount):
        self.__balance = self.__balance + amount

    # make a withdrawal of the amount provided
    # by the parameter, if there are sufficient funds
    # returns True if withdrawal made, else returns False
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            return True
        else:
            return False

