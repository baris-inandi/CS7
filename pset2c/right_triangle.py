def right_triangle(height: int) -> str:
    result = []
    for i in range(height):
        result.append(((i) * " ") + ((height - i) * "*"))
    return "\n".join(result)


def main():
    print(right_triangle(int(input("What should be the height of the triangle? "))))


if __name__ == "__main__":
    main()
