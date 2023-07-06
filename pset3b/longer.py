"""
Write a function named print_longer that takes two lists as input and prints out
the longer one as well as the last element of the list. You may assume the input lists are
nonempty and your function should work with any nonempty list no matter what the
size. If the two lists are the same length, it should print "The lists are the same
length!" To give you practice with f-strings, when printing the longer list you may only
use one print statement and it may only take one f-string as an argument. Demonstrate
your function works by testing it in a main function. For example,
print_longer(['chocolate', 'vanilla'], [1, 5, 9, 7]) should print
 [1, 5, 9, 7] is the longer list and its last element is 7
"""


def print_longer(list1, list2):
    len1, len2 = len(list1), len(list2)
    if len1 == len2:
        print("The lists are the same length!")
    else:
        longer = list1 if len1 > len2 else list2
        last = longer[-1]
        print(f"{longer} is the longer list and its last element is {last}")


def main():
    print_longer(["chocolate", "vanilla"], [1, 5, 9, 7])


if __name__ == "__main__":
    main()
