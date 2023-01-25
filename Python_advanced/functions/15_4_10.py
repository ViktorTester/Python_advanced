numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
           (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
           (90, 1, -45, -21)]


def avg(number):
    return sum(number) / len(number)


print(min(numbers, key=avg))
print(max(numbers, key=avg))

# Given a list of numbers containing tuples of numbers. The program,
# using the built-in functions min() and max(), displays those tuples
# (each on a separate line) that have the minimum and maximum arithmetic mean of the elements.
