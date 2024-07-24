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
        test_data = ['05-28 13:47:18', '05-28 13:58:47', '05-28 14:16:47', '05-28 14:29:58', '05-28 14:38:58',
                     '05-28 14:48:08', '05-28 14:57:30', '05-28 15:20:30', '05-28 15:28:32', '05-28 15:36:17',
                     '05-28 15:42:11', '05-28 15:48:58']
        start_time = self.Process_time.get_start_process_time("../Test data/IOClient.txt_05-28-2024_13-23-42.617.txt")
        self.assertListEqual(start_time, test_data)

    def test_get_stop_time(self):
        test_data = ['05-28 13:47:45', '05-28 13:59:15', '05-28 14:17:21', '05-28 14:30:37', '05-28 14:39:28',
                     '05-28 14:48:33', '05-28 14:58:03', '05-28 15:21:00', '05-28 15:29:00', '05-28 15:36:44',
                     '05-28 15:42:41', '05-28 15:49:25']
        stop_time = self.Process_time.get_stop_process_time("../Test data/IOClient.txt_05-28-2024_13-23-42.617.txt")
        self.assertListEqual(stop_time, test_data)

    def test_merge_list(self):
        test_data = [('05-28 13:47:18', '05-28 13:47:45'), ('05-28 13:58:47', '05-28 13:59:15'), ('05-28 14:16:47', '05-28 14:17:21')]
        start_list = ['05-28 13:47:18', '05-28 13:58:47', '05-28 14:16:47']
        stop_list = ['05-28 13:47:45', '05-28 13:59:15', '05-28 14:17:21']
        merge_list = self.Process_time.create_start_stop_tupple_list(start_list, stop_list)
        self.assertListEqual(merge_list, test_data)

    def test_process_time(self):
        test_result= 252000
        # start = "05-28 13:47:18"
        # stop = "05-28 13:47:45"
        start = "01-29 12:00:00"
        stop = "02-01 10:00:00"
        pt = self.Process_time.process_time_calculation(start, stop)
        self.assertEqual(test_result, pt)


    def test_start_proc_line(self):
        start_time = self.Process_time.get_start_process_line_number("../Test data/IOClient.txt_05-28-2024_13-23-42.617.txt")
        print(start_time)

    def test_stop_line_id_new_view(self):
        start_time = self.Process_time.get_start_process_line_number("../Test data/IOClient.txt_05-28-2024_13-23-42.617.txt")
        stop_process_line_id = self.Process_time.get_next_switch_view("../Test data/IOClient.txt_05-28-2024_13-23-42.617.txt", start_time)
        print(stop_process_line_id)

    def test_merge_line_number_id(self):
        start_list = [1731, 2021, 2432, 2737, 3017, 3278, 3592, 4198, 4522, 4812, 5053, 5846]
        stop_list = [1769, 2063, 2468, 2772, 3051, 3349, 3626, 4235, 4557, 4846, 5617, 5982]
        merge_list = self.Process_time.create_start_stop_tupple_list(start_list, stop_list)
        print("\n", merge_list)

    def test_get_time_stamp(self):
        print()
        print(self.Process_time.get_line_time_stamp("../Test data/IOClient.txt_05-28-2024_13-23-42.617.txt", 17))
        print(self.Process_time.get_line_time_stamp("../Test data/IOClient.txt_05-28-2024_13-23-42.617.txt", 18))





