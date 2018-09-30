#coding:utf-8


class Personne:
    """
    Creation de personne
    """

    def __init__(self, prenom, nom, age):
        """
        Une personne
        :return:
        """
        self.prenom = prenom
        self.nom = nom
        self.age = age
        print("J'ai cree une personne")

    def introRequeteAge(function):
        print("Vous avez demandé l'age du personnage ? La voici")
        return function

    @introRequeteAge
    def afficheAge(self):

        if self.age <= 1:
            print("L'age de {} {} est {} an.".format(self.prenom, self.nom, self.age))

        else:
            print("L'age de {} {} est {} ans.".format(self.prenom, self.nom, self.age))

p = []

for i in range(15):
    p.append("per{}".format(i))

print(p)

for i in range(len(p)):
    age = i
    p[i] = Personne("Carufel", "Martin", age)
    p[i].afficheAge()



