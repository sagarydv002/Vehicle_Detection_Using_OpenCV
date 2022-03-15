from re import A
import cv2
import imutils
import numpy as np
from matplotlib.pyplot import gray
cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    detected = 0
    _,img=cam.read()
    img=imutils.resize(img,width=300)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars= car_cascade.detectMultiScale(gray,1.1,1)
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow(" Video Frame", img)
        b= str(len(cars))
        a=int(b)
        detected=a
        n=detected
        print ("--------------------------")
        print ("Found: %d "%(n))
        if n>=2:
            print ("Found Cars")
        else:
            print ("no cars")
            if cv2.waitKey(33) == 27:
                break
cam.release()
cv2.destroyAllWindows()