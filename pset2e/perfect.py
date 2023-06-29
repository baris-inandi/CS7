import math


def divisors(n) -> list[int]:
    # returns a list of divisors of n, except n
    out = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            out.append(i)
            a = n // i
            if i != a and a != n:
                out.append(a)
    return out


def is_perfect(n: int) -> bool:
    return sum(divisors(n)) == n


def main():
    u = int(input("Enter a number: "))
    for i in range(1, u + 1):
        if is_perfect(i):
            print(i)


if __name__ == "__main__":
    main()
