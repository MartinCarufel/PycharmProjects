import yaml
from argparse import ArgumentParser

class Argument_yaml():

    def __init__(self):

        self.arg_data = None
        parser = ArgumentParser()
        parser.add_argument("-f", "--file", help="File name and location", )
        self.args = parser.parse_args()
        self.__read_yaml__()



    def __read_yaml__(self):
        with open(self.args.file, 'r') as f:
            self.arg_data = yaml.safe_load(f)


def main():
    o = Argument_yaml()



if __name__ == "__main__":
    main()