class BankAccount:
    def __init__(self, interes = 0.1):
        self.account_balance=0
        self.interes = interes

    def deposit(self,amount):
        self.account_balance += amount
        return self

    def withdraw(self,amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"balance: {self.account_balance}")
        return self

    def yield_interest(self):
        self.account_balance += self.account_balance*self.interes
        return self

account1= BankAccount()
account2= BankAccount()

account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest()
account1.display_account_info()
account2.deposit(400).deposit(400).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest()
account2.display_account_info()

class User:

    MAXIMO = 3

    def __init__(self, username,lastName, email_address):
        self.name = username
        self.lastName = lastName
        self.email = email_address
        self.accounts = []

    def agregar_cuenta(self, bankAccount):
        if len(self.accounts) < self.MAXIMO:
            self.accounts.append(bankAccount)
        else:
            print(f"Superaste el maximo de {self.MAXIMO} cuentas.")
            return self

    def deposito(self, indice, amount=0):
        self.accounts[indice].account_balance += amount

    def retiro(self, amount=0):
        self.account_balance -= amount

    def balance(self):
        print(f"El Balance de {self.name} {self.lastName} es {self.account_balance} Dolares")
    
amaranta = User("Amaranta","Vicencio", "amaranta@gmail.com")
anto = User("Anto","Vicencio", "anto@gmail.com")
franco = User ("Franco","Franco", "Franco@gmail.com")

print(amaranta.balance)
print(anto.balance)

amaranta.deposito(100)
amaranta.deposito(200)
anto.deposito(50)
print(amaranta.balance)	
print(anto.balance)
