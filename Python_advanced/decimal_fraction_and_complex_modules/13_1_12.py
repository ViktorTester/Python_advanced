from decimal import *

num = Decimal(input())
num_tuple = num.as_tuple()

num = int(num)

maximum = max(num_tuple.digits)
minimum = min(num_tuple.digits)

if num != 0:
    print(maximum + minimum)
else:
    print(maximum)

# The input is a Decimal number, the program outputs
# the sum of the largest and smallest digits of the Decimal number.