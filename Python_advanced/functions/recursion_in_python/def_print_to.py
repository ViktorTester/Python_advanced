def print_to(n: int):
    """recursion function"""
    if n > 0:
        print_to(n - 1)
        print(n)

print_to(int(input()))

# # The print_to function takes one natural number 'n' and prints on the screen
# # an increasing sequence of integers from n to 1 inclusive.