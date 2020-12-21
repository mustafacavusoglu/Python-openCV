import  cv2
import  numpy as np




#-->0 = bilgisayar kamerası
#-->1 = usb ile takılmış kamera
#-->video ismi = bilgisayarda ki video


kamera = cv2.VideoCapture(0)

while True:
    ret,kare = kamera.read()


    cv2.rectangle(kare,(160,120),(480,360),[0,0,255],4)

    bolge = kare[120:360,160:480]
    print(kare.shape)

    cv2.imshow("video",kare)
    cv2.imshow("bolge",bolge)



    if cv2.waitKey(1)  & 0xFF == ord("q"):
        break



kamera.release()
cv2.destroyAllWindows()
