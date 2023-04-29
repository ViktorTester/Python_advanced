s = input().split()
letters = {}

for x in s:
    letters[x] = letters.get(x, -1) + 1
    if letters[x] == 0:
        print(1, end=' ')
    else:
        print(1 + letters[x], end =' ')

# Given a string of text consisting of words and space characters.
# A word is a sequence of letters, words separated by one or more spaces.

# The program determines for each word the serial number of its occurrence
# in the text in this particular form, case-sensitive. For the first occurrence of a word,
# the program will print 1, for the second occurrence of the same word, 2, and so on.