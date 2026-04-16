class Person:
    def __init__(self,name,age,hight,wight):
        self.name = name
        self.age = age
        self.hight = hight
        self.wight = wight
    
    def eat(self):
        print("eating food")

class Criketor(Person):
    def __init__(self,name,age,hight,wight,team):
        super().__init__(name,age,hight,wight)
        self.team = team
    
    # overwrite the eat method
    def eat(self):
        print("eating healthy food and drink")
    
    # overload the + operator to add the ages of two cricketers
    def __add__(self,other):
        return self.age + other.age
    # overload the * operator to multiply the ages of two cricketers
    def __mul__(self,other):
        return self.age * other.age
    # overload the > operator to compare the ages of two cricketers
    def __gt__(self,other):
        return self.age > other.age


sakib = Criketor("sakib",35,5.9,75,"BD")
sakib.eat()
mushi = Criketor("mushi",36,5.8,70,"BD")
print(mushi+sakib)
print(mushi*sakib)
print(mushi>sakib)