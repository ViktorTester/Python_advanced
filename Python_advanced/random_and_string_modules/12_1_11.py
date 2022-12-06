from random import randrange

n = int(input())

for i in range(n):
    num = randrange(2)
    if num == 0:
        print("Heads")
    else:
        print("Tails")

# The program, using the random module, simulates coin tosses.
# The program takes as input the number of attempts and displays the results of the rolls:
# Heads or Tails (each on a separate line).