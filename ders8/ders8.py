import  cv2

import numpy as np


def main():
    resim = np.zeros((600,600,3),dtype = "uint8")
    resim.fill(182)



    cv2.line(resim, (400, 200), (200, 400), [183, 12, 150], 5)
    cv2.line(resim, (200, 200), (400, 400), [183, 12, 150], 5)
    cv2.line(resim, (200, 300), (400, 300), [183, 12, 150], 5)




    cv2.putText(resim, "mustafa", (230,190), cv2.FONT_HERSHEY_PLAIN, 2, [0, 0, 255], 1)


    cv2.circle(resim, (300, 300), 100, [183, 12, 150], 5)

    cv2.rectangle(resim,(200,200),(400,400),[183,12,150],5)

    cv2.imshow("resim", resim)



    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()