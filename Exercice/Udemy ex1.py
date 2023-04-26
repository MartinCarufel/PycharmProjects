def conv_to_inch(nb):
    print("{} pouces".format(nb / 2.54))

def conv_to_cm(nb):
    print("{} cm".format(nb*2.54))

def ask_choice():
    print("Quel conversion voulez vous faire ?")
    print("Pour convertir des pouce en cm entrer: a")
    print("Pour convertir des cm en pouce entrer: b")

    while True:
        reponse = input("Quel est votre choix: ").upper()
        if reponse in ["A", "B"]:
            break
        print("Repondre par la lettre A ou B")
    return reponse

choix = ask_choice()
while True:

    try:
        valeur = float(input("Entrer la valeur a convertir: "))
    except:
        print("Convertion impossible")
    if choix == "A":
        conv_to_cm(valeur)
    elif choix == "B":
        conv_to_inch(valeur)

    quitter = input("Voulez vous quitter (Q) ? ").upper()
    if quitter == "Q":
        break





