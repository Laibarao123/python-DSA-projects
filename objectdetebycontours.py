import cv2
import numpy as np
# countours covers object surrounding objects
# in this we are doing live object detection by using contours
def nothing(x):
    pass
cv2.namedWindow("wscube")
cv2.createTrackbar("th","wscube",0,255,nothing)

cv2.createTrackbar("lb","wscube",0,255,nothing)
cv2.createTrackbar("lg","wscube",0,255,nothing)
cv2.createTrackbar("lr","wscube",0,255,nothing)

cv2.createTrackbar("ub","wscube",255,255,nothing)
cv2.createTrackbar("ug","wscube",255,255,nothing)
cv2.createTrackbar("ur","wscube",255,255,nothing)


cap=cv2.VideoCapture(0)
while cap.isOpened():
    r,frame=cap.read()
    if r==True:
        th=cv2.getTrackbarPos('th',"wscube")

        LB = cv2.getTrackbarPos('lb', "wscube")
        LG = cv2.getTrackbarPos('lg', "wscube")
        LR = cv2.getTrackbarPos('lr', "wscube")

        UB= cv2.getTrackbarPos('ub', "wscube")
        UG= cv2.getTrackbarPos('ug', "wscube")
        UR= cv2.getTrackbarPos('ur', "wscube")

        lower=np.array([LB,LG,LR])
        upper=np.array([UB,UG,UR])
        frame=cv2.flip(frame,1)
        frame=cv2.resize(frame,(250,250))
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        m=cv2.inRange(hsv,lower,upper)
        res=cv2.bitwise_and(frame,frame,mask=m)
        fr=cv2.bitwise_not(res)
        _,thi=cv2.threshold(m,th,255,cv2.THRESH_BINARY)
        cnt,hr=cv2.findContours(thi,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame,cnt,-1,(255,0,0),2)
        cv2.imshow("thr",thi)
        cv2.imshow("res", res)
        cv2.imshow("mask",m)
        cv2.imshow("ws",frame)
        if cv2.waitKey(25) & 0xff == ord("p"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()



