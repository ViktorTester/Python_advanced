n = int(input())
new_set = ''

for i in range(n):
    new_set += input().lower()

new_set = set(new_set)

print(len(new_set))

# The program displays the total number of unique
# characters in all read words, case-insensitive.

# The input to the program in the first line is the number
# n - the total number of words. Next come n lines with words.