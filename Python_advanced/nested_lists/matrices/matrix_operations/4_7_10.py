num = input().split()
n = int(num[0])
m = int(num[1])
array1 = []
array2 = []

for e in range(n):
    array1.append(input().split())
array1 = [[int(y) for y in x] for x in array1]

input()

num2 = input().split()
m = int(num[1])
k = int(num[0])

arr = [[0] * k for _ in range(n)]

for g in range(m):
    array2.append(input().split())
array2 = [[int(y) for y in x] for x in array2]

for i in range(n):
    for j in range(k):
        for p in range(m):
            arr[i][j] += array1[i][p] * array2[p][j]

for r in range(len(arr)):
    for l in range(len(arr[r])):
        print(str(arr[r][l]).ljust(2), end=' ')
    print()

# The program multiplies two matrices.

# The program receives two natural numbers n and m as input — the number of rows
# and columns in the first matrix, then the elements of the first matrix,
# then an empty string. This is followed by the numbers m and k — the number
# of rows and columns of the second matrix, then the elements of the second matrix.