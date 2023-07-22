"""
Finds the max increase between any two elements in a random list
(not necessarily adjacent)
"""
import random
import sys
import time


def max_increase(a):
    index1 = -1
    index2 = -1
    max_increase = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[j] - a[i] > max_increase:
                max_increase = a[j] - a[i]
                index1 = i
                index2 = j
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
