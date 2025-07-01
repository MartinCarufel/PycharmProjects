import unittest
import main_spire
from main_spire import fetch_doc_in_dict, csv_construct_req
import re
import json


class TestSuiteMainSpireFetchDOcInDict(unittest.TestCase):
    def setUp(cls):
        with open("./test_data/testdata2.json", encoding="utf-8") as f:
            cls.test_data = json.load(f)
        with open("./test_data/req_test_data.json", encoding='utf-8') as f:
            cls.req_test_data = json.load(f)

    def tearDown(self):
        pass


    def test_req_extract(self):
        test_file = self.test_data["2"]["file name"]
        tc_table = fetch_doc_in_dict(test_file)
        result = csv_construct_req(tc_table[self.req_test_data["1"]["test case name id"]]
                                   [self.req_test_data["1"]["test step index"]]
                                   [self.req_test_data["1"]["test step col index"]])
        self.assertEqual(result, self.req_test_data["1"]["expected result"])