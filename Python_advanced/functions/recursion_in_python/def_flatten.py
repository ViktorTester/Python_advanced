def flatten(n: list) -> list:
    arr = []
    for i in n:
        if type(i) == list:
            arr.extend(flatten(i))
        else:
            arr.append(i)
    return arr

assert flatten([1, [2, 3, [4]], 5]) == [1, 2, 3, 4, 5]
assert flatten([1, [2, 3], [[2], 5], 6]) == [1, 2, 3, 2, 5, 6]
assert flatten([[[[9]]], [1, 2], [[8]]]) == [9, 1, 2, 8]
print('Ok')

# The function takes a list of unlimited nesting as input, and returns a linear list.