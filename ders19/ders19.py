import cv2
import numpy as np
import sqlite3

kamera = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*"XVID")

#kayit = cv2.VideoWriter("kayit.mp4",fourcc,30,(640,480))

while True:

    ret,kare = kamera.read()

    yuz_c = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    goz_c = cv2.CascadeClassifier("haarcascade_eye.xml")
    smile = cv2.CascadeClassifier("haarcascade_smile.xml")


    #aslii = cv2.imread("klblk.jpg")


    #asli = cv2.resize(aslii,(640,480), interpolation =cv2.INTER_AREA)


    kare_gri = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    yuzler = yuz_c.detectMultiScale(kare_gri, 1.2, 4)


    for x, y, w, h in yuzler:
        cv2.rectangle(kare, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(kare, "yuz", (x, y-8), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

        yuz_b = kare[y:y + h, x:x + w]

        gri_yuz_b = cv2.cvtColor(yuz_b,cv2.COLOR_BGR2GRAY)

        gozler = goz_c.detectMultiScale(gri_yuz_b, 1.2, 4)

        smiles = smile.detectMultiScale(gri_yuz_b,1.2,4)

        #for q, w, e, r in smiles:
            #cv2.rectangle(yuz_b, (q, w), (q+e, w+r), (63, 63, 63), 2)
            #cv2.putText(kare, "gulucuk", (x+q,y+ w-5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

           


        for a, b, c, d in gozler:
            cv2.rectangle(yuz_b, (a, b), (a+c, b+d), (0, 0, 255), 2)
            cv2.putText(kare, "goz", (x+a,y+ b-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)


    cv2.imshow("resim",kare)



    if cv2.waitKey(1) & 0xFF == ord("h"):
        break

kamera.release()
cv2.destroyAllWindows()
