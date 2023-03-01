with open(input(), encoding='utf-8') as file:
    text = [line.strip() for line in file.readlines()]

    arr = []
    for i in text:
        if len(text) <= 10:
            print(i)
        else:
            arr.append(text[-10:])
            print(*arr[0], sep='\n')
            break

# The input program is given a line of text with the name of the text file.
# The program displays the last 10 lines of this file.