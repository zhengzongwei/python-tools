import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", action="store", help="show output")

args = parser.parse_args()

if args.output():
    print("This is some output")
