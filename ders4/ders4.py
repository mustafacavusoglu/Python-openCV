import cv2
import numpy as np



resim = cv2.imread("kedili ben.jpg")
yuz = resim[175:520,375:600]

sag_goz = cv2.rectangle(yuz,(77,155),(122,184),(50,10,10),2)
sol_goz = cv2.rectangle(yuz,(160,195),(190,225),[50,10,10],2)

cv2.circle(yuz,(132,232),25,[255,0,0],9)

print("resim özellikleri : {} \nresim boyutu : {}\nresimn bit değeri : {}".format(resim.shape,resim.size,resim.dtype))

#resmi uzatma

uzatılan_resim = cv2.copyMakeBorder(yuz,100,100,100,100,cv2.BORDER_REPLICATE)



#resmi aynalama

aynalanan_resim = cv2.copyMakeBorder(yuz,100,100,100,100,cv2.BORDER_REFLECT)

#resmi tekrar etme

tekraredilen_resim = cv2.copyMakeBorder(yuz,100,100,100,100,cv2.BORDER_WRAP)


#resmin etrafını sarma

sarmalanan_resim = cv2.copyMakeBorder(yuz,100,100,100,100,cv2.BORDER_CONSTANT,value  = [50,10,10])

#cv2.imshow("kedili ben",yuz)
#cv2.imshow("resim",resim)
cv2.imshow("uzatılan",uzatılan_resim)
cv2.imshow("aynalanan",aynalanan_resim)
cv2.imshow("tekrar edilen",tekraredilen_resim)
cv2.imshow("sarmalanan",sarmalanan_resim)



cv2.waitKey(0)
cv2.destroyAllWindows()