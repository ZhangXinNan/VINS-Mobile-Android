

import numpy as np
import cv2

video_file = "C:\\Users\\zhang\\Desktop\\video.avi"
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(video_file)
i = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if frame is None:
        break
    i+=1
    print(i)
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.putText(frame, str())
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()