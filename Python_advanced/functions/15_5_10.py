numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013,
           23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]


def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def rounding(number):
    return round(number, 2)


print(*(map(rounding, numbers)), sep='\n')

# The program uses the map() function to round all the elements of the 'numbers' list
# to 2 decimal places, and then prints them out, each on a separate line.