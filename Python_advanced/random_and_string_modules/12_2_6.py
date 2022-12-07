from random import randrange


def generate_ip():
    ip = ''
    for i in range(4):
        num = randrange(0, 256)
        ip += str(num) + '.'
    return ip[:-1]


correct_ip = generate_ip()

print(correct_ip)

# The IP address consists of four numbers from the range from 0 to 255 (inclusive) separated by a dot.

# The generate_ip() function, using the random module, generates and returns a random, valid IP address.
