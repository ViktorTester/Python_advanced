def mean(*args):

    arr = [args[i] for i in range(len(args)) if type(args[i]) in (int, float)]

    if len(arr) == 0:
        return 0.0
    else:
        return sum(arr) / len(arr)


print(mean())
print(mean(7))
print(mean(1.5, True, ['one'], 'two', 2.5, (1, 2)))
print(mean(True, ['one'], 'two', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# The mean() function, which takes an arbitrary number of arguments and returns
# the arithmetic mean of the numeric (int or float) arguments passed to it.