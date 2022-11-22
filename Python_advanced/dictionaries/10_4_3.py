a, b = list(input().lower()), list(input().lower())
res1, res2 = {}, {}

arr1 = [a[i] for i in range(len(a)) if a[i].isalpha()]
arr2 = [b[j] for j in range(len(b)) if b[j].isalpha()]

for x in arr1:
    res1[x] = res1.get(x, 0) + 1

for y in arr2:
    res2[y] = res2.get(y, 0) + 1

if res1 == res2:
    print("YES")
else:
    print("NO")

# Two proposals are submitted to the input of the program.
# The program determines whether they are anagrams or not.
# The program ignores case, punctuation and spaces.