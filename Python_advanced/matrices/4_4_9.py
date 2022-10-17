n, m = int(input()), int(input())
matrix = []
arr2 = []

for _ in range(n * m):
    matrix.append(input())
    if len(matrix) == m:
        print(*matrix)
        arr2.append(matrix[:m])
        del matrix[:m]
print()

for c in range(m):
    for r in range(n):
        print(arr2[r][c], end=' ')
    print()

# The program receives two natural numbers n and m as input, each on a separate
# line — the number of rows and columns in the matrix. Next, the elements of the matrix
# themselves are introduced - words, each on a separate line; in a row there are elements
# first of the first line, then the second, and so on.

# The program reads the elements of the matrix one by one, outputs them as a matrix,
# outputs an empty row, and again the same matrix, but this time swapping rows with columns:
# the first row is output as the first column, and so on.