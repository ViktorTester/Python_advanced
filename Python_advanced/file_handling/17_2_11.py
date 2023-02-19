s = open(input(), 'r', encoding='utf-8')

for line in s:
    print(line.strip())

s.close()

# The input to the program is a string with the name of a text file.
# The program displays its contents on the screen.