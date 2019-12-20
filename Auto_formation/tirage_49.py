#coding:utf-8
import random

class Loto():
    def __init__(self, number):
        self.number = number
        self.boulier = []
        self.createBoulier()
        self.remettre_la_boulre = False

    def pickValue(self):
        end = len(self.boulier)
        # print('Numbre de boule restante: {}' .format(len(self.boulier)))
        index = random.randint(0, end-1)
        draw = self.boulier[index]
        if not self.remettre_la_boulre:
            self.boulier.remove(draw)

        # print(pickBag[index])
        return (draw, self.boulier)

    def tirage(self, boule_tirer, remettre_la_boule):
        le_tirage = []
        self.remettre_la_boulre = remettre_la_boule
        for i in range(boule_tirer):
            result = self.pickValue()
            le_tirage.append(result[0])
            self.boulier = result[1]
        return le_tirage



    def createBoulier(self):
        self.boulier = []

        for i in range(1, self.number+1):
            self.boulier.append(i)
        return self.boulier

result = []
l1 = Loto(49)
l1.createBoulier()
for i in range(20):
    result.append(l1.tirage(6, True))
for i in range(len(result)):
    print(result[i])

l2 = Loto(10)
result = l2.tirage(10, False)
print(result)

# boulier = createBoulier(49)
# print(boulier)

# test = pickValue(boulier)
# print(test[0])
# print(test[1])
# tirage = []
# for i in range(7):
#
#     result = pickValue(boulier)
#     tirage.append(result[0])
#     boulier = result[1]
# print(tirage)
#     # print(result[1])