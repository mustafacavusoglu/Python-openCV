import cv2
import numpy as np


def main():

    android = cv2.imread("android.jpg")
    ezgi = cv2.imread("ezgi_senler.jpg")

    android_gri = cv2.cvtColor(android, cv2.COLOR_BGR2GRAY)
    


    yukseklik,genislik,kanal = android.shape

    ROI = ezgi[0:yukseklik,145:657]

    ret,mask = cv2.threshold(android_gri,80,255,cv2.THRESH_BINARY)

    #ret2,mask2 = cv2.threshold(android_gri,250,255,cv2.THRESH_BINARY)

    mask_inver = cv2.bitwise_not(android_gri)

    ezgi_arkaplan = cv2.bitwise_and(ROI,mask_inver,mask = mask_inver)


    toplam = cv2.add(android,ezgi_arkaplan)

    ezgi[0:yukseklik,145:657] = toplam

    cv2.imshow("ezgi",ezgi_arkaplan)
    cv2.imshow("a", android)
    cv2.imshow("android_gri",android_gri)
    cv2.imshow("mask",mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
