from random import choice

N = 5


def drunk_walk():
    """Simulates a random walk. Returns the number blocks walked as well as
    a boolean that is True if ended up at home and False ended up in jail.
    Takes no input parameters. Must not print anything!
    """
    at, blocks_walked = 6, 0
    while not (at == 1 or at == 11):
        x = choice([-1, 1])  # nosec B311 (ignore bandit warning)
        at += x
        blocks_walked += 1
    return (blocks_walked, at == 1)


def main():
    # Add your solution to the problem that makes use of the above.
    total = 0
    for _ in range(N):
        (blocks, landed_home) = drunk_walk()
        total += blocks
        print("Here we go again... time for a walk!")
        print(f"Walked {blocks} blocks, and ")
        print(f"Landed in {'HOME' if landed_home else 'JAIL'}")
        print()
    print(f"Averate # of blocks equals {total / N:.1f}")


if __name__ == "__main__":
    main()
