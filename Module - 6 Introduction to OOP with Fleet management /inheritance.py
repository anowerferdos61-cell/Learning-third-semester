class Gadget:
    def __init__(self, brand, model, price,color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color

    def run(self):
        print(f"{self.brand} {self.model} is running.")


class Laptop(Gadget):
    def __init__(self, brand, model, price, color, ram):
        self.ram = ram
        super().__init__(brand, model, price, color)


    def coding(self):
        print(f"learning python and practicing coding on {self.brand} {self.model}.")
    
    def __repr__(self):
        return f"Laptop(brand={self.brand}, model={self.model}, price={self.price}, color={self.color}, ram={self.ram}\n"

class Mobile(Gadget):
    def __init__(self, brand, model, price, color, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, model, price, color)
    
    def calling(self):
        print(f"calling on {self.brand} {self.model}.")
    
    def __repr__(self):
        return f"Mobile(brand={self.brand}, model={self.model}, price={self.price}, color={self.color}, dual_sim={self.dual_sim}\n"

class Camera:
    def __init__(self,megapixels):
        self.megapixels = megapixels
    
    def change_lens(self):
        print(f"changing lens on {self.brand} {self.model}.")

# inheritance


my_laptop = Laptop("Dell", "XPS 15", 1500, "Silver", "16GB")
my_laptop.run()
my_laptop.coding()
print(my_laptop)

my_mobile = Mobile("apple",'iPhone 13',120000,'white',True)
my_mobile.run()
my_mobile.calling()
print(my_mobile)