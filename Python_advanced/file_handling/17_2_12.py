s = open(input(), 'r', encoding='utf-8')

text = [line.strip() for line in s.readlines()]

print(text[-2])

s.close()

# The input to the program is a string with the name of a text file.
# The program displays its penultimate line.