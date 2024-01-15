class Product:
    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    def show(self):
        return print("PRODUCT INFORMATION:\nProduct ID: {}\nProduct Name: {}\nPrice: PHP {}".format(self.product_id, self.product_name, self.product_price))

    def change_price(self, product_price):
        self.product_price = product_price
        return print("New Price: PHP {}".format(self.product_price))

Milkshake = Product("110822", "Milkshake", 50)