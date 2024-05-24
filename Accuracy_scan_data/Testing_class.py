import unittest
import scan_data
import regex

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
        print(df["RMS"])
