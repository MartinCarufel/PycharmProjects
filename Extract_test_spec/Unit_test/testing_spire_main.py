import unittest
import main_spire
from main_spire import fetch_doc_in_dict
import re
import json


class TestSuiteMainSpireFetchDOcInDict(unittest.TestCase):
    def setUp(cls):
        with open("./test_data/testdata2.json", encoding="utf-8") as f:
            cls.test_data = json.load(f)

        pass

    def tearDown(self):
        pass

    def test_ouput_is_A_Dictionary_Structure(self):
        test_file = self.test_data["1"]["file name"]
        output_result = fetch_doc_in_dict(test_file)
        self.assertIsInstance(output_result, dict)

    def test_title_formating(self):
        test_file = self.test_data["1"]["file name"]
        expected_title_formating_pattern = re.compile(r"TC\d{5} –|- .+")
        # expected_title_formating_pattern = re.compile(r".")
        output_result = fetch_doc_in_dict(test_file)
        for key, value in output_result.items():
            self.assertIsNotNone(expected_title_formating_pattern.match(output_result[key][0]))

    def test_req_extract(self):
        # print(self.test_data)
        print(self.test_data["2"]["file name"])



