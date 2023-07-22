"""
Finds the max increase between any two elements in a random list
(not necessarily adjacent)
"""
import random
import sys
import time


def max_increase(a):
    if len(a) < 1:
        print("empty list")
        return
    index1 = -1
    index2 = -1
    max_increase = 0
    min = a[0]
    min_index = 0
    for i in range(1, len(a)):
        if a[i] - min > max_increase:
            max_increase = a[i] - min
            index1 = min_index
            index2 = i
        elif a[i] < min:
            min = a[i]
            min_index = i
    if max_increase == 0:
        print("this data didn't increase ever")
    else:
        print(
            f"For a random list of size {len(a)}, the max increase",
            f"was {max_increase}, between indices {index1} and {index2}.",
        )


def make_random_nums(size):
    MAX_NUM = 1_000_000
    print(f"Generating random list of {size} numbers.")
    return [random.randint(0, MAX_NUM) for i in range(size)]


def main():
    list_size = int(input("Please the size of the list to be generated: "))

    numbers = make_random_nums(list_size)
    # uncomment this if you want to see the list generated:
    # print(numbers)

    print(f"Now searching for the max increase.")
    start_time = time.time()
    max_increase(numbers)
    elapsed_time = time.time() - start_time
    print(f"it took {elapsed_time:.4f} seconds to find.")


if __name__ == "__main__":
    main()
