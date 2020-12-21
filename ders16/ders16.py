import cv2
import numpy as np




def main():
    resim = cv2.imread("ezgi.jpg")

    mask = np.zeros(resim.shape[:2],np.uint8)


    gbdModel = np.zeros((1,65),dtype = np.float64)
    fgdModel = np.zeros((1,65),dtype = np.float64)

    rect = (60,30,360,400)

   
    cv2.grabCut(resim,mask,rect,gbdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    

    mask2 = np.where((mask == 0 )| (mask == 2),0,1 ).astype(np.uint8)

    for x in  range(mask2.shape[0]):
        for y in range(mask2.shape[1]):
            print("satır: {} sütun:{} değer: {}".format(x,y,mask2[x,y]))


    resim = resim*mask2[:,:,np.newaxis]






    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
