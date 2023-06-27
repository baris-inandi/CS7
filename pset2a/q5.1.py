def first():
    print("Inside first function!")


def second():
    first()
    print("Inside second function!")


def third():
    print("Inside third function!")
    first()
    second()


def main():
    first()
    third()
    second()
    third()


main()
