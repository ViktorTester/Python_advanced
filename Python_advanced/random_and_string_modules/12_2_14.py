from string import ascii_letters, digits, ascii_uppercase, ascii_lowercase
from random import choice

count, length = int(input()), int(input())
arr = [i for i in (ascii_letters + digits) if i not in 'lI1oO0']

letters = {'EN': [x for x in ascii_uppercase if x not in 'OI'],
           'en': [x for x in ascii_lowercase if x not in 'ol'],
           'dig': [x for x in digits if x not in '01']}


def generate_password(length):
    password = ''

    for value in letters.values():
        password += choice(value)

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

# Each password must contain at least one number and at least one letter in upper and lower case.