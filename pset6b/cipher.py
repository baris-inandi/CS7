import argparse

# with Andres Mahomar


def shift_char(char, n):
    # Shifts a character by n places in the alphabet
    return chr(ord("A") + ((ord(char) + n) % 26))


def shift_char_if_eligible(char, n):
    """
    Shifts char by n places in the alphabet only if
    it is an uppercase letter, otherwise returns char
    """
    if char.isalpha() and char.isupper():
        return shift_char(char, n)
    return char


def vignere(s, key, is_decipher):
    out = ""
    for i in range(len(s)):
        shift = ord(key[i % len(key)])
        if is_decipher:
            shift *= -1
        out += shift_char_if_eligible(s[i % len(s)], shift)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("key")
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("-d", "--decrypt", action="store_true")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as f:
            s = f.read()
        with open(args.output_file, "w") as f:
            f.write(vignere(s, args.key, args.decrypt))
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
