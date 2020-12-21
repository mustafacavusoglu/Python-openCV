import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

dusuk = np.array([95,50,50])
yuksek = np.array([103,255,255])

while True: 

    ret,goruntu = kamera.read()

    hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)

   

    mask = cv2.inRange(hsv,dusuk,yuksek)
    son = cv2.bitwise_and(goruntu,goruntu, mask=mask)

    #cv2.imshow("goruntu",goruntu)
    cv2.imshow("hue--stration--value",hsv)
    cv2.imshow("son",son)
    #cv2.imshow("mask",mask)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()