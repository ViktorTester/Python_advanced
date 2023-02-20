with open('lines.txt', 'r', encoding='utf-8') as file:
    text = [line.strip() for line in file.readlines()]
    top = max(text, key=len)
    arr = [text[i] for i in range(len(text)) if len(text[i]) == len(top)]
    print(*arr, sep='\n')

# The lines.txt file contains lines of text. The program outputs all lines
# of the greatest length from the file without changing their order.