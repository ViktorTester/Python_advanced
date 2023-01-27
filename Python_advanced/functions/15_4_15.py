numbers = input().split()


def digitsSum(digit):
    total = 0
    for i in range(len(digit)):
        total += int(digit[i])
    return total


print(*(sorted(numbers, key=digitsSum)))

# The input to the program is a string of natural numbers.
# A list of numbers is formed from the elements of the string.

# The program sorts a list of numbers in ascending order of the sum of their digits.
# In this case, if two numbers have the same sum of digits,
# their relative position in the initial list is preserved.
