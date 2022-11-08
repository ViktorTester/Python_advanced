m, n = int(input()), int(input())

set_a = {input() for i in range(m)}
arr = [input() for j in range(n)]

for x in range(len(arr)):
    if arr[x] in set_a:
        print('YES')
    else:
        print('NO')

# The boy received at the end of the school year a list of literature for the summer.
# Now he needs to find out which books from this list he has.

# The input to the program in the first line is a natural number m — the number
# of books in the boy's home library. The second line contains a natural
# number n — the number of books on the list for the summer.
# Then there are m lines with the titles of books from the
# home library and n lines of titles from the list for the summer.