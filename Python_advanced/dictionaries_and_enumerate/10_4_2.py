a, b = list(input()).strip('.,!?:;-'), list(input())
res1, res2 = {}, {}

for x in a:
    res1[x] = res1.get(x, 0) + 1

for y in b:
    res2[y] = res2.get(y, 0) + 1

if res1 == res2:
    print("YES")
else:
    print("NO")

# An anagram is a word (phrase) formed by rearranging the letters that make up
# another word (or phrase). For example, the English words evil and live are anagrams.

# The input to the program is two words. The program determines if they are anagrams.