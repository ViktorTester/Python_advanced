s = input()
counter = 0
arr = []

if 'T' in s:
    for i in range(len(s)):
        if s[i] == 'T':
            counter += 1
            arr.append(counter)
        else:
            counter = 0
    print(max(arr))
else:
    print(0)

# A string, consisting of letters of the english alphabet "H" and "T" is given.
# The letter "H" - means Heads, and the letter "T" - mean Tails.
# The program counts the largest number of Tails in a row.