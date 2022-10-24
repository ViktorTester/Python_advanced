n = int(input())
matrix = []
arr = []

for j in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

arr1, arr2, arr3, arr4 = [], [], [], []

for i in range(len(matrix)):
    for b in range(len(matrix[i])):
        if i < b and i < ((len(matrix)) - 1 - b):
            arr1.append(matrix[i][b])
        elif b > i > ((len(matrix)) - 1 - b):
            arr2.append(matrix[i][b])
        elif i > b and i > ((len(matrix)) - 1 - b):
            arr3.append(matrix[i][b])
        elif b < i < ((len(matrix)) - 1 - b):
            arr4.append(matrix[i][b])

print(f'Upper quarter: {sum(arr1)}', f'Right Quarter: {sum(arr2)}',
      f'bottom quarter: {sum(arr3)}', f'left quarter: {sum(arr4)}', sep='\n')

# The square matrix is divided into four quarters bounded by the main and secondary diagonals.
# The program calculates the sum of the elements of each quarter.
# Diagonal elements are not taken into account.