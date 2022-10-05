s = input()
x = str(len(s) * 60)
z = (x[:2] + '.' + x[2:])

if z[-1] == '0' and z[-2] == "0":
    z = (x[:2] + '.' + x[3:])
    print(z.replace('.', ' р. ') + ' cents')
elif len(s) == 1:
    print("0 dollars. 60 cents")
else:
    print(z.replace('.', 'dollars ') + ' cents')

# or

s = input()
x = 60 * len(s)

print(f'{x // 100} dollars {x % 100} cents')

# A string of text is given. The program calculates the cost of a line based
# on the fact that every one character (including space) costs 60 cents.
