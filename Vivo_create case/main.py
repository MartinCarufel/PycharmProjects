import pyautogui
from pyautogui import *
from time import sleep
import win32gui


class Auto_vivo:

    def __init__(self):
        self.tooth_base_cood = (580, 300)
        self.tooth_xspacing = 75
        self.tooth_yspacing = 92
        self.tooth_number_yspacing = 239
        self.tooth_number_cood = (580, 221)
        self.win_workspace = {
                        'new case': (175, 40),
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
                        'next': (1836, 1040),
                        'add patient': (200,595),
                        'create patient': (310,650)}
        self.win_scan_cood = {
                        'start': (1717,123),
                        'reset': (1846,123),
                        'shine control': (1650, 200),
                        'monochrome': (1650, 230),
                        'next': (1840, 1040)
                        }

    def create_case_scan_mesh(self, test_list):
        for patient, tooth in test_list:

            click(self.win_workspace['new case'][0], self.win_workspace['new case'][1])
            sleep(2)
            click(self.win_plan_editor_cood['add patient'][0],self.win_plan_editor_cood['add patient'][1])
            typewrite(patient)
            click(self.win_plan_editor_cood['create patient'][0], self.win_plan_editor_cood['create patient'][1])
            click(self.win_plan_editor_cood[tooth][0], self.win_plan_editor_cood[tooth][1])
            moveRel(75,-25)  # select prosthesis
            click()
            moveRel(61,54)   # select crown
            click(1800, 0)   # click empty place
            click(self.win_plan_editor_cood['next'][0], self.win_plan_editor_cood['next'][1])


print(win32gui.EnumWindows())
test = Auto_vivo()
test_list1 = [('mart1', 'upper18')]
test.create_case_scan_mesh(test_list1)






