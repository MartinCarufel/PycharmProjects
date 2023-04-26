import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")

        self.l = tk.Label(self, text="button")
        self.l.pack(side=tk.TOP, fill=tk.X)
        self.l.bind_all("a", self.activate)
    def activate(self, event):
        print(event)
        print("button action from bind {} at {}, {}".format(event.char, event.x, event.y))

if __name__ == "__main__":
    app = Root()
    app.mainloop()
