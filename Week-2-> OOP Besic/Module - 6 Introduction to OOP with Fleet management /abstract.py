from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod # enforce all child class to have or implement eat method
    
    def eat(self):
        print("Animal is eating")

class Monkey(Animal):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def eat(self):
        print("hey nana ! i am eating banana\n")

monkey = Monkey("George")
monkey.eat()
