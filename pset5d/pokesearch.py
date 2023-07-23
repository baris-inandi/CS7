from pokedex import data as pdx

TRAITS = ["HP", "Attack", "Sp. Attack", "Sp. Defense", "Speed"]


def english_name(pokemon):
    """OPTIONAL:
    You can use this as a sorting key function for Pokemon"""
    return pokemon["name"]["english"]


def pokesearch(trait, minimum, maximum):
    """
    Returns a list of Pokemon data structures (dictionaries,
    as shown in the pset problem description) that
    have a value of trait between minimum and maximum
    """
    return sorted(
        [pokemon for pokemon in pdx if minimum <= pokemon["base"][trait] <= maximum],
        key=lambda x: english_name(x),
    )


def main():
    print("What Pokemon trait would you like to search on?")
    trait = input("Valid traits are HP, Attack, Sp. Attack, Sp. Defense, Speed: ")
    if trait not in TRAITS:
        raise ValueError("Invalid trait: " + trait)
    minval = int(input(f"What is the minimum value for {trait}? "))
    maxval = int(input(f"What is the maximum value for {trait}? "))
    print("The Pokemon that match are:")
    results = pokesearch(trait, minval, maxval)
    for pokemon in results:
        print(f"{pokemon['name']['english']:32} {pokemon['base'][trait]}")


if __name__ == "__main__":
    main()
