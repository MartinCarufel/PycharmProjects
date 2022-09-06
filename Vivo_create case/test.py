import pyautogui as pg


class Test_suite:

    def __init__(self):
        self.win_main = {
            'win logo': 'win_logo.png',
            'new case': 'new case.png'

        }
        pass

    def test1(self):
        # location = pg.locateCenterOnScreen('win_logo.png', confidence=0.9)
        # print(location)
        # pg.moveTo(pg.locateCenterOnScreen('win_logo.png', confidence=0.9))
        pg.click(pg.locateCenterOnScreen(self.win_main['new case'], confidence=0.9))


t = Test_suite()
t.test1()
