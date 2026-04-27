class Menu:
    def __init__(self):
        self.items = []
    
    def add_menu_item(self,item):
        self.items.append(item)
    
    def find_item(self,item_name):
        for itm in self.items:
            if itm.name.lower()==item_name.lower():
                return itm
        return None

    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"{item} removed")
        else:
            print(f"{item_name} not found")
    
    def show_menu(self):
        print("***Menu***")
        print(f"name\tprice\tquantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")