import numpy as np
import glob
import cv2


template = cv2.imread("icons-maps-google.png")
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template = cv2.Canny(template, 80, 190, apertureSize=3)
(tH, tW) = template.shape[:2]
cv2.imshow("Template", template)
cv2.waitKey(0)