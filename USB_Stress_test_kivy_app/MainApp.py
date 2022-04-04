from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import re
import sys
import os
# sys.path.append('D:/user_data/Martin/OneDrive/Documents/git/PycharmProjects/USB_Stress_test_log_parser')
from usb_parser import *

from kivy.uix.button import Button

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Application(Widget):
    pass

class BoxLayoutEx(BoxLayout):
    text_box_content = StringProperty


    def get_text_box(self, text_):
        line_list = text_.split("\n")
        usb_err_summary = []
        for line in range(len(line_list)):
            line_list[line] = line_list[line].replace('\\', '/')
            reg_ex = 'IO-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]'  # Find in path/file the IO serial
            hp_serial = re.search(pattern=reg_ex, string=line_list[line]).group()
            print("Process the log for HP {}.".format(hp_serial))
            usb_err_summary.append(check_for_usb_error(line_list[line]))
            csv_data = extract_stress_test_data(line_list[line])
            df = convert_listcsv_to_dataframe(csv_data, hp_serial=hp_serial)
            summary = compile_test_data_per_minute(df, hp_serial)
            create_test_result_summary_csv(hp_serial, summary)
            check_for_usb_error_v2(line_list[line], hp_serial)

    pass

class TestMainApp(App):
    pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TestMainApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
