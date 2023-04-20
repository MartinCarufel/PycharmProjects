import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, text="Hello World", padx=10, pady=20)
        self.label.pack()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Root()
    root.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
