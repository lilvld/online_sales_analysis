from product import Product
from product_manager import ProductManager

manager = ProductManager()

laptop = Product("Calculator", 1200, 3)
mouse = Product("Mouse Wireless", 30, 15)
tastatura = Product("Tastatura", 39, 30)

manager.add_product(laptop)
manager.add_product(mouse)
manager.add_product(tastatura)
