import tkinter as tk
from tkinter import ttk

class My_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.toto = tk.IntVar()
        self.toto.set(0)
        self.tank = [{"id": 1, "name": "Tank 1", "capacity": 100, "level":0},
                     {"id": 2, "name": "Tank 2", "capacity": 200, "level":0}]
        # self.master = master
        self.main_win = tk.Canvas(self)
        self.main_win.pack()
        self.frame = ttk.Frame(self)
        self.progressBar = ttk.Progressbar(self.main_win, mode='determinate', orient="vertical", length=200,
                                           variable=self.toto)
        self.progressBar.pack(padx=10, pady=10)
        self.frame.pack(padx=5, pady=5)
        self.b1 = tk.Button(self, text="mod", command=lambda: self.tank_relative_level(1, 10))
        self.b1.pack()

    def tank_relative_level(self, id, value):
        for tank_id in range(len(self.tank)):
            if self.tank[tank_id]["id"] == id:
                # self.tank[tank_id]["level"] += value
                # self.progressBar["value"] = self.tank[tank_id]["level"]
                # print(self.tank[tank_id]["level"])
                # print(self.progressBar["value"])
                self.toto.set(self.toto.get() + 10)
                print(self.progressBar["value"])






        # self.main_win = tk.Canvas(self)
        # self.frame1 = ttk.Frame(self.main_win)
        # self.frame1.pack()
        # self.tank1 = ttk.Progressbar(self.frame1)
        # self.tank1.pack()


# root = tk.Tk()
app = My_app()
app.mainloop()
