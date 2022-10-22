import subprocess
import os
import sys
import re
import pandas as pd

# sys.path.append("D:/user_data/Martin/OneDrive/Documents/git/PycharmProjects/USB_Stress_test_log_parser")
sys.path.append("C:/Users/mcarufel/Documents/Github/PycharmProjects/USB_Stress_test_log_parser")
import log_parser


usb_strest_test_path = "C:/tools/scanner-io-4.0.1-484-hptest/usb_stress_test.exe"

def main():
    file = "usb_stress_testIO-04-000979_disc.log"
    reg_ex = 'IO-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]'  # Find in path/file the IO serial
    hp_serial = re.search(pattern=reg_ex, string=file).group()
    os.system(usb_strest_test_path)
    print("USB ST finished")
    usb_error = log_parser.check_for_usb_error_v2(file, hp_serial)
    extract_data = log_parser.extract_stress_test_data(file)
    df = log_parser.convert_listcsv_to_dataframe(log_parser.extract_stress_test_data(file))
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    # print(df[df['Duration'].between(13.0, 13.9)]['# total dropped'].max)  # Trouve la valeur max de toutes les lignes
    fail_flag = log_parser.acceptance_test(df, drop_frame_criteria=7, fps_criteria= 29.95)

    print("Fail code: {}" .format(fail_flag))
    print("USB Error: {}" .format(usb_error))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


