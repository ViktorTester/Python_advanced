n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j != n - 1:
            if i + j < n:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 2
        else:
            matrix[i][n - i - 1] = 1

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print(matrix[x][y], end=' ')
    print()

# The input to the program is a natural number n. The program creates an
# n × n matrix and fills it according to the following rule:

# the numbers on the secondary diagonal are 1;
# numbers above this diagonal are 0;
# numbers below this diagonal are 2.