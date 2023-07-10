from typing import Tuple


def ampm_to_military(h: int, m: int, s: int, a: str) -> Tuple[int, int, int]:
    if h == 12:
        h = 0
    if a == "P":
        h += 12
    return h, m, s


def fraction_of_day(h: int, m: int, s: int, a: str) -> float:
    h, m, s = ampm_to_military(h, m, s, a)
    return (h * 3600 + m * 60 + s) / 86400


def print_fraction_of_day(h: int, m: int, s: int, a: str) -> Tuple[str, float]:
    o1, o2 = f"{h}:{m:0>2} {'AM' if a == 'A' else 'PM'}", fraction_of_day(h, m, s, a)
    print(f"{o1:>8}\t{o2:.4f}")
    return o1, o2


def main():
    print(f"{'Time':>5}\t\tFraction Since Midnight")
    print_fraction_of_day(12, 0, 0, "A")
    for i in range(1, 12):
        print_fraction_of_day(i, 0, 0, "A")
    for i in range(1, 11):
        print_fraction_of_day(i, 0, 0, "P")


if __name__ == "__main__":
    main()
