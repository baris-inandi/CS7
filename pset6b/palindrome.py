def is_palindrome(s):
    if s[0].lower() != s[-1].lower():
        return False
    if len(s) <= 2:
        return True
    return is_palindrome(s[1:-1])


def main():
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("aAA"))
    print(is_palindrome("kayaK"))


if __name__ == "__main__":
    main()
