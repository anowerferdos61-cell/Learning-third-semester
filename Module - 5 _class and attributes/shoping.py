class Shoping:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        self.cart = []
    
    def add_to_cart(self,item,quantity,price):
        self.cart.append((item, quantity, price))
    
    def remove_from_cart(self,item,quantity):
        for item_in_cart in self.cart:
            if item_in_cart[0] == item and item_in_cart[1] >= quantity:
                self.cart.remove(item_in_cart)
                break
        else:
            print(f"{item} with quantity {quantity} not found in cart.")

    def calculate_total(self):
        total = 0
        for item, quantity, price in self.cart:
            total += quantity * price           
            if total > self.amount:
                print(f"please add more {self.amount - total} to your account to complete the purchase.")
        print(f'total price of items in cart: {total}')
            
    
shoping1 = Shoping("Anower", 1000)
shoping1.add_to_cart("jira", 1, 500)
shoping1.add_to_cart("alu", 5, 70)
shoping1.add_to_cart("rice", 4,100)
shoping1.add_to_cart("sugar", 2, 50)
# shoping1.calculate_total()
shoping1.remove_from_cart("alu", 7)
shoping1.calculate_total()