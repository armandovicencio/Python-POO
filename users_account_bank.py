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


class User:

    MAXIMO= 4

    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.accounts = BankAccount(int_rate=0.02, balance=0)	# agregó esta línea
    
    def get_account(self,bankAccount):
              
        if len(self.accounts) < self.MAXIMO:
            self.accounts.append(bankAccount)
        else:
            print(f"Superaste el maximo de {self.MAXIMO} cuentas.")
            return self


    
    def depositar(self,indice, amount):
    	
        self.accounts[indice].account_balance += amount	
        return self


    def make_withdrawal (self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self): 
        print(f"{self.name} tiene {self.account_balance} en su saldo")
        return self
    def transfer_money (self, other_user, amount):
        if amount < 0:
            raise ValueError("transferencia debe ser positiva")
        self.make_withdrawal(amount)
        other_user.account_balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# salida: 300
print(monty.account_balance)	# salida: 50

## make_withdrawal (self, amount) : haz que este método disminuya el saldo del usuario 
# en la cantidad especificada
guido.make_withdrawal(100)      # salida: 200
print(guido.account_balance)

# display_user_balance (self) : haz que este método imprima el nombre del usuario 
# y el saldo de la cuenta en el terminal

guido.display_user_balance()

# BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario 
# en la cantidad y agrega esa cantidad al saldo de otro other_user

guido.transfer_money(monty,500)
guido.display_user_balance()
monty.display_user_balance()

amaranta = User("Amaranta", "amaranta@gmail.com")
antonela = User("Antonela", "antonela@gmail.com")
franco = User("franco", "franco@gmail.com")




guido.make_deposit(1).make_deposit(1).make_deposit(1).make_withdrawal(5).display_user_balance()
monty.make_deposit(5).make_deposit(5).make_withdrawal(3).make_withdrawal(3).display_user_balance()

franco.make_deposit(34)
franco.display_user_balance()

monty.transfer_money(antonela, 2).display_user_balance()
monty.display_user_balance()