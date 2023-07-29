import random
from sys import argv


def generate_random_birthday():
    # Returns the day of the year (1-365) that someone was born on
    return random.randint(1, 365)


def group_has_same_birthday(num_people):
    # Returns True if at least two people in the group have the same birthday
    birthdays = {}
    for _ in range(num_people):
        birthday = generate_random_birthday()
        if birthday in birthdays:
            return True
        birthdays[birthday] = True
    return False


def run_simulations(num_simulations, num_people):
    # Returns the amount of simulations where at least two people in the group have the same birthday
    return sum([group_has_same_birthday(num_people) for _ in range(num_simulations)])


def print_simulation_results(num_simulations, num_people, num_sims_with_match):
    print(f"After {num_simulations} simulations")
    print(f"with {num_people} students")
    print(f"there were {num_sims_with_match} simulations with at least one match")


def main():
    if len(argv) != 3:
        print("Usage: python birthday.py <num_simulations> <num_people>")
        exit(1)
    num_simulations = int(argv[1])
    num_people = int(argv[2])
    num_sims_with_match = run_simulations(num_simulations, num_people)
    print_simulation_results(num_simulations, num_people, num_sims_with_match)


if __name__ == "__main__":
    main()
