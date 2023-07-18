import string


def character_index(char):
    if char not in string.ascii_lowercase:
        return -1
    return string.ascii_lowercase.index(char.lower())


def alphabetical_bubble_sort(word):
    word = list(word)
    for _ in range(len(word)):
        for j in range(len(word) - 1):
            if character_index(word[j + 1]) < character_index(word[j]):
                word[j], word[j + 1] = word[j + 1], word[j]
    return "".join(word)


def alphabetical(words):
    """Takes the a list of words and returns a list of strings
    with each of the letters in each word sorted in alphabetical
    (not unicode!) order.
    For example, the for the parameter
    ['apple', 'pumpkin', 'log', 'River', 'fox', 'pond']
    the return value should be
    ['aelpp', 'ikmnppu', 'glo', 'eiRrv', 'fox', 'dnop']
    """
    # Etiher use the built-in sorted function:
    # list(map(lambda word: "".join(sorted(word)), words))

    # Or use a custom bubble sort function:
    return list(map(alphabetical_bubble_sort, words))


def main():
    # Add your solution to the problem that makes use of the above.
    print(alphabetical(["apple", "pumpkin", "log", "River", "fox", "pond"]))


if __name__ == "__main__":
    main()
