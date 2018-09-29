from tkinter import *


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.a()

    def a(self):
        self.call_button = Button(self, text = "Call", command=self.b)
        self.call_button.grid(row=5, column=5) # This is fixing your issue

    def b(self):
        self.call_button.destroy()

root = Tk()

but = Button(text="allo", command= lambda: App.b(app))
but.grid(row=1, column=1)
app = App(master=root)
app.mainloop()