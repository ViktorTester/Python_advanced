n = input()
matrix = []

for _ in range(8):
    matrix.append(['.'] * 8)

pos_x, pos_y = 8-int(n[1]), ord(n[0])-97
matrix[pos_x][pos_y] = '🐎'

for x in range(8):
    for y in range(8):
        if (x - pos_x) ** 2 + (y - pos_y) ** 2 == 5:
            matrix[x][y] = matrix[x][y].replace('.', '*')

for r in range(8):
    for c in range(8):
        print(matrix[r][c], end=' ')
    print()

# There is a knight on an 8×8 chessboard. The program marks the position of the
# knight on the board and all the cells that the knight beats.
#
# The input to the program is the coordinates of the knight on the chessboard in chess notation.