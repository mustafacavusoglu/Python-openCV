import cv2
import numpy as np
import os
import sys



resimm = "C:/Users/mustdo/Desktop/dosyalar/iPhone/BDJP7305.JPG"
yol = "C:/Users/mustdo/Desktop/"

a = cv2.imread(resimm,0)
#resim = cv2.imread("gri.JPG")

#gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

cv2.imshow("resim",a)


#cv2.imwrite(str(yol) + "gri12.JPG",a)


cv2.waitKey(0)

cv2.destroyAllWindows()

