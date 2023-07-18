"""Add your solution to the problem 'real_estate' here."""


def is_vowel(c):
    """Returns true if c is an upper- or lower-case vowel character"""
    return c.lower() in ["a", "e", "i", "o", "u"]


def devowel(ad):
    """Takes the text ad and returns a string with
    non-initial vowels removed. The letter 'y' is not considered a
    vowel."""
    prev, out = " ", ""
    for c in ad:
        if not is_vowel(c) or prev.isspace():
            out += c
        prev = c
    return out


def main():
    # Add your solution to the problem that makes use of the above.
    print(devowel(input("Enter an ad: ")))


if __name__ == "__main__":
    main()
