from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance
    
    def add_to_balance(self, amount):
        self.balance += amount

    @abstractmethod
    def withdraw_money(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self, amount):
        if ((self.balance - amount) < self.min_balance):
            print("You have exceeded your minimum balance.")
        else:
            self.balance -= amount

savings_Account = SavingsAccount(200, 100)
savings_Account.withdraw_money(150)
