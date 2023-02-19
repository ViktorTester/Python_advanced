s = open('prices.txt', 'r', encoding='utf-8')

text = [line.strip().split('\t') for line in s.readlines()]
arr = [int(i[1]) * int(i[2]) for i in text]

print(sum(arr))

s.close()

# In the prices.txt file, each line is divided into three columns using a tab character (\t):

# name of product;
# quantity of goods (integer);
# product price for 1 piece (integer).
# The program displays the total cost of the order.