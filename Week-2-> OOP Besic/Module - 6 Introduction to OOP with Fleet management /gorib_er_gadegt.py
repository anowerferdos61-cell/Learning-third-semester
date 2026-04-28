# Gorib er gadegt practice 
#  common and uncommon thing and inheritance.

class Gadget:
    def __init__(self, brand, model, price,color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color

    def run(self):
        print(f"{self.brand} {self.model} is running.")


class Laptop:
    def __init__(self,ram):
        self.ram = ram
    
    def coding(self):
        print(f"learning python and practicing coding on {self.brand} {self.model}.")

class Mobile:
    def __init__(self,dual_sim):
        self.dual_sim = dual_sim
    
    def calling(self):
        print(f"calling on {self.brand} {self.model}.")

class Camera:
    def __init__(self,megapixels):
        self.megapixels = megapixels
    
    def change_lens(self):
        print(f"changing lens on {self.brand} {self.model}.")
