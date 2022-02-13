class Producto():
    def __init__(self, precio, name, peso, brand, costo):
        self.precio = precio
        self.name = name
        self.peso = peso
        self.brand = brand
        self.costo = costo
        self.status = "a la venta"
    def sell(self):
        self.status = "vendido"
        return self
    def add_tax(self,tax):
        self.precio += self.precio * tax
        return self
    def returns(self, reason):
        if reason == "defectuoso":
            self.status = "defectuoso"
            self.precio = 0
            return self
        elif reason == "in box":
            self.status = "a la venta"
            return self
        elif reason == "abrió":
            self.status = "usado"
            self.precio -= self.precio * 0.2
            return self
    def display_info(self):
        print ("Precio: $" + str(self.precio))
        print ("Nombre: " + str(self.name))
        print("Peso: " + str(self.peso) + " gs")
        print ("Marca: " + str(self.brand))
        print ("Costo: $" + str(self.costo))
        print ("Status: " + str(self.status))

shirt = Producto(30, "camisa", 2, "Arrow", 30)
shirt.add_tax(.15).sell().display_info()
pants = Producto(50, "jeans", 2, "Levi's", 40)
pants.add_tax(.20).sell().returns("defectuoso").display_info()
cigar = Producto(25, "kent", 2, "fuma otras cosas", 20)
cigar.add_tax(.10).sell().returns("abrió").display_info()