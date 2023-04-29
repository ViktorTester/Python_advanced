text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

text = list(text)
result = {}
for x in text:
    result[x] = result.get(x, 0) + 1

print(result)

# The program creates a dictionary in which the number of
# occurrences of each character in the string text is counted.