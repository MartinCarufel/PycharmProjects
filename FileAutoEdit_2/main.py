#coding:utf-8

from tkinter import *
from time import sleep
import os
import shutil
import tkinter.filedialog
import csv
conjoint = ["IGA", "METRO", "BELL CANADA", "RENO DEPOT", "RONA", "NETFLIX.COM", "LE LUNCH", "MICROSOFT"]
martin_anne = ["HARVEYS", "JUMBO RESTAURANT", "VIRGIN MOBILE", "ULTRAMAR", "SUBWAY", "MCDONALD", "DOMINOS", "CHEZ GERARD",
               "AU COQ", "SCORES", "BARBIES", "RTM - ABONNEMENT", "A&W", "PACINI", 'LES DELICES', "NICKELS", "SHELL",
               "PETRO", "Baila Prod", "WENDY", "JULIANO", "MEGAPLEX", "AMIR", "MIKE'S"]


#inputFile = tkinter.filedialog.askopenfilename()
inputFile = "conciliation_20180924.csv"

#saveFile = tkinter.filedialog.asksaveasfilename()
saveFile = "conciliation_20180924_mod.csv"
outputFile = open(saveFile, "w")

listTag = ['no_carte', 'date', 'achat', 'debit', 'credit', 'total', 'compte']

feuille = []
xdict = {}
j = 0
line2 = []


def compte_pour(content):
    #print(content)
    found = False
    for i in martin_anne:
        if i in content[2]:
            if "4540330755072014" in content[0]:
                content.append('m')
                #print(content)
                #outputFile.write(content + ",m," + '\n')
                #print("Depense Martin")
                found = True
            if "4540330755072022" in content[0]:
                content.append('a')
                #outputFile.write(content + ",a," + '\n')
                # print("Depense Anne-Marie")
                found = True
            # break
        else:
            pass
    for i in conjoint:
        if i in content[2]:
            content.append('c')
            #outputFile.write(content + ",c," + '\n')
            # print("Depense Conjoint")
            found = True
            # break
        # else:
        # pass
    if not found:
        content.append('n')
        # lineToList = content.split(",")
        # # print(lineToList)
        # if lineToList[0] == 'VISA 4540330755072014"':
        #     print("Carte: {} - Martin - {} - {} - {} ".format(lineToList[0], lineToList[3], lineToList[5],
        #                                                       lineToList[11]))
        #     choice = input("Choix: (m, a, c ) ? ")
        #     outputFile.write(content + "," + choice + '\n')
        # elif lineToList[0] == 'VISA 4540330755072022"':
        #     print("Carte: {} - Anne-Marie - {} - {} - {} ".format(lineToList[0], lineToList[3], lineToList[5],
        #                                                           lineToList[11]))
        #     choice = input("Choix: (m, a, c ) ? ")
        #     outputFile.write(content + "," + choice + '\n')
        # else:
        #     print("else")
        #     outputFile.write(content + ","'\n')
        #     pass
    #print(content)
    return content



with open(inputFile, 'r') as f, open('output.csv', 'w') as fo:
    for line in f:
        line = line.replace('"', '').replace("'", "").split(',')
        lineOut = line[0] + ',' + line[3] + ',' + line[5] + ',' + line[10] + ',' + line[11] + ','
        line2 = lineOut.split(',')
        line2 = compte_pour(line2)
        #print(lineOut)

        #fo.write(lineOut)
        for i in range(len(listTag)):
            #print(line2)
            xdict[listTag[i]] = line2[i]
            #print(xdict)

        print(xdict)
        feuille.append(xdict.copy())

root = Tk()

var = StringVar()
vCarte  = StringVar()
vDate   = StringVar()
vAchat  = StringVar()
vDebit  = StringVar()
vCredit = StringVar()
vTotal  = StringVar()
vcompte = StringVar()


lCarte = Label(root, textvariable=vCarte)
lDate =  Label(root, textvariable=vDate)
lAchat = Label(root, textvariable=vAchat)
lDebit = Label(root, textvariable=vDebit)
lCredit = Label(root, textvariable=vCredit)
lTotal = Label(root, textvariable=vTotal)
lcompte = Label(root, textvariable=vcompte)
label_radio = Label(root)


def sel():
    selection = var.get()
    label_radio.config(text = selection)


def affiche_radio_button(compte):
    R1 = Radiobutton(root, text="Martin", variable=var, value='m', command=sel)
    R1.grid(column=2, columnspan=4, row=2)

    R2 = Radiobutton(root, text="Anne-Marie", variable=var, value='a', command=sel)
    R2.grid(column=2, columnspan=4, row=3)

    R3 = Radiobutton(root, text="Conjoint", variable=var, value='c', command=sel)
    R3.grid(column=2, columnspan=4, row=4)

    R4 = Radiobutton(root, text="deux", variable=var, value='d', command=sel)
    R4.grid(column=2, columnspan=4, row=5)

    R5 = Radiobutton(root, text="non selectionner", variable=var, value='n', command=sel)
    R5.grid(column=2, columnspan=4, row=6)


j=0
for i in feuille:
    var = tkinter.StringVar(None, i['compte'])
    vCarte.set(i['no_carte'])
    vDate.set(i['date'])
    vAchat.set(i['achat'])
    vDebit.set(i['debit'])
    vCredit.set(i['credit'])
    vTotal.set(i['total'])
    vcompte.set(i['compte'])
    lCarte.grid(column=0, row=j)
    lDate.grid(column=1, row=j)
    lAchat.grid(column=2, row=j)
    lDebit.grid(column=3, row=j)
    lCredit.grid(column=4, row=j)
    lTotal.grid(column=5, row=j)
    lcompte.grid(column=6, row=j)
    affiche_radio_button(i['compte'])
    but = Button(root, text='Send')
    but.grid(column=2, columnspan=4, row=7)
    but.wait_variable(var)

    root.update_idletasks()
    j += 1
    sleep(.2)

#
# j=0
# for i in feuille:
#     lCarte = Label(root, text=i['no_carte'])
#     lDate = Label(root, text=i['date'])
#     lAchat = Label(root, text=i['achat'])
#     lDebit = Label(root, text=i['debit'])
#     lCredit = Label(root, text=i['credit'])
#     lTotal = Label(root, text=i['total'])
#     lCarte.grid(column=0, row=j)
#     lDate.grid(column=1, row=j)
#     lAchat.grid(column=2, row=j)
#     lDebit.grid(column=3, row=j)
#     lCredit.grid(column=4, row=j)
#     lTotal.grid(column=5, row=j)
#     root.update_idletasks()
#     j += 1
#     sleep(.1)


#root.mainloop()
