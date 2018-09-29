#coding:utf-8

import re


liste = ["Martin C.", "Anne-Marie", "Justin", "Gabriel", "Martin J.", "Claude", "Diane B.", "Luc", "Eric", "Janie", "Benjamin", "Émiliie", "Diane B."]
nb_count = 0

find_name = input("Quel nom voulez-vous rechercher ?\n\t-> ")

search_exp = find_name.lower() + ".*"

regex = re.compile(search_exp)
for idx, value in enumerate(liste):
    result = regex.search(value.lower())
    if result is not None:
        nb_count += 1
        print("La position du nom {} est : {}".format(find_name, idx))
        print("Le nom trouvé est : {}".format(value))

if nb_count > 1:
    print("Il a plusieurs {} dans la liste" .format(find_name))
print (nb_count)