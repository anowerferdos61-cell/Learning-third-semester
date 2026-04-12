class Pen:
    manufacturer_area = "new market"
    def __init__(self, color, tip_size, price,brand):
        self.color = color
        self.tip_size = tip_size
        self.price = price
        self.brand = brand

    def write(self, text):
        print(f"Writing '{text}' with a {self.color} pen of tip size {self.tip_size}.")

my_pen = Pen ('black',.5,10,'matador')
print(my_pen.color,my_pen.tip_size,my_pen.price,my_pen.brand)
my_pen.write("Hello, how are you?")

her_pen = Pen('blue', 0.6,11, 'pin-point')
print(her_pen.color, her_pen.tip_size, her_pen.price, her_pen.brand)
her_pen.write("This is a blue pen with a tip size of 0.6.")