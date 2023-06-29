"""
A certain charity designates donors who give $10,000.00 or more as 
Benefactors; those who give $1,000.00 or more but less than $10,000.00 as Patrons; 
those who give $200.00 or more but less than $1,000.00 as Supporters; those who 
give $15.00 but less than $200.00 as Friends; and those who give less than $15 as 
Cheapskates. $0 would be considered a Cheapskate amount.
Write a function donor() containing a nested if-else statement (or 
statements) that, given a keyboard input with the amount of a contribution, 
returns the correct designation for that contributor.
"""


def donor(amount: float) -> str:
    if amount >= 10_000:
        return "Benefactor"
    elif amount >= 1_000:
        return "Patron"
    elif amount >= 200:
        return "Supporter"
    elif amount >= 15:
        return "Friend"
    elif amount >= 0:
        return "Cheapskate"
    else:
        exit()


def main():
    amount = float(input("Enter the amount of a contribution: $"))
    name = donor(amount)
    print(name + "!")


if __name__ == "__main__":
    main()
