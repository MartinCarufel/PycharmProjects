import tkinter as tk
from tkinter import ttk
import threading
from time import sleep

class My_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pump_th = threading.Thread(target=self.pump_thread)
        self.geometry("800x600")
        self.tank1_value = tk.IntVar()
        self.tank1_full_var = tk.BooleanVar()
        self.tank1_value.set(0)

        self.tank2_value = tk.IntVar()
        self.tank2_full_var = tk.BooleanVar()
        self.tank2_value.set(0)
        self.pump_button_state = (False)
        self.tank = [{"id": 1, "name": "Tank 1", "capacity": 100, "level":0},
                     {"id": 2, "name": "Tank 2", "capacity": 200, "level":0}]
        self.tank1_entry = 0
        self.main_win = tk.Canvas(self, width=800, height=400)
        self.main_win.pack(padx=20, side=tk.LEFT)
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=5, pady=5)
        self.tank1_level = ttk.Progressbar(self.main_win, mode='determinate', orient="vertical", length=200,
                                           variable=self.tank1_value, maximum=self.tank[0]["capacity"])
        self.tank1_level.grid(row=1, column=1, rowspan=3)
        self.tank1_full = tk.Checkbutton(self.main_win, state="disabled",
                        text="Full", variable=self.tank1_full_var)
        self.tank1_full.grid(row=1, column=2, sticky=tk.W)
        self.tank1_full_var.set(False)
        self.tank1_level_label = tk.Label(self.main_win, textvariable=self.tank1_value)
        self.tank1_level_label.grid(row=4, column=1)
        self.tank1_fill_button = tk.Button(self.main_win, text="Fill", command=lambda: self.fill_tank(1))
        self.tank1_fill_button.grid(row=2, column=2, padx=5)
        self.tank1_fill_value = tk.Entry(self.main_win, width= 4)
        self.tank1_fill_value.grid(row=2, column=3, padx=5)
        self.tank1_fill_value.bind('<Return>', func=lambda event: self.fill_tank(1))

        self.tank2_level = ttk.Progressbar(self.main_win, mode='determinate', orient="vertical", length=200,
                                           variable=self.tank2_value, maximum=self.tank[1]["capacity"])
        self.tank2_level.grid(row=1, column=5, rowspan=3)
        self.tank2_full = tk.Checkbutton(self.main_win, state="disabled",
                                         text="Full", variable=self.tank2_full_var)
        self.tank2_full.grid(row=1, column=6, sticky=tk.W)
        self.tank2_full_var.set(False)
        self.tank2_fill_button = tk.Button(self.main_win, text="Fill", command=lambda: self.fill_tank(2))
        self.tank2_fill_button.grid(row=2, column=6, padx=5)
        self.tank2_fill_value = tk.Entry(self.main_win, width=4)
        self.tank2_fill_value.grid(row=2, column=7, padx=5)
        self.tank2_fill_value.bind('<Return>', func=lambda event: self.fill_tank(2))
        self.tank2_level_label = tk.Label(self.main_win, textvariable=self.tank2_value)
        self.tank2_level_label.grid(row=4, column=5)
        self.pump_button = tk.Button(self.main_win, text="Pump", command=self.pump)
        self.pump_button.grid(row=4, column=4, padx=30, sticky=tk.W)

    def tank_relative_level(self, id, value):
        for tank_id in range(len(self.tank)):
            if self.tank[tank_id]["id"] == id:
                self.tank1_value.set(self.tank1_value.get() + 10)

    def fill_tank(self, tank, value=None):
        if value == None:
            if tank == 1:
                value = int(self.tank1_fill_value.get())
            if tank == 2:
                value = int(self.tank2_fill_value.get())
        new_tank_level = self.tank[tank-1]["level"] + value
        if new_tank_level < 0:
            self.tank[tank - 1]["level"] = 0
        elif new_tank_level > self.tank[tank-1]["capacity"]:
            self.tank[tank - 1]["level"] = self.tank[tank-1]["capacity"]
        else:
            self.tank[tank - 1]["level"] = self.tank[tank-1]["level"] + value
        if tank == 1:
            self.tank1_value.set(self.tank[tank-1]["level"])
        if tank == 2:
            self.tank2_value.set(self.tank[tank-1]["level"])
        self.check_full()

    def check_full(self):
        if self.tank[0]["level"] == self.tank[0]["capacity"]:
            self.tank1_full_var.set(True)
        else:
            self.tank1_full_var.set(False)
        if self.tank[1]["level"] == self.tank[1]["capacity"]:
            self.tank2_full_var.set(True)
        else:
            self.tank2_full_var.set(False)



    def pump(self):
        if not self.pump_button_state:
            self.th = threading.Thread(target=self.pump_thread)
            self.pump_button_state = True
            self.th.start()
            self.pump_button.config(relief='sunken')
        else:
            self.pump_button_state = False
            self.pump_button.config(relief='raise')


    def pump_thread(self):
        while self.pump_button_state:
            fill = min(self.tank[0]["level"], 1)
            self.fill_tank(1, -fill)
            self.fill_tank(2, fill)
            sleep(0.1)


app = My_app()
app.mainloop()
