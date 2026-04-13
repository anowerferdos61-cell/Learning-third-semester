# Ena Poribahan
# Fleet Management System

class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.drivers = []
        self.bus = []
        self.routes = []
        self.counter = []
        self.supervisor = []

class Driver:
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number
class Bus:
    def __init__(self, bus_number, capacity):
        self.bus_number = bus_number
        self.capacity = capacity

class Route:
    def __init__(self, route_number, start, destination):
        self.route_number = route_number
    def purchase_ticket(self, passenger_name,start, destination):
        pass

class Counter:
    def __init__(self, location):
        self.location = location

class Supervisor:
    def __init__(self, name):
        self.name = name

red_mia = Driver("Red Mia", "DL12345")
