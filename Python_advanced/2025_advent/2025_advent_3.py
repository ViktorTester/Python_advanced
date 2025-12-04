with open("test.txt", "r", encoding="utf-8") as f:
    arr = [line.strip() for line in f]

total = 0

for i in arr:
    digits = list(map(int, i))

    best_left = digits[0]
    best_pair = 0

    for x in range(1, len(digits)):
        best_pair = max(best_pair, best_left * 10 + digits[x])

        if digits[x] > best_left:
            best_left = digits[x]

    total += best_pair

print(total)