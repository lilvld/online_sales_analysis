from product import Product
from product_manager import ProductManager

manager = ProductManager()

laptop = Product("Laptop", 649, 10)
mouse = Product("Mouse", 14, 25)
tastatura = Product("Tastatura", 39, 30)

manager.add_product(laptop)
manager.add_product(mouse)
manager.add_product(tastatura)

manager.show_products()

print(manager.total_value())