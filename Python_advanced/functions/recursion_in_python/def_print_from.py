def print_from(n: int):
    """recursion function"""
    if n > 0:
        print(n)
        print_from(n - 1)

print_from(int(input()))

# The print_from function takes one natural number 'n' and prints on the screen
# a descending sequence of integers from n to 1 inclusive.