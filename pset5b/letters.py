import string


def missing_letters(word_list):
    """Takes a word list and returns a sorted
    list of letters, capitalized that do not appear
    in the list.
    """
    return sorted(
        set(string.ascii_uppercase) - {j.upper() for i in word_list for j in i}
    )


def main():
    print(missing_letters(["Now", "is", "the", "TIME"]))


if __name__ == "__main__":
    main()
