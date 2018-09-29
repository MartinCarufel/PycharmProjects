# coding: utf-8


class Personne:
    """Classe definissant les personnes"""

    personne_creer = 0

    def __init__(self, nom, prenom, age):
        self._nom = nom
        self._prenom = prenom
        self._age = age

        Personne.personne_creer += 1

    def _get_nom(self):
        return self._nom

    def _set_nom(self, nom):
        print("Je set le nom:")
        self._nom = nom
        return self._nom

    nom = property(_get_nom, _set_nom)

    def _get_prenom(self):
        return self._prenom

    def _set_prenom(self, prenom):
        print("Je set le prenom:")
        self._prenom = prenom
        return self._prenom

    prenom = property(_get_prenom, _set_prenom)

    def _get_age(self):
        if self._age <= 1:
            return str(self._age) + " an"
        else:
            return str(self._age) + " ans"
    def _set_age(self, age):
        print("Je set l'age:")
        self._age = age
        return self._age

    age= property(_get_age, _set_age)


per1 = Personne("Carufel", "Martin", 42)
per2 = Personne("Ouellette", "Anne-Marie", 42)
per3 = Personne("Carufel", "Justin", 1)

print("La personne1 se nomme {} {} et elle a {}" .format(per1.prenom, per1.nom, per1.age))
print("La personne2 se nomme {} {} et elle a {}" .format(per2.prenom, per2.nom, per2.age))
print("La personne3 se nomme {} {} et elle a {}" .format(per3.prenom, per3.nom, per3.age))

per1.age = 78

print("La personne1 se nomme {} {} et elle a {}" .format(per1.prenom, per1.nom, per1.age))