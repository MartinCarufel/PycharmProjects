import main
import unittest
import mock

class Test_module(unittest.TestCase):

    def setUp(self):
        self.o = main.Name_draw()

    def test_draw_name(self):
        # o = main.Name_draw()
        self.o.participant_in = ['Eric', 'Luc', 'Martin', 'Jean', 'Jacques', 'Albert', 'Paul', 'Yves', 'Samuel']
        self.o.draw_name()
        self.assertIsInstance(self.o.name_draw, str)

    def test_convert_file_to_list(self):
        test_list = self.o.convert_file_to_list('test_participants.txt')
        print(test_list)
        self.assertListEqual(test_list, ['Eric', 'Luc', 'Martin', 'Jean', 'Jacques', 'Albert', 'Paul', 'Yves', 'Samuel'])

    def test_name_accepted(self):
        self.o.participant_in = ['Toto', 'Tata']
        self.o.name_draw = "Toto"
        with mock.patch('builtins.input', return_value="y"):
            self.assertEqual(self.o.accept_the_name().upper(), 'Y')
            self.assertEqual(self.o.participant_in, ['Tata'])
        print(self.o.participant_in)

    def test_name_not_accepted(self):
        self.o.participant_in = ['Toto', 'Tata']
        self.o.name_draw = "Toto"
        with mock.patch('builtins.input', return_value="n"):
            self.assertEqual(self.o.accept_the_name().upper(), 'N')
            self.assertEqual(self.o.participant_in, ['Toto', 'Tata'])
        print(self.o.participant_in)

    def test_convert_list_to_file(self):
        file = 'write_to_file.txt'
        list = ['Tata', 'Toto', 'Tutu', 'Titi']
        self.o.convert_list_to_file(list, file)


if __name__ == '__main__':
    unittest.autotest()