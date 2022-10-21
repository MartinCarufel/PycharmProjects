import pyautogui as pg
from time import sleep



class Auto_vivo:

    def __init__(self):
        self.tooth_base_cood = (580, 300)
        self.tooth_xspacing = 75
        self.tooth_yspacing = 92
        self.tooth_number_yspacing = 239
        self.tooth_number_cood = (580, 221)
        self.delay_1 = 1
        self.delay_2 = 1.2
        self.delay_3 = 5
        self.conf_lvl_hi = 0.9
        self.win_workspace = {
                        'new case': 'new case.png',
                        }
        self.win_plan_editor_cood = {
                        'upper18': (580, 300),
                        'upper17': (655, 300),
                        'upper16': (730, 300),
                        'upper15': (805, 300),
                        'upper14': (880, 300),
                        'upper13': (955, 300),
                        'upper12': (1030, 300),
                        'upper11': (1105, 300),
                        'upper21': (1180, 300),
                        'upper22': (1255, 300),
                        'upper23': (1330, 300),
                        'upper24': (1405, 300),
                        'upper25': (1480, 300),
                        'upper26': (1555, 300),
                        'upper27': (1630, 300),
                        'upper28': (1705, 300),
                        'lower18': (580, 392),
                        'lower17': (655, 392),
                        'lower16': (730, 392),
                        'lower15': (805, 392),
                        'lower14': (880, 392),
                        'lower13': (955, 392),
                        'lower12': (1030, 392),
                        'lower11': (1105, 392),
                        'lower21': (1180, 392),
                        'lower22': (1255, 392),
                        'lower23': (1330, 392),
                        'lower24': (1405, 392),
                        'lower25': (1480, 392),
                        'lower26': (1555, 392),
                        'lower27': (1630, 392),
                        'lower28': (1705, 392),
                        'reset all': (1840, 595),
                        'save': (1703, 1040),
                        'next': 'next.png',    # (1836, 1040)
                        'add patient': 'add patient.png',      # (200, 595)
                        'create patient': 'create patient.png',      # (310, 650)
                        'crown': 'crown.png',
                        'prothesis': 'prothesis.png',
        }
        self.win_scan_cood = {
                        'start': 'start.png',    # (1717,123)
                        'pause': 'pause.png',
                        'reset': (1846,123),
                        'shine control': (1650, 200),
                        'monochrome': (1650, 230),
                        'next scan': 'next scan.png',    # (1836, 1040)
                        'abort scan': 'abort scan.png',
                        'cancel scan': 'cancel scan.png',
                        }
        self.win_side_bar = {
                        'S': (40, 40),
                        'plan editor': (40, 115),
                        'ribbon workspace': 'ribbon workspace.png'


                        }

    def create_case_scan_mesh(self, test_list):
        print("Test will start in 5 seconds, don't move the mouse")
        for i in range(5, 1, -1):
            print(i)
            sleep(1)

        for patient, tooth in test_list:
            pg.click(1000, 10, interval=self.delay_1)   # click to focus on Vivo
            pg.click(pg.locateCenterOnScreen(self.win_workspace['new case'], confidence=self.conf_lvl_hi), interval=self.delay_1)
            pg.click(pg.locateCenterOnScreen(self.win_plan_editor_cood['add patient'], confidence=self.conf_lvl_hi), interval=self.delay_1)
            pg.typewrite(patient)
            sleep(1)
            if pg.locateCenterOnScreen(self.win_plan_editor_cood['create patient'], confidence=self.conf_lvl_hi) != None:
                pg.click(pg.locateCenterOnScreen(self.win_plan_editor_cood['create patient'], confidence=self.conf_lvl_hi), interval=self.delay_1)
            else:
                pg.press('enter')
            pg.click(self.win_plan_editor_cood[tooth][0], self.win_plan_editor_cood[tooth][1], interval=self.delay_1)
            pg.click(pg.locateCenterOnScreen(self.win_plan_editor_cood['prothesis'], confidence=self.conf_lvl_hi), interval=self.delay_1)
            pg.click(pg.locateCenterOnScreen(self.win_plan_editor_cood['crown'], confidence=self.conf_lvl_hi), interval=self.delay_1)
            pg.click(1800, 750, interval=self.delay_1)   # click empty place
            pg.click(1800, 750, interval=self.delay_1)
            pg.click(pg.locateCenterOnScreen(self.win_plan_editor_cood['next'], confidence=self.conf_lvl_hi), interval=self.delay_2)
            pg.click(pg.locateCenterOnScreen(self.win_scan_cood['start'], confidence=self.conf_lvl_hi), interval=self.delay_1)
            sleep(6)    # scan model for 10 sec.
            pg.click(pg.locateCenterOnScreen(self.win_scan_cood['pause'], confidence=self.conf_lvl_hi), interval=self.delay_3)
            pg.click(pg.locateCenterOnScreen(self.win_scan_cood['next scan'], confidence=self.conf_lvl_hi), interval=0)
            sleep(15)
            pg.click(pg.locateCenterOnScreen(self.win_side_bar['ribbon workspace'], confidence=self.conf_lvl_hi), interval=self.delay_1)
            cancel_scan_list = [self.win_scan_cood['abort scan'], self.win_scan_cood['cancel scan']]
            for img in cancel_scan_list:
                if pg.locateOnScreen(img) != None:
                    pg.click(pg.locateCenterOnScreen(img))
                    break
            # pg.click(pg.locateCenterOnScreen(self.win_scan_cood['abort scan'], confidence=self.conf_lvl_hi), interval=self.delay_1)


    def test1(self):
        location = pg.locateCenterOnScreen('new case.png', confidence=self.conf_lvl_hi)


test = Auto_vivo()
# test_list1 = [('test1', 'upper18'), ('test1', 'upper17')]
test_list1 = [('test1', 'upper18'), ('test2', 'upper17'),
 ('test3', 'upper16'), ('test4', 'upper15'),
 ('test5', 'upper14'), ('test6', 'upper13'),
 ('test7', 'upper12'), ('test8', 'upper11'),
 ('test9', 'upper28'), ('test10', 'upper27'),
 ('test11', 'upper26'), ('tes12', 'upper25'),
 ('test13', 'upper24'), ('test14', 'upper23'),
 ('test15', 'upper22'), ('test16', 'upper21')]
for i in range(10):
    test.create_case_scan_mesh(test_list1)





