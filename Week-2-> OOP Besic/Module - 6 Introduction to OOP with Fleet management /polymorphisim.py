# poly -- > many (multiple forms)
# morphism --> shape or form

class Animal:
    def __init__(self,name):
        self.name = name
    
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    # def make_sound(self):
    #     print("gheu! gheu!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print("meow! meow!")

don = Cat("Don")
don.make_sound()
dog = Dog("Rex")
don2 = Cat("Don2")

animals = [don, dog, don2]

for animal in animals:
    animal.make_sound()
