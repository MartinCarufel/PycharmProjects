
def func1():
    print("function 1")


def func2():
    print("function 2")


def func3():
    print("function 3")

def switcher(choix):
    switch = {
        1: func1,
        2: func2,
        3: func3
             }
    x = switch.get(choix, lambda: "Invalid")
    return x()


z = None
while True:
    z = input('Faite votre choix: ')
    if z == 'q':
        break
    switcher(z)

