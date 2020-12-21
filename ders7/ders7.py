import cv2
import numpy as np



def main():
    android = np.zeros((400,400,3),dtype = "uint8")

    cv2.rectangle(android, (0, 0), (200, 200), [150, 0, 255], 3)
    cv2.rectangle(android, (200, 0), (400, 200), [0, 0, 255], 3)
    cv2.rectangle(android, (0, 200), (200, 400), [0, 255, 255], 3)
    cv2.rectangle(android, (200, 200), (400, 400), [255, 0, 255], 3)

    cv2.rectangle(android, (100, 100),(300, 300), [0, 150, 255], 3)

    #iki_kat_kucuk = cv2.pyrDown(android)

    #iki_kat_buyu = cv2.pyrUp(android)

    print(android)


    cv2.imshow("resim",android)


    cv2.waitKey(0)
    cv2.destroyAllWindows()





1


if __name__  == "__main__":
    main()