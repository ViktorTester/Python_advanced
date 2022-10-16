def duplicate_packing(s):
    arr = []
    arr2 = []

    for i in range(len(s)):
        if not arr2:
            arr2.append(s[i])
        elif arr2:
            if arr2[-1] == s[i]:
                arr2.append(s[i])
            elif arr2[-1] != s[i]:
                arr.append(arr2)
                arr2 = [s[i]]

    if arr2:
        arr.append(arr2)
    print(arr)


s = input().split()
duplicate_packing(s)

# The input to the program is a string of text containing characters.
# The program packs sequences of identical characters of the given string into sublists.
