a, b = int(input()), int(input())

numbers = [i for i in range(a, b + 1)]

result = filter(lambda x: '0' not in str(x), numbers)

answer = [j for j in result if all(map(lambda y: j % int(y) == 0, str(j)))]

print(*answer)

# The input to the program is two natural numbers a and b. The program detects all
# integers in the range [a; b], which are divided by each
# digit contained in them without a remainder.
