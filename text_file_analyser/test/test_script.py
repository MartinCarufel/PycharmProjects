import unittest
import text_file_analyser as tfa
import pandas as pd


class test_1(unittest.TestCase):

    def test_string_counter(self):
        data_file = tfa.Text_File_analyser("usb_stress_testIO-04-000979.log")
        string_count = data_file.string_counter("error code 995")
        self.assertEqual(13, string_count)

    def test_data_spliter(self):
        data_file = tfa.Text_File_analyser("usb_stress_testIO-04-000979.log")
        csv_data = data_file.data_spliter("\| +[0-9]+.[0-9][0-9]", "\| +")


    def test_data_spliter_2(self):
        data_file = tfa.Text_File_analyser("usb_stress_testIO-04-000979.log")
        csv_data = data_file.data_spliter("\| HEATER   :", "( )+ ")
        for l in csv_data:
            print(l)


if __name__ == '__main__':
    unittest.main()