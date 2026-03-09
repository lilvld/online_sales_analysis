
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def total_price(self):
        total = 0
        for product in self.cart_items:
            total += product.price
        return f"Valoarea totala a cosului: {total}"

    def show_cart(self):
        for product in self.cart_items:
            print(product.name, product.price)