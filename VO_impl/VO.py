import cv2
import numpy as np

from extractor import Extractor

cap = cv2.VideoCapture('../DrivingVideo.mp4')
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
# cap.set(cv2.CAP_PROP_BUFFERSIZE,10)
W, H = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
imgScalingFactor = 2
print("Number of frames in video: ", cap.get(cv2.CAP_PROP_FRAME_COUNT),"\n","Frame size: ", W, H)

ext = Extractor()

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (W//4, H//4))
    if ret:
        kps = ext.detectFeatures(frame)
        ext.matchFeatures(frame, kps)
        frame = cv2.drawKeypoints(frame, kps, None, color=(0,0,255), flags=0)
    else:
        print("End of video reached. Exiting.")
        break
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
