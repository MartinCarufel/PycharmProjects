import pandas as pd
import re
import sys
import os


def average(lst):
    return sum(lst) / len(lst)


def prog_setup():
    param_file_name = str(sys.argv[1])
    reg_ex = 'IO-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]'    # Find in path/file the IO serial
    hp_serial = re.search(pattern=reg_ex, string=param_file_name).group()
    return (param_file_name, hp_serial)


def check_for_usb_error(input_file):
    """
    This function check for USB error. Take a text file and look for specific error string.

    """
    error_strings = ["Read to COM port failed with error code 995"]
    usb_error_count = 0
    with open(input_file, mode='r') as f:
        for line in f:
            for error_str in error_strings:
                if re.match(error_str, line) is not None:
                    usb_error_count += 1
    return (input_file, usb_error_count)

def check_for_usb_error_v2(input_file, hp_serial):
    """
    This function check for USB error. Take a text file and look for specific error string.

    """
    data_summary = open("Data_summary.csv", mode='a')
    error_strings = ["Read to COM port failed with error code 995",
                     "USB error (update gain CAM2_ID): 1004"]
    usb_error_count = 0
    with open(input_file, mode='r') as f:
        for line in f:
            for error_str in error_strings:
                if re.match(error_str, line) is not None:
                    usb_error_count += 1
    for error in error_strings:
        data_summary.write(hp_serial + ',' + error + ',' + str(usb_error_count)  + "\n")
    # return (usb_error_count)


def extract_stress_test_data(input_file):
    """
    This function get in input the file output log from the USB Stress test in format text
    and convert only the test result data second per second into a two dim list of CSV string. Each column are splits
    with comma.

    input_file: usb stress test log.txt
    output: list of a list of string data

    ex on input file
    +--------------------------------------------------------------------------------------+
    | START
    STRESS
    TEST |
    | |
    | Date: 02 / 02 / 22
    12: 21:53 |
    ...
    +----------+---------------+----------------+----------------+----------+----------+----------+--------+--------------+--------------+--------------+--------------+
    | duration |  # total frames | #total bad pkt | #total dropped | #frames  | #dropped | avg. fps |  MB/s  | #C0 Dead img | #C1 Dead img | #C2 Dead img | #C3 Dead img |
    +----------+---------------+----------------+----------------+----------+----------+----------+--------+--------------+--------------+--------------+--------------+
    Warm - Up 2.00 seconds...

    *****Data that will be collected***
    | 1.00 | 30 | 0 | 0 | 30 | 0 | 30.00 | 295.42 | 0 | 0 | 0 | 0 |
    | 2.00 | 60 | 0 | 0 | 30 | 0 | 30.00 | 295.37 | 0 | 0 | 0 | 0 |
    | 3.00 | 90 | 0 | 0 | 30 | 0 | 30.00 | 295.49 | 0 | 0 | 0 | 0 |
    ....
    """

    match_data = "\| +[0-9]+.[0-9][0-9]"    # Regex to find the test result data to filter out any other text
    match_pattern = "\| +"                  # Regex to find all separating character between to text column
    csv_data = []

    with open(input_file, mode='r') as f:
        for line in f:
            if re.match(match_data, line) is not None:
                new_line = re.sub(pattern=match_pattern, repl=",", string=line)[1:-2]
                csv_data.append(new_line.split(sep=','))
    return csv_data


header = ["Duration", "# Total Frame", "# total bad pkt",  "# total dropped", "# frames",
          "# dropped", "avg. fps", "MB/s", "#C0 Dead img", "#C1 Dead img", "#C2 Dead img", "#C3 Dead img"]


def convert_listcsv_to_dataframe(csv_data, hp_serial="xxxxxxx"):
    """
    This function take as input a list of list of string extracted from the USB Stress
    test and convert it to a dataframe.
     """

    header = ["Duration", "# Total Frame", "# total bad pkt", "# total dropped", "# frames",
              "# dropped", "avg. fps", "MB/s", "#C0 Dead img", "#C1 Dead img", "#C2 Dead img", "#C3 Dead img"]
    df = pd.DataFrame(csv_data, columns=header)
    df["Duration"] = df["Duration"].astype(float)
    df["avg. fps"] = df["avg. fps"].astype(float)
    df["# total dropped"] = df["# total dropped"].astype(int)
    df.to_excel("Export_data " + hp_serial + ".xlsx")
    return df


def compile_test_data_per_minute(df, hp_serial="xxxxxxx"):
    total_drop = []
    avg_fps_list = []
    avg_fps = []
    nb_line, nb_col = df.shape
    thread_duration = int(df["Duration"].max())
    for i in range(0, nb_line):
        if i == 0:
            avg_fps.append(df["avg. fps"].iloc[i])
        elif int(df["Duration"].iloc[i]) < thread_duration:
            avg_fps.append(df["avg. fps"].iloc[i])
        else:
            total_drop.append(df["# total dropped"].iloc[i-1])
            avg_fps_list.append(average(avg_fps))
            avg_fps = []
            avg_fps.append(df["avg. fps"].iloc[i])
    df_summary = pd.DataFrame()
    df_summary["Total Drop Frame"] = total_drop
    df_summary["Total Drop Frame"] = df_summary["Total Drop Frame"].astype(int)
    df_summary["Avg FPS"] = avg_fps_list
    df_summary["Avg FPS"] = df_summary["Avg FPS"].round(decimals=3)
    df_summary.to_excel("Export_summary " + hp_serial + ".xlsx")
    return df_summary


def create_test_result_summary_csv(hp_serial, df_summary, pod_serial="no POD SN found"):
    """
    This function create a CSV file that summarize for the given HP the total of drop frame and the average FPS
    for each thread
    :param hp_serial:
    :param df_summary:
    :return:
    """
    if not os.path.exists("Data_summary.csv"):
        data_summary = open("Data_summary.csv", mode='w')
        data_summary.close()


    data_summary = open("Data_summary.csv", mode='a')
    # data_summary.writelines("ALLO\n")
    if pod_serial != None:
        data_summary.write("POD Serial," + pod_serial + "\n")
    data_summary.writelines("hp serial,Thread,Total Drop Frame,Avg FPS\n")
    print('File Data_summary.csv created\n')
    for index, row in df_summary.iterrows():
        data_summary.write(hp_serial + ',' + str(int(index)) + ',' + str(int((row["Total Drop Frame"]))) + ',' + str(row["Avg FPS"]) + ',')
        data_summary.write("\n")
    data_summary.write(hp_serial + ',' + 'Average drop frame,' + str(df_summary["Total Drop Frame"].mean()) + "\n")
    data_summary.write(hp_serial + ',' + 'Max drop frame,' + str(df_summary["Total Drop Frame"].max()) + "\n")
    data_summary.write(hp_serial + ',' + 'Min drop frame,' + str(df_summary["Total Drop Frame"].min()) + "\n")
    data_summary.write(hp_serial + ',' + 'Avg FPS,' + str(df_summary["Avg FPS"].mean()) + "\n")

    data_summary.close()


def get_path_list_from_file(file):
    """
    Read a text file that contain path\filename and return a list of path and convert DOS '\' with Python '/'
    :param file:
    :return: list
    """
    with open(file, mode='r') as f:
        path_list = []
        for line in f:
            line = line.replace('\\', '/')
            line = line.replace('\n', '')
            path_list.append(line)
    return path_list


def main():
    usb_err_summary = []
    for file in get_path_list_from_file('File_list_to_analyse.txt'):
        reg_ex = 'IO-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]'  # Find in path/file the IO serial
        hp_serial = re.search(pattern=reg_ex, string=file).group()
        reg_ex2 = 'DWIOK-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]'  # Find in path/file the DWIOK serial
        pod_serial = re.search(pattern=reg_ex2, string=file).group()
        print("Process the log for HP {}.".format(hp_serial))
        usb_err_summary.append(check_for_usb_error(file))
        csv_data = extract_stress_test_data(file)
        df = convert_listcsv_to_dataframe(csv_data, hp_serial=hp_serial)
        summary = compile_test_data_per_minute(df, hp_serial, pod_serial)
        create_test_result_summary_csv(hp_serial, summary)
        check_for_usb_error_v2(file, hp_serial)

    print('DONE !')


if __name__ == '__main__':
    main()
