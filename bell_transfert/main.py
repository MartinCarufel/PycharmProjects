import pyautogui as pg
from time import sleep

nb= 3

for i in range(nb):
    pg.click(618, 204, interval=3)
    pg.click(58, 204, interval=0.2)
    pg.typewrite("anne.marie.ouellette18")
    pg.press('@')
    pg.typewrite("gmail.com")
    sleep(1)
    pg.click(91, 800, interval=8)
    pg.click(661, 204, interval=4)