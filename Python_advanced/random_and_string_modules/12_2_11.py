from random import sample, shuffle

arr = [x for x in range(1, 76)]
game_numbers = sample(arr, 25)
arr2 = []

shuffle(game_numbers)

game_numbers[12] = 0

for i in range(len(game_numbers)):
    arr2.append(game_numbers[i])
    if len(arr2) == 5:
        print(*arr2)
        arr2 = []

# The game of bingo requires a 5×5 card containing various (unique)
# integers from 1 to 75 (inclusive), with the center cell being empty (filled with the number 0).

# The program uses the random module to generate and display a random bingo card.