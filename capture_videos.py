import cv2
import numpy as np

cap1 = cv2.VideoCapture(0)


# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))

while(True):
    # get a frame
    ret, frame = cap1.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    filter = cv2.Canny(gray, 100, 200)

    # save a frame
    #out.write(frame)

    # show a frame
    cv2.imshow("Color", frame)
    #cv2.imshow("Gray", gray)
    cv2.imshow("Canny", filter)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap1.release()
#out.release()
cv2.destroyAllWindows()