import cv2
import numpy as np 

img = cv2.imread("st2.jpg",cv2.IMREAD_GRAYSCALE)
#img1 = cv2.imread("f1.jpg",cv2.IMREAD_GRAYSCALE)
resized_image = cv2.resize(img, (50, 50))
#resized_image1 = cv2.resize(img1, (50, 50))
cv2.imwrite("f2.jpg",resized_image)
#cv2.imwrite("pesh1.png",resized_image1)

#cap = cv2.VideoCapture(0)

#while cv2.waitKey(1):
    #ret, frame = cap.read()
    #cv2.imshow('frame',frame)

#cap.release()
cv2.destroyAllWindows()