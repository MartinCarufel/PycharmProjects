class Personne:

    def __init__(self):
        self._age = 0
        self._nom = ""


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        self._age = a

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def age(self, nom):
        self._nom = nom

