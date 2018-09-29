from PIL import Image, ImageGrab
from datetime import *
import pyautogui


#i_image = Image.open("D:/Users/Martin/Pictures/Avatar/avatar_11220.jpg")
#i_image.show()

current_time = datetime.now()
current_time = datetime.strftime(current_time, '%Y-%m-%d_%H%M%S')

print(current_time)


first_coor = pyautogui.position()
secon_coor = pyautogui.position()
full_coord = first_coor + secon_coor

screenshot = ImageGrab.grab(full_coord)
vfilename = "Screenshot" + '_' + current_time + ".png"
print(vfilename)
screenshot.save(vfilename, format='PNG')
