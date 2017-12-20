import sys
from . import start


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    start(args)


if __name__ == "__main__":
    main()
