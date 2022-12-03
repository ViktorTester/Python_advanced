tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18),
          (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
arr1 = []
arr2 = []

for i in range(len(tuples)):
    arr1.append(tuples[i][0])
    arr2.append(tuples[i][1:])

result = dict(zip(arr1, arr2))

print(result)

# Can be replaced with the following code:

result = {i[0]: i[1:] for i in tuples}

# Using the generator, the program outputs a 'result' dictionary,where the key
# is the first element of each tuple and the value is the tuple of the remaining two elements.