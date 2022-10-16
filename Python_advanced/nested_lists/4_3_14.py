def list_sublists():
    s = input().split()
    arr, total = [], [[]]

    for i in range(len(s)):
        for j in range(len(s)):
            arr = s[j:i + j + 1]
            if len(arr) == i + 1:
                total.append(arr)

    print(total)


list_sublists()

# The input to the program is a string of text containing characters.
# A list is formed from this string. A program that prints out a list containing
# all possible sublists of the list, including the empty list.
