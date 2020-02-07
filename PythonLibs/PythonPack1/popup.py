import tkinter



def create_popup(msg):
    popup = tkinter.Tk()
    screenX = popup.winfo_screenwidth()
    screenY = popup.winfo_screenheight()

    print(screenX, 'x', screenY)
    popup.wm_title('Info')
    popup.minsize(width=180, height=80)
    popup.update()

    label = tkinter.Label(popup, text=msg)
    label.pack()
    b1 = tkinter.Button(popup, text='OK', command=popup.destroy, bg='#ff00ad008000')
    b1.pack(pady=16, ipadx=15, )
    popup.update()
    popupX = popup.winfo_width()
    popupY = popup.winfo_height()
    print(popupX, 'x', popupY)
    xpos = int((screenX-popupX)/2)
    ypos = int((screenY - popupY) / 2)
    popup.geometry('+{}+{}'.format(xpos-5, ypos+14))
    popup.mainloop()
