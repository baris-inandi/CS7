# Suppose a non-empty Python list of integers named foobar has been created. Write one or more Python statements to perform each of the following. Note that each task is independent of the other three:
foobar = [-3, -2, -1, 0, 1, 2, 3]
# Set every element of foobar to the value 5.
foobar = [5 for _ in range(len(foobar))]
# Shift all elements by one to the right and move the last element into the first position. For example, [1, 4, 9, 16, 25] would be transformed to [25, 1, 4, 9, 16].
foobar.insert(0, foobar.pop())
# Swap the first value in the foobar list with the last value in the list.
foobar[0], foobar[-1] = foobar[-1], foobar[0]
# Change all negative values to positive values (of the same magnitude) in foobar.
foobar = list(map(abs, foobar))
