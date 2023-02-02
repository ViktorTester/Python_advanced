func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False

print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))

# Using anonymous function syntax, I wrote a 'func' function that takes an integer
# argument and returns True if it's divisible by 19 or 13 and False otherwise.