from decimal import *

num = Decimal(input())

answer = num.exp() + num.ln() + num.log10() + num.sqrt()

print(answer)

# The input to the program is a Decimal number d. The program calculates the value of the expression:
# e ** d + ln(d) + lg(d) + sqrt(d)
