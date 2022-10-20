n = int(input())
matrix = []

for j in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

for i in range(n):
    matrix[i][i], matrix[n-i-1][i] = matrix[n-i-1][i], matrix[i][i]

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()

# A square matrix of numbers is given. The program swaps the elements on the main
# and side diagonals, while each element must remain in the same column (that is, in each
# column, you need to swap the element on the main diagonal and on the side diagonal).

# The input to the program is a natural number n — the number of rows and columns in
# the matrix, then the elements of the matrix line by line, separated by a space.