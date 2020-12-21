import cv2
import numpy as np

kamera = cv2.VideoCapture(0)


while True:
    ret,resim = kamera.read()


    canny = cv2.Canny(resim,100,200)
    laplacian = cv2.Laplacian(resim,cv2.CV_64F)
    sobel_dikey = cv2.Sobel(resim,cv2.CV_64F,1,0,ksize=5)


    cv2.imshow("cannny",canny)
    cv2.imshow("sobel",sobel_dikey)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


kamera.release()
cv2.destroyAllWindows()
