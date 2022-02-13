class Tienda():
    def __init__(self,productos,origen,vendedor):
        self.productos = productos
        self.origen = origen
        self.vendedor = vendedor
    def add_product(self,productos):
        self.productos.append(productos)
        return self
    def remove_product(self, producto):
        self.productos.remove(producto)
        return self
    def inventory(self):
        print ("Productos:", self.productos)
        return self
    def store_info(self):
        print ("Informacion")
        print ("Vendedor: " + str(self.origen))
        return self
tienda1 = Tienda(["camisas","cigarros","pantalones","alcohol"], " Providencia s/n, Santiago", "ClandestinoOK")
tienda1.store_info()
tienda1.add_product("vino").inventory()
tienda1.remove_product("camisas").inventory()
tienda1.add_product("vodka").remove_product("pantalones").store_info().inventory()





# update_price(self, percent_change, is_increased) : 
# actualiza el precio del producto.
# Si is_increased es True, el precio debería aumentar
# en el porcentaje de cambio proporcionado. 
# Si es False, el precio debe disminuir en el cambio porcentual 
# proporcionado.

            