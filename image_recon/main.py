from python_imagesearch.imagesearch import imagesearch, click_image
import pyautogui
import cv2
from screeninfo import get_monitors

pyautogui.moveTo(100, 100)
# pyautogui.click(clicks=1, interval=0.0, button=pyautogui.PRIMARY)

for m in get_monitors():
    print(str(m))

# x,y = pyautogui.position()
# print(x,y)
#
# pos = imagesearch("4.png")
# img = cv2.imread("4.png")
# print(img.shape[0]/2, img.shape[1]/2)
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#
#     pyautogui.moveTo(pos[0]+img.shape[0]/2, pos[1]+img.shape[1]/2)
#     pyautogui.click(clicks=2, interval=0.0, button=pyautogui.PRIMARY)
#     # click_image("3.png", pos, action="right", timestamp=0.1)
# else:
#     print("image not found")
