import unittest

class TestingCode(unittest.TestCase):
    def setUp(self):
        print("Setup test 1")

    def tearDown(self):
        print("Tear down test 1")

    def test_first_test(self):
        a = 10
        self.assertEqual(a, 10)

    def test_first_A(self):
        c = 1
        self.assertEqual(c, 1)

class TestingCode2(unittest.TestCase):
    def setUp(self):
        print("Setup test 2")

    def tearDown(self):
        print("Tear down test 2")

    def test_second_test(self):
        b = 20
        self.assertEqual(b, 20)

if __name__ == '__main__':
    unittest.main()