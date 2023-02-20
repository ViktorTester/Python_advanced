with open('data.txt', 'r', encoding='utf-8') as file:
    text = [line.strip() for line in file.readlines()]
    for i in range(1, len(text) + 1):
        print(text[-i])

# The text file data.txt contains lines of text. The program displays all the lines of
# the given file in reverse order: first the last one, then the penultimate one, and so on.