import unittest
import scan_data
import regex
import pandas as pd
import cv2
import pyautogui
from time import sleep
import numpy as np
import threading
import matplotlib.pyplot as plt

class data_test(unittest.TestCase):

    # def __init__(self, *args):
    #     super().__init__()
    #     self.screenshot = None
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
                           '41 - 45', '46 - 50', '51 - 55', '56 - 60', '61 - 65', '66 - 70', '71 - 75', '76 - 80']
        index = self.data_class.create_range_index(range_band)
        print(index)
        self.assertListEqual(index, expected_result)

    def test_plot_data(self):
        data = {
            'range': ['1 - 5', '6 - 10', '11 - 15', '16 - 20', '21 - 25', '26 - 30', '31 - 35', '36 - 40',
                           '41 - 45', '46 - 50', '51 - 55', '55 - 60', '61 - 65', '66 - 70', '71 - 75', '76 - 80'],
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

    def take_screenshot(self, wait_time, img_exp):
        sleep(wait_time)
        self.screenshot = pyautogui.screenshot()
        self.screenshot = np.array(self.screenshot)  # Convert to a NumPy array
        self.screenshot = cv2.cvtColor(self.screenshot, cv2.COLOR_RGB2BGR)
        self.screenshot = self.screenshot.astype(np.uint8)
        self.result = cv2.matchTemplate(image=self.screenshot, templ=img_exp, method=cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(self.result)
        h, w, _ = img_exp.shape
        top_left = max_loc
        pyautogui.click(x=top_left[0] + w - 10, y=top_left[1] + 10)


    def close_window(self):
        pass


    def test_continue_window(self):
        img_exp = cv2.imread("./Test_data/Expected Screenshot/More data.png")
        img_exp = img_exp.astype(np.uint8)
        th = threading.Thread(target=self.take_screenshot, args=[0.5, img_exp])
        th.start()
        self.data_class.ask_continue()
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(self.result)
        self.assertGreaterEqual(max_val, 0.70)
        print(max_val)
        th.join()

    def test_screen(self):

        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)  # Convert to a NumPy array
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # Convert from RGB to BGR
        screenshot = screenshot.astype(np.uint8)
        target_image_path = "./Test_data/image1.png"
        target_image = cv2.imread(target_image_path)
        if target_image is None:
            raise FileNotFoundError(f"Target image not found at path: {target_image_path}")
        target_image = target_image.astype(np.uint8)

        # Perform template matching
        result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)

        # Get the best match position
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Get the dimensions of the target image
        h, w, _ = target_image.shape

        # Draw a rectangle around the matched region
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)

        # Show the result (optional)
        cv2.imshow('Detected', screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save the result image (optional)
        cv2.imwrite('result.png', screenshot)

    def test_split_blocks(self):
        blocks = self.data_class.split_cvs_blocks("./Test_data/batchMetrologySummary_block.csv")
        print(blocks[-3:-2])


    def test_read_block(self):
        block = self.data_class.split_cvs_blocks("./Test_data/batchMetrologySummary_block.csv")
        print(block)
        df = self.data_class.read_cvs_block("./Test_data/batchMetrologySummary_block.csv", block[-3:-2][0])
        print(df)

    def test_bar_graph(self):
        df = pd.read_csv("./Test_data/Test_result_3_user.csv", index_col=0)
        fig, ax = plt.subplots(layout='constrained', figsize=(10,5))

        width = 0.8 / (len(df.columns)-1)  # the width of the bars
        multiplier = 0
        # lbl = ["tata", "toto", "tutu"]
        lbl = np.asarray(df["range"])
        # print(lbl)
        x = np.arange(len(lbl))  # the label locations
        for (user, user_data) in df.items():
            # print(user, user_data)

            offset = width * multiplier
            if user != "range":
                # print(list(user_data))
                print(x)
                rects = ax.bar(x + offset, np.asarray(user_data), width, label=user, align='center')
                # ax.bar_label(rects, padding=3)
                multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('%')
        # ax.set_title('Penguin attributes by species')
        ax.set_xticks(x + width, lbl)
        ax.tick_params(axis='x', labelrotation=90)
        #labelrotationfloat
        # ax.legend(loc='upper left', ncols=3)
        leg = ['tata', 'toto', 'tutu']
        ax.legend()
        ax.set_ylim(0, 100)


        plt.show()



