import cv2
import numpy as np

resim = cv2.imread("ders3.jpg",0)

print(resim.size)
print(resim.dtype)
print(resim.shape)
degerler = np.array(resim)
#print(degerler)
print(resim.item(250,250))
print(resim[250,250])



cv2.imshow("kaplan",resim)













cv2.waitKey(0)
cv2.destroyAllWindows()


