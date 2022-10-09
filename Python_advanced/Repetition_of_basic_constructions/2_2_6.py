def product_of_numbers():
    n = int(input())
    arr = []

    for i in range(n):
        a = int(input())
        arr.append(a)

    b = int(input())

    for j in range(len(arr)):
        for g in range(len(arr)):
            if j != g:
                if arr[j] * arr[g] == b:
                    return "YES"
    return "NO"


print(product_of_numbers())

# The program determines whether a number is a product of two numbers from a given set.

# The first line contains the number n - the number of numbers in the set.
# The next n lines contain the integers that make up the set (can be repeated).
# Then comes an integer that is or is not the product of any two numbers from the set.