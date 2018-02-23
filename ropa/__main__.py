import argparse
import sys
from . import start


def main():
    parser = argparse.ArgumentParser(description='Ropa - GUI based on Ropper')
    parser.add_argument('file', nargs='?')
    args = parser.parse_args()

    start(sys.argv, args.file)


if __name__ == "__main__":
    main()
