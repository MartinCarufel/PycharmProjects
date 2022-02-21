import cv2
import numpy as np

# Read the image using imread function
image = cv2.imread('test1.jpg')
cv2.imshow('Original Image', image)

# let's downscale the image using new  width and height
down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)

new_img = cv2.resize(src=image, dsize=[200, 200], interpolation=cv2.INTER_LINEAR)
cv2.imshow("new" ,new_img)
cv2.waitKey()
new_img = cv2.resize(src=image, dsize=None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow("new" ,new_img)
# let's upscale the image using new  width and height
up_width = 600
up_height = 400
up_points = (up_width, up_height)
# resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)

# Display images
# cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.waitKey()
# cv2.imshow('Resized Up image by defining height and width', resized_up)
# cv2.waitKey()

#press any key to close the windows
cv2.destroyAllWindows()










""" Read, display and write image
im = cv2.imread("test1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Picture", im)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imwrite("test_gray.jpg", im)
"""