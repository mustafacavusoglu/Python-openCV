import cv2
import numpy as np



def main():
    kamera = cv2.VideoCapture(0)

    #fourcc = cv2.VideoWriter_fourcc(*"XVID") #formatlama
    fourcc = cv2.VideoWriter_fourcc(*"XVID")

    #kayit = cv2.VideoWriter("kayit.mp4", fourcc, 30, (640, 480))
    kayit = cv2.VideoWriter("kayit.mp4",fourcc,30,(640,480))

    while True:
        ret,goruntu = kamera.read()

        #ters = cv2.flip(goruntu,0)
        ters = cv2.flip(goruntu,0)

        if ret == True:

            kayit.write(ters)

        cv2.imshow("kare",ters)





        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    kamera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()