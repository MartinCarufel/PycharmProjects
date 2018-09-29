#coding:utf-8
import tkinter
import sys

mainapp = tkinter.Tk()
mainapp.title("Test titre")

def say_hello():
    #keyPress = input("press a key")
    message = tkinter.Label(mainapp, text="Bonjour")
    message.pack()
    bouton = tkinter.Button(mainapp, text="OK", padx=90, pady=30, command=mainapp.quit)
    bouton.pack()
    mainapp.mainloop()
    #print("Hello world {}".format(keyPress))

def say_bye():
    sys.stderr.write('\nBye, Bye\n')     #il faut utiliser le sys pour printer dans la console
    #print("Bye Bye everyone")     Ceci ne fonctionne lorsqu<appeler par robot framework

