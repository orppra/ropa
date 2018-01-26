import argparse
import sys
from . import start


def main():
    parser = argparse.ArgumentParser(description='Ropa - GUI based on Ropper')
    g = parser.add_mutually_exclusive_group()
    g.add_argument('-f', '--file', dest='file')
    g.add_argument('-l', '--load', dest='load')
    args = parser.parse_args()

    start(sys.argv, args.file, args.load)


if __name__ == "__main__":
    main()
