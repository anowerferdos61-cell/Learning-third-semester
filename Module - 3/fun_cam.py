import cv2
import pyautogui
import time
import numpy as np

print("🎉 মজার Webcam Effects চালু হচ্ছে...")
print("Exit করতে 'q' চাপো")
print("রং পরিবর্তন: 'c' | স্ক্রিনশট: 's' | মিরর অন/অফ: 'm'")

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

mirror = True
color_mode = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    if mirror:
        frame = cv2.flip(frame, 1)
    
    # বিভিন্ন মজার ইফেক্ট
    if color_mode == 0:
        effect = frame
        title = "Normal"
    elif color_mode == 1:
        effect = cv2.bitwise_not(frame)          # Negative
        title = "Negative"
    elif color_mode == 2:
        effect = cv2.applyColorMap(frame, cv2.COLORMAP_JET)   # Thermal
        title = "Thermal"
    elif color_mode == 3:
        effect = cv2.applyColorMap(frame, cv2.COLORMAP_WINTER)
        title = "Cool"
    elif color_mode == 4:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        effect = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        effect = cv2.Canny(effect, 80, 150)
        effect = cv2.cvtColor(effect, cv2.COLOR_GRAY2BGR)
        title = "Sketch"
    
    cv2.putText(effect, f"Effect: {title}", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
    
    cv2.imshow("😂 Fun Webcam Effects", effect)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        color_mode = (color_mode + 1) % 5
    elif key == ord('m'):
        mirror = not mirror
        print("মিরর মোড পরিবর্তন হয়েছে")
    elif key == ord('s'):
        filename = f"screenshot_{time.strftime('%H-%M-%S')}.png"
        cv2.imwrite(filename, effect)
        print(f"✅ স্ক্রিনশট সেভ হয়েছে: {filename}")
        # pyautogui দিয়ে ছোট নোটিফিকেশন
        pyautogui.alert(text=f"স্ক্রিনশট সেভ হয়েছে!\n{filename}", title="Virtual Cam", button="OK")

cap.release()
cv2.destroyAllWindows()