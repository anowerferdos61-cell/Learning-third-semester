class Engine:
    def start(self):
        print("Engine started")

class Driver:
    def drive(self,car):
        car.start()
        print("Driving the car")

class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()
        print("Car started")
    def drive(self):
        self.driver.drive(self)

my_car = Car()
my_car.start()
my_car.drive()