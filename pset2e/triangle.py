def triangle(rows: int):
    s = 0
    for i in range(1, rows + 1):
        h = i * 100
        for j in range(i):
            print(h + (j * s), end=" ")
        s += 2
        print()


def main():
    triangle(9)


if __name__ == "__main__":
    main()
