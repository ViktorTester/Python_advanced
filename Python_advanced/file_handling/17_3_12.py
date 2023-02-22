import string

with open('file.txt', 'r', encoding='utf-8') as file:
    text = [line.strip() for line in file.readlines()]
    X = len(text)
    Y = 0
    Z = 0

    for i in text:
        Y += len(i.split())

    file.seek(0)

    text = [line.strip() for line in file.read()]
    for j in text:
        if j not in string.punctuation and j != '' and j.isalpha():
            Z += len(j)

    print(f'Input file contains: \n{Z} letters \n{Y} words \n{X} lines')

# The text file 'file.txt' is typed in Latin. The program displays the number
# of letters of the Latin alphabet, words and lines.