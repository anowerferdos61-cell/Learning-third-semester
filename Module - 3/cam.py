import cv2
import numpy as np

print("🎥 Webcam চালু হচ্ছে... Exit করতে 'q' চাপো")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # ফ্রেম মিরর করা
    frame = cv2.flip(frame, 1)
    
    # মজার ফিল্টার
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    # Cartoon Effect
    cartoon = cv2.stylization(frame, sigma_s=60, sigma_r=0.45)
    
    # অনেকগুলো মজার ইফেক্ট দেখানো হচ্ছে
    effects = {
        "Original": frame,
        "Cartoon": cartoon,
        "Negative": cv2.bitwise_not(frame),
        "Sketch": cv2.cvtColor(cv2.Canny(gray, 80, 150), cv2.COLOR_GRAY2BGR),
        "Warm": cv2.applyColorMap(frame, cv2.COLORMAP_AUTUMN),
        "Cool": cv2.applyColorMap(frame, cv2.COLORMAP_WINTER)
    }
    
    # একসাথে দেখানোর জন্য ছোট করে সাজানো
    top_row = np.hstack((effects["Original"], effects["Cartoon"]))
    bottom_row = np.hstack((effects["Negative"], effects["Sketch"]))
    combined = np.vstack((top_row, bottom_row))
    
    cv2.imshow("😂 Funny Webcam Effects - Press 'q' to Exit", combined)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()