import sys
from random import randint


def main():
    arguments = sys.argv[1:]
    index = int(arguments[1])

    filename = arguments[0]
    f = open(filename, "w")

    while index > 0:
        f.write(str(randint(1, 1000)))
        f.write(" ")
        index -= 1

    f.close()


if __name__ == '__main__':
    main()
