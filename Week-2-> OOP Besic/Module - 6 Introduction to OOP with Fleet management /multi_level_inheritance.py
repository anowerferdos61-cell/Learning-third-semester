class Viecle:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def move(self):
        pass

    def __repr__(self):
        return f"(name = {self.name}, price = {self.price})"

class Bus(Viecle):
    def __init__(self, name, price,seat):
        self.seat = seat
        super().__init__(name, price)
    
class Truck(Viecle):
    def __init__(self, name, price, load_capacity):
        self.load_capacity = load_capacity
        super().__init__(name, price)
    
    def __repr__(self):
        return super().__repr__()

class PickupTruck(Truck):
    def __init__(self, name, price, load_capacity,what_will_carry):
        self.what_will_carry = what_will_carry
        super().__init__(name, price, load_capacity)

    def __repr__(self):
        return super().__repr__()

class ACBus(Bus):
    def __init__(self, name, price, seat,temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)


Hanif = ACBus("Hanif",12000000,36,22)
print(Hanif)
print(Hanif.seat)
