numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]


result = {}
for i in range(len(numbers)):
    result[i] = numbers[i] ** 2

# Can be replaced with the following code:

result = {i: numbers[i] ** 2 for i in range(len(numbers))}

print(result)

# The program, using the generator, outputs the 'result' dictionary,
# in which the key is the position of the number
# in the 'numbers' list (starting from 0), and the value is its square.
