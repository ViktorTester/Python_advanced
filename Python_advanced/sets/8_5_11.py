n = int(input())
arr = []

for i in range(n):
    arr.append(input().lower())

for j in range(len(arr)):
    print(len(set(arr[j])))

# A program displays the number of unique characters of each read word, case-insensitive.

# The input to the program in the first line is the number
# n - the total number of words. Next come n lines with words.