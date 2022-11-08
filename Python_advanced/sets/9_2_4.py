m, n = int(input()), int(input())

set_a = {input() for i in range(m)}
arr = [input() for j in range(n)]

for x in range(len(arr)):
    if arr[x] in set_a:
        print('YES')
    else:
        print('NO')



# The children are playing the game of the city. They love this game very much
# and know many cities, but by the end of the game they forget which cities have already been named.

# The program reads information about the game and reports whether the next city is named again or not.

# The input to the program in the first line is a natural
# number n - the number of named cities, in the next n lines the named
# cities are entered and another line with a new, just named city.