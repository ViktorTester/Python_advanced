with open('ledger.txt', encoding='utf-8') as file:
    text = [line.strip() for line in file.readlines()]

    total = 0
    for i in text:
        total += int(i[1:])

    print('$' + str(total))

# There is a ledger.txt text file with data on the company's
# sales per month. Each file of the file indicates how much the
# client paid for the goods, in dollars (an integer number):

# $ 47
# $ 100
# $ 60
# $ 12
# $ 8
# ...

# The program calculates the total monthly revenue of the company.
