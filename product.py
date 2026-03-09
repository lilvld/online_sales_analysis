
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Produsul {self.name} are pretul: {self.price}, si cantitatea de: {self.quantity}")

    def update_quantity(self, quantity):
        self.quantity = quantity
        print(f"Noua cantitate a {self.name} este: {self.quantity}")