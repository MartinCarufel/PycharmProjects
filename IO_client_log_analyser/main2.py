from tkinter import filedialog
import pandas as pd

def main():
    sourcefile = filedialog.askopenfilename()
    keywords = ["Meshing Time", "GPU Texture mapping enabled", "Texturing Time", "Total meshing Time"]
    date = []
    time = []
    data_type = []
    value = []
    with open(sourcefile, mode='r') as f:
        for line in f:
            for keyword in keywords:
                if line.find(keyword) != -1:
                    line_splited = line.split(" - ")
                    # print(line, end="")
                    # print(line_splited)
                    date.append(line_splited[0][0:5])
                    time.append(line_splited[0][6:14])
                    data_type.append(line_splited[2].split(": ")[0])
                    value.append(line_splited[2].split(": ")[1][:-1])

                    break
    # print(date)
    # print(time)
    # print(data_type)
    # print(value)

    df = pd.DataFrame(columns=['Date', 'Time', 'Data Type', 'Value'])
    df['Date'] = date
    df['Time'] = time
    df['Data Type'] = data_type
    df['Value'] = value

    pd.set_option('display.max_rows', None)
    save_file_name = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[("CSV", '*.csv')])
    df.to_csv(save_file_name)
    print(df)



if __name__ == '__main__':
    main()
