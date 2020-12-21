import cv2
import numpy as np 



kamera = cv2.VideoCapture(0)

dusuk =np.array([78,85,85])
yuksek = np.array([100,255,255])



while True:
    ret,goruntu = kamera.read()

    hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv,dusuk,yuksek)

    son_resim = cv2.bitwise_and(goruntu,goruntu,mask=mask)

    kernel = np.ones((5,5),np.uint8)

    #morfolojik filtreler

    erode = cv2.erode(mask,kernel,iterations = 1 )

    #erode1 = cv2.morphologyEx(mask,cv2.MORPH_ERODE,kernel)

    dilate = cv2.dilate(mask,kernel,iterations=1 )

    #dilate1 = cv2.morphologyEx(mask,cv2.MORPH_DILATE,kernel)

    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    
    

    
    
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    cv2.imshow("closing",opening)





    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


kamera.release()
cv2.destroyAllWindows()












