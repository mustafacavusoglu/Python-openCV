import cv2
import numpy as np



def main():
    x = cv2.imread("x.jpg")
    y = cv2.imread("y.jpg")

    print(x[300,500])
    print(y[300,500])

    print(x[300,500]+y[300,500])
    toplam = cv2.add(x,y)

    cv2.imshow("toplam",toplam)

    agirlikli_toplam = cv2.addWeighted(x,0.3,y,0.7,0)
    cv2.imshow("ağırlıklı toplam",agirlikli_toplam)


    print("X FOTO\nyükseklik : {}\ngenişlik : {}\nkanal sayısı : {}\n ".format(x.shape[0],x.shape[1],x.shape[2]))
    print("Y FOTO\nyükseklik : {}\ngenişlik : {}\nkanal sayısı : {}\n ".format(y.shape[0], y.shape[1], y.shape[2]))



    cv2.imshow("x.jpg",x)
    cv2.imshow("y.jpg",y)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ ==  "__main__":
    main()

