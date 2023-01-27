numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
           (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]

def avgNumbers(number):
    return min(number) + max(number)

print(sorted(numbers, key=avgNumbers))

# Given a list of numbers containing tuples of numbers. The program sorts and
# displays the list of numbers according to the sum
# of the minimum and maximum elements of the tuple.