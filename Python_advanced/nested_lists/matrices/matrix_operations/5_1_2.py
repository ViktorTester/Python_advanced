n = int(input())
matrix = []
arr = []

for b in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

if len(matrix) > 1:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            arr.append(matrix[i][n - i - 1])
            if j > i > n - 1 - j:
                arr.append(matrix[i][j])
            elif i > j and i > n - 1 - j:
                arr.append(matrix[i][j])
            elif i == j and i >= len(matrix) / 2:
                arr.append(matrix[i][j])
    print(max(arr))
else:
    print(matrix[0][0])

# The program displays the maximum element in the shaded area of the square matrix.

# The input to the program is a natural number n — the number of rows and columns
# in the matrix, then the elements of the matrix.

# _  _  _  _  *
# _  _  _  *  *
# _  _  *  *  *
# _  *  *  *  *
# *  *  *  *  *