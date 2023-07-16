from random import randint


def do_roll():
    """Simulates rolling 2 dice. Returns the sum of the two rolls."""
    r1, r2 = randint(1, 6), randint(1, 6)  # nosec B311 (ignore bandit warning)
    print_roll(r1, r2)
    return r1 + r2


def print_roll(roll_1, roll_2):
    """
    Prints the results of a roll.
    roll_1, roll_2 are integers representing the rolls.
    Returns nothing.
    """
    print(f"Computer rolls a {roll_1} and a {roll_2}, for a total of {roll_1+roll_2}.")


def get_point():
    """
    Plays craps (rolls) until a point is established.
    Returns the value of the point.
    """
    out = do_roll()
    return out if out in [4, 5, 6, 8, 9, 10] else get_point()


def play_from_point(point):
    """
    Plays using the value of point
    Returns True if the player wins, False otherwise.
    """
    new = do_roll()
    if new == 7:
        return False
    elif new == point:
        return True
    return play_from_point(point)


def main():
    # Add your solution to the problem that makes use of the above functions.
    # Note: this does *not* mean that all the functions must be called from main.
    point = get_point()
    print(f"{point} is now the established POINT.")
    if play_from_point(point):
        print("YOU WIN")
    else:
        print("YOU LOSE")


if __name__ == "__main__":
    main()
