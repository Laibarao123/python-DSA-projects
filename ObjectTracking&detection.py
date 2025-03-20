#OBJECT TRCAKING AND DETECTION:



# x,y=489,34
# w=802-489
# h=919-34
import cv2
import numpy as np
cap=cv2.VideoCapture(r"C:\Users\dell\Desktop\CV PY files\vid1.mp4")
r,f=cap.read()
x,y,w,h=150,34,313,885        #roi
t=(x,y,w,h)
roi=f[y:y+h,x:x+w]
hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv_roi,np.array((0.0,60.0,32.0)),np.array((180.,255.,255.)))
roi_hst=cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hst,roi_hst,0,255,cv2.NORM_MINMAX)
tr=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

cv2.imshow("test",roi)
while cap.isOpened():
    r,f=cap.read()
    if r==True:
        hsv_f=cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
        d=cv2.calcBackProject([hsv_f],[0],roi_hst,[0,180],1)
        r,tp=cv2.CamShift(d,t,tr)
        x,y,w,h=tp
        final=cv2.rectangle(f,(x,y),(x+w,y+h),(0,0,255),4)
        cv2.imshow("wscube", final)
        # cv2.imshow("wscube",frame)
        if cv2.waitKey(25) & 0xff == ord("p"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()



