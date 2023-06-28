def main():
    end = int(input("I will compute the sum of even integers from 2 through? "))
    s = 0
    for i in range(2, end + 1, 2):
        s += i
    print(s)


if __name__ == "__main__":
    main()
