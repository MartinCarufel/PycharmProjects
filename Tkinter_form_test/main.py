import tkinter as tk
from tkinter import filedialog

from tkinter import filedialog
import os
import requests
import json

class Form:
    def __init__(self):
        self.dir_path = ""
        self.project_id = ""
        self.section_id = ""
        self.root = tk.Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=20)
        self.root.columnconfigure(3, weight=1)
        self.dir_var = tk.StringVar()
        self.project_var = tk.StringVar()
        self.project_var.set("2")
        self.section_var = tk.StringVar()

        self.root.title("Test Tkinter")
        self.root.geometry('700x300')
        self.dir_lbl = tk.Label(self.root, text="Parent folder")
        self.dir_lbl.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.dir_entry = tk.Entry(self.root, textvariable=self.dir_var)
        self.dir_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)
        self.browse = tk.Button(self.root, text="Browse", command= self.browse, width=10)
        self.browse.grid(column=2, row=0, sticky=tk.EW, padx=5, pady=5)

        self.project_lbl = tk.Label(self.root, text="Project")
        self.project_lbl.grid(column=0, row=1, padx=5, pady=5)
        self.project_entry = tk.Entry(self.root, textvariable=self.project_var)
        self.project_entry.grid(column=1, row=1, padx=5, pady=5, sticky=tk.W)
        self.section_lbl = tk.Label(self.root, text="Section")
        self.section_lbl.grid(column=0, row=2, padx=5, pady=5)
        self.section_entry = tk.Entry(self.root, textvariable=self.section_var)
        self.section_entry.grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)
        self.submit = tk.Button(self.root, text="Run", command=self.submit, width=8)
        self.submit.grid(column=0, row=3, padx=5, pady=5)
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy, width=12)
        self.exit_button.grid(column=1, row=3,)




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

        pass

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


app = Form()
app.root.mainloop()
