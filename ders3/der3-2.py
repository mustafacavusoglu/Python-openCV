import cv2
import numpy as np



resim = cv2.imread("ders3.jpg")


resim[200:400,400:600,0:2]= 255
b,g,r = cv2.split(resim)


print(b[100,100]) #blue
print(g[100,100]) #green
print(r[100,100]) #red
print(resim[100,100])


print("resmin boyutu : ",resim.size)
print("resmin özelliği : ",resim.shape)
print("resmin bit ddeğeri : ",resim.dtype)

print(resim[50,50])






bolge = resim[300:400,128:528]

#resim[0:100,0:400] = bolge
#resim[100:200,0:400] = bolge
#resim[0:100,320:720] = bolge


#cv2.imshow("kesilen bölge ",bolge)

cv2.imshow("kaplan",bolge)
#cv2.imshow("kaplan Blue",b)
#cv2.imshow("kaplan Green",g)
#cv2.imshow("kaplan Red",r)

cv2.waitKey(0)
cv2.destroyAllWindows()
