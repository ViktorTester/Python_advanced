scrabble = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

word = list(input())
counter = 0
for i in range(len(word)):
    for key, value in scrabble.items():
        if word[i] in value:
            counter += key

print(counter)

# In the Scrabble game, each letter is worth a certain number of points.
# The total value of a word is the sum of the points of its letters.
# The rarer the letter occurs, the more it is valued.

# The program calculates the total cost of the entered word.