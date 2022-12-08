from random import sample

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

for i in range(len(matrix)):
    matrix[i] = sample(matrix[i], len(matrix[i]))

# The program randomly shuffles the contents of a matrix (two-dimensional list) using the random module.
