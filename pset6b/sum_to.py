def sum_to(n):
    if n <= 1:
        return 1
    return 1 / n + sum_to(n - 1)


def main():
    print("Sum to 2:", sum_to(2))
    print("Sum to 5:", sum_to(5))
    print("Sum to 10:", sum_to(100))


if __name__ == "__main__":
    main()
