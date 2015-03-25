# cat2.py
import sys


def main():
    arguments = sys.argv[1:]

    for argument in arguments:
        filename = argument
        f = open(filename, 'r')

        content = f.read()
        print(content)

        f.close()


if __name__ == '__main__':
    main()
