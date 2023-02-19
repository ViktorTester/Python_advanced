import random

s = open('lines.txt', 'r', encoding='utf-8')

text = [line.strip() for line in s.readlines()]

print(random.choice(text))

s.close()

# The lines.txt file consists of several lines.
# The program displays a random line from this file on the screen.