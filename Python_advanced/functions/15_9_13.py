n = list(input())

result = all(
    [any(map(lambda x: x.isdigit(), n)),
     any(map(lambda x: x.islower(), n)),
     any(map(lambda x: x.isupper(), n)),
     len(n) >= 7]
)

if result:
    print('YES')
else:
    print('NO')

# A good password is at least 7 characters long, contains at least one number,
# an uppercase letter, and a lowercase letter. The program determines if the entered password is good.