with open("test.txt", "r", encoding="utf-8") as f:
    data = f.read().strip()

arr = [item.strip() for item in data.split(",") if item.strip()]

total = 0


def badCondition(number):
    n = len(number)

    for j in range(1, n // 2 + 1):
        if n % j == 0:
            times = n // j
            if number[:j] * times == number:
                return number


for i in arr:
    s = i.split("-")
    start = int(s[0])
    end = int(s[1])

    for num in range(start, end + 1):
        result = badCondition(str(num))
        if result:
            total += int(result)

print(total)
