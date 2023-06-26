
try:
    with open("c:\\tmp\\tata.txt") as f:
            for line in f:
                print(line.strip())

except Exception as e:
    print(f"Erreur : {e}")
