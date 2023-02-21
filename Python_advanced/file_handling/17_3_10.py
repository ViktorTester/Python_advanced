with open('numbers.txt', 'r', encoding='utf-8') as file:
    text = [line.split() for line in file.readlines()]
    for i in range(len(text)):
        text[i] = sum(map(int, text[i]))
        print(text[i])

# Each line in the numbers.txt file can contain one or
# more integers separated by one or more spaces.

# The program calculates the sum of the numbers in each line and displays
# this sum on the screen (for each line, the sum of the numbers in this line is displayed).