import sys


def main():
    args = sys.argv[1:]
    print(sum([int(arg) for arg in args]))


if __name__ == "__main__":
    main()
