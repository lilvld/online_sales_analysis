from product import Product
from product_manager import ProductManager

from cart import Cart
import random

manager = ProductManager()
cart = Cart()
products = manager.products

laptop = Product("Laptop", 649, 10)
mouse = Product("Mouse", 14, 25)
tastatura = Product("Tastatura", 39, 30)

manager.add_product(laptop)
manager.add_product(mouse)
manager.add_product(tastatura)

manager.show_products()

print(manager.total_value(), "\n")

selected = random.sample(products, 3)

for i in selected:
    cart.add_to_cart(i)

cart.show_cart()

print(cart.total_price(), "\n")
