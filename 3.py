import numpy as np
import cv2

def Detect(classifier, img, scaleFactor, minNeighbors, font, text):
    c = cv2.CascadeClassifier(classifier)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = c.detectMultiScale(gray, scaleFactor, minNeighbors)
    for (x,y,w,h) in objects:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.putText(img,text,(x-10,y-10), font, 0.5, (10,255,255), 2, cv2.LINE_AA)
    return 


font = cv2.FONT_HERSHEY_SIMPLEX

sign = ["stop","pesh","zapr"]
mode = ["haar15","haar10","lbp"]
test = ["problems","ok"]
s = 2
m = 0
t = 1

if sign[s] == "stop":

    if test[t] == "problems":
        img1 = cv2.imread("test images/st1.jpg")
        img2 = cv2.imread("test images/st3.jpg")
        img3 = cv2.imread("test images/st6.jpg")

    if test[t] == "ok":
        img1 = cv2.imread("test images/st9.jpg")
        img2 = cv2.imread("test images/st11.jpg")
        img3 = cv2.imread("test images/st6.jpg")
        #img1 = cv2.imread("test images/st7.jpg")
        #img2 = cv2.imread("test images/st8.jpg")
        #img3 = cv2.imread("test images/st5.jpg")

    if mode[m] == "haar10":
        Detect('cascade_stop_3_10.xml',img1,1.3,6,font,'Stop')
        Detect('cascade_stop_3_10.xml',img2,1.3,6,font,'Stop')
        Detect('cascade_stop_3_10.xml',img3,1.3,6,font,'Stop')

    elif mode[m] == "haar15":
        Detect('cascade_stop_3_15.xml',img1,1.3,6,font,'Stop')
        Detect('cascade_stop_3_15.xml',img2,1.3,6,font,'Stop')
        Detect('cascade_stop_3_15.xml',img3,1.3,6,font,'Stop')

    elif mode[m] == "lbp":
        Detect('cascade_stop_lbp20.xml',img1,1.1,6,font,'Stop')
        Detect('cascade_stop_lbp20.xml',img2,1.1,6,font,'Stop')
        Detect('cascade_stop_lbp20.xml',img3,1.1,6,font,'Stop')

elif sign[s] == "pesh":

    if test[t] == "problems":
        img1 = cv2.imread("test images/p2.jpg")
        img2 = cv2.imread("test images/p3.jpg")
        img3 = cv2.imread("test images/p4.jpg")

    if test[t] == "ok":
        img1 = cv2.imread("test images/p1.jpg")
        img2 = cv2.imread("test images/p3.jpg")
        img3 = cv2.imread("test images/p4.jpg")
        #img3 = cv2.imread("test images/p5.jpg")

    Detect('cascade_pesh_lbp14.xml',img1,1.1,6,font,'Walkway')
    Detect('cascade_pesh_lbp14.xml',img2,1.1,6,font,'Walkway')
    Detect('cascade_pesh_lbp14.xml',img3,1.1,6,font,'Walkway')

elif sign[s] == "zapr": 

    if test[t] == "problems":
        img1 = cv2.imread("test images/z7.jpg")
        img2 = cv2.imread("test images/z8.jpg")
        img3 = cv2.imread("test images/z9.jpg")
    elif test[t] == "ok":
        img1 = cv2.imread("test images/z2.jpg")
        img2 = cv2.imread("test images/z3.jpg")
        img3 = cv2.imread("test images/z4.jpg")

    Detect('cascade_zapr_lbp13.xml',img1,1.1,6,font,'No entry')
    Detect('cascade_zapr_lbp13.xml',img2,1.1,6,font,'No entry')
    Detect('cascade_zapr_lbp13.xml',img3,1.1,6,font,'No entry')

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)

cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    
    Detect('cascade_stop_3_15.xml',img,1.1,6,font,'Stop')
    Detect('cascade_pesh_lbp14.xml',img,1.1,6,font,'Walkway')
    Detect('cascade_zapr_lbp13.xml',img,1.1,6,font,'No entry')
    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()