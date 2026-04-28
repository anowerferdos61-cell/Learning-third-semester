class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self,name):
        self.name = name
        self.products = []

    def add_product(self,product):
        self.products.append(product)

    def buy_product(self,product_name,quantity):
        for product in self.products:
            if product.name == product_name:
                payable_amount = product.price * quantity
                print(f"congratulations you have bought {product_name} {quantity} units--> {payable_amount} taka\n")
                return
        print(f"sorry {product_name} is not available in the shop")

shop = Shop('Anower\'s shop')
p1 = Product('rice',50)
shop.add_product(p1)

p2 = Product('sugar',120)
shop.add_product(p2)

p3 = Product('salt',42)
shop.add_product(p3)
shop.buy_product('rice',2)
shop.buy_product('sugar',3)
shop.buy_product('salt',1)
shop.buy_product('oil',1)