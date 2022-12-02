numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

arr = []
arr2 = []
for i in range(len(numbers)):
    arr = []
    for j in range(1, numbers[i] + 1):
        if numbers[i] % j == 0:
            arr.append(j)
    arr2.append(arr)

result = dict(zip(numbers, arr2))

# Can be replaced with the following code:

result = {n: [i for i in range(1, n // 2 + 1) if n % i == 0] + [n] for n in numbers}

print(result)

# Using the generator, the program outputs a dictionary 'result',
# where the key is the 'numbers' list element, and the value is an
# ascending sorted list of all its divisors, starting from 1.
