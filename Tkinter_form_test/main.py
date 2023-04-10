import tkinter as tk
from tkinter import filedialog


class Form:
    def __init__(self):
        self.dir_path = ""
        self.root = tk.Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=20)
        self.root.columnconfigure(3, weight=1)
        self.dir_var = tk.StringVar()
        self.project_id = tk.StringVar()

        self.root.title("Test Tkinter")
        self.root.geometry('700x300')
        self.dir_lbl = tk.Label(self.root, text="Parent folder")
        self.dir_lbl.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.dir_entry = tk.Entry(self.root, textvariable=self.dir_var)
        self.dir_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)
        self.browse = tk.Button(self.root, text="Browse", command= self.browse)
        self.browse.grid(column=2, row=0, sticky=tk.EW, padx=5, pady=5)
        self.project_lbl = tk.Label(self.root, text="Project")
        self.project_lbl.grid(column=0, row=1, padx=5, pady=5)
        self.project_entry = tk.Entry(self.root, textvariable=self.project_id)
        self.project_entry.grid(column=1, row=1, padx=5, pady=5)
        self.submit = tk.Button(self.root, text="Run", command=self.submit)
        self.submit.grid(column=0, row=4, padx=5, pady=5)




    def submit(self):
        self.dir_path = self.dir_var.get()

        print(self.dir_path)
        pass

    def browse(self):
        self.path = filedialog.askdirectory()
        self.path = self.path.replace('/', '\\')
        self.dir_var.set(self.path)



app = Form()

app.root.mainloop()
