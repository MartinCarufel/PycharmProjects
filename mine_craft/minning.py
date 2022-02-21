import win32api, win32con
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

def l_click(x,y, hold=0):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    sleep(hold)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def r_click(x,y, hold=0):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    sleep(hold)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)




l_click(950, 350)
sleep(0.2)

for i in range(10):
    l_click(960, 531, 2)
    keyboard.press("w")
    sleep(0.2)
    keyboard.release("w")
#     pass
    # pressHoldRelease(0x57)  # key W
    # l_click(960,531,5)