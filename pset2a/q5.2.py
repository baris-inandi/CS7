def first():
    print("Inside first function!")


def second():
    first()
    print("Inside second function!")


def third():
    first()
    print("Inside third function!")
    second()


def main():
    first()
    third()
    second()
    third()


main()
