# import random  
# num = random.randint(1, 100)
# print(f"Random integer between 1 and 10: {num}")

# import datetime
# date = datetime.date.today()
# print(date)
# time = datetime.datetime.now().time()
# print (time)

# import calendar
# cal = calendar.calendar(1971)
# print(cal)


# import getpass

# username = input("Username: ")
# password = getpass.getpass(prompt="Password: ")

# if username == "admin" and password == "1234":
#     print("Login সফল!")
# else:
#     print("ভুল username বা password!")


# import getpass
# import time

# print("System initializing...")
# time.sleep(2)

# print("Loading security module...")
# time.sleep(1.5)

# print("Ready!\n")

# password = getpass.getpass(prompt="Password: ")
# print("Password নেওয়া হয়েছে!")
import turtle

t = turtle.Turtle()
t.speed(3)
t.color("blue")
t.penup()
t.goto(-100, 0)
t.pendown()

t.write("Hello, Geeks!", font=("Arial", 30, "bold"))

turtle.done()