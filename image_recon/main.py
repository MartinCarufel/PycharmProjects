from python_imagesearch.imagesearch import imagesearch, click_image
import pyautogui
import cv2

pos = imagesearch("2.png")
img = cv2.imread("2.png")
if pos[0] != -1:
    print("position : ", pos[0], pos[1])

    pyautogui.moveTo(pos[0]+img.shape[0]/2, pos[1]+img.shape[1]/2)
    # pyautogui.click(clicks=2, interval=0.0, button=pyautogui.PRIMARY)
    # click_image("2.png", pos, action="right", timestamp=0.1)
else:
    print("image not found")