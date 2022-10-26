num = input().split()
n = int(num[0])
m = int(num[1])
arr = [0] * n
array1 = []
array2 = []

for i in range(n):
    arr[i] = [0] * m

for e in range(n):
    array1.append(input().split())
array1 = [[int(y) for y in x] for x in array1]

strange = input()

for g in range(n):
    array2.append(input().split())
array2 = [[int(y) for y in x] for x in array2]

for i in range(len(array1)):
    for j in range(len(array1[i])):
        arr[i][j] = array1[i][j] + array2[i][j]

for r in range(len(arr)):
    for l in range(len(arr[r])):
        print(str(arr[r][l]).ljust(2), end=' ')
    print()

# The program calculates the sums of two matrices.

# The input to the program is two natural numbers n and m — the number of rows
# and columns in the matrices, then the elements of the first matrix,
# then an empty string, followed by the elements of the second matrix.
