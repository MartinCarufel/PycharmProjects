import unittest
import sys

    class TestSuite(unittest.TestCase):

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')


    def test_1(self):

        for i in range(3):
            result = self.Runner()



    def Runner(self):
        cont = None
        # cont = raw_input('Continue? ')
        while cont not in ['y', 'n']:
            cont = raw_input('Continue? ')
            if cont == 'n':
                print('exit')
                self.exit(False)

        return True

    def exit(self, condition):
        try:
            assert condition

        except AssertionError:
            # self.tearDown()
            sys.exit()