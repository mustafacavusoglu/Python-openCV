import cv2
import numpy as np        



def main():
    resim = cv2.imread("satranc.JPG")

    resim_gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

    resim_gri = np.float32(resim_gri)

    koseler = cv2.goodFeaturesToTrack(resim_gri,80,0.001,10)

    koseler = np.int0(koseler)

    for kose in koseler:
        x,y = kose.ravel()
        cv2.circle(resim,(x,y),3,(0,255,255),-1)

    cv2.imshow("resim",resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
