
import regex
from tkinter import filedialog
from datetime import datetime
class Process_time:

    def __init__(self):
        self.file_path = filedialog.askopenfilename()
        self.start_stop_time = None
        self.start_process_line_number = []
        self.stop_process_time_list = []
        pass

    def get_start_process_time(self):
        start_process_time_list = []
        start_regex_pattern = "IOBridgeThread - startPostProcessing"
        compile_regex_start = regex.compile(start_regex_pattern)
        with open(self.file_path, mode='r') as f:
            lines = f.readlines()
            for line in lines:
                if compile_regex_start.search(line) != None:
                    start_process_time_list.append(line[0:14])
                    pass
                else:
                    pass
        return start_process_time_list

    def get_start_process_line_number(self):
        start_regex_pattern = "IOBridgeThread - startPostProcessing"
        compile_regex_start = regex.compile(start_regex_pattern)
        with open(self.file_path, mode='r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if compile_regex_start.search(lines[i]) != None:
                    self.start_process_line_number.append(i)
                    pass
                else:
                    pass
        return self.start_process_line_number

    def get_next_switch_view(self):
        start_list = self.start_process_line_number.copy()
        # stop_regex_pattern = "Post processing popup closed"
        stop_regex_pattern = "View entered : Review view"
        compile_regex_stop = regex.compile(stop_regex_pattern)
        with open(self.file_path, mode='r') as f:
            lines = f.readlines()
            start_list.append(len(lines))
            for st_list_id in range(len(start_list)-1):
                for line_id in range(start_list[st_list_id], start_list[st_list_id+1], +1):
                    if compile_regex_stop.search(lines[line_id]) != None:
                        self.stop_process_time_list.append(line_id)
                        break
        return self.stop_process_time_list


    def get_stop_process_time(self):
        stop_process_time_list = []
        # stop_regex_pattern = "Post processing popup closed"
        stop_regex_pattern = "View exited : Review view"
        compile_regex_stop = regex.compile(stop_regex_pattern)
        with open(self.file_path, mode='r') as f:
            lines = f.readlines()
            for line in lines:
                if compile_regex_stop.search(line) != None:
                    stop_process_time_list.append(line[0:14])
                else:
                    pass
        return stop_process_time_list

    def create_start_stop_tupple_list(self, start_list, stop_list):
        start_stop_process_time = []
        if len(start_list) == len(stop_list):
            for i in range(len(start_list)):
                start_stop_process_time.append((start_list[i], stop_list[i]))
        else:
            print("Number of element of start list doesn't match the number of element of stop list")
        return start_stop_process_time

    def process_time_calculation(self, start_time, stop_time):
        proc_time = 0
        month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        start_month = int(start_time[0:2])
        start_day = int(start_time[3:5])
        start_hour = int(start_time[6:8])
        start_minute = int(start_time[9:11])
        start_second = int(start_time[12:])
        stop_month = int(stop_time[0:2])
        stop_day = int(stop_time[3:5])
        stop_hour = int(stop_time[6:8])
        stop_minute = int(stop_time[9:11])
        stop_second = int(stop_time[12:])
        if start_month == stop_month:
            proc_time = ((stop_day * 24 * 3600 + stop_hour * 3600 + stop_minute * 60 + stop_second) -
                         (start_day * 24 * 3600 + start_hour * 3600 + start_minute * 60 + start_second))
        else:
            proc_time = ((month_days[start_month] - start_day) * 24 * 3600 + stop_day * 24 * 3600 + stop_hour * 3600 +
                         stop_minute + stop_second) - (start_hour * 3600 + start_minute * 60 + start_second )
        return proc_time

    def get_line_time_stamp(self, line_no):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            return lines[line_no][0:14]

    def display_process_time(self, process_time_list):
        print('Process start line number, Process end line number, process time (s)')
        for i in range(len(process_time_list)):
            print(f'{self.start_process_line_number[i]+1},{self.stop_process_time_list[i]+1},{process_time_list[i]}')

    def export_to_csv(self, process_time_list):
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d_%H%M%S")
        with open(f"Process_time_{formatted_now}.csv", 'w') as f:
            f.writelines('Process start line number, Process end line number, process time (s)\n')

            for i in range(len(process_time_list)):
                f.writelines(f'{self.start_process_line_number[i]+1},{self.stop_process_time_list[i]+1},{process_time_list[i]}\n')



def main():
    process_time_calc = []
    pt = Process_time()
    path = filedialog.askopenfilename()
    # path = r"C:\Users\u120230\git\PycharmProjects\IOS Processing time\Test data\IOClient.txt_05-28-2024_13-23-42.617.txt"
    start_process_time = pt.get_start_process_time(path)
    stop_process_time = pt.get_stop_process_time(path)
    start_stop_time = pt.create_start_stop_tupple_list(start_process_time, stop_process_time)
    for start, stop in start_stop_time:
        process_time_calc.append(pt.process_time_calculation(start, stop))
    print(process_time_calc)

def main2():
    process_time_calc = []
    pt = Process_time()
    # path = filedialog.askopenfilename()
    # path = r"C:\Users\u120230\git\PycharmProjects\IOS Processing time\Test data\IOClient.txt_05-28-2024_13-23-42.617.txt"

    start_proc_line_number_list = pt.get_start_process_line_number()
    stop_proc_line_number_list = pt.get_next_switch_view()
    start_stop_list = pt.create_start_stop_tupple_list(start_proc_line_number_list, stop_proc_line_number_list)

    for start, stop in start_stop_list:
        process_time_calc.append(pt.process_time_calculation(pt.get_line_time_stamp(start),
                                                             pt.get_line_time_stamp(stop)))
    pt.display_process_time(process_time_calc)
    pt.export_to_csv(process_time_calc)



if __name__ == '__main__':
    main2()

