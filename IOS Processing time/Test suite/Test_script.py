import unittest
import main

class test_script(unittest.TestCase):

    # def __init__(self, *args):
    #     super().__init__()
    #     self.screenshot = None
    def setUp(self):
        self.Process_time = main.Process_time()
        pass

    def tearDown(self):
        pass

    def test_get_start_time(self):
        start_time = self.Process_time.get_start_process_time("../Test data/IOClient.txt_05-28-2024_13-23-42.617.txt")
        print(len(start_time))
        print(start_time)

    def test_get_stop_time(self):
        stop_time = self.Process_time.get_stop_process_time("../Test data/IOClient.txt_05-28-2024_13-23-42.617.txt")
        print(len(stop_time))
        print(stop_time)


    def test_merge_list(self):
        start_list = ['05-28 13:47:18', '05-28 13:58:47', '05-28 14:16:47', '05-28 14:29:58', '05-28 14:38:58',
                      '05-28 14:48:08', '05-28 14:57:30', '05-28 15:20:30', '05-28 15:28:32', '05-28 15:36:17',
                      '05-28 15:42:11', '05-28 15:48:58']
        stop_list = ['05-28 13:47:45', '05-28 13:59:15', '05-28 14:17:21', '05-28 14:30:37', '05-28 14:39:28',
                     '05-28 14:48:33', '05-28 14:58:03', '05-28 15:21:00', '05-28 15:29:00', '05-28 15:36:44',
                     '05-28 15:42:41', '05-28 15:49:25']

        merge_list = self.Process_time.create_start_stop_tupple_list(start_list, stop_list)
        print(merge_list)

    def test_process_time(self):
        # start = "05-28 13:47:18"
        # stop = "05-28 13:47:45"
        start = "01-29 12:00:00"
        stop = "02-01 10:00:00"
        pt = self.Process_time.process_time_calculation(start, stop)
        print(pt)


