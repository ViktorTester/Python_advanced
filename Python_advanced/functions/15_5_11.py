def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424,
           1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668,
           944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163,
           345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105,
           130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959,
           1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433,
           456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]


def divisible_by_5(num):
    if 0 < num // 100 < 10:
        return num % 5 == 2


def cube(num):
    return num ** 3


filtered = filter(divisible_by_5, numbers)
mapped = map(cube, filtered)

print(*mapped, sep='\n')

# The program, using the filter() and map() functions, selects three-digit numbers
# from the given list of numbers that give a remainder of 2 when divided by 5,
# and displays their cubes, each on a separate line.
