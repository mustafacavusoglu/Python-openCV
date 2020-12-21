import cv2
import numpy as np

kamera = cv2.VideoCapture(0)


while True:
    ret,kare = kamera.read()


    gri_kare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    nesne = cv2.imread("gozluk.jpg",0)

    h,w = nesne.shape
    res = cv2.matchTemplate(gri_kare,nesne,cv2.TM_CCOEFF_NORMED)
    esik_deger = 0.7

    loc = np.where(res>esik_deger)

    for n in zip(*loc[::-1]):
        cv2.rectangle(kare,n,(n[0]+w,n[1]+h),(0,0,255),2)
        cv2.putText(kare,"gozluk kutusu",(n[0]+13,n[1]-15),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
    cv2.imshow("kare",kare)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()

