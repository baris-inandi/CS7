def print_triangle(side_length):
    if side_length < 1:
        return
    print("[]" * side_length)
    print_triangle(side_length - 1)


def main():
    print_triangle(5)


if __name__ == "__main__":
    main()
