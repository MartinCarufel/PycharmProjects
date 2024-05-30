import unittest
import scan_data
import regex
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import pyautogui
from time import sleep
import numpy as np
import threading


class data_test(unittest.TestCase):
    def setUp(self):
        self.data_class = scan_data.Data_analyser()
        pass

    def tearDown(self):
        pass

    def test_import_csv(self):
        expected_data_shape = (10,7)
        scan_title_regex = "(.*LOWER_ARCH\.stl)|(.*UPPER_ARCH\.stl)"
        scan_title_regex_compiled = regex.compile(scan_title_regex)
        # data = scan_data.Data_analyser()
        df = self.data_class.read_csv("./Test_data/batchMetrologySummary.csv")
        self.assertTupleEqual(expected_data_shape, df.shape, msg="Error, Wrong data format")
        print("\n", df.iloc[0][0])
        print('\n\nRegex Result', scan_title_regex_compiled.match(df.iloc[0][0]))
        self.assertIsNotNone(scan_title_regex_compiled.match(df.iloc[0][0]), msg="Error, Unexpected data in fisrt line first col")

    def test_col_RMS(self):
        df = self.data_class.read_csv("./Test_data/batchMetrologySummary.csv")
        # print(df["RMS"])
        for dt in df["RMS"]:
            print(dt)

    def test_range(self):
        range_band = [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.060, 0.065,
                           0.070, 0.075, 0.080]
        self.range_band_count = []
        df = self.data_class.read_csv("./Test_data/batchMetrologySummary.csv")
        data_table = []
        data_expected_table = [0, 0, 0, 2, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(range_band)-1):
            data_table.append(self.data_class.value_within_range_count(range_band[i], range_band[i+1], df['RMS']))
            pass


    def test_range_index_creator(self):
        range_band = [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.060, 0.065,
                      0.070, 0.075, 0.080]

        expected_result = ['1 - 5', '6 - 10', '11 - 15', '16 - 20', '21 - 25', '26 - 30', '31 - 35', '36 - 40',
                           '40 - 45', '46 - 50', '51 - 55', '55 - 60', '61 - 65', '66 - 70', '71 - 75', '76 - 80']
        index = self.data_class.create_range_index(range_band)
        print(index)
        self.assertListEqual(index, expected_result)

    def test_plot_data(self):
        data = {
            'range': ['1 - 5', '6 - 10', '11 - 15', '16 - 20', '21 - 25', '26 - 30', '31 - 35', '36 - 40',
                           '40 - 45', '46 - 50', '51 - 55', '55 - 60', '61 - 65', '66 - 70', '71 - 75', '76 - 80'],
            'Martin scan': [0, 0, 0, 2, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }
        df = pd.DataFrame(data)

        self.data_class.plot_bar_graph(df)

    def test_file_dialog(self):
        path = self.data_class.select_file()
        print(path)

    def test_entry_window(self):
        self.data_class.choose_data_name()
        print(self.data_class.entry_box_text)

    def take_screenshot(self, wait_time):
        sleep(wait_time)
        screenshot = pyautogui.screenshot()
        return screenshot
    def test_continue_window(self):
        img_exp = cv2.imread("./Test_data/Expected Screenshot/2024-05-30 14_55_07-More data _.png")
        # th = threading.Thread(target=self.take_screenshot, args=[2])
        # th.run()
        self.data_class.ask_continue()
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)  # Convert to a NumPy array
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        result = cv2.matchTemplate(image=screenshot, templ=img_exp, method=cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # cv2.imshow('Detected', screenshot)
        # cv2.waitKey(0)
        # print(min_loc, max_loc)
        h, w, _ = img_exp.shape
        top_left = max_loc
        pyautogui.click(x=top_left[0] + w -5, y=top_left[1] -5)
        self.assertGreaterEqual(max_val, 0.70)
        print(max_val)
