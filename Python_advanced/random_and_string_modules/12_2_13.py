from string import ascii_letters, digits
from random import choice

count, length = int(input()), int(input())
arr = [i for i in (ascii_letters + digits) if i not in 'lI1oO0']


def generate_password(length):
    password = ''
    while len(password) < length:
        password += choice(arr)
    return password


def generate_passwords(count, length):
    pas = [generate_password(length) for _ in range(count)]
    return pas


passwords = generate_passwords(count, length)
print(*passwords, sep='\n')

# Using the random module, the program generates n passwords of length m characters,
# consisting of lowercase and uppercase English letters and numbers,
# except for those that are easy to confuse with each other:

# "l" (L is small);
# "I" (i is large);
# "1" (number);
# "o" and "O" (capital and small letters);
# "0" (digit).
