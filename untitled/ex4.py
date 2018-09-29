# coding: utf-8
import math

liste = [445, 55, 52, 48, 305, 51, 49, 54, 298, 54, 50]

for i in range(len(liste)-1):
    for j in range(i+1, len(liste)-2, 1):
        #print("test {} contre {}" .format(liste[i], liste[j]))
        if math.isclose(liste[i], liste[j], abs_tol=10):
            print("La liste contient deux nombre proche, {} et {}" .format(liste[i], liste[j]))



class Myclass:
    """Class defining ... """

    def __init__(self, param1):
        """Class constructor"""
        self.param1 = param1

    def method(self):
        """Method that do something"""
        print("Method")