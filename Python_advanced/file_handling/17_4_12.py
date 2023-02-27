with open('Cgoats.txt', encoding='utf-8') as file1, open(
        'answer.txt', 'w', encoding='utf-8') as file2:
    goats = [line.strip() for line in file1.readlines()]

    for i in range(len(goats)):
        if goats[i] == 'GOATS':
            arr = (goats[i + 1:])

    total_goats = len(arr)
    dct = {}

    for j in arr:
        dct[j] = dct.get(j, 0) + 1

    for key, value in dct.items():
        if int(value / 100 * total_goats) > 7:
            print(key, file=file2)

# There is a text file goats.txt in the first line of which the word COLORS is written,
# followed by a list of all possible colors of goats. Then comes a line with the word GOATS,
# and then directly listing goats of different colors.
# The list of goats includes only the lines from the first list.

# The program creates an answer.txt file and outputs to it a list of goats whose number
# is more than 7% of the total number of goats in the list.
