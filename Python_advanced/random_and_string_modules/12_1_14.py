from random import randrange

arr = []

while len(arr) < 7:
    num = randrange(1, 50)
    if num not in arr:
        arr.append(num)

arr.sort()

print(*arr)

# The lottery ticket contains 7 numbers from the range from 1 to 49 (inclusive).

# The program, using the random module, generates 7 different random numbers for
# a lottery ticket. The program checks the numbers for the absence of duplicates
# and displays the numbers in ascending order on one line with one space character.