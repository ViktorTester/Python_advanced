ip_address = input().split('.')

result = all(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, ip_address))

print(result)

# The program checks if the entered IP address is correct.