with open('input.txt', 'r', encoding='utf-8') as file1, open('output.txt', 'w', encoding='utf-8') as file2:
    text = [line.strip() for line in file1.readlines()]

    for index, item in enumerate(text, 1):
        file2.write(str(index) + ') ' + str(item) + '\n')

# There is a text file input.txt, consisting of several lines. The program writes
# the contents of this file to the file output.txt in the form of a numbered list,
# where each line is preceded by its number,
# the symbol ')' and a space. Line numbering starts from 1.