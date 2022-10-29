n = int(input())
matrix = []
arr = [[0] * n for _ in range(n)]

for b in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

for i in range(n):
    for j in range(len(matrix[i])):
        arr[i][j] = matrix[j][i]

for r in range(len(arr)):
    for l in range(len(arr[r])):
        print(str(arr[r][l]).ljust(2), end=' ')
    print()

# The program transposes a square matrix.

# The input to the program is a natural number n — the number of
# rows and columns in the matrix, then the elements of the matrix.

# A transposed matrix is a matrix obtained from the original
# matrix by replacing rows with columns.