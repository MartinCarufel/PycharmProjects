import pandas as pd
from tkinter import filedialog
def find_last_max_value(file_path):
    # Define the path to your CSV file


    # Initialize a variable to store the last line with data
    last_data_line = None

    # Open the CSV file
    with open(csv_file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Strip whitespace from the line
            line = line.strip()

            # Check if the line is empty or contains only whitespace
            if line:
                # Update the last data line
                last_data_line = line

    # Check if any data was found in the file
    cols = ['avg mean', 'avg amd', 'avg stdev', 'avg 1sig', 'avg 2sig' ,'avg rms']
    last_data_line = last_data_line.lstrip(',').split(sep=',')
    print(last_data_line)
    df = pd.DataFrame([last_data_line], columns=cols)
    return df

def find_last_line(file_path):
    # Define the path to your CSV file
    line_count = 0

    # Initialize a variable to store the last line with data
    last_data_line = None

    # Open the CSV file
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Strip whitespace from the line
            line = line.strip()
            line_count += 1

    return line_count

def read_specific_line(file_path, line_number):
    # Initialize a counter to keep track of the line number
    current_line_number = 0

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Increment the line number counter
            current_line_number += 1

            # Check if the current line number matches the desired line number
            if current_line_number == line_number:
                # Return the content of the line
                line = line.strip()
                line = line.lstrip(',')
                line = line.split(',')
                return line  # Strip any leading/trailing whitespace

    # If the desired line number is not found, return None
    return None

def format_data_in_df(data, header):
    cols = header
    df = pd.DataFrame([data], columns=cols)
    return df


files_path = filedialog.askopenfilename()
last_line = find_last_line(files_path)
avg_line = read_specific_line(files_path, last_line-3)
print(format_data_in_df(avg_line, ["avg mean", "avg amd", "avg stdev", "avg 1sig", "avg 2sig", "avg rms"]))
print()
max_line = read_specific_line(files_path, last_line)
print(format_data_in_df(max_line, ["max mean", "max amd", "max stdev", "max 1sig", "max 2sig", "max rms"]))
