# coding: utf-8

class Test:
    """"""

    def __init__(self, **kwags):
        """Constructor for Test"""
        self.param = kwags



def main():
    print("allo")
    t1 = Test(nom="Martin", age=45)
    print(t1.param["nom"])

if __name__ == '__main__':
    main()
