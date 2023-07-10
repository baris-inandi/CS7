def get_prices():
    prices = []
    for _ in range(10):
        prices.append(int(input("enter stock price: ")))
    return prices


def print_change(day1_price, day2_price, day1_num):
    diff = abs(day2_price - day1_price)
    print(
        f"Largest change of {diff} from {day1_price} to {day2_price} occurred between day #{day1_num} and day #{day1_num+1}."
    )


def find_change():
    max_diff = 0
    p1 = -1
    for i in range(10):
        p2 = int(input(f"enter stock price for day {i+1}: "))
        if p1 == -1:
            p1 = p2
        diff = abs(p2 - p1)
        if diff > max_diff:
            max_diff = diff
            day1_price = p1
            day2_price = p2
            day1_num = i + 1
        p1 = p2
    return [day1_price, day2_price, day1_num]


def main():
    print_change(*find_change())


if __name__ == "__main__":
    main()
