def digit_sum(n):
    if n < 10:
        return n
    else:
        return digit_sum(n // 10) + n % 10


def main():
    print(digit_sum(3456))


if __name__ == "__main__":
    main()
