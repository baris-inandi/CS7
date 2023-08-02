from Pizza import Pizza


def main() -> None:
    appetizer = Pizza(name="Pepperoni", diameter=16, price=10.50, num_slices=10)
    print(appetizer)
    dinner = Pizza(name="Anchovy & Pineapple", diameter=20, price=11.95, num_slices=8)
    print(dinner)
    print(dinner.area_per_slice())
    print(appetizer.area_per_slice())
    print(dinner.cost_per_slice())
    print(appetizer.cost_per_slice())
    print(dinner.cost_per_square_inch())
    print(appetizer.cost_per_square_inch())


if __name__ == "__main__":
    main()
