n = int(input())
matrix = []

for j in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

for i in range(n // 2):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()

# A square matrix of numbers is given. The program mirrors its elements with
# respect to the horizontal axis of symmetry.
#
# The input to the program is a natural number n — the number of rows and columns
# in the matrix, then the elements of the matrix line by line, separated by a space.