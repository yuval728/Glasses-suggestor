import cv2
import os

glasses_list = os.listdir('Glasses')

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

num=1
while True:
    k=cv2.waitKey(10)
    if k == ord('d'):
        num += 1
    if k == ord('a'):
        num -= 1
    if k == ord('q'):
        break
    if k == ord('r'):
        num = 1
    
    if num > len(glasses_list):
        num = 1
        
    overlay = cv2.imread(f'Glasses/{glasses_list[num-1]}', cv2.IMREAD_UNCHANGED)
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        
        overlay = cv2.resize(overlay, (w, int(h*0.8)))
        for i in range(overlay.shape[0]):
            for j in range(overlay.shape[1]):
                if overlay[i, j, 3] != 0:
                    frame[y+i, x+j] = overlay[i, j, 0:3]
    cv2.imshow('Frame', frame)
    
cap.release()
cv2.destroyAllWindows()
    