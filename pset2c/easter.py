def easter(y: int) -> tuple[int, int]:
    # 1. Let y be the year (such as 1800 or 2001 or whatever)
    # 2. Divide y by 19 and call the remainder a. Ignore the quotient.
    a = y % 19
    # 3. Divide y by 100 to get a quotient b and a remainder c.
    b, c = y // 100, y % 100
    # 4. Divide b by 4 to get a quotient d and a remainder e.
    d, e = b // 4, b % 4
    # 5. Divide 8 * b +13 by the value 25, to get a quotient g. Ignore the remainder.
    g = (8 * b + 13) // 25
    # 6. Divide 19 * a + b - d - g + 15 by the value 30, to get a remainder h. Ignore the quotient.
    h = (19 * a + b - d - g + 15) % 30
    # 7. Divide c by 4 to get a quotient j, and a remainder k.
    j, k = c // 4, c % 4
    # 8. Divide (a + 11*h) by the value 319, to get a quotient m. Ignore the remainder.
    m = (a + 11 * h) // 319
    # 9. Divide 2 * e + 2 * j - k - h + m + 32 by the value 7 to get a remainder r. Ignore the quotient.
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    # 10. Divide h - m + r + 90 by the value 25, to get a quotient n. Ignore the remainder.
    n = (h - m + r + 90) // 25
    # 11. Divide h - m + r + n + 19 by the value 32, to get a remainder p. Ignore the quotient.
    p = (h - m + r + n + 19) % 32
    # Then Easter falls on day p of month n.
    return (n, p)


def main():
    y = int(input("Enter a year: "))
    e = easter(y)
    print(f"{e[0]}/{e[1]}")


if __name__ == "__main__":
    main()
