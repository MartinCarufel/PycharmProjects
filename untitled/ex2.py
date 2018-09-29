# coding: utf-8


class Personne:
    """Classe definissant les personnes"""

    personne_creer = 0

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __repr__(self):
        return "Personne: nom({}), prénom({}), âge({})".format(self.nom, self.prenom, self.age)

    def __getattr__(self, val):
        print("Affiche l'attribut {} de l'objet" .format(val))

    def __setattr__(self, key, value):
        print("On change la veuleur de l'attribut {} par {}." .format(key, value))
        dict.__setattr__(self, key, value)


        Personne.personne_creer += 1

per1 = Personne("Carufel", "Martin", 42)
per2 = Personne("Ouellette", "Anne-Marie", 42)
per3 = Personne("Carufel", "Justin", 1)

print("La personne1 se nomme {} {} et elle a {}" .format(per1.prenom, per1.nom, per1.age))
print("La personne2 se nomme {} {} et elle a {}" .format(per2.prenom, per2.nom, per2.age))
print("La personne3 se nomme {} {} et elle a {}" .format(per3.prenom, per3.nom, per3.age))

per1.age = 78

print("La personne1 se nomme {} {} et elle a {}" .format(per1.prenom, per1.nom, per1.age))

