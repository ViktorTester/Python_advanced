from random import randint

arr = []

while len(arr) < 100:
    num = randint(1000000, 9999999)
    if num not in arr:
        arr.append(num)
        print(num)
    else:
        continue

# The program generates 100 random numbers of lottery tickets using the random
# module and displays them each on a separate line. The following conditions apply:

# the number cannot start with zeros;
# the lottery ticket number must be 7 digits long;
# all 100 lottery tickets must be different.