class User:
    def __init__(self, username, email_address):# ahora nuestro método tiene 2 parametros!
        self.name = username			#y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		# y el atributo email
        self.account_balance = 0		# el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer parámetro

    # agrega el método deposit 
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
    	
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self


    def make_withdrawal (self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self): 
        print(f"{self.name} tiene {self.account_balance}" "en su saldo")
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

