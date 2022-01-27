class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate =int_rate
        self.balance =balance

    def deposit(self, amount):	
        self.balance += amount	
        return self

    def withdraw (self, amount):
        if self.balance > 0:
            self.balance -= amount
            return self

    def display_account_info(self): 
        print(self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
           self.balance += self.balance * self.int_rate
           return self

account1= BankAccount()
account2= BankAccount()

account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest()
account1.display_account_info()
account2.deposit(400).deposit(400).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest()
account2.display_account_info()





