from random import randrange

n = int(input())
password = ''

for i in range(n):
    num = randrange(2)
    if num == 0:
        password += chr(randrange(65, 91))
    else:
        password += chr(randrange(97, 123))

print(password)

# The program generates a random password using the random module.
# The program takes the length of the password as input and outputs a random password
# containing only English characters a..z, A..Z (in lower and upper case).