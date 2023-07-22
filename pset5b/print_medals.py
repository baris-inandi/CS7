def print_medals(medal_counts):
    """Takes the a dictionary of medal counts and prints
    a nicely formatted table with totals for each country
    as described in the pset 5 problem.
    """
    print(f"{'Country':>14}{'Gold':>8}{'Silver':>8}{'Bronze':>8}{'Total':>8}")
    for i in sorted(list(medal_counts)):
        print(f"{i:>14}", end="")
        for j in medal_counts[i]:
            print(f"{j:>8}", end="")
        print(f"{sum(medal_counts[i]):>8}", end="")
        print()


def main():
    MEDAL_COUNTS = {
        "Canada": [0, 3, 0],
        "Italy": [0, 0, 1],
        "Germany": [0, 0, 1],
        "Japan": [1, 0, 0],
        "Kazakhstan": [0, 0, 1],
        "Russia": [3, 1, 1],
        "South Korea": [0, 1, 0],
        "United States": [1, 0, 1],
    }
    print_medals(MEDAL_COUNTS)


if __name__ == "__main__":
    main()
