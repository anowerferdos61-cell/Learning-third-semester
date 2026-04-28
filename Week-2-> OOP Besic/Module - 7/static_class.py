class Shoping:
    cart = [] # static variable
    origin = 'India'
    def __init__(self, name,location):
        self.name = name # instance variable
        self.location = location
    
    def perchase(self,item,price,amount):
        remaining_amount = price - amount
        print(f"you have to pay {remaining_amount} for {amount} {item}")
    
    @staticmethod
    def multiply(a,b):
        return a*b

    @classmethod
    def hudai_dekhi(self,item):
        print(f"kinbo na hudai dekhi {item} from {self.origin}")

shop1 = Shoping("shop1","Dhaka")
shop1.perchase("apple",100,5)
Shoping.perchase("banana",2,3,4)
shop1.hudai_dekhi("orange")
Shoping.hudai_dekhi("grapes")