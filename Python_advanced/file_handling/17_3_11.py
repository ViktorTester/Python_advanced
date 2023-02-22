with open('nums.txt', 'r', encoding='utf-8') as file:
    text = [line.strip() for line in file.read()]

    s = ''
    total = 0
    for i in range(len(text)):
        if text[i].isdigit():
            s += text[i]
        else:
            s += ' '

    arr = s.split()

    for j in range(len(arr)):
        total += int(arr[j])

    print(total)

# In the nums.txt file, non-negative integers and anything else can be written.
# A number is a sequence of one or more consecutive digits (number is always non-negative).
# The program calculates the sum of all numbers written in the file.