import tkinter as tk
from tkinter import ttk

class My_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.tank1_value = tk.IntVar()
        self.tank1_full_var = tk.BooleanVar()
        self.tank1_value.set(0)
        self.tank = [{"id": 1, "name": "Tank 1", "capacity": 100, "level":0},
                     {"id": 2, "name": "Tank 2", "capacity": 200, "level":0}]
        self.tank1_entry = 0
        # self.master = master
        self.main_win = tk.Canvas(self, width=800, height=400)
        self.main_win.pack(padx=20, side=tk.LEFT)
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=5, pady=5)
        self.tank1_level = ttk.Progressbar(self.main_win, mode='determinate', orient="vertical", length=200,
                                           variable=self.tank1_value)
        self.tank1_level.grid(row=1, column=1, rowspan=3)
        self.tank1_full = tk.Checkbutton(self.main_win, state="disabled",
                        text="Full", variable=self.tank1_full_var)
        self.tank1_full.grid(row=1, column=2, sticky=tk.W)
        self.tank1_full_var.set(True)
        self.tank1_level_label = tk.Label(self.main_win, textvariable=self.tank1_value)
        self.tank1_level_label.grid(row=4, column=1)
        # self.tank1_full_label = tk.Label(self.main_win, text="Full")
        # self.tank1_full_label.grid(row=1, column=3, sticky=tk.W)
        self.tank1_fill_button = tk.Button(self.main_win, text="Fill", command=lambda: self.fill_tank(1, self.tank1_entry))
        self.tank1_fill_button.grid(row=2, column=2, padx=5)
        self.tank1_entry = self.tank1_fill_value = tk.Entry(self.main_win)
        self.tank1_fill_value.grid(row=2, column=3)

    def tank_relative_level(self, id, value):
        for tank_id in range(len(self.tank)):
            if self.tank[tank_id]["id"] == id:
                # self.tank[tank_id]["level"] += value
                # self.progressBar["value"] = self.tank[tank_id]["level"]
                # print(self.tank[tank_id]["level"])
                # print(self.progressBar["value"])
                self.tank1_value.set(self.tank1_value.get() + 10)

    def fill_tank(self, tank, value):
        value = int(self.tank1_value.get())
        print(value)
        if tank == 1:
            if self.tank[tank-1]["level"] < self.tank[tank-1]["capacity"]:
                self.tank[tank-1]["level"] = max(self.tank[tank-1]["level"] + value, self.tank[tank-1]["capacity"])
                self.tank1_value.set(self.tank[tank-1]["level"])

        pass






        # self.main_win = tk.Canvas(self)
        # self.frame1 = ttk.Frame(self.main_win)
        # self.frame1.pack()
        # self.tank1 = ttk.Progressbar(self.frame1)
        # self.tank1.pack()


# root = tk.Tk()
app = My_app()
app.mainloop()
