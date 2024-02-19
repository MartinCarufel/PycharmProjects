from datetime import datetime

import matplotlib.axis
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.patches import FancyArrowPatch
class T_data:
    def __init__(self):
        " 2024-02-01 10:46:37"
        self.df = pd.read_csv("temperature_IO-04-007131_2024-02-15.csv")
        self.df2 = pd.read_csv("tamb 20c 7131_0215_154550.csv", skiprows=8)
        self.plt_title = "Pre-heating HP IO-04-007131 with sleeve 1"
        self.D_ZERO = self.df.iloc[0, 0][1:12]
        print(self.D_ZERO)
        self.T_ZERO = self.df.iloc[0, 0][12:]
        print(self.T_ZERO)
        self.CSV_ROWS, col = self.df.shape
        # self.D_ZERO = "2024-02-01"
        # self.T_ZERO = "10:46:37"
        # self.CSV_ROWS = 400

    def split_date(self, datestring_to_split):
        """
        :param datestring_to_split: date in format yyyy-mm-dd
        :return:
        """
        year = int(datestring_to_split[0:4])
        month = int(datestring_to_split[5:7])
        day = int(datestring_to_split[8:])

        return (year, month, day)

    def split_time(self, time_to_split):
        """
        :param time_to_split: time format HH:mm:ss
        :return:
        """

        hour = int(time_to_split[0:2])
        min = int(time_to_split[3:5])
        sec = int(time_to_split[6:])
        return (hour, min, sec)



    def delta_time_count(self, first_date, first_time, second_date, second_time):
        f_date = self.split_date(first_date)
        f_time = self.split_time(first_time)
        s_date = self.split_date(second_date)
        s_time = self.split_time(second_time)

        delta = datetime(s_date[0], s_date[1], s_date[2], hour=s_time[0], minute=s_time[1], second=s_time[2]) -\
                datetime(f_date[0], f_date[1], f_date[2], hour=f_time[0], minute=f_time[1], second=f_time[2])
        return int(delta.total_seconds())

    def create_universal_time_list(self):
        u_time = []
        for ind in self.df.index:
            # print(self.df["time_ms"][ind])
            u_time.append(self.delta_time_count(self.D_ZERO, self.T_ZERO, self.df["time_ms"][ind][1:11],
                                                self.df["time_ms"][ind][12:]))
        self.df["uTime"] = u_time
        self.df.to_csv("export.csv")
        return u_time

    def create_summary_dataframe(self):
        df = pd.DataFrame()
        df2 = pd.DataFrame()
        extr_col = self.df["uTime"]
        df.insert(0, "OSG Time", extr_col)
        extr_col = self.df["heater_C"]
        df.insert(1, "Heater", extr_col)
        extr_col = self.df["preheating_state"]
        df.insert(2, "Ready", extr_col)
        df.loc[df["Ready"] != "Ready", "Ready"] = 0
        df.loc[df["Ready"] == "Ready", "Ready"] = 45
        extr_col = self.df2["Scan Relative Time"]
        df2.insert(0, "time Tcouple", extr_col)
        extr_col = self.df2["CH3"]
        df2.insert(1, "amb", extr_col)
        extr_col = self.df2["CH2"]
        df2.insert(2, "Mirror", extr_col)
        return (df, df2)


    def plot_a(self):
        self.df[["uTime", "heater_C", "cam0_C", "cam1_C", "cam2_C", "cam3_C", "uvProj_C"]].plot(x="uTime")
        plt.xlabel("Time (s)")
        plt.ylabel("Temperature (°C)")
        # arrow1 = plt.arrow(x=741, y=43.5, dx=-160, dy=-10, width=10, head_starts_at_zero=False, length_includes_head=True)
        plt.annotate("Start\nScan", xy=(743, 43.2), xytext=(512, 34), arrowprops={'arrowstyle':'->'})
        # plt.savefig("figure1.svg", format="svg")
        plt.show()

    def plot_b(self):
        fig, ax = plt.subplots()
        # print(self.df["uTime"])
        self.df.plot(x="uTime", y=["heater_C", "cam0_C", "cam1_C", "cam2_C", "cam3_C", "uvProj_C"],
                     figsize=[8, 6], ax=ax)


        # ax.annotate("Start\nScan", xy=(300, 43.2), xytext=(200, 30), arrowprops={'arrowstyle':'-', 'lw':1.5})
        plt.xlabel('Time (s)')
        plt.ylabel('Temperature (°C)')
        plt.show()
def main():
    dt = T_data()
    u_time_list = dt.create_universal_time_list()
    new_df1, new_df2 = dt.create_summary_dataframe()
    print(new_df1, new_df2)
    # print(u_time_list)
    # print(dt.df["uTime"])
    plt.close("all")
    # dt.df.plot.line(x="uTime", y="heater_C")
    dt.df.to_csv("export.csv")
    # dt.plot_b()
    ax = new_df1.plot(x="OSG Time", y="Heater", x_compat=True)
    new_df1.plot(ax=ax, x="OSG Time", y="Ready")
    new_df2.plot(ax=ax, x="time Tcouple", y="amb")
    new_df2.plot(ax=ax, x="time Tcouple", y="Mirror")
    plt.text(100, 25, "allo")
    plt.title(dt.plt_title)
    plt.xlabel('Time (s)')
    plt.xticks(rotation='vertical')
    plt.ylabel('Temperature (°C)')
    xspace = 15
    yspace = 2
    ax.xaxis.set_major_locator(ticker.MultipleLocator(xspace))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(yspace))
    plt.grid()
    plt.ylim(15, 47)
    plt.xlim(0, max(new_df1["OSG Time"]))
    plt.show()

    # dt.df.plot.scatter(x="uTime", y="heater_C")
    # # ts = dt.df["heater_C"]
    # arrow = FancyArrowPatch((512, 34), (743, 43.2))





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

