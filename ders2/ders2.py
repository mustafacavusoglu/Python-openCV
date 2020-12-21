import cv2
import numpy as np

resim = cv2.imread("ati.JPG")

cv2.imshow("resim",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

