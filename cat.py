import sys


def main():
    filename = "file.txt"
    f = open(filename, 'r')
    content = f.read()

    print (content)

    f.close()


if __name__ == '__main__':
    main()
