import cv2
video_0=cv2.VideoCapture(0)
while (True):
    retu, frame0=video_0.read()
    cv2.imshow('frame', frame0)
    if cv2.waitKey(1) & 0xFF==ord('a'):
        break
video_0.release()
cv2.destroyAllWindows()
