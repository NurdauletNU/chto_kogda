import cv2 as cv
import sys



def reading_showing_img():
    img=cv.imread(cv.samples.findFile("src.jpg"))
    print(type(img), img)
    if img is None:
        sys.exit("not found")
    cv.imshow("Display window", img)
    cv.imshow("Display window cropped", img[0:600, 0:500])  #  y1:y2, x1:x2
    k=cv.waitKey(0)


reading_showing_img()