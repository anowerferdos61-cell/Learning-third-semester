# readoly --> you can only get the value but you cannot set it.
# getter --> to get the value of private attribute through a method, 
# # we can also use @property decorator to make it more elegant and pythonic.
# setter --> to set the value of private attribute

class user:
    def __init__(self,name,age,money):
        self.name = name
        self._age = age
        self.__money = money
    
    @property
    def get_money(self):
        return self.__money
    
    @get_money.setter #setter for get_money, we can set money
    def get_money(self,money):
        if money < 0:
            print("money cannot be negative")
        self.__money += money
    
    @property  #getter without setter, readonly attribute
    def age(self):
        return self._age

samsu = user("ferdos",24,1000)
print(samsu.age)
print(samsu.get_money)
samsu.get_money = 500
print(samsu.get_money)