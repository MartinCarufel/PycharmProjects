import subprocess
import os
import sys
import re
import pandas as pd
from datetime import datetime
import shutil

# sys.path.append("D:/user_data/Martin/OneDrive/Documents/git/PycharmProjects/USB_Stress_test_log_parser")
sys.path.append("../USB_Stress_test_log_parser")
import log_parser


usb_strest_test_path = "C:/Users/dwos/Desktop/WST/vivo-usb-test/usb_stress_test.exe"

drop_frame_threshold = 7
fps_threshold = 29.95


def find_log():
    expression = "usb_stress_testIO-[0-9][0-9]-[0-9]{6}.log"
    dir_content = os.listdir(".")
    # print(dir_content)
    for i in range(len(dir_content)):
        file_found = re.match(pattern=expression, string=dir_content[i])
        # print(dir_content[i])
        if file_found != None:
            return file_found.group()

def extract_serial_number(file_name):
    reg_ex = 'IO-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]'  # Find in path/file the IO serial
    return re.search(pattern=reg_ex, string=file_name).group()

def display_result(fail_code, usb_error):
    pass_result =  """
**************************************************
*******************  PASS  ***********************
**************************************************"""

    fail_result =  """
==================================================
====== FAIL == FAIL == FAIL == FAIL == FAIL ======
=================================================="""
    error_sum = usb_error["Read to COM port failed with error code 995"] + \
                usb_error["USB error \(update gain CAM2_ID\): 1004"] + \
                usb_error["Stop everything"]

    if fail_code == 0 and error_sum == 0:
        print(pass_result)
    else:
        print(fail_result)
        print("----- Error Details -----")
        if fail_code & 0x01:
            print("Too many drop frame.")
        if fail_code & 0x02:
            print("Frame per second too low.")
        if error_sum != 0:
            print("USB connection issue or critical error.")

def log_test_result(hp_serial, fail_code, usb_error, dest_base_path):
    time_obj = datetime.now()
    time_str = time_obj.strftime("%Y-%m-%d_%H:%M:%S")
    message = time_str + " - HP: " + hp_serial + " - "
    error_sum = usb_error["Read to COM port failed with error code 995"] + \
                usb_error["USB error \(update gain CAM2_ID\): 1004"] + \
                usb_error["Stop everything"]

    if fail_code == 0 and error_sum == 0:
        message = message + "*** PASS ***"
    else:
        message = message + "ERROR - "
        if fail_code & 0x01:
            message = message + "Fail dropframe, "
        if fail_code & 0x02:
            message = message + "Fail FPS, "
        if error_sum != 0:
            message = message + "USB or critical error"
    try:
        dest = dest_base_path + "result.log"
        with open(dest, 'a') as f:
            f.writelines("{}\n" .format(message))
    except FileNotFoundError:
        os.mkdir(dest_base_path)
        with open(dest, 'a') as f:
            f.writelines("{}\n" .format(message))


def file_archive(file, dest_base_path):
    time_obj = datetime.now()
    time_str = time_obj.strftime("%Y-%m-%d_%H%M%S")
    dest_file = dest_base_path + file[:-4] + "_" + time_str + ".log"
    try:
        shutil.move(file, dest_file)
    except FileNotFoundError:
        os.mkdir(dest_base_path)
        shutil.copy(file, dest_file)


def main2():
    test_data_dest_base_path = "C:/test_data/"
    os.system(usb_strest_test_path)
    print("USB ST finished")
    log_file = find_log()
    # print(log_file)
    hp_serial = extract_serial_number(log_file)
    usb_error = log_parser.check_for_usb_error_v2(log_file, hp_serial)
    # print(usb_error)
    df = log_parser.convert_listcsv_to_dataframe(log_parser.extract_stress_test_data(log_file))
    fail_flag = log_parser.acceptance_test(df, drop_frame_criteria=drop_frame_threshold, fps_criteria=fps_threshold)  # fps 29.95
    display_result(fail_flag, usb_error)
    log_test_result(hp_serial, fail_flag, usb_error, test_data_dest_base_path)
    file_archive(log_file, test_data_dest_base_path)





    # print("Fail code: {}".format(fail_flag))
    # print("USB Error: {}".format(usb_error))
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # print(df[df['Duration'].between(13.0, 13.9)][
    #           '# total dropped'].max)  # Trouve la valeur max de toutes les lignes




def main():
    # file = "usb_stress_testIO-04-000979_disc.log"
    # reg_ex = 'IO-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]'  # Find in path/file the IO serial
    # hp_serial = re.search(pattern=reg_ex, string=file).group()


    # os.system(usb_strest_test_path)
    print("USB ST finished")

    expression = "usb_stress_testIO-[0-9][0-9]-[0-9]{6}.log"
    dir_content = os.listdir(".")
    # print(dir_content)
    for id in range(len(dir_content)):
    # for file in dir_content:
        result = re.match(expression, dir_content[id])
        if result != None:
            print("file found:" .format(dir_content[id]))
            reg_ex = 'IO-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]'  # Find in path/file the IO serial
            hp_serial = re.search(pattern=reg_ex, string=dir_content[id]).group()
            usb_error = log_parser.check_for_usb_error_v2(dir_content[id], hp_serial)
            # extract_data = log_parser.extract_stress_test_data(str(result))
            df = log_parser.convert_listcsv_to_dataframe(log_parser.extract_stress_test_data(dir_content[id]))
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            print(df[df['Duration'].between(13.0, 13.9)][
                      '# total dropped'].max)  # Trouve la valeur max de toutes les lignes
            fail_flag = log_parser.acceptance_test(df, drop_frame_criteria=7, fps_criteria=29.95)

            print("Fail code: {}".format(fail_flag))
            print("USB Error: {}".format(usb_error))
            break
        else:
            print("Not Found")


def test_re():
    import os
    expression = "usb_stress_testIO-[0-9][0-9]-[0-9]{6}.log"
    dir_content = os.listdir(".")
    # print(dir_content)
    for file in dir_content:
        result = re.match(expression, file)
        if result != None:
            print(result, result.string)
            break
        else:
            print("Not Found")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test_re()
    main2()


