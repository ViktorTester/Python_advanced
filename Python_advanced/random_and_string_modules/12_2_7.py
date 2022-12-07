from string import ascii_uppercase as letters
from random import randint, choice


def generate_index():
    index = ''
    for i in range(2):
        index += str(choice(letters))
    index += str(randint(1, 99)) + '_' + str(randint(1, 99))
    for i in range(2):
        index += str(choice(letters))

    return index


correct_index = generate_index()
print(correct_index)

# Postal code in Latveria looks like: LetterLetterNumber_NumberLetterLetter,
# where Letter is a capital letter of the English alphabet,
# Number is a number from 0 to 99 (inclusive).

# The generate_index() function, using the random module,
# generates and returns a random, valid postal code for Latveria.
