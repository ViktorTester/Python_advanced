a = int(input())
a = str(a)
b = ''

if a[-1] == '0' and len(a) == 5:
    for i in range(len(a)):
        if a[i] == '0':
            continue
        else:
            b += a[i]
    print(b[::-1])
else:
    if len(a) == 5:
        print(str(a)[::-1])
    else:
        print(str(a)[0] + (str(a)[1:][::-1]))

# Given a five-digit or six-digit natural number. The program reverses the order
# of its last five digits. The number is displayed without leading zeros.