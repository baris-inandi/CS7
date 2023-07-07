def eligible_for_house(age: int, length_of_citizenship: int) -> bool:
    """
    No Person shall be a Representative who shall
    not have attained to the Age of twenty-five Years,
    and been seven Years a Citizen of the United
    States, and who shall not, when elected, be an
    Inhabitant of that State in which he shall be chosen.
    """
    return age >= 25 and length_of_citizenship >= 7


def eligible_for_senate(age: int, length_of_citizenship: int) -> bool:
    """
    No Person shall be a senator who shall not have attained
    to the Age of thirty Years, and been nine Years a Citizen of
    the United States, and who shall not, when elected, be an
    Inhabitant of that State for which he shall be chosen.
    """
    return age >= 30 and length_of_citizenship >= 9


def main():
    """
    Someone of age 37 and 3 years of citizenship is not eligible
    for election to either the House or the Senate, so the functions
    should both return False.
    """
    print(eligible_for_house(37, 3))  # False
    print(eligible_for_senate(37, 3))  # False
    """
    eligible_for_house(47, 8) should return True, but
    eligible_for_senate(47, 8) should return False.
    """
    print(eligible_for_house(47, 8))  # True
    print(eligible_for_senate(47, 8))  # False


if __name__ == "__main__":
    main()
