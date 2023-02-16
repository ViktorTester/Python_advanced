numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
result = filter(lambda x: str(x) != str(x)[::-1], numbers)
print(*result)

# The code removes all palindrome numbers from the list and
# prints the result on one line separated by a space.