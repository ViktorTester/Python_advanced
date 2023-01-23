def sq_sum(*args):
    arr = [args[i] ** 2 for i in range(len(args))]
    return sum(arr)


print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# The sq_sum() function takes an arbitrary number of numeric
# arguments and returns the sum of their squares.
