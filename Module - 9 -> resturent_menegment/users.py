from abc import ABC
from order import Order
class user(ABC):
    def __init__(self,name,phone,email,address):
        super().__init__()
        self.name = name
        self.email = email
        self.address = address

class Customer(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("we don\'t have that much")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("item added")
        else:
            print("Item not found")
    
    def view_cart(self):
        print('--- cart ---')
        print("name\tprice\tquantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")

        print(f"total price : {self.cart.total_price()}")
    
    def pay_bill(self):
        print(f'total {self.cart.total_price()} paid sussesfully')

class Employee(user):
    def __init__(self, name, phone, email, address,age,salary,designetion):
        super().__init__(name, phone, email, address)
        self.age = age
        self.salary = salary
        self.designetion = designetion

class Admin(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_employee (self,restaurent,employe):
        restaurent.add_employee(employe)
    
    def view_employe(self,restaurent):
        restaurent.view_employe()
    
    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)
    
    def delet_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

    def show_menu(self,restaurent):
        restaurent.menu.show_menu()