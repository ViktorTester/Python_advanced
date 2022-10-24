num = input().split()
n = int(num[0])
m = int(num[1])
matrix = []
arr = []

for i in range(1, n * m + 1):
    matrix.append(i)
    if len(matrix) == m:
        arr.append(matrix)
        matrix = []

for x in range(len(arr)):
    for y in range(len(arr[x])):
        print(str(arr[x][y]).ljust(2), end=' ')
    print()

# The program receives two natural numbers n and m as input. The program creates an
# n × m matrix and fills it with numbers from 1 to n ⋅ m.

# The input to the program on one line is two natural numbers
# n and m — the number of rows and columns in the matrix.