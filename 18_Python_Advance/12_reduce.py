from functools import reduce
a = [1, 2, 3, 4, 5, 6]
def sum(a, b):
    return a + b

#reduce() is a function that applies a given function cumulatively to the items of an iterable, reducing it to a single value.
c = reduce(sum, a)

# Printing the result
print(c)
