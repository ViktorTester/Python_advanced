n = int(input())
matrix = ['.'.split() * n for _ in range(n)]
arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(len(matrix[i])):
        matrix[i][i] = '*'
        matrix[i][n - i - 1] = '*'
        if i == n // 2:
            matrix[i][j] = '*'
        elif j == n // 2:
            matrix[i][j] = '*'


for r in range(len(matrix)):
    for l in range(len(matrix[r])):
        print(str(matrix[r][l]).ljust(2), end=' ')
    print()

# The input to the program is an odd natural number n. The program creates an
# n × n matrix by filling it with symbols ' . ' Then fills with characters ' * '
# the middle row and column of the matrix, the main and secondary diagonal of the matrix.