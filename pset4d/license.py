"""Add your solution to the problem 'license' here."""
import string
import random


def random_capital():
    """Returns a randomly selected upper-case letter. Takes no input."""
    return random.choice(string.ascii_uppercase)  # nosec B311 (ignore bandit warning)


def random_plate():
    """Returns one randomly selected license plate. Takes no input."""
    return (
        str(random.randint(100, 999))  # nosec B311 (ignore bandit warning)
        + " "
        + "".join([random_capital() for _ in range(3)])
    )


def main():
    for _ in range(20):
        print(random_plate())


if __name__ == "__main__":
    main()
