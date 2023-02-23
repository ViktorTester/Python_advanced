from random import choice

with open('last_names.txt', 'r') as last_names, open('first_names.txt', 'r') as first_names:
    text_fnames = [line.strip() for line in first_names.readlines()]
    text_lnames = [line.strip() for line in last_names.readlines()]

    for i in range(3):
        print(choice(text_fnames), choice(text_lnames))

# There are two text files first_names.txt and last_names.txt,
# one with first names and the other with last names.

# The program, using the random module, creates 3 random pairs of first
# name + last name, and then prints them out, each on a separate line.