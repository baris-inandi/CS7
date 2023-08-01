def index_of(text, a_string) -> int:
    """
    Returns the starting position of the first substring of text that matches
    a_string.  Return -1 if a_string is not a substring of the text.
    """
    if len(text) < len(a_string):
        return -1
    if text[: len(a_string)] == a_string:
        return 0
    index = index_of(text[1:], a_string)
    if index == -1:
        return index
    return index + 1


def main():
    print(index_of("Mississippi", "sip"))
    print(index_of("Mississippi", "pip"))
    print(index_of("Mississippi", "Miss"))


if __name__ == "__main__":
    main()
