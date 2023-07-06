# end dates of all signs
signs = {
    "Aries": (4, 19),
    "Taurus": (5, 20),
    "Gemini": (6, 20),
    "Cancer": (7, 22),
    "Leo": (8, 22),
    "Virgo": (9, 22),
    "Libra": (10, 22),
    "Scorpio": (11, 21),
    "Sagittarius": (12, 21),
    "Capricorn": (1, 19),
    "Aquarius": (2, 18),
    "Pisces": (3, 20),
}


def before(month1: int, day1: int, month2: int, day2: int) -> bool:
    # returns true if first date is before or equal to second date
    if month1 == month2 and day1 == day2:
        return True
    if month1 < month2:
        return True
    if month1 == month2:
        return day1 < day2
    return False


def sign(month: int, day: int) -> str:
    for s in signs:
        if before(month, day, *signs[s]):
            return s
    return "INVALID_DATE"


def main():
    month = int(input("Enter your birth month: "))
    day = int(input("Enter your birth day: "))
    print(sign(month, day))


if __name__ == "__main__":
    main()
