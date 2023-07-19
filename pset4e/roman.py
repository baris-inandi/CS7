ROMAN_NUMERALS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def iter_roman(roman_numeral):
    for i in range(len(roman_numeral) - 1):
        current = ROMAN_NUMERALS[roman_numeral[i]]
        next_ = ROMAN_NUMERALS[roman_numeral[i + 1]]
        yield (current, next_)


def to_arabic(roman_numeral):
    """Takes a valid roman numeral and returns an integer that is
    the corresponding the decimal number"""
    if not is_valid(roman_numeral):
        raise ValueError("Invalid roman numeral")
    result = 0
    for (current, next_) in iter_roman(roman_numeral):
        result += current * (1 if current >= next_ else -1)
    result += ROMAN_NUMERALS[roman_numeral[-1]]
    return result


def is_valid(roman_numeral):
    """Bonus EC problem: takes a roman numeral and returns a boolean
    that is True if the numeral is valid and False if it is not"""
    # if the string is empty, it is not valid
    if not roman_numeral:
        return False
    # all characters must be roman numerals
    for i in roman_numeral:
        if i not in ROMAN_NUMERALS:
            return False
    # if there is only one character, it is always valid
    if len(roman_numeral) == 1:
        return True
    # if length != 2, the first must never be smaller than the second
    if len(roman_numeral) != 2 and (
        ROMAN_NUMERALS[roman_numeral[0]] < ROMAN_NUMERALS[roman_numeral[1]]
    ):
        return False
    count = 1
    for (c, n) in iter_roman(roman_numeral):
        # subtraction rules:
        if n > c and (
            # only subtract one number from another
            (count > 1)
            # cannot subtract a number that is twice as big (e.g. )
            or (n - c == c)
            # cannot subtract a number from one that is more than 10 times greater (e.g. 99 is XCIX, not IC)
            or (n / c > 10)
        ):
            return False
        if c == n:
            count += 1
            if count > 3:
                return False
        else:
            count = 1
    return True


def print_valid_test_cases(test_case, expected):
    print(
        f"{test_case:<13} {to_arabic(test_case):<8} {expected:<8} {is_valid(test_case)}"
    )


def print_invalid_test_cases(test_case):
    print(f"{test_case:<13} {is_valid(test_case)}")


def main():
    print("VALID EXAMPLES")
    print(f"{'Roman':<13} {'Output':<8} {'Correct':<8} {'Valid?'}")
    print_valid_test_cases("LXXXVII", 87)
    print_valid_test_cases("CCXIX", 219)
    print_valid_test_cases("MCCCLIV", 1354)
    print_valid_test_cases("MMDCLXXIII", 2673)
    print_valid_test_cases("MCDLXXVI", 1476)

    print()
    print("INVALID EXAMPLES")
    print(f"{'Roman':<13} {'Valid?'}")
    print_invalid_test_cases("IL")
    print_invalid_test_cases("VX")
    print_invalid_test_cases("LC")
    print_invalid_test_cases("VM")
    print_invalid_test_cases("VX")
    print_invalid_test_cases("DDM")
    print_invalid_test_cases("VX")
    print_invalid_test_cases("XXXX")
    print_invalid_test_cases("IXI")
    print_invalid_test_cases("This is")
    print_invalid_test_cases(":(")
    print_invalid_test_cases("VX")
    print_invalid_test_cases("LC")
    print_invalid_test_cases("DM")
    print_invalid_test_cases("IIV")
    print_invalid_test_cases("CCM")


if __name__ == "__main__":
    main()
