from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            product.display_info()

    def total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return f"Valoarea totala este de: {total}"

    def remove_product(self, name):
        self.products = [i for i in self.products if i.name != name]