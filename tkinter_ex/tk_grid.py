import tkinter as tk

class App_grid(tk.Tk):
    def __init__(self):
        super().__init__()
        self.columnconfigure(0, minsize=200, )
        self.rowconfigure(1, minsize=50)

        self.row0_col0 = tk.Label(self, text="Martin Carufel", bd=8, relief="ridge")
        self.row0_col0.grid(column=0, row=0)
        self.row0_col1 = tk.Label(self, text="Martin Carufel", width=20, bg="#8800e0", justify='left',
                                  anchor='w', bd=8, fg="#FFFFFF", relief="groove", wraplength=50)
        self.row0_col1.grid(column=1, row=0, sticky=tk.W)
        self.row0_col2 = tk.Label(self, text="Martin Carufel", bd=3, relief="solid")
        self.row0_col2.grid(column=2, row=0)

        self.row1_col0 = tk.Label(self, text="Martin Carufel")
        self.row1_col0.grid(column=0, row=1)
        self.row1_col1 = tk.Label(self, text="M")
        self.row1_col1.grid(column=1, row=1)
        self.row1_col2 = tk.Label(self, text="Martin Carufel")
        self.row1_col2.grid(column=2, row=1)

        self.row2_col0 = tk.Label(self, text="Martin Carufel")
        self.row2_col0.grid(column=0, row=2)
        self.row2_col1 = tk.Label(self, text="M")
        self.row2_col1.grid(column=1, row=2)
        self.row2_col2 = tk.Label(self, text="Martin Carufel")
        self.row2_col2.grid(column=2, row=2)

        self.my_spinbox = tk.Spinbox(from_=0, to=105, value=[x for x in range(0, 105, 5)], state="readonly", wrap=True)
        self.my_spinbox.grid(column=0, row=3, )

        self.frame1 = tk.Frame(width=500, height=500, bd=3, relief="solid")
        self.frame1.grid(column=0, row=4, padx=10, pady=10)

        self.frame1.pack_propagate(False)
        self.field1 = tk.Entry(self.frame1)
        self.field1.pack(padx= 10, pady=10, side="bottom", anchor="w")
        self.mainmenu = tk.Menu(self.frame1)
        self.submenu_1 = tk.Menu(self.mainmenu, tearoff=0)
        self.submenu_1.add_checkbutton(label="sub menu 1")
        self.submenu_1.add_checkbutton(label="sub menu 2")
        self.mainmenu.add_cascade(label="Menu 1", menu=self.submenu_1)

        self.config(menu=self.mainmenu)




def main():
    app = App_grid()
    app.mainloop()

if __name__ =="__main__":
    main()