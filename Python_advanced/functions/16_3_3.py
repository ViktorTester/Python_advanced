words = 'the world is mine take a look what you have started'.split()
result = map(lambda x: '"' + x + '"', words)
print(*result)

# The code wraps all the elements of the 'words' list in double quotes,
# and then prints the result on a single space-separated line.
