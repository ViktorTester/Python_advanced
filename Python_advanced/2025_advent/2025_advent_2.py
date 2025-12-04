with open("test.txt", "r", encoding="utf-8") as f:
    data = f.read().strip()

arr = [item.strip() for item in data.split(",") if item.strip()]

total = 0


def badCondition(number):

    if len(number) % 2 == 0:
        half = int(len(number) / 2)
        if number[0:half] == number[half::]:
            return number


for i in arr:
    s = i.split("-")
    num = int(s[0])

    while num != int(s[1]) + 1:
        result = badCondition(str(num))
        if result:
            total += int(result)
        num += 1


print(total)
