with open('words.txt', encoding='utf-8') as file:
    text = file.readline().split()

    top = max(text, key=len)

    for i in range(len(text)):
        if len(text[i]) == len(top):
            print(text[i])

# There is a words.txt text file with words separated by a gap. The program
# finds and displays the longest words of this file, without changing their order.
