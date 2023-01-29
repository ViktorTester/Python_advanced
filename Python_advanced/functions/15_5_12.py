def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc


def add(x, y):
    return x + (y ** 2)


def square(num):
    return num ** 2


numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1,
           -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96,
           58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38,
           67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17,
           43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95,
           78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

total = reduce(add, numbers, 0)
print(total)

numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1,
           -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96,
           58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38,
           67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17,
           43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95,
           78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

result = sum(map(square, numbers))
print(result)

# The program calculates and displays the sum of the
# squares of the elements of the numbers list.

# The result can be achieved in two ways: using reduce()
# function, and using map() and sum() functions.
