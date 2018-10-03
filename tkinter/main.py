#coding:utf-8


import tkinter

mainapp = tkinter.Tk()
mainapp.title("Test titre")
# mainapp.minsize(640, 480)
# mainapp.geometry("800x600")
# # mainapp.resizable(width=False, height=False)    #interdire redim
# mainapp.positionfrom("user")
# mainapp.geometry("800x600+20+20")    #positionne la fenêtre de geometrie X par Y a 20,20  (x,y)

#centrer fenetre




screen_x = mainapp.winfo_screenwidth()
screen_y = mainapp.winfo_screenheight()
window_x = 800
window_y = 600
pos_x = (screen_x // 2) - (window_x // 2)
pos_y = (screen_y // 2) - (window_y // 2)
geo = "{}x{}+{}+{}".format(window_x, window_y, pos_x, pos_y)
mainapp.geometry(geo)

message = tkinter.Label(mainapp, text="Bonjour")
message.pack()

bouton = tkinter.Button(mainapp, text="OK", padx=90, pady=30, command=mainapp.quit)
bouton.pack()



mainapp.mainloop()