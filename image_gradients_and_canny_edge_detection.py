import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    _, frame = camera.read()
    cv2.imshow("Camera", frame)
    lap = cv2.Laplacian(frame, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))
    cv2.imshow("Laplacian", lap)

    edges = cv2.Canny(frame,0,0 )
    cv2.imshow("canny", edges)

    if cv2.waitKey(5) == ord('x'):
        break
camera.release()
cv2.destroyAllWindows()
