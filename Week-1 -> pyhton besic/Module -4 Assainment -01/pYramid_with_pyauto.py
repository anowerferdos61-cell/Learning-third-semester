import pyautogui
import time

n = int(input("enter a number"))
time.sleep(5)
for i in range(1, n + 1):
    space = " " * (n - i)
    hash = "# " * i
    print(space + hash)
    pyautogui.typewrite(space + hash)
    pyautogui.press("enter")