def right_triangle(height: int):
    for i in range(height):
        print(((i) * " ") + ((height - i) * "*"))


def main():
    right_triangle(int(input("What should be the height of the triangle? ")))


if __name__ == "__main__":
    main()
