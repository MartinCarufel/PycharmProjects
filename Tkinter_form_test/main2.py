import tkinter as tk
from tkinter import ttk as ttk
from tkinter import filedialog

from tkinter import filedialog
import os
import requests
import json

class Form(tk.Frame):
    def __init__(self, root, cont):
        super().__init__(root)
        self.root = cont
        self.dir_path = ""
        self.project_id = ""
        self.section_id = ""
        # self.root = tk.Tk()
        self.dir_var = tk.StringVar()
        self.project_var = tk.StringVar()
        self.project_var.set("2")
        self.section_var = tk.StringVar()
        self._create_gui()
        self.pack()

    def _create_gui(self):
        # self.root.title("Test Tkinter")
        # self.root.geometry("700x200")
        dir_lbl = tk.Label(self, text="Parent folder")
        dir_lbl.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        dir_entry = tk.Entry(self, textvariable=self.dir_var)
        dir_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)
        browse = tk.Button(self, text="Browse", command=self.browse, width=10)
        browse.grid(column=2, row=0, sticky=tk.EW, padx=5, pady=5)

        project_lbl = tk.Label(self, text="Project")
        project_lbl.grid(column=0, row=1, padx=5, pady=5)
        project_entry = tk.Entry(self, textvariable=self.project_var)
        project_entry.grid(column=1, row=1, padx=5, pady=5, sticky=tk.W)
        section_lbl = tk.Label(self, text="Section")
        section_lbl.grid(column=0, row=2, padx=5, pady=5)
        section_entry = tk.Entry(self, textvariable=self.section_var)
        section_entry.grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)
        submit = tk.Button(self, text="Run", command=self.submit, width=8)
        submit.grid(column=0, row=3, padx=5, pady=5)
        exit_button = tk.Button(self, text="Exit", command=self.root.destroy, width=12)
        exit_button.grid(column=1, row=3, )

    def submit(self):
        self.dir_path = self.dir_var.get()
        self.project_id = self.project_var.get()
        self.section_id = self.section_var.get()
        print("path: {}".format(self.dir_path))
        print("Project: {}".format(self.project_id))
        print("Section: {}".format(self.section_id))
        creator = Folder_creator("martin.carufel@dental-wings.com", '18,Mac&Amo')
        creator.tr_section_http_request(self.project_id, self.section_id)
        creator.create_folder_list()
        creator.create_subfolder(self.dir_path)

    def browse(self):
        self.path = filedialog.askdirectory()
        self.path = self.path.replace('/', '\\')
        self.dir_var.set(self.path)


class Folder_creator:
    def __init__(self, user, password):
        self.USER = user
        self.PASSWORD = password
        self.head = {"Content-Type": "application/json"}
        self.rjson = None
        self.parent_folder = ""
        self.subfolders = []

    def tr_section_http_request(self, project, section_id):
        URL = "https://testrail.dwos.com/index.php?/api/v2/get_cases/{}&section_id={}".format(project, section_id)
        self.rjson = requests.get(URL, headers=self.head, auth=(self.USER, self.PASSWORD)).json()

    def create_folder_list(self):
        for tc in self.rjson:
            self.subfolders.append("{} {}".format(str(tc["id"]), tc["title"][3:]))

    def create_subfolder(self, parent_folder):
        for subfolder in self.subfolders:
            os.mkdir(parent_folder + "/" + subfolder)

app = tk.Tk()
cont = ttk.Frame(app, padding=(3,3,10,10))
# app.title("Test Tkinter")
cont.columnconfigure(0, weight=1)
cont.columnconfigure(1, weight=20)
cont.columnconfigure(2, weight=1)
cont.columnconfigure(3, weight=1)
app.geometry('700x300')
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=20)
app.columnconfigure(3, weight=1)
Form(app, cont)
app.mainloop()
