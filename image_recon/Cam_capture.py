import cv2


vid = cv2.VideoCapture(0)

ret, frame = vid.read()
cv2.imshow("cam", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()