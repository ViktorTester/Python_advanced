a = int(input())
s = list(str(a))
arr = []

if len(str(a)) <= 3:
    print(a)
else:
    s.reverse()
    counter = 0
    for i in range(len(s)):
        arr.append(s[i])
        counter += 1
        if counter % 3 == 0:
            arr.append(',')
            counter = 0
    arr.reverse()
    if arr[0] == ',':
        arr.pop(0)

print(''.join(arr))

# The input to the program is a natural number. The program inserts commas into
# the given number in accordance with the standard American convention for commas in large numbers.
