with open('text.txt', 'r', encoding='utf-8') as file:
    line = file.read()
    print(line[::-1])

# The file text.txt has one line of text. The program displays this line in reverse order.