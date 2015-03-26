import sys


def main():
    filename = sys.argv[1]

    f = open(filename, 'r')

    content = f.read()

    numbers = content.split()

    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])

    print (sum(numbers))


if __name__ == '__main__':
    main()
