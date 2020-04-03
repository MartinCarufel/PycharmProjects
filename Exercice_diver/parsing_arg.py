import argparse

parser = argparse.ArgumentParser(description='Test Arg Parse')
parser.add_argument("-add", nargs='*', metavar="num", type=int, dest='plus',
                    help="All the number separate by space wil be added")
parser.add_argument("-sub", nargs='*', metavar="num", type=int, dest='sous',
                    help="All the number separate by space wil be added")

args = parser.parse_args()

print(sum(args.plus) - sum(args.sous))

