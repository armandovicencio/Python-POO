from .productos import Producto
from .tienda import Tienda

def test_store():
    tienda = Tienda("Toy store")
    tienda.add_product(Producto("barbie", 7.77, "doll"))
    tienda.add_product(Producto("g i joe", 4.77, "doll"))
    tienda.add_product(Producto("Zelda II: The adventure of Link", 50.3, "video game", sku="abcdef"))

    tienda.inventory()
    tienda.set_clearance('doll', 50)
    tienda.inventory()

    tienda.sell_product(sku="abcdef")
    tienda.sell_product(id=0)
    tienda.inventory()

print(Tienda.inventory())