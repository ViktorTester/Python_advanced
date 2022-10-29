n = int(input())
matrix = [[0] * n for _ in range(n)]

for x in range(n):
    for i in range(n):
        for j in range(n):
            if x == i - j or x == j - i:
                matrix[i][j] = x

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print(matrix[x][y], end=' ')
    print()

# The input to the program is a natural number n. The program creates an
# n × n matrix and fills it according to the following rule:

# on the main diagonal in place of each element should be the number 0;
# on two diagonals adjacent to the main one, the number 1;
# on the next two diagonals, the number 2, and so on.

# The input to the program is a natural number n — the number of rows and columns in the matrix.