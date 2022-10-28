n = int(input())
matrix = []

for g in range(n):
    matrix.append(input().split())
matrix = [[int(y) for y in x] for x in matrix]

m = int(input())

matrix_copy = matrix.copy()

for x in range(m - 1):
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for p in range(n):
                arr[i][j] += matrix[i][p] * matrix_copy[p][j]
    matrix_copy = arr.copy()

for r in range(len(arr)):
    for l in range(len(arr[r])):
        print(str(arr[r][l]).ljust(2), end=' ')
    print()

# The program raises a square matrix to the m-th power.

# The input to the program is a natural number n — the number of rows and
# columns in the matrix, then the elements of the matrix, then a natural number m.