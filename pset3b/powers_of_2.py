"""
Write a function named print_powers_of_2 that accepts an integer >= 0 and
prints each power of 2 from 2^0 (which is equal to 1) up to that maximum power, inclusive.
For example, print_powers_of_2(10) should print
 1 2 4 8 16 32 64 128 256 512 1024
"""


def print_powers_of_2(n):
    m = 1
    for _ in range(n + 1):
        print(m, end=" ")
        m *= 2
    print()


def main():
    print_powers_of_2(10)


if __name__ == "__main__":
    main()
