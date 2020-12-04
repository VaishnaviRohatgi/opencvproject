import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output2.avi', fourcc, 20 , (640, 480))
print(cap.isOpened())
while (cap.isOpened()):
    check, frame = cap.read()
    if check==True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        k = cv2.waitKey(1)

        if k & 0xFF == ord('q'):
            break
    else:
            break
cap.release()
out.release()
cv2.destroyAllWindows()