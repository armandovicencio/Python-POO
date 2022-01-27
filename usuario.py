class User:		# declara una clase y dale el nombre User
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0
               
        # Luego, para instanciar un par de nuevos usuarios:
guido = User()
monty = User()
# Si queremos acceder a los atributos de nuestra instancia,
#  podemos referirnos a ellos desde nuestras instancias por nombre:
print(guido.name)	# salida: Michael
print(monty.name)	# salida: Michael

# También podemos establecer los valores para los atributos de nuestra instancia:
guido.name = "Guido"
monty.name = "Monty"

print(guido.name)	# salida: Michael
print(monty.name)	# salida: Michael

