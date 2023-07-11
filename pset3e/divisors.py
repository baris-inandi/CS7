"""
The proper divisors of an integer n are the positive divisors less than n. A positive
integer is said to be a deficient, perfect, or abundant number if the sum of its proper divisors
is less than, equal to, or greater than the number, respectively. For example,
 8 is deficient, because its proper divisors are 1, 2 and 4, and 1+2+4 < 8;
 6 is perfect, because 1+2+3 = 6;
12 is abundant, because 1+2+3+4+6 > 12.
Write a Python program that accepts two positive integer values that are input by the
user running the program (say m and n, where m <= n) and prints deficient, perfect or
abundant for each value between m and n inclusive. Your program must implement a
function
def divisors(n):
 …
The function must return (not print!) deficient, perfect or abundant for a given number.
You may want to Google for examples of perfect numbers to be sure your function is
behaving correctly. The output from your main program will look something like this:
Please input an integer value for m: 5
Now input an integer value for n that is greater than or equal to
5: 31
5 is deficient
6 is perfect
7 is deficient
"""

import math


def get_divisors(n) -> list[int]:
    # returns a list of divisors of n, except n
    out = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            out.append(i)
            a = n // i
            if i != a and a != n:
                out.append(a)
    return out


def divisors(n) -> str:
    d = get_divisors(n)
    if sum(d) < n:
        return "deficient"
    elif sum(d) > n:
        return "abundant"
    return "perfect"


def main():
    m = int(input("Please input an integer value for m: "))
    n = int(input(f"Now input an integer value for n >= {m}: "))
    for i in range(m, n + 1):
        print(f"{i} is {divisors(i)}")


if __name__ == "__main__":
    main()