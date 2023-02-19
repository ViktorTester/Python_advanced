s = open('numbers.txt', 'r', encoding='utf-8')

text = [int(line.strip()) for line in s.readlines()]

print(sum(text))

s.close()

# The numbers.txt file consists of lines, each of which contains an integer.
# The program displays the sum of these numbers.