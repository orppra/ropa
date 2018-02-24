import argparse
import sys

from ropa.gui import App


def start(args, file=None, load=None):
    app_name = 'ropa'

    w = App(app_name, args, file)

    w.show()
    w.quit()


def main():
    parser = argparse.ArgumentParser(description='Ropa - GUI based on Ropper')
    parser.add_argument('file', nargs='?')
    args = parser.parse_args()

    start(sys.argv, args.file)


if __name__ == "__main__":
    main()
