#coding:utf-8

import os
import tkinter.filedialog
conjoint = ["IGA", "METRO", "BELL CANADA", "RENO DEPOT", "RONA", "NETFLIX.COM", "LE LUNCH", "MICROSOFT"]
martin_anne = ["HARVEYS", "JUMBO RESTAURANT", "VIRGIN MOBILE", "ULTRAMAR", "SUBWAY", "MCDONALD", "DOMINOS", "CHEZ GERARD",
               "AU COQ", "SCORES", "BARBIES", "RTM - ABONNEMENT", "A&W", "PACINI", 'LES DELICES', "NICKELS", "SHELL",
               "PETRO", "Baila Prod", "WENDY", "JULIANO", "MEGAPLEX", "AMIR", "MIKE'S"]


path = tkinter.filedialog.askopenfilename()

saveFile = tkinter.filedialog.asksaveasfilename()
outputFile = open(saveFile, "w")


with open(path) as f:
    content = f.readline()
    content = content.strip('"",""\n')
    while content:
        #print(content)
        found = False

        for i in martin_anne:
            if i in content:
                if "4540330755072014" in content:
                    outputFile.write(content + ",m," + '\n')
                    #print("Depense Martin")
                    found = True
                if "4540330755072022" in content:
                    outputFile.write(content + ",a," + '\n')
                    #print("Depense Anne-Marie")
                    found = True
                #break
            else:
                pass
        for i in conjoint:
            if i in content:
                outputFile.write(content + ",c," + '\n')
                #print("Depense Conjoint")
                found = True
                #break
            #else:
                #pass
        if not found:
            lineToList = content.split(",")
            #print(lineToList)
            if lineToList[0] == 'VISA 4540330755072014"':
                print("Carte: {} - Martin - {} - {} - {} " .format(lineToList[0],lineToList[3],lineToList[5],lineToList[11]))
                choice = input("Choix: (m, a, c ) ? ")
                outputFile.write(content + "," + choice + '\n')
            elif lineToList[0] == 'VISA 4540330755072022"':
                print("Carte: {} - Anne-Marie - {} - {} - {} " .format(lineToList[0],lineToList[3],lineToList[5],lineToList[11]))
                choice = input("Choix: (m, a, c ) ? ")
                outputFile.write(content + "," + choice + '\n')
            else:
                print("else")
                outputFile.write(content + ","'\n')
                pass
        content = f.readline()
        content = content.strip('"",""\n')
