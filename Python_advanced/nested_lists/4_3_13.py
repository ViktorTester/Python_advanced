def chunked():
    arr = []

    while s:
        arr.append(s[:a])
        del s[:a]
    print(arr)


s, a = input().split(), int(input())
chunked()

# The input to the program is two strings, one character,
# the other the number n. The list is formed from the first line.

# The chunked() function takes as input a list and a number that specifies the
# size of a chunk (chunk), and returns a list of chunks of the specified length.