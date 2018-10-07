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

listTag = ['no_carte', 'date', 'achat', 'debit', 'credit', 'total']

feuille = []
xdict = {}
j = 0
line2 = []
with open(inputFile, 'r') as f, open('output.csv', 'w') as fo:
    for line in f:
        line = line.replace('"', '').replace("'", "").split(',')
        lineOut = line[0] + ',' + line[3] + ',' + line[5] + ',' + line[10] + ',' + line[11] + ',' + line[12] + ',' + line[13]
        line2 = lineOut.split(',')
        fo.write(lineOut)
        for i in range(len(listTag)):
            xdict[listTag[i]] = line2[i]
            #print(xdict)

        #print(xdict)
        feuille.append(xdict.copy())

print(feuille[i]['no_carte'])
print(type(feuille[i]['no_carte']))



root = Tk()
var = StringVar()
var.set('hello')

vCarte  = StringVar()
vDate   = StringVar()
vAchat  = StringVar()
vDebit  = StringVar()
vCredit = StringVar()
vTotal  = StringVar()

Label(root, textvariable = var)


lCarte = Label(root, textvariable=vCarte)
lDate =  Label(root, textvariable=vDate)
lAchat = Label(root, textvariable=vAchat)
lDebit = Label(root, textvariable=vDebit)
lCredit = Label(root, textvariable=vCredit)
lTotal = Label(root, textvariable=vTotal)


for i in feuille:
    vCarte.set(i['no_carte'])
    vDate.set(i['date'])
    vAchat.set(i['achat'])
    vDebit.set(i['debit'])
    vCredit.set(i['credit'])
    vTotal.set(i['total'])
    lCarte.grid(column=0, row=0)
    lDate.grid(column=1, row=0)
    lAchat.grid(column=2, row=0)
    lDebit.grid(column=3, row=0)
    lCredit.grid(column=4, row=0)
    lTotal.grid(column=5, row=0)
    root.update_idletasks()

    sleep(1)


