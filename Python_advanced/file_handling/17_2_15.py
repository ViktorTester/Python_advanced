s = open('nums.txt', 'r', encoding='utf-8')

text = s.read().split()

text2 = [int(line) for line in text]

print(sum(text2))

s.close()

# The nums.txt file contains two integers, they can be separated by space and
# end-of-line characters. The program displays the sum of these numbers.