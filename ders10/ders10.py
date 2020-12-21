import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

def ayarlama(kare,yuzde ):

    genislik = int(kare.shape[1] * yuzde / 100)
    yukseklik = int(kare.shape[0] * yuzde / 100)
    boyut = (genislik,yukseklik)

    return cv2.resize(kare,boyut, interpolation =cv2.INTER_AREA)


def main():
    while True:

        ret,kare = kamera.read()

        kare2 = ayarlama(kare,25)

        gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)


        cv2.imshow("kare",kare)
        cv2.imshow("kare2",kare2)
        cv2.imshow("gri",gri)

        





        if cv2.waitKey(1)  & 0xFF == ord("q"):
             break

    kamera.release()
    cv2.destroyAllWindows()




if __name__ == "__main__":
    main()