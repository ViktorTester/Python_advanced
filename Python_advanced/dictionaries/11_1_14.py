my_dict = {
    'C1': [10, 20, 30, 7, 6, 23, 90],
    'C2': [20, 30, 40, 1, 2, 3, 90, 12],
    'C3': [12, 34, 20, 21],
    'C4': [22, 54, 209, 21, 7],
    'C5': [2, 4, 29, 21, 19],
    'C6': [4, 6, 7, 10, 55],
    'C7': [4, 8, 12, 23, 42],
    'C8': [3, 14, 15, 26, 48],
    'C9': [2, 7, 18, 28, 18, 28]
}
arr = []
arr1 = []

for key, value in my_dict.items():
    arr = []
    for i in range(len(value)):
        if value[i] < 20 or value[i] == 20:
            arr.append(value[i])
    arr1.append(arr)

arr3 = []

for key in my_dict:
    arr3.append(key)

my_dict = dict(zip(arr3, arr1))

print(my_dict)

# Can be replaced with the following code:

my_dict = {k: [i for i in v if i <= 20] for k, v in my_dict.items()}

# The program, using the generator, outputs the
# 'my_dict' dictionary, except for those whose value is greater than 20.
