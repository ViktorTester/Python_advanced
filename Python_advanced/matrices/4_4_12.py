n = int(input())
matrix = []
arr = []

for j in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

for i in range(len(matrix)):
    for b in range(len(matrix[i])):
        if i == b:
            arr.append(matrix[i][b])
        elif i > b:
            arr.append(matrix[i][b])

print(max(arr))

# The input to the program is a natural number n — the number of rows and
# columns in the matrix, then the matrix elements (integers) line by line separated by a space.

# The program displays one number — the maximum element in the shaded area of the square matrix.

# *  _  _  _  _
# *  *  _  _  _
# *  *  *  _  _
# *  *  *  *  _
# *  *  *  *  *