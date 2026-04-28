# class Shop:
    # cart =[]  # cart is a class attribute.
#     def __init__(self,buyer):
#         self.buyer = buyer
    
#     def add_to_cart(self,itens):
#         self.cart.append(itens)
        
# mehjabeen_shop = Shop("Mehjabeen")
# mehjabeen_shop.add_to_cart("phone")
# mehjabeen_shop.add_to_cart("laptop")
# print(mehjabeen_shop.buyer)
# print(mehjabeen_shop.cart)

# samira_shop = Shop("Samira")
# samira_shop.add_to_cart("tablet")
# print(samira_shop.buyer)
# print(samira_shop.cart) 

class Shop:
    shoping_mall = "jamuna future park"

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []  # cart is an instance attribute.
    
    def add_to_cart(self,items):
        self.cart.append(items)

mehjabeen_shop = Shop("Mehjabeen")
mehjabeen_shop.add_to_cart("phone")
mehjabeen_shop.add_to_cart("laptop")
print(mehjabeen_shop.buyer,"\n",mehjabeen_shop.cart)

samira_shop = Shop("Samira")
samira_shop.add_to_cart("tablet")
samira_shop.add_to_cart("headphones")
samira_shop.add_to_cart("smartwatch")
print(samira_shop.buyer,"\n",samira_shop.cart)