from text_file_analyser import Text_File_analyser
import pandas as pd



def main():
    tf = Text_File_analyser("usb_stress_testIO-04-000979.log")
    csv_data = tf.data_spliter("\| Date :", " +")
    df = pd.DataFrame(csv_data)
    df = df[[3, 4]]
    print(df)

def main2():

    # Creating the dataframe
    df = pd.DataFrame({"A": [12, 4, 5, None, 1],
                       "B": [7, 2, 54, 3, None],
                       "C": [20, 16, 11, 3, 8],
                       "D": [14, 3, None, 2, 6]})

    print(df)

    # skip the Na values while finding the maximum
    print(df.max(axis=1, skipna=True))

if __name__ == '__main__':
    main()