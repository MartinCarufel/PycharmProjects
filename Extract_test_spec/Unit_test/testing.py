import unittest
import main

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
