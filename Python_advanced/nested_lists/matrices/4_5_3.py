n, m = int(input()), int(input())
matrix = []

for j in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

col = input().split()

for g in range(len(col)):
    col[g] = int(col[g])

for z in range(len(matrix)):
    matrix[z][col[0]], matrix[z][col[1]] = matrix[z][col[1]], matrix[z][col[0]]
    print(*matrix[z])

# The program swaps the columns in the matrix.
#
# At the input of the program on different lines are two natural numbers n and m — the
# number of rows and columns in the matrix, then the matrix elements row by row
# separated by a space, then the numbers i and j — the numbers of the columns to be exchanged.