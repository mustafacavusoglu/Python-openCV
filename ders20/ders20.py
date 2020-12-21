import cv2
import numpy as np 



video = cv2.VideoCapture("22.mp4")
insan_bulucu = cv2.CascadeClassifier("haarcascade_fullbody.xml")
while True:
    ret,kare = video.read()

    gri_kare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    bedenler = insan_bulucu.detectMultiScale(gri_kare,1.1,4)

    for x,y,w,h in bedenler:
        cv2.rectangle(kare,(x,y),(x+w,y+h),(0,0,255),2)


    cv2.imshow("kare",kare)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break


video.release()
cv2.destroyAllWindows()

