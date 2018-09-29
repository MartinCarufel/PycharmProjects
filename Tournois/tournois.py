# coding: utf-8

from tkinter import *
from random import shuffle

class Players:
    """Class defining ... """

    def __init__(self):
        """Class constructor"""
        self.player_list = []

    def p_add(self, player_name):
        """This methode add new player"""
        #player_name = input("Entrer nom du joueur: ")
        self.player_list.append(player_name)

    def p_change_name(self, player_id):
        """this methode change the player name"""
        print("lose")

    def p_find(self, name):
        """Method that do something"""
        print("Method")

    def p_list(self):
        """This methode return a list all player"""
        return self.player_list

class Equipes:

    def __init__(self):
        self.liste_equipe = []

    def create_equipe(self, liste_joueurs):
        try:
            for i in range(0, len(liste_joueurs), 2):
                une_equipe = {"nom_equipe":"equipe"+str(i//2), "equipiers":liste_joueurs[i] + " et " + liste_joueurs[i+1], "serie":""}
                self.liste_equipe.append(une_equipe)

        except IndexError:
            print("Il manque un joueur")

    def set_equipe_serie(self, rech_equipe):
        print("Je cherche l'equipe: {}" .format(rech_equipe))
        for i, val in enumerate(self.liste_equipe):
            if val['nom_equipe'] == rech_equipe:
                new_serie = input("Entrer la serie de l'equipe {}" .format(rech_equipe))
                self.liste_equipe[i] = {"nom_equipe":val["nom_equipe"], "equipiers":val["equipiers"], "serie":new_serie}
            print(i, val)
# class App(Frame):
#     def __init__(self, **kwargs):
#         Frame.__init__(self, )

s_equipe = Equipes()

player_list1 = Players()
une_liste = ["Martin", "Anne-Marie", "Justin", "Gabriel"]
#une_liste = ["Martin", "Anne-Marie", "Justin"]

for i in une_liste:
    player_list1.p_add(i)



result = list(player_list1.player_list)

shuffle(result)

s_equipe.create_equipe(une_liste)

print(s_equipe.liste_equipe[:])

s_equipe.set_equipe_serie("equipe0")
s_equipe.set_equipe_serie("equipe1")

print(s_equipe.liste_equipe[:])

# button1 = Button(main_app, text="Entrer un joueur", command=player_list1.player_add)
# button1.pack()
# main_app.mainloop()
# main_app.destroy()
