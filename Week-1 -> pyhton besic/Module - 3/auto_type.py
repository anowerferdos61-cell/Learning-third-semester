# import pyautogui
# import time
# time.sleep(5)
# for i in range(0,3):
#     pyautogui.write('i love coding',interval=.25)
#     pyautogui.press('enter')


import pyautogui
import time

print("where you want to write")

time.sleep(5)

messages = [
    "Bro000000"
]

for msg in messages * 10:
    pyautogui.typewrite(msg + "\n")
    time.sleep(1.5) 

# import pyautogui
# import time
# import random

# print("মাউস ডান্স শুরু হচ্ছে... ৮ সেকেন্ড পর শুরু। Stop করতে Ctrl + C চাপো")

# time.sleep(8)

# for i in range(30):        # ৩০ বার ডান্স করবে
#     x = random.randint(100, 1000)
#     y = random.randint(100, 700)
#     pyautogui.moveTo(x, y, duration=0.3)
#     time.sleep(0.2)
    
# print("finis!")