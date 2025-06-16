import unittest
import main
import main_spire

class TestSuite(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    def test_open_word(self):
        d = main.Word_collector("../DEV-0044600 STMN IOS Main Application Verification Specifications Rev 4.docx")
        print(type(d.doc))
        self.assertIsInstance(d.doc, docx.document.Document)
        self.assertIsInstance(d, main.Word_collector)

    def test_2(self):
        a = 10
        self.assertIsInstance(a, int)

    def test_clean_string(self):
        test_string = "6894_004, 6894_007,     6894_007\n\r, 342523"
        output = []
        main.clean_and_split(test_string, output)
        for i in output:
            print(i)


    def test_title_filter(self):
        test_strings = ["TC07001 – Indicating the battery level of the scanner",
                       "TC07003 - No scanner is detected - Manual connection (First time use)"]

        expected_string = [",Test Case,TC07001 - Indicating the battery level of the scanner,,,",
                           ",Test Case,TC07003 - No scanner is detected - Manual connection (First time use),,,"]

        for i in range(len(test_strings)):

            print(main_spire.csv_construct_tc(test_strings[i]))





