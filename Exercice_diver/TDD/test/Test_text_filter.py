# coding: utf-8

from unittest import TestCase
from ..source.text_filter import get_number_part


class Test_text_filter(TestCase):

    def test_case1(self):
        digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        to_test = "Temp00734400"
        for i in get_number_part(to_test):
            self.assertIn(int(i), digit)


