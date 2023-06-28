def top():
    return """  _______
 /       \\
/         \\"""


def bottom():
    return """\\         /
 \\_______/
"""


def line():
    return '-"-\'-"-\'-"-'


def hexagon():
    return top() + "\n" + bottom()


def main():
    print(hexagon())
    print(line())
    print(hexagon())
    print(line())
    print(bottom())
    print(top())
    print(line())
    print(bottom())


if __name__ == "__main__":
    main()
