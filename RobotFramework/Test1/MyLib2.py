#coding:utf-8
import tkinter
import sys

mainapp = tkinter.Tk()
mainapp.title("Test titre")

choix = "vide"

def yes():
    choix = "yes"
    return "yes"
    mainapp.destroy()

def no():
    choix = "no"
    return "no"
    mainapp.destroy()


def say_hello():
    #keyPress = input("press a key")
    message = tkinter.Label(mainapp, text="Bonjour")
    message.pack()
    bouton = tkinter.Button(mainapp, text="YES", padx=90, pady=30, command=yes)
    bouton.pack()
    bouton = tkinter.Button(mainapp, text="NO", padx=90, pady=30, command=no)
    bouton.pack()
    mainapp.mainloop()
    #print("Hello world {}".format(keyPress))
    return choix


def say_bye():
    sys.stderr.write('\nBye, Bye\n')     #il faut utiliser le sys pour printer dans la console
    #print("Bye Bye everyone")     Ceci ne fonctionne lorsqu<appeler par robot framework

def yes():
    global choix
    choix = "yes"
    #print(choix)
    mainapp.destroy()
    #return choix

def no():
    global choix
    choix = "no"
    mainapp.destroy()
    #print(choix)
    #return choix


#monchoix = say_hello()
#print(monchoix)

