s = input().split()
letters = {}

for x in s:
    letters[x] = letters.get(x, -1) + 1
    if letters[x] == 0:
        print(x, end=' ')
    else:
        print(x + '_' + str(letters[x]), end =' ')

# The input to the program is a string containing identifier strings. The program corrects
# them so that there are no duplicates in the resulting string. To do this,
# the postfix _n is added to the repeating identifiers, where n is the number of times
# such an identifier has already been encountered.