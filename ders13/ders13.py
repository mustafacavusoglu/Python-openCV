import cv2
import numpy as np


kamera = cv2.VideoCapture(0)

dusuk = np.array([98, 110, 110])
yuksek = np.array([103, 255, 255])

while True:

    ret, goruntu = kamera.read()

    hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)




    mask = cv2.inRange(hsv, dusuk, yuksek)
    son = cv2.bitwise_and(goruntu, goruntu, mask=mask)


    #smoothed
    kernel = np.ones((15,15),dtype=np.float32) /225
    smoothed = cv2.filter2D(son,-1,kernel)


    #blured
    blur = cv2.GaussianBlur(son,(15,15),0,)

    #median
    median = cv2.medianBlur(son,13)


    #bilateral
    bilateral = cv2.bilateralFilter(son,15,75,75)




   
    cv2.imshow("son", son)
    #cv2.imshow("smoothed",smoothed)
    #cv2.imshow("blur",blur)
    #cv2.imshow("median",median)
    cv2.imshow("bilateral",median)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()