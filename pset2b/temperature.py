def f_to_k(f: float) -> float:
    return ((5 / 9) * (f - 32)) + 273.16


def main():
    f = float(input("Input a Fahrenheit temperature to be converted: "))
    k = f_to_k(f)
    print(f"{f} degrees Fahrenheit equals {k} degrees Kelvin")


if __name__ == "__main__":
    main()
