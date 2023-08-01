def C(n, k) -> int:
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    return C(n - 1, k - 1) + C(n - 1, k)


def print_pascal_triangle(rows):
    for n in range(rows):
        for k in range(n + 1):
            print(f"{C(n, k):<4}", end=" ")
        print()


def main():
    print_pascal_triangle(8)


if __name__ == "__main__":
    main()
