import random
from sys import argv


def main():
    if len(argv) != 3:
        print("Usage: python roulette.py [input_file] [n]")
        exit(1)
    input_file = argv[1]
    n = int(argv[2])
    with open(input_file, "w+") as f:
        out = ""
        for _ in range(int(n)):
            out += str(random.randint(0, 36)) + "\n"
        f.write(out[:-1])


if __name__ == "__main__":
    main()
