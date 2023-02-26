from random import randint

random_numbers = [str(randint(111, 777)) + '\n' for _ in range(25)]

with open('random.txt', 'w', encoding='utf-8') as file:
    file.writelines(random_numbers)

# The program writes 25 random numbers in the range from 111 to 777 (inclusive)
# to the random.txt text file, each on a new line.